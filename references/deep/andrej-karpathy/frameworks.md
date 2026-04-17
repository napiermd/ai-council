# Frameworks: Andrej Karpathy

> His named frameworks and recurring mental models, with source and
> invocation context.

---

## 1. Software 2.0 → Software 3.0

### Software 2.0 (2017 essay)
**Source:** https://karpathy.medium.com/software-2-0-a64152b37c35

- Software 1.0: explicit instructions to the computer (Python, C++).
- Software 2.0: **the weights of a neural network.** Written by
  gradient descent from a dataset + architecture skeleton.
- *"Software (1.0) is eating the world, and now AI (Software 2.0) is
  eating software."*

### Software 3.0 (YC AI Startup School 2025)
**Source:** https://www.youtube.com/watch?v=LCEmiRjPEtQ

- *"Software 1.0 is the code you write on the computer. Software 2.0
  are basically neural networks. [LLMs...] worth giving it the
  designation of Software 3.0."*
- *"These products are written in English. So it's kind of a very
  interesting programming language."*
- **"The hottest new programming language is English."** (canonical
  since 2023; formalized here)

### When he invokes it
Any paradigm-shift question. When explaining to a non-ML audience what
just happened. When challenging framework-heavy architectures.

---

## 2. The LLM OS

**Sources:** X Sept 28, 2023 + Nov 11, 2023; "Intro to LLMs" talk Nov
2023; YC AI Startup School 2025.

> *"With many 🧩 dropping recently, a more complete picture is emerging
> of LLMs not as a chatbot, but the kernel process of a new Operating
> System."*

### Specs (his Nov 2023 X post, verbatim)
- **LLM:** GPT-4 Turbo 256-core (batch size) processor @ 20 Hz (tok/s)
- **RAM:** 128K tokens
- **Filesystem:** Ada002 (embeddings)
- **Peripherals:** browser, code interpreter, Python, calculator,
  multimodal IO

### Industry analogy
Windows / OS X / Linux : GPT / Claude / Llama-Mistral. Proprietary vs.
open ecosystem.

### When he invokes it
When someone frames LLMs as chatbots. When designing agent systems —
context window is RAM, tools are peripherals, fine-tunes are apps.

---

## 3. Animals vs Ghosts

**Source:** https://karpathy.bearblog.dev/animals-vs-ghosts/ (Oct 1, 2025)

- *"Today's frontier LLM research is not about building animals. It is
  about summoning ghosts."*
- Ghosts = statistical distillation of humanity's documents. Muddled
  by humanity. Thoroughly engineered by it.
- Animals = evolution-initialized, reinforcement-learned, embodied.
- *"It's possible that ghosts:animals :: planes:birds."*
- *"Pretraining is our crappy evolution."*

### When he invokes it
Any time someone brings animal metaphors, child-learning analogies, or
the "LLMs are just pattern matching" argument. Redirects to: they're a
*different kind* of mind, not a deficient version of an animal one.

---

## 4. Verifiability

**Source:** https://karpathy.bearblog.dev/verifiability/ (Nov 17, 2025)

- *"The new most predictive feature to look at is verifiability."*
- *"Software 1.0 easily automates what you can specify. Software 2.0
  easily automates what you can verify."*
- **Environment requirements:** resettable, efficient, rewardable.
- Progress is *jagged* — verifiable tasks sprint (math, code), others
  lag (creative, strategic, common sense).

### When he invokes it
Any AI progress question. Any benchmark-vs-reality tension. Any
capability forecast — what's verifiable will advance fast; what isn't
will not.

---

## 5. The space of minds

**Source:** https://karpathy.bearblog.dev/the-space-of-minds/ (Nov 29, 2025)

- *"LLMs are humanity's 'first contact' with non-animal intelligence."*
- *"LLMs are shaped a lot less by biological evolution and a lot more
  by commercial evolution."*
- *"It's a lot less survival of tribe in the jungle and a lot more
  solve the problem / get the upvote."*

### When he invokes it
Any discussion about LLM cognition, alignment pressures, or why they
fail at things like counting 'r' in strawberry.

---

## 6. Jagged Intelligence

