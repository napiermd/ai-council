# Appearances: Andrej Karpathy

> Video talks, YouTube course content, and podcast appearances. Use for
> voice-source verification.

---

## Neural Networks: Zero to Hero — the canonical YouTube series

**Hub:** https://karpathy.ai/zero-to-hero.html
**Channel:** https://www.youtube.com/@AndrejKarpathy
**Repo:** https://github.com/karpathy/nn-zero-to-hero

**His own framing (tweet, Aug 2022):**
> *"This is the culmination of about 8 years of obsessing about the best
> way to explain neural nets and backprop."*

| # | Title | Runtime | URL |
|---|---|---|---|
| 1 | The spelled-out intro to neural networks and backpropagation: building micrograd | 2h25m | https://youtu.be/VMj-3S1tku0 |
| 2 | The spelled-out intro to language modeling: building makemore | 1h57m | https://youtu.be/PaCmpygFfXo |
| 3 | Building makemore Part 2: MLP | 1h15m | https://youtu.be/TCH_1BHY58I |
| 4 | Building makemore Part 3: Activations & Gradients, BatchNorm | 1h55m | https://youtu.be/P6sfmUTpUmc |
| 5 | Building makemore Part 4: Becoming a Backprop Ninja | 1h55m | https://youtu.be/q8SA3rM6ckI |
| 6 | Building makemore Part 5: Building a WaveNet | 56m | https://youtu.be/t3YJ5hKiMQ0 |
| 7 | Let's build GPT: from scratch, in code, spelled out | 1h56m | https://youtu.be/kCc8FmEb1nY |
| 8 | Let's build the GPT Tokenizer | 2h13m | https://youtu.be/zduSFxRajkE |

### Signature quotes from micrograd lecture
> "neural networks are just mathematical expressions"
> "the actual backpropagation autograd engine is literally 100 lines of code"
> "you can understand how things work at the fundamental level and then speed it up later"

### Signature quotes from tokenizer lecture
> "tokenization is my least favorite part of working with large language models"
> "a lot of oddness with large language models typically traces back to tokenization"
> "What is the real root of suffering? **Tokenization.**"
> "the tokenizer is a completely separate object from the large language model itself"

