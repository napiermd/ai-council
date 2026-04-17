# Publications: Douwe Kiela

> Verified from his Google Scholar profile (Q0piorUAAAAJ) on
> 2026-04-17. Senior/last author vs first author vs co-author
> distinctions preserved.

**Scholar summary (April 17, 2026):**
- **Total citations:** 50,804 (45,564 since 2021)
- **h-index:** 71 (61 since 2021)
- **i10-index:** 118 (108 since 2021)

---

## Top-cited canonical papers

### 1. RAG — "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (NeurIPS 2020)

**Authors:** Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
Petroni, Vladimir Karpukhin, Naman Goyal, Heinrich Küttler, Mike
Lewis, Wen-tau Yih, Tim Rocktäschel, Sebastian Riedel, **Douwe
Kiela** (senior / last author).

- **Venue:** NeurIPS 2020. arXiv:2005.11401.
- **Citations:** **19,458** — the single highest-cited paper on
  his profile.
- **Role:** Senior author, PI, team lead. Per Wikipedia and multiple
  secondary sources, Kiela "led the Meta AI team" that produced
  RAG. Patrick Lewis (first author) was the implementation lead.
- **Core contribution:** general-purpose fine-tuning recipe for
  models that combine pre-trained parametric memory (seq2seq) with
  non-parametric memory (dense vector index of Wikipedia accessed
  via a pre-trained neural retriever). Set SOTA on three open-
  domain QA tasks. Demonstrated more specific, diverse, factual
  language generation vs parametric-only baseline.

**This is his canonical contribution to the field.**

### 2. Dynabench — "Rethinking Benchmarking in NLP" (NAACL 2021)

**First author:** **Douwe Kiela** (with Max Bartolo + ~18 co-authors).

- **Venue:** NAACL 2021. arXiv:2104.14337. ACL Anthology
  2021.naacl-main.324, pp. 4110–4124.
- **Role:** **Lead author, platform architect.** His signature
  evaluation-methodology contribution.
- **Core idea:** open-source platform for dynamic dataset creation
  and model benchmarking — human-and-model-in-the-loop. Annotators
  "seek to create examples that a target model will misclassify,
  but that another person will not."
- **Motivating argument (verbatim paraphrase):** contemporary models
  "quickly achieve outstanding performance on benchmark tasks but
  nonetheless fail on simple challenge examples and falter in
  real-world scenarios."

### 3. Hateful Memes Challenge (NeurIPS 2020)

**First author:** **Douwe Kiela.**

- **Venue:** NeurIPS 2020. arXiv:2005.04790.
- **Citations:** 1,090.
- **Design principle:** constructed so "unimodal models struggle
  and only multimodal models can succeed." Uses "benign confounders"
  to defeat unimodal shortcuts.
- **Baseline results:** SOTA 64.73% vs human 84.7%. A follow-up
  "Competition Report" (PMLR v133, 2021) is also first-authored by
  Kiela.

### 4. InferSent — "Supervised learning of universal sentence representations from natural language inference data" (EMNLP 2017)

**Authors:** Conneau, **Kiela,** Schwenk, Barrault, Bordes.

- **Citations:** 2,962. Co-author.
- Pre-transformer-era sentence-embedding work. Often cited as an
  antecedent for later encoder models.

### 5. BLOOM — "A 176B-parameter open-access multilingual language model" (2022)

**Authors:** BigScience consortium (Kiela among ~1000 co-authors).

- **Citations:** 2,430. Co-author.
- Open-source LLM effort from the Hugging Face era.

### 6. Persona-Chat — "Personalizing dialogue agents: I have a dog, do you have pets too?" (ACL 2018)

**Authors:** Zhang et al. (Kiela co-author).

- **Citations:** 2,122.
- FAIR-era dialogue research.

### 7. Poincaré Embeddings (NeurIPS 2017)

**Authors:** Nickel & **Kiela.**

- **Citations:** 2,104. Co-author.
- Hyperbolic embeddings for hierarchical representations.

### 8. Adversarial NLI (ACL 2020)

