# Deep Profile: Harrison Chase

**Role in council:** Agent-orchestration anchor. The voice that
designs multi-step, stateful, human-in-the-loop LLM workflows.
When the question is "how do we actually run this in production
with handoffs, memory, failure handling, and checkpoints?" — he
is the anchor.

**Canonical fact:** Co-founder and CEO of LangChain. Author of the
LangChain framework (first committed late 2022). Author of
**LangGraph** (stateful agent orchestration) and **LangSmith**
(observability / eval / deployment). Most-invited podcast guest on
AI agents in 2024-2026. Prolific blog author on agent
architecture patterns.

---

## Quick facts

- **Current roles:** Co-founder and CEO, LangChain
- **Co-founder (CTO):** Ankush Gola
- **Current product lineup (2026):**
  - **LangChain OSS** — Python + JS/TS framework
  - **LangGraph** — stateful agent orchestration (OSS)
  - **LangSmith Platform** — "Agent Engineering Platform"
    (observability + evaluation + deployment)
  - **Deep Agents** — long-running autonomous agents ("Deep Agents
    Deploy: an open alternative to Claude Managed Agents")
  - **LangSmith Fleet** — no-code agent builder for enterprise
- **Enterprise customers (named, 2026):** Klarna, Vanta, Rippling,
  Lyft, Harvey, Cloudflare, Home Depot, Workday, Cisco, LinkedIn,
  Coinbase, Monday.com, Podium, ServiceNow, C.H. Robinson
- **Tagline:** "Ship agents that work"
- **LangChain Interrupt 2026** — annual conference ("Agents at
  Enterprise Scale")
- **X / Twitter:** @hwchase17 (very high volume)

---

## Cadence + caveats

**Framework churn baggage.** LangChain has been publicly criticized
for API churn (LCEL → LangGraph migrations, deprecation patterns).
The roster note already flags this. Invoke him for agent-state-flow
design, not as a blanket framework endorsement.

**Context engineering vocabulary overlap with Kiela.** Both Chase
and Kiela use "context engineering." The framing differs:
- **Kiela:** context engineering subsumes RAG + MCP + prompting
  into an infrastructure category (the "context layer")
- **Chase:** context engineering is an agent-architecture pattern
  — what to put in the LLM's context window at each step of a
  stateful workflow

The terms rhyme but are not identical. When invoking both in a
session, clarify which framing is in play.

---

## File structure

- `README.md` — this file
- `embodiment.md` — persona invocation for LLM roleplay
- `voice.md` — verbatim quotes, cadence, recurring phrasings
- `biography.md` — education, career arc, LangChain founding
- `frameworks.md` — named frameworks (LangChain, LangGraph,
  LangSmith, Deep Agents, Fleet, context-engineering patterns,
  ambient agents, agent evaluation)
- `publications.md` — blog-post canon + any papers / talks
- `appearances.md` — podcasts, conference talks, keynotes
- `positions.md` — strong positions, disagreements (Cognition AI
  multi-agent debate, Anthropic "Building Effective Agents"
  response), predictions
- `recent-30d.md` — last-30-days signal window (high cadence —
  daily X posts + 2 in-window Chase-authored blog posts)

---

## When to invoke Chase in council

- **Agent state design** — nodes, edges, conditional edges,
  checkpointers, supervisors
- **Multi-agent vs single-agent** architecture decisions
- **Human-in-the-loop** checkpoint placement
- **Agent memory** — short-term vs long-term, continual learning
- **Agent evaluation** — LLM-as-judge, evaluators, evaluator
  templates
- **Agent observability** — tracing, debugging, failure modes
- **Ambient agents** vs chat agents distinction
- **Enterprise agent deployment** — harnesses, fleets, deploy
- **Handoffs** between agents
- Framework-level questions about LangGraph design tradeoffs

## When NOT to invoke Chase

- Pure model-quality / training questions (use Karpathy / Liang)
- Pure retrieval / grounding architecture (use Kiela)
- Clinical-specific safety (use Bitterman)
- Production inference ops at scale (use Huyen)
- "Which framework should I use?" — he'll answer "LangChain" and
  the question needs a neutral comparison

---

## Last reviewed

- Reviewed: 2026-04-17
- Status: deep profile under construction (scaffolding in place)
