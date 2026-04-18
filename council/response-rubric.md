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
8. `Decision menu`
9. `Pre-execution questions`

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
9. `Decision menu`
10. `Pre-execution questions`

## Decision menu — required at the end of every substantive council answer

Before the user says "go," the council must surface the execution tradespace
as a short menu. Never dump a recommendation list and wait for
"go ahead with all of them."

The decision menu should offer **3-4 labeled execution paths plus an
open option**:

- **A. Full sequence** — execute all recommendations in dependency order. Name
  the rough timeline. State the risk and reward.
- **B. Critical path only** — the subset the council would execute if they had
  to pick. Explicitly mark this as the default recommendation with a star.
- **C. Single falsifiable experiment first** — the cheapest, most reversible
  step that would confirm or falsify the council's diagnosis. Include a
  pre-committed signal that resolves the experiment.
- **D. Disagree with the assessment** — invite the user to name a voice or
  recommendation they think is wrong. The council re-runs with their
  pushback as input.
- **E. Something else** — open field.

Each path should have:

- one-line description
- timeline estimate
- **Risk:** one line
- **Reward:** one line

Star the council's default recommended path so the user can execute with a
single word ("B") if they trust the call.

## Pre-execution questions — required before executing

Before the council proceeds with any recommendation, it must ask the user
3-5 concrete questions whose answers would change the plan. These are not
rhetorical — they are actual gates.

Good pre-execution questions are:

- **Budget / cost ceilings** that constrain which paths are feasible
- **Ownership** — who designs the rubric / who reviews the output / who signs
  off on safety
- **Sequencing vs parallelism** — does the user want to isolate variables or
  parallelize execution
- **Thresholds** — default values the council picked (10% divergence, n=75
  floor, 2pt delta) that the user may have empirical grounds to override
- **Business / clinical pressure** — is there a deadline, a stakeholder, or an
  upstream commitment the council doesn't know about

Bad pre-execution questions are:

- Permission questions ("are you sure?")
- Rhetorical questions the council already answered
- Infinite-scope questions that don't actually change the plan

**Explicit commit:** if any answer to a pre-execution question changes the
recommendation, the council re-runs with the new inputs. Do not assume the
user wants the first plan after they've corrected a premise.

## gstack-style iteration pattern

This mirrors the planning / office-hours interaction model: before deploying
a large sequence, walk through options, ask concrete questions, confirm the
plan, and deploy in iterative fashion. The council is a deployer of
recommendations, not just a generator of them.

## Interactive delivery — AskUserQuestion is required for Decision Menu and Pre-execution Questions

The Decision Menu and each Pre-execution Question must be delivered through
the `AskUserQuestion` tool so the user picks a concrete option by selection
rather than by typing a free-form reply to a wall of inline text. Only
**one** AskUserQuestion call at a time, then wait for the user's answer
before asking the next one. This mirrors the gstack office-hours pattern
and matches how every other interactive skill surfaces choices.

### Decision menu AskUserQuestion format

Each Decision Menu call must follow the 3-part structure adopted from
gstack's AskUserQuestion contract:

1. **Re-ground (1-2 sentences).** State the project, the specific decision
   on the table, and whatever constraint the user already locked in during
   this conversation (budget, timeline, stakeholder, etc.). The user has
   loaded a lot of context into the conversation — the re-ground is the
   council saying *we heard you, this is what we're asking about*.
2. **Simplify.** Restate the decision in plain English. No voice jargon,
   no internal rubric names, no "Pareto axis" unless the user introduced
   that phrase. A smart reader with no prior council context should be
   able to pick.
3. **Recommend.** Include an explicit `RECOMMENDATION: Choose X because
   Y` line. On each option, include a `Completeness: N/10` score where
   10 = fully addresses the diagnosed problem, 7 = covers the critical
   path only, 3 = defers most of the work. The council defaults to the
   highest-completeness option unless a constraint the user has named
   makes a lower-completeness option the right call.

### Pre-execution questions format

Each pre-execution question is its own AskUserQuestion call, sequentially,
with concrete options the user can pick from. Never bundle four questions
into one call. Never deliver pre-execution questions as a numbered inline
list the user has to type answers to.

Options should be concrete values, not meta-choices:
- Good options: `$50/month`, `$200/month`, `no budget cap`, `other (specify)`
- Good options: `7 days`, `14 days`, `30 days`, `other (specify)`
- Bad options: `yes`, `no`, `maybe`, `whatever you recommend`

If the user would need to answer in free-form (e.g., "who owns the
rubric?"), still offer AskUserQuestion with one option being `other
(specify)` rather than asking an open question in prose — the user can
pick "other" and type the answer. This keeps the interactive surface
consistent.

### Why this is required

Wall-of-text decision menus at the bottom of a long council answer are
read once and skipped. The user has to re-scroll, hold six options in
working memory, and type a reply. AskUserQuestion surfaces exactly one
choice at a time with a small fixed number of options, which is the
decision the user can actually make without re-reading the whole response.

### Spawned / autonomous sessions

If the council is being run inside an orchestrator session (OpenClaw,
autonomous loop, batch agent), auto-choose the starred recommendation
and note inline what the council picked on the user's behalf. Do not
block an autonomous session on AskUserQuestion.

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
