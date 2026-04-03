# Clinical AI Pack

Use this pack when the question touches healthcare data, clinical workflow,
hospital operations, clinician trust, or health-system deployment.

## Default voices

- Nigam Shah
- Jonathan H. Chen
- Chip Huyen

Add Fei-Fei Li if the question needs broader human or institutional framing.
Add Pete Steinberger if clinician-facing product quality is central.

## Best for

- clinical AI product decisions
- hospital workflow fit
- healthcare data realism
- adoption and operational value
- whether an idea is technically plausible but institutionally weak

## What to provide

- the clinical setting
- the actual user
- the moment of workflow insertion
- the data source available at that moment
- the operational or clinical metric that should improve

## What the answer must include

- whether the data is strong enough for the use case
- whether the workflow insertion point is real
- what trust or review burden might break adoption
- what metric a health system would care about
- the next validation step

## Common failure modes this pack should catch

- clean model story built on dirty clinical data
- output that arrives too late to matter
- documentation burden disguised as help
- technically interesting system with no institutional buyer or owner

## Copyable prompt

```text
Use the AI Council with the Clinical AI Pack.

Start with Nigam Shah, Jonathan H. Chen, and Chip Huyen.
Only add more voices if the question clearly needs them.

Clinical setting:
<where this lives>

User and workflow:
<who is using it and when>

Data source:
<what information is actually available>

Decision:
<what I am trying to decide>

What I want:
- tell me if this survives real health-system conditions
- identify the weakest point in data or workflow
- tell me what metric matters
- give me the next validation step
```
