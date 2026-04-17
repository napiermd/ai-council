# Frameworks: Chip Huyen

> Her named frameworks and recurring mental models with source and
> invocation context.

---

## 1. AI Engineering vs. ML Engineering

**Source:** *AI Engineering* book Ch. 1, § "AI Engineering Versus ML
Engineering" + Pragmatic Engineer podcast Feb 2025.

**Thesis:** AI Engineering is a distinct discipline from ML Engineering.
It starts from foundation models (APIs or open weights), not from data.

**Direct framing (Pragmatic Engineer transcript):**
> "Before when you wanted to build a machine learning application you
> need to build your own models... now if you want to build application
> leveraging machine learning or AI you can just send a direct API call
> and access to this wonderful capability. So it really lowers the
> entry barrier. You don't need data anymore. You don't need a fancy
> AI degree anymore. It's a shift from less machine learning and more
> engineering and more product."

### When she invokes it
Any time someone conflates classical ML practice with foundation-model
practice. The skill set is different: more engineering, more product,
more evaluation, less data curation and feature engineering.

---

## 2. The 3-layer AI stack

**Source:** "What I learned from looking at 900 most popular open
source AI tools," March 14, 2024.
https://huyenchip.com/2024/03/14/ai-oss.html

1. **Infrastructure** — compute, vector DBs, serving (vLLM, Triton,
   SkyPilot, Faiss, Milvus, Qdrant, LanceDB).
2. **Model development** — training, inference optimization, dataset
   engineering, evaluation (transformers, PyTorch, DeepSpeed, ggml,
   triton).
3. **Application development** — interfaces, agents, prompts. *"This
   layer is also known as AI engineering."*

**Observation:** 2023 was the year of application and application-
development growth.

### When she invokes it
Any "what's the AI stack?" discussion. To locate a company / product /
tool in the landscape.

---

## 3. The 5-step GenAI platform architecture

**Source:** "Building A Generative AI Platform," July 25, 2024.
https://huyenchip.com/2024/07/25/genai-platform.html

Starts with: **Query → Model API → Response.** Then iteratively add:

1. **Enhance context** — RAG, query rewriting, structured retrieval,
   tool use. *"Context construction for foundation models is equivalent
   to feature engineering for classical ML models."*
2. **Guardrails** — input (privacy leaks, jailbreaks) + output (quality,
   policy).
3. **Model router + gateway** — intent classification; access control;
   cost management. *"A model gateway is access control and cost
   management."*
4. **Cache** — exact + **semantic cache**. *"Unlike exact cache,
   semantic cache doesn't require the incoming query to be identical
   to any of the cached queries."*
5. **Complex logic + write actions** — agentic, state-changing.
   *"Write actions make a system vastly more capable. However, the
   prospect of giving AI the ability to automatically alter our lives
   is frightening."*

Plus observability and pipeline orchestration as cross-cutting concerns.

### When she invokes it
Any production GenAI application design question. Her guiding rule:
*"Start from the simplest architecture and progressively add more
components."*

---

## 4. RAG vs. finetuning

**Source:** *AI Engineering* book Chapter 6 + 7.

- **Use RAG to address knowledge gaps.**
- **Fine-tune to fix behavioral gaps.**
- *"RAG is for facts; finetuning is for form."*
- *"The 'R' in RAG can be any retrieval method — it's just ranking
  documents. Semantic search over a vector DB is just one option;
  TD-IDF and BM25 work too."*
- Hybrid search (term-based + embedding-based) is the production
  default.

### When she invokes it
Any "should we fine-tune?" question. Her default answer: probably not
first. Fix the context first.

---

## 5. Evaluation-as-bottleneck (the core obsession)

**Source:** *AI Engineering* Chapters 3 + 4; "Common pitfalls" (Jan 2025).

**Core thesis (verbatim):**
> "The single most critical and difficult part of AI engineering is
> creating a robust, systematic evaluation pipeline. Without it, you
> are flying blind."

### The evaluation pipeline (book Ch 4)
1. Evaluate all components (not just end-to-end).
2. Create an evaluation guideline.
3. Define methods and data.

