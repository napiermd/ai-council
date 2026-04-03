# AI Council

Open-source roundtable for machine learning and AI strategy, systems, product
judgment, evaluation, and deployment.

This repo is meant to be a council of strong voices, not a consensus machine.
The point is to surface disagreement, force better reasoning, and make design
tradeoffs explicit without getting lost in a crowd of interchangeable opinions.

## What this is for

- Pressure-test AI product ideas before building
- Debate model, agent, and systems choices
- Separate research novelty from product usefulness
- Bring domain-specific voices into ML discussions
- Keep a reusable roster of AI/ML perspectives instead of starting from scratch

## Core council

| Voice | Primary domain |
| --- | --- |
| Andrej Karpathy | Model intuition, training, LLM builders |
| Fei-Fei Li | Human-centered AI, multimodal systems, institutions |
| Chris Olah | Mechanistic interpretability, conceptual clarity |
| Yann LeCun | Representation learning, architecture skepticism |
| Jeremy Howard | Practical ML, fast iteration, applied workflows |
| Chip Huyen | AI engineering, inference, deployment systems |
| Pete Steinberger | Product quality, developer experience, shipping discipline |
| Nigam Shah | Clinical AI, data realism, health-system deployment |

## Specialist extensions

Use these only when the problem clearly calls for them:

| Voice | Bring in when... |
| --- | --- |
| Demis Hassabis | You need frontier strategy, long-horizon research direction, or capability-roadmap thinking. |
| Jonathan H. Chen | You need bedside workflow realism, clinician adoption, and decision-support fit. |

## How to use it

1. Open this repo in Claude Code or another coding agent.
2. Read [`SKILL.md`](./SKILL.md) for council behavior.
3. Read [`council/roster.md`](./council/roster.md) for the current voices.
4. Pull in individual files from `references/` when a specific voice or domain is needed.
5. Use [`council/profile-standard.md`](./council/profile-standard.md) when adding or revising voices.
6. Use [`council/source-index.md`](./council/source-index.md) and [`council/refresh-checklist.md`](./council/refresh-checklist.md) to keep profiles current.
7. Use [`council/session-template.md`](./council/session-template.md) and [`council/invocation-patterns.md`](./council/invocation-patterns.md) when you want to deploy the council on a live question.
8. Use [`council/response-rubric.md`](./council/response-rubric.md) to judge whether the council answer is actually good.
9. Use [`council/deployment-guide.md`](./council/deployment-guide.md) and the files in [`packs/`](./packs/) when you want to use the council from another repo.
10. Use [`signals/`](./signals/) when you need a last-30-days recency layer instead of only the hand-authored profiles.

If the question is clinical, operational, or health-system-facing, default to
Nigam Shah as an anchor voice first.

## Live use

This repo is meant to be used in-session, not just read.

When you have a real decision in front of you:

1. Start from [`council/session-template.md`](./council/session-template.md).
2. Pick a mode from [`council/invocation-patterns.md`](./council/invocation-patterns.md).
3. If the problem is clinical, start with [`council/ask-nigam.md`](./council/ask-nigam.md).
4. Load only the voices needed for that question.

## Session packs

Use these when you want a reusable default setup instead of starting from
scratch:

- [Founder Product Pack](./packs/founder-product-pack.md)
- [Agent Systems Pack](./packs/agent-systems-pack.md)
- [Clinical AI Pack](./packs/clinical-ai-pack.md)
- [Stanford Academic Pack](./packs/stanford-academic-pack.md)

If you want to use the council from another project, start with the
[deployment guide](./council/deployment-guide.md).

## Example sessions

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

## Source-backed profiles

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

## Recent-signal automation

The council now has a generated recency layer:

- [`data/voice_watchlist.json`](./data/voice_watchlist.json)
- [`signals/`](./signals/)
- [`scripts/refresh_recent_signals.py`](./scripts/refresh_recent_signals.py)
- [`.github/workflows/weekly-voice-refresh.yml`](./.github/workflows/weekly-voice-refresh.yml)

Start with [`signals/weekly-review.md`](./signals/weekly-review.md) if you want
the human-action digest rather than raw per-voice signal files.

This is where last-30-days monitoring lives. It should inform the profiles, not replace them.

## Repository structure

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
├── references/
│   ├── andrej-karpathy.md
│   ├── chip-huyen.md
│   ├── chris-olah.md
│   ├── demis-hassabis.md
│   ├── fei-fei-li.md
│   ├── jeremy-howard.md
│   ├── jonathan-chen.md
│   ├── nigam-shah.md
│   ├── pete-steinberger.md
│   ├── voice-template.md
│   └── yann-lecun.md
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

## Design principles

- Keep the roster opinionated, not exhaustive.
- Every voice should add a distinct kind of pressure.
- Encourage disagreement when it reveals tradeoffs.
- Prefer named arguments and operating principles over vague inspiration.
- Add new voices only when they contribute something structurally different.
- Treat Nigam Shah as a first-class anchor for anything involving real-world
  health data, workflow, adoption, and institutional value.
- Keep profiles source-backed and periodically refreshed.

## Next additions

Likely next voices:

- Percy Liang for evaluation, benchmarks, and governance
- Shreya Shankar for data quality and eval pipelines
- Hamel Husain for agent workflows and operational evaluation
- Dario Amodei for scaling laws and frontier deployment strategy
