# Positions & Debates: Jeremy Howard

> Strong positions, disagreements, predictions, his signature "no."

---

## 1. AI democratization — his life's work

**Anchor claim:** Most practitioners don't need PhDs. Domain experts
can leverage the technology themselves if given the right tools.

### Verbatim
> *"I hate creating stuff that most people can't use."* — Latent Space

> *"Can we create an army of passionate domain experts who can change
> their little part of the world?"* — Latent Space

> *"Who's going to listen to me, you know, cause as you said, I don't
> have a PhD, not at a university."* — Latent Space

### fast.ai's stated target audience
> *"uncool languages like C#, uncool operating systems like Windows...
> uncool datasets... and with uncool backgrounds (maybe you didn't go
> to Stanford)"* — fast.ai About

His career-long wager: **domain experts who don't fit the elite ML
archetype produce the most valuable applied work.** Kaggle taught him
this. fast.ai proves it. Answer.AI extends it.

---

## 2. SB-1047 opposition (April-Sept 2024)

**Primary source:** https://www.answer.ai/posts/2024-04-29-sb1047.html

### Verbatim core claims
> *"Open source has been a key enabler of the success of the US
> software industry."*

> *"An AI model is a general purpose piece of software that runs on
> a computer, much like a word processor, calculator, or web browser."*

> *"Placing liability on the creators of general purpose tools like
> these mean that, in practice, such tools can not be created at all,
> except by big businesses."*

> *"Concentrating control within a few large entities creates single
> points of failure and increases the potential for systemic risks."*

> *"By imposing the restrictions on open-source AI, SB-1047 could
> reduce AI safety, through reducing transparency, collaboration,
> diversity, and resilience."*

> *"Instead of regulating the development of AI models, the focus
> should be on regulating their applications."*

### Alignment (parallel, not joint)
- **Andrew Ng** (separate LinkedIn / TIME op-eds)
- **Fei-Fei Li** (Fortune op-ed)
- **Yann LeCun** (Meta; open-source advocate)
- **a16z** (open letter)
- Y Combinator, Meta, Mozilla, EleutherAI, Hugging Face

### Outcome
SB-1047 vetoed by Gov. Newsom on September 29, 2024.

---

## 3. "AI Safety and the Age of Dislightenment" (Nov 7, 2023)

**Source:** https://www.fast.ai/posts/2023-11-07-dislightenment.html

The **umbrella essay** that preceded SB-1047 opposition. Howard
interviewed 60+ experts and reviewed 300+ academic papers before
writing.

### Definition
> *"What if, faced with a new power, with uncertainty, with a threat
> to our safety, we withdraw to the certainty of centralization, of
> control, of limiting power to a select few? This is the
> Dislightenment."*

### Core arguments
> *"the frontier of AI becoming inaccessible to everyone who doesn't
> work at a small number of companies, whose dominance will be
> enshrined by virtue of these ideas."*

> *"Models are, literally, just a bunch of numbers. They can be
> copied trivially easily, and once you've got them, you can pass
> them around to all your friends for nothing."*

> *"security through obscurity is ineffective and dangerous."*

> *"How much safer would you feel if the world's top cyber-security,
> bio-weapons, and social engineering academics were working with the
> benefits of AI... compared to if only a handful of people at a
> for-profit company had full access?"*

### Tyler Cowen (on Marginal Revolution) featured this quote
> *"Proposals for stringent AI model licensing and surveillance will
> likely be ineffective or counterproductive, concentrating power in
> unsustainable ways, and potentially rolling back the societal gains
> of the Enlightenment."*

---

## 4. Against AI x-risk / doomerism

Howard co-signed a rebuttal to CAIS's 2023 "extinction from AI"
statement alongside Seth Lazar and Arvind Narayanan.

He is **simultaneously** bearish on x-risk AND bearish on near-term
AGI hype. He is NOT a LeCun-style full skeptic — he uses LLMs daily.

### From "Jeremy Howard is bearish on LLMs" podcast (Feb 17, 2026)
> *"Can they really extrapolate outside the training distribution?
> The answer is no, they can't."*

> *"I think they can't go outside their distribution because it's
> just something that that type of mathematical model can't do."*

> *"The difference between pretending to be intelligent and actually
> being intelligent is entirely unimportant, as long as you're in the
> region in which the pretense is actually effective."*

### On LLMs as research engines
> *"Breakthrough research requires either: 1. Going in a totally new
> and unexpected direction that everyone decided long ago was stupid,
> or 2. Finding some extraordinary new experimental data that means
> we have to change our theories. LLMs can't run experiments, so
> we'll focus on 1."* — X, July 2024

