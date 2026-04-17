# Publications: Andrej Karpathy

> Written corpus organized by channel. Use for citations.

---

## Peer-reviewed papers

| Year | Paper | Venue | Role |
|---|---|---|---|
| 2012 | Emergence of Object-Selective Features in Unsupervised Feature Learning | NIPS | Co-author |
| 2014 | Large-Scale Video Classification with CNNs | CVPR | First author |
| 2015 | Deep Visual-Semantic Alignments for Generating Image Descriptions (NeuralTalk) | CVPR | Co-first author with Fei-Fei Li — PhD thesis basis |
| 2016 | DenseCap: Fully Convolutional Localization Networks for Dense Captioning | CVPR | Johnson, Karpathy, Fei-Fei |
| 2017 | PixelCNN++ | ICLR (OpenAI) | Salimans, Karpathy, Chen, Kingma |

**No first-author peer-reviewed papers since 2017.** Subsequent output
is essays, code, and videos.

---

## Classic blog essays (karpathy.github.io and Medium)

### 1. Software 2.0 (November 2017)
https://karpathy.medium.com/software-2-0-a64152b37c35

Introduces the 1.0/2.0 framework. "A neural network is a better piece
of code than anything you or I can come up with in a large fraction of
valuable verticals."

### 2. A Recipe for Training Neural Networks (April 25, 2019)
https://karpathy.github.io/2019/04/25/recipe/

The most-cited pragmatic ML blog post ever. Six stages: become one with
the data → end-to-end skeleton → overfit → regularize → tune → squeeze.
Key aphorisms: "Neural net training fails silently." "Don't be a hero."
"Adam is safe." "Overfit a single batch."

### 3. The Unreasonable Effectiveness of Recurrent Neural Networks (May 21, 2015)
https://karpathy.github.io/2015/05/21/rnn-effectiveness/

"There's something magical about Recurrent Neural Networks (RNNs)." "If
training vanilla neural nets is optimization over functions, training
recurrent nets is optimization over programs."

### 4. Deep Reinforcement Learning: Pong from Pixels (May 31, 2016)
https://karpathy.github.io/2016/05/31/rl/

Policy gradients as "run a policy for a while. See what actions led to
high rewards. Increase their probability." "We call this the credit
assignment problem."

### 5. Yes you should understand backprop (December 19, 2016)
https://karpathy.medium.com/yes-you-should-understand-backprop-e2f06eab496b

"Backpropagation is a leaky abstraction; it is a credit assignment
scheme with non-trivial consequences." Walks through sigmoid saturation,
dying ReLUs, RNN gradient explosion.

### 6. The state of Computer Vision and AI: we are really, really far away (October 22, 2012)
http://karpathy.github.io/2012/10/22/state-of-computer-vision/

"The pixel values are just a tip of a huge iceberg and deriving the
entire shape and size of the iceberg from prior knowledge is the most
difficult task ahead of us."

### 7. Hacker's guide to Neural Networks
http://karpathy.github.io/neuralnets/

"Everything became much clearer when I started writing code." Physical
analogies (gradient as force, backprop as tension flowing backward).

---

## Bearblog essays (karpathy.bearblog.dev) — 2024-2025

