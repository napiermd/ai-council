# Invocation Patterns

Use these patterns to activate the council intentionally instead of vaguely.

## General review

```text
Use the AI Council to review this direction.
I want the sharpest 2-4 voices only, not everyone.
Show me the main disagreement, then tell me what to do next.
```

## Draft or memo review

```text
Use the AI Council to review this draft in rating mode.
Activate only the 3-5 voices that matter.
For each voice, give:
- an overall rating out of 10
- a short why
- one thing to keep
- one thing to fix

Then give me:
- a council meeting section where they argue with each other
- the council range
- whether this is ready to submit
- the single best next revision move
```

## Product decision

```text
Use the AI Council to pressure-test this product direction.
Bias toward product quality, engineering realism, and what will actually ship well.
Tell me if this is real, premature, or overbuilt.
```

Recommended voices:

- Steinberger
- Huyen
- Howard

## Architecture or model decision

```text
Use the AI Council to review this model or architecture choice.
I want the strongest argument for and against the current direction.
Separate research risk from product risk.
```

Recommended voices:

- Karpathy
- LeCun
- Olah

## Agent or systems workflow

```text
Use the AI Council to review this agent or workflow design.
Focus on evals, observability, failure modes, and whether this will hold up in production.
```

Recommended voices:

- Huyen
- Karpathy
- Steinberger

## Frontier roadmap

```text
Use the AI Council to review this long-horizon AI roadmap.
Do not optimize for immediate shipping alone.
Tell me whether this builds durable capability or just local wins.
```

Recommended voices:

- Hassabis
- LeCun
- Karpathy

## Clinical AI

```text
Use the AI Council to review this clinical AI direction.
Ask Nigam first.
Then add only the voices needed for workflow, systems, and human-centered design.
I want to know whether this survives real data, workflow, and deployment conditions.
```

Recommended voices:

- Nigam Shah
- Jonathan H. Chen
- Huyen
- Fei-Fei Li

## Ask Nigam

```text
Ask Nigam what he thinks about this clinical AI idea.
I want the health-system realism check first:
- data quality
- workflow fit
- operational value
- deployment friction

Then tell me which other voices to bring in.
```
