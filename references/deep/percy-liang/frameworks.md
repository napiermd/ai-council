# Frameworks: Percy Liang

> Named frameworks and methodological commitments. Each anchored
> to a specific paper, blog post, or verbatim quote.

---

## 1. HELM (Holistic Evaluation of Language Models)

**His flagship evaluation contribution.** First author. TMLR 2023.
arXiv:2211.09110.

### Seven metrics, every scenario
1. **Accuracy**
2. **Calibration**
3. **Robustness**
4. **Fairness**
5. **Bias**
6. **Toxicity**
7. **Efficiency**

### Scope
- **16 core scenarios** (7 metrics applied 87.5% of the time)
- **42 total scenarios** with 7 targeted evaluations across 26
  targeted scenarios
- **30 prominent language models** evaluated
- Cross-model scenario coverage lifted from 17.9% → 96.0%
- **25 top-level findings** surfaced

### Framing
> *"We intend for HELM to be a living benchmark for the community,
> continuously updated."*

### HELM ecosystem
- **HELM Classic** — original 2022 leaderboard
- **HELM Capabilities** — curated capability scenarios (March 2025)
- **HELM Safety** — safety-specific properties and risks
- **HELM Long Context** — long-context evaluation (September 2025)
- **MedHELM** — clinical / medical tasks (May 2025)
- **VHELM** — vision-language models
- **HEIM** — Holistic Evaluation of Text-to-Image Models
- **Holistic Evaluation of Audio-Language Models**
- **AIR-Bench** — AI risk categorization
- **ToRR** — Table Reasoning and Robustness (vision-language)
- **Enterprise Benchmark** — enterprise-specific use cases
- **HELM Lite** — simplified leaderboard subset

### When he invokes it
Any single-metric benchmark claim. Any model comparison. Any
evaluation-methodology debate.

---

## 2. Foundation Models — the term itself

**His naming contribution to the field.** Bommasani, ..., Liang et
al. 2021. arXiv:2108.07258.

### Verbatim definition
> *"Models trained on broad data at scale such that they can be
> adapted to a wide range of downstream tasks."*

### Why it matters
Before 2021: "language model," "large model," "pretrained model"
were all used interchangeably. The term "foundation model" was
chosen deliberately to mark a category distinction — these models
are a base layer that others build on.

### His defense of the framing (verbatim)
> *"'Foundation model' illustrates that we're not building the
> whole stack. We're building the foundation. You can't move into
> a house if you don't have the rest of the house, but once you
> have a strong foundation, the house is much easier to build."*

### Cultural footprint
The term stuck. CRFM is named around it. Five years later it is
load-bearing across academia, industry, and policy.

---

## 3. Foundation Model Transparency Index (FMTI)

**His institutional accountability contribution.**

- Launched October 2023; updates 2024, 2025
- **100 transparency indicators**
- 2023 avg score: 37/100; Meta top at 54
- 2024 avg: 58
- **2025 avg: 40 (declined year-over-year)** — IBM top 95, xAI
  bottom 14. arXiv:2512.10169
- Co-authors: Bommasani, Kapoor, Maslej, Longpre, Xiong, Wan,
  Klyman, **Liang**

### Argument
> *"Without transparency, there is no accountability."*

### The year-over-year trend is his evidence
That the industry is regressing on transparency absent a
regulatory floor.

---

## 4. "Open-weight ≠ Open-source" distinction

**His insistence on linguistic precision.**

### Definitions
- **Open-weight** = model weights released; training data, code,
  failures not
- **Open-source** = reproducible end-to-end; code, data, and
  ideally failures all public

> *"Models like Llama 3, Mixtral are 'open-weight models', not
> 'open-source models'."*

### Why it matters
- Fine-tuning open-weight models without training data risks
  catastrophic forgetting
- "Open source" claims from labs that don't release data are
  category errors
- The distinction shapes regulatory, academic, and procurement
  conversations

---

## 5. Marin — "open development"

**His newest named framework.** Launched May 19, 2025.

### What "open development" means beyond open-source
- **Preregistered experiments** on GitHub
- **Public failures** — not just successes
- **GitHub-contributable research** — anyone can suggest /
  contribute
- **Lead:** David Hall; Liang oversees
- **Funders:** Google, Open Athena, Schmidt Sciences

### Proof point
**Marin 32B Base ("mantis")** — October 29, 2025:
> *"It is the best open-source base model (beating OLMo 2 32B
> Base) and it's even close to the best comparably-sized open-
> weight base models, Gemma 3 27B PT and Qwen 2.5 32B Base."*

