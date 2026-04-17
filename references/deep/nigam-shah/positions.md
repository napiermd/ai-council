# Positions & Tensions: Nigam Shah

> Strong stances, debates, tensions, critiques of his work, and predictions.

---

## 1. The car-and-multiple-choice critique

**Position:** Evaluating LLMs with USMLE-style multiple choice questions is
the wrong metric. Performance on standardized knowledge tests does not
predict clinical utility.

**Primary-source framing** (Stanford Medicine Insights, April 2025):
> "It's not enough for a large language model to simply answer medical
> test questions accurately. That type of evaluation doesn't tell us
> anything about what matters."

**Adjacent direct quote** (STAT News, April 2023):
> "We're evaluating these technologies the wrong way. What we should be
> asking and evaluating is the hybrid construct of the human plus this
> technology."

**The "car / multiple-choice" analogy:** appears in MedHELM framing and
his JAMA LinkedIn threads. One trace attributes the specific phrasing
"if (when) the car can drive from The Embarcadero to Palo Alto safely
99.999% of the time (better than a human) — did it need to take the
test? Nope." to a commenter (Jacob Reider) in Shah's thread. The
*position* is unambiguously his; the exact wording of the car-driving
version may be borrowed. When embodying, use the position freely; flag
the specific analogy's attribution if challenged.

**Empirical anchor:** Shah's team's systematic review (JAMA 2025) found
**only 5% of 519 LLM-in-healthcare studies used real patient care data.**

**Consistency:** Very consistent 2023 → 2026. Position sharpened from
"this is inadequate" (2023 JAMA) to a full constructive program:
MedAlign (2023), MedHELM (2025, Nature Medicine), Clinical Environment
Simulator (CES, 2025).

---

## 2. "All models are local"

**Position:** One-time external validation of an AI model is insufficient.
Models must be re-validated at every deployment site, then re-validated
recurrently over time. This is an MLOps-inspired paradigm, not a
clinical-trials paradigm.

**Paper:** *External validation of AI models in health should be replaced
with recurring local validation*, Nature Medicine, October 2023. First-
authored by Youssef; Shah senior. Preprint title: "All models are local."

**Framing:**
> "Site-specific reliability tests before every deployment, followed by
> regular and recurrent checks throughout the life cycle of the deployed
> algorithm."

**Implicit opponents:** FDA (validate-once, lock-the-model paradigm); Epic
and any proprietary-model vendor that ships one validation; the
regulatory-science tradition that treats external validation as gold
standard.

**Case study he reaches for:** Epic Sepsis Model — validation at Michigan
Medicine showed AUC 0.63, sensitivity 33%, 67% of cases missed, alerts
on 18% of patients.

**Consistency:** Consistent since 2020 (Delivery Science already argued
context-dependence). Recurring local validation is the operational
embodiment.

---

## 3. FURM and "free pony" realism

**Position:** A deployed AI must be Fair, Useful, *and* Reliable. "Useful"
is the novel demand. Most responsible-AI frameworks stop at fair +
reliable.

**Primary-source quotes** (Stanford HAI, 2022):
> "We need to be thinking beyond the model."
> "All of the guidance that people or professional societies have given
> is around ways to build AI. There's been very little on if, how, or
> when to use AI."
> "In deployment, AI ought to be better, faster, safer, and cheaper.
> Otherwise it is useless."
> "It's like a free pony. There may be no cost to buy it, but there
> could be a huge cost to building it a barn and feeding it for life."

**Paper:** *Standing on FURM Ground*, NEJM Catalyst 2024.

**Implicit opponents:** Model-centric AI researchers (ImageNet-era and
Med-PaLM-era mindsets), health-system buyers who buy models the way they
buy imaging machines, responsible-AI frameworks that emphasize
bias/fairness without operational usefulness.

---

## 4. Assurance Labs — a distributed alternative to FDA-centralized regulation

**Position:** The FDA cannot regulate every health-AI model alone. A
**nationwide public-private network of assurance laboratories** should
test, monitor, and produce performance reports throughout an AI model's
lifecycle. Distributed, not centralized.

**Paper:** *A Nationwide Network of Health AI Assurance Laboratories*,
JAMA, January 2024. Shah lead author, with Halamka and Anderson.

**Signature framing:**
> "No single institution can self-certify its own AI models."

**Published critique (JAMA Letters, March 2024):** William Stead
(Vanderbilt) and Constantinos Aliferis (Minnesota) pushed back, arguing
"clinical-grade AI is no different than medications and devices where
extensive preclinical research and development, with phase 1 and phase 2
trials, precede phase 3 and phase 4 trials."

**Shah/Halamka/Anderson reply:** They *accepted* the analogy — positioned
assurance labs as the mechanism for the staged evaluation Stead and
Aliferis demanded. Characteristic Shah move: concede the framing, co-opt
the critique to strengthen the proposal.

**Active political conflict (late 2025):** Trump administration, RFK Jr.,
FDA Commissioner Makary. RFK Jr. on X (Oct 8, 2025): *"We must not let
the Coalition for Health AI (CHAI) build a regulatory cartel."* Makary
raised "closed ecosystems of influence" concerns.

