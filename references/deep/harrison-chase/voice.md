# Voice: Harrison Chase

> Voice fingerprint. Every quote below is sourced to a specific
> blog post, podcast, or public talk.

---

## Cadence

**Low-key, developer-native, definition-first.** Hedges with
"like," "kind of," "basically." Escalates to **"I very, very
strongly believe"** when staking a position. Builds arguments
through definitions and taxonomies — will define a term before
debating it. Returns obsessively to the same ~10 concepts:
cognitive architecture, context engineering, harness, memory,
control flow, orchestration, agentic spectrum, ambient, human-in-
the-loop, traces.

**Not an academic.** His canon is blog posts, OSS code, and
podcasts — not papers.

---

## Verbal tics and rhetorical moves

- **Definition-first opening.** Defines the term, then builds
  from the definition
- **Hedging filler:** "like," "kind of," "basically"
- **Position-staking escalator:** "I very, very strongly believe…"
- **Launch-into-explanation marker:** "So…"
- **X-is-a-Y, Z-is-a-W template:** "LangChain is a framework,
  LangGraph is a runtime, DeepAgents is a harness."
- **Triads:** predictions and frameworks come in threes —
  planning/UX/memory; model/harness/context; notify/question/review
- **Pivots away from definition wars:** "rather than arguing over
  which work to include or exclude as being a true AI agent…"
- **Closes with pragmatic advice** — "start simple, test in
  production, own the memory"

---

## Signature metaphor — the "beer taste" metaphor

> *"Agentic infrastructure does not make your beer taste better.
> Cognitive architectures absolutely make your beer taste better."*
— "Why you should outsource your agentic infrastructure…" blog

> *"Focus on what makes your beer taste better: cognitive
> architectures, not infrastructure."*

> *"Let you own the differentiating parts of your application and
> outsource the rest."*

This is his canonical "buy vs build" framing, applied to agent
stacks. Customers build the cognitive architecture; LangChain
sells the infrastructure.

---

## Verbatim quotes — sourced

### On what is an agent

> *"An AI agent is a system that uses an LLM to decide the control
> flow of an application."*
— "What is an AI agent?" blog (June 28, 2024)

> *"A system is more 'agentic' the more an LLM decides how the
> system can behave."*
— same blog

