#!/usr/bin/env python3
"""Generate recent public signal files for council voices.

This script is intentionally conservative:
- It only writes generated files under signals/.
- It treats automated signals as supporting context, not canonical worldview.
- It does not rewrite the hand-authored voice profiles.
"""

from __future__ import annotations

import argparse
import datetime as dt
import email.utils
import json
import pathlib
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ROOT = pathlib.Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "voice_watchlist.json"
SIGNALS_DIR = ROOT / "signals" / "recent"
SUMMARY_PATH = ROOT / "signals" / "summary.md"
USER_AGENT = "ai-council-refresh/1.0 (+https://github.com/napiermd/ai-council)"


def fetch_text(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_google_news(query: str) -> list[dict]:
    encoded = urllib.parse.quote(f"{query} when:30d")
    url = f"https://news.google.com/rss/search?q={encoded}&hl=en-US&gl=US&ceid=US:en"
    xml_text = fetch_text(url)
    root = ET.fromstring(xml_text)
    items = []
    for item in root.findall("./channel/item"):
        title = text_of(item.find("title"))
        link = text_of(item.find("link"))
        pub_raw = text_of(item.find("pubDate"))
        published = parse_date(pub_raw)
        source = None
        source_node = item.find("source")
        if source_node is not None:
            source = (source_node.text or "").strip()
        items.append(
            {
                "title": title,
                "url": link,
                "published": published,
                "source": source or "Google News",
                "kind": "news",
            }
        )
    return items


def parse_github_user_events(user: str) -> list[dict]:
    url = f"https://api.github.com/users/{user}/events/public"
    payload = fetch_text(url)
    data = json.loads(payload)
    items = []
    for event in data:
        created_at = parse_iso_date(event.get("created_at"))
        repo_name = (event.get("repo") or {}).get("name", "")
        event_type = event.get("type", "Event")
        title = f"{event_type} in {repo_name}" if repo_name else event_type
        repo_url = f"https://github.com/{repo_name}" if repo_name else f"https://github.com/{user}"
        items.append(
            {
                "title": title,
                "url": repo_url,
                "published": created_at,
                "source": "GitHub",
                "kind": "github",
            }
        )
    return items


def text_of(node: ET.Element | None) -> str:
    return (node.text or "").strip() if node is not None else ""


def parse_date(value: str) -> dt.datetime | None:
    if not value:
        return None
    try:
        parsed = email.utils.parsedate_to_datetime(value)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=dt.timezone.utc)
        return parsed.astimezone(dt.timezone.utc)
    except Exception:
        return None


def parse_iso_date(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(dt.timezone.utc)
    except Exception:
        return None


def reviewed_date(profile_path: pathlib.Path) -> dt.date | None:
    text = profile_path.read_text()
    match = re.search(r"Reviewed:\s*(\d{4}-\d{2}-\d{2})", text)
    if not match:
        return None
    return dt.date.fromisoformat(match.group(1))


def render_voice(voice: dict, items: list[dict], errors: list[str], today: dt.date, window_days: int) -> str:
    header = [
        f"# Recent Signals: {voice['name']}",
        "",
        f"- Generated: {today.isoformat()}",
        f"- Window: last {window_days} days",
        f"- Profile: [{voice['profile_path']}](../../{voice['profile_path']})",
        "",
        "Treat this file as recent public context, not as the canonical statement of the voice.",
        "",
    ]

    if items:
        header.extend(["## Recent public signals", ""])
        for item in items[:8]:
            pub = item["published"].date().isoformat() if item["published"] else "undated"
            header.append(f"- {pub} | {item['source']} | [{item['title']}]({item['url']})")
        header.append("")
    else:
        header.extend(["## Recent public signals", "", "- No recent automated signals captured in this window.", ""])

    header.extend(["## Manual watch sources", ""])
    for source in voice.get("manual_watch", []):
        header.append(f"- [{source['label']}]({source['url']})")
    header.append("")

    if errors:
        header.extend(["## Refresh notes", ""])
        for error in errors:
            header.append(f"- {error}")
        header.append("")

    return "\n".join(header) + "\n"


def render_summary(rows: list[dict], today: dt.date, window_days: int) -> str:
    lines = [
        "# Recent Signals Summary",
        "",
        f"- Generated: {today.isoformat()}",
        f"- Window: last {window_days} days",
        "",
        "| Voice | Recent items | Reviewed | Output |",
        "| --- | ---: | --- | --- |",
    ]
    for row in rows:
        reviewed = row["reviewed"].isoformat() if row["reviewed"] else "missing"
        output_path = f"recent/{row['id']}.md"
        lines.append(f"| {row['name']} | {row['count']} | {reviewed} | [{output_path}]({output_path}) |")
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Automated signals are a recency layer, not a substitute for the hand-authored profiles.",
            "- Use these files when the question depends on what a voice appears to be emphasizing now.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--window-days", type=int, default=None)
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text())
    window_days = args.window_days or manifest.get("window_days", 30)
    today = dt.datetime.now(dt.timezone.utc).date()
    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=window_days)

    SIGNALS_DIR.mkdir(parents=True, exist_ok=True)

    summary_rows = []
    for voice in manifest["voices"]:
        all_items = []
        errors = []
        for source in voice.get("sources", []):
            try:
                if source["type"] == "google_news":
                    items = parse_google_news(source["query"])
                elif source["type"] == "github_user_events":
                    items = parse_github_user_events(source["user"])
                else:
                    errors.append(f"Unsupported source type: {source['type']}")
                    continue
                for item in items:
                    if item["published"] and item["published"] >= cutoff:
                        all_items.append(item)
            except Exception as exc:
                errors.append(f"{source['label']}: {exc}")

        all_items.sort(key=lambda item: item["published"] or dt.datetime(1970, 1, 1, tzinfo=dt.timezone.utc), reverse=True)
        out = render_voice(voice, all_items, errors, today, window_days)
        out_path = SIGNALS_DIR / f"{voice['id']}.md"
        out_path.write_text(out)

        summary_rows.append(
            {
                "id": voice["id"],
                "name": voice["name"],
                "count": len(all_items),
                "reviewed": reviewed_date(ROOT / voice["profile_path"]),
            }
        )

    summary_rows.sort(key=lambda row: row["name"].lower())
    SUMMARY_PATH.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_PATH.write_text(render_summary(summary_rows, today, window_days))
    return 0


if __name__ == "__main__":
    sys.exit(main())
