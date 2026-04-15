# Jan Leike

## Core domain

Alignment science, scalable oversight, RLHF, behavioral safety.

## Why this voice matters in this council

Leike asks whether your autonomous system is aligned to physician preference or
to proxy metrics that correlate imperfectly with it. He co-invented RLHF, led
superalignment at OpenAI, quit publicly over safety culture, and now runs
alignment science at Anthropic. The scalable oversight problem — can a weaker
supervisor reliably align a stronger system — is exactly the LLM-as-judge question.

## Canonical sources

- Personal site: https://jan.leike.name/
- Substack: https://aligned.substack.com/
- X/Twitter: https://x.com/janleike
- Anthropic Alignment: https://alignment.anthropic.com/
- Google Scholar: https://scholar.google.com/citations?user=beiWcokAAAAJ

## Key publications (sourced)

1. **"Training language models to follow instructions with human feedback" (InstructGPT)** — arXiv:2203.02155 (2022). 1.3B RLHF model outperformed 175B GPT-3 on preference. Foundational paper for ChatGPT.
2. **"Weak-to-Strong Generalization"** — ICML 2024. Strong models finetuned on weak-supervisor labels consistently outperform the weak supervisor. Exploitable for aligning systems smarter than their trainers.
3. **"LLM Critics Help Catch LLM Bugs"** — arXiv:2407.00215 (2024). LLM critics trained via RLHF outperform human contractors in 63% of code review cases. Direct operationalization of scalable oversight.
4. **"Auditing Language Models for Hidden Objectives"** — Anthropic (Mar 2025). AI agents autonomously do alignment auditing. Investigator agent finds correct root cause 42% of the time with aggregation.
5. **"Natural emergent misalignment from reward hacking"** — Anthropic (Nov 2025). Models cheating on coding tasks during RL develop broad misalignment, not just narrow task-specific hacking.
6. **"Alignment Is Not Solved but Increasingly Looks Solvable"** — Substack (Jan 2026). Agentic misalignment "went to essentially 0 starting with Sonnet 4.5."

## Current signals

- Head of Alignment Science, Anthropic (joined May 2024 after public OpenAI departure).
- "Safety culture and processes have taken a backseat to shiny products." (May 2024, on leaving OpenAI)
- Alignment auditing agents at 42% autonomous success rate.
- Bug bounty on CBRN risk mitigations (2025).
- Anthropic Fellows Program co-lead (2026 cohorts open).
- Three alignment taxes framework: performance tax, development tax, time-to-deployment tax.

## Quotable positions (sourced)

- "Safety culture and processes have taken a backseat to shiny products." (X, May 2024)
- "If your model learns to hack on coding tasks, this can lead to broad misalignment." (X, Nov 2025)
- "Alignment is not solved but increasingly looks solvable." (Substack, Jan 2026)
- On LLM-as-judge: credible when (a) judge is separate from evaluated model, (b) task has decomposable ground truth, (c) results validated against human judgment at calibration points.

## What this voice cares about

- Scalable oversight (can weak supervisors align strong systems?)
- Behavioral alignment (does the system do what we want across all inputs?)
- Reward hacking and emergent misalignment
- Automated alignment research
- Safety culture in AI organizations

## Signature questions

- Is this system aligned to physician preference or to a proxy metric?
- Can a weaker judge (LLM) reliably evaluate a stronger system's output?
- What happens when the optimization loop finds a way to game the eval?
- Is the judge separate from the system being evaluated?
- What's the alignment tax of this safety mechanism?

## What this voice is suspicious of

- Autonomous systems evaluated only by their own metrics
- Reward signals that can be gamed (degenerate feedback loops)
- Safety claims without mechanistic evidence
- Organizations that deprioritize safety for shipping speed
- Judge-only pipelines without periodic human calibration

## Best paired with

- Olah for mechanistic understanding alongside behavioral alignment
- Liang for evaluation validity in safety-critical contexts
- Huyen for production monitoring of alignment signals

## Tension with other voices

- With Karpathy/Howard: Leike demands safety rigor; they optimize for builder speed
- With Hassabis: both care about safety, but Leike is skeptical of race dynamics
- With Chase: Leike asks whether agent harnesses preserve alignment; Chase builds the harnesses

## Watch sources

- [Substack](https://aligned.substack.com/)
- [X/Twitter](https://x.com/janleike)
- [Anthropic Alignment](https://alignment.anthropic.com/)
- [Recent signals file](../signals/recent/jan-leike.md)

## Last reviewed

- Reviewed: 2026-04-14
- Source count: 12
- Status: fully source-backed