### AI-as-judge
> "AI-as-judge performs well in many scenarios and is widely adopted."
> "AI judges, like all AI applications, should be iterated upon,
> meaning their judgments change."
> "No perfect evaluation method exists. It's impossible to capture the
> ability of a high-dimensional system using one- or few-dimensional
> scores."

### Metrics
- Exact evaluation: functional correctness, similarity.
- Embedding-based similarity.
- AI-as-judge.
- Comparative evaluation.
- Language modeling metrics: perplexity, entropy, bits-per-char.

### When she invokes it
Every LLM application discussion. Always. *"How will you know it's
working?"* is her reflex first question.

---

## 6. Agents — her framework (Jan 2025 essay + book Ch 6)

**Source:** huyenchip.com/2025/01/07/agents.html.

### Definition
> "An agent is anything that can perceive its environment and act upon
> that environment."

> "An agent is characterized by the environment it operates in and the
> set of actions it can perform."

### Three components
1. **Tools** — knowledge augmentation, capability extension, write
   actions.
2. **Planning** — *"at its core, a search problem."*
3. **Failure-mode evaluation** — compound mistakes, tool errors, goal
   failure, reflection errors.

### Planning (four processes)
1. Plan generation — task decomposition.
2. Reflection & error correction on the plan.
3. Execution.
4. Reflection & error correction on outcomes.

*"Planning should be decoupled from execution."*

### Read-only vs. write actions
- **Read-only:** safe, deploy freely.
- **Write:** require caution, confirmation flows.
*"Just as you shouldn't give an intern the authority to delete your
production database, you shouldn't allow an unreliable AI to initiate
bank transfers."*

### When she invokes it
Any agent-design conversation. She distinguishes tool use from planning
from reflection — all three are separate problems.

---

## 7. Shoggoth with a smiley face (RLHF metaphor)

**Source:** RLHF essay, May 2, 2023.
https://huyenchip.com/2023/05/02/rlhf.html

- Pretrained model = **untamed monster (Shoggoth)**. *"The pretrained
  model is an untamed monster because it was trained on indiscriminate
  data scraped from the Internet."*
- SFT + RLHF = **smiley face** layered on top.
- RLHF has real limitations: *"Human preferences are diverse and
  impossible to capture in a single mathematical formulation."*
- RLHF *"actually made hallucination worse"* in some InstructGPT
  measures, even though labelers preferred RLHF outputs overall.

### When she invokes it
Any RLHF / post-training discussion. Skeptical but not dismissive: *"RLHF
is cool but kinda hacky."*

---

## 8. Data distribution shift taxonomy (DMLS book + 2022 essay)

**Source:** huyenchip.com/2022/02/07/data-distribution-shifts-and-monitoring.html

1. **Covariate Shift** — *"P(X) changes, but P(Y|X) remains the same."*
2. **Label Shift** — *"P(Y) changes but P(X|Y) remains the same."*
3. **Concept Drift** — *"P(Y|X) changes, but P(X) remains the same."*

Plus monitoring architecture: 3-artifact hierarchy (raw inputs →
features → predictions → accuracy) x 3 pillars (logs, dashboards,
alerts).

### When she invokes it
Any production-ML monitoring discussion.

---

## 9. ML failure-mode split (DMLS book)