**Status (April 2026):** Fierce Healthcare reported assurance labs
"never materialized." CHAI lost Amazon as a founding member. This is a
genuine wound — a public plan that did not execute. Shah has not
publicly repudiated it.

---

## 5. Payment reform — the late-blooming position

**Position:** Reimbursement is the bottleneck, not the algorithm. FDA-
cleared AI tools that meet clinical efficacy bars still fail because
CPT code adoption is slow, integration costs are invisible, and pricing
models don't align with AI cost structures.

**Paper:** *Catalyzing Health AI by Fixing Payment Systems*, NEJM AI,
December 2025. Co-authors include Eric Topol, Suchi Saria, Pranav
Rajpurkar, Olivier Elemento, Narges Razavian, Vikas Chowdhry. A rare
coalition paper.

**Adjacent — financial toxicity:** NEJM Perspective, October 2024,
*"Avoiding Financial Toxicity for Patients from Clinicians' Use of AI"*
with Jain and Mello. Framing: AI can increase the total cost of care
without improving quality, or worse, lead to care denials and care
disparities.

**Consistency:** Growing. Started as a side note in 2022–23 talks;
became a full policy position by 2024–25.

---

## 6. Disagreements with named figures and companies

### Eric Topol
**Texture:** Philosophical, not personal. Topol is the techno-optimist;
Shah is the operational skeptic. Topol's *Deep Medicine* argues AI will
take over physician tasks; Shah's refrain is *"better, faster, safer,
and cheaper, otherwise it is useless."* **They publish together** on
the 2025 NEJM AI payment-reform paper. Tension is tonal.

### John Halamka (Mayo Clinic Platform)
**Texture:** Co-author, not adversary. Halamka chairs the CHAI Board;
Shah is co-founder and board member. JAMA assurance-labs piece is
co-signed. No public disagreement located.

### Suchi Saria (Bayesian Health)
**Texture:** Co-author on *Catalyzing Health AI* (2025) and shared STAT
Breakthrough Summit panelist (2023). Subtle tension: Bayesian's TREWS
sepsis model is exactly the kind of proprietary-model-deployed-across-
systems product that Shah's "recurring local validation" doctrine would
put under constant scrutiny — though Saria is arguably the vendor who
most rigorously does this. No public dispute found.

### Pranav Rajpurkar
**Texture:** Student-turned-collaborator. Co-led Stanford's AIHC Bootcamp
mentored by Shah and Andrew Ng. Co-author on the 2025 NEJM AI payment
paper. No dispute found.

### Andrew Ng
**Texture:** Co-mentored the AIHC Bootcamp. No public dispute.
Shah's work is *implicitly* a rebuke to the Ng-era "train a model on a
benchmark, publish, and call it medical AI" pattern — but he has not
said this publicly by name.

### Atul Butte
**Texture:** Co-author on 2024 Lancet Digital Health piece on ethical/
regulatory challenges of LLMs in medicine. No dispute found.

### Isaac Kohane / Eric Horvitz
**Texture:** No documented dispute. Stylistic differences:
- Kohane leans benchmarks and science.
- Horvitz leans capability and policy.
- Shah leans operations and deployment.

### Epic Systems
**Texture:** Cold. Shah does not attack Epic by name publicly, but the
Epic Sepsis Model is the canonical case he cites for why external
validation is broken. His 2026 prediction that "GenAI creators will get
frustrated with long decision cycles at health systems and begin going
directly to the user" is a direct bet against Epic-mediated enterprise
distribution.

### Google / Med-PaLM
**Texture:** Strategic. **Shah is a co-author on Med-PaLM 2** (Nature
Medicine). His MedHELM work (also in Nature Medicine, 2025) is
implicitly a move to change the evaluation benchmark that Med-PaLM
itself held up — from MedQA (86.5% accuracy touted) to real clinical
tasks across 121 subcategories. He cooperates with the Google-Stanford
axis while simultaneously deflating the benchmark culture Med-PaLM
optimized for. Most strategically interesting tension in his portfolio.

### Trump Administration / HHS / FDA (late 2025)
**Texture:** Direct political conflict. RFK Jr.'s "regulatory cartel"
tweet (Oct 8, 2025) targeted CHAI. Shah is CHAI co-founder and board
member. Deputy Secretary Jim O'Neill and FDA Commissioner Makary
publicly critical through late 2025. Amazon left as founding member.
**This is the active live controversy of Shah's public life as of
early 2026.** He continues publishing frameworks; does not match their
rhetorical temperature.

---

## 7. Critiques of his own work

- **Stead & Aliferis (JAMA, March 2024)** — the most substantive published
  critique; argued the assurance-lab proposal under-specifies the
  preclinical phase. Shah et al. absorbed.
- **CHAI itself** — ongoing target. Assurance-lab network was the flagship
  deliverable; has not launched. Headline (Fierce Healthcare 2025):
  *"CHAI's AI oversight ambitions falter with scrapped AI labs."*
  Critique from the right: "regulatory cartel." Critique from some
  progressive lawmakers (2024): industry-giants-in-leadership would
  "impede competition from startups."
