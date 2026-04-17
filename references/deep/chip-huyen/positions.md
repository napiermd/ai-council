# Positions & Debates: Chip Huyen

> Strong stances, public tensions, predictions, and the signature "no."

---

## 1. Evaluation — her anchor obsession

### The Lamppost Problem (LinkedIn essay, 2024)

Her most quotable public provocation:

> *"The most popular enterprise AI applications today aren't the ones
> that solve the most important problems or make the most money. The
> most popular applications are the ones that are easiest to evaluate."*
> — LinkedIn activity 7190717542858907648, 2024.

Her blunt version:

> *"Open-ended evaluation is the biggest bottleneck to AI adoption."*

### AI Engineering book (2025)
> *"The single most critical and difficult part of AI engineering is
> creating a robust, systematic evaluation pipeline. Without it, you
> are flying blind."*

> *"Developing evaluations has received little systematic attention
> compared to developing algorithms."*

### GenAI Platform essay (2024)
> *"Evaluation is necessary at every step of the development process."*

### When she invokes it
Every LLM application discussion. Always. First question: *"How will
you know it's working?"*

---

## 2. Human eval vs. AI-as-judge

**Source:** "Common pitfalls when building generative AI applications"
(Jan 2025).

> *"A common pitfall is forgoing human evaluation to rely entirely on
> AI judges. The teams with the best products I've seen all have human
> evaluation."*

> *"AI judges must be evaluated and iterated over time, just like all
> other AI applications."*

Operational prescription: daily manual review of 30–1000 examples. AI
judges must be correlated against human scores continually.

### Position
AI-as-judge is **legitimate and widely adopted** when used correctly
— but it does not replace human evaluation; it augments it.

---

## 3. RAG vs. Finetuning

**Her signature one-liner** (from *AI Engineering* Ch. 7):

> *"Fine-tuning is for form, while RAG is for facts."*

### Her progressive workflow
1. Prompt engineering
2. Few-shot examples (up to ~50)
3. RAG
4. Fine-tuning (last resort)

### On fine-tuning specifically
Framed as *"a significant technical and organisational investment that
should be approached as a last resort, not a first solution."*

**Why not fine-tune first:**
- Hosting/maintenance complexity.
- Model churn obsoletes fine-tunes fast.
- Usually the problem is knowledge, not form.
- You need evaluation infrastructure to verify improvement — most
  teams don't have it.

---

## 4. Agents — capability decomposition

**Source:** "Agents" essay (Jan 7, 2025), *AI Engineering* book Ch. 6.

### Definition
> *"An agent is anything that can perceive its environment and act upon
> that environment."*

### Her capability formula
Agent capability = **tool inventory** × **planning strength**.

### Compound mistakes
> *"With 95% accuracy per step, accuracy drops to 60% over 10 steps
> and 0.6% over 100 steps."*

### Canonical failure mode
> *"The agent is convinced that it's accomplished a task when it
> hasn't."*

Example: assigns only 40 of 50 people to hotel rooms, reports success.

### On LeCun's "auto-regressive LLMs can't plan"
She **cites** the position but **counters** it, suggesting the problem
may be lack of tooling rather than intrinsic incapacity.

### When she invokes it
Any agent-design conversation. She is neither an agent-maximalist nor a
skeptic — she's an evaluator.

---

## 5. RLHF — "cool but kinda hacky"

**Source:** "RLHF: Reinforcement Learning from Human Feedback" (May 2,
2023) + 10 open challenges post (Aug 2023).

### Headline
> *"RLHF, Reinforcement Learning from Human Preference, is cool but
> kinda hacky."*

### Empirical framing
> *"Empirically, RLHF improves performance significantly compared to
> SFT alone. However, I haven't seen an argument that I find foolproof."*

### Counterintuitive finding
> *"RLHF actually made hallucination worse."* (InstructGPT experiments.)

> *"Even though RLHF caused worse hallucination, it improved other
> aspects, and overall, human labelers prefer RLHF model over SFT
> alone model."*

