# Recent Signals (Last 30 Days): Nigam Shah

> Auto-refreshable window of his public activity. Re-run the
> `last30days` skill to regenerate.

---

## Last refresh

- **Date:** 2026-04-17 (initial pass + handle correction)
- **Window:** 2026-03-18 → 2026-04-17
- **Handle correction:** Initial pass used wrong handle `@NigamShah`.
  Actual handle is **`@drnigam`** — https://x.com/drnigam.
- **Sources queried:** Reddit, X (via @drnigam handle + keyword
  search), YouTube, Hacker News, Bluesky (failed 403), web
- **Status:** **Sparse / effectively empty.** Re-run with corrected
  handle returned 0 X posts (Bird search errored out entirely). Initial
  pass with wrong handle returned 2 X posts from @AtroposHealth (not
  Shah directly). Either way, last30days is not yielding live Shah
  signal in this window.

## Why the results were sparse — diagnosis

Three separate problems, two of them fixable:

1. **Shah is LinkedIn-first, not X-first.** His LinkedIn (`/in/nigam`) is
   his primary long-form channel. `last30days` does **not** support
   LinkedIn. For any clinical-AI or academic voice where LinkedIn is the
   main channel, this skill will under-report.
2. **Reddit search failed on the Codex fallback chain.** The script
   attempted `gpt-5.1-codex-mini` first (400 error — not supported on
   this Codex account), fell back, and the fallback returned a response
   object with an empty `output` array ("No output text found in OpenAI
   response"). This is a silent failure mode in
   `scripts/lib/openai_reddit.py` lines 288-356. When it happens, Reddit
   returns 0 threads across the board, regardless of topic.
3. **Bluesky returned HTTP 403.** Even though the `--diagnose` check
   reports `bluesky: true`, the actual API call 403'd during the
   research pass. Likely an expired session or token scope issue.

### What this means for future voices

- **Heavy X/Reddit voices (Karpathy, Willison, Steinberger, Howard):**
  the skill will return meaningful results. Use it as primary recency
  layer.
- **LinkedIn-primary voices (Shah, Chen, Bitterman, some of Liang):**
  the skill is a weak signal. Supplement with direct fetch of LinkedIn
  profile + Stanford/NEJM archive search.
- **Mixed voices (Huyen, Kiela):** use `last30days` + WebFetch in
  parallel.

### Immediate workarounds

- For Shah specifically: the 90-day deep research pass (via multi-agent
  research + direct WebFetch) produced richer material than the 30-day
  signals window. That approach is the one that actually worked.
- To check Bluesky state, see env vars `BSKY_HANDLE` and
  `BSKY_APP_PASSWORD`. Re-authenticate at
  `bsky.app/settings/app-passwords` if stale.
- To work around the Reddit Codex fallback bug, consider setting a
  direct `OPENAI_API_KEY` env var so the skill uses the Standard API
  key path (lines 322-356) instead of the Codex auth path (lines
  301-320). The Standard API path has a different fallback chain that
  is less brittle.

---

## Confirmed recent items

### Atropos Health media amplification (April 2026)

**@AtroposHealth** — X post, 2026-04-08 (his co-founded company
amplifying CEO Brigham Hyde):

> "#AtroposHealth CEO and Co-Founder Dr. @BrighamHyde shares in
> @DigitalITNews1 how an evidence-on-demand approach helps clinicians
> and researchers make faster, smarter, data-driven decisions."

https://x.com/AtroposHealth/status/2041887777025888713

**@AtroposHealth** — X post, 2026-04-06:

> "Is the AI selloff in CRO stocks missing the point? #AtroposHealth
> CEO & Co-Founder Dr. @BrighamHyde shares his perspective in
> @Reuters: AI can augment clinical trials, but human coordination
> remains..."

https://x.com/AtroposHealth/status/2041185447536148585

**Relevance to Shah:** These are from the company he co-founded, not
direct Shah posts. But they signal the company's positioning
(evidence-on-demand, CRO augmentation, clinical trial workflow) —
which is Shah's Green Button thesis in commercial form.

---

## What the last30days pass did NOT surface

- No direct X posts from @drnigam in the 30-day window were returned
  by the research script. (Likely means either low posting frequency in
  the window or a platform-auth issue with the search. LinkedIn is his
  higher-yield channel; LinkedIn search was not part of the script.)
- No new podcast appearances in the window.
- No new major press interviews.
- No new preprints attributed to Shah in the window.

---

## Known-recent context (backfilled from 90-day research)

Not strictly "last 30 days" but current and load-bearing:

- **MedHELM** (Nature Medicine 2026, published earlier in 2026).
- **DistilINFO interview (March 31, 2026)** — Shah's point on MedHELM's
  single-response limit.
- **PMWC 2026 Luminary Award and speaking slot** (March 2026).
- **TechCrunch interview (Jan 13, 2026)** — provider-side-first position.
- **Stanford Report 2026 predictions** (Dec 2025).
- **Catalyzing Health AI by Fixing Payment Systems** (NEJM AI, Nov 2025).
- **CHAI regulatory-cartel controversy** — active since October 2025,
  ongoing.

---

## How to refresh this file

Run from the repo root:

```bash
# Via the last30days skill
python3 /Users/andrewn/.claude/skills/last30days/scripts/last30days.py \
  "Nigam Shah Stanford health AI clinical AI CHAI Atropos Health" \
  --emit=compact \
  --no-native-web \
  --save-dir=~/Documents/Last30Days \
  --x-handle=drnigam
```

Then manually cross-check:
- https://www.linkedin.com/in/nigam (primary channel)
- https://x.com/drnigam
- https://news.stanford.edu (search "Nigam Shah")
- https://ai.nejm.org (new editorial-board activity)
- https://chai.org (policy statements)

---

## What to look for specifically

1. **New LinkedIn long-form posts** — issue-driven, 2–6 paragraphs, his
   richest voice-sampling channel.
2. **CHAI developments** — assurance labs status, political conflict
   with HHS/FDA, new framework announcements.
3. **New Stanford Health Care deployments** — ChatEHR user/session
   growth, new production models.
4. **Atropos Health milestones** — customer announcements, funding,
   product launches.
5. **New Nature Medicine / NEJM AI commentary** — he's on the NEJM AI
   editorial board, so new editorials likely.
6. **Any public response to the RFK Jr. / Makary CHAI critique** — his
   tone here is diagnostic of his 2026 posture.

---

## Last reviewed

- Reviewed: 2026-04-17
- Refresh cadence: every 30 days recommended.
