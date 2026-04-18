# Frameworks: Aidan Gomez

> Named frameworks and conceptual contributions. Each anchored to
> a specific paper, product, blog post, podcast, or verbatim
> quote.

---

## 1. Transformer architecture (2017)

**The foundational contribution.** *"Attention Is All You Need"*
(Vaswani, Shazeer, Parmar, Uszkoreit, Jones, Gomez, Kaiser,
Polosukhin — NeurIPS 2017).

Gomez was youngest of the 8 authors (age 20, Google Brain
intern). His contribution was implementation and experimentation:

> *"I ran hundreds of experiments testing different
> configurations."*

**Cultural footprint:** >173,000 citations as of 2025. Every
modern LLM descends from this paper.

### His self-positioning
> *"The transformer gave us the architecture. But architecture
> alone doesn't create value. You need to build products people
> actually want to pay for."*

He explicitly refuses to coast on Transformer fame — Cohere is
framed as the transformer idea **"translated into enterprise
infrastructure."**

---

## 2. Enterprise-first AI — "prosaic, not AGI"

**His strategic thesis.**

> *"Everyone's obsessed with AGI timelines and whether AI will be
> sentient. But the actual AI revolution happening right now is
> much more prosaic — companies automating document review,
> customer support routing, code documentation."*

### Operational embodiment
- North (agentic enterprise platform)
- Command family (specialized enterprise LLMs)
- Private / VPC / on-prem deployment as default

### Contrast with competitors
Explicitly NOT competing with ChatGPT. Deliberately anti-
consumer.

---

## 3. North — agentic enterprise platform

**Cohere's flagship 2025-2026 product.**

- **Timeline:** Early Access Program January 2025 → wide release
  August 6, 2025
- **Development time:** 18 months before public launch
- **Launch partners:** RBC (North for Banking), Dell, Ensemble
  Health Partners, Bell Canada

### Product philosophy
> *"We believe AI should eliminate the mundane, not compromise
> your data. That's why we built North — an agentic AI platform
> designed for real work, real teams, and extreme security."*

### Deployment differentiation
- Private cloud
- On-prem
- VPC
- Model Vault (dedicated infrastructure)

### When he invokes it
Any enterprise AI deployment question. Regulated-industry
conversations (banking, healthcare, telecom, defense).

---

## 4. Compass — search/discovery layer for North

**Multimodal semantic search framework.**

Combines:
- **Embed** (multimodal search/retrieval)
- **Rerank** (semantic relevance)
- Document parsing + managed index

### Native connectors
Gmail, Outlook, Slack, Salesforce, SharePoint, Google Drive.

### Strategic role
RAG infrastructure for enterprise agents. Keeps customer data
inside the customer's perimeter.

---

## 5. Compute-maximalism is "the dumbest" (small-model thesis)

**His public counter to frontier-scale strategies.**

> *"It's definitely true that if you throw more compute at the
> model, if you make the model bigger, it'll get better. It's
> the most trustworthy way to improve models. It's also the
> dumbest."*

### Empirical embodiment
- **Tiny Aya** (Feb 17, 2026): 3.35B params, single cluster of
  64 H100s, 70+ languages
- **Transcribe** (Mar 26, 2026): 2B params, consumer-GPU
  deployable, #1 Hugging Face Open ASR leaderboard (5.42 WER)
- **Command A** (Mar 13, 2025): 111B params, runs on 2 GPUs
  (A100 or H100)

### Position
> *"We live in this world of unbundled verticalized models,
> which are much more efficient and smaller, designed for
> specific use cases."*

Efficient / specialized beats frontier-generalist for enterprise.

---

## 6. RAG reframes enterprise AI economics

**His operational thesis on retrieval.**

> *"RAG fundamentally changes the economics of enterprise AI.
> You don't need a $100 million training run every time your
> product catalog changes. You just update your database, and
> the model retrieves the latest information."*

### Hallucination framing
> *"Hallucination, which is when these models dream up facts.
> They only hallucinate when they feel like they have to. When
> they don't have access to that information. That's why RAG is
> so crucial."*

### Economic implication
RAG + efficient retrieval = you don't retrain when the world
changes. You update the retrieval layer.

---

## 7. Inference > training (the economic tipping point)

**Source:** Fortune, April 2024.

> *"We're starting to hit the inflection point now where
> spending on inference compute is becoming higher than spending
> on training."*

