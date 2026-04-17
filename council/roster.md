# Council Roster

## Core voices

| Voice | Domain | Activate when... |
| --- | --- | --- |
| Andrej Karpathy | LLM builders, training intuition, model-product bridge | You need a builder's view of model quality, data, tokenization, or what is likely to work in practice. |
| Chip Huyen | AI engineering, inference, evals, serving systems | You need a clear production view on latency, reliability, orchestration, and deployment. |
| Jeremy Howard | Practical ML, fast iteration, applied evidence, democratization | You need a fast applied path, not a research fantasy. |
| Pete Steinberger | Product quality, agentic engineering, shipping discipline | You need a ruthless product and implementation filter on what will actually feel good and be maintainable. |
| Simon Willison | Pragmatic AI tooling, practitioner judgment, shipping in public | You need a grounded read on a specific model, tool, or pattern from someone who has actually tried it this week. |
| Nigam Shah | Clinical AI, data realism, health-system deployment | You need a health-system realism check on data quality, workflow, deployment friction, and operational value. Treat him as the anchor voice for clinical AI questions. |
| Jonathan H. Chen | Bedside AI, workflow fit, outcomes orientation | You need a clinician-operator lens on whether a system helps care or only sounds impressive. |
| Danielle Bitterman | Clinical NLP, LLM safety evaluation, physician-scientist | You need a practicing physician's view on whether your clinical AI evaluation actually protects patients. |
| Douwe Kiela | RAG, grounded generation, hallucination reduction | You need to keep AI output grounded in source documents and understand retrieval-generation tradeoffs. |

## Specialist extensions

| Voice | Domain | Activate when... |
| --- | --- | --- |
| Fei-Fei Li | Human-centered AI, institutional governance, spatial intelligence | You need to think beyond the model and into people, context, institutional design, and governance. |
| Harrison Chase | Agent orchestration, stateful workflows, context engineering | You need to design multi-agent state flow, human-in-the-loop checkpoints, memory, or failure handling in loops. Use knowing that LangChain carries real framework-churn baggage. |
| Percy Liang | LLM evaluation science, benchmark design, accountability | You need to know whether your evaluation is valid, comprehensive, and replicable — not just whether it runs. |
| Ethan Mollick | AI adoption in knowledge work, empirical productivity studies | You need a read on whether professionals will actually use this, and what changes in their work when they do. |
| Aidan Gomez | Founder-operator, enterprise AI, scaling a business from research lab to revenue | You need the voice of someone who built a language-AI company through multiple rounds, enterprise sales, and pivots. The "navigated business" seat. |
| Bob Wachter | Health-system operations, digital-health implementation realism | You need a department-chair lens on what actually happens when clinical AI meets a real hospital, clinician cognitive load, and unintended consequences. |

## Recommended activation sets

### Building an LLM feature

- Karpathy
- Huyen
- Steinberger
- Willison

### Evaluating a model or benchmark

- Liang
- Huyen
- Karpathy
- Willison (for practitioner reality check)

### Agent architecture or orchestration

- Chase
- Huyen
- Karpathy
- Steinberger

### Clinical AI product

- Nigam Shah (anchor)
- Jonathan H. Chen
- Danielle Bitterman
- Bob Wachter (if health-system deployment or institutional friction is central)
- Huyen
- Fei-Fei Li (if governance is central)

### Grounding and hallucination

- Kiela
- Bitterman
- Shah

### Deciding whether a product idea is real or hype

- Steinberger
- Howard
- Mollick (for knowledge-work adoption realism)
- Fei-Fei Li

### Founder / business decisions (stage, pricing, pivots)

- Gomez
- Steinberger
- Howard

### Will professionals actually use this

- Mollick
- Wachter (if clinical)
- Chen (if clinical)
- Steinberger

## Priorities

If the problem touches clinical data quality, operational messiness, deployment
into a real health system, or measurable workflow value — activate Nigam Shah
first, then add other voices around him.

If the problem is about agent orchestration, state management, or multi-agent
loops — activate Harrison Chase first.

If the problem is about whether your evaluation is valid — activate Percy Liang.

If the problem is a founder decision about scope, pricing, or how to navigate a
business transition — activate Aidan Gomez first.

If the problem is whether real professionals will adopt the tool — activate
Ethan Mollick first.

## Archived voices

These voices were removed from the active council on 2026-04-17. Their profiles
remain in `references/` for historical context. Reactivate only if the
underlying question genuinely maps to their domain.

- **Yann LeCun** — predictable LLM-skeptic contrarianism; JEPA work has not
  shipped consumer product. Reactivate only for an explicit "is transformer
  architecture the right long-term bet" question.
- **Chris Olah** — mechanistic interpretability rarely load-bearing for a
  product-stage company. Reactivate if a specific interpretability or
  circuits question is on the table.
- **Jan Leike** — alignment-science lens is mostly abstract at current scope.
  Reactivate if building autonomous agents where evaluation-gaming is a real
  concern.
- **Demis Hassabis** — frontier-strategy voice operates on decade horizons.
  Reactivate for roadmap conversations that are actually about decade-scale
  capability, not this quarter.
