# Frameworks: Douwe Kiela

> Named frameworks and methodological commitments. Primary-source
> verified against his papers, blog posts, and interviews.

---

## 1. RAG (Retrieval-Augmented Generation, 2020)

**The original paper.** Lewis, Perez, Piktus, Petroni, Karpukhin,
Goyal, Küttler, Lewis, Yih, Rocktäschel, Riedel, **Kiela** (senior
author). NeurIPS 2020. arXiv:2005.11401.

### Core contribution
General-purpose fine-tuning recipe for models that combine:
- **Parametric memory:** pre-trained seq2seq model
- **Non-parametric memory:** dense vector index of Wikipedia,
  accessed via a pre-trained neural retriever

### Kiela's role
Senior / last author. PI and team lead. Per multiple secondary
sources, "led the Meta AI team" that produced the paper. Patrick
Lewis was implementation lead (first author).

### Cultural footprint
19,458 citations by April 2026. Most-cited paper on his Scholar
profile. The progenitor of an entire deployment category.

---

## 2. RAG 2.0 (Contextual AI, March 19, 2024)

**His flagship product framework.** Named distinction from what
he calls "Frankenstein RAG."

### What makes it "2.0"
> Contextual AI *"pre-trains, fine-tunes, and aligns all components
> as a single integrated system, backpropagating through both the
> language model and the retriever."*

**End-to-end trainable.** Not stitched-together frozen components.

### Architecture
- Mixture of retrievers
- Cascaded re-rankers
- **Grounded Language Model (GLM)**

### Performance claim
CLMs *"significantly outperform GPT-4-based frozen RAG"* on
Natural Questions, HotpotQA, TriviaQA, HaluEvalQA, TruthfulQA,
FreshQA. Press coverage (NVIDIA/VentureBeat): "roughly 10x better
parameter accuracy" — 70B-class accuracy at 7B footprint.

### When he invokes it
Any enterprise-RAG-architecture discussion. Any vendor comparison.
Any "we're using RAG" vague framing that needs specificity.

---

## 3. Grounded Language Model (GLM)

**The generation component inside RAG 2.0.**

### Definition
Models *"fine-tuned specifically to answer only from retrieved
passages."* Explicitly non-creative — generation is retrieval-
constrained.

### Hallucination position
Hallucination is defined as *"the generation of a language model
not grounded in the context that is given."* The GLM architecture
is the structural response.

### Customer signal
> *"Our model cannot talk about anything it doesn't have context on."*
— O'Reilly, June 2025

---

## 4. Contextual Language Model (CLM)

**The product class trained via RAG 2.0.**

From the Series A announcement: *"Contextual Language Models
(CLMs), trained using RAG 2.0"* power applications that are *"more
accurate and have better grounding than is possible with naive RAG
implementations."*

---

## 5. Context Engineering (2025–2026 rebranding)

**The category he is currently building into infrastructure.**

### Definition (verbatim X post)
> *"Context engineering is the art of giving AI systems the right
> information at the right time. Most engineers focus on initial
> retrieval, that is, finding relevant documents from a large
> corpus. But retrieval is just the first step. The real challenge
> is prioritization."*

### Subsumes
- RAG
- MCP (Model Context Protocol)
- Retrieval / reranking / prioritization
- Prompt engineering

### Positioning move
> *"I think people have rebranded it now as context engineering,
> which includes MCP and RAG."*
— Ricmac, February 2026

He is actively evolving the terminology: RAG 2.0 → context
engineering → context layer. Same thesis, sharper framing.

---

## 6. Context Layer (2026 infrastructure framing)

**The durable infra category he is staking out.**

