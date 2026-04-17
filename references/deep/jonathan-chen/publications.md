# Publications: Jonathan H. Chen

> Paper corpus + tools + benchmarks.

**Google Scholar (April 2026):** h-index 47, i10-index 103, ~12,120
citations. https://scholar.google.com/citations?user=xHC1VkoAAAAJ

---

## Top-cited canonical papers

### 1. Machine Learning and Prediction in Medicine — Beyond the Peak of Inflated Expectations
**Chen JH, Asch SM. *N Engl J Med.* 2017;376(26):2507-2509.** ~1,463 citations.
DOI: 10.1056/NEJMp1702071.
URL: https://www.nejm.org/doi/10.1056/NEJMp1702071

**His foundational essay.** Verbatim:
> "Machine learning now rides atop the 'peak of inflated expectations.'"

> "Precise predictions about the distant future are often fundamentally
> impossible."

> "The relevance of clinical data decays with an effective 'half-life'
> of about 4 months."

> "No amount of algorithmic finesse or computing power can squeeze out
> information that is not present."

> "An accurate prediction of a patient outcome does not tell us what
> to do if we want to change that outcome."

> "Let's move past the hype cycle and on to the 'slope of
> enlightenment.'"

### 2. GPT-4 Diagnostic Reasoning RCT
**Goh E, Gallo R, Hom J, … Chen JH. *JAMA Netw Open.* 2024;7(10):e2440969.**
~631 citations. Chen = corresponding author.
URL: https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2825395

Design: 50 physicians, randomized GPT-4 + conventional resources vs.
conventional resources only, 6 NEJM-style vignettes.

**Striking finding:** LLM-assisted physicians NOT significantly better
(adj. diff 2 pp, P=0.60). **LLM alone scored 16 pp HIGHER than
conventional resources (P=0.03).** This is the result that cracked
Chen's decade-long "human + AI > either alone" prior.

### 3. GPT-4 Management Reasoning RCT
**Goh E, Gallo RJ, Strong E, … Chen JH. *Nat Med.* 2025;31(4):1233-1238.**
~155 citations. Chen = corresponding author.
PubMed: https://pubmed.ncbi.nlm.nih.gov/39910272/

92 physicians. **Pairing DID help** (+6.5%, CI 2.7-10.2, P<0.001). But
pairing ≈ GPT-4 alone (−0.9%, P=0.8). LLM users took +119 seconds
per case.

### 4. Wayfinding — From Predicting Diagnostic Labels to Wayfinding
**Adler-Milstein J, Chen JH, Dhaliwal G. *JAMA.* 2021;326(24):2467-2468.**
DOI: 10.1001/jama.2021.22396.
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12049696/

**His most important philosophical paper.** Diagnostic AI should not
predict final labels; it should help clinicians navigate.

Verbatim:
> "Current AI tools have not realized this potential, due in part to
> the long-standing focus of these tools on predicting final
> diagnostic labels instead of helping clinicians navigate the
> dynamic refinement process of diagnosis."

> "Wayfinding is the process of determining a current position and
> navigating a route between an origin and a destination."

> "AI tools that support the dynamic diagnostic refinement process
> should help the clinician understand where they are on the
> diagnostic pathway and help them select the paths most likely to
> reduce uncertainty."

### 5. MedAgentBench — A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents
**Jiang Y, Black KC, Geng G, Park D, Zou J, Ng AY, Chen JH.** arXiv:2501.14654.
NEJM AI 2025. Chen = senior author. Andrew Ng is ML co-author.
URL: https://arxiv.org/abs/2501.14654
GitHub: https://github.com/stanfordmlgroup/MedAgentBench

**First FHIR-compliant virtual-EHR agent benchmark.** 300 tasks, 10
categories, 100 patient profiles, 700K+ data elements. Best model
(Claude 3.5 Sonnet v2): 69.67%. Query tasks: 85.33%. Action tasks:
54.00%.

**MedAgentBench v2** (Eric Chen et al., PSB 2026): GPT-4.1 with memory
hits 98.0%; without memory 91.0%.

### 6. From Tool to Teammate — Clinician-AI Collaborative Workflows RCT
**Chen JH et al. *npj Digital Medicine.* 2026;9.** March 2026.
URL: https://www.nature.com/articles/s41746-026-02545-1

70 clinicians. AI-first 85% / AI-second 82% / Traditional 75% / AI
alone 90%. **Chen's direct response to his own 2024 JAMA Netw Open
finding:** collaborative workflows must be *designed*, not assumed.
When they are, both workflows beat traditional resources.

### 7. MedAgentBrief + MedFactEval
**Grolleau F, Alsentzer E, … Haredasht FN, Shah NH, Schulman K, Chen
JH.** arXiv:2509.05878 (2025). Biocomputing 2026.
URL: https://arxiv.org/abs/2509.05878

**Co-authored with Nigam Shah and Emily Alsentzer.** Framework for
LLM discharge summary evaluation. MedFactEval LLM Jury achieved
**κ = 0.81** agreement with 7-physician panel — non-inferior to a
single human expert (κ = 0.67, P < 0.001).

Prospective deployment (medRxiv companion): 384 discharges, 57% used
AI-generated content, 25% had omissions, 20% inaccuracies, **only 2%
hallucinations.** Physician burnout scores: 1.75 → 1.20 (P=.03).

### 8. How chatbots and large language model AI systems will reshape modern medicine — Fountain of Creativity or Pandora's Box?
**Li R, Kumar A, Chen JH. *JAMA Intern Med.* 2023;183(6):596-597.**
~127 citations.
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12049698/

