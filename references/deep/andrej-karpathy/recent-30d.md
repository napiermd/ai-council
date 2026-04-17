# Recent Signals (Last 30 Days): Andrej Karpathy

> Auto-refreshable 30-day signal window. Re-run `last30days` skill to
> regenerate.

---

## Last refresh

- **Date:** 2026-04-17
- **Window:** 2026-03-18 → 2026-04-17
- **Sources returned:** X (11 posts via @karpathy handle + keyword),
  YouTube (18 videos, 8 with transcripts), Reddit (0 — Codex fallback
  bug, see Shah's `recent-30d.md` for details), HN (0), Bluesky (403).
- **Status:** Rich return compared to Shah's low-X voice. Karpathy is
  heavy X — the skill worked well here. **The tool works for voices
  whose primary channel is X; it under-reports voices whose primary
  channel is LinkedIn.**

---

## Signal themes in the window

### 1. LLM-as-brain-upload discussion (April 9-10, 2026)

Karpathy posted an extended thread on AI capability-understanding gap
and brain-uploading as a framing:

**X April 9, 2026 (score 70, 19,966 likes, 2,415 reposts):**
> "Judging by my tl there is a growing gap in understanding of AI
> capability. The first issue I think is around recency and tier of
> use. I think a lot of people tried the free tier of ChatGPT somewhere
> [...]"

**X April 10, 2026 (score 64):**
> "Yes it's the tractable form of brain upload. There's a ton of scifi
> on brain uploads that requires way too exotic tech (scanning and
> simulating brains etc), when we're about to get a lossy and
> approximate [version]."

**X April 10, 2026 (score 52):**
> "These neuroscience adjacent ideas are exotic armchair philosophy
> when the LLM simulation path will work really well and so much faster
> and it's not even remotely a contest."

**X April 10, 2026 (score 52, describing the hypothetical upload company):**
> "No the company physically gets you to come in, sits you down and
> asks you a precise set of maximally informative questions specifically
> designed for the best upload fidelity."

### 2. OpenClaw / Steinberger praise (April 9, 2026)

**X April 9, 2026 (score 63, 3,546 likes):**
> "Someone recently suggested to me that the reason OpenClaw moment was
> so big is because it's the first time a large group of non-technical
> people (who otherwise only knew AI as synonymous with ChatGPT [...]"

(This is Karpathy endorsing Steinberger's OpenClaw framing as the first
real AI moment for non-technical users.)

### 3. PDF-converter frustration (April 9, 2026)

**X (score 60):**
> "I just tried it this morning on the 245-page Mythos pdf and it failed
> badly and the outputs were all mangled. Converting pdfs is really
> hard, I think it has to probably be a Skill not a program."

**X (score 52):**
> "In my experience there are approximately one thousand different pdf
> converters that are all equally terrible for anything except the
> simplest documents."

### 4. Personal wikipedia / knowledge base pattern (April 4-6, 2026)

**X April 4, 2026 (score 63, 8,747 likes, 790 reposts):**
> "Farzapedia, personal wikipedia of Farza, good example following my
> Wiki LLM tweet. I really like this approach to personalization in a
> number of ways, compared to 'status quo' of an AI that allegedly
> [...]"

**X April 6, 2026 (score 57):**
> "The core idea is that this lets you skip writing but it doesn't let
> you skip reading and thinking. And the surprising result is that this
> works. Personally I process most of what I file by reading it."

Position: LLM-maintained personal knowledge bases > RAG. A large
fraction of his recent token budget goes here.

### 5. Wistful reply about OpenAI product direction (April 10, 2026)

**X (score 60, 1,352 likes):**
> "Yeah exactly. It's such a cool concept for a product. It doesn't
> seem like oai will continue pushing the direction, (which makes
> sense) but I hope a startup can clone it and actually give it care
> [...]"

(Reply about an OpenAI product he likes that he doesn't expect OpenAI
to keep pushing.)

---

## YouTube signal — No Priors March 2026 episode

Top-ranked YouTube result in the window:

**"Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the
Loopy Era of AI"** — No Priors, March 20, 2026.
- 712,108 views; 13,868 likes
- URL: https://www.youtube.com/watch?v=kwSVtQ7dziU

Transcripts pulled. Core content transcribed and surfaced in
`voice.md`, `frameworks.md`, and `positions.md` (auto-research, claws,
Dobby-the-elf, skill issue, macro-actions, token throughput).

---

## What the window did NOT surface

- New peer-reviewed papers (consistent with his post-2017 publishing
  pattern).
- LinkedIn posts — he is much lighter on LinkedIn than Shah, Howard, or
  Huyen. X is his primary channel.
- Commencement addresses / TEDx — consistent with his talk pattern;
  he doesn't do these formats.
- Eureka Labs product launches — quiet in this window.

---

## How to refresh this file

```bash
python3 /Users/andrewn/.claude/skills/last30days/scripts/last30days.py \
  "Andrej Karpathy AI LLM training Eureka Labs" \
  --emit=compact \
  --no-native-web \
  --save-dir=~/Documents/Last30Days \
  --x-handle=karpathy \
  --deep
```

Supplement with direct WebFetch on:
- https://karpathy.bearblog.dev (new bearblog essays)
- https://github.com/karpathy (new repos)
- https://eurekalabs.ai (product launches)

---

## Last reviewed

- Reviewed: 2026-04-17
- Refresh cadence: every 30 days recommended; he's high-signal on X
  and the skill returns rich data for him.