### The labeling problem
> *"Getting different labelers to give consistent scores for the same
> response turns out to be quite difficult."*

> *"Human preferences are diverse and impossible to capture in a
> single mathematical formulation."*

### The metaphor
**Shoggoth with a smiley face.** Pretrained monster + SFT/RLHF polish.

---

## 6. Model size / scaling — NOT a scaling maximalist

Her emphasis is on **inference cost, routing, and adaptation**, not on
training ever-larger models.

### From Predictive Human Preference (2024)
> *"With more and more models being developed, each with different
> capabilities and a cost structure, model routing has clear economic
> values."*

> *"There are prompts for which other models can outperform GPT-4."*

> *"Predictive human preference is the first and the most important
> step in model routing."*

### Her thesis
Stop asking *"which model is best overall?"* — ask *"which model is
best for THIS prompt?"*

She was a year early on the model-routing pattern.

---

## 7. MLOps vs. LLMOps / AI Engineering

**Her explicit distinction** (Pragmatic Engineer interview, Feb 2025):

> *"AI engineering differs from ML engineering in that it's less about
> model development, and more about adapting and evaluating models."*

> *"ML knowledge is no longer a must-have for building AI applications."*

### Her structural metaphor
> *"Context construction for foundation models is equivalent to feature
> engineering for classical ML models."*

### The workflow inversion
> *"Start with building the product first, and only invest in data and
> models once the product shows promise."*

Foundation models invert the ML-engineering data-first order.

---

## 8. Prompt engineering — real engineering

**Source:** *AI Engineering* book + LLM engineering blog.

### Her position
> *"The problem is not with prompt engineering. It's a real and useful
> skill to have."*

> *"Prompt experiments should be conducted with the same rigor as any
> ML experiment."*

### The core failure mode
> *"If someone accidentally changes a prompt, it will still run but
> give very different outputs."*

> *"Small changes to a prompt can lead to very different results. It's
> essential to version and track the performance of each prompt."*

---

## 9. Synthetic data — measured, not ideological

**Source:** *AI Engineering* book + TWIML podcast.

> Best results come from *"a careful mix of high-quality human data and
> targeted synthetic data."*

- Attribution/licensing is the hardest unsolved operational problem.
- She references **LIMA** ("Less Is More for Alignment") — 1,000
  curated examples — approvingly.
- *"A small amount of high-quality data can outperform a large amount
  of noisy data."* (AI Engineering)

Core elements of dataset engineering: **quality, coverage, quantity.**

---

## 10. Hiring ML engineers

**Her most-cited hiring claim** (MLOps guide, June 2020):

> *"If you have to choose between engineering and ML, choose
> engineering."*

> *"It's easier for great engineers to pick up ML knowledge, but it's
> a lot harder for ML experts to become great engineers."*

> *"In traditional SWE, coding is the hard part, whereas in ML, coding
> is a small part of the battle. For ML, applications developed with
> the most/best data win."*

### On interviews
> *"A candidate who claims to work with convolutional neural networks
> (CNNs) and fails to answer a question about convolutions is going to
> be evaluated differently from a candidate who doesn't work with CNNs
> at all."*

Claims must align with demonstrated knowledge.

### What she values
- SQL and JavaScript are underrated.
- Better to be *"really good at one language than someone mediocre at
  multiple languages."*
- Transferable skills — design thinking, asking the right questions,
  communication — over specific frameworks.

---

## 11. Data quality — the Brockman quote

Attributed approvingly in *AI Engineering*:

> *"Manual inspection of data has probably the highest value-to-prestige
> ratio of any activity in machine learning."* (Greg Brockman, quoted
> by Huyen)

She uses this line repeatedly. It is her shorthand for "look at your
data before you do anything else."

---

## 12. Production LLM failure modes

**Source:** "Building LLM applications for production" (April 2023).

### Her canonical line
> *"It's easy to make something cool with LLMs, but very hard to make
> something production-ready with them."*

### Specific failure modes she enumerates
- **Ambiguous output format** — downstream expects structure.
- **Stochasticity** — *"LLMs are stochastic – there's no guarantee
  that an LLM will give you the same output for the same input every
  time."*
