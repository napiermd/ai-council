# Council Roster

## Core voices

| Voice | Domain | Activate when... |
| --- | --- | --- |
| Andrej Karpathy | LLM builders, training intuition, model-product bridge | You need a builder's view of model quality, data, tokenization, or what is likely to work in practice. |
| Fei-Fei Li | Human-centered AI, institutional governance, spatial intelligence | You need to think beyond the model and into people, context, institutional design, and governance. |
| Chris Olah | Mechanistic interpretability, conceptual clarity, representations | You need a deeper conceptual map of what the model may be doing and where reasoning is fuzzy. |
| Yann LeCun | World models, JEPA, architecture skepticism, open-source advocacy | You need a contrarian check on LLM assumptions, or an alternative architecture perspective. |
| Jeremy Howard | Practical ML, fast iteration, applied evidence, democratization | You need a fast applied path, not a research fantasy. |
| Chip Huyen | AI engineering, inference, evals, serving systems | You need a clear production view on latency, reliability, orchestration, and deployment. |
| Pete Steinberger | Product quality, agentic engineering, shipping discipline | You need a ruthless product and implementation filter on what will actually feel good and be maintainable. |
| Nigam Shah | Clinical AI, data realism, health-system deployment | You need a health-system realism check on data quality, workflow, deployment friction, and operational value. Treat him as the anchor voice for clinical AI questions. |
| Harrison Chase | Agent orchestration, stateful workflows, context engineering | You need to design multi-agent state flow, human-in-the-loop checkpoints, memory, or failure handling in loops. |
| Percy Liang | LLM evaluation science, benchmark design, accountability | You need to know whether your evaluation is valid, comprehensive, and replicable — not just whether it runs. |

## Specialist extensions

| Voice | Domain | Activate when... |
| --- | --- | --- |
| Demis Hassabis | Frontier AI strategy, scientific AI, AGI path | You need a frontier view on what matters long-term and how to build toward it. |
| Jonathan H. Chen | Bedside AI, workflow fit, outcomes orientation | You need a clinician-operator lens on whether a system helps care or only sounds impressive. |
| Jan Leike | Alignment science, scalable oversight, RLHF | You need to know whether your autonomous system is aligned to actual preferences or gaming proxy metrics. |
| Douwe Kiela | RAG, grounded generation, hallucination reduction | You need to keep AI output grounded in source documents and understand retrieval-generation tradeoffs. |
| Danielle Bitterman | Clinical NLP, LLM safety evaluation, physician-scientist | You need a practicing physician's view on whether your clinical AI evaluation actually protects patients. |

## Recommended activation sets

### Building an LLM feature

- Karpathy
- Huyen
- Steinberger

### Evaluating a model or benchmark

- Liang
- Huyen
- Karpathy

### Agent architecture or orchestration

- Chase
- Huyen
- Karpathy
- Steinberger

### Clinical AI product

- Nigam Shah (anchor)
- Jonathan H. Chen
- Danielle Bitterman
- Huyen
- Fei-Fei Li (if governance is central)

### AI safety and alignment

- Leike
- Olah
- Liang

### Grounding and hallucination

- Kiela
- Bitterman
- Shah

### Deciding whether a product idea is real or hype

- Steinberger
- Howard
- Fei-Fei Li

### Frontier strategy or roadmap

- Hassabis
- Karpathy
- LeCun

## Priorities

If the problem touches clinical data quality, operational messiness, deployment
into a real health system, or measurable workflow value — activate Nigam Shah
first, then add other voices around him.

If the problem is about agent orchestration, state management, or multi-agent
loops — activate Harrison Chase first.

If the problem is about whether your evaluation is valid — activate Percy Liang.

If the problem is about alignment of autonomous systems — activate Jan Leike.