### Scaling-law preregistration (February 2026)
1e22 FLOP trained; 1e23 FLOP loss **preregistered on GitHub** —
falsifiable, public prediction. A category-defining move for
research culture.

---

## 6. Third-party evaluation with legal safe harbor

**His policy proposal for evaluation infrastructure.**

ICML 2025 position paper — *"Position: In-House Evaluation Is Not
Enough. Towards Robust Third-Party Evaluation and Flaw Disclosure
for General-Purpose AI."* arXiv:2503.16861.

### Core thesis
> *"Legally protected third-party evaluation and coordinated flaw
> disclosure are essential to safe AI systems."*

### Proposed infrastructure
- Bug-bounty-style flaw disclosure for AI models
- Legal safe harbors for red-teamers and independent evaluators
- Coordinated disclosure timelines, not ad-hoc
- Required because in-house evaluation is structurally conflicted

---

## 7. "Turn on the headlights, make a map, then steer"

**His three-part framing for AI research posture.**

> *"Turn on the headlights (improve transparency), make a map to
> see where we are (perform evaluations), and ensure that we are
> steering in the right direction."*

### Operational mapping
- **Headlights** = FMTI, disclosure requirements
- **Map** = HELM, holistic evaluation, AutoBencher
- **Steering** = policy, governance, Marin-style open development

---

## 8. System 1 / System 2 framing for foundation models

**His cognitive-architecture framing for where LMs fit and where
they fall short.**

> *"Foundation models as serving a bit like a System 1. They're
> really good at quickly arriving at some sort of gut reaction."*

> *"You really would like a System 2 that could do the rational
> thing."*

### Implication
LMs are not wrong to be "System 1"-like — they are good at it.
The gap is pairing them with System 2 verification, reasoning, and
grounding. This is part of his broader "tools, not goal posts"
framing.

---

## 9. "Leaky abstraction" for large models

**His theoretical framing for why robustness guarantees are hard.**

> *"I'm very pessimistic about kind of having completely robust
> guarantees on large models, just because they're kind of a leaky
> abstraction."*

### Implication
- Formal verification is likely impossible at scale
- Empirical evaluation is the only feasible path
- Monitoring and control matter more than certification

---

## 10. AutoBencher (ICLR 2025)

**His response to benchmark saturation.**

Auto-generates **22%-harder** datasets than existing benchmarks.
Treats benchmark design itself as a machine-learning problem.

### Standing prediction
Benchmarks have ~2-year half-lives before saturation. HELM Classic
→ HELM Lite → AutoBencher is the dated evidence.

---

## 11. CodaLab Worksheets

**His research-reproducibility infrastructure.**

- Provenance-tracked experiments
- Precedes modern ML reproducibility tooling
- Reflects his foundational commitment: if it cannot be reproduced,
  it cannot be evaluated, and if it cannot be evaluated, it cannot
  be trusted.

---

## 12. CS336: Language Models from Scratch

**His teaching contribution to academic capability.**

Students implement a modern LM pipeline end-to-end — tokenizer,
architecture, training, evaluation — as a Stanford graduate course.

### Framing (verbatim)
> *"Researchers are becoming detached from the technical details
> of how LMs work. In CS336, we try to fix that by having students
> build everything."*

### Implication
Academic labs must retain hands-on LM-building capability, or
they lose the right to critique industry.

---

## 13. Marginal-risk framing for policy

**His analytical contribution to open-weight regulation debates.**

### Core argument
Regulating open-weight models should not be based on worst-case
speculation or absolute-risk framings. The relevant question is:
*does releasing this model's weights increase risk **marginally**
beyond what already exists in the ecosystem?*

### Evidence
> *"So far, there's little compelling evidence that open foundation
> models increase the marginal risk."*

### Policy implication
> *"Ensure the continued open release of foundation models absent
> evidence of marginal risk."*

The default should be open; the burden is on the regulator to show
marginal risk.

---

## 14. Ecosystem Graphs

**His supply-chain documentation framework.**

Documents the FM landscape: which models inherit from which, which
data came from where, which labs depend on which compute
providers. An institutional response to opaque AI supply chains.

---

## 15. Nutrition-label / spec-sheet metaphor

**His accessible framing for transparency requirements.**

> *"We need a nutrition label or a spec sheet for these objects
> that we're selling or people are buying and using."*

### When he invokes it
Any conversation with a non-technical audience about disclosure
requirements. Any regulatory / procurement discussion.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: HELM paper + FMTI papers + Marin announcement +
  ICML 2025 position paper + 3 research agents.
- Status: comprehensive; each framework anchored to a specific
  paper, post, or verbatim quote.