- **Cost at scale** — *"The cost of LLMOps is in inference."* At
  DoorDash-scale 10B predictions/day, $0.004/prediction = *"$40 million
  a day!"*
- **API unreliability** — *"APIs are very unreliable, and no commitment
  yet on when SLAs will be provided."*
- **Composability gap** — *"All tasks produce correct results but the
  overall solution is incorrect."*
- **Hallucination** as #1 production blocker per enterprise conversations.

### Orchestration caveat
> *"While it's tempting to jump straight to an orchestration tool when
> starting a project, start building your application without one
> first."*

---

## 13. Common pitfalls in GenAI apps (her consolidated 2025 list)

**Source:** huyenchip.com/2025/01/16/ai-engineering-pitfalls.html

1. **Not everything is a nail.** *"Generative AI isn't an exception —
   its seemingly limitless capabilities only exacerbate the tendency
   to use generative AI for everything."*
2. **"The hard part is user experience (UX)."** Confusing bad product
   with bad AI.
3. **Over-engineering.** *"Incorporating external tools too early can
   cause 2 problems: Abstract away critical details, making it hard to
   understand and debug your system. Introduce unnecessary bugs."*
4. **Over-indexing on early success.** *"It's easy to build a demo, but
   hard to build a product."*
5. **Forgoing human evaluation** (see §2).
6. **Crowdsourcing use cases.** *"Without an overall strategy that
   considers the big picture, it's easy to get sidetracked into a
   series of small, low-impact applications."*

### Closing refrain
> *"AI is the easy part, product is the hard part."*

---

## 14. Infrastructure abstraction

**Source:** "Why data scientists shouldn't need to know Kubernetes"
(Sep 2021).

> *"I became a data scientist because I wanted to spend more time with
> data, not with spinning up AWS instances, writing Dockerfiles,
> scheduling/scaling clusters, or debugging YAML configuration files."*

> *"You shouldn't be expected to be full-stack to become a data
> scientist."*

### Position
Infrastructure complexity should be abstracted so ML engineers can
focus on ML engineering. Pushes back on the "you must be full-stack"
narrative.

---

## 15. Open-source AI landscape

**Source:** "What I learned from looking at 900 most popular open
source AI tools" (March 2024).

### Findings
- 2023 was the year of application and application-development layer
  growth.
- 20 accounts host 23% of repos.
- **Applications started by individuals, on average, have gained more
  stars than applications started by organizations.**
- 18.8% of popular repos gained no new stars in 24 hours — most die fast.
- A distinct WeChat/Mandarin/RNN sub-ecosystem in China is an
  under-reported story.

---

## 16. Multimodality

**Source:** "Multimodality and Large Multimodal Models (LMMs)"
(Oct 2023).

> *"Little doubt that multimodal systems in general, and LMMs in
> particular, will be even more impactful than large language models."*

> *"Image is perhaps the most versatile format for model inputs."*

> *"Text is a much more powerful mode for model outputs."*

Video-as-images critique: treating video as *"sequences of images"* is
*"a severe limitation"* — ignores sound.

---

## 17. Distribution shifts / monitoring (from DMLS + 2022 post)

> *"ML systems often fail silently."*

> *"A large percentage of what might look like data shifts on
> monitoring dashboards are caused by internal errors."*

> *"60 out of 96 failures happened due to causes not directly related
> to ML."*

> *"Feature distributions shift all the time, and most of these changes
> are benign."*

Retraining decisions too often *"based on gut feelings instead of
experimental data."*

---

## 18. Disagreements / tensions with named figures

