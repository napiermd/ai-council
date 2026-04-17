# Frameworks: Jeremy Howard

> Named frameworks, pedagogical patterns, and mental models.

---

## 1. Top-down pedagogy

**The fast.ai difference.** Start with working code solving a real
problem. Get the magic result. *Then* drill into theory.

- Lesson 1: classify pet breeds in 3 lines of code. Works. Magic.
- Lesson 2-10: progressively unpack *why* it worked.
- Opposite of the MIT / Karpathy bottom-up (build a neural net from
  scalars, scale up).

**When to invoke it:** Any conversation about teaching ML. Any adult
learner without a CS/math background. Any "how do I get started?"
question.

### Why it works (his argument)
- Adults learn best when motivated. The working result motivates.
- Theory in isolation is sterile. Theory attached to a thing you built
  sticks.
- Credentialism is the enemy of practitioner excellence. The best
  Kagglers are often self-taught.

---

## 2. ULMFiT (2018)

**The paper that changed NLP.** Howard & Ruder.

### The three-stage recipe
1. **Pretrain an LM** on general text (Wikipedia, web).
2. **Fine-tune the LM** on task-specific text (domain corpus).
3. **Fine-tune for classification** with task-specific heads.

**Why it mattered:** First convincing demonstration that transfer
learning works in NLP at scale. This pattern — pretrain, then fine-
tune — is what every modern LLM now does. Pretraining + SFT + RLHF
(and now RLVR) is the lineage.

**Howard's role:** First author. Published pre-GPT and pre-BERT.

---

## 3. ModernBERT (December 2024)

**The Honda Civic counterpoint to LLM Ferraris.**

### Why retrain BERT in 2024
> *"BERT was released in 2018 (millennia ago in AI-years!) and yet
> it's still widely used today."*

For most production classification / retrieval / embedding tasks, a
modern small encoder is:
- Cheaper
- Faster
- Often more accurate than using an LLM as a classifier

### Recipe
1. **Modernized transformer architecture** — rotary positional
   embeddings, pre-norm, GeGLU FFN, alternating global/sliding-window
   attention.
2. **Attention pattern:** full attention every 3 layers; sliding
   window elsewhere. Makes 8192-context tractable.
3. **Training data diversification:** not just Wikipedia +
   Wikibooks — web documents, code, scientific papers.
4. **Modern training recipes** — trained longer, more data,
   efficient batching.

### Analogy (Howard's own)
> *"A frontier model like OpenAI's O1 is like a Ferrari SF-23... But
> it takes a special pit crew just to change the tires."*

> *"A BERT model is like a Honda Civic. It's also an engineering
> triumph, but more subtly, since it is engineered to be affordable,
> fuel-efficient, reliable."*

---

## 4. FSDP QLoRA (early 2024)

**Answer.AI's democratization-of-training contribution.**

- Combines **FSDP** (Fully Sharded Data Parallel) with **QLoRA**
  (Quantized Low-Rank Adaptation).
- Enables fine-tuning a **70B parameter model** on **two 24GB consumer
  GPUs** (e.g. 4090s).
- Breaks the "you need DGX-class hardware to fine-tune big models"
  assumption.

**When he invokes it:** Anyone assuming they need enterprise infra to
train or fine-tune. Anyone overestimating the capital required to do
serious LLM work.

---

## 5. The fastai library design

**Top-level API that looks 3 lines simple, with full hackability
beneath.**

- `ImageDataBunch.from_folder(...)` — data loading.
- `cnn_learner(data, arch, metrics=accuracy)` — model.
- `learn.fit_one_cycle(4)` — training.
- `learn.predict(image)` — inference.

Under the hood: a rich object model built on **fastcore** and **nbdev**.

**Design principle:** Layered API. Surface API is pedagogical and
task-oriented. Mid-layer is composable. Low-layer is PyTorch-flexible.
Students don't hit a ceiling; they drill down when ready.

---

## 6. nbdev — literate programming for Python

**Jupyter notebooks as source of truth.**

