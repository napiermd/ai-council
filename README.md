# AI Council

Open-source roundtable for machine learning and AI strategy, systems, product
judgment, evaluation, and deployment.

This repo ships as:

- an installable CLI: `ai-council`
- a slash-command pack for Claude and Codex
- a reusable council corpus of voices, packs, references, and examples

## Install

### Local install from a clone

```bash
git clone <your-url>/ai-council.git
cd ai-council
./scripts/install.sh
```

That install does three things:

- links `ai-council` into `~/.local/bin`
- adds `~/.local/bin` to your shell startup file if needed
- installs council command files into `~/.claude/commands/`, `~/.Codex/commands/`, and `~/.codex/commands/`

Open a new terminal, then verify:

```bash
ai-council doctor
ai-council list commands
ai-council list voices
```

### Optional npm-style install

If you prefer a package-style entrypoint, this repo also exposes a `bin`:

```bash
npm install -g .
ai-council doctor
```

## Slash Commands

Installed slash commands:

- `/council`
- `/council-product`
- `/council-systems`
- `/council-clinical`
- `/ask-nigam`
- `/council-review`
- `/council-paper`
- `/council-pr-review`
- `/council-sqs`

These are installed into:

- `~/.claude/commands/`
- `~/.Codex/commands/`
- `~/.codex/commands/`

## CLI Commands

Core CLI surface:

```bash
ai-council help
ai-council doctor
ai-council list voices
ai-council list packs
ai-council list commands
ai-council prompt direct "..."
ai-council prompt systems "Should this agent stack keep a planner?"
ai-council prompt product "Is this product wedge actually sharp enough?"
ai-council prompt clinical "Would this workflow survive deployment?"
ai-council prompt nigam "Would a hospital actually adopt this workflow?"
ai-council prompt paper "What is the weak claim in this memo?"
ai-council prompt pr-review "Should this design doc be approved?"
ai-council prompt sqs "Should SQS keep optimizing assembly agents?"
```

## File-Aware Review Commands

Use these when you want the council to review a concrete artifact, not just a
question:

```bash
ai-council review path/to/file.md
ai-council sqs-review path/to/file.md
ai-council review --lines 80 path/to/file.md
ai-council review --tail 60 path/to/file.md
ai-council review --full path/to/file.md
```

`review` is the generic rating-mode artifact review.
`sqs-review` adds the SQS-specific clinical and agent-systems context.
Both commands inline the target file contents with line numbers.
Use `--lines N`, `--tail N`, or `--full` to control scope per invocation.
`AI_COUNCIL_MAX_REVIEW_LINES` still sets the default head truncation limit.

## Quick Start

Use the council in-session when you need pressure on:

- product direction
- model, agent, and systems choices
- evaluation design
- workflow realism
- deployment tradeoffs

If the question is clinical, operational, or health-system-facing, default to
Nigam Shah as an anchor voice first.

Good starting commands:

```bash
ai-council prompt product "Is this product wedge actually sharp enough?"
ai-council prompt systems "Should this workflow stay multi-agent?"
ai-council prompt clinical "Would this survive real hospital conditions?"
ai-council review docs/design.md
```

## What This Repo Is

This repo is meant to be a council of strong voices, not a consensus machine.
The point is to surface disagreement, force better reasoning, and make design
tradeoffs explicit without getting lost in a crowd of interchangeable opinions.

Use it to:

- pressure-test AI product ideas before building
- debate model, agent, and systems choices
- separate research novelty from product usefulness
- bring domain-specific voices into ML discussions
- keep a reusable roster of AI/ML perspectives instead of starting from scratch

## Core Council

| Voice | Primary domain |
| --- | --- |
| Andrej Karpathy | LLM builders, training intuition, model-product bridge |
| Chip Huyen | AI engineering, inference, evals, serving systems |
| Jeremy Howard | Practical ML, fast iteration, democratization |
| Pete Steinberger | Product quality, agentic engineering, shipping discipline |
| Simon Willison | Pragmatic AI tooling, practitioner judgment, shipping in public |
| Nigam Shah | Clinical AI, data realism, health-system deployment |
| Jonathan H. Chen | Bedside workflow realism, clinician adoption, decision-support fit |
| Danielle Bitterman | Practicing physician's view on whether clinical AI evaluation protects patients |
| Douwe Kiela | Grounded generation, RAG, hallucination reduction |

## Specialist Extensions

Use these only when the problem clearly calls for them:

| Voice | Bring in when... |
| --- | --- |
| Fei-Fei Li | You need human-centered AI, institutional governance, or spatial-intelligence framing. |
| Harrison Chase | You need multi-agent state flow, memory, or human-in-the-loop checkpoint design. (Use knowing LangChain carries real framework-churn baggage.) |
| Percy Liang | You need to know whether an evaluation is valid, comprehensive, and replicable. |
| Ethan Mollick | You need an empirical read on whether real professionals will adopt the tool, and how their work changes when they do. |
| Aidan Gomez | You need a founder-operator who has scaled a language-AI company through enterprise sales and multiple funding rounds. |
| Bob Wachter | You need department-chair-level health-system implementation realism and institutional memory from the EHR-rollout era. |

