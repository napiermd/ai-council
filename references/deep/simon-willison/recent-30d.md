# Recent Signals (Last 30 Days): Simon Willison

> Auto-refreshable 30-day window. Re-run `last30days` to regenerate.

---

## Last refresh

- **Date:** 2026-04-17
- **Window:** 2026-03-18 → 2026-04-17
- **Sources returned:** X (40 posts, 23 from @simonw directly), YouTube
  (16 videos, 8 transcripts), Reddit (0 — Codex bug), HN (0), Bluesky
  (403).
- **Status:** **Rich return.** Willison is high-volume on X (40 posts
  vs. Shah's 2, Huyen's 9, Karpathy's 11). The last30days skill works
  well for him.

---

## Headline event in the window

### Qwen3.6-35B-A3B beats Claude Opus 4.7 on his pelican benchmark
— April 16-17, 2026

**X, April 16, 2026 (2,235 likes, 138 reposts):**
> "Shocking result on my pelican benchmark this morning, I got a
> better pelican from a 21GB local Qwen3.6-35B-A3B running on my
> laptop than I did from the new Opus 4.7!"

**Follow-up, same day:**
> "Here's Qwen 3.6-35B-A3B vs. Claude Opus 4.7 for 'Generate an SVG
> of a flamingo riding a unicycle', in case you thought Qwen might be
> cheating at the pelican benchmark"

**Clarifying a confused reader (April 17):**
> "That's a different test, ChatGPT has an image generation tool — my
> pelican test is about having text output models generate SVG code"

**Hardware note:**
> "128GB M5, but this 21GB model should run OK on a 32GB machine"

### Full blog post
> "Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude
> Opus 4.7"
> URL: https://simonwillison.net/2026/Apr/16/qwen-beats-opus/

> "I'm giving this one to Qwen 3.6. Opus managed to mess up the
> bicycle frame!"

> "I don't think they do, but honestly this result did give me a
> little glint of suspicion." (on whether labs might be training on
> his benchmark)

> "If the thing you need is an SVG illustration of a pelican riding a
> bicycle though, right now Qwen3.6-35B-A3B running on a laptop is a
> better bet than Opus 4.7!"

Backup test: **flamingo on a unicycle** — his private control to
verify the pelican hasn't leaked into training data.

---

## Coding-agents-for-maintenance thesis (April 17, 2026)

**X:**
> "Is there still a widespread belief that LLMs and coding agents are
> good for greenfield development but don't help for maintaining large
> existing codebases? I don't think that idea holds up any more..."

This is him updating his position publicly. In 2024 he was more
cautious about AI-assisted maintenance; by April 2026 he's shifted.

---

## Other signals in the window

### Continued pelican / local-model posts
He was posting heavily about local Qwen vs. cloud comparisons and the
"playing the long game" to trick labs into over-investing in the
pelican benchmark.

### Secondary figures he's boosting
His X retweets / amplifications in this window included:
- @airiaiai8 (AI security content)
- @gustavosalami
- @gracker_gao

These are the sub-10K-follower researchers he's known for amplifying.

### YouTube in the window
Four videos ranked (of 16 found), including:
- His No Priors or Latent Space adjacent content
- A "Coding Agents" tutorial

---

## Thematic summary of the 30-day window

1. **Local models keep closing the gap.** He is clearly impressed with
   Qwen3.6-35B-A3B.
2. **He's shifting his position on AI-assisted maintenance** — now
   thinks coding agents do help large existing codebases, not just
   greenfield.
3. **The pelican benchmark keeps revealing surprises.** Expected
   outcome (bigger cloud model wins) did not hold in this case.
4. **He continues to clarify misinterpretations of his benchmark** —
   pelican = text→SVG, not image generation.
5. **No major new coinage or framework in this window.**

---

## What the window did NOT surface

- No new annual review (the 2025 year-in-review was published Dec 31,
  2025).
- No new blog-named coinage in Mar-Apr 2026.
- No major agent security post (his last one was Nov 2025).
- No Bluesky or Reddit data (skill failures).
- No new `llm` CLI major release.

---

## How to refresh this file

```bash
python3 /Users/andrewn/.claude/skills/last30days/scripts/last30days.py \
  "Simon Willison LLMs CLI prompt injection" \
  --emit=compact \
  --no-native-web \
  --save-dir=~/Documents/Last30Days \
  --x-handle=simonw \
  --deep
```

Supplement with direct WebFetch on:
- https://simonwillison.net (always)
- https://simonwillison.net/atom/entries/ (RSS)
- https://til.simonwillison.net
- https://github.com/simonw (new repos)
- https://tools.simonwillison.net (new vibe-coded tools)

---

## What to look for on the next refresh

1. **New coinages** — he names 1-3 things per year on average.
2. **Annual review** — Dec 31 every year.
3. **New model release reactions** — he reacts same-day.
4. **Pelican benchmark updates** — he runs it on every new frontier
   release.
5. **New `llm` CLI plugins** — he ships these constantly.
6. **Security posts** — new prompt injection exploits surface
   regularly.
7. **tools.simonwillison.net** — the vibe-coded tool count keeps
   climbing.
8. **Podcast appearances** — he does ~1-2 major podcasts per month.

---

## Last reviewed

- Reviewed: 2026-04-17
- Refresh cadence: every 14-30 days — he's high-signal on X and the
  skill returns rich data for him.