Three-tier framework for LLM impact on medicine: (1) text
analysis/synthesis/documentation, (2) new care-delivery workflows,
(3) redrawing the human/AI expertise boundary. Names "confabulation"
explicitly.

### 9. Chatbot vs Medical Student Performance
**Strong E, DiGiammarino A, Weng Y, … Chen JH. *JAMA Intern Med.* 2023.**
~174 citations.
URL: https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2806980

GPT-4 scored 4.2 points higher than M1/M2 students; 93% passing rate
vs 85%. Critical finding: **confabulation** decreased with GPT-4 vs
GPT-3.5 but did not disappear.

### 10. Opioid Distribution
**Chen JH, Humphreys K, Shah NH, Lembke A. *JAMA Intern Med.* 2016;176(2):259-261.**
~190 citations. Chen first author, **Shah co-author.**
URL: https://pubmed.ncbi.nlm.nih.gov/26658497/

Top 10% of opioid prescribers account for 57% of prescriptions — but
**the same long-tail pattern holds for all drugs.** The "pill mill bad
apples" framing is wrong. Most opioid prescriptions come from the
broad base of general practitioners.

### 11. Standing on FURM Ground (with Shah)
**Callahan A, … Chen JH, … Shah NH. *NEJM Catalyst.* 2024.**
URL: https://catalyst.nejm.org/doi/abs/10.1056/CAT.24.0131

**Chen + Shah co-authorship.** Fair, Useful, Reliable evaluation
framework applied to 6 Stanford AI candidates; 2 advanced.

### 12. Diagnostic Reasoning Prompts for Interpretability
**Savage T, Nayak A, Gallo R, … Chen JH. *npj Digital Medicine.* 2024.**
~311 citations. Senior author.

Chain-of-thought-style reasoning prompts preserve LLM diagnostic
accuracy — interpretable prompting matters.

### 13. MedAlign — EHR Instruction Following
**Fleming SL, Lozano A, … Chen JH. *AAAI.* 2024.** ~130 citations.
arXiv: https://arxiv.org/html/2308.14089v2

983 natural-language instructions on EHR data, 15 clinicians across
7 specialties, 276 longitudinal EHRs. **8.3% accuracy drop going from
32K to 2K context** on GPT-4 — real evidence that long-context
matters for EHR tasks.

### 14. Real-time NGS Prediction in Live Clinical Setting
***npj Digital Medicine.* 2025;8:533.**
URL: https://www.nature.com/articles/s41746-025-01816-7

ML model predicts whether to order Heme-STAMP (expensive NGS panel)
— **AUC 0.77, comparable to expert hematologists (0.78)** —
deployed live. Embodies the HealthRex "don't order a test unless it
will change management" philosophy.

### 15. Decaying Relevance of Clinical Data
***Int J Med Inform.* 2017.** ~127 citations.

Source of the **"4-month half-life"** finding.

### 16. Explainable AI models using real-world EHR data — Systematic Scoping Review
**Payrovnaziri SN, … Chen JH. *JAMIA.* 2020.** ~391 citations.

### 17. Applications of ML in Routine Laboratory Medicine
**Rabbani N, Kim GYE, Suarez CJ, Chen JH. *Clin Biochem.* 2022.** ~140 citations.

### 18. Toward Expert-Level Medical QA with LLMs (Med-PaLM 2)
**Singhal K, Tu T, … (contributing Chen). *Nature Medicine.* 2025.**
~2,219 citations. Chen is contributing author.

---

## Tools (HealthRex Lab)

### OrderRex
**Chen's signature decision-support tool.**

Origin (verbatim):
> "Why look at just one person's chart? Why not look at the last
> thousand charts?"

> "Other doctors who ordered this CT scan also ordered this medication."

> "What if there was that kind of algorithm available to me at the
> point of care?"

> "Imagine, technology allowing medical decisions to be informed by
> the collective experience of thousands of other physicians right at
> the point-of-care."

URL: https://healthpolicy.fsi.stanford.edu/news/could-orderrex-become-amazon-medical-data

### ChatEHR
Stanford internal LLM-in-Epic tool (Shah-led, Chen contributor). See
Shah deep profile.

### GitHub: HealthRex CDSS
https://github.com/HealthRex/CDSS

---

## Benchmarks

### MedAgentBench / MedAgentBench v2
See paper #5 above. The FHIR-compliant agent benchmark.

### MedFactEval
See paper #7 above. LLM jury for clinical summaries.

### NOHARM — Numerous Options Harm Assessment for Risk in Medicine
Concept framework: measure clinical **harm**, not just accuracy.
Chen's positioning: *"The benchmark that finally measures 'clinical
harm,' not just 'accuracy.'"*

Note: formal publication citation not yet verified; the concept is
consistently attributed to Chen's public framing.

---

## Key public-framing essays

### Who's Training Whom? (NEJM AI 2024) — AAMC Fenley Writing Award, Silver 2025
His most personal piece of writing. Verbatim:
> "The chatbot was likely providing better counseling than I did in
> real life."

> "Technology is leveraged to complement, not replace, the human
> elements of medicine."

> "We, as humans, may not have as much of a monopoly on empathy and
> personal connection as we might like to imagine."

URL: https://www.aamc.org/career-development/affinity-groups/gia/awards/2025-who-s-training-whom

---

## Funding

- **NIH K01-ES026837** (2015-2020, NIEHS) — launching grant.
- **Josiah Macy Jr. Foundation** (July 2025, $200K) — AI in medical
  education.
- Additional Stanford, NIH, industry funding for HealthRex.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: Google Scholar + PubMed + Nature Medicine + NEJM AI +
  JAMA + HealthRex Lab + 2 parallel research agents.
- Status: comprehensive, primary-source-verified.
