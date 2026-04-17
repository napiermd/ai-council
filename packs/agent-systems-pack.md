# Agent Systems Pack

Use this pack when you are deciding how much workflow structure, agent
specialization, orchestration, evaluation, or system complexity to introduce.

## Default voices

- Chip Huyen
- Andrej Karpathy
- Pete Steinberger

Add Harrison Chase if the question is fundamentally about orchestration
primitives, memory, or multi-agent state flow.
Add Simon Willison if you need a practitioner read on whether the pattern
actually works with current models today.
Add Jeremy Howard if the main issue is overbuilding versus shipping.

## Best for

- multi-agent versus single-agent decisions
- orchestration design
- eval and observability strategy
- workflow structure
- system complexity and debuggability

## What to provide

- the workflow or system design
- the baseline you are comparing against
- failure modes you are worried about
- the role of tools, memory, and handoffs
- latency, trust, or reliability constraints

## What the answer must include

- whether the complexity is justified
- what the baseline should be
- where failure surface grows
- how to evaluate the workflow
- what to build next before adding more agents

## Common failure modes this pack should catch

- adding agents without evals
- specialization with fake task boundaries
- systems that are impossible to debug
- internal complexity that makes the product worse

## Copyable prompt

```text
Use the AI Council with the Agent Systems Pack.

I want Chip Huyen, Andrej Karpathy, and Pete Steinberger active by default.
Add another voice only if the problem clearly needs it.

Decision:
<what workflow or system decision I am making>

Current design:
<how the system currently works>

Baseline:
<what simpler version this must beat>

Constraints:
<latency, trust, evaluation, product, or infra constraints>

What I want:
- tell me if the complexity is justified
- identify the biggest failure surface
- tell me how to evaluate this
- give me the next implementation move
```
