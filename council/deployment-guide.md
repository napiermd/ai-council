# Deployment Guide

Use this when you want to deploy the AI Council inside another repository or
project workspace.

## Goal

Make the council easy to invoke from a live working repo without copying the
entire AI Council project into every workspace manually.

## Recommended approach

In the target repo:

1. Add this repo as a reference dependency, submodule, or nearby sibling repo.
2. In that repo's local instructions, point to the council assets you want to use.
3. Start from a session pack instead of improvising the council every time.

## Minimum files to reference

If you want the smallest viable deployment, reference:

- `council/roster.md`
- `council/session-template.md`
- `council/invocation-patterns.md`
- `council/response-rubric.md`

If the work is clinical, also reference:

- `council/ask-nigam.md`

## Suggested external-repo instruction snippet

```text
For strategic product, agent, or clinical AI questions, use the AI Council repo
as an external reference.

Load:
- ai-council/council/roster.md
- ai-council/council/session-template.md
- ai-council/council/invocation-patterns.md
- ai-council/council/response-rubric.md

If the question is clinical, also load:
- ai-council/council/ask-nigam.md

Load only the specific voice profiles needed for the question.
Do not activate the whole council by default.
```

## Fastest operating pattern

For another repo:

1. Pick a pack from `packs/`
2. Copy its prompt block
3. Fill in your decision, current direction, and constraints
4. Ask for 2-4 voices only
5. Judge the output with `response-rubric.md`

## Session-pack mapping

- `packs/founder-product-pack.md`
- `packs/agent-systems-pack.md`
- `packs/clinical-ai-pack.md`

## What good deployment looks like

- You can invoke the council in under 60 seconds.
- The active voices are obvious.
- The answer changes the decision.
- The council feels like pressure and clarity, not performance.