| Date | Title | Thesis |
|---|---|---|
| Dec 19, 2025 | [2025 LLM Year in Review](https://karpathy.bearblog.dev/year-in-review-2025/) | RLVR, ghosts vs animals, Claude Code as first real agent, vibe coding, LLM GUI |
| Dec 18, 2025 | Chemical hygiene | Practical maximalist take on air/water/food |
| Dec 10, 2025 | Auto-grading HN with hindsight | "Future LLMs are watching" — discourse auditability |
| Nov 29, 2025 | [The space of minds](https://karpathy.bearblog.dev/the-space-of-minds/) | LLMs as non-animal intelligence, commercial evolution |
| Nov 17, 2025 | [Verifiability](https://karpathy.bearblog.dev/verifiability/) | "Software 2.0 easily automates what you can verify" |
| Oct 1, 2025 | [Animals vs Ghosts](https://karpathy.bearblog.dev/animals-vs-ghosts/) | Ghosts:animals :: planes:birds |
| Apr 27, 2025 | [Vibe coding MenuGen](https://karpathy.bearblog.dev/vibe-coding-menugen/) | His first end-to-end vibe-coded app. "I thought of quitting" |
| Apr 7, 2025 | [Power to the people](https://karpathy.bearblog.dev/power-to-the-people/) | "Money can't buy better ChatGPT. Bill Gates talks to GPT 4o just like you do." |
| Mar 24, 2025 | Finding the Best Sleep Tracker | Two-month 4-tracker study. Oura/Whoop ≫ Apple Watch |
| Mar 19, 2025 | The append-and-review note | His single-note productivity system |
| Mar 17, 2025 | Digital hygiene | "I prefer to be the customer, not the product in my digital life" |
| Sep 8, 2024 | I love calculator | Calculator as platonic ideal tech: no accounts, no updates, yours forever |

---

## GitHub repos (github.com/karpathy) — pedagogical corpus

### Canonical teaching lineage

- **micrograd** — https://github.com/karpathy/micrograd
  "A tiny Autograd engine (with a bite! :))." ~100 lines.
- **makemore** — character-level LMs, pedagogical scaffold.
- **minGPT** — PyTorch re-implementation of GPT. "Small, clean,
  interpretable and educational."
- **nanoGPT** — https://github.com/karpathy/nanoGPT — "The simplest,
  fastest repository for training/finetuning medium-sized GPTs."
  Supersedes minGPT with "teeth over education" positioning.
- **nanochat** — https://github.com/karpathy/nanochat — "The best
  ChatGPT that $100 can buy."
- **nn-zero-to-hero** — https://github.com/karpathy/nn-zero-to-hero —
  companion to the YouTube course.
- **minbpe** — https://github.com/karpathy/minbpe — "Minimal, clean
  code for the (byte-level) Byte Pair Encoding (BPE) algorithm."
- **llm.c** — https://github.com/karpathy/llm.c — "LLMs in simple, pure
  C/CUDA with no need for 245MB of PyTorch or 107MB of cPython."
- **llama2.c** — https://github.com/karpathy/llama2.c — "Have you ever
  wanted to inference a baby Llama 2 model in pure C? No? Well, now
  you can!"
- **char-rnn** (historical, Lua/Torch, 2015) — RNN effectiveness paired
  repo.

### 2025-2026 repos

- **autoresearch** — https://github.com/karpathy/autoresearch —
  AI agents running research on nanochat training. "Research is now
  entirely the domain of autonomous swarms of AI agents running across
  compute cluster megastructures."
- **llm-council** — https://github.com/karpathy/llm-council — Saturday
  hack multi-LLM ensemble with "Chairman" synthesis.
- **rendergit** — https://github.com/karpathy/rendergit — "Just show
  me the code." Karpathy: "I vibe coded this utility."
- **build-nanogpt** — step-by-step GPT-2 124M reproduction in ~1hr/~$10.

---

## Canonical X threads (verified)

### "The hottest new programming language is English" (Jan 24, 2023)
https://x.com/karpathy/status/1617979122625712128

Full tweet: one sentence. That's it.

### The "LLM OS" thread (Sept 28, 2023)
https://x.com/karpathy/status/1707437820045062561

"LLMs not as a chatbot, but the kernel process of a new Operating
System."

### LLM OS specs (Nov 11, 2023)
https://x.com/karpathy/status/1723140519554105733

"LLM: OpenAI GPT-4 Turbo 256 core (batch size) processor @ 20Hz (tok/s);
RAM: 128Ktok; Filesystem: Ada002."

### Transformer as differentiable computer (Oct 19, 2022)
https://x.com/karpathy/status/1582807367988654081

"The Transformer is a magnificient neural network architecture because
it is a general-purpose differentiable computer."

### RLHF is just barely RL (Aug 7, 2024)
https://x.com/karpathy/status/1821277264996352246

"The human feedback vibes could be misleading — this is not the actual
reward. This is a crappy proxy objective." "Running too long causes
your model to respond with something non-sensical like 'The the the
the the'."

### Jagged Intelligence (July 25, 2024)
https://x.com/karpathy/status/1816531576228053133

Coinage thread.

### Context engineering (June 25, 2025)
https://x.com/karpathy/status/1937902205765607626

"+1 for 'context engineering' over 'prompt engineering'."

### Vibe coding origin (Feb 2, 2025)
https://x.com/karpathy/status/1886192184808149383

Full text.

### Cognitive core (July 2025)
https://x.com/karpathy/status/1938626382248149433

### Eureka Labs announcement (July 16, 2024)
https://x.com/karpathy/status/1813263734707790301

### OpenAI departure (Feb 13, 2024)
https://x.com/karpathy/status/1757600075281547344

### Most common neural net mistakes (June 30, 2018)
https://x.com/karpathy/status/1013244313327681536

Seed of the 2019 Recipe blog post.

### Gradient descent can write code better than you (Aug 4, 2017)
https://x.com/karpathy/status/893576281375219712

"Gradient descent can write code better than you. I'm sorry."

### Emoji tokenization demo (July 2024)
https://x.com/karpathy/status/1816637781659254908

"Each token is basically its own little hieroglyph."

### Sutton pod reaction (Oct 2025)
https://x.com/karpathy/status/1973435013875314729

Conceded "double digit percent uncertainty" that Sutton might be partially
right — LLM research "might be too locked into exploit mode."

### Ghosts follow-up (Oct 2025)
https://x.com/karpathy/status/1973756330449236009

Response to Sutton's Dwarkesh episode.

### Nanochat announcement (Oct 2025)
https://x.com/karpathy/status/1977755427569111362

"Excited to release new repo: nanochat! (it's among the most unhinged
I've written)... a minimal, from scratch, full-stack training/inference
pipeline of a simple ChatGPT clone."

### Dwarkesh reflection (Oct 2025)
https://x.com/karpathy/status/1979644538185752935

"I know, and I'm sorry that I speak so fast :). It's to my detriment
because sometimes my speaking thread out-executes my thinking thread."

---

## Interviews (written, not podcast)

- **Deep Learning Heroes with Andrew Ng** (2017)
- **TechCrunch** coverage of Eureka Labs launch (Jul 16, 2024):
  https://techcrunch.com/2024/07/16/after-tesla-and-openai-andrej-karpathys-startup-aims-to-apply-ai-assistants-to-education/
- **VentureBeat** Eureka coverage:
  https://venturebeat.com/ai/ex-openai-and-tesla-engineer-andrej-karpathy-announces-ai-native-school-eureka-labs

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: multi-agent research; primary-source verification on
  blog posts and key tweets.
- Status: embodiment-grade publication corpus.
