# Frameworks: Danielle Bitterman

> Named frameworks and methodological commitments.

---

## 1. TRIPOD-LLM (Nature Medicine 2025)

**Her flagship contribution.** Reporting standard for LLM medical
studies.

**Citation:** Gallifant J, Bitterman DS, et al. "The TRIPOD-LLM
reporting guideline for studies using large language models." *Nature
Medicine* 2025;31:60-69.

### Structure
- **19 main items + 50 subitems** from title through discussion
- **Modular format** accommodating various research designs
- **14 main items + 32 subitems** apply across all categories
- Extension of **TRIPOD + AI** statement for LLM-specific concerns

### Why it matters
> "Large language models (LLMs) are rapidly being adopted in
> healthcare, necessitating standardized reporting guidelines."

The unique LLM failure modes (hallucinations, omissions, reliability,
explainability, reproducibility, privacy, bias propagation) weren't
covered by existing frameworks. TRIPOD-LLM fills the gap.

### Emphasis
- **Transparency** — open methodology, code, evaluation data where
  possible
- **Human oversight** — how humans review / correct LLM outputs
- **Task-specific performance reporting** — not aggregate benchmark
  scores

### Development
- **Delphi process** — expedited
- **Expert consensus** with multi-institutional authors
- **Living document** — will evolve with the field
- **Interactive website** — https://tripod-llm.vercel.app/ for
  completion and PDF generation

### When she invokes it
Any time a clinical LLM paper, deployment evaluation, or regulatory
discussion comes up. This is her floor-raising move for the field.

---

## 2. Clinical-grade evaluation

**Her term of art.** What "clinical grade" actually requires — and it
has to be **earned, not claimed.**

### Minimum criteria
- **Real clinical data**, not benchmark proxies
- **Clinician-annotated ground truth** at scale (12,999 sentences
  across 18 configurations = the existence proof)
- **Hallucination severity stratification**, not just rate
- **Human oversight design** as first-class
- **Adversarial testing** — fabricated inputs, malicious prompts
- **Reporting per TRIPOD-LLM**

### When she invokes it
Any vendor claim, any pre-deployment conversation, any accuracy-only
framing.

---

## 3. Hallucination severity > hallucination rate

**Her operational counterpoint to accuracy-first framings.**

### The methodology
**"A framework to assess clinical safety and hallucination rates of
LLMs for medical text summarisation"** (npj Digital Medicine 2025):

- **18 experimental configurations**
- **12,999 clinician-annotated sentences**
- **Hallucination rate: 1.47%**
- **Omission rate: 3.45%**

### Distinction that matters
- Hallucination = added false content
- Omission = missing true content
- **Different clinical consequences.** Omission can be worse.
- **Severity stratification** matters more than raw rate — a 1%
  hallucination rate that produces wrong drug interactions is
  different from a 1% hallucination rate that produces irrelevant
  social-history details.

### When she invokes it
Any LLM summarization or document-generation discussion. Any "we
achieved X% accuracy" claim.

---

## 4. Adversarial hallucination attacks

**"Multi-model assurance analysis showing large language models are
highly vulnerable to adversarial hallucination attacks during clinical
decision support"** (Communications Medicine 2025).

### The finding
- **Six leading LLMs**
- **300 doctor-designed clinical vignettes** each containing a single
  fake lab value, sign, or disease
- Models **repeat or elaborate on planted error up to 83% of cases**
- **Mitigation prompt halves the rate but does not eliminate it**

### The implication
Your LLM is not robust to dictation typos, transcription errors, or
malicious inputs that look plausible. You need adversarial evaluation
as standard practice, not an afterthought.

### When she invokes it
Any clinical-LLM deployment discussion. Any input-sanitization
conversation. Any "we trained on real data" claim.

---

## 5. Data poisoning in medical LLMs

**"Medical large language models are vulnerable to data-poisoning
attacks"** (Nature Medicine 2024/2025).

### The thesis
Public web corpora used in pretraining contain medical misinformation.
Targeted poisoning of even a tiny fraction can induce specific
clinical errors.

### Implication for practitioners
- You cannot trust "trained on a big medical corpus" as a safety
  guarantee
- Evaluation must include resistance to known poisoning vectors
- Disclosure of training data provenance matters

---

## 6. Foundation model evaluation, alignment, and oversight

Lab research area #1. The umbrella frame for her work.

### Three legs
1. **Evaluation** — clinician-annotated ground truth, severity
   stratification, reproducibility
2. **Alignment** — does the model's behavior match clinical intent?
   Not just instruction-following — *clinical*-instruction-following.
3. **Oversight** — human-in-the-loop design, sampling-based QA,
   rollback pathways

---

## 7. Oncology information extraction

Lab research area #2. Domain-specific NLP pipelines for cancer EHR
data. Stake-increasing because oncology decisions are high-stakes and
highly detail-dependent.

---

## 8. Patient-facing oncology AI (with caution)

Lab research area #3. Personalized educational materials for cancer
patients. Her position: patient-facing is higher-stakes than
physician-facing; requires heavier evaluation and trials.

---

## 9. Translational AI + clinical evaluation

Lab research area #4. Actual clinical studies, not just retrospective
evaluation. Bridges research to deployment.

---

## 10. Reporting-standards-first culture

**The broader intellectual move.** The field matures when reporting
matures. TRIPOD for classical ML. TRIPOD+AI. TRIPOD-LLM. The path is
clear: you raise the floor of what gets published, which raises the
floor of what gets deployed.

### Implicit argument
- Academic journals as levers
- Reporting guidelines as sneakier-than-regulation policy
- EQUATOR Network cataloging as cultural infrastructure

---

## 11. Safety-first evaluation culture

Her framing across all outputs. Before you deploy, you evaluate.
Before you evaluate, you define harm. Before you define harm, you
ask: *what would change management?*

This pairs with Chen's "does it change what I do at 3am?" and Shah's
"what's the operational metric?" — three complementary clinician-
operator framings.

---

## 12. Oncology specificity

Radiation oncology is high-stakes + detail-oriented. Treatment-intent
reasoning, contouring, dosimetry, staging nuance — all of these are
sensitive to small errors. Her clinical grounding means she asks
oncology-specific evaluation questions, not generic ones.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: bittermanlab.org + TRIPOD-LLM + hallucination-rates +
  adversarial-attacks papers.
- Status: embodiment-grade.