See `council/roster.md` for archived voices and the reasoning behind removals.

## How To Use The Corpus

1. Open this repo in Claude Code, Codex, or another coding agent.
2. Read [`SKILL.md`](./SKILL.md) for council behavior.
3. Read [`council/roster.md`](./council/roster.md) for the current voices.
4. Pull in individual files from `references/` when a specific voice or domain is needed.
5. For embodiment-grade use, load from `references/deep/<voice>/` and start with `embodiment.md` + `voice.md`.
6. Use [`council/session-template.md`](./council/session-template.md) and [`council/invocation-patterns.md`](./council/invocation-patterns.md) when deploying the council on a live question.
7. Use [`council/rating-scale.md`](./council/rating-scale.md) for review-panel behavior.
8. Use [`council/response-rubric.md`](./council/response-rubric.md) to judge whether a council answer is actually good.
9. Use [`council/deployment-guide.md`](./council/deployment-guide.md) and the files in [`packs/`](./packs/) when deploying the council into another repo.
10. Use [`signals/`](./signals/) when you need a last-30-days recency layer instead of only the hand-authored profiles.

## Packs

Use these when you want a reusable default setup instead of improvising every
session:

- [Founder Product Pack](./packs/founder-product-pack.md)
- [Agent Systems Pack](./packs/agent-systems-pack.md)
- [Clinical AI Pack](./packs/clinical-ai-pack.md)
- [Stanford Academic Pack](./packs/stanford-academic-pack.md)

## Live Use

This repo is meant to be used in-session, not just read.

When you have a real decision in front of you:

1. Start from [`council/session-template.md`](./council/session-template.md).
2. Pick a mode from [`council/invocation-patterns.md`](./council/invocation-patterns.md).
3. If the problem is clinical, start with [`council/ask-nigam.md`](./council/ask-nigam.md).
4. If you want judgment, use [`council/rating-scale.md`](./council/rating-scale.md) and ask for `rating mode`.
5. If you want the voices to challenge each other instead of only scoring in parallel, ask for a `council meeting`.
6. Load only the voices needed for that question.

If you want the installable command surface instead of manual file loading, run
`./scripts/install.sh` and use `ai-council` plus the installed slash commands.

## Deployment In Other Repos

If you want to use the council from another project, start with the
[deployment guide](./council/deployment-guide.md).

Typical pattern:

1. Keep this repo as a sibling repo, submodule, or reference dependency.
2. Install the CLI and slash commands with `./scripts/install.sh`.
3. Use a pack or review command instead of manually reconstructing the prompt every time.

## Example Sessions

Use these as copyable starting points:

- [Product direction review](./examples/product-direction-review.md)
- [Product direction response](./examples/product-direction-response.md)
- [Agent workflow review](./examples/agent-workflow-review.md)
- [Agent workflow response](./examples/agent-workflow-response.md)
- [Clinical AI ask Nigam](./examples/clinical-ai-ask-nigam.md)
- [Clinical AI ask Nigam response](./examples/clinical-ai-ask-nigam-response.md)
- [Academic memo review](./examples/academic-memo-review.md)
- [Academic memo response](./examples/academic-memo-response.md)
- [Paper critique review](./examples/paper-critique-review.md)
- [Class project review](./examples/class-project-review.md)

## Source-Backed Profiles

The goal is not to imitate a person's brand voice. The goal is to distill
repeatable operating patterns from:

- official bios and institutional profiles
- official websites or labs
- first-party technical writing, talks, or repositories
- current public signals about what they are actively building or emphasizing

Profiles should show their source basis and a `Last reviewed` marker so the
council does not quietly drift into stale fan fiction.

Use [`council/source-index.md`](./council/source-index.md) as the fast audit
surface, and [`council/refresh-checklist.md`](./council/refresh-checklist.md)
as the repeatable maintenance workflow.

## Recent-Signal Automation

The council now has a generated recency layer:

- [`data/voice_watchlist.json`](./data/voice_watchlist.json)
- [`signals/`](./signals/)
- [`scripts/refresh_recent_signals.py`](./scripts/refresh_recent_signals.py)
- [`.github/workflows/weekly-voice-refresh.yml`](./.github/workflows/weekly-voice-refresh.yml)

Start with [`signals/weekly-review.md`](./signals/weekly-review.md) if you want
the human-action digest rather than raw per-voice signal files.

This is where last-30-days monitoring lives. It should inform the profiles, not replace them.

## Repository Structure

