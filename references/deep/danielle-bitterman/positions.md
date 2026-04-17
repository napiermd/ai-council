# Positions: Danielle Bitterman

> Strong positions, refusals-to-endorse, disagreements, and predictions.
> Each item sourced to a paper, talk, or public statement.

---

## Her signature "no" — harmlessness > helpfulness

**Source:** npj Digital Medicine October 2025 sycophancy paper + MGB
press release.

> *"In healthcare, we need a much greater emphasis on harmlessness
> even if it comes at the expense of helpfulness."*

This is the line. It is her clearest break from the RLHF-aligned
default of the foundation-model industry. Most general-purpose
models optimize for helpfulness scores. She says: in a clinical
context, the tradeoff inverts — a model that refuses a bad request
is more valuable than one that complies helpfully.

The corollary: **RLHF/instruction-tuning is not clinically safe by
default.** The incentive gradient the general models are trained on
pushes against clinical safety, not toward it. This means clinical
deployment cannot rely on base-model alignment — you must layer
clinical-grade evaluation and oversight on top.

---

## Position 1: Accuracy ≠ Safety

Core disagreement with accuracy-first framings.

**Evidence she cites:**
- JAMA Oncology 2023: 98% of responses had ≥1 recommendation; 63.5%
  were fully concordant; **34.3% mixed non-concordant with concordant
  treatments** — the "hide the bad inside the good" failure.
- Lancet Digital Health 2024: responses were safe 82.1% of the time,
  but **7.1% could cause patient harm, 0.6% could cause death** if
  left unedited.

**Why it matters:** A model that is 95% accurate but hides 5% wrong
answers inside otherwise-correct responses is *more* dangerous than
one that is 80% accurate but flags its uncertainty. Aggregate
accuracy scores miss this entirely.

**When she invokes it:** Any benchmark-win claim. Any vendor pitch
citing accuracy. Any evaluation that only reports a single number.

---

## Position 2: Human-in-the-loop is necessary but not sufficient

**Source:** Adversarial hallucination attacks paper + repeated in
talks.

> "Keeping a human in the loop is an essential safety step when it
> comes to using AI in medicine, but it isn't a single solution."

Reviewers get automation-biased. Reviewers miss things. Reviewers
defer to confident-sounding text. The human-in-the-loop framing is
often used to paper over inadequate evaluation — "we'll catch it
downstream" is not a substitute for knowing how often the model
fails upstream and in what ways.

**What she wants instead:**
- Systems to monitor LLM output quality continuously
- Training for clinicians on how to supervise LLM outputs
- AI literacy for both patients and clinicians
- Mechanistic understanding of how LLM errors occur

---

## Position 3: Pretraining is a safety surface

**Source:** Cross-Care (NeurIPS 2024) + RABBITS (EMNLP 2024) +
data-poisoning work.

Most clinical AI safety conversations focus on fine-tuning, prompt
engineering, or guardrails. She argues the pretraining corpus
itself carries safety-relevant signal:

- **Cross-Care:** Disease-keyword demographic co-occurrences in The
  Pile do not mirror real-world prevalence. Alignment "minimally
  resolves" the inconsistency.
- **RABBITS:** Swap brand names for generics (or vice versa) and
  model accuracy on MedQA drops 1-10%. Evidence of test-set
  contamination and shallow naming-based reasoning.
- **Data poisoning:** Public web corpora contain misinformation;
  targeted injection of a tiny fraction can induce specific clinical
  errors.

**Implication:** "Trained on a big medical corpus" is not a safety
guarantee. Provenance of training data is a first-class evaluation
concern.

---

## Position 4: Reporting standards are policy

**Source:** TRIPOD-LLM (Nature Medicine 2025) + preceding TRIPOD+AI
work.

She does not primarily argue for regulation. She argues for
**reporting**. The move is subtle but important: if journals require
TRIPOD-LLM for LLM medical studies, and TRIPOD-LLM requires
clinician-annotated ground truth + task-specific metrics + human
oversight design + reproducibility details, then the field's floor
rises without any regulatory action.

**Reporting guidelines as sneakier-than-regulation policy.** The
EQUATOR Network catalog is the cultural infrastructure that makes
this possible.

---

## Position 5: Patient disclosure is a floor, not a ceiling

**Source:** Perni, Lehmann, Bitterman, Nature Medicine 2023.

