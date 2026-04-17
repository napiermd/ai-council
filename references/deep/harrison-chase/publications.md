# Publications: Harrison Chase

> Chase is not an academic author. His canon is **blog posts** on
> the LangChain blog, the "In the Loop" series, OSS commits, and
> conference talks. No peer-reviewed papers or arXiv preprints
> with him as first author.

---

## Scholar footprint

**No Google Scholar profile.** Not applicable — his written output
is not peer-reviewed academic publication.

---

## Canonical blog posts (author: Chase)

All at `https://www.langchain.com/blog/` (formerly
`blog.langchain.dev`, now redirecting).

### 1. "What is an AI agent?" (June 28, 2024)
**The definitional reference.** Canonical LangChain-house framing.

Key quotes:
- *"An AI agent is a system that uses an LLM to decide the control
  flow of an application."*
- *"A system is more 'agentic' the more an LLM decides how the
  system can behave."*
- Endorses Andrew Ng's spectrum framing.

### 2. "What is a 'cognitive architecture'?" (2024)
Introduces his signature term for the system design around an LLM.

- *"What I mean by cognitive architecture is how your system
  thinks."*
- *"I like the word 'cognitive' because agentic systems rely on
  using an LLM to reason. I like the word 'architecture' because
  these agentic systems still involve engineering."*

### 3. "Why you should outsource your agentic infrastructure, but own your cognitive architecture" (2024)
**Home of the "beer taste" metaphor.**

- *"Agentic infrastructure does not make your beer taste better.
  Cognitive architectures absolutely make your beer taste better."*

### 4. "Planning for Agents" (July 20, 2024)
Planning, reflection, tools as the three core primitives.

- *"Planning and reasoning by an agent involves the LLM's ability
  to think about what actions to take."*
- *"The lowest hanging fix for improving planning is ensuring the
  LLM has all required information."*
- *"No matter how powerful the model becomes, you will always need
  to communicate what it should do."*

### 5. "State of AI Agents" Report (November 2024)
First edition; 1,300+ respondents.

- **51% of respondents had agents in production**
- Mid-sized companies (100–2000 employees) leading adoption at 63%
- Cursor, Perplexity, Replit cited as most-talked-about agent
  apps

A 2025 follow-up ("State of Agent Engineering 2025") exists.

### 6. "The rise of 'context engineering'" (June 23, 2025)
**His category-defining post.**

- *"Context engineering is building dynamic systems to provide
  the right information and tools in the right format such that
  the LLM can plausibly accomplish the task."*
- Credits (in the post): Tobi Lutke, Ankur Goyal, Walden Yan, Dex
  Horthy
- **No reference to Kiela** — parallel evolution, not derived

### 7. "Introducing Ambient Agents" (2025)
Three human-in-the-loop primitives: notify, question, review.
Agent Inbox as the UX pattern.

- *"Ambient agents listen to an event stream and act on it
  accordingly."*
- *"Ambient does not mean fully autonomous."*
- *"If an agent is running fully autonomously in the background,
  then it really can't make a mistake."*

### 8. "Deep Agents" (2025)
Four components: planning tool, sub-agents, file system, detailed
system prompt.

- *"Using an LLM to call tools in a loop is the simplest form of
  an agent."*
- *"'Shallow' here refers to the agents inability to plan over
  longer time horizons and do more complex tasks."*
- *"People reach for subagents too soon. If your prompt is 20
  lines, you should expand it rather than outsource it."*

### 9. "Not Another Workflow Builder" (October 2025)
Argues code wins at high complexity, no-code / NL wins at low
barrier, visual builders fail both ends.

- *"I am not excited about visual workflow builders. Not simple
  enough for the average user. Not scalable for complex use
  cases."*

### 10. "OpenAI's Bet on a Cognitive Architecture" (November 2023)
Commentary on GPTs launch.

### 11. "You don't know what your agent will do until it's in production" (February 2026)
Pinned X tweet links to this. Production monitoring thesis.

