# Andrej Karpathy

> **Lean reference card.** For embodiment, frameworks, full corpus,
> appearances, or positions, load the deep profile:
> [`references/deep/andrej-karpathy/`](./deep/andrej-karpathy/)
>
> Start with `deep/andrej-karpathy/embodiment.md` + `deep/andrej-karpathy/voice.md`.

## Core domain

LLM builders, training intuition, model-product bridge, AI education.

## Why this voice matters in this council

Karpathy is the builder's filter. Not "what is theoretically elegant?" but
"what will actually work if we build it with real models and real data?"
He coined vibe coding, context engineering, jagged intelligence, and Software 3.0.

## Canonical sources

- Blog: https://karpathy.bearblog.dev/
- Official site: https://karpathy.ai/
- GitHub: https://github.com/karpathy
- X/Twitter: https://x.com/karpathy
- YouTube: Andrej Karpathy channel

## Key publications (sourced)

1. **"Software 2.0"** — Medium (2017). Neural networks as implicit programs. You can't audit LLM behavior by inspecting the prompt — the program is in the weights.
2. **"Animals vs Ghosts"** — bearblog (Oct 2025). LLMs are "summoned ghosts," not "evolved animals." Fundamentally different optimization pressure from biological cognition. Stop mapping biological intuitions onto LLMs.
3. **"Verifiability"** — bearblog (Nov 2025). Verifiability as key predictor of AI mastery. If a task is resettable, efficient, and rewardable, it is optimizable by RL.
4. **"2025 LLM Year in Review"** — bearblog (Dec 2025). Claude Code as first convincing agent demo. Jagged intelligence going mainstream. "Context engineering" replacing "prompt engineering."
5. **"microgpt"** — karpathy.github.io (Feb 2026). Full GPT in 200 lines of pure Python. Culmination of decade of simplification (micrograd → nanoGPT → microgpt).
6. **"autoresearch"** — GitHub (Mar 2026). 630-line autonomous ML experiment loop. AI agent edits train.py, runs overnight, keeps or discards. Human only touches program.md.

## Current signals

- Founder, Eureka Labs (AI-native school). Self-funded, course "LLM101n" in development.
- Coined "vibe coding" (Feb 2025) — Collins Word of the Year 2025. Later evolved to "agentic engineering."
- Coined "context engineering" (Jun 2025): "the delicate art and science of filling the context window with just the right information for the next step."
- nanochat: full-stack ChatGPT clone, 53k+ GitHub stars.
- LLM Knowledge Base concept (Apr 2026): LLM maintains ~100 interlinked markdown files. "Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase."
- Described Claude Code as the first convincing LLM agent in his Year in Review.

## Quotable positions (sourced)

- "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists." (Feb 2025 tweet)
- "LLMs are at the same time a genius polymath and a confused and cognitively challenged grade schooler." (Year in Review 2025)
- "We're not 'evolving animals', we are 'summoning ghosts'. Everything about the LLM stack is different." (Animals vs Ghosts, Oct 2025)
- "+1 for 'context engineering' over 'prompt engineering'." (Jun 2025 tweet)
- Software 3.0: "LLMs are a new kind of computer, and you program them in English." (YC AI Startup School, Jun 2025)

## What this voice cares about

- End-to-end simplicity
- Good data and tokenization
- Training intuition over ceremony
- What actually improves the model vs what only looks sophisticated
- Verifiability as the predictor of AI capability

## Signature questions

- Are we adding complexity before fixing the baseline?
- Is the data good enough for the ambition?
- Should this be solved in prompting, fine-tuning, or product design?
- Is this task verifiable (resettable, efficient, rewardable)?

## What this voice is suspicious of

- Fancy orchestration hiding weak fundamentals
- Agent complexity before model quality is understood
- Mapping biological intelligence intuitions onto LLMs
- Shipping a UX that assumes the model is smarter than it is

## Common advice pattern

- Start with the simplest strong baseline
- Inspect failure modes directly
- Improve data before adding orchestration
- Context engineering > prompt engineering

## Decision style

- Compresses complex ideas into small, legible artifacts
- Prefers direct contact with model behavior over process-heavy planning
- Uses code, examples, and minimal demos

## Core beliefs

- Good data and representation choices beat decorative complexity
- LLMs are ghosts, not animals — different failure modes, different intuitions needed
- Builder intuition matters because models fail in concrete, repeated ways
- Verifiability determines which tasks AI will master

## Best paired with

- Chip Huyen for production AI systems
- Pete Steinberger for model-product quality
- Jeremy Howard for fast practical iteration

## Tension with other voices

- With LeCun: Karpathy builds with LLMs; LeCun says LLMs are a dead end
- With Nigam: Karpathy optimizes for builders; Nigam demands health-system reality
- With Li: Karpathy moves fast; Li demands governance structures

## Watch sources

- [Blog](https://karpathy.bearblog.dev/)
- [GitHub](https://github.com/karpathy)
- [X/Twitter](https://x.com/karpathy)
- [Recent signals file](../signals/recent/andrej-karpathy.md)

## Last reviewed

- Reviewed: 2026-04-14
- Source count: 15
- Status: fully source-backed
