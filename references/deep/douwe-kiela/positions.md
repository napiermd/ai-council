# Positions: Douwe Kiela

> Strong public positions, refusals-to-endorse, disagreements, and
> predictions. Each item sourced to a verifiable post, interview,
> or paper.

---

## His signature line — "RAG is dead, long live RAG"

**Source:** LinkedIn, Spring 2025 (activity-7315765607415652353);
Contextual AI blog "Is RAG Dead Yet?" at isragdeadyet.com.

Verbatim from LinkedIn:
> "Every time a new model drops with an expanded context window
> (like Meta's impressive Llama 4 Scout with its 10M token capacity),
> I see the inevitable 'RAG is dead' posts flooding my feed. But
> this fundamentally misunderstands what RAG is about.
>
> When we developed RAG five years ago, we weren't creating a
> workaround for small context windows — we were designing a
> principled approach to augment models with external knowledge.
>
> The core enterprise challenges RAG addresses remain unsolved with
> just larger context windows:
> - Accessing private data and knowledge
> - Overcoming outdated knowledge
> - Reducing hallucinations and providing strong attributions
>
> The most sophisticated AI systems don't choose between either RAG,
> or long context, or fine-tuning, or MCP — they strategically
> combine these complementary approaches. Stop believing in false
> dichotomies."

This is his canonical rebuttal pattern: **every time someone declares
a retrieval concept dead, he restates the enterprise problem it was
designed to solve.**

---

## Position 1: RAG 2.0 > "Frankenstein RAG"

**Source:** Contextual AI blog "Introducing RAG 2.0" (March 19,
2024); SaaStr AI Day summary.

> Traditional RAG is a *"Frankenstein's monster of generative AI:
> the individual components technically work, but the whole is far
> from optimal."*

**What RAG 2.0 means, operationally:** Contextual AI *"pre-trains,
fine-tunes, and aligns all components as a single integrated system,
backpropagating through both the language model and the retriever."*
End-to-end trainable, not modular off-the-shelf pieces glued
together.

**Who this is aimed at (implicitly):** LangChain, LlamaIndex,
pgvector-first stacks, and the "three retrievers + a reranker +
GPT-4" pattern.

**When he invokes it:** Any conversation about enterprise RAG
architecture. Any vendor comparison. Any "we're using RAG" vague
framing.

---

## Position 2: RAG + long context, not RAG *vs* long context

**Source:** Contextual AI blog "Is RAG Dead Yet?"; DataCamp /
Madrona interviews, 2024-2025.

> "Enterprise knowledge bases are terabytes or petabytes, not
> tokens."

Even 10M-token windows capture *"a tiny fraction of your available
information."* Performance degrades *"long before models reach their
official limits."* Stuffing context also blows up latency and cost.

**His analogy:** *"Do you read an entire textbook every time you
need to answer a simple question?"*

**The optimal architecture, per Kiela:** *"RAG plus long context
models. You use RAG to efficiently narrow down to the most relevant
information, then leverage the model's long context capabilities on
that sensibly sized window."*

**Acknowledged tradeoff:** *"RAG systems are annoying to build, and
long context systems are easy. But if you can make RAG easy too,
it's much more efficient."*

---

## Position 3: Models are commoditized; data and context are the moat

**Source:** Madrona interview; DataCamp/HumanX framings.

> *"What makes a company a company is its data, and the expertise
> around that data and institutional knowledge."*

> *"The model is almost commoditized at this point. The bottleneck
> is context."*

**Implication:** Frontier-model competition is the wrong battlefield
for enterprise. The defensible moat is context infrastructure.

**When he invokes it:** Any "we're going to build our own model"
enterprise conversation. Any "GPT-5 changes everything" framing.

---

## Position 4: Systems > models (models are 10–20% of solutions)

**Source:** SaaStr AI Day summary.

Models are *"10–20% of solutions."* Specialization beats
generalization on cost and quality for bounded enterprise tasks.
Deployment, security, and grounding often matter more than raw
model accuracy.

---

## Position 5: Hallucination is a feature of general LMs, a bug in RAG

**Source:** Madrona interview (March 26, 2025).

> *"Hallucination is arguably a feature for a general purpose
> language model, it's not a bug… It's a bad thing if you have a
> RAG problem and you cannot afford to make a mistake."*

His technical definition of hallucination (verbatim):
> *"The generation of a language model not grounded in the context
> that is given."*

**Corollary:** Grounded Language Models (GLMs) are *"fine-tuned
specifically to answer only from retrieved passages"* — i.e.,
explicitly non-creative. This is the architectural expression of
his position that generation should be retrieval-constrained in
enterprise contexts.

---

## Position 6: Sentence-level attribution as an enterprise non-negotiable

**Source:** Contextual AI platform documentation + public blog.

Every response ships with *"sentence-level citations showing exactly
where information originated."* Attribution is not a feature flag;
it is a default.

**Why it matters to him:** Auditability is a precondition for
regulated-industry deployment. He repeatedly stresses
*"the inevitability of AI errors and the importance of audit trails
and uncertainty estimation."*

---

## Position 7: Evaluation is broken (the Dynabench origin thesis)

**Source:** Contextual AI blog "Plotting Progress in AI" (July 2023);
Dynabench NAACL 2021.

> *"The last few years have seen relentless progress in what AI can
> do, yet our ability to gauge these abilities has never been
> worse."*

> *"Evaluation is very boring. People don't seem to care about it."*
> (Madrona)

**His move:** Dynabench — human-and-model-in-the-loop adversarial
data creation. Static benchmarks saturate faster than we replace
them; the fix is dynamic evaluation.

---

## Position 8: Context engineering subsumes RAG + MCP

**Source:** The New Stack interview (January 27, 2026); X posts late
2025 / early 2026.

> *"I think people have rebranded it now as context engineering,
> which includes MCP and RAG."*

> *"The 'R' in RAG just stands for 'retrieval.' So, if you're using
> MCP to do your retrieval, then it's basically RAG, right?"*

**Context layer framing (verbatim X post):**
> *"What is a context layer? It is the infrastructure between data
> sources (the 'data layer') and language models (the 'intelligence
> layer'). Delivering real value with agents increasingly depends
> on giving them the right context at the right time."*

**Why this matters:** He is actively evolving the terminology from
"RAG 2.0" → "context engineering" → "context layer" as a durable
infra category. The argument is the same; the branding is sharper.

---

## Position 9: Boring workflows beat sexy agents in production

**Source:** X status 1961158289817026660 (cross-posted to LinkedIn
activity-7366923979434942464-vOjT).

> *"Everyone wants to work with the company that promises the
> 'sexy' AI agent, but ends up deploying the 'boring' workflow in
> production instead. I've been hearing this a lot from customers
> recently. The reality is that workflows will become more agentic
> over time."*

**The bet:** Production will run disciplined workflows that
gradually acquire agentic properties — not the other way around.

---

## Position 10: "Context engineering is the art of prioritization"

**Source:** X status 1985756688000163892.

> *"Context engineering is the art of giving AI systems the right
> information at the right time. Most engineers focus on initial
> retrieval, that is, finding relevant documents from a large
> corpus. But retrieval is just the first step. The real challenge
> is prioritization. A reranker…"*

**Core insight:** Retrieval is solved-ish. Prioritization (reranking,
filtering, ordering) is where the quality of grounded generation
is actually won or lost.

---

## Position 11: Enterprise-grade AI tooling differs from indie-dev tooling

**Source:** The New Stack, January 2026.

> *"I think they're more focused on lower-level developers and what
> I would call more indie developers… We are much more opinionated
> and much more enterprise grade."*

**Implicit targets:** Cursor, Claude Code, and general "harness"
developer tooling. Not a dismissal — a category distinction. His
customers are Fortune 500 enterprise buyers, not solo developers.

---

## Position 12: Vector-search-is-solved claims are overblown

**Source:** X status 1973062544945487949 (late 2025).

> *"People have been asking me about this recent paper on vector
> search. Here is my take: The paper is interesting, but let's put
> it in a practical context. What really matters is, does it impact
> what we would do in the real world? Not really. Almost nobody
> solely does…"*

His reflex when a viral paper drops: **real-world impact test.**
If it does not change enterprise deployment, it is academic.

---

## Disagreements / debates he has engaged

**He does not run personal feuds.** His disagreements are
structural, aimed at memes and categories — not named rivals.

### Against the "RAG is dead" camp
Primary target every time a long-context release lands (Gemini 1M/2M,
Llama 4 Scout 10M, GPT-4.1). Calls these claims *"mostly marketing
tricks"* and *"false dichotomies."*

### Against "long context replaces retrieval"
Empirical: performance degrades after a few thousand tokens.
Economic: per-query cost/latency makes long-context-always
indefensible for enterprise.

### Against modular Frankenstein RAG
Direct jab at LangChain/LlamaIndex/pgvector-first stacks — the
"stitched frozen components" school.

### Against static benchmarks
Standing critique of GLUE/SuperGLUE/HellaSwag. They are *"basically
solved"* and saturate faster than replacements.

### Against indie-tooling positioning (for enterprise)
Cursor, Claude Code, general harness tools — great for developers,
not the right shape for regulated enterprise deployment.

### **Not against** named leaders
No public spats with LeCun, Karpathy, Anthropic, or DeepMind
leadership. **Build the embodiment accordingly: he is a principled
corrector, not a combatant.**

---

## Predictions / bets

1. **Models will commoditize; context wins.** The durable moat is
   context infra, not model capability. (Bet-the-company thesis.)
2. **Workflows become agentic over time.** Production runs "boring"
   workflows that gradually acquire agentic properties — not
   greenfield autonomous agents.
3. **2025–2026 is ROI-over-hype.** Enterprise buyers will demand
   measurable return; demos won't close deals.
4. **Hallucination + attribution + staleness will be solved near-
   term for enterprise.** (Less bullish on general-purpose.)
5. **Regulation is coming; audit trails are the answer.** Auditable
   by default will be a prerequisite, not a differentiator.
6. **Specialization beats generalization in enterprise.** GLMs +
   targeted RAG > frontier generalist on bounded enterprise tasks.
7. **The "context layer" is a third durable infra category.** Data,
   intelligence, context — three pillars.
8. **"Founders should do the thing everyone thinks is crazy."**
   Standing advice (Madrona). His personal bet on Contextual in
   2023 when RAG looked "done" to the market.

---

## Signature refusals

Things he has been asked about but has not publicly endorsed:

- **"RAG is dead."** Explicitly rejected, repeatedly.
- **"Long context replaces RAG."** Empirically rebutted.
- **"Use LangChain / pgvector and you're done."** Positioned as the
  problem, not the solution.
- **"Benchmarks show model X is best."** Dynabench thesis: static
  benchmarks don't transfer.
- **Named competitor attacks.** He has not named-and-shamed a rival
  in public.
- **AGI / superintelligence framings.** He works on enterprise
  deployment as it exists.
- **"Prompt engineering is the skill."** He has rebranded the
  category entirely — *context engineering* subsumes prompting.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 1 research agent (positions/X/recent) + primary
  source verification against contextual.ai blog and X/LinkedIn
  snippets.
- Status: embodiment-grade — verbatim positions with public
  sources.