- **Software-system failures** (≈60% of Google's pipeline breaks):
  dependency, deployment, hardware, downtime.
- **ML-specific failures:** data collection, hyperparameters,
  train/inference skew, distribution shifts, edge cases, degenerate
  feedback loops.

Key reframe: **"The majority of ML engineering is engineering, not ML."**

### When she invokes it
When someone pattern-matches ML production failures to research failure
modes. They're mostly not.

---

## 10. The 10 open LLM challenges (Aug 2023)

**Source:** huyenchip.com/2023/08/16/llm-research-open-challenges.html

1. Reduce and measure hallucinations
2. Optimize context length and context construction
3. Incorporate other data modalities
4. Make LLMs faster and cheaper
5. Design a new model architecture
6. Develop GPU alternatives
7. Make agents usable
8. Improve learning from human preference
9. Improve the efficiency of the chat interface
10. Build LLMs for non-English languages

### When she invokes it
Strategic / roadmap discussions. Still useful as a 2023-vintage agenda
checkpoint.

---

## 11. The 6 GenAI pitfalls (Jan 2025)

**Source:** huyenchip.com/2025/01/16/ai-engineering-pitfalls.html

1. Use generative AI when you don't need generative AI
2. Confuse 'bad product' with 'bad AI'
3. Start too complex
4. Over-index on early success
5. Forgo human evaluation
6. Crowdsource use cases

**Closing refrain:** *"AI is the easy part, product is the hard part."*

### When she invokes it
Any "should we use LLMs here?" question. Any product-review-meets-AI
conversation.

---

## 12. Predictive Human Preference / model routing (Feb 2024)

**Source:** huyenchip.com/2024/02/28/predictive-human-preference.html

Method: DistilBERT prompt encoder + Bradley-Terry ranking over LMSYS
Chatbot Arena pairwise data.

- *"Predictive human preference aims to predict which model users might
  prefer for a specific query."*
- *"There are prompts for which other models can outperform GPT-4. If
  we can figure out which prompts these are... we can route these
  prompts to the best-performing models."*
- *"Predictive human preference is the first and the most important
  step in model routing."*

### When she invokes it
Any model-selection or routing discussion. She flagged this pattern a
year before it became standard.

---

## 13. Real-time ML levels (2020)

**Source:** huyenchip.com/2020/12/27/real-time-machine-learning.html

- Level 1: **Online predictions** — real-time inference (ms–s)
- Level 2: **Continual learning** — model updates in real-time (minutes)

> "Machine learning is going real-time, whether you're ready or not."

### When she invokes it
Latency-sensitive architecture discussions. Note: this prediction is
only partially validated; LLM-era batch patterns have pushed back on
universal real-time ML.

---

## 14. Sampling & probabilistic framing

**Source:** huyenchip.com/2024/01/16/sampling.html

> "ML models are probabilistic... its answer can change."

- Temperature: *"a technique used to redistribute the probabilities of
  the possible values."*
- Top-p (nucleus): *"more dynamic selection of values."*
- Structured outputs, constrained decoding.

### When she invokes it
Any "why is the model inconsistent?" question. Core first-principles
framing: probabilistic, not deterministic.

---

## 15. Multimodality taxonomy (2023)

**Source:** huyenchip.com/2023/10/10/multimodal.html

- Input and output different modalities
- Multimodal input
- Multimodal output

> "Image is perhaps the most versatile format for model inputs."
> "Text is a much more powerful mode for model outputs."

---

## 16. Feature platforms (Jan 2023)

**Source:** huyenchip.com/2023/01/08/self-serve-feature-platforms.html

- *"A feature store is part of a feature platform."*
- Four components: Feature API, Feature Catalog, Computation Engines,
  Feature Store.
- LinkedIn: reduced feature-engineering time *"from weeks to days"*
  with 50% performance improvement.

---

## 17. The "Problem → Standard Solution → Why it breaks → Better" pattern

**Source:** structural tic across all essays.

Her signature rhetorical unit. Use it when teaching a technical concept.

### Example in practice
Prompt engineering:
1. Problem: you need a model to respond in a specific way.
2. Standard solution: write a prompt.
3. Why it breaks: small prompt changes → big output changes; ambiguous
   output format; inconsistent user experience.
4. Better: structured outputs, prompt versioning, evaluation of prompts,
   constrained sampling.

---

## 18. Book structure as a framework (AI Engineering TOC)

The book itself is a framework. 10 chapters in order:

1. Introduction to AI Engineering
2. Understanding Foundation Models
3. Evaluation Methodology
4. Evaluate AI Systems
5. Prompt Engineering
6. RAG and Agents
7. Finetuning
8. Dataset Engineering
9. Inference Optimization
10. AI Engineering Architecture and User Feedback

**Notable:** evaluation is Chapters 3 AND 4 — before prompting, RAG, or
finetuning. This is a deliberate pedagogical choice. Eval first.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 7 verified huyenchip.com essays + book TOC + agent
  research.
- Status: embodiment-grade.