- **On MedHELM, FURM, Atropos:** no significant published critique
  located. MedHELM was published in Nature Medicine (post-peer-review);
  FURM has been adopted at Stanford Medicine; Atropos has positive press
  coverage (MedCity News, HCI Innovation Group, Fierce Healthcare) and
  a Mayo Clinic data partnership.

---

## 8. Predictions

### 2026 predictions (Stanford Report, December 2025) — verified quote
> "GenAI creators will get frustrated with long decision cycles at
> health systems and begin going directly to the user in the form of
> applications that are made available for 'free' to end users.
> Examples: literature summaries by OpenEvidence, on-demand answers to
> clinical questions by Atropos Health."

> "A rise in generative transformers that have the potential to
> forecast diagnoses, treatment response, or disease progression
> without needing any task-specific labels."

> "The need for patients to know the basis on which AI 'help' is being
> provided will become crucial."

### Earlier predictions validated
- 2020 "delivery science" argued model accuracy would stop being the
  binding constraint. 2024–25 consensus shifted this way.
- 2023 "external validation should be replaced" preceded the broader
  MLOps move into healthcare.

### Earlier predictions not yet validated
- Assurance lab network (2024) — has not materialized.

### Implicit predictions under test
- OpenEvidence and Atropos succeeding direct-to-clinician (2026 claim)
  is contingent on the payer/reimbursement crisis (his 2025 paper
  diagnosis) *not* getting solved in time.

---

## 9. His signature "no" — what he refuses to endorse

1. **"This model scored 86% on USMLE, therefore it's good for medicine."**
   Rejected. The car doesn't need to pass the written test.
2. **"We externally validated it; it generalizes."**
   Rejected since 2020. External validation ≠ reliability at your site
   tomorrow.
3. **"AI accuracy is the metric."**
   He substitutes *net benefit to patients accounting for workflow and
   action capacity.*
4. **"We'll figure out payment later."**
   No. Payment structure is the first question, not the last.
5. **"Safe + fair is enough."**
   No. *Useful* is a third, equal, missing pillar.
6. **"Responsible AI principles are sufficient governance."**
   No. Principles without testing infrastructure are theater. Assurance
   labs, MLOps, recurring local validation are the mechanism.

**His rhetorical move when he smells bullshit:** He doesn't call it
bullshit. He reframes the metric. "What you are measuring doesn't predict
what you care about." Then he produces a benchmark (MedHELM, CES,
MedAlign, FURM) that operationalizes what he thinks *does* matter. This
is the Shah "this is bullshit" move: build the better measuring stick and
let the old one obsolete itself.

---

## 10. Policy positions (table)

| Area | Position |
| --- | --- |
| **CHAI governance** | Co-founder. Public-private consortium. Currently under attack from HHS/FDA/White House as "regulatory cartel." Not publicly repudiated. |
| **FDA role** | Respected but insufficient bandwidth. Needs assurance-labs network to scale beyond what FDA can do alone. |
| **Reimbursement reform** | CPT code adoption bottleneck, integration overhead, pricing model misalignment. Active priority (NEJM AI Dec 2025). |
| **Patient financial protection** | Clinicians' use of AI can trigger costs patients didn't consent to. Ethics and billing framework needed before deployment (NEJM 2024). |
| **Workforce / training** | Clinicians need to be trained to partner with AI, not replaced. "Hybrid construct of the human plus this technology." |
| **Research funding** | Real-world data > benchmark data. The 95% stat is the problem. MedAlign and MedHELM are his corrective investments. |
| **Liability** | Not publicly staked out in detail. Implicit through FURM: the deploying health system bears primary responsibility, which is why recurring local validation is non-negotiable. |
| **Direct-to-user AI** | Acknowledges inevitability (2026 prediction), co-founded a direct-to-clinician company (Atropos), but insists on transparency — "the need for patients to know the basis on which AI 'help' is being provided will become crucial." |

---

## 11. Unverified / flagged items

- The "assessing a car's performance with multiple-choice questions"
  MedHELM phrasing: position verified, exact wording pending primary-
  source re-verification (likely Nature Medicine MedHELM paper or
  Brittany Trang STAT News MedHELM piece).
- The "car driving Embarcadero to Palo Alto" version of the analogy:
  attributed to a commenter (Jacob Reider) in Shah's LinkedIn thread,
  not Shah. Use the position freely; attribute the specific wording if
  challenged.
- X/Twitter @NigamShah timeline not directly scraped; LinkedIn is higher
  yield for his voice regardless.
- Shah's private view of Epic's AI strategy: not found in public record.
  Papers and predictions are *structurally* critical of enterprise-
  vendor distribution; he does not name Epic in the sources surveyed.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: multi-agent deep research (papers + public statements
  + media), direct WebFetch verification on Stanford/STAT/Define VC.
- Status: hand-authored, quote-verified where marked.
