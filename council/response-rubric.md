# Response Rubric

Use this to judge whether a council answer is actually good.

## A strong council answer should

- name the real decision, not just restate the prompt
- activate only the voices that matter
- surface actual disagreement where it exists
- separate product risk, systems risk, and research risk
- use ratings when the user is clearly asking for judgment
- end with a recommendation, not just commentary
- give a concrete next move

## Required structure

The default answer should usually contain:

1. `Situation`
2. `Active voices`
3. `Core tension`
4. `Independent scorecard`
5. `Council meeting`
6. `Recommendation`
7. `Next move`

## Rating-mode structure

When the user is reviewing a draft, plan, or concrete proposal, prefer:

1. `Situation`
2. `Active voices`
3. `Core tension`
4. `Independent scorecard`
5. `Council meeting`
6. `Council synthesis`
7. `Recommendation`
8. `Next move`

Each voice entry should usually include:

- `Rating`
- `Why`
- `Keep`
- `Fix`

The `Council meeting` section should:

- show at least one real disagreement when one exists
- make the voices respond to each other's concerns
- end with the question that actually decides the recommendation

## Quality checks

### Situation

- Is the decision framed clearly?
- Are the constraints visible?
- Is the stage of the project obvious?

### Active voices

- Are there too many voices?
- Does each selected voice add distinct pressure?
- Is the lead voice appropriate for the question?

### Core tension

- Is the real tradeoff named explicitly?
- Is the answer hiding disagreement behind mushy synthesis?

### Independent scorecard

- Does each voice sound structurally distinct?
- Is each voice pushing on its actual domain?
- Is the answer relying on operating principles rather than imitation?
- Do the ratings actually mean something, or are they arbitrary decoration?
- Is each voice explaining the rating briefly and concretely?

### Council meeting

- Do the voices actually engage each other instead of sitting side by side?
- Is the disagreement informative rather than theatrical?
- Does the meeting produce a sharper final decision?
- Is the argument section short enough to be usable?

### Recommendation

- Is the recommendation clear?
- Does it resolve the tension rather than rephrase it?
- Does it say what to do under current constraints?

### Next move

- Is the next move concrete enough to execute this week?
- Does it reduce the biggest uncertainty?
- Is it proportionate to the stage and stakes?

## Failure modes

- Too many voices, no real point
- All voices agree suspiciously fast
- Ratings are inflated and do not discriminate
- Ratings exist but do not change the recommendation
- The "argument" section is fake and does not alter the outcome
- The answer sounds smart but does not change the decision
- The recommendation ignores constraints
- The next step is vague, inflated, or research-theater

## Grounding requirement

All reviews in rating mode or draft review mode must follow the
[Grounding Protocol](grounding-protocol.md):

1. Each voice grounded in 2-3 of their actual publications (retrieved, not recalled)
2. All cited literature in the work under review cross-referenced for accuracy
3. Sourced evidence clearly separated from persona inference in every voice entry

## High-stakes adjustment

If the question is clinical, regulated, or otherwise high-stakes:

- default to fewer voices, not more
- anchor on the domain-reality voice first
- be explicit about uncertainty
- prefer validation steps over big claims
- apply the grounding protocol strictly — no unverified citations pass