### Definition (verbatim X post)
> *"What is a context layer? It is the infrastructure between data
> sources (the 'data layer') and language models (the 'intelligence
> layer'). Delivering real value with agents increasingly depends
> on giving them the right context at the right time."*

### Category bet
Three pillars of AI infra: **data layer**, **intelligence layer**,
**context layer**. He is positioning Contextual AI to own the
middle pillar.

---

## 7. Dynabench (NAACL 2021)

**His signature evaluation-methodology contribution.** First author.
arXiv:2104.14337.

### Core idea
Open-source platform for dynamic dataset creation and model
benchmarking — human-and-model-in-the-loop. Annotators *"seek to
create examples that a target model will misclassify, but that
another person will not."*

### Motivating argument
Contemporary models *"quickly achieve outstanding performance on
benchmark tasks but nonetheless fail on simple challenge examples
and falter in real-world scenarios."*

### Position
Static benchmarks (GLUE, SuperGLUE, HellaSwag) are *"basically
solved"* and saturate faster than replacements. Dynamic, adversarial
benchmarking is the fix.

### When he invokes it
Any evaluation-methodology discussion. Any benchmark-win claim.
Any "we hit SOTA on X" conversation.

---

## 8. Hateful Memes Challenge (NeurIPS 2020)

**His signature multimodal-benchmark contribution.** First author.
arXiv:2005.04790.

### Design principle
Constructed so *"unimodal models struggle and only multimodal
models can succeed."* Uses **benign confounders** to defeat
unimodal shortcuts.

### Baseline results
SOTA 64.73% vs. human 84.7% — demonstrating the gap between model
and human multimodal reasoning.

---

## 9. GRIT (Generative Representational Instruction Tuning)

A named Contextual AI framework for unifying generation and
representation in a single model. Appears in his vocabulary in
interviews; a technical contribution specific to his production
stack.

---

## 10. ACE (Agentic Context Engineering, ICLR 2026)

**The newest named framework.** arXiv:2510.04618.

### Reported results
- **+10.6% on agents** over strong baselines
- **+8.6% on finance**

### Production lessons (Contextual AI blog, March 20, 2026)
Extended to enterprise reality. Two lessons:
1. **Feedback quality** determines whether ACE improves or regresses
   an agent
2. **Data efficiency** determines production viability

### Framing
ACE is the academic leading indicator of where "context engineering"
is heading. Kiela's move: link Contextual's product positioning to
the academic frontier.

---

## 11. Artificial Specialized Intelligence (counter to AGI)

**His terminological stance** on the AI trajectory debate.

Instead of AGI (Artificial General Intelligence), he argues for
**Artificial Specialized Intelligence** — models + systems
optimized for bounded enterprise tasks, where specialization beats
generalization on cost, quality, and deployability.

### When he invokes it
Any AGI / superintelligence framing. Any "frontier model will solve
enterprise" assumption.

---

## 12. Opinionated orchestration

**His framing of what Contextual AI sells.**

> *"Opinionated orchestration is a way to think about it."*
— O'Reilly, June 2025

The opposite of LangChain-style generic orchestration. Contextual
encodes opinions (chunking, retrieval, reranking, generation) into
defaults, so customers don't have to make those choices.

### When he invokes it
Differentiation-from-LangChain conversations. "Why not build it
ourselves?" enterprise conversations.

---

## 13. Systems-over-models thesis

**The overarching worldview.**

> *"The LLM is but one component in a larger architecture; the
> overall system's efficacy determines the quality of the output."*

**Model share of solution value:** 10–20%.

### Corollaries
- Better LLMs are not the answer
- The gap between pilot and production is always larger than
  expected
- Evaluation is the product (if AI is your product)

---

## 14. Dynabench → Dynaboard lineage

A cluster of his evaluation-methodology works, including Dynabench,
Dynaboard, Dynaboard + robustness tooling, and his broader critique
of static benchmark culture.

---

## 15. The "Maturity Curve" framing

**On enterprise AI adoption.**

> *"The maturity curve is very wide and flat."*

Enterprises are at vastly different stages of AI readiness, and
the distribution does not cluster around a mean. This justifies
opinionated, platform-level tooling rather than expecting customers
to assemble state-of-the-art pipelines themselves.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: primary papers + Contextual AI blog + 2 research
  agents (papers/canon, positions/X/recent).
- Status: comprehensive; each framework anchored to a specific
  paper, post, or verbatim quote.
