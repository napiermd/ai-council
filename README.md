# AI Council

Open-source roundtable for machine learning and AI strategy, systems, product
judgment, evaluation, and deployment.

This repo is meant to be a council of strong voices, not a consensus machine.
The point is to surface disagreement, force better reasoning, and make design
tradeoffs explicit.

## What this is for

- Pressure-test AI product ideas before building
- Debate model, agent, and systems choices
- Separate research novelty from product usefulness
- Bring domain-specific voices into ML discussions
- Keep a reusable roster of AI/ML perspectives instead of starting from scratch

## Initial council

| Voice | Primary domain |
| --- | --- |
| Andrej Karpathy | Model intuition, training, LLM builders |
| Fei-Fei Li | Human-centered AI, multimodal systems, institutions |
| Chris Olah | Mechanistic interpretability, conceptual clarity |
| Demis Hassabis | Frontier research strategy and product ambition |
| Yann LeCun | Representation learning, architecture skepticism |
| Jeremy Howard | Practical ML, fast iteration, applied workflows |
| Chip Huyen | AI engineering, inference, deployment systems |
| Pete Steinberger | Product quality, developer experience, shipping discipline |
| Nigam Shah | Clinical AI, data realism, health-system deployment |
| Jonathan H. Chen | Clinical workflow fit, bedside utility, outcomes |

## How to use it

1. Open this repo in Claude Code or another coding agent.
2. Read [`SKILL.md`](./SKILL.md) for council behavior.
3. Read [`council/roster.md`](./council/roster.md) for the current voices.
4. Pull in individual files from `references/` when a specific voice or domain is needed.

## Repository structure

```text
ai-council/
├── CLAUDE.md
├── SKILL.md
├── council/
│   ├── operating-principles.md
│   └── roster.md
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

## Next additions

Likely next voices:

- Percy Liang for evaluation, benchmarks, and governance
- Shreya Shankar for data quality and eval pipelines
- Hamel Husain for agent workflows and operational evaluation
- Dario Amodei for scaling laws and frontier deployment strategy