- *"Agents accept natural language input, where the space of
  possible queries is unbounded… Production monitoring for agents
  requires monitoring the inputs and outputs themselves, not just
  the system metrics around them."*
- *"Human reviewers can meaningfully assess 50-100 traces per
  hour, but at 1,000 requests per day, full manual review would
  require 10-20 hours of dedicated human time, daily."*

### 12. "Agent Frameworks, Runtimes, and Harnesses — oh my!" (2025/2026)
**The taxonomy post.**

- *"LangChain is an agent framework, LangGraph is an agent runtime,
  DeepAgents is an agent harness."*

### 13. "Reflections on Three Years of Building LangChain" (October 20, 2025)
Co-timed with Series B + v1.0.

- *"Almost exactly 3 years ago, I pushed the first lines of code
  to `langchain` as an open source package."*
- *"A month later, ChatGPT launched, and everything for `langchain`
  changed."*
- *"LangGraph was inspired by the limitations of the initial
  `langchain`."*
- *"We traded power for ease of use."*
- *"Model neutrality still remains one of the main benefits of our
  products."*
- *"Building reliable agents is quite hard!"*

### 14. "Continual learning for AI agents" (April 5, 2026)
**Three-layer thesis:** model, harness, context.

- *"Learning can happen at three distinct layers: the model, the
  harness, and the context."*
- *"All of these flows are powered by traces — the full execution
  path of what an agent did."*

### 15. "Your harness, your memory" (April 11, 2026) — **FLAGSHIP 2026 POST**

- *"Agent harnesses are not going away."*
- *"Managing context, and therefore memory, is a core capability
  and responsibility of the agent harness."*
- *"If you use a closed harness, especially if it's behind an API,
  you don't own your memory."*
- *"This is incredibly alarming — it means that memory will become
  locked into a single platform, a single model."*
- *"Without memory, your agents are easily replicable by anyone
  who has access to the same tools. With memory, you build up a
  proprietary dataset."*

Names **Claude Managed Agents** and **OpenAI Responses API** as
the "worst" tier of closed-harness lock-in.

---

## Additional meaningful posts

### "MCP: Flash in the Pan or Future Standard?" (LangChain blog debate)
- Chase took the **pro-MCP** side
- His employee **Nuno Campos** (LangGraph lead) took the skeptical
  side — a rare public intra-team debate

### "How to think about agent frameworks"
- *"Nearly all of the 'agentic systems' we see in production are
  a combination of 'workflows' and 'agents'."*
- *"You should use workflows when you can use workflows."*
- *"Any framework that makes it harder to control exactly what is
  being passed to the LLM is just getting in your way."*

### "Previewing Interrupt 2026: Agents at Enterprise Scale" (April 9, 2026)
Conference preview.

---

## Teaching (co-authored with Andrew Ng)

DeepLearning.AI short courses:
- **"LangChain for LLM Application Development"**
- **"Functions, Tools and Agents with LangChain"**
- **"Build an Agent with LangGraph"**

These are the canonical intro curriculum for anyone starting with
LangChain.

---

## OSS corpus (his real "publications")

- **langchain** (Python) — first committed October 16, 2022 by
  hwchase17
- **langchainjs** (TypeScript) — February 2023
- **langgraph** — January 2024 (v0.1 June 2024; v1.0 October 2025)
- **langgraph-supervisor-py** — supervisor multi-agent pattern
- **langgraph-swarm-py** — swarm multi-agent pattern
- **langgraph-checkpoint-postgres** — production state persistence
- **langmem** — memory SDK (February 27, 2025)
- **deepagents** — harness abstraction (2025)

---

## Public report series

- **"State of AI Agents"** (November 2024, 1,300+ respondents)
- **"State of Agent Engineering"** (2025 follow-up)

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: LangChain blog + 2 research agents.
- Status: comprehensive — his corpus is blog-post + OSS, fully
  inventoried through April 2026.