| Figure | Texture | Notes |
|---|---|---|
| **Simon Willison** | **Mild terminological tension** | On her Jan 2025 Agents post, Willison endorsed her definition and planning section ("particularly strong"), but has said elsewhere the term *"agent"* is a distraction — wished her post was titled *"LLMs with tool use."* Terminological, not substantive. |
| **Yann LeCun** | Cites his "LLMs can't plan" position, counters it | She suggests the problem may be tooling, not intrinsic model incapacity. Polite disagreement. |
| **Andrej Karpathy** | No direct interaction surfaced | Complementary in spirit. Neither dunks on the other. |
| **Jeremy Howard** | Distant, no direct interaction | Shared fast.ai / Full Stack Deep Learning adjacency. |
| **Harrison Chase (LangChain)** | **No direct attack surfaced.** | Her "start without an orchestrator" advice is general, not LangChain-specific. She has never publicly attacked LangChain by name. Treat her stance as orchestration-framework-caution generally. |
| **Sebastian Raschka** | **Mutual respect** | She endorsed his *Machine Learning Q and AI*: *"He can go deep into any theoretical topics... If you're starting your journey into machine learning, Sebastian is your guide."* |
| **Eugene Yan** | **Close collaboration** | Co-panel at NVIDIA GTC 2025. Aligned on evaluation. |
| **Hamel Husain + Shreya Shankar** | **Close eval-community alignment** | They co-teach eval; Huyen's eval obsession aligns tightly. |
| **Andrew Ng** | No direct interaction | Distant. |
| **Swyx (Latent Space)** | Aligned but no podcast appearance | Swyx coined "AI Engineer"; Huyen wrote the book. Swyx endorsed her book: *"the definitive segue into AI Engineering from one of the greats of ML Engineering."* No direct Latent Space podcast episode — notable gap. |
| **Gergely Orosz (Pragmatic Engineer)** | Collaboration | Extended newsletter interview + follow-up "AI Engineering Stack" piece. |
| **Sam Charrington (TWIML)** | Repeat guest | Multiple episodes, long relationship. |

---

## 19. Predictions (with dates)

| Date | Prediction | Source | Status |
|---|---|---|---|
| Dec 2020 | Real-time ML is inevitable | huyenchip.com/real-time | Partially validated — latency-tolerant LLM era has pushed back on universal real-time |
| Oct 2023 | Multimodality > text LLMs in impact | multimodal post | In progress — GPT-4V, Gemini, video models trending this way |
| Feb 2024 | Model routing becomes economically necessary | predictive-human-preference | Validated — routing is now standard |
| Mar 2024 | Infra layer lags application layer | 900 OSS tools | Validated — margin compression in infra |
| Jan 2025 | Agents + foundation models vs. RL agents will converge | agents post | Early — emerging pattern |
| Jan 2025 | Function calling with wide tool sets becomes universal | agents post | Validated — now standard |

---

## 20. Her signature "no"

Things she refuses to endorse:

1. **"Use AI for everything."** *"Not everything is a nail."*
2. **AI-judge-only evaluation.** Must include human eval.
3. **Fine-tuning as a first move.** Last resort.
4. **Data scientists must be full-stack.** Infrastructure should be
   abstracted.
5. **Premature orchestration.** Start without one first.
6. **Dashboards without ground truth.** Silent failures make monitoring
   decorative without outcome measurement.
7. **Interview-hack books.** Her ML Interviews book rejects this
   framing.
8. **Framework bloat** (general, not any specific framework).
9. **"Bigger model = better."** Route to the best model per prompt.
10. **Pure structural completeness over human preference.** She
    emphasizes labeler preference and downstream metric over theoretical
    optimality.

### Her rhetorical move when she smells hype
She does not dunk. She reframes the problem to an unglamorous layer:
**evaluation, data quality, cache, UX.** When everyone is excited about
a new thing, she asks for numbers.

---

## 21. Self-quantified humility

**X post, July 2025** (status 1947335669879345334):

> *"I'm slowly beginning to accept that my productivity, when working
> with AI coding agents, is limited by my human brain. AI can do many
> tasks in parallel, but I can only track the context of a few, so I
> only run a few tasks at a time. I am the bottleneck."*

This line — *"I am the bottleneck"* — is her signature self-effacing
admission. Echoes Karpathy's "remove yourself as the bottleneck"
thesis but frames it as an honest limitation, not an optimization goal.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch + last30days.
- Status: embodiment-grade; primary-source verified where marked.