---

## 5. ULMFiT's legacy (and the credit fight)

**Source:** https://arxiv.org/abs/1801.06146 (Howard & Ruder, 2018)

Howard has pushed back publicly on the erasure of ULMFiT in LLM
lineage stories.

### X, March 2025
> *"I'm glad @levelsio checked this, but sad our contrib has been
> erased by later big tech co's. Alec Radford said ULMFiT inspired
> GPT. ULMFiT's first demo predated BERT. Today's 3-stage LLM approach
> of general corpus pretraining and 2 stages of fine-tuning was
> pioneered by ULMFiT."*

### His reframing of fine-tuning
> *"There's no such thing [as fine-tuning vs. pre-training]. There's
> only continued pre-training."* — Latent Space

> *"I still don't know how to fine tune language models properly and
> I haven't found anybody who feels like they do."* — Latent Space

---

## 6. ModernBERT — small models still matter

**Source:** https://www.answer.ai/posts/2024-12-19-modernbert.html

> *"BERT was released in 2018 (millennia ago in AI-years!) and yet
> it's still widely used today."*

> *"A frontier model like OpenAI's O1 is like a Ferrari SF-23... It
> takes a special pit crew just to change the tires."*

> *"A BERT model is like a Honda Civic. It's also an engineering
> triumph, but more subtly, since it is engineered to be affordable,
> fuel-efficient, reliable."*

### The market-reality argument
Encoder-only models total >1B monthly HuggingFace downloads, nearly
3x the decoder-only total. ModernBERT serves real production work
(classification, retrieval, entity extraction) that LLMs can't match
on latency/cost.

---

## 7. Open-source model champion

### From Answer.AI FSDP+QLoRA launch
> *"everyone to be able to create their own personalized models, so
> that they are in control of their own AI systems."*

### On closed-lab capture (Latent Space)
> *"companies are sociopathic by design... the alignment problem as
> it relates to companies has not been solved."*

### Predicting OpenAI governance (pre-2023 board crisis)
> *"OpenAI's current governance structure can't continue and that it
> was definitely going to fall apart."* — Latent Space

---

## 8. Small models > scaling

Howard pushes small, fine-tuned, domain-specific models over frontier-
scale.

### From Latent Space
> *"A really underappreciated one is a BTLM 3B, which is a like kind
> of 7B quality 3B model."*

> *"You know, a 5.1.5 web [phi-1.5 web] with fine tuning for your
> task... might quite solve a lot of tasks that people have in their
> kind of day-to-day lives."*

---

## 9. Application-layer regulation (the load-bearing alternative)

Howard's consistent recommendation across SB-1047 post + Dislightenment
essay:

1. Target regulation at **applications / deployment**, not at model
   development.
2. Specifically regulate high-risk domains: healthcare, criminal
   justice, critical infrastructure.
3. Promote open-source to increase transparency.
4. Invest in government AI expertise.
5. Require disclosure when AI connects to sensitive infrastructure.
6. Mandate transparency tools (datasheets, model cards).
7. Focus on infrastructure security, not model restrictions.

---

## 10. Solveit — anti-vibe-coding (October 2025)

**Source:** https://www.answer.ai/posts/2025-10-01-solveit-full.html

### Verbatim
> *"It's easier than ever to get started, but also easier than ever
> to let AI steer you into a situation where you're overwhelmed by
> code you don't understand."*

> *"It's basically the opposite of 'vibe coding'; it's all about small
> steps, deep understanding, and deep reflection."*

> *"Our goal isn't to have AI write all our code — it's to create a
> powerful partnership between human understanding and AI
> capabilities."*

Direct contrast with Karpathy's vibe coding, Steinberger's agentic
engineering. He's not opposed to AI-assisted coding — he's opposed
to skipping the understanding.

---

## 11. "Dialog engineering" > prompt engineering

From Latent Space:
> *"I've created a new approach. It's not called prompt engineering.
> I'm creating a system for doing dialogue engineering."*

Answer.AI's Solveit is the product expression. Small-steps iterative
conversation with the model, not one-shot prompt crafting.

---

## 12. Disagreements with named figures

