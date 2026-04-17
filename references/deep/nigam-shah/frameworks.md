# Frameworks: Nigam Shah

> His named frameworks and recurring mental models, each with source,
> mechanics, and when he invokes them.

---

## 1. Delivery Science for AI (2020)

**Citation:** Li RC, Asch SM, Shah NH. "Developing a delivery science
for artificial intelligence in healthcare." *npj Digital Medicine* 3:107
(2020). DOI: 10.1038/s41746-020-00318-y.

**Thesis:** Building accurate ML models is not the hard part; delivering
them into care is.

**Mechanics:** AI "in practice" is not a model — it is a care-delivery
system that the model enables. The sub-discipline required to close the
gap between model accuracy and clinical value is a blend of design
thinking, process improvement, and implementation science.

**When he invokes it:** Any time someone pitches a model and skips the
question of deployment.

**Signature framing:**
> "AI delivery science will require a broader set of tools, such as
> design thinking, process improvement, and implementation science, as
> well as a broader definition of what AI will look like in practice,
> which includes not just machine learning models and their predictions,
> but also the new systems for care delivery that they enable."

---

## 2. FURM — Fair, Useful, Reliable Models (2024)

**Citation:** Callahan A, ... Shah NH. "Standing on FURM Ground: A
Framework for Evaluating Fair, Useful, and Reliable AI Models in Health
Care Systems." *NEJM Catalyst* (June 2024). DOI: 10.1056/CAT.24.0131.
ArXiv preprint: 2403.07911.

**Thesis:** Before a health system deploys an AI model, it must pass a
structured 6-step evaluation — anything less is negligence.

**The six steps:**
1. Ethical review for value mismatches.
2. Simulation-based usefulness estimation (this is the novel leg —
   powered by APLUS, below).
3. Financial projection for sustainability.
4. IT feasibility analysis.
5. Deployment strategy design.
6. Prospective monitoring plan.

**Stanford's pass rate applying FURM:** 6 candidates reviewed; 2 advanced.
That 2/6 ratio is the argument. Most "promising" AI shouldn't ship.

**When he invokes it:** The default governance framework he pushes onto
health systems. Open-source tools released for other health systems to
adopt.

**Why it matters:** Most responsible-AI frameworks stop at "fair +
reliable." Shah insists on the third, missing leg: **useful.** Useful is
measured against the workflow, the capacity to act, and the net benefit
over *not* using AI.

---

## 3. Recurring Local Validation / "All models are local" (2023)

**Citation:** Youssef A, Pencina M, Thakur A, Yang T, Peek N, Shah NH.
"External validation of AI models in health should be replaced with
recurring local validation." *Nature Medicine* 29(11):2686–2687 (2023).
DOI: 10.1038/s41591-023-02540-z.

**Thesis:** One-time external validation of clinical AI is scientifically
obsolete. Models must be locally re-validated on a continuing schedule.

**Mechanics:** Patient data drifts across time, geography, and facility.
A model validated once elsewhere provides no guarantee of performance at
your site next year. Modern ML tooling, updated regulation, and market
forces make frequent local revalidation newly feasible — so it should
become the default rather than a one-time ceremony.

**The case study he reaches for:** Epic Sepsis Model. Shipped with claimed
AUC 0.76–0.83. External validation at Michigan Medicine found AUC 0.63,
sensitivity 33%, 67% of sepsis cases missed, alerts on 18% of all
patients. For Shah, this is not an Epic failure — it's a validation
*paradigm* failure.

**When he invokes it:** Any claim that "we validated the model, so it
generalizes."

**Signature analogy:** Weather forecasting. Local, continuously
re-calibrated. Not a one-time certification.

---

## 4. MedHELM (2026)

**Citation:** Bedi S, ... Shah NH et al. "Holistic evaluation of large
language models for medical tasks with MedHELM." *Nature Medicine*
32:943–951 (2026). DOI: 10.1038/s41591-025-04151-2.

**Thesis:** USMLE-style benchmarks don't measure what clinicians actually
do. MedHELM does.

**Mechanics:** Clinician-validated taxonomy organizing medical AI into
5 categories → 22 subcategories → 121 tasks. 37 benchmarks included;
9 LLMs evaluated against 35 of them.

**Five categories:**
1. Clinical decision support
2. Clinical note generation
3. Patient communication
4. Medical research
5. Administration

**Findings:** DeepSeek R1 66% win rate on task comparisons. Claude 3.5
Sonnet achieved comparable results at ~15% lower computational cost.

**Paired companion: MedArena.** Human-preference battleground where real
clinicians compare LLM outputs on their own queries. As of November
2025, only ~33% of clinician queries resembled factual-recall tasks —
the implicit case against USMLE-style evaluation.

**When he invokes it:** LLM evaluation discussions. MedHELM is his
replacement for the MedQA/USMLE benchmark culture.

**Signature limit:** Even MedHELM evaluates only single responses — not
multi-turn conversations. He has said this publicly (DistilINFO, March
2026).

---

## 5. Green Button (2014) → Atropos Health

**Citations:**
- Longhurst CA, Harrington RA, Shah NH. "A 'Green Button' for using
  aggregate patient data at the point of care." *Health Affairs*
  33(7):1229-1235 (July 2014).
- Gombar S, ... Shah NH. "It is time to learn from patients like mine."
  *npj Digital Medicine* 2:16 (2019).
- Callahan A, ... Shah NH. "Using Aggregate Patient Data at the Bedside
  via an On-Demand Consultation Service." *NEJM Catalyst* (2021).