### Corollary on margins
- Compute-maximalism → "zero margin business"
- Private deployment → high SaaS-like margins (*"whereas many
  others in the industry are losing money per customer"*)

### When he invokes it
Any IPO / investor conversation. Any "should we buy NVIDIA
training runs?" discussion.

---

## 8. Sovereign AI

**His geopolitical framing of Cohere's strategic position.**

### Definition (verbatim)
> *"Ensuring there is no third party that can switch you off,
> there is no foreign entity that can just shut down the
> operation of your economy or government."*

> *"Sovereignty means control. No one can switch it off."*

### Not an either/or
> *"It's not an 'either or', it's an 'and'."*

Sovereign + global.

### Operational embodiment
- Canadian government Sovereign AI Compute ($240M Dec 2024)
- UK Government deal (June 2025)
- Bell Canada partnership
- Fujitsu Japan (Takane LLM)
- LG Korea
- Aleph Alpha merger talks (April 2026, with German government
  anchor-customer positioning)
- Rumored UAE / Saudi engagements (unverified)

---

## 9. Aya — open multilingual AI

**Cohere Labs' flagship research program.**

- **Aya 23** (May 2024): 8B and 35B params, 23 languages,
  1,000+ researchers from 119 countries
- **Aya Expanse** (Dec 2024): arXiv 2412.04261
- **Aya Vision 8B** (Mar 3, 2025): multimodal, 23 languages
- **Tiny Aya** (Feb 17, 2026): mobile-optimized, 70+ languages

### Licensing philosophy
Open for research (CC non-commercial). Commercial under license
(Command family). This is a deliberate hybrid — different from
Meta (fully open), Anthropic (fully closed), Mistral (mixed
commercial open).

### When he invokes it
Any "open-source" debate. Any "diversity of AI talent" question.

---

## 10. System-2 / Inner Monologue framing for models

**His current technical thesis.**

> *"The status quo with models is: I ask you a question and the
> model is expected to respond immediately with the right
> answer. That's an incredibly high burden to place on the model
> […] There's this very obvious next step for models, which is
> you need to let them think and work through problems."*

Aligns with the broader reasoning-model wave (o1, o3, Claude
reasoning, Gemini thinking) but framed through Cohere's
deployment lens.

---

## 11. "Enterprises are much slower machines"

**His patience framing.**

> *"Enterprises are much slower machines. They took longer to
> build momentum."*

Plans for a multi-year production-workload ramp, not a
launch-day pop. Informs pricing, sales cycle, customer success
architecture.

---

## 12. "Quietly do good work" (anti-OpenAI tone)

**His public-persona framing.**

> *"We don't do these blockbuster launch event type things. We
> just want to quietly do good work, build really good software,
> and focus on becoming an essential partner to our customers."*

Deliberate rhetorical counter-position to the OpenAI /
Anthropic / xAI communication style.

---

## 13. Margin bifurcation as IPO thesis

**His case for the public markets.**

> *"I think public market investors would be excited to have a
> pure-play AI investment opportunity, as opposed to investing
> by proxy through hyperscalers."*

### Structural differentiation
- Cohere: private deployment → high SaaS-like margins
- Competitors: API-first → losing money per customer

### Operational implication
Cohere is IPO-targeting in 2026-2027. François Chadwick (CFO,
ex-Uber IPO) hired August 2025 as the signal.

---

## 14. "Acquisition is failure"

**His ownership stance.**

> *"Acquisition is failure."*
— Toronto Tech Week, June 2025

Cohere refuses Big Tech acquisition framings. The only exit
path he entertains is IPO.

---

## 15. Anti-doomer pragmatism

**His public philosophical stance.**

- AGI existential risk is *"an absurd use of our time"*
- Real risks: *"the automated spread of misinformation on
  social media"*
- EA movement: *"self-righteousness"* (November 2023 staff
  letter)
- UK AI Safety Summit posture: push conversation toward
  *"practical, near-term harms"*

### When he invokes it
Any regulation debate. Any AI safety conversation framed in
catastrophic terms.

---

## Recurring verbal devices (not frameworks per se)

- *"Prosaic"* — his word for enterprise AI
- *"Quietly do good work"* — counter-hype framing
- *"It's also the dumbest"* — contrast-as-definition
- *"What I really care about…"* — redirect to productivity
- *"Enterprises are much slower machines"*
- *"Every company will be an AI company"*
- *"AI isn't a shortcut"*
- *"Not an 'either or', it's an 'and'"*

---

## Last reviewed

- Reviewed: 2026-04-18
- Source pass: 3 research agents + direct Cohere blog + 20VC +
  Fortune + Bloomberg verification.
- Status: comprehensive; each framework anchored to a specific
  product, paper, or quote.