| Figure | Relationship |
|---|---|
| **Geoffrey Hinton** | Disagrees on x-risk. Howard co-rebutted the CAIS extinction statement Hinton signed. No personal acrimony. |
| **Dan Hendrycks / CAIS** | Hendrycks was central to SB-1047. Howard's objections directly contradict his architecture. Structural disagreement, repeated. |
| **Scott Wiener** | SB-1047 author. Howard's essay is the direct counter-frame. |
| **Yoshua Bengio** | Signed SB-1047 support. Howard opposes. No personal dispute visible. |
| **Sam Altman / OpenAI** | Repeatedly critical. OpenAI Dev Day 2023: *"an absolute embarrassment."* Predicted OpenAI's governance would fracture — before the 2023 board crisis. |
| **Andrew Ng** | Aligned on SB-1047 opposition; parallel vectors, not a joint letter. No substantive public disagreements. |
| **Yann LeCun** | Aligned on open source. LeCun: more absolutist ("LLMs are a dead end"). Howard: pragmatic ("LLMs are compressed search engines — powerful but bounded"). |
| **Rachel Thomas** | fast.ai co-founder. Still aligned, now at Answer.AI after stint at QUT. |
| **Eric Ries** | Answer.AI co-founder; alignment. |
| **Chris Lattner** | Howard is an advisor to Modular AI. Called Mojo *"the biggest programming language advance in decades."* |
| **Dario Amodei / Elon Musk** | 2026 critique on "AI will replace programmers": *"Neither of them has been a software engineer recently. The actual bottleneck was never typing code — it's design, architecture, and building things that haven't been built before."* |
| **Karpathy** | Aligned on practical ML + democratization. Different pedagogical styles (top-down vs bottom-up). Mutual respect. |
| **Willison** | Aligned on open source + ship-it ethos. Willison amplifies Howard's work. |

---

## 13. Predictions on record

| Year | Prediction | Status |
|---|---|---|
| pre-2023 | OpenAI governance will fracture | Validated (2023 board crisis) |
| 2023+ | Small fine-tuned models matter more than people think | Validating |
| 2024+ | Encoder-only models remain dominant for production NLP | Validated (ModernBERT downloads) |
| 2026 | LLMs cannot extrapolate outside training distribution | Position, not yet validatable |
| 2024 | AI regulation at model-level favors incumbents | Policy debate, ongoing |

---

## 14. His signature "no" — what he refuses to endorse

1. **AI x-risk framing as top-priority policy concern.**
2. **Frontier-model licensing / compute thresholds** as regulation
   mechanism.
3. **Credentialism** — "PhD gatekeeping" in AI education.
4. **Closed-weight dominance.**
5. **Bottom-up math-first pedagogy.**
6. **LLMs-will-replace-programmers.**
7. **LLMs as breakthrough-research engines.**
8. **"Vibe coding"** without understanding.
9. **Big-tech governance of AI ecosystems.**
10. **Regulation of model *creation*** (vs. application).

### His rhetorical move
He doesn't call safety measures "theater" (that exact phrase is
unverified). He **reframes** regulation as an incumbent-capture
mechanism. He builds the counter-tool (FSDP QLoRA, fastai, Solveit).
He lets the ethical argument land through accessible code.

---

## 15. Historical analogy repertoire

Howard reaches for historical analogies consistently:
- **Edison's 1876 Menlo Park** — Answer.AI founding frame
- **Counter-Enlightenment / de Maistre** — Dislightenment essay
- **iPhone / TCP-IP** — LLM accessibility frame (Solveit launch)
- **Faraday-to-Edison arc** — AI field's current state
- **Lead gasoline / asbestos** — regulatory irreversibility cautions

---

## 16. His recommendation engine

### Courses + tools
- **fast.ai** courses (Practical Deep Learning for Coders)
- **Computational Linear Algebra** (fast.ai)
- **Solveit** / "How to Solve It With Code"
- **fastai, fastcore, nbdev, fasthtml, claudette, cosette**
- **Mojo** (Modular AI — he's an advisor)

### Books cited
- Polya, *How to Solve It* (Solveit basis)
- Fred Brooks, *No Silver Bullet*
- Piotr Woźniak on memory/creativity

### People he consistently boosts
- Tim Dettmers (QLoRA, FSDP QLoRA)
- Sebastian Ruder (ULMFiT co-author)
- Sylvain Gugger (fastai/nbdev co-author)
- Chris Lattner (Mojo)
- DeepSeek, Qwen teams
- Daniel Han (Unsloth), Teknium (OpenHermes)
- HuggingFace bitsandbytes team
- Arvind Narayanan, Seth Lazar (x-risk rebuttal co-authors)

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 3 parallel research agents + direct WebFetch.
- Status: embodiment-grade; primary-source-verified where marked.
