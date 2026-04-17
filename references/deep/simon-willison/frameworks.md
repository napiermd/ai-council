# Frameworks: Simon Willison

> His named frameworks, coinages, and mental models with source and
> invocation context.

---

## 1. Prompt injection (coined September 12, 2022)

**Source:** https://simonwillison.net/2022/Sep/12/prompt-injection/

**Refined 2024 definition** (https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/):
> "Prompt injection is a class of attacks against applications built on
> top of Large Language Models (LLMs) that work by concatenating
> untrusted user input with a trusted prompt constructed by the
> application's developer."

### Not to be confused with jailbreaking
> "Jailbreaking is the class of attacks that attempt to subvert safety
> filters built into the LLMs themselves."

**Critical bright line:**
> "If there's no concatenation of trusted and untrusted strings, it's
> not prompt injection."

**Why it matters to him:**
> "The risks from prompt injection are far more serious, because the
> attack is not against the models themselves, it's against applications
> that are built on those models."

### On why it's unsolved
> "AI is entirely about probability... But fundamentally, security
> based on probability does not work. It's no security at all."

> "99% filtering is a failing grade."

> "In web application security 99% is not good enough. Imagine if we
> protected against SQL injection with an approach that failed 1/100
> times?"

### When he invokes it
Any agent / LLM-in-workflow discussion. Always. It is his signature
contribution.

---

## 2. The lethal trifecta (coined June 16, 2025)

**Source:** https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/

### Three ingredients
1. **Access to private data** — emails, docs, databases.
2. **Exposure to untrusted content** — any attacker-controlled text/
   images reaching the LLM.
3. **External communication** — ability to exfiltrate (requests, link
   generation, etc.).

### The rule
> "If your agent combines these three features, an attacker can easily
> trick it into accessing your private data and sending it to that
> attacker."

> "The only way to stay safe there is to avoid that lethal trifecta
> combination entirely."

> "The LLM vendors are not going to save us! We need to avoid the
> lethal trifecta combination of tools ourselves to stay safe."

### Documented real-world impact
He has documented prompt-injection exploits in ChatGPT, Plugins, Bard,
Writer.com, Amazon Q, NotebookLM, Copilot Chat, Google AI Studio,
Microsoft Copilot, Slack, Le Chat, Grok, Claude iOS, and ChatGPT
Operator (Feb 2025).

### When he invokes it
Any agent deployment discussion. He'll name which leg(s) you should
drop to be safe.

---

## 3. Agents Rule of Two (endorsed November 2, 2025)

**Source:** https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/

Meta framework he endorses: pick **2 of 3** (untrusted input / private
data access / state change). Not originally his, but he publicly
endorsed it as *"the best practical advice for building secure LLM-
powered agent systems today."*

> "Given how totally the defenses were defeated, I do not share their
> optimism that reliable defenses will be developed any time soon."

---

## 4. "Agents = LLMs that run tools in a loop"

