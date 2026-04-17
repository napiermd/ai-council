# Recent Signals (Last 30 Days): Chip Huyen

> Auto-refreshable 30-day signal window. Re-run `last30days` skill to
> regenerate.

---

## Last refresh

- **Date:** 2026-04-17
- **Window:** 2026-03-18 → 2026-04-17
- **Sources returned:** X (9 posts via @chipro handle + keyword
  search), YouTube (40 videos, 8 transcripts — 29 ranked), Reddit (0,
  Codex bug), HN (0), Bluesky (403).
- **Status:** Mixed return. Signal mostly from **OTHER PEOPLE
  recommending her books**, not from Chip herself posting. She is lower
  X volume than Karpathy and higher than Shah. LinkedIn (315K
  followers) is her higher-yield channel.

---

## Signal themes in the window

### 1. Her books as canonical recommendations (April 2026)

Her two books appear in most "books every AI engineer should read"
lists this month:

**@itsjasonai** (X, April 16, 2026):
> "2. AI Engineering: Building Applications by Chip Huyen — If you're
> building anything with LLMs today, this is the one. Chip ran ML at
> major companies. The book reads like a working engineer's manual..."

**@gosneyphoto** (X, April 14, 2026):
> "3/5 @rasbt (Sebastian Raschka) & @chipro (Chip Huyen) — Practical
> ML engineering. Books like 'Build a LLM from Scratch' and 'Designing
> Machine Learning Systems.' Ship real AI, not just notebooks."

**@EcZachly** (X, April 12, 2026, 1076 likes):
> "You only need to read four books to truly get what's going on in ML
> and data engineering: — Fundamentals of Data Engineering by Joe Reis
> — Designing Data Intensive Applications by Martin Kleppmann..."
(includes Chip's work)

**@kurisgreen** (Portuguese, April 5, 2026):
> "Chip Huyen é mt foda, ela não contente em lançar uma das maiores
> referencias pra ML Engineering, lançou outra pra AI Engineering hehe"
(*"Chip Huyen is so badass, she wasn't satisfied with launching one of
the biggest references for ML Engineering, she launched another for
AI Engineering"*)

**@agenticgirl** (March 27, 2026, 31 likes):
> "Every AI engineer eventually builds a small personal library. Not
> tutorials. Not random blog posts. But the books that actually explain
> how modern AI systems work."
(Her books included.)

### 2. Coverage of her Feb 2025 Pragmatic Engineer appearance

Top-ranked YouTube result in the window:
- **"AI Engineering with Chip Huyen"** — The Pragmatic Engineer,
  originally Feb 5, 2025. 208,551 views; 5,075 likes.
  - URL: https://www.youtube.com/watch?v=98o_L3jlixw
  - Her verified opening: *"Before when you wanted to build a machine
    learning application you need to build your own models... now if
    you want to build application leveraging machine learning or AI
    you can just send a direct API call and access to this wonderful
    capability. So it really lowers the entry barrier. You don't need
    data anymore. You don't need a fancy AI degree anymore. It's a
    shift from less machine learning and more engineering and more
    product."*

### 3. Korean/Portuguese AI community adoption

Her books appear in AI/ML roadmaps in Korean, Portuguese, Chinese
communities — strong evidence of international reach (translations in
progress into 6+ languages).

### 4. No direct posts from @chipro in the window returned

The skill's X search via her handle returned 9 posts total, but many
are recommendations *about* her rather than *from* her. She is either
posting less frequently in April 2026 or her posts are getting less
engagement than others' recommendations of her books.

---

## What the window did NOT surface

- **No LinkedIn posts** from Chip — skill doesn't cover LinkedIn (where
  she has 315K followers).
- **No new blog posts on huyenchip.com.** Last essay: January 2025
  ("Common pitfalls"). She has published ~1 major essay per 1-3 months;
  nothing new in the Mar-Apr 2026 window.
- **No stealth-startup announcement.** She is "Building at Stealth"
  since January 2026; nothing public yet.
- **No new book / conference keynote announcements.**
- **Bluesky 403** — same pattern as Shah/Karpathy.
- **Reddit silent** — Codex fallback bug, same as other voices.

---

## How to refresh this file

```bash
python3 /Users/andrewn/.claude/skills/last30days/scripts/last30days.py \
  "Chip Huyen AI Engineering ML systems" \
  --emit=compact \
  --no-native-web \
  --save-dir=~/Documents/Last30Days \
  --x-handle=chipro \
  --deep
```

Supplement with direct WebFetch on:
- https://huyenchip.com/blog (new essays)
- https://www.linkedin.com/in/chiphuyen/ (her higher-yield channel)
- https://github.com/chiphuyen (new repos)
- Stealth-startup launch (when it happens)

---

## What to look for specifically on the next refresh

1. **New blog essays on huyenchip.com** — she publishes deep technical
   essays at 1-3 month intervals. A new one is due.
2. **LinkedIn long-form posts** — her highest-yield channel for voice
   sampling. Check activity feed at linkedin.com/in/chiphuyen.
3. **Stealth startup announcement** — she is currently (Jan 2026+)
   "Building at Stealth." Topic unknown.
4. **ACM Queue editorial contributions** — she joined the editorial
   board in October 2024.
5. **Conference talks** — she is a regular speaker at QCon, Databricks
   Data+AI, PyTorch Conference, TEDAI SF.
6. **Sniffly-style dogfooding projects on GitHub** — she drops small
   tools (like the Claude Code analytics dashboard) periodically.
7. **Any Latent Space guest appearance** — notable gap in her podcast
   record despite swyx endorsing her book.

---

## Last reviewed

- Reviewed: 2026-04-17
- Refresh cadence: every 30 days recommended; supplement with direct
  LinkedIn check since the skill can't access LinkedIn.
