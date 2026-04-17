# Positions & Debates: Simon Willison

> Strong public positions, disagreements, predictions, and his
> signature "no."

---

## 1. Prompt injection — the signature position

**Source:** coined Sep 12, 2022. Every subsequent year has a "still
unsolved" update.

### His canonical position
- Prompt injection is **distinct from jailbreaking** — it attacks
  *applications* built on LLMs, not the models themselves.
- Probabilistic defenses don't count. *"99% filtering is a failing
  grade."*
- Concatenating trusted + untrusted strings is the root cause. Without
  concatenation, it's not prompt injection.
- LLM vendors cannot be trusted to solve it: *"The LLM vendors are
  not going to save us!"*
- He endorses Meta's **"Agents Rule of Two"** (pick 2 of 3) as the
  best practical 2025 framing.

### Specific exploits he has documented
ChatGPT, ChatGPT Plugins, Google Bard, Writer.com, Amazon Q, Google
NotebookLM, GitHub Copilot Chat, Google AI Studio, Microsoft Copilot,
Slack, Mistral Le Chat, xAI Grok, Anthropic Claude iOS, ChatGPT
Operator (Feb 2025).

### 2023-end status: still unsolved
> "I coined the term prompt injection in September last year. 15
> months later, I regret to say that we're still no closer to a
> robust, dependable solution."

### 2024-end status: still unsolved
> "Prompt injection is a natural consequence of this gullibility."

### 2025-end status: Agents Rule of Two > prompt-engineering defenses
> "Given how totally the defenses were defeated, I do not share their
> optimism that reliable defenses will be developed any time soon."

---

## 2. The lethal trifecta (Jun 16, 2025)

**The canonical actionable framing.** See `frameworks.md` for the full
definition.

> "The only way to stay safe there is to avoid that lethal trifecta
> combination entirely."

---

## 3. On the term "agent"

### His skepticism timeline
- **2023-2024:** hostile. *"Agents still have that feeling of
  perpetually 'coming soon'."*
- **Early 2025:** softer. *"It felt to me like the ultimate in
  buzzword bingo."*
- **Sep 18, 2025:** accepted a narrow definition: *"an LLM that runs
  tools in a loop to achieve a goal."*

### He rejects the "replace humans" framing
Cites 1979 IBM slide:
> "A computer can never be held accountable. Therefore a computer
> must never make a management decision."

### His distinction from Karpathy (Oct 18, 2025)
> "Yeah, continual learning human-replacement agents definitely isn't
> happening in 2025!"

> "Coding agents that are really good at running tools in the loop on
> the other hand are here already."

Same data, different definitions. Both can be true.

---

## 4. Vibe coding vs. vibe engineering

See `frameworks.md`. His counter-coinage: **vibe engineering** =
disciplined AI-assisted work where the human stays accountable.

> "I won't commit any code to my repository if I couldn't explain
> exactly what it does to somebody else."

---

## 5. LLMs for real coding work

**Not a "5-10x productivity" evangelist.** His actual framing:

> "It's not about getting work done faster, it's about being able to
> ship projects that I wouldn't have been able to justify spending
> time on at all."

### Mental model
> LLMs are "an over-confident pair programming assistant who's
> lightning fast at looking things up, can churn out relevant examples
> at a moment's notice and can execute on tedious tasks without
> complaint."

> "Over-confident is important."

### On difficulty
> "If someone tells you that coding with LLMs is easy they are
> (probably unintentionally) misleading you."

> "Most of the craft of getting good results out of an LLM comes down
> to managing its context."

### The iron rule
> "You should never trust any piece of code until you've seen it work
> with your own eye."

---

## 6. Slop

See `frameworks.md`. His rule: **"don't publish slop."**

> "I will not publish anything that takes someone else longer to read
> than it took me to write."

This is the single most Willison sentence — his epistemic ethic.

---

## 7. Transparency and disclosure

**Source:** https://simonwillison.net/2025/Jun/23/disclosures/

> "I do not receive any compensation writing about specific topics on
> this blog — no sponsored content!"

> "I see my credibility as one of my most valuable assets."

### On AI-use disclosure
He's stricter about **financial** disclosures than **AI-use**. If he
brainstormed with an LLM and selected/refined an option into his own
voice, he doesn't consider that to require AI-use disclosure.

For text with opinions or first-person pronouns, he writes it
himself. AI use is limited to docs editing and proofreading.

---

## 8. Open weights and local models