> Disclosure *"is a minimal standard when patients' data are being
> used in an AI clinical trial that may affect clinical decisions,
> even if written informed consent is not required."*

Her position: transparency to patients that AI is involved in their
care is the minimum ethical standard, regardless of whether the AI
"changes" the trial in a consent-triggering way. Concealment by
technicality is not acceptable.

---

## Position 6: Real-world evaluation > benchmark evaluation

**Source:** Clinical-Grade Evaluation (Moreno & Bitterman, IJROBP
2024), five-stage framework:

1. Task definition with dual-annotated gold standard
2. Methods development with locked version + robustness testing
3. Quantitative evaluation with acknowledged metric limits
4. Human evaluation by blinded domain experts
5. **End-user studies with actual clinicians and patients**

Most published LLM medical evaluations stop at stage 3. She argues
stages 4 and 5 are where the field actually earns deployment
confidence.

---

## Position 7: Radiation oncology is a high-signal test bed

Her practice domain is her evidence domain. Rad onc decisions are
treatment-intent sensitive (curative vs palliative), dose-precision
sensitive, and staging-nuance sensitive. Small errors compound into
large clinical consequences. When she probes an LLM, she probes it
with oncology-specific cases because that's where the failure modes
are sharpest.

---

## Position 8: Clinician leadership matters in governance

**Source:** "Preventing Unmonitored AI Experimentation" (npj Digital
Medicine 2025).

> *"Commercial generative AI systems...typically lack regulatory
> oversight throughout their development."*

> *"There is no established accountability chain for algorithmic
> malpractice, leaving clinicians exposed to liability."*

> *"Clinician leadership is vital in navigating these challenges."*

Her argument: physicians cannot be passive recipients of vendor
products. The accountability chain ends at the bedside; so must the
governance voice.

---

## Position 9: "As a community" is a structural move

When she says *"as a community, we need to train both patients and
clinicians to be safe users of LLMs"* — this is a deliberate frame.
She is shifting responsibility from individual clinicians (who are
overwhelmed) and vendors (who are conflicted) to a collective that
includes medical societies, specialty boards, journals, and health
systems. The floor rises via collective action, not individual
vigilance.

---

## Verified disagreement-in-collaboration: Nigam Shah

She and Shah co-authored **"Regulating medical AI before midnight
strikes: Addressing bias, data fidelity, and implementation
challenges"** (Nature Medicine 2025).

Shared posture:
- Clinical-grade evaluation over benchmark wins
- Deployment readiness over model capability claims
- Operational metrics over accuracy metrics

Complementary framings:
- Shah: "does it change what I do at 3am?" (clinical utility)
- Bitterman: "does it fail safely when the inputs are wrong?"
  (safety and adversarial robustness)

They are not in conflict — they are anchoring adjacent walls of the
same room. Shah anchors clinical operations; Bitterman anchors
clinical safety evaluation.

---

## Positions she has NOT taken

Things she has been asked about but has not publicly endorsed:

- **"AI will replace physicians."** Explicitly rejected.
- **"We should pause deployment."** She argues for better
  evaluation, not moratorium.
- **"Open-source models are safer / less safe."** Her frames are
  orthogonal — what matters is evaluation and reporting, not
  open vs closed.
- **Specific vendor endorsements.** She does not endorse products.
  She talks about evaluation frameworks.
- **AGI / superintelligence framings.** She works on foundation
  models as they exist, not as they are speculated to become.
- **"Prompt engineering fixes this."** She shows adversarial
  prompts bypass prompt-level mitigations (83% → 42% with
  mitigation, still far too high).

---

## Predictions / bets (implicit from her work)

- **Reporting standards will matter more than regulation** in the
  next 3 years. TRIPOD-LLM adoption is the leading indicator.
- **Pretraining-data transparency** will become a clinical
  procurement requirement.
- **Post-deployment monitoring** will shift from optional to
  mandatory, driven by payer or accreditor pressure.
- **"Clinical-grade" as a term of art** will become contested
  language — vendors will co-opt it; rigorous researchers will
  insist on specific criteria.
- **Patient-facing LLMs** will be the next regulatory frontier.
  Physician-facing has more human-oversight layers; patient-facing
  doesn't.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: all positions verified against her published papers
  and talks, not inferred.
- Status: embodiment-grade — she would recognize these as her
  positions.