**Thesis:** Every bedside clinician hits situations where guidelines
don't answer the question in front of them. The right response is not
"randomize a trial." It is "tell me what happened to the last 500
patients like this one, at this institution, in the last three years."

**Mechanics:** A specialty-consultation service architecture, not an
algorithm. A physician triggers a question; the service queries
longitudinal EHR aggregates; evidence returns within a day (down from
nine months in historical IRB-mediated processes).

**Productized by Atropos Health.** Shah co-founded. Atropos now operates
this as a commercial on-demand consult service ("Prognostogram") and
has a "massive library of questions already asked and answered," enabling
proactive surfacing of matching evidence alongside a clinical note.

**When he invokes it:** Any time someone treats RCT-as-only-evidence as
the default; any time someone dismisses real-world evidence; any time
someone questions Atropos.

**Signature framing:**
> "Medicine is one of the few industries that doesn't learn from how it
> served its past customers."

---

## 6. Clinical Environment Simulator (CES, 2025)

**Thesis:** Static benchmarks miss the operational realism of medicine.
CES evaluates clinical LLMs within digital hospital environments where
every decision dynamically alters future states.

**What it enables:**
1. Temporal reasoning under evolving constraints.
2. Resource-aware decision-making.
3. Operational resilience through adversarial testing.

**When he invokes it:** Discussion of LLM benchmarking realism, especially
when someone points to MedHELM's single-response limit.

---

## 7. MedAlign (2023)

**Lead:** Fleming SL, ... Shah NH.

**Thesis:** A clinician-generated instruction-tuning dataset for LLM
medical tasks, to counter the dominance of synthetic-clinical datasets
that don't reflect what clinicians actually ask.

---

## 8. EHRSHOT + CLMBR-T-base (2023)

**Citation:** Wornow M, Thapa R, Steinberg E, Fries J, Shah NH. "EHRSHOT:
An EHR Benchmark for Few-Shot Evaluation of Foundation Models." NeurIPS
2023 spotlight. arXiv:2307.02028.

**Shipped:**
- **CLMBR-T-base** — 141M parameter foundation model pretrained on 2.57M
  patients' structured EHR data.
- **6,739-patient longitudinal dataset.**
- **15 few-shot clinical prediction tasks.**

**Thesis:** Foundation models for medicine need longitudinal, not
ICU-only (vs MIMIC), data.

---

## 9. MINIMAR — Minimum Information for Medical AI Reporting (2020)

**Citation:** Hernandez-Boussard, Bozkurt, Ioannidis, Shah. *JAMIA* 2020.
~422 citations.

**Thesis:** Every clinical decision-support AI needs a minimum set of
reporting metadata. A compliance floor for clinical AI reporting.

---

## 10. Model Facts Labels (2020)

**Citation:** Sendak, ... Shah. *npj Digital Medicine* 2020.

**Thesis:** FDA-drug-facts-style labels for AI models, presented to
bedside clinicians. Tells them "how, when, how not, and when not" to use
the model.

**Cross-reference:** Shah's "nutrition label" analogy from the STAT op-ed
(March 2022) is the rhetorical version of this framework.

---

## 11. APLUS — simulation framework (referenced in FURM)

**Thesis:** Operationalizes "usefulness" as a simulated quantity — the
novel second leg of FURM. Simulates the integration of a model into
workflow to quantify expected clinical utility.

---

## 12. DEPLOYR (deployment framework)

**Thesis:** Technical framework for real-time deployment of
research-created models into EHR systems with clinical-trigger-based
inference.

---

## Non-named frameworks / reflex heuristics

### The quartet interrogation template
Whenever an AI-in-medicine proposal is in the room, mentally run:
1. What workflow?
2. What action?
3. What net benefit?
4. At which site?
5. Validated when?

### The "better, faster, safer, cheaper" deployment test
> "In deployment, AI ought to be better, faster, safer, and cheaper.
> Otherwise it is useless."
> — Stanford HAI, 2022.

### The 5-question LLM checklist (LinkedIn 2023)
Before using LLMs for any medical or healthcare task:
1. What training data, and was it representative?
2. What biases are known?
3. How will we evaluate in deployment (not benchmarks)?
4. Does benchmark performance predict real-world clinical value?
5. What is the strategy for factual errors?

### The number-needed-to-benefit framing
From JAMA 2019 "Making Machine Learning Models Clinically Useful" (with
Milstein and Bagley): evaluate utility in context of the *range of
clinical decisions available*, their *cost and efficacy*, and *patient
adherence probability*. Plants decision-curve analysis in clinical ML
thinking.

### Silent deployment / silent trials
Running a model in the background to observe performance before go-live.

### The ripple-effects frame
> "Building and integrating an algorithm into any workflow will have
> ripple effects that are beyond just what the algorithm does."
> — Stanford Medicine, March 2022.

### The hybrid construct
> "What we should be asking and evaluating is the hybrid construct of
> the human plus this technology."
> — STAT News, April 2023.

### The bolt-on vs. AI-native distinction
> "You can only be a native if you began when the thing was around. If
> a company has already existed for 20 years and is now adding AI —
> that's a bolt-on."
> — TechTarget, November 2025.

### The assurance-labs architecture
From JAMA 2024: federated public-private network, shared standards,
nationwide registry. Distributed, not centralized — politically and
practically distinctive.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: peer-reviewed papers + press releases + direct WebFetch
  verification.
- Status: hand-authored, primary-source-backed where cited.
