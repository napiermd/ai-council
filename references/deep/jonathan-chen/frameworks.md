# Frameworks: Jonathan H. Chen

> Named frameworks, methodological commitments, and benchmarks.

---

## 1. Prospective evaluation > retrospective benchmarks

**Chen's methodological signature.** The field has too many papers
with retrospective test sets. He runs randomized controlled trials.

### The archetype
**"GPT-4 assistance for improvement of physician performance on
patient care tasks: a randomized controlled trial"** — Nature Medicine,
April 2025. PubMed: 39910272.

- 92 practicing physicians.
- Randomized: GPT-4 + conventional resources vs. conventional resources
  alone.
- 5 expert-developed clinical vignettes based on real patient cases.
- Primary outcome scoring by expert rubrics.
- **Finding:** +6.5% improvement, 95% CI 2.7–10.2, P<0.001.
- **Striking secondary finding:** GPT-4 alone scored similarly to
  physician + GPT-4. (−0.9%, 95% CI −9.0 to 7.2, P=0.8.)
- **Tradeoff:** LLM users required +119 seconds per case on average.

### Why it matters
This is the framework. Clinical AI evaluation belongs in prospective
trials, not retrospective benchmarks.

---

## 2. MedAgentBench — "A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents"

**Source:** https://arxiv.org/abs/2501.14654 + https://stanfordmlgroup.github.io/projects/medagentbench/
**NEJM AI:** https://ai.nejm.org/doi/abs/10.1056/AIdbp2500144
**GitHub:** https://github.com/stanfordmlgroup/MedAgentBench

### The design
- **300 patient-specific clinically-derived tasks** (10 categories)
- **100 realistic patient profiles**, 700K+ data elements
- **FHIR-compliant interactive environment** — not just question-
  answering
- **Agent capabilities tested:** retrieve from EHR → reason → take
  action (orders, medications)
- **Accompanying codebase**

### Chen's framing (paraphrased from Stanford HAI coverage)
> "AI agents can do things" — meaning they could theoretically
> directly retrieve patient information from the EHR, reason, and
> take action by entering orders for tests and medications.

### Results
- **Original release:** best model Claude 3.5 Sonnet v2: **69.67%**
  success rate.
- **MedAgentBench v2** (Eric Chen et al., PSB 2026):
  - **91.0%** success without memory
  - **98.0%** success with memory
  - Using GPT-4.1 as base model

### Why it matters
The gap from 70% → 98% is enormous on a benchmark designed to reflect
real EHR agent tasks. The gap from 98% → production-safe is where the
hard research lives.

---

## 3. NOHARM — No-Observed Harm Annotation for Review of Medicine

Framework for classifying clinical harm in LLM outputs during
evaluation. Chen is co-author.

### Why it matters
Most evaluation treats "wrong answer" as a binary. Clinical harm is
not binary — a missed mild finding is different from a contraindicated
medication recommendation. NOHARM gives evaluators a structured way
to surface high-stakes errors.

---

## 4. The continuously learning health system

**Source:** HealthRex Lab homepage + Chen's broader research
framing.

### The vision
Every patient encounter generates data. Every data point refines the
model. The refined model comes back to the next bedside as clinical
decision support.

### Intellectual lineage
- **Larry Weed** (Problem-Oriented Medical Record — SOAP note inventor)
- **David Eddy** (founder of evidence-based medicine; argued medicine
  operates on informal clinical judgment that could be systematized)
- **IOM Roundtable on the Learning Healthcare System**
- Modern ML + EHR data as the substrate that finally makes it possible

### Chen's contribution
Operationalize it. Build the tools (decision support), run the trials
(evaluation), train the next generation (medical AI education at
Stanford).

---

## 5. "Collective experience of the many"

**Source:** HealthRex Lab homepage.

### The premise
Clinicians individually hold tacit knowledge from thousands of
patient encounters. That knowledge doesn't diffuse well.
Informatics can surface the collective pattern and deliver it back
to the next physician seeing the next patient.

### Operationalized
- EHR data mining + machine learning to surface **latent knowledge**
- Delivered back as **clinical decision support**
- Measured prospectively (see #1)

---

## 6. The hybrid construct (shared with Shah)

> "The hybrid construct of the human plus this technology."
> (phrasing from Shah; Chen operates within the same frame)

### Chen's RCT interpretation
- +6.5% for physician + GPT-4 over physician alone: **hybrid works**
- −0.9% for physician + GPT-4 vs. GPT-4 alone: **not a simple story**
- Resist spinning. Let the data be ambiguous.

---

## 7. The action-authority question

**Chen's signature interrogation move.** When shown an agentic
clinical AI:
1. *What's the action authority?* (Can it order tests? Medications?)
2. *Who verifies?* (Physician in the loop? Retrospective audit?)
3. *What happens when it's wrong?* (Error rate, harm profile, recovery.)

### Why it matters
MedAgentBench's 30% failure rate on the original release is not just
a benchmark stat — it's a reminder of what "agentic" costs when you
hand over authority.

---

## 8. Workflow realism — "What happens at 3am?"

**Chen's bedside lens.**

### The questions
- Cognitive load at 3am on a complex patient
- Handoff patterns across shifts
- Alert fatigue — what does another alert cost?
- Documentation burden — is the scribe helping or flattening reasoning?
- Does the AI surface errors that weren't in the prior workflow?
- Does the clinician actually read the AI output before signing?

### Why it matters
He's a practicing internist. These aren't abstract — he sees them.
When he pushes back on a proposed AI tool, it's with a specific
clinical scenario in mind.

---

## 9. Ambient documentation as high-yield near-term

Chen's pragmatic take: among clinical AI applications in 2024-2026,
**ambient scribes and documentation tools are the highest-yield,
lowest-harm deployments**. They reduce real, measurable physician
burden. He's published on the evaluation infrastructure for these.

---

## 10. Harm classification as its own research problem

Not a sidebar. Not a throw-in. **Harm evaluation deserves its own
methodology.** NOHARM is the operationalization.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: HealthRex + papers + Stanford HAI coverage.
- Status: embodiment-grade.