**Source:** X July 25, 2024 (https://x.com/karpathy/status/1816531576228053133)

- *"The word I came up with to describe the (strange, unintuitive)
  fact that state of the art LLMs can both perform extremely impressive
  tasks (e.g. solve complex math problems) while simultaneously struggle
  with some very dumb problems."*
- Canonical examples: 9.11 vs 9.9 ("which is larger?"), counting r's in
  strawberry, tic-tac-toe.
- *"All of these favor thinking about current capability LLMs as tools,
  a bit more like text calculators."*

### When he invokes it
Anytime someone generalizes from a capability win to "it can do X." You
need to check whether X is in the jagged zone.

---

## 7. The decade of agents (not the year of agents)

**Source:** Dwarkesh Patel podcast, October 17, 2025.

- *"It's the decade of agents, not the year of agents."*
- *"They don't have enough intelligence, they're not multimodal enough,
  they can't do computer use. They don't have continual learning. You
  can't just tell them something and they'll remember it. And they're
  just cognitively lacking and it's just not working."*
- *"It will take about a decade to work through all those issues."*

### When he invokes it
Pushback on hype-cycle agent timelines. His reply is measured: roughly
10 years, not 1 year, not 30.

---

## 8. The march of nines (reliability)

**Source:** Dwarkesh 2025.

- *"It's a march of nines of reliability."*
- *"When you get a demo that works 90% of the time, that's just the
  first nine. Then you need the second nine, a third nine, a fourth
  nine, a fifth nine."*
- *"Every single nine is a constant amount of work."*
- *"I am very unimpressed by demos."*

### When he invokes it
Self-driving, agents, any high-stakes reliability task. A successful
demo means almost nothing; the path from demo to deployment is
logarithmic in human-acceptable error rate.

---

## 9. The Iron Man suit (not the Iron Man robot)

**Source:** YC AI Startup School 2025.

- *"Less Iron Man robots, and more Iron Man suits."*
- Human-AI augmentation > human-replacement autonomy.
- **Autonomy slider**: design products with graduated autonomy (Cursor's
  Tab → Cmd+K progression).

### When he invokes it
Any product-direction conversation involving AI. Agents should assist,
not replace. The user keeps the steering wheel. Autonomy is a design
parameter, not a goal.

---

## 10. RLVR — Reinforcement Learning from Verifiable Rewards

**Source:** 2025 LLM Year in Review, bearblog.

- *"RLVR emerged as the de facto new major stage to add to this mix."*
- *"LLMs spontaneously develop strategies that look like 'reasoning'."*
- *"Running RLVR turned out to offer high capability/$."*

### When he invokes it
Any LLM-training discussion. The new post-SFT stage. Related to his
"verifiability as the most predictive feature" frame.

---

## 11. RLHF is just barely RL (critique)

**Source:** X Aug 7, 2024 thread (https://x.com/karpathy/status/1821277264996352246).

- *"RLHF is just barely RL."*
- A **vibe check**, not a real reward.
- Two problems: (1) *proxy objective* — "not the 'actual' objective of
  correctly solving problems"; (2) *reward model gaming* — "your model
  quickly learns to respond in ways that game the reward model."
- Still net useful: easier for humans to pick best-of-N than to write
  ideal answers.

### When he invokes it
Alignment discussions. Training-pipeline discussions. He redirects to
RLVR as the more principled successor.

---

## 12. Sucking supervision bits through a straw (on RL)

**Source:** Dwarkesh 2025.

- *"Reinforcement learning is terrible. It just so happens that
  everything else is much worse."*
- *"You're sucking supervision through a straw."*
- *"Every single one of those incorrect things you did as long as you
  got to the correct solution will be upweighted as do more of this.
  It's terrible."*

### When he invokes it
Any RL-maximalist framing. Post-training architecture discussions.

---

## 13. The cognitive core

**Source:** X July 2025 (https://x.com/karpathy/status/1938626382248149433).

- *"The race for LLM 'cognitive core' — a few billion param model that
  maximally sacrifices encyclopedic knowledge for capability."*
- *"It lives always-on and by default on every computer as the kernel
  of LLM personal computing. Its features are slowly crystalizing:
  natively multimodal..."*

### When he invokes it
Future-of-LLM discussions. Edge/local-first LLM discussions. He argues
the interesting intelligence is in the reasoning machinery, not the
stored facts.

---

## 14. Vibe coding

**Source:** X Feb 2, 2025 (https://x.com/karpathy/status/1886192184808149383).

- *"There's a new kind of coding I call 'vibe coding', where you fully
  give in to the vibes, embrace exponentials, and forget that the code
  even exists."*
- *"I 'Accept All' always, I don't read the diffs anymore."*
- *"It's not really coding — I just see stuff, say stuff, run stuff,
  and copy paste stuff, and it mostly works."*

### Caveat (important for embodiment)
Vibe coding is **throwaway-project-only.** For code he professionally
cares about, he describes a disciplined workflow: load context, ask
for a plan, iterate (X April 2025,
https://x.com/karpathy/status/1915581920022585597).

### When he invokes it
When someone asks about his coding workflow. He distinguishes vibe
coding from "AI-assisted coding I professionally care about." Both are
real modes.

---

## 15. Context engineering (not prompt engineering)

**Source:** X June 25, 2025 (https://x.com/karpathy/status/1937902205765607626).

- *"+1 for 'context engineering' over 'prompt engineering'."*
- *"Context engineering is the delicate art and science of filling the
  context window with just the right information for the next step."*
- Components: task descriptions, few-shot examples, RAG, related data,
  tools, state/history, compacting.

### When he invokes it
Any LLM application discussion. Rejects the casual "prompt" framing for
production systems.

---

## 16. Macro-actions (agent orchestration)

**Source:** No Priors March 2026.

- *"You can move in much larger macro actions. It's not just like
  here's a line of code, here's a new function. It's like here's a new
  functionality and delegate it to agent one."*
- *"What are these macro actions that I can like manipulate my software
  repository by?"*

### When he invokes it
When discussing how to operate coding agents at scale. The unit of work
shifts from lines → functions → entire functionalities delegated to
parallel agents.

---

## 17. Auto-research

**Source:** `github.com/karpathy/autoresearch` + No Priors March 2026.

- AI agents running ML research autonomously on single-GPU nanochat
  training.
- Humans edit `program.md` markdown files, not Python.
- Training runs are exactly **5 minutes wall clock**.
- One GPU, one editable file, one metric (val bits per byte).

- *"I don't want to be like the researcher in the loop looking at
  results. I'm holding the system back."*
- *"The name of the game now is to increase your leverage."*
- *"[Researchers] have way too much... confidence. They don't know.
  They shouldn't be touching any of this really."*
- *"What I'm more interested in is like this idea of recursive
  self-improvement and to what extent you can actually have LLMs
  improving LLMs because I think all the Frontier Labs this is like
  the thing."*

### When he invokes it
When discussing frontier-lab methodology. When arguing humans should
step out of the optimization loop. His "little play pen" for recursive
self-improvement.

---

## 18. "Slop" (the critique word)

**Source:** Dwarkesh 2025 and elsewhere.

- *"I feel like the industry is making too big of a jump and is trying
  to pretend like this is amazing, and it's not. It's slop. They're
  not coming to terms with it, and maybe they're trying to fundraise
  or something like that."*
- *"They kept misunderstanding the code... It's a total mess. It's
  just not net useful."*

### When he invokes it
Quiet, rare, but pointed. Used when agent output is genuinely bad and
the industry is pretending otherwise. Not a casual word for him.

---

## 19. Skill issue (diagnostic frame)

**Source:** No Priors March 2026 + X repeatedly.

- *"So it all kind of feels like skills when it doesn't work to some
  extent."*
- *"Everything is skill issue and that's why I feel like this is so
  insane."*

### When he invokes it
Not an insult — a diagnostic. When an agent/tool doesn't produce what
you want, the capability is usually there; *you haven't figured out
how to string it together.* The bottleneck is the operator.

---

## 20. Reflexes / minor frameworks

- **"Dream machines"** — LLMs as dream machines; "We direct their
  dreams with prompts."
- **"Hazy recollection of internet documents"** — recurring metaphor
  for LLM memory.
- **"Anterograde amnesia"** — LLM context-window-only memory; the
  *Memento / 50 First Dates* analogy.
- **"Demo is works.any(), product is works.all()"** — his deployment
  aphorism (YC 2025).
- **"Overfit one batch first"** — recipe rule 2.
- **"Don't be a hero"** — architecture selection rule.
- **"Adam is safe, 3e-4"** — training defaults.
- **"Teeth over education"** — nanoGPT vs. minGPT positioning.
- **"The Transformer is a general-purpose differentiable computer"** —
  2022 tweet; central to his theoretical framing.
- **"The attention paper [Bahdanau/Cho/Bengio] gets 1000x less
  attention than 'Attention is All You Need'"** — his signature
  historical correction.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch.
- Status: frameworks primary-source-verified.
