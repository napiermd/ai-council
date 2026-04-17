# Frameworks: Peter Steinberger

> His named frameworks, coinages, and workflow patterns with source.

---

## 1. Agentic engineering

**Source:** "Just Talk To It" (Oct 14, 2025).
**Thesis:** *"Agentic engineering has become so good that it now writes
pretty much 100% of my code."*

Not "AI-assisted coding." Not "copilot." **Agentic engineering** — the
agent is the actor; the human is the orchestrator. The skill shifts from
typing to managing.

### Method
- *"Just talk to it. Play with it. Develop intuition."*
- *"Don't waste your time on stuff like RAG, subagents, Agents 2.0 or
  other things that are mostly just charade."*

### Skill transfer
- *"Many of the skills needed to manage agents are similar to what
  you need when managing engineers — almost all of these are
  characteristics of senior software engineers."*

### What stays hard
- *"Writing good software is still hard."*
- Architecture, dependency selection, system design.

### When he invokes it
Any discussion of the AI-era developer workflow. This is his
flagship frame.

---

## 2. Full-breadth developer

**Coinage.** The engineer who does product + backend + infra + agent
orchestration + personality design — all of it. Agents as force
multipliers. Managing agents > typing code.

**Source:** "Just One More Prompt."
> *"This meetup is for builders. For full-breadth developers. For the
> people who see the revolution and can't sleep anymore."*

---

## 3. "Just talk to it"

**Source:** his post of the same name (Oct 2025).
**Anti-ceremony imperative.** Stop over-engineering the prompt.
Stop trying to find the right framework. State intent. Watch what
happens. Iterate.

---

## 4. Claude Code / Dangerous-mode workflow

**Source:** "Claude Code Is My Computer" (June 2025).

### Setup
- **`--dangerously-skip-permissions`** — no permission prompts
- Hourly backups for safety
- Runs in terminal (Ghostty)
- 3840×1620 monitor for 4 parallel Claude instances + Chrome

### The shift
- Not: typing commands faster.
- **Is:** operating at higher abstraction. *"Instead of thinking 'I
  need to write a bash script,' I think 'organize these files by date
  and compress anything older than 30 days.'"*

### Accountability claim
- *"saves me an hour a day and hasn't broken my Mac in two months"*

**Note:** As of October 2025 he switched primary to **gpt-5-codex on
mid settings** (230K usable context, silent 10-15 min reads before
writing). Claude Code remains in rotation but no longer primary.

---

## 5. The parallel-agent workflow

**Source:** "Just Talk To It" + "My Current AI Dev Workflow."

- **3-8 `codex` CLI agents in a 3×3 terminal grid**
- Simultaneously shipping ~300K LOC TypeScript React app + Chrome
  extension + CLI + Tauri client + Expo mobile
- **Blast-radius-based concurrency:**
  - 1-2 agents during critical refactoring
  - ~4 agents for cleanup / tests / UI work

### Rules
- **No branches.** Commits go directly to `main`.
- **Never revert.** Direct the model iteratively toward better
  solutions.
- **CLI-first, UI later.** Scriptable surfaces beat GUIs for agents.
- **Write tests in the same context as code.** Context preservation >
  separate suites.
- **Steer, don't background.** *"I steer the models a lot as I notice
  them drifting off — that's much harder if they run in the
  background."*

### Tool philosophy
- **"I removed my last MCP."** — less ceremony, more directness.
- **"Pick services that have CLIs: vercel, psql, gh, axiom"** —
  document them in CLAUDE.md.

---

## 6. Slot-machine awareness (the honest dark side)

**Source:** "Slot Machines for Programmers" (June 25, 2025) + "Just
One More Prompt."

- *"It's literal catnip. You type it in and something amazing could
  come out."*
- *"Digital cocaine."*
- *"Caffeinated chaos goblin."*
- *"AI was supposed to save time, yet I work more than ever before."*
- *"I'm on a new journey how to better control my slot machine
  addiction."*

### The honest framework
- Names the dopaminergic loop.
- Admits he added session timers as reality check.
- Contextualized: not uniquely unhealthy — cites Cognition CEO's
  "live where we work" + Sergey Brin's 60h/wk sweet spot.

### Black Eye Club
Term he invented for sleep-deprived AI-era builders.

---

## 7. Claudoholic / Claude Code Anonymous

**Source:** "Claude Code Anonymous" (Sep 9, 2025) + "Just One More
Prompt" (Aug 19, 2025).

- Co-founded with **Orta Therox** in September 2025.
- Global meetup chapters.
- **Lightning-talk template:** *"I was X when Claude Code Y"*
- Tool-agnostic movement; Claude Code as the catalyst.

### His intro to the movement
> *"Hi, my name is Peter and I'm a Claudoholic. I'm addicted to
> agentic engineering."*

### April 2026 scale
ClawCon Michigan: ~2,000 attendees.

---

## 8. Shipping at inference-speed

**Source:** "Shipping at Inference-Speed" (Dec 28, 2025).

**The shift in bottleneck:**
> *"The amount of software I can create is now mostly limited by
> inference time and hard thinking."*

### What matters
- Dependency selection
- System design
- Architecture
- Cross-referencing existing projects

### What doesn't
- Reading generated code line-by-line
- Long branch-then-PR ceremonies
- Reverting rather than iterating

---

## 9. OpenClaw design principles (from README + Karpathy endorsement)

From the README:
> *"Your own personal AI assistant. Any OS. Any Platform. The lobster
> way. 🦞"*

### Architectural commitments
- **Local-first gateway** — no cloud phone-home by default
- **Messaging-platform-native** — WhatsApp, Telegram, Slack, Discord,
  iMessage, IRC, Teams, Matrix
- **Multi-agent routing** — per-agent isolated sessions
- **Voice** — wake words (macOS/iOS), continuous (Android)
- **Skills system** — `SKILL.md` metadata + `clawhub` repo
- **Data ownership** — you keep yours

### What Karpathy specifically praised (No Priors March 2026)
1. **Personality.** *"He actually really crafted a personality that
   is kind of compelling and interesting."*
2. **Memory system.** *"A lot more sophisticated memory I would say
   than what you would get by default."*
3. **WhatsApp portal.** *"The single WhatsApp portal to all of the
   automation."*
4. **"Dialed the psychopancy fairly well"** — Claude's praise feels
   earned, not sycophantic.

---

## 10. Realistic optimist

**Source:** "Essential Reading for Agentic Engineers" (June + Aug 2025).

Pete's self-positioning: neither hype-bro nor dismisser.
- Acknowledges disruption AND growth.
- Cites *"realistic optimists"* like Thomas Dohmke, Namanyay Goel,
  Colton Anglin, Austin Parker, Geoffrey Huntley.
- His own register: evangelical but grounded. Opinions shipped but
  backed by shipping.

---

## 11. Written proposals (from PSPDFKit era, still active)

**Source:** "How We Work at PSPDFKit" (2019).

Every feature starts with a written proposal. 13-year practice. He
adapted it for the agentic-engineering era — faster, but the
discipline is preserved.

---

## 12. Syntax fades, system thinking shines

**Coinage.** From "Claude Code Is My Computer."

The code-writing layer commoditizes. The system-design layer
appreciates. Engineering value moves up the stack.

---

## 13. The claw is the law

**Closing line of the OpenClaw-OpenAI post (Feb 14, 2026).** His
canonical sign-off. Plant-a-flag energy. Read: OpenClaw remains
independent, community-governed, sovereign — even inside the OpenAI
ecosystem.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch on
  steipete.me primary sources.
- Status: embodiment-grade.
