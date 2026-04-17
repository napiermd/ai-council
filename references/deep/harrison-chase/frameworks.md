# Frameworks: Harrison Chase

> Named frameworks and conceptual contributions. Each anchored to
> a specific blog post, OSS release, or verbatim quote.

---

## 1. LangChain (OSS framework, October 2022)

**The original.** Python (+ later JS/TS) library for composing LLM
calls, tools, retrievers, memory. First committed October 16, 2022;
`langchain` 0.0.1 live nine days later.

### Chase on its purpose
> *"I saw some common abstractions in terms of what they were
> building, and then thought it would be a cool side project to
> factor out some of those common abstractions."*

### Chase's self-critique
> *"We traded power for ease of use."*

LangChain v1.0 (October 20, 2025) is built on top of LangGraph to
resolve these limitations.

---

## 2. LangGraph (runtime, January 2024)

**Stateful agent orchestration.** OSS. Response to LangChain's
limitations.

### Core abstractions
- **State** — shared data structure (TypedDict or Pydantic model)
  passed between nodes, with reducer function
- **Nodes** — Python functions taking state, returning partial
  updates
- **Edges** — fixed or **conditional** transitions
- **StateGraph** — builder class; compiles to a runnable graph

### Checkpointer pattern
- Persists graph state at **every super-step** (BSP execution
  model)
- Backends: in-memory, SQLite, Postgres (production)
- Enables: human-in-the-loop interrupts, resumability after crash,
  time-travel debugging, per-thread memory

### Supervisor pattern
- Coordinator node decides which specialist sub-agent to invoke
  next via **tool-calling handoff**
- Packaged as `langgraph-supervisor-py`

### LangGraph vs LCEL
- **LCEL** = declarative pipe DSL, DAG only (no loops, no state)
- **LangGraph** = imperative graph API with cycles, conditional
  edges, explicit state, checkpoints, streaming, async, durable
  execution

### Chase's framing
> *"LangGraph was inspired by the limitations of the initial
> langchain."*

> *"When you need to run agents in production, you will want some
> sort of runtime for agents."*

---

## 3. LangSmith (platform, February 2024 GA)

**The "Agent Engineering Platform."** Observability + evaluation +
deployment.

### Three pillars
1. **Observability** — traces for debugging complex chains /
   agents. OpenTelemetry-native.
2. **Evaluation** — LLM-as-judge + human feedback + evaluator
   templates + pairwise scoring
3. **Deployment** — agent server with memory, conversational
   threads, durable checkpointing

### Fleet
**LangSmith Fleet** — no-code agent builder for enterprise
(renamed from Agent Builder in March 2026). Supports:
- MCP server extensibility
- Skills (specialized knowledge modules)
- Sandboxes (private preview, secure code execution)
- ABAC (attribute-based access control)
- Audit logs

### Scale
- **1B+ events/day**
- **12× YoY trace volume growth**

### Chase's philosophical stance
> *"You should be able to know what the agent has done. That
> seems like step one."*

> *"There is no substitute for just like looking at the inputs and
> outputs."*

---

## 4. DeepAgents (harness, 2025)

**His newest named framework.** OSS package `deepagents`.

### Definition
> *"A deep agent is just a prompt, a list of tools, and a set of
> subagents."*

Plus: **file system state**.

### Inspiration
Claude Code's ~2,000-line system prompt. Chase studied it and
extracted the pattern.

### Four components
1. **Planning tool**
2. **Sub-agents** (with context isolation + summary compression)
3. **File system** (as persistent state)
4. **Detailed system prompt**

### Chase's framing
> *"The dominant agent architecture to emerge is also the simplest:
> running in a loop, calling tools."*

> *"The core algorithm is actually the same — it's an LLM running
> in a loop calling tools."*

### Product family
- **Deep Agents v0.5** — April 7, 2026
- **Deep Agents Deploy** — April 9, 2026, *"an open alternative
  to Claude Managed Agents"*

---

## 5. Cognitive Architecture (concept, 2024)

**His signature conceptual contribution.**

### Definition
> *"What I mean by cognitive architecture is how your system
> thinks."*

> *"I like the word 'cognitive' because agentic systems rely on
> using an LLM to reason. I like the word 'architecture' because
> these agentic systems still involve engineering."*

### Claim
> *"Nearly all the advanced 'agents' we see in production have a
> very domain specific architecture."*

### Implication — the "beer taste" framing
> *"Agentic infrastructure does not make your beer taste better.
> Cognitive architectures absolutely make your beer taste better."*

Customers build the cognitive architecture; LangChain sells the
infrastructure.

---

## 6. Context Engineering (concept, June 2025)

**His category-defining move.**

### Definition (verbatim)
> *"Context engineering is building dynamic systems to provide the
> right information and tools in the right format such that the
> LLM can plausibly accomplish the task."*

### Claim
> *"Context engineering is becoming the most important skill an AI
> engineer can develop."*

> *"Prompt engineering is a subset of context engineering."*

### Overlap with Kiela
Both Chase and Kiela use "context engineering" — **parallel
evolution, not shared derivation.** Chase's post credits Tobi
Lutke, Ankur Goyal, Walden Yan, Dex Horthy; no reference to Kiela.

