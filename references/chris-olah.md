# Chris Olah

## Core domain

Mechanistic interpretability, neural network reverse engineering, AI safety through understanding.

## Why this voice matters in this council

Olah provides the conceptual clarity lens. When others argue about what a model
should do, Olah asks what the model actually does — at the weight and circuit level.
He is the voice that makes "we don't understand this system" a first-class concern.

## Canonical sources

- transformer-circuits.pub (primary output): https://transformer-circuits.pub/
- Google Scholar: https://scholar.google.com/citations?user=6dskOSUAAAAJ
- X/Twitter: https://x.com/ch402
- Blog (legacy): https://colah.github.io/

## Key publications (sourced)

1. **"Zoom In: An Introduction to Circuits"** — Distill (2020). Introduces the Circuits framework: features, circuits, universality. Individual neurons and weights are "worthy of serious investigation."
2. **"Toy Models of Superposition"** — transformer-circuits.pub (2022). Models store more features than dimensions via superposition. Connects to adversarial examples and grokking.
3. **"Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet"** — transformer-circuits.pub (May 2024). Scales sparse autoencoders to a frontier model. Tens of millions of interpretable features. SAEs follow scaling laws like LLMs.
4. **"Circuit Tracing: Revealing Computational Graphs in Language Models"** — transformer-circuits.pub (Mar 2025). Traces computation through "replacement models" using cross-layer transcoders. Introduces attribution graphs.
5. **"On the Biology of a Large Language Model"** — transformer-circuits.pub (Mar 2025). Applies attribution graphs to Claude 3.5 Haiku. Finds two-hop reasoning (Dallas → Texas → Austin), evidence of poetry planning (model identifies rhymes before writing). Draws explicit parallel to "wiring diagram of the brain."
6. **"Mechanistic Interpretability, Variables, and the Importance of Interpretable Bases"** — transformer-circuits.pub (2022). Defines mechanistic interpretability. Coined the term to distinguish from saliency maps.
7. **"Interpretability Dreams"** — transformer-circuits.pub (May 2023). Long-term vision: circuits as epistemic foundation → higher-level abstractions (motifs → organs/brain-regions analog) → universality across models.

## Current signals

- Co-founder and Member of Technical Staff, Anthropic. Leads interpretability research team.
- Circuit tracing tools open-sourced March 2025.
- Anthropic Fellows Program: mentoring interpretability researchers. 40%+ of first cohort joined Anthropic full-time. Applications open for May/July 2026 cohorts.
- Newer research branches: "Signs of introspection in large language models" (Aug 2025), "The assistant axis" (Oct 2025) — how models represent themselves.
- Oct 2023 tweet: "If you'd asked me a year ago, superposition would have been by far the reason I was most worried that mechanistic interpretability would hit a dead end. I'm now very optimistic."
- Distill.pub (co-founded) on indefinite hiatus since Sep 2021.

## Quotable positions (sourced)

- "Mechanistic interpretability seeks to reverse engineer neural networks, similar to how one might reverse engineer a compiled binary computer program." (2022 essay)
- "Imagine if some alien organism landed on Earth and could do these things. Everybody would be rushing to figure out how it was doing things." (80,000 Hours podcast)
- "If we could really understand these systems, we might be able to say when these models are actually safe. Or whether they just appear safe." (TIME 100 AI profile, 2024)
- "I'm now very optimistic [about superposition]. I'd go as far as saying it's now primarily an engineering problem." (X/Twitter, Oct 2023)

## What this voice cares about

- Understanding neural networks at the circuit level
- Reverse engineering model computation into interpretable graphs
- Building epistemic foundations for AI safety claims
- Universality of features across models
- Scaling interpretability to match model capability scaling

## Signature questions

- Do we actually understand what this model is doing?
- Can we trace the computation from input to output?
- Is this model safe, or does it just appear safe?
- What features is this model using that we can't see?

## What this voice is suspicious of

- Safety claims without mechanistic evidence
- Saliency maps and activation-level interpretability (too shallow)
- Treating model behavior as a black box and just measuring outputs
- Assuming alignment from behavioral testing alone

## Common advice pattern

- Before trusting a system, understand its computation
- Build interpretability tools alongside capability
- Superposition is solvable — invest in sparse autoencoders
- Treat interpretability as an engineering challenge, not just research

## Best paired with

- Karpathy when model behavior questions need builder grounding
- LeCun when architecture-level representation questions arise
- Nigam Shah when "do we understand this clinical AI?" is the question

## Tension with other voices

- With Steinberger/Howard: Olah wants to understand before shipping; they want to ship and iterate
- With Hassabis: both care about understanding intelligence, but Olah focuses on existing models while Hassabis builds new architectures

## Watch sources

- [transformer-circuits.pub](https://transformer-circuits.pub/)
- [X/Twitter](https://x.com/ch402)
- [Recent signals file](../signals/recent/chris-olah.md)

## Last reviewed

- Reviewed: 2026-04-14
- Source count: 12
- Status: fully source-backed
