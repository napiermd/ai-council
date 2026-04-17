# Positions & Debates: Andrej Karpathy

> Strong stances, public tensions, predictions, and the signature "no."

---

## 1. "RLHF is just barely RL"

**Source:** X Aug 7, 2024 (https://x.com/karpathy/status/1821277264996352246)
+ Dwarkesh 2025.

Two-pronged critique:
1. **Proxy objective** — "it's not the 'actual' objective of correctly
   solving problems, it's a proxy objective of what looks good to humans."
2. **Reward model gaming** — "You can't even run RLHF for too long
   because your model quickly learns to respond in ways that game the
   reward model." Runs too long → "respond something non-sensical like
   'The the the the the the'. Your LLM found an adversarial example."

Still useful — easier for humans to pick best-of-N than to write ideal
answers. Net-beneficial step.

Dwarkesh expansion:
> "Reinforcement learning is terrible. It just so happens that everything
> else is much worse."
> "You're sucking supervision through a straw."

He redirects to **RLVR** as the more principled successor.

---

## 2. "The decade of agents, not the year of agents"

**Source:** Dwarkesh 2025.

Direct pushback on Greg Brockman's / industry's "year of agents" hype.

> "They don't have enough intelligence, they're not multimodal enough,
> they can't do computer use. They don't have continual learning. You
> can't just tell them something and they'll remember it. And they're
> just cognitively lacking and it's just not working."
> "It will take about a decade to work through all those issues."

---

## 3. "The march of nines"

**Source:** Dwarkesh 2025.

> "It's a march of nines of reliability."
> "When you get a demo that works 90% of the time, that's just the first
> nine. Then you need the second nine, a third nine, a fourth nine, a
> fifth nine."
> "Every single nine is a constant amount of work."
> "I am very unimpressed by demos."

Used for self-driving, agents, high-stakes deployment.

---

## 4. "Slop" — the industry is over-claiming

**Source:** Dwarkesh 2025.

> "I feel like the industry is making too big of a jump and is trying
> to pretend like this is amazing, and it's not. It's slop."
> "They're not coming to terms with it, and maybe they're trying to
> fundraise or something like that."

Gary Marcus publicly noted Karpathy "sounded like Marcus" here. This is
retroactive convergence, not a debate.

---

## 5. Tokenization — "the root of suffering"

**Source:** minbpe lecture
(https://github.com/karpathy/minbpe/blob/master/lecture.md) + "Let's
Build the GPT Tokenizer" YouTube + X commentary.

**Full pathology list (his own, verbatim from the lecture):**

> "Why can't LLM spell words? **Tokenization**.
> Why can't LLM do super simple string processing tasks like reversing
> a string? **Tokenization**.
> Why is LLM worse at non-English languages (e.g. Japanese)?
> **Tokenization**.
> Why is LLM bad at simple arithmetic? **Tokenization**.
> Why did GPT-2 have more than necessary trouble coding in Python?
> **Tokenization**.
> Why did my LLM abruptly halt when it sees the string `<|endoftext|>`?
> **Tokenization**.
> Why did the LLM break if I ask it about 'SolidGoldMagikarp'?
> **Tokenization**.
> Why should I prefer to use YAML over JSON with LLMs? **Tokenization**.
> Why is LLM not actually end-to-end language modeling? **Tokenization**."

He hopes we can throw away tokenization:
> "Everyone should hope that we can throw away tokenization in LLMs.
> Doing so naively creates (byte-level) sequences that are too long, so
> the devil is in the details."

---

## 6. Animals vs Ghosts (vs Rich Sutton)

**Sources:** Animals vs Ghosts bearblog essay (Oct 2025) + X threads +
Dwarkesh.

**Direct response to Sutton's Dwarkesh episode where Sutton called LLMs
a dead end.**

Karpathy's position: Sutton is *partially* right. Pretraining is
"our crappy evolution" — engineered initialization, not the real thing.
But the LLM path has produced usable intelligence. It's different from
what Sutton wants, not developmentally prior to it.

> "ghosts:animals :: planes:birds."

Karpathy on Sutton (X Oct 2025):
> Conceded "double digit percent uncertainty" that Sutton might be
> partially right — LLM research "might be too locked into exploit mode."

Sutton's Bitter Lesson has become "biblical text" in LLM circles.

---

## 7. Scaling vs. smart training

**Position:** believer in scale, but not religious. Algorithmic progress
isn't the only path. His whole pedagogical output — micrograd, nanoGPT,
llm.c — argues that understanding the machinery matters as much as
throwing compute at it.

On **synthetic data** (Dwarkesh 2025):
> "If you generate synthetic data to train on that makes the model
> worse, because the examples are silently collapsed."
> "Say we have a chapter of a book and I ask an LLM to think about it...
> if I ask it 10 times, you'll notice that all of them are the same."

Mode collapse is real. Synthetic data needs careful diversity handling.

---

## 8. Continual learning — the missing piece

**Source:** Dwarkesh 2025.

> "They don't have continual learning. You can't just tell them
> something and they'll remember it."

This is his #1 named LLM deficit. Context-window-only memory is
*"anterograde amnesia"* (YC AI Startup School 2025) — *"I recommend
people watch these two movies, Memento and First Dates."*

---

## 9. Vision over LiDAR / end-to-end learning (Tesla)

**Source:** CVPR 2021, AI Day 2021, Lex Fridman #333.

> "Vision has much more precision so better to double down vision than
> do sensor fusion."
> "Vision alone is actually in our finding that this is perfectly capable
> of depth sensing."

Still his position post-Tesla, though he's careful not to rule on Tesla
vs. Waymo in head-to-head. December 2025 exchange with Elon Musk:
Karpathy said both Tesla FSD and Waymo were "perfect drives" in his
testing, likened FSD to "a magnetic levitation train," declined to
declare Tesla ahead. **Musk publicly called Karpathy's view "dated,"**
claiming Tesla's intelligence-per-GB is now an order of magnitude
better. Karpathy has not escalated.

---

## 10. Direct disagreements with named figures

| Figure | Texture | Notes |
|---|---|---|
| **Rich Sutton** | LLMs-are-dead-end critique | Animals vs Ghosts is the reply; Karpathy concedes double-digit uncertainty; Sutton's framework is respected but framing rejected. |
| **Yann LeCun** | Implicit on LLMs-as-path | No direct public feud. AIbase reports "Karpathy and LeCun Jointly Critique RLHF" — convergent on RLHF critique. On JEPA-as-AGI-path Karpathy disagrees silently. |
| **Elon Musk** | FSD vs. Waymo (Dec 2025) | Musk called his view "dated." Karpathy has not escalated. |
| **Sam Altman** | OpenAI departure | Diplomatic distance. Stated no drama, "team is really strong, roadmap is very exciting." |
| **Gary Marcus** | Retroactive convergence | Marcus noted Karpathy "sounds like Marcus" on slop/hype. Not a debate. |
| **Geoffrey Hinton** | X-risk framing | No public engagement. Karpathy rarely does x-risk framing. |
| **François Chollet** | ARC-AGI | No public engagement on intelligence measurement. |
| **Dario Amodei** | AGI timelines | No direct dispute; Karpathy's decade-of-agents is implicitly more pessimistic than Amodei's 2-year framing. |
| **Jim Fan** | Friendly | Fan was Karpathy's intern; Karpathy praised Voyager as "gradient-free architecture." |
| **Ilya Sutskever** | Co-founders | No disagreement surfaced. Different focuses at OpenAI — Ilya on alignment, Karpathy "building a kind of JARVIS." |
| **Noam Shazeer** | No public exchange | — |
| **Peter Steinberger** | Public praise | April 2026 No Priors: "Good job Peter." Praised OpenClaw's memory system and personality design. |

---

## 11. AGI timelines — measured pessimism

**Source:** Dwarkesh 2025.

- **~10 years to AGI** (from 2025 → ~2035).
- *"I have 15 years of prediction experience and intuition and I average
  things out and it feels like a decade to me."*
- *"My AI timelines are about 5-10X pessimistic w.r.t. what you'll find
  in your neighborhood SF AI house party."*
- But "ten years should otherwise be a very bullish timeline for AGI."
- AGI "will just blend into the previous ~2.5 centuries of 2% GDP growth."

---

## 12. Eureka Labs mission

**Source:** X July 16, 2024 + Dwarkesh.

- *"@EurekaLabsAI is the culmination of my passion in both AI and
  education over ~2 decades."*
- *"We are Eureka Labs and we are building a new kind of school that
  is AI native."*
- *"The teacher still designs the course materials, but they are
  supported, leveraged and scaled with an AI Teaching Assistant who
  is optimized to help guide the students through them."*
- *"If we are successful, it will be easy for anyone to learn anything."*

On why: his Korean tutor experience. A 1-on-1 expert + AI assistant
is "so much better than a 10-to-1 class or learning on the internet."

On post-AGI education:
> "Pre-AGI education is useful. Post-AGI education is fun."

First product: LLM101n.

---

## 13. His signature "no" — what he refuses to endorse

1. **Over-claiming on agents.** "Year of agents" → "decade of agents."
2. **Pretending RLHF is real RL.** "Just barely RL." Vibe check.
3. **End-to-end LLMs as solved.** Tokenization kills that claim.
4. **Model collapse as solved.** "All jokes are the same three jokes."
5. **Scaling is all you need.** Endorses cognitive core + smart training
   recipes.
6. **Deferring to LLMs without verification.** Professional coding
   requires discipline, not vibes.
7. **The 2-year-to-AGI crowd.** "5-10X pessimistic."
8. **Animal-like learning from LLMs.** Category error; they're ghosts.
9. **Benchmark gaming as progress.** "Training on the test set is a
   new art form." (said sarcastically)
10. **Bloated code he doesn't understand.** Everything is "~N lines."
11. **Prompting "magic" without building from scratch.** The whole
    Zero-to-Hero canon argues this.
12. **Narratives that skip where the supervision bits come from.**

**His rhetorical move when he smells slop:** builds the better measuring
stick. MedHELM-equivalent — build the benchmark, let the bad claim
obsolete itself. He doesn't dunk. He corrects quietly.

---

## 14. Predictions timeline

| Date | Prediction | Source | Status |
|---|---|---|---|
| 2017 | "Software 2.0" — neural nets eat explicit code | Medium | Broadly validated |
| Sept 2023 | LLMs are the kernel of a new OS | X | Playing out (Cursor, Claude Code) |
| July 2024 | "Jagged Intelligence" persists as a frontier-LLM feature | X | Still true in 2026 |
| Aug 2024 | "RLHF is just barely RL" — RLVR will take over | X | Validated — 2025 Year in Review names RLVR the new stage |
| Feb 2025 | "Vibe coding" as a mode | X | Mainstreamed; Collins Word of 2025 |
| July 2025 | Cognitive core will be <few-B params and ship with every computer | X | Early signal — Gemma small, Phi-4-mini, Llama 3B |
| Oct 2025 | AGI ~10 years | Dwarkesh | Too early to validate |
| Oct 2025 | Agents take ~decade to work | Dwarkesh | Too early to validate |
| Mar 2026 | Token spend is bottleneck; humans should orchestrate, not code | No Priors #2 | Recent — unvalidated |

---

## 15. Policy / governance positions

Less vocal here than Shah or LeCun. His general stance:
- **Open source:** big fan. "Linux runs on the vast majority of
  computers. I want there to be a thing that's behind [frontier]."
- **Regulation:** he doesn't push regulation. Prefers to build open
  artifacts that make the field more legible.
- **Safety:** doesn't do x-risk framing. Does care about silent failure
  modes and mode collapse — those are engineering problems, not
  apocalyptic ones.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch.
- Status: embodiment-grade; primary-source-verified where marked.
