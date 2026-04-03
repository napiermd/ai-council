# Example: Clinical AI Ask Nigam Response

## Situation

You are deciding whether an LLM-based documentation and synthesis workflow is a
real clinical product direction or a technically plausible idea that will fail
once it meets health-system data and care workflow constraints.

## Active voices

- Nigam Shah
- Jonathan H. Chen
- Chip Huyen

## Core tension

The tension is between apparent usefulness and operational survivability.

The idea sounds strong because documentation burden is real, but the decisive
question is not whether clinicians dislike documentation. It is whether the
system can fit the actual data, timing, trust, and workflow conditions of care
without creating new review burden.

## What each voice is saying

- Nigam Shah: Start with the real data-generating process. What inputs are
  actually available at the moment of use, how messy are they, and what metric
  the health system would care about if this worked. If the workflow adds hidden
  review work, it fails operationally even if the model output looks good.
- Jonathan H. Chen: The bedside moment matters. If the output arrives at the
  wrong time, requires too much interpretation, or is not trusted enough to act
  on, the product is not helping care.
- Chip Huyen: Reliability is not optional here. You need a narrow, auditable
  workflow with clear failure handling, not a broad assistive surface that is
  impossible to evaluate.

## Recommendation

Treat this as a real direction only if you narrow it to a specific workflow,
specific input surface, and specific operational metric.

Do not frame it as general clinical intelligence. Frame it as a tightly scoped
workflow tool that must prove trust, timing, and measurable operational value.

## Next move

Choose one clinical moment of use, map the exact available inputs, define the
output a clinician would act on, and identify the health-system metric that
would justify adoption before expanding the scope.
