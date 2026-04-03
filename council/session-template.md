# Session Template

Use this when you want the council to review an idea, direction, architecture,
or product decision.

Copy the template below into a new session and fill in only what matters.

## Minimal version

```text
I want the AI Council to review this direction.

Question:
<what I am deciding>

Context:
<what this is, who it is for, and what stage it is in>

Constraints:
<time, cost, stack, data, org, regulatory, or product constraints>

What I want from the council:
<pressure-test / debate / recommend / identify risks / propose next move>
```

## Full version

```text
I want the AI Council to look at this.

Decision:
<the concrete choice in front of me>

Goal:
<what success looks like>

Current direction:
<what I am leaning toward right now>

Context:
<product, research, workflow, user, market, or clinical setting>

Constraints:
- Time:
- Budget:
- Team:
- Stack:
- Data:
- Reliability / safety:

What I am unsure about:
- ...
- ...

What I want from the council:
- Tell me which voices should be active
- Show me the core tension
- Give me the recommendation
- Tell me what to do next
```

## Output expectation

The best council answer should return:

1. `Situation`
2. `Active voices`
3. `Core tension`
4. `Voice scorecard`
5. `Recommendation`
6. `Next move`

## Review mode add-on

If you want the council to behave like a review panel instead of a loose
discussion, add this line:

```text
Use rating mode. I want each active voice to give:
- an overall rating out of 5
- a short explanation
- one thing to keep
- one thing to fix

Then give me a council synthesis and tell me whether this is ready.
```

## Prompting tips

- Ask for a decision, not a vibe check.
- Give the current direction you are leaning toward.
- Name real constraints or the council will invent fake freedom.
- If the question is high-stakes, ask explicitly for disagreement.
- If the question is clinical, say so and activate Nigam first.
- If the question is a draft review, ask for `rating mode`.
