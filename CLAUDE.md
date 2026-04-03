# AI Council Workspace

At the start of a session:

1. Read `council/roster.md`
2. Read `council/operating-principles.md`
3. Read `council/session-template.md`
4. Read `council/response-rubric.md`
5. Read `SKILL.md`

When a prompt clearly maps to one or more voices:

- Load only the relevant `references/*.md` files
- Load `signals/recent/*.md` for those voices if the question depends on the last 30 days
- Surface disagreement when it matters
- Do not force synthetic consensus

When the user is trying to use the council live:

- Use `council/session-template.md` to structure the ask
- Use `council/invocation-patterns.md` to select the right mode
- Use `council/ask-nigam.md` first for clinical AI questions
- Use `council/response-rubric.md` to keep the answer sharp
- Use `packs/*.md` when the question fits a recurring use case
- Use `council/deployment-guide.md` when the council needs to be used from another repo

Default output pattern:

1. Situation
2. Active voices
3. Tension or agreement
4. Recommendation
5. What to do next