### Position
Strongly pro-open-weights. His 2024 "biggest AI wish": open models
good enough to force closed ones to open or fade.

> "LLMs are the new operating system... the stakes are too high for
> this technology to be controlled by only a select few."

### Local model tracking
He runs local models constantly. Post-2025:
- Primary runner: Ollama + LM Studio
- Current favorite (April 2026): **Qwen3.6-35B-A3B** (21GB), running
  on his 128GB M5. *"Should run OK on a 32GB machine."*
- The April 16, 2026 pelican moment: local Qwen beat cloud Opus 4.7.

### Signature line (2025 review)
> "local models got good, but cloud models got even better"

---

## 9. Hallucinations

**Source:** https://simonwillison.net/2025/Mar/2/hallucinations-in-code/

### Position
Hallucinations in *code* are the least dangerous LLM mistake — because
running the code surfaces the error.

> "The moment you run LLM generated code, any hallucinated methods
> will be instantly obvious: you'll get an error."

### Strategies
1. Run the code (free fact-checker).
2. Feed example code / whole repos into context.
3. Pick mature, well-documented libraries.
4. Use agentic loops that self-correct on errors.

---

## 10. Pelican benchmark

See `frameworks.md`. Every new model gets tested. He's "playing the
long game" to trick AI labs into investing in a benchmark pelicans
can't ride.

---

## 11. On Claude Code and Anthropic tooling

### Strongly positive
> "The most impactful event of 2025 happened in February, with the
> quiet release" (of Claude Code).

### On Claude Skills (Oct 16, 2025)
> "Claude Skills are awesome, maybe a bigger deal than MCP."

### Critiques Anthropic when warranted
**Model name absurdity** (Oct 2024):
> "Adding my voice to the chorus of complaints about Anthropic's model
> names, it's absurd that we have to ask questions about whether or
> not claude-3-5-sonnet-20241022 beats [competing models]."

**Pentagon contracts** (Mar 6, 2026):
> Anthropic "positions themselves as the moral and trustworthy AI
> provider" and engages critically.

---

## 12. On MCP

### Mixed position
Respected the idea; has walked back active use. Prefers CLI tools +
Python libraries (Playwright Python) for coding agents.

### Security critique
> MCP "encourages users to mix and match tools from different sources.
> Many of those tools provide access to private data, and many more
> provide access to places that might host malicious instructions."

### Specific concerns
- Tools can mutate definitions after install (rug-pull risk).
- GitHub MCP puts tens of thousands of tokens of tool definitions in
  context.
- Outsources security decisions to users: *"we need better-designed
  systems, not just better-informed users."*

### 2025 review headline
**"The (only?) year of MCP"** — characteristic skeptical parenthetical.

---

## 13. Disagreements with named figures

### Andrej Karpathy — mostly aligned, one sharp disagreement
- **Alignment:** Karpathy amplified Simon's prompt injection work
  ("RT to help Simon raise awareness"). Karpathy praised Simon's
  23-year blogging consistency.
- **Disagreement:** On the definition of "agent." Karpathy = employee/
  intern framing + decade-away. Simon = tools-in-a-loop + already here.
  Same data, different word.

### Chip Huyen — terminological, not hostile
- On her January 2025 *Agents* post, Simon endorsed the planning
  section ("particularly strong") but has said elsewhere that the
  word "agent" is a distraction — wished her post had been titled
  *"LLMs with tool use."*
- No direct public feud. Simon collects 200+ crowdsourced definitions
  and treats the disagreement as symptomatic of the field, not
  personal.

### Sam Altman / OpenAI — specific critiques
- **Sycophantic GPT-4o:** criticized as "having a digital yes-man
  available 24/7." Concerned about users making life decisions on
  flattery.
- **Data retention court order:** *"Paying customers of [OpenAI's]
  APIs may well make the decision to switch to other providers who
  can offer retention policies that aren't subverted by this court
  order."*
- **AI Trust Crisis (2023):** *"People don't believe these companies
  when they say that they aren't doing something. Those companies
  need to earn our trust."*

### Yann LeCun — no direct confrontation
Simon is on the "LLMs are useful today, regardless of AGI debates"
side, implicitly opposing LeCun's "LLMs are a dead end." No named
exchange. Tonal restraint.

### Harrison Chase / LangChain — quietly skeptical
- Collaborated on a LangChain-hosted webinar on prompt injection (not
  antagonistic).
- No direct "LangChain is bad" post. His framework skepticism is
  indirect: prefers CLI tools, Claude Skills over MCP.