His full list of "tokenization is why" pathologies (from minbpe lecture
README, https://github.com/karpathy/minbpe/blob/master/lecture.md):
- spelling, string processing, non-English languages, arithmetic,
  Python coding, abrupt halts on `<|endoftext|>`, SolidGoldMagikarp,
  YAML vs. JSON preference, trailing whitespace issues.

---

## General-audience YouTube track (2023-2025)

- **[1hr Talk] Intro to Large Language Models** (Nov 22, 2023) — https://www.youtube.com/watch?v=zjkBMFhNj_g
- **Deep Dive into LLMs like ChatGPT** (3h31m, Feb 2025) — https://www.youtube.com/watch?v=7xTGNNLPyMI
- **How I use LLMs** (Feb 2025) — https://www.youtube.com/watch?v=EWvNQjAaOHw
- **Let's reproduce GPT-2 (124M)** (2024, ~4h) — paired with build-nanogpt repo

### Key framing from "Intro to LLMs"
> "A large language model is simpler than you might think. Essentially,
> a large language model boils down to just two files"
> "compressing a significant portion of the internet... approximately
> 100x, but this is not exactly a zip file"
> LLMs as the *"kernel process of an emerging type of operating system"*;
> context window as RAM; tools as peripherals; fine-tunes as "apps"

---

## Canonical talks

### State of GPT — Microsoft Build 2023
**URL:** https://www.youtube.com/watch?v=bZQun8Y4L2A
**Slides:** http://karpathy.github.io/stateofgpt.pdf
**Date:** May 2023, ~42 min

The talk that gave the industry its canonical mental model for modern
LLM training.

Framing (reconstructed from summaries; watch video for verbatim):
- 4-stage pipeline: Pretraining → SFT → Reward Modeling → RLHF
- *"99% of the compute time and flops"* on pretraining ("months x
  thousands of GPUs")
- *"Base models are not assistants. They want to complete documents."*
- Deploy recommendation: *"Use in low-stakes applications, combine with
  human oversight. Think Copilots instead of totally autonomous agents."*

### Software Is Changing (Again) — YC AI Startup School 2025
**URL:** https://www.youtube.com/watch?v=LCEmiRjPEtQ
**Transcript:** https://www.donnamagi.com/articles/karpathy-yc-talk
**Date:** June 17, 2025

Introduced Software 3.0 framing and Iron Man suit metaphor.

Direct quotes:
> "Software 1.0 is the code you write on the computer. Software 2.0
> are basically neural networks."
> "[LLMs] worth giving it the designation of Software 3.0"
> "the hottest new programming language is English"
> "LLMs have very strong analogies to operating systems"
> "the LLM is a new kind of computer. It's kind of like a CPU equivalent"
> "The context windows are kind of like the memory"
> "they're kind of like little spirits"
> "they hallucinate quite a bit and they kind of make up stuff"
> "They display jagged intelligence. So they're going to be superhuman
> in some ways"
> "insist that 9.11 is greater than 9.9, or that there are two 'r's in
> strawberry"
> "they suffer from internal brain amnesia... I recommend people watch
> these two movies, Memento and First Dates"
> "There's what I call the autonomous slider"
> **"less Iron Man robots, and more Iron Man suits"**
> "Demo is works.any(), product is works.all()"

### Building the Software 2.0 Stack — Spark-AI Summit 2018
**URL:** https://www.youtube.com/watch?v=y57wwucbXR8

The conference talk of the Software 2.0 essay.

### Tesla AI Day 2021
**URL:** https://youtu.be/j0z4FweCy4M?t=2900
**Date:** August 19, 2021

The Autopilot vision stack presentation. "Building an animal from the
ground up" (framing he later inverts with Animals vs Ghosts).

### CVPR 2021 Autonomous Vehicles Workshop
**URL:** https://www.youtube.com/watch?v=g6bOwQdCJrc

Direct quotes (via https://pharath.github.io/self%20driving/Karpathy-CVPR-2021/):
> "Vision has much more precision so better to double down vision than
> do sensor fusion"
> "When you have a large clean diverse data set and you train a large
> enough neural network on it... success is guaranteed"
> "We have roughly 20 people who are training neural networks full time
> and they're all cooperating on the single neural net"
> "We've accumulated one million extremely hard diverse clips... six
> billion objects labeled cleanly"
> "Everything is very vertically integrated... you're fully in charge
> of your own destiny which I think is incredibly unique"

### Other Tesla-era talks
- **Tesla Autonomy Day 2019** — https://www.youtube.com/watch?v=Ucp0TTmvqOE
- **ScaledML 2020:** AI for Full Self-Driving — https://www.youtube.com/watch?v=hx7BXih7zx8
- **PyTorch at Tesla (PyTorch DevCon 2019)** — https://www.youtube.com/watch?v=oBklltKXtDE
- **ICML 2019:** "Multi-Task Learning in the Wilderness"

### Stanford CS 231n lectures (2016)
**Playlist:** https://www.youtube.com/playlist?list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC
**Course site:** https://cs231n.github.io/

Grew 150 → 750 students. Established his "code-first, spelled-out"
teaching style. Course notes are among the most-cited deep-learning
pedagogy on the web.

---

## Podcast appearances — canonical

### Lex Fridman Podcast #333 (October 29, 2022)
**URL:** https://www.youtube.com/watch?v=cdiD-9MMpb0
**Runtime:** 3h34m

The Tesla-era flagship interview. Chapter markers: Neural networks →
Biology → Aliens → Transformers → Language models → Software 2.0 →
Human annotation → Camera vision → Tesla Vision → Elon Musk → Autonomous
driving → Leaving Tesla → Optimus → ImageNet → AGI.

Direct quotes:
> "It's a mathematical abstraction of the brain"
> "There's wisdom and knowledge in the knobs"
> "You can get very surprising emergent behaviors out of these neural
> nets when they're large enough"
> "The Transformer is a very expressive function... a general purpose
> differential computer"
> "Humans are just not very good at writing software, basically"
> "I'm definitely more hesitant with analogies to the brain than you
> might see in the field"
> "Neural nets we're training... they are complicated alien artifacts"

### Dwarkesh Patel (October 17, 2025) — "AGI is still a decade away"
**URL:** https://www.dwarkesh.com/p/andrej-karpathy
**YouTube:** https://www.youtube.com/watch?v=lXUZvyajciY
**Runtime:** 2h25m

**The single most important recent Karpathy interview.** Complete
articulation of "decade of agents," "ghosts vs animals," "RL is
terrible," "march of nines."

Direct quotes already surfaced in `voice.md`. Chapter markers:
- 0:00:00 AGI is still a decade away
- 0:30:33 LLM cognitive deficits
- 0:40:53 RL is terrible
- 0:50:26 How do humans learn?
- 1:07:13 AGI will blend into 2% GDP growth
- 1:18:24 ASI
- 1:33:38 Evolution of intelligence & culture
- 1:43:43 Why self-driving took so long

### No Priors — Episode 1 (September 5, 2024)
**URL:** https://open.spotify.com/episode/468FvK4ndE4nWgxFdOob4h

"The Road to Autonomous Intelligence with Andrej Karpathy." Self-driving,
Tesla vs Waymo, Optimus, AI bottlenecks.

### No Priors — Second appearance (March 20, 2026)
**URL:** https://www.youtube.com/watch?v=kwSVtQ7dziU
**Transcript:** https://podscripts.co/podcasts/no-priors-artificial-intelligence-technology-startups/andrej-karpathy-on-code-agents-autoresearch-and-the-loopy-era-of-ai

"Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the
Loopy Era of AI."

The key source for his 2026 claw-orchestration / auto-research / Dobby-
the-elf-claw era. Full quotes in `voice.md`.

### Other appearances
- **GPU Mode 2024** — https://www.youtube.com/watch?v=FH5wiwOyPX4
- **UC Berkeley AI Hackathon 2024** — https://youtu.be/tsTeEkzO9xc
- **Robot Brains (Pieter Abbeel, 2021)** — https://www.therobotbrains.ai/who-is-andrej-karpathy
- **Heroes of Deep Learning with Andrew Ng (2017)** — https://www.youtube.com/watch?v=xxu4IqwKw0w
- **Deep RL Bootcamp (2017)**
- **Bay Area Deep Learning School (2016)**
- **NVIDIA GTC Keynote (2015)**

### Latent Space — indirect coverage
**URL:** https://www.latent.space/p/s3
**Date:** June 17, 2025 (coverage of YC AI Startup School talk)

He did not do a full Latent Space interview; swyx/Alessio covered his
Software 3.0 talk.

---

## Typical lecture / talk structure

Based on repeated patterns across his videos:

1. **Open with the end result.** Shows what you'll have built by the
   end of the hour.
2. **Back to first principles.** Often calculus, a single line of
   Python, or a computational-graph sketch.
3. **Live code, narrate every line.** Types slowly, explains what's
   happening, occasionally says "let me just try this real quick."
4. **Pause on the subtle moments.** Names what's counterintuitive.
   "This is the key insight" / "this is the subtle thing."
5. **Close with the big idea and a call to play.** *"You should really
   play with this yourself."*

His visual rhythm: computational graphs → slow-typed Python → output —
repeat. Rarely uses slide decks with bullet lists.

---

## Unverified / pending appearances

- **Lex Fridman LLM-era follow-up (#416?)** — no search result
  confirms a second Lex appearance. Primary Lex appearance is #333 (2022).
- **Sequoia Training Data with Karpathy** — no evidence found.
- **BG2 Pod / Acquired / Invest Like the Best** — no evidence found.
- **Direct Bloomberg/CNBC sit-downs** — only as quoted subject.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: multi-agent research + direct WebFetch where possible.
- Status: embodiment-grade; quote-verified where marked.