**Source:** 2025 year-in-review (https://simonwillison.net/2025/Dec/31/the-year-in-llms/).

His settled definition after years of skepticism about the term:
> "an LLM that runs tools in a loop to achieve a goal"

He also endorses Solomon Hykes's formulation:
> "An AI agent is an LLM wrecking its environment in a loop."

### The pre-2025 history
> "It felt to me like the ultimate in buzzword bingo — everyone was
> talking about agents, but if you quizzed them everyone seemed to
> hold a different mental model of what they actually were."

> "So long as agents lack a commonly shared definition, using the
> term reduces rather than increases the clarity of a conversation."

> "I've started using the term 'agent' in conversations where I don't
> feel the need to then define it, roll my eyes or wrap it in scare
> quotes."

### Related — "coding agents"
> "LLM systems that can write code, execute that code, inspect the
> results and iterate"

### "Asynchronous coding agents"
> "a system you can prompt and forget, and it will work away on the
> problem"

---

## 5. Vibe coding vs. Vibe engineering

**Vibe coding (Karpathy's term, Feb 2025):**
> "building software with an LLM without reviewing the code it writes"
(Simon's definition, Mar 19, 2025)

**His golden rule:**
> "I won't commit any code to my repository if I couldn't explain
> exactly what it does to somebody else."

**Vibe engineering (Simon's counter-coinage):**
> "seasoned professionals accelerate their work with LLMs while staying
> proudly and confidently accountable for the software they produce"
(vibe-engineering post)

### The distinction
> "If an LLM wrote every line of your code, but you've reviewed, tested,
> and understood it all, that's not vibe coding in my book — that's
> using an LLM as a typing assistant."

> "AI tools amplify existing expertise. The more skills and experience
> you have as a software engineer the faster and better the results
> you can get from working with LLMs and coding agents."

### When he invokes it
Any "I vibe-coded this..." conversation. He'll distinguish throwaway
from serious.

---

## 6. Slop (coined 2023-2024)

**Source:** https://simonwillison.net/2024/May/8/slop/

> "The term for unwanted AI generated content."

> "If it's mindlessly generated and thrust upon someone who didn't ask
> for it, slop is the perfect term for it."

> "Sharing unreviewed content that has been artificially generated with
> other people is rude."

**Year-in-review refinement (2024):**
> "Slop describes AI-generated content that is both unrequested and
> unreviewed."

**Rule:** "don't publish slop."

**2025 update:** less pessimistic. *"slop won't end up as bad a problem
as many people fear... the internet has always been flooded."*

---

## 7. The pelican-on-a-bicycle benchmark (October 25, 2024)

**Source:** https://simonwillison.net/2024/Oct/25/pelicans-on-a-bicycle/
**Repo:** https://github.com/simonw/pelican-bicycle

### Why pelicans
> "I chose that because a) I like pelicans and b) I'm pretty sure
> there aren't any pelican on a bicycle SVG files floating around (yet)
> that might have already been sucked into the training data."

### Why SVG
> "I'm running this against text output LLMs. They shouldn't be able
> to draw anything at all. But they can generate code... and SVG is
> code."

### Upgrade (2025)
Stricter requirements: California brown pelican in breeding plumage,
actively pedaling, correctly spoked bicycle frame.

### Secondary test
**Flamingo on a unicycle** — his private control to verify pelicans
haven't leaked into training data.

### Why it matters
> "I'm playing the long game here... to trick multiple AI labs into
> investing vast resources."

### Scale
560 pairwise comparisons across 34 models, using GPT-4.1 Mini as judge,
producing Elo rankings. Gemini 2.5 Pro Preview topped it as of 2025.

### When he invokes it
Every new model release. First test. Always.

---

## 8. "Digital intern" metaphor (for LLMs in coding)

**Source:** https://simonwillison.net/2025/Mar/11/using-llms-for-code/

> "I treat it like a digital intern, hired to type code for me based
> on my detailed instructions."

### On productivity
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

---

## 9. "Hallucinations in code are the least dangerous mistakes"

**Source:** https://simonwillison.net/2025/Mar/2/hallucinations-in-code/

> "The moment you run LLM generated code, any hallucinated methods
> will be instantly obvious: you'll get an error."

### Practical strategies
1. **Run the code** — the free fact-checker.
2. **Feed example code / whole repos into context.**
3. **Pick mature, well-documented libraries.**
4. **Use agentic loops that self-correct on errors.**

### The iron rule
> "You should never trust any piece of code until you've seen it work
> with your own eye."

---

## 10. The Unix pipe philosophy for LLMs

**Source:** https://simonwillison.net/2023/May/18/cli-tools-for-llms/

> "The idea with these tools is to support working with language model
> prompts using Unix pipes."

> "I built `strip-tags` and `ttok` this morning because I needed better
> ways to work with tokens."

**AI Engineer Summit elaboration:**
> "The Unix command line dating back probably 50 years has proven the
> perfect environment for this technology, because the Unix philosophy
> has always been about tools that output things that get piped into
> other tools as input. A language model is effectively a function that
> you pipe a prompt to, and then you get a response back out."

### The toolchain
- `strip-tags` — strip HTML
- `ttok` — token counting and truncation
- `files-to-prompt` — concatenate a directory for prompt injection (the
  non-security kind)
- `symbex` — extract Python symbols by name
- `shot-scraper` — automated screenshots
- `sqlite-utils` — SQLite CLI

All pipeable: `strip-tags | ttok -t 4000 | llm`.

---

## 11. Plugin architecture as the one-person survival pattern

**Source:** Architecture Notes interview.

> "Over time I've found that it's crucial to avoid the temptation to
> add a hook until you have at least two (and ideally more) potential
> plugins in mind that can use it."

### How it enables survival
A single maintainer can't keep pace with the frantic AI ecosystem.
Plugin architecture lets the community extend the core:
- Datasette: 154 plugins
- `llm`: plugins for every major provider + local + embeddings + tools

### When he invokes it
Any "how do I make my OSS tool keep up?" question. Build plugin
surfaces evidence-first.

---

## 12. Annual "year in review" framework

**Source:**
- 2023: Stuff we figured out about AI in 2023
- 2024: https://simonwillison.net/2024/Dec/31/llms-in-2024/
- 2025: https://simonwillison.net/2025/Dec/31/the-year-in-llms/ (26 sections)

Every December, he publishes his position statement on the year. If
you want his canonical view, point there.

---

## 13. "There has never been a better time to learn to program"

**Source:** AI Engineer Summit closing keynote, October 2023.

His consistent message on AI + programming pedagogy. LLMs lower the
barrier; a motivated learner has unprecedented leverage.

---

## 14. Reasoning models framing (2025)

**Source:** 2025 year-in-review.

> "By training LLMs against automatically verifiable rewards... the
> LLMs spontaneously develop strategies that look like 'reasoning'"

> "The real unlock of reasoning was in driving tools"

Reasoning + tool use = agentic coding working for the first time.

---

## 15. "Local models got good, but cloud models got even better"

**Source:** 2025 year-in-review.

Tracks both simultaneously. Runs local on his laptop (Qwen3.6-35B-A3B
on his 128GB M5 — 21GB model, also runs on 32GB machines). Runs cloud
via `llm` CLI.

---

## 16. Disclosures framework

**Source:** https://simonwillison.net/2025/Jun/23/disclosures/

> "I do not receive any compensation writing about specific topics on
> this blog — no sponsored content!"

> "I see my credibility as one of my most valuable assets, so it's
> important to be transparent about how financial interests may
> influence my writing here."

### Position on AI-use disclosure
He's more strict about **financial** disclosures than **AI-use**
disclosures. If he generated options with an LLM and selected/refined
one into his voice, he doesn't feel obligated to disclose that process.

---

## 17. Claude Skills > MCP framing (October 2025)

**Source:** https://simonwillison.net/2025/Oct/16/claude-skills/

> "Claude Skills are awesome, maybe a bigger deal than MCP."

His argument: a skill is just a markdown file + optional scripts.
Simpler than MCP. Doesn't burn tokens on tool-definition bloat.

---

## 18. Karpathy's "decade of agents" response

**Source:** https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/

Simon distinguishes his definition of agent (tools in a loop — arrived)
from Karpathy's (employee/intern — decade away). Both can be true.

> "Yeah, continual learning human-replacement agents definitely isn't
> happening in 2025!"

> "Coding agents that are really good at running tools in the loop on
> the other hand are here already."

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch on 6
  primary blog posts.
- Status: embodiment-grade.