> *"Rather than arguing over which work to include or exclude as
> being a true AI agent, we can acknowledge that there are
> different degrees to which systems can be agentic."*
— same blog (endorsing Andrew Ng's framing)

> *"With an agent, there's some aspect of it where the LLM is
> kind of deciding what to do and what steps to do in what order."*
— Latent Space, September 2023

> *"An agent, by definition, is an LLM interacting with tools and
> other sources of data."*
— "Your harness, your memory" blog, April 11, 2026

### On cognitive architecture

> *"What I mean by cognitive architecture is how your system
> thinks."*
— "What is a cognitive architecture?" blog

> *"I like the word 'cognitive' because agentic systems rely on
> using an LLM to reason. I like the word 'architecture' because
> these agentic systems still involve engineering."*
— same blog

> *"The way that I think about a cognitive architecture is
> basically what's the system architecture of your LLM
> application?"*
— Sequoia Training Data, 2024

> *"Nearly all the advanced 'agents' we see in production have a
> very domain specific architecture."*
— "Planning for Agents" blog

> *"You'll probably want to experiment with different cognitive
> architectures just as frequently as you experiment with prompts."*
— "What is a cognitive architecture?" blog

### On context engineering

> *"Context engineering is building dynamic systems to provide the
> right information and tools in the right format such that the
> LLM can plausibly accomplish the task."*
— "The rise of 'context engineering'" blog (June 23, 2025)

> *"Most of the time when an agent is not performing reliably the
> underlying cause is that the appropriate context, instructions
> and tools have not been communicated to the model."*
— same blog

> *"Context engineering is becoming the most important skill an AI
> engineer can develop."*
— same blog

> *"LLMs are not mind readers — you need to give them the right
> context."*
— same blog

> *"Prompt engineering is a subset of context engineering."*
— same blog

> *"Everything's context engineering. Context engineering is such
> a good term."*
— Sequoia Training Data, long-horizon agents episode

### On Framework / Runtime / Harness taxonomy

> *"LangChain is an agent framework, LangGraph is an agent runtime,
> DeepAgents is an agent harness."*
— "Agent Frameworks, Runtimes, and Harnesses — oh my!" blog

> *"When you need to run agents in production, you will want some
> sort of runtime for agents."*
— same blog

> *"DeepAgents is the newest project we're working on. It is
> higher level than agent frameworks… It's more than a framework —
> it comes with batteries included."*
— same blog

> *"LangChain 1.0 is built on top of LangGraph to take advantage
> of the agent runtime it provides."*
— same blog

### On Deep Agents / Shallow Agents

> *"Using an LLM to call tools in a loop is the simplest form of
> an agent."*
— "Deep Agents" blog

> *"The dominant agent architecture to emerge is also the
> simplest: running in a loop, calling tools."*
— same blog

> *"'Shallow' here refers to the agents inability to plan over
> longer time horizons and do more complex tasks."*
— same blog

> *"The core algorithm is actually the same — it's an LLM running
> in a loop calling tools."*
— same blog

> *"People reach for subagents too soon. If your prompt is 20
> lines, you should expand it rather than outsource it."*
— "Deep Agents" blog (paraphrased from ODSC West 2025)

### On long-horizon agents, file systems, traces

> *"I very, very strongly believe that right now if you're
> building a long-horizon agent, you need to give it access to a
> file system."*
— Sequoia Training Data, long-horizon episode

> *"Traces just tell you what's in your context. And that's so
> important."*
— same episode

> *"You have these long-horizon agents, they're running for long
> periods of time… at some point you need to compact that."*
— same episode

> *"When you're building an agent, the logic for how your
> application works is not all in the code."*
— same episode

> *"You don't actually know what the context at step 14 will be,
> because there's 13 steps before that that could pull arbitrary
> things in."*
— same episode

> *"With agents, you don't know what the agent does before you
> ship it."*
— same episode

> *"You probably want to be testing online… behavior doesn't emerge
> until it's actually being used with real world inputs."*
— same episode

### On ambient agents & human-in-the-loop

> *"Ambient agents listen to an event stream and act on it
> accordingly, potentially acting on multiple events at a time."*
— "Introducing Ambient Agents" blog + Sequoia Training Data

> *"Ambient does not mean fully autonomous."*
— Sequoia AI Ascent 2025 keynote

> *"It should not (solely) be triggered by human messages."*
— "Introducing Ambient Agents" blog

> *"If an agent is running fully autonomously in the background,
> then it really can't make a mistake."*
— same blog

> *"A big part of working with someone else is communicating with
> them. Asking them questions when you're unsure."*
— same blog

> *"Having this human in the loop just gets better results."*
— Sequoia Training Data ambient episode

> *"An email agent… if you've emailed me in the past year or so,
> it's drafted a response or sent a calendar invite."*
— Sequoia Training Data ambient episode

### On memory, harness, continual learning (2026 flagship theme)

> *"Memory is incredibly important to creating good and sticky
> agentic experiences."*
— "Your harness, your memory" blog (April 11, 2026)

> *"Memory — and therefore harnesses — should be open, so that you
> own your own memory."*
— same blog

> *"Memory is important, and it creates lock in that they don't
> get from just the model."*
— same blog

> *"Without memory, your agents are easily replicable by anyone
> who has access to the same tools."*
— same blog

> *"Agent harnesses are not going away."*
— same blog

> *"If you use a closed harness, especially if it's behind an
> API, you don't own your memory."*
— same blog

> *"Learning can happen at three distinct layers: the model, the
> harness, and the context."*
— "Continual learning for AI agents" blog (April 5, 2026)

> *"All of these flows are powered by traces — the full execution
> path of what an agent did."*
— same blog

### On LangChain origin / philosophy / self-critique

> *"Almost exactly 3 years ago, I pushed the first lines of code
> to `langchain` as an open source package. There was no company
> at the time, and no grand plan for what the project would
> become."*
— "Reflections on Three Years of Building LangChain" (Oct 2025)

> *"A month later, ChatGPT launched, and everything for
> `langchain` changed."*
— same blog

> *"I was instantly fascinated by the technology but cannot claim
> to have had any idea how big LLMs would become."*
— same blog

> *"Model neutrality still remains one of the main benefits of our
> products."*
— same blog

> *"Building reliable agents is quite hard!"*
— same blog

> *"We traded power for ease of use."*
— same blog (self-critique of original LangChain)

> *"LangGraph was inspired by the limitations of the initial
> `langchain`."*
— same blog

> *"I saw some common abstractions in terms of what they were
> building, and then thought it would be a cool side project to
> factor out some of those common abstractions."*
— Latent Space, September 2023

> *"It was very crazy. I didn't know I was going to leave my
> previous job. I had no clue what I was going to do next."*
— Fortune, October 2025

> *"There's a ton of players. I like to say we have 500
> competitors and zero competitors."*
— Fortune, October 2025

### On planning, reasoning, and the limits of models alone

> *"Planning and reasoning by an agent involves the LLM's ability
> to think about what actions to take."*
— "Planning for Agents" blog

> *"The lowest hanging fix for improving planning is ensuring the
> LLM has all required information."*
— same blog

> *"We're basically saying: 'don't worry about planning, LLM,
> I'll do it for you!'"*
— same blog (on custom cognitive architectures)

> *"No matter how powerful the model becomes, you will always need
> to communicate what it should do."*
— same blog

> *"Prompting and custom architectures are here to stay."*
— same blog

### On observability / LangSmith

> *"I agree that those are big pain points that get exacerbated
> when you have these complex chains and agents where you can't
> really see what's going on inside of them."*
— Latent Space, September 2023

> *"The main use case we see for this is in debugging… as you
> have these more complex things, debugging what's actually going
> on becomes really painful."*
— Latent Space, September 2023

> *"You should be able to know what the agent has done. That
> seems like step one."*
— Sequoia Training Data, 2024

> *"There is no substitute for just like looking at the inputs and
> outputs."*
— Arize Observe

### On himself / vision

> *"It's so early on that there's so much to be built."*
— Sequoia Training Data, 2024

> *"My advice would just like build as many things as possible…
> it's still really early in the space."*
— Latent Space, September 2023

> *"GPT-5 is going to come out, and it will probably make some of
> the things you did not relevant."*
— Sequoia Training Data, 2024

> *"Our goal is to figure out what the agents of the future look
> like and build tools to facilitate that."*
— "Reflections on Three Years" blog

---

## Core framework vocabulary

- **Control flow** (the LLM decides it)
- **Cognitive architecture** (how the system thinks)
- **Harness / Framework / Runtime** (stack levels)
- **Context engineering** (dynamic systems + right info + right
  tools + right format)
- **Ambient** (vs chat; event-driven, background)
- **Agentic spectrum** (not binary)
- **Memory moat**
- **Traces** (the substrate for learning)
- **Human-in-the-loop** (notify / question / review)
- **Compact / compress** (context over long horizons)
- **Model neutrality**

## Banned / avoided framings

- **"Fully autonomous"** — ambient does not mean autonomous
- **Definition wars** — pivots to spectrum framing
- **Visual workflow builders** — dismisses directly
- **Closed harness APIs** — active 2026 target
- **AGI timelines** — not his register
- **Named-competitor attacks** — prefers taxonomy-by-category
- **Hype language** — uses "like," "kind of" as anti-hype tells

---

## Signature triads

He structures frameworks and predictions in threes:

- **3 layers of continual learning:** model, harness, context
- **3 HITL patterns:** notify, question, review
- **3 agent-stack levels:** framework, runtime, harness
- **3 agent predictions (Sequoia AI Ascent 2024):** planning, UX,
  memory
- **3 core Deep Agents primitives:** planning tool, sub-agents,
  file system
- **3 opening-post posts of 2026:** memory, continual learning,
  Interrupt preview

---

## Structural tics

### Opening moves
- Define the term first
- Acknowledge the meme / question is incomplete
- Pivot to spectrum or taxonomy framing

### Closing moves
- Recommend pragmatic next step (start simple; own memory; test
  in production)
- Invite the community to build on the primitive
- Point at a blog post for depth

---

## Sources consolidated

Primary:
- LangChain blog (40+ posts, author page
  langchain.com/blog/author/harrison)
- Latent Space (September 6, 2023) — "The Point of LangChain"
- Sequoia Training Data (3 episodes: 2024, 2025, 2026)
- No Priors (Episode 57, 2024)
- The MAD Podcast (March 12, 2026) — in-window
- TWIML AI (Ep. 698, August 19, 2024)
- Gradient Dissent (2023)
- Fortune (October 2025) — Series B coverage
- Arize Observe (2023)
- LangChain Interrupt 2025 keynote

Last verified: 2026-04-17.