**Difference in framing:**
- **Kiela:** infrastructure category (the "context layer"),
  subsuming RAG + MCP + prompting
- **Chase:** orchestrator-layer discipline — what goes in the LLM's
  context window at each step of a stateful workflow

---

## 7. Framework / Runtime / Harness taxonomy (2026)

**His stack-levels framing.**

> *"LangChain is an agent framework, LangGraph is an agent runtime,
> DeepAgents is an agent harness."*

### Framework
- **Library of primitives.** LangChain, CrewAI, LlamaIndex
- Low opinion, high flexibility

### Runtime
- **Stateful execution engine.** LangGraph
- Adds state, checkpoints, resumability

### Harness
- **Opinionated agent with prompt + tools + subagents + file
  system.** DeepAgents, Claude Code, Cursor
- High opinion, batteries included

---

## 8. Agentic Spectrum (concept, 2024, endorsing Andrew Ng)

**His refusal to litigate the "is this an agent?" question.**

Instead of a binary, a spectrum of agentic-ness:
1. **Router** — LLM picks a downstream workflow
2. **State Machine** — LLM controls transitions between states
3. **Autonomous Agent** — LLM decides the full loop
4. (implicit higher)

> *"A system is more 'agentic' the more an LLM decides how the
> system can behave."*

### Empirical claim
**73% of production LangChain systems are chains, not agents.**
Most teams should start simpler.

---

## 9. Ambient Agents (concept, 2025, Sequoia AI Ascent)

**His UX-primitive framing.**

### Definition
> *"Ambient agents listen to an event stream and act on it
> accordingly, potentially acting on multiple events at a time."*

### Key distinction
> *"Ambient does not mean fully autonomous."*

### Three human-in-the-loop patterns
1. **Notify** — "I did X"
2. **Question** — "should I do X?"
3. **Review** — "X is ready; approve or edit"

### UX primitive — Agent Inbox
Modeled on email + ticketing. Open-sourced around Sequoia AI
Ascent 2025 (May 2, 2025).

---

## 10. Memory / "Your Harness, Your Memory" (thesis, April 2026)

**His active 2026 fight.**

### Claims
> *"Memory is incredibly important to creating good and sticky
> agentic experiences."*

> *"Memory is important, and it creates lock in that they don't
> get from just the model."*

> *"Without memory, your agents are easily replicable by anyone
> who has access to the same tools."*

### Prescription
> *"Memory — and therefore harnesses — should be open, so that you
> own your own memory."*

### Product response
- **LangMem SDK** (February 27, 2025)
- **DeepAgents memory-harness integration**

---

## 11. Continual Learning in Three Layers (April 2026)

**His learning-architecture framing.**

> *"Learning can happen at three distinct layers: the model, the
> harness, and the context."*

- **Model weights** — catastrophic forgetting makes this unsolved
- **Harness** — rules, skills, subagents, memory retrieval
- **Context** — what gets pulled into the window this turn

### Traces as the substrate
> *"All of these flows are powered by traces — the full execution
> path of what an agent did."*

Positions LangSmith as the substrate for self-improving harnesses.

---

## 12. Multi-Agent Patterns (2024–2026)

Three named patterns, all packaged in LangGraph:

### Supervisor
Central coordinator + specialized workers. Communication via
tool-calling handoff. Package: `langgraph-supervisor-py`.

### Hierarchical teams
Supervisors of supervisors. Compositions of Supervisor pattern.

### Swarm
Peer-to-peer handoffs. No central coordinator. Package:
`langgraph-swarm-py`.

### Chase's response to Cognition's "Don't Build Multi-Agents"
> *"We think LangGraph is really great for enabling completely
> custom context engineering — but we want to make it even
> better."*

Agreed with the critique of naive parallel multi-agents; pushed
back on the absolutist framing.

---

## 13. Durable Execution / Stateful Workflows

**LangGraph's core differentiator.**

- Checkpointing at every step
- Postgres-backed state for production
- Resumability after crash
- Time-travel debugging
- Per-thread memory
- BSP-style (Bulk Synchronous Parallel) execution model

---

## 14. Triadic frameworks (recurring pattern)

He reaches for threes reliably:

| Framework | Triad |
|-----------|-------|
| **Continual learning** | model, harness, context |
| **HITL patterns** | notify, question, review |
| **Stack levels** | framework, runtime, harness |
| **Agent predictions (2024)** | planning, UX, memory |
| **Deep Agents primitives** | planning tool, sub-agents, file system |

This is a reliable structural tic — when in doubt, count to three.

---

## 15. "Agent Engineer" as emerging profession (Interrupt 2025)

Confirmed via multiple secondary summaries. Three pillars:
- **Prompting**
- **Engineering** (code, state, observability)
- **Product sense + ML literacy**

Positions LangChain's products (framework + runtime + harness)
as the toolchain for this emerging profession.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: LangChain blog + 3 research agents + direct
  verification of April 2026 posts.
- Status: comprehensive; each framework anchored to a specific
  post, release, or quote.
