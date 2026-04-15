# AI Council Improvement Roadmap

## Current State (2026-04-14)

- 10 voice profiles, fully source-backed with publications and URLs
- Grounding protocol requiring sourced evidence vs persona inference
- Signal files for all 10 voices
- Structured review format with rating mode
- Used for: SQS paper review (v1→v4, 5.3→8.4)

## Gaps Identified

### 1. No automated signal refresh

The `signals/recent/` files are manually written snapshots. They go stale
within weeks. Each voice has a `Watch sources` section with URLs — these
should be checked automatically.

**Build:** A script that, for each voice:
- Fetches their X/Twitter feed (last 30 days)
- Fetches their blog/site RSS or recent pages
- Fetches Google Scholar for new publications
- Summarizes new signals into `signals/recent/<voice>.md`

**Run:** Weekly via cron or on-demand before a council review.

### 2. No review history

Council reviews are generated in conversation context and lost. There's no
record of: what was reviewed, what the ratings were, what changed because
of it, whether the council was right.

**Build:** A `reviews/` directory. Each review saved as a dated markdown file
with: paper/topic, active voices, ratings, recommendations, what was acted on.

**Why it matters:** Without history, the council can't improve. We can't ask
"were the council's predictions about the paper accurate?" or "which voice
gave the most useful feedback?"

### 3. No cross-voice calibration

All voices rate on 1-10 but there's no calibration of what "7" means.
Shah's 7 might be Chen's 8. Ratings are not comparable across reviews.

**Build:** A calibration document with 2-3 anchor examples at specific
scores (e.g., "a 5 means X, a 7 means Y, a 9 means Z"). Each voice
should reference the same anchor scale.

### 4. No automated literature verification

The grounding protocol requires cross-referencing citations, but this is
done manually by the AI during the review. It should be systematic.

**Build:** A script that takes a .bib file or paper.tex, extracts all
citations, and for each one:
- Searches Google Scholar / Semantic Scholar for the paper
- Verifies title, authors, year, venue match
- Checks if the paper's characterization matches the source's actual findings
- Flags mismatches

This would have caught the Stetson, Yetisgen, and AlpacaEval errors
automatically instead of requiring a manual research agent.

### 5. No voice interaction testing

The council meeting section has voices "arguing" but there's no way to
test whether the arguments are structurally distinct or just GPT-style
consensus with different names attached.

**Build:** A validation check: after generating a council meeting, ask
"could you swap Voice A's argument with Voice B's without changing the
substance?" If yes, the voices aren't distinct enough.

### 6. No external voice addition protocol

Adding a new voice requires writing a full profile from scratch. There's
no intake template that asks: "what distinct pressure does this voice add
that no existing voice covers?"

**Build:** A `council/add-voice-checklist.md` that requires:
- What gap this voice fills
- Which existing voice it's closest to (and how it differs)
- At least 3 sourced publications
- A test question where this voice would give different advice than all existing voices

### 7. No integration with project review workflows

The council is invoked manually in conversation. There's no way to
trigger a council review from a CI/CD pipeline, a PR, or a scheduled job.

**Build:** A script `scripts/run_council_review.ts` that:
- Takes a document path (paper, design doc, strategy memo)
- Loads relevant voice profiles
- Generates a structured review
- Saves to `reviews/`
- Optionally posts to Slack

### 8. No disagreement tracking

The council is most valuable when voices disagree. Currently disagreements
are generated in the meeting section but not tracked or scored.

**Build:** Tag each review with: which voices disagreed, on what, and
who turned out to be right (retrospective annotation).

## Priority Order

| # | Improvement | Effort | Impact |
|---|---|---|---|
| 1 | Review history (`reviews/` directory) | 1 hour | Track what the council recommends and whether it was right |
| 2 | Rating calibration anchors | 30 min | Make scores comparable across reviews |
| 3 | Automated signal refresh script | 1 day | Keep voice profiles current without manual work |
| 4 | Citation verification script | 1 day | Catch mischaracterized citations automatically |
| 5 | Add-voice checklist | 30 min | Prevent duplicate or weak voice additions |
| 6 | Review workflow integration | 2 hours | Trigger reviews from CI/PR/cron |
| 7 | Voice interaction testing | 1 hour | Ensure voices are structurally distinct |
| 8 | Disagreement tracking | 30 min | Learn which voices add the most value |