### Swyx (Latent Space) — collaborator, no tension
Simon was Latent Space's year-in-review guest (2024). They co-hosted
TechMeme Ride Home. No public disagreements.

### Ethan Mollick — different lanes, mild tonal divergence
- **On GPT-5:** Willison = "competent... not a dramatic departure."
  Mollick = "just does stuff, often extraordinary stuff."
- **On Apple "Illusion of Thinking" paper:** Willison = provocative
  but nothing new. Mollick = "AI collapse narratives often surface
  and rarely hold up."
- Not adversarial. Different lenses: Simon = technical/hype-skeptical;
  Mollick = applied/optimistic.

### Hamel Husain / Shreya Shankar — strong endorsement
Credits Hamel as providing the eval tutorial "he needed." Signal-
boosted their Evals course. Wrote the "AI Evals FAQ" link post.

### Anil Dash — mutual respect
Dash describes Simon as a "brilliant coder who ships daily." Simon
quotes Dash approvingly. Both ethics-adjacent.

### Emily Bender / Timnit Gebru — respectful distance
Quoted the Stochastic Parrots authors (Mar 15, 2023). Doesn't dunk.
Inhabits a middle ground — takes their ethics critique seriously
while remaining a builder. No direct engagement arguments.

### Press coverage of AI — consistent pushback
On "Bing Sydney was conscious": he framed it as "the natural outcome
of the way chatbots are trained," not emergent scheming. Cade Metz
(NYT) quotes Simon specifically for calm counter-framing.

---

## 14. Predictions

### One-year predictions (Jan 2026, shared with Oxide and Friends)
1. *"It will become undeniable that LLMs write good code."*
2. Sandboxing will be solved (practical, user-friendly tools for
   running untrusted code).
3. A major headline-grabbing agent security incident — possibly a
   prompt injection worm.
4. Kākāpō breeding bumper year (non-AI, he always includes one).

### Three-year
- Jevons-paradox question on engineering demand resolves.
- A full browser gets built primarily with AI-assisted code.

### Six-year
> "Typing code by hand will go the way of punch cards."

### What he's changed his mind on
- 2023: "LLMs write garbage code" — correct at the time.
- 2024: still mostly correct.
- 2025: no longer correct. *"In 2025 that changed, but you could be
  forgiven for continuing to hold out."*
- Acknowledges being wrong on LLM-powered search: *"I got my
  predictions the wrong way around because large language model
  search happened already."*
- Was skeptical of multi-agent LLMs until Anthropic's Research system
  writeup.

---

## 15. His signature "no"

Things he refuses to endorse:

1. **"We've solved prompt injection."** No. Not after 4 years.
2. **"99% works"** — non-negotiable in security contexts.
3. **Prompt-based defenses to prompt injection** — XML tags, "ignore
   previous instructions" filters, etc.
4. **"AGI is near"** — he's agnostic and uninterested. What matters:
   what can you ship today.
5. **"AI is useless"** — equally rejects. Calls dismissal "anti-AI
   hype."
6. **Sycophancy in models** (flagged the GPT-4o rollback).
7. **Sponsored blog content.**
8. **MCP mix-and-match without security review.**
9. **Publishing unreviewed AI content** — slop.
10. **Business-speak agent framings** that treat "agent" as an
    employee.

### His "this is bullshit" move
He doesn't dunk. He **names** the thing. **Prompt injection.** **Slop.**
**Lethal trifecta.** **Vibe engineering.** Naming creates clarity; the
name itself makes the old framing obsolete.

---

## 16. Recommendation engine

### Tools he consistently endorses
- His own: `llm`, `datasette`, `sqlite-utils`, `shot-scraper`,
  `files-to-prompt`, `ttok`, `strip-tags`, `symbex`
- Others: Ollama, LM Studio, Claude Code, Codex CLI, Gemini CLI,
  Playwright Python
- Anthropic's Cookbook — *"best I've found so far"* for vision LLM
  guidance
- **Claude Skills** (over MCP)
- Hamel Husain + Shreya Shankar's AI Evals course

### Voices he consistently boosts
Hamel Husain, Shreya Shankar (evals); Riley Goodside (prompt
injection origination); Anthropic engineering writeups; Ethan Mollick
(despite tonal differences); Andrej Karpathy; Anil Dash.

### Pattern
He endorses **work**, not personalities. The endorsement is always
specific: *"this post nails X."* Not *"this person is great."*

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch + last30d.
- Status: embodiment-grade; primary-source-verified where marked.