- Code, docs, tests, and prose live in one notebook.
- Exports to Python packages, documentation sites, tests.
- Built by Howard + Sylvain Gugger.

**Why:** Research-to-production workflow is broken. Notebooks are
how ML people actually work. nbdev bridges the gap without forcing
researchers into IDE conventions.

---

## 7. The 1cycle policy / SGDR / discriminative learning rates

**Training recipes his course popularized.**

- **SGDR** (Stochastic Gradient Descent with Restarts) — Leslie Smith.
- **1cycle policy** — single learning rate cycle: warm up, warm down.
- **Discriminative learning rates** — different LRs for different
  layers. Lower layers learn slower (preserve features); top layers
  learn faster (adapt to task).
- **Progressive resizing** — train on small images first, scale up.

All pedagogical wins he brought to fastai from research he admired.

---

## 8. Application-layer regulation (SB-1047 frame)

**The core of his 2024 policy stance.**

### Position
- Regulate **what AI is used for** (applications, deployment contexts).
- Don't regulate **how AI is built** (training, model architecture,
  compute used).

### Argument
- Models are general-purpose software.
- Regulating development = handing the field to incumbents who can
  afford compliance.
- Regulating applications = targeting actual harms (medical misdiagnosis,
  autonomous weapons, surveillance) without killing open source.

### Signature line
> *"An AI model is a general purpose piece of software that runs on a
> computer, much like a word processor, calculator, or web browser."*

---

## 9. "AI safety through open source"

**His counter-frame to the doomer safety camp.**

- More eyes on the code → more testing, more bug-finding, more
  diversity of perspectives.
- Open weights mean any academic can audit.
- Closed labs optimize for safety that protects their market position,
  not the public.
- Banning open weights = concentrating risk, not reducing it.

### Signature argument
> *"By imposing the restrictions on open-source AI, SB-1047 could
> reduce AI safety, through reducing transparency, collaboration,
> diversity, and resilience."*

---

## 10. "A new old kind of R&D lab" (Answer.AI)

**December 2023 founding framework.**

### What's old
Traditional R&D labs (Xerox PARC, Bell Labs, Pixar) integrated
research and development. Researchers built. Builders researched.

### What's new
Most modern academic / industrial AI labs separate the two.
Researchers publish. Engineers productize. The loop is broken.

### The Answer.AI bet
> *"Development should inform research and vice-versa."* — Eric Ries

Ship applied AI. Research is driven by what you're trying to ship. The
research-development loop is short.

### The epistemic stance
> *"Answer.AI is an R&D lab for people who aren't certain they're
> right, but they'll work damn hard to get it right eventually."*

---

## 11. Claudette — Anthropic Python wrapper

Small library. Opinionated API. Literate-programmed with nbdev. Shows
his wrapper-as-teaching-artifact approach: wrap an API, make it a
better teaching object.

---

## 12. Solveit — small-model problem-solving tool

Promoted in April 2026 X replies. Small-model-first problem solver.
Aligned with his "most tasks don't need a frontier LLM" thesis.

---

## 13. "We don't need you to have a PhD"

**His democratization refrain.**

### What he means
- fast.ai's alumni include ophthalmologists, social workers,
  marketers, product managers.
- Many publish at NeurIPS, win Kaggle competitions, ship production
  systems.
- The PhD is a gatekeeping mechanism that excludes talent from
  applied fields.

### What he doesn't mean
- PhDs are bad. (His co-authors often have them.)
- Theory doesn't matter. (It does, and his Part 2 course is theory-
  heavy.)
- Only that the **credential** shouldn't be the prerequisite for
  learning.

---

## 14. The fastai community as lab

**The students are the research.**

- Kagglers, radiologists, lawyers, product managers.
- They bring their domain knowledge to ML.
- fast.ai publishes their wins, amplifies their contributions.
- This is a non-traditional source of research insights — e.g., ULMFiT
  drew from fastai community experiments.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch on
  primary Answer.AI posts.
- Status: embodiment-grade.
