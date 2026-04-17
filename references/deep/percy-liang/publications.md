# Publications: Percy Liang

> Verified from his Google Scholar profile (`pouyVyUAAAAJ`) on
> 2026-04-17.

**Scholar summary (April 17, 2026):**
- **Total citations:** 138,781
- **h-index:** 137 all-time (124 since 2021)
- **i10-index:** 332 all-time (307 since 2021)

Top-tier academic-AI citation footprint.

---

## Top-cited canonical papers

### 1. SQuAD — "100,000+ Questions for Machine Comprehension of Text" (EMNLP 2016)

**Authors:** Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, **Percy
Liang** (senior / last author).

- **arXiv:** 1606.05250 (June 16, 2016)
- **Citations:** **11,508** — his most-cited paper
- **Role:** senior advisor / faculty PI
- **Contribution:** 100,000+ crowd-sourced reading-comprehension
  questions over Wikipedia. Logistic-regression baseline F1 51.0%
  vs. human F1 86.8%. Defining pre-LLM NLP benchmark.

### 2. "On the Opportunities and Risks of Foundation Models" (arXiv 2021)

**Authors:** Rishi Bommasani, Drew A. Hudson, ..., Liang (senior
author), 114+ authors total.

- **arXiv:** 2108.07258 (August 16, 2021; revised July 12, 2022)
- **Citations:** **9,425**
- **Role:** Founding director co-organizing the manuscript, senior
  author
- **Contribution:** **Coined the term "foundation model"** —
  verbatim: *"models trained on broad data at scale such that they
  can be adapted to a wide range of downstream tasks."* This is
  the defining vocabulary act of the CRFM.

### 3. Prefix-Tuning (ACL 2021)

**Authors:** Xiang Lisa Li, **Liang** (senior author).

- **Citations:** **6,814**
- **Role:** Senior author
- **Contribution:** Foundational parameter-efficient fine-tuning
  (PEFT) method — optimizes a small continuous prefix vector to
  adapt a frozen LM to tasks. Precursor / sibling to LoRA.

### 4. "Emergent Abilities of Large Language Models" (TMLR 2022)

**Authors:** Jason Wei et al., Liang co-author.

- **Citations:** **5,149**
- **Role:** Co-author
- The signature paper on scale-driven capability jumps.

### 5. "Generative Agents: Interactive Simulacra of Human Behavior" (UIST 2023)

**Authors:** Joon Sung Park, Joseph O'Brien, Carrie J. Cai, Meredith
Ringel Morris, **Liang** (co-author), Michael S. Bernstein.

- **Citations:** **5,019**
- **Role:** Co-author
- The "Smallville" agent simulation paper that launched the
  character-agent / multi-agent simulation wave.

### 6. "Understanding Black-Box Predictions via Influence Functions" (ICML 2017 — Best Paper)

**Authors:** Pang Wei Koh, **Percy Liang**.

- **Citations:** **4,510**
- **Role:** Senior author
- **ICML Best Paper Award.** Influence functions applied to modern
  deep networks for interpretability / data attribution.

### 7. "Know What You Don't Know: Unanswerable Questions for SQuAD" — SQuAD 2.0 (ACL 2018)

**Authors:** Pranav Rajpurkar, Robin Jia, **Liang** (senior author).

- **Citations:** **3,997**
- **Role:** Senior author
- **Contribution:** SQuAD 2.0 added adversarial unanswerable
  questions, forcing models to know when to abstain — a precursor
  to calibration / "I don't know" framings.

### 8. Lost in the Middle — "How Language Models Use Long Contexts" (TACL 2024)

**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape,
Michele Bevilacqua, Fabio Petroni, **Percy Liang**.

- **arXiv:** 2307.03172 (July 6, 2023)
- **Citations:** **3,877**
- **Role:** Senior author
- **Contribution:** Identified the **U-shaped performance curve** —
  models perform best when relevant info is at the beginning or
  end of the context and degrade significantly when it is in the
  middle. One of the most operationally influential empirical
  papers of 2023.

### 9. Stanford Alpaca (CRFM blog + GitHub, March 13, 2023)

**Authors:** Rohan Taori, Ishaan Gulrajani, Tianyi Zhang, Yann
Dubois, Xuechen Li, Carlos Guestrin, **Percy Liang**, Tatsunori B.
Hashimoto.

- **Citations:** **3,707**
- **Role:** Co-senior (with Hashimoto)
- **Contribution:** LLaMA-7B fine-tuned on 52K self-instruct
  demonstrations from text-davinci-003. Fine-tune cost <$100 on
  8×A100; data gen <$500. Qualitatively matches text-davinci-003.
