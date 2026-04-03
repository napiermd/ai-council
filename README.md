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

If the question is clinical, operational, or health-system-facing, default to
Nigam Shah as an anchor voice first.

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

## Repository structure

```text
ai-council/
├── CLAUDE.md
├── SKILL.md
├── council/
│   ├── operating-principles.md
│   ├── profile-standard.md
│   ├── refresh-checklist.md
│   ├── roster.md
│   └── source-index.md
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
