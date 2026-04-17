# Positions: Harrison Chase

> Strong public positions, disagreements, predictions. Each item
> sourced to a verifiable blog post, tweet, or podcast quote.

---

## His signature 2026 line — "Your harness, your memory"

**Source:** April 11, 2026 flagship blog post at
www.langchain.com/blog/your-harness-your-memory.

> *"Agent harnesses are not going away."*

> *"Managing context, and therefore memory, is a core capability
> and responsibility of the agent harness."*

> *"If you use a closed harness, especially if it's behind an API,
> you don't own your memory."*

> *"This is incredibly alarming — it means that memory will become
> locked into a single platform, a single model."*

> *"Without memory, your agents are easily replicable by anyone who
> has access to the same tools. With memory, you build up a
> proprietary dataset."*

This is his active 2026 fight. Directly names **Anthropic's Claude
Managed Agents** and the **OpenAI Responses API pattern** as the
"worst" tier of closed-harness lock-in. The DeepAgents product is
the architectural rebuttal.

---

## Position 1: What is an agent?

**Source:** "What is an agent?" (November 13, 2024, evergreen
reference).

> *"An AI agent is a system that uses an LLM to decide the control
> flow of an application."*

**Rejects the binary.** Endorses Andrew Ng's spectrum framing:

> *"A system is more 'agentic' the more an LLM decides how the
> system can behave."*

**Four-level autonomy ladder:**
1. Router
2. State Machine
3. Autonomous Agent
4. (implicit higher)

---

## Position 2: Context engineering (his definition)

**Source:** "The rise of 'context engineering'" (June 23, 2025).

> *"Context engineering is building dynamic systems to provide the
> right information and tools in the right format such that the
> LLM can plausibly accomplish the task."*

> *"Most of the time when an agent is not performing reliably the
> underlying cause is that the appropriate context, instructions
> and tools have not been communicated to the model."*

> *"Providing complete and structured context to the AI is far more
> important than any magic wording."*

> *"LLMs are not mind readers — you need to set them up for
> success."*

**Credits (in the post):** Tobi Lutke, Ankur Goyal, Walden Yan,
Dex Horthy. **No reference to Kiela** — the shared vocabulary is
parallel evolution, not one derived from the other.

### Note on Kiela overlap
Chase and Kiela both use "context engineering" but the framings
differ. **Kiela:** context engineering as infrastructure category
(the "context layer"), subsuming RAG + MCP + prompting.
**Chase:** context engineering as an orchestrator-layer discipline
— what to put in the LLM's context window at each step of a
stateful workflow. Both frames can coexist; in a council session,
clarify which is active.

---

## Position 3: Workflows + agents, not workflows vs agents

**Source:** "How to think about agent frameworks" +
endorsement of Anthropic's "Building Effective Agents" (Dec 2024).

> *"Nearly all of the 'agentic systems' we see in production are a
> combination of 'workflows' and 'agents'."*

> *"You should use workflows when you can use workflows."*

> *"Any framework that makes it harder to control exactly what is
> being passed to the LLM is just getting in your way."*

**73% of production LangChain systems are chains, not agents** —
his empirical claim that most teams should start simpler.

---

## Position 4: Memory is the moat

**Source:** Sequoia Training Data podcast, January 2026 —
"Context Engineering Our Way to Long-Horizon Agents."

> *"That's where memory, I think, can be a real moat."*

**The structural argument:**
- Models are commoditizing
- Agents are easily replicable by anyone with access to the same
  tools
- Memory is the proprietary dataset that accumulates with use
- **Therefore:** memory ownership is the durable competitive
  advantage, and closed-harness APIs steal it from you

---

## Position 5: Continual learning happens in three layers

**Source:** "Continual learning for AI agents" (April 5, 2026).

> *"Learning can happen at three distinct layers: the model, the
> harness, and the context."*

- **Model weights** — catastrophic forgetting makes this unsolved
  for agents
- **Harness** — rules, skills, subagents, memory retrieval
- **Context** — what gets pulled into the window this turn

> *"All of these flows are powered by traces — the full execution
> path of what an agent did."*

Positions LangSmith traces as the substrate for self-improving
harnesses — the data flywheel is his.

---

## Position 6: Ambient agents, not chat

**Source:** "Introducing ambient agents" + Sequoia AI Ascent talk
(May 2, 2025).

Ambient agents *"listen to an event stream and act on it
accordingly"* — potentially thousands running concurrently.

**Three human-in-the-loop patterns:**
- **Notify** — "I did X"
- **Question** — "should I do X?"
- **Review** — "X is ready; approve or edit"

> *"Rather than forcing users into new chat windows, these agents
> help save your attention for when it matters most."*

**UX primitive:** the **Agent Inbox** — modeled on email + ticketing.

---

## Position 7: Pragmatic multi-agent (not naive)

**Source:** response to Cognition AI's "Don't Build Multi-Agents"
(Walden Yan, June 2025).

**Not a scorched-earth rebuttal — co-opt and reframe:**

> *"We think LangGraph is really great for enabling completely
> custom context engineering — but we want to make it even
> better."*

**Agrees with Cognition:** naive parallel multi-agents without
context sharing are broken.

**Disagrees with Cognition:** the fix is not "don't build
multi-agents" — the fix is proper state management + context
compression.