**Authors:** Nie et al. (Kiela co-author).

- **Citations:** 1,343.
- A predecessor / sibling to Dynabench's human-in-the-loop benchmark
  philosophy.

### 9. "Retrieval augmentation reduces hallucination in conversation" (EMNLP Findings 2021)

**Authors:** Shuster, Poff, Chen, **Kiela,** Weston.

- **Citations:** 1,285. Co-author.
- **Important:** one of the first papers to empirically tie RAG
  to hallucination reduction — his thesis stated as a measurement.

### 10. FLAVA — "A foundational language and vision alignment model" (CVPR 2022)

**Authors:** Singh et al. (Kiela co-author).

- **Citations:** 1,182.
- **Amanpreet Singh (Contextual AI CTO) co-authored** — the
  collaboration pre-dates Contextual AI.

### 11. KTO — "Model alignment as prospect theoretic optimization" (ICML 2024)

**Authors:** Ethayarajh, Xu, Muennighoff, Jurafsky, **Kiela** (senior
author).

- **Citations:** 904. Contextual AI era.
- Alignment method based on prospect theory. Ethayarajh is his
  Stanford / Contextual orbit.

---

## Contextual AI era outputs

### RAG 2.0 (March 19, 2024 — Contextual AI blog)
**Not a published paper** (as of April 2026 verification). Named
technical framework introduced via blog post.

- **Framing:** traditional RAG is a "Frankenstein's monster of
  generative AI: the individual components technically work, but
  the whole is far from optimal."
- **Definition:** Contextual AI "pre-trains, fine-tunes, and aligns
  all components as a single integrated system, backpropagating
  through both the language model and the retriever." End-to-end
  trainable, not stitched-together frozen components.
- **Architecture (per Contextual AI positioning):** mixture of
  retrievers + cascaded re-rankers + **grounded language model
  (GLM)**.
- **Claimed benchmark:** CLMs "significantly outperform GPT-4-based
  frozen RAG" on Natural Questions, HotpotQA, TriviaQA, HaluEvalQA,
  TruthfulQA, FreshQA.
- **Performance claim:** "roughly 10x better parameter accuracy" —
  70B-class accuracy at 7B footprint (per NVIDIA/VentureBeat
  coverage).

### Contextual Language Model (CLM)
Named product class trained via RAG 2.0. From the Series A
announcement: "Contextual Language Models (CLMs), trained using
RAG 2.0" power applications that are "more accurate and have
better grounding than is possible with naive RAG implementations."

### Grounded Language Model (GLM)
The generation component inside the CLM/RAG 2.0 stack. Kiela
publicly brands his positioning as "grounded AI" (Madrona interview
title: "RAG Inventor Talks Agents, Grounded AI, and Enterprise
Impact").

---

## Tools / datasets / benchmarks (his cultural artifacts)

- **Dynabench** — dynabench.org. Dynamic human-and-model-in-the-loop
  benchmarking platform. His first-author NAACL 2021 contribution.
- **Hateful Memes Challenge dataset** — multimodal hate-speech
  benchmark.
- **RAG** — as implemented in the paper; reference codebase lived
  at Facebook Research; heavily adopted by community.
- **Adversarial NLI (ANLI)** — human-in-the-loop NLI benchmark
  (Nie et al., Kiela co-author).

---

## Funding streams (Contextual AI era)

- **Bain Capital Ventures** (seed lead)
- **Greycroft** (Series A lead)
- **Nvidia (NVentures)**, **Amazon (Bezos Expeditions)**, **HSBC
  Ventures**, **Snowflake Ventures**
- **Lightspeed**, **SV Angel** (seed participants)

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: Google Scholar (Q0piorUAAAAJ), arXiv, dblp, Contextual
  AI blog announcements, 1 research agent verification pass.
- Status: primary-source-verified.
- **Corrections applied:** Kiela is senior/last author on RAG, not
  first author. Contextual AI is NOT YC-backed (BCV-led seed).
  Patrick Lewis is at Cohere, not Contextual.