```text
ai-council/
├── CLAUDE.md
├── SKILL.md
├── .github/workflows/
│   └── weekly-voice-refresh.yml
├── council/
│   ├── ask-nigam.md
│   ├── deployment-guide.md
│   ├── invocation-patterns.md
│   ├── operating-principles.md
│   ├── profile-standard.md
│   ├── refresh-checklist.md
│   ├── response-rubric.md
│   ├── roster.md
│   ├── session-template.md
│   └── source-index.md
├── examples/
│   ├── academic-memo-response.md
│   ├── academic-memo-review.md
│   ├── agent-workflow-review.md
│   ├── agent-workflow-response.md
│   ├── class-project-review.md
│   ├── clinical-ai-ask-nigam.md
│   ├── clinical-ai-ask-nigam-response.md
│   ├── paper-critique-review.md
│   ├── product-direction-response.md
│   └── product-direction-review.md
├── packs/
│   ├── agent-systems-pack.md
│   ├── clinical-ai-pack.md
│   ├── founder-product-pack.md
│   └── stanford-academic-pack.md
├── data/
│   └── voice_watchlist.json
├── references/                   # lean voice cards — quick load
│   ├── aidan-gomez.md
│   ├── andrej-karpathy.md
│   ├── bob-wachter.md
│   ├── chip-huyen.md
│   ├── danielle-bitterman.md
│   ├── douwe-kiela.md
│   ├── ethan-mollick.md
│   ├── fei-fei-li.md
│   ├── harrison-chase.md
│   ├── jeremy-howard.md
│   ├── jonathan-chen.md
│   ├── nigam-shah.md
│   ├── percy-liang.md
│   ├── pete-steinberger.md
│   ├── simon-willison.md
│   ├── voice-template.md
│   └── deep/
├── reviews/
│   └── 2026-04-14-sqs-paper-v4.md
├── scripts/
│   └── refresh_recent_signals.py
├── signals/
│   ├── README.md
│   ├── summary.md
│   ├── weekly-review.md
│   └── recent/
│       └── *.md
└── .gitignore
```

## Design Principles

- Keep the roster opinionated, not exhaustive.
- Every voice should add a distinct kind of pressure.
- Encourage disagreement when it reveals tradeoffs.
- Prefer named arguments and operating principles over vague inspiration.
- Add new voices only when they contribute something structurally different.
- Treat Nigam Shah as a first-class anchor for anything involving real-world
  health data, workflow, adoption, and institutional value.
- Keep profiles source-backed and periodically refreshed.

## Embodiment-Grade Profiles (`references/deep/`)

Lean reference cards in `references/*.md` are the lookup cards. The `deep/`
subdirectory holds embodiment-grade profiles — quote-sourced, multi-file
dossiers that let an LLM accurately speak as the voice, not just cite them.

Each deep profile contains:

- `embodiment.md` — the persona-invocation file. Load this first.
- `voice.md` — verbatim quotes, recurring analogies, banned phrases, cadence.
- `frameworks.md` — named frameworks with mechanics and invocation contexts.
- `publications.md` — paper corpus by theme.
- `appearances.md` — podcasts, keynotes, media interviews with direct quotes.
- `positions.md` — strong stances, tensions, predictions.
- `biography.md` — career arc, roles, companies, awards.
- `recent-30d.md` — auto-refreshable last-30-days signal window.
- `README.md` — index and load order.

Built so far:

- `references/deep/nigam-shah/` (2026-04-17) — first voice. 9 files, ~2500 lines.

Next planned builds:

- Andrej Karpathy
- Chip Huyen
- Simon Willison
- Pete Steinberger
- Jeremy Howard
- Jonathan Chen
- Danielle Bitterman
- Douwe Kiela

Specialist extensions (Fei-Fei Li, Chase, Liang, Mollick, Gomez, Wachter)
built on demand.

## Recent-Signal Automation Limitations

The `last30days` skill (at `~/.claude/skills/last30days/`) covers Reddit,
X, YouTube, Bluesky, Hacker News, TikTok, Instagram, Truth Social, and web.
Known gaps:

- No LinkedIn coverage.
- Reddit search depends on OpenAI Responses API with Codex auth.
- Bluesky auth requires `BSKY_HANDLE` + `BSKY_APP_PASSWORD`.
- TikTok/Instagram require `SCRAPECREATORS_API_KEY`.

For low-X and low-Reddit voices, direct WebFetch on LinkedIn, Stanford
profiles, and journal archives is higher yield. For heavy X and Reddit voices,
the `last30days` skill is the right tool.

## Potential Future Voices

- Shreya Shankar for data quality and eval pipelines
- Hamel Husain for agent workflows and operational evaluation
- Dario Amodei for scaling laws and frontier deployment strategy
- Gary Marcus for AI reliability skepticism and regulatory red-teaming
- Alistair Johnson for clinical NLP benchmarks and EHR data realism (MIMIC)