**DeepAgents product answer:** subagents with **context isolation
and summary compression**:
> *"Subagent work doesn't clutter the main agent's context, and
> large subtask context is compressed into a single result for
> token efficiency."*

---

## Position 8: Evaluation is pairwise / arena-style, not
independent scoring

**Source:** "You don't know what your agent will do until it's in
production" + LangSmith product direction.

> *"Human reviewers can meaningfully assess 50-100 traces per hour,
> but at 1,000 requests per day, full manual review would require
> 10-20 hours of dedicated human time, daily."*

**The operational consequence:**
- Pairwise / arena-style judges scale better than independent
  scoring
- LLM-as-judge + human feedback, not human review alone
- Regression testing built into the eval loop

---

## Position 9: Agents require production-grade observability

**Source:** Pinned X tweet (Feb 26, 2026) linking to "You don't
know what your agent will do until it's in production."

> *"Agents accept natural language input, where the space of
> possible queries is unbounded… Production monitoring for agents
> requires monitoring the inputs and outputs themselves, not just
> the system metrics around them."*

LangSmith's 1B+ events/day is the operational embodiment of this
claim.

---

## Position 10: I am not excited about visual workflow builders

**Source:** LinkedIn post (October 2025, continues to circulate).

> *"I am not excited about visual workflow builders.
> 1. Not simple enough for the average user. I believe there should
>    be a simpler way to create, modify, and adapt no-code agents.
> 2. Not scalable for complex use cases."*

**His synthesis:** code (LangGraph) wins at high complexity; fleet
+ natural-language builders win at low barrier. Visual block-
builders fail at both ends.

---

## Position 11: MCP is useful, but scoped

**Source:** LangChain blog debate "MCP: Flash in the Pan or Future
Standard?"

Chase took the **pro-MCP** side.

> *"MCP is useful when you want to bring tools to an agent you
> don't control."*

**Analogy:** MCP is to agents what Zapier is to SaaS — value is in
the long-tail of integrations, not the hot center.

**Notable:** his own LangGraph lead **Nuno Campos** took the
skeptical side. A rare public intra-team disagreement.

---

## Position 12: Harness > Framework > Runtime

**Source:** X thread, October 2025 — "Agent Framework vs Runtime
vs Harness."

> *"A term I've heard recently is agent 'harness'. We're building
> DeepAgents to be that. I wrote a blog on my interpretation of
> that term and how it differs from 'framework' (LangChain) and
> 'runtime' (LangGraph)."*

**Stack levels:**
- **Framework:** LangChain (library of primitives)
- **Runtime:** LangGraph (stateful execution engine)
- **Harness:** DeepAgents (opinionated agent with prompt + tools
  + subagents + file system)

---

## Competitive positioning (public)

### DSPy
Chase publicly calls DSPy *"the best framework"* for optimization.
No spat — they don't compete. LangGraph is orchestration, DSPy is
optimization.

### CrewAI, OpenAI Agents SDK
Grouped as **"agent abstractions"** — easy start, low ceiling.

### AutoGen, LlamaIndex
Listed in comparison matrices without direct attack.

### Cognition AI (Devin)
Friendly disagreement on multi-agent (see Position 7).

### Anthropic "Building Effective Agents"
**Endorsement, not disagreement.** Chase built the LangGraph
taxonomy to mirror it.

### Anthropic Claude Managed Agents / OpenAI Responses API
**Active 2026 fight.** Named as "worst" tier of closed-harness
lock-in.

### Visual workflow builders (n8n, Zapier-for-agents)
Publicly hostile — "not simple enough, not scalable."

### Company-positioning quote
> *"There's a ton of players. I like to say we have 500
> competitors and zero competitors."*
— Chase to Fortune, October 2025

---

## Predictions / bets

1. **Harnesses eat frameworks.** LangChain + LangGraph +
   DeepAgents = the vertical stack he's betting on.
2. **Memory is the moat.** Proprietary memory beats proprietary
   model for enterprise defensibility.
3. **Open harness wins over closed harness.** Bet against Claude
   Managed Agents and OpenAI Responses API as long-term
   architectures.
4. **Context engineering replaces prompt engineering** as the core
   discipline.
5. **Ambient agents + Agent Inbox is the UX future.** Chat is not
   the endgame.
6. **Most production agent systems stay as chains** (~73%).
   Empirical claim he uses against over-engineering.
7. **2026 = "year of agent orchestration at enterprise scale"**
   (Interrupt 2026 framing).
8. **Workflows + agents are complementary, not rivals.**
9. **DSPy + LangGraph converge but don't merge.** Agent stacks
   have both optimization and orchestration layers.
10. **Traces become training data for continual learning.**
    Observability → self-improvement pipelines.

---

## Signature refusals

Things he has been asked about but does not publicly endorse:

- **Closed harness APIs as a long-term architecture** — rejected
- **Pure agent abstractions without context control** — rejected
- **Visual workflow builders** — rejected
- **"Don't build multi-agents"** (Cognition framing) — rejected as
  absolutist
- **AGI timelines** — not his register
- **Pause petitions** — not a signatory
- **Naming specific competitors as enemies** — prefers framing by
  category ("harness," "framework," "abstraction") over personal

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 1 research agent + direct verification of April
  2026 blog posts.
- Status: embodiment-grade — verbatim positions with public
  sources.
