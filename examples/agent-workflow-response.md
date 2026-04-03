# Example: Agent Workflow Response

## Situation

You are deciding whether a multi-agent workflow actually improves output enough
to justify coordination overhead, debugging cost, and evaluation complexity.

## Active voices

- Chip Huyen
- Andrej Karpathy
- Pete Steinberger

## Core tension

The tension is between modular intelligence and operational complexity.

A multi-agent workflow can create useful decomposition, but it can also create a
system that is harder to evaluate, harder to debug, and worse to use than a
strong single-agent baseline.

## What each voice is saying

- Huyen: Do not add agents faster than you can evaluate them. Every extra
  handoff adds failure surface. If you cannot measure whether specialization
  helps, the system is just more complex.
- Karpathy: Some decomposition is helpful, but most agent trees are cargo cults.
  Use specialization only where the task boundaries are real and the model
  behavior actually improves from separation.
- Steinberger: If the workflow becomes hard to understand, users will not trust
  it. Internal sophistication does not matter if the product becomes opaque or
  annoying.

## Recommendation

Do not start with a large swarm.

Build a small workflow with explicit roles only where the task boundary is
genuine and observable. Treat the single-agent version as the baseline you have
to beat.

## Next move

Implement one narrow multi-step workflow with traceable handoffs, define the
baseline single-agent version beside it, and compare quality, latency, and
debuggability before adding any more specialization.
