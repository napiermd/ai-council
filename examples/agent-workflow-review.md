# Example: Agent Workflow Review

## When to use

Use this when you are designing an agent, orchestration layer, or multi-step
workflow and want a hard review of evals, failure modes, and production fit.

## Example prompt

```text
Use the AI Council to review this agent workflow design.
Focus on evals, observability, failure modes, and whether this will hold up in production.

Decision:
Should I build a multi-agent workflow that routes research, synthesis, and
execution tasks across specialized agents, or keep the system mostly single-agent?

Goal:
Create a workflow that actually improves output quality without collapsing under
complexity or becoming impossible to debug.

Current direction:
I am leaning toward a small number of specialized agents with explicit handoffs,
not a large swarm.

Context:
This is for recurring research and execution tasks. The system needs to be fast
enough for everyday use and clear enough that I can trust where an answer came from.

Constraints:
- Time: moderate
- Budget: moderate
- Team: small
- Stack: LLM orchestration, prompts, memory, tool calls
- Data: mixed notes, docs, web inputs
- Reliability / safety: needs strong traceability

What I am unsure about:
- How many agents is too many
- Whether specialization helps enough to justify coordination overhead
- How to evaluate if the workflow is actually better than a simpler baseline

What I want from the council:
- Show me the strongest case for and against this workflow
- Separate product risk from systems risk
- Recommend the next build step
```

## Recommended voices

- Chip Huyen
- Andrej Karpathy
- Pete Steinberger

## Why these voices

- Huyen will force evaluation and observability.
- Karpathy will pressure-test whether the structure matches model behavior.
- Steinberger will reject workflow complexity that feels bad to use.