- Academic-only release — catalyst for the open instruction-
  tuning wave.

### 10. HELM — "Holistic Evaluation of Language Models" (TMLR 2023)

**Authors:** **Percy Liang (first author)**, Rishi Bommasani, Tony
Lee, Dimitris Tsipras, Dilara Soylu, et al. (50 authors incl.
Chris Manning, Chris Ré, Tatsu Hashimoto).

- **arXiv:** 2211.09110 (November 16, 2022; v2 October 1, 2023)
- **Role:** **First author** — his flagship evaluation contribution
- **Verbatim from the abstract:** *"We measure 7 metrics (accuracy,
  calibration, robustness, fairness, bias, toxicity, and
  efficiency) for each of 16 core scenarios when possible (87.5%
  of the time)."*
- **Scope:** 30 prominent language models on 42 scenarios. Lifted
  cross-model scenario coverage from 17.9% → 96.0%. Surfaced 25
  top-level findings.
- **Framing:** *"We intend for HELM to be a living benchmark for
  the community, continuously updated."*

### 11. Distributionally Robust Neural Networks for Group Shifts (2019)

**Authors:** Shiori Sagawa, Pang Wei Koh, Tatsunori Hashimoto,
**Liang** (senior author).

- **Citations:** **2,770**
- **Contribution:** The group DRO framework for training models
  that minimize worst-case group risk — foundational for
  robustness / fairness evaluation.

---

## MedHELM (arXiv 2025)

**Clinical-domain extension of HELM.** arXiv:2505.23802 (June 2025).

- **Clinician-validated taxonomy:** 5 categories, 22 subcategories,
  **121 tasks** — developed with **29 clinicians**
- **35 benchmarks** (17 existing + 18 new), 9 frontier LLMs
- **Findings:**
  - DeepSeek R1: 66% win-rate
  - o3-mini: 64% win-rate
  - Claude 3.5 Sonnet: comparable at 40% lower cost
  - **Strongest domains:** Clinical Note Generation (0.73–0.85),
    Patient Communication (0.78–0.83)
  - **Weakest domains:** Clinical Decision Support (0.56–0.72),
    Administration / Workflow (0.53–0.63)

---

## HELM ecosystem (CRFM, continuing)

GitHub: github.com/stanford-crfm/helm (~2.8k stars).

- **HELM Classic** — original 2022 leaderboard (30 models, 42
  scenarios, 7 metrics)
- **HELM Capabilities** — capability-focused scenarios (March
  2025)
- **HELM Safety** — safety-specific properties and risks
- **HELM Long Context** — long-context evaluation (September 2025)
- **MedHELM** — clinical / medical tasks (May 2025)
- **VHELM** — vision-language models
- **HEIM** — Holistic Evaluation of Text-to-Image Models
- **Holistic Evaluation of Audio-Language Models**
- **AIR-Bench** — AI risk categorization
- **ToRR** — Table Reasoning and Robustness (vision-language)
- **Enterprise Benchmark** — enterprise-specific use cases

---

## Other CRFM outputs (non-paper)

- **Stanford Mistral (2021)** — reproducible GPT-2 Small/Medium
  training framework (5 models each, 600+ checkpoints, different
  seeds). **Distinct from Mistral AI the French company** — same
  name, different project.
- **BioMedLM** — with MosaicML
- **LegalBench + Pile of Law**
- **Levanter** — JAX-based LM training framework
- **FMTI (Foundation Model Transparency Index)** — October 2023,
  updated 2024, 2025. 100 transparency indicators. **2023 avg
  score 37/100; Meta top at 54/100.**
- **Ecosystem Graphs** — documenting the FM landscape / supply
  chain
- **Marin** — radical-openness lab (May 19, 2025)

---

## Tools and platforms (his cultural artifacts)

- **HELM** — multi-metric holistic benchmarking
- **CodaLab Worksheets** — reproducibility platform; research
  provenance tracking
- **Marin** — open-development lab
- **FMTI** — transparency scoring
- **Ecosystem Graphs** — FM supply-chain documentation
- **Levanter** — JAX LM training framework

---

## Funding streams

- **NSF CAREER Award** (2016)
- **Microsoft Research Faculty Fellowship** (2014)
- **Sloan Research Fellowship** (2015)
- **Marin funders:** Google, Open Athena, Schmidt Sciences
- CRFM under Stanford HAI umbrella

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: Scholar (`pouyVyUAAAAJ`), arXiv, CRFM blog, 1
  research agent verification pass.
- Status: primary-source-verified.
- **Open questions flagged:** Liang's exact Together AI title
  (listed as "Founder" without operational C-title); NIST-specific
  engagement; Foundation Model Development Cooperative status.
