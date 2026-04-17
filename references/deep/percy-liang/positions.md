# Positions: Percy Liang

> Strong public positions, disagreements, predictions. Each item
> sourced to a verifiable tweet, paper, interview, or regulatory
> comment.

---

## His signature line — "Open-source AND safety, not either / or"

**Source:** Air Street Press interview, Marin launch blog,
consistent across talks.

> *"Not only is there no trade-off between openness and safety, but
> openness is essential for safety."*

This is the load-bearing claim of his public identity. It is a
direct rebuttal to the Anthropic / closed-lab thesis that weight
release is net-negative for safety.

---

## Position 1: Holistic evaluation > narrow benchmarks

**Source:** HELM paper (TMLR 2023), GenAI Summit talk.

> *"The pace of innovation is happening so quickly that we're not
> able to measure."*

HELM is the institutional embodiment: 7 metrics (accuracy,
calibration, robustness, fairness, bias, toxicity, efficiency)
across 42 scenarios.

On saturation (MedHELM):
> *"The relatively high scores of the top models indicate potential
> saturation, which motivates the need for more difficult
> benchmarks."*

**When he invokes it:** Any single-number-benchmark claim. Any
"SOTA on MMLU" framing. Any vendor comparison.

---

## Position 2: "Nutrition labels" for foundation models

**Source:** Multiple interviews, FMTI framing.

> *"We need a nutrition label or a spec sheet for these objects
> that we're selling or people are buying and using."*

**FMTI (Foundation Model Transparency Index):** 100 transparency
indicators. **2025 edition shows average score FELL from 58 to 40
year-over-year.** IBM top (95), xAI bottom (14).

**His argument:** Without a regulatory floor, transparency
regresses. The data is now empirical, not hypothetical.

---

## Position 3: Open-weight ≠ open-source

**Source:** Air Street Press interview; repeatedly across talks.

> *"Models like Llama 3, Mixtral are 'open-weight models', not
> 'open-source models'."*

The distinction matters:
- Open-weight = weights released; training data, code, failures
  not released
- Open-source = reproducible end-to-end; training data, code, and
  ideally failures are public

> *"There's lots of crucial information we're missing and without
> the training data, you risk catastrophic forgetting if you
> fine-tune."*

**Marin** operationalizes his open-source definition: preregistered
experiments, public failures, GitHub-contributable research.

---

## Position 4: Current evaluation is fundamentally broken

**Source:** Multiple HELM-related talks and papers.

> *"Current model evaluation is fundamentally broken."*

His evidence: only 9 of 30 major LMs disclosed sufficient test-
train overlap info in the HELM audit. Most benchmark scores are
self-reported by the models' own builders on curated scenarios.

**His fix:** HELM as a public-goods evaluation infrastructure.
AutoBencher (ICLR 2025) auto-generates 22%-harder datasets to
defeat saturation.

---

## Position 5: Third-party evaluation is non-negotiable

**Source:** ICML 2025 position paper, *"Position: In-House
Evaluation Is Not Enough. Towards Robust Third-Party Evaluation and
Flaw Disclosure for General-Purpose AI"* (arXiv 2503.16861).

> *"Legally protected third-party evaluation and coordinated flaw
> disclosure are essential to safe AI systems."*

**His proposal:** Bug-bounty-style flaw disclosure with legal safe
harbors for researchers. Red-teamers cannot be held liable for
honest disclosure.

---

## Position 6: "Foundation models" as a distinct paradigm

**Source:** Bommasani/Liang et al. 2021 paper — the act of coining
the term itself.

Verbatim definition from the paper:
> *"Models trained on broad data at scale such that they can be
> adapted to a wide range of downstream tasks."*

The framing "ignited debate" — some researchers argued the term was
premature or marketing-y. Liang defended the framing as a distinct
technology category requiring dedicated study. **Five years in,
the term has stuck across academia, industry, and policy.**

---

## Position 7: Academic labs must retain hands-on LM-building capability

**Source:** CS336 ("Language Models from Scratch") framing; June 18,
2025 tweet.

> *"Researchers are becoming detached from the technical details of
> how LMs work. In CS336, we try to fix that by having students
> build everything."*

**Why it matters:** If academia outsources LM-building to industry,
academia loses the ability to critique industry. Liang's teaching
is the operational response.

---

## Position 8: SB 1047 / California AI bills — evidence-based regulation

**Source:** Co-author of *"A Path for Science- and Evidence-based
AI Policy"* (Stanford Law, 2024).

His stance on SB 1047: existing evidence does not support the
premise of compute-threshold-based liability. Open foundation
models' **marginal** risk is what matters, not worst-case
speculation.

**He is not a "pause" signatory.** He signs evidence-based
regulatory proposals with colleagues; does not issue solo
polemics.

---

## Position 9: NIST / AISI engagement — open release must stay

**Source:** CRFM + RegLab response to US AISI draft guidelines on
dual-use foundation model misuse risk.

His asks of AISI:
1. Strengthen reproducible + third-party evaluation guidance
2. Clarify post-deployment monitoring
3. Extend guidance across the full supply chain
4. *"Ensure the continued open release of foundation models
   absent evidence of marginal risk."*

The last point is load-bearing: **the default should be open; the
burden is on the regulator to show marginal risk.**

---

## Position 10: Scaling-law preregistration as scientific practice

**Source:** Marin, February 2026 tweet (status 2034367256277533100).

> *"In Marin, we are trying to get really good at scaling laws. We
> have trained models up to 1e22 FLOPs and have made a prediction
> of the loss at 1e23 FLOPs, which @WilliamBarrHeld is running.
> This prediction is preregistered on GitHub, so we'll see in a
> few days how accurate our prediction is…"*

**Why it matters:** Preregistered, falsifiable, public predictions
are the normative scientific bar. He is applying it to
frontier-scale AI research, which almost no lab does. A category-
defining move for research culture.

---

## Position 11: The FMTI trajectory is the data

**Source:** FMTI 2025, 3rd edition. arXiv 2512.10169.

**Average transparency score:**
- 2023: 37/100 (Meta top at 54)
- 2024: 58
- 2025: **40**

**The year-over-year decline is his evidence** that the industry is
regressing on transparency, not progressing. He uses the data
itself as the argument.

---

## Position 12: Open-source can keep pace (Marin 32B proof)

**Source:** Marin launch; October 29, 2025 tweet (status
1983561556127567911).

> *"Marin 32B Base (mantis) is done training! It is the best
> open-source base model (beating OLMo 2 32B Base) and it's even
> close to the best comparably-sized open-weight base models,
> Gemma 3 27B PT and Qwen 2.5 32B Base."*

**The empirical bet:** fully-open development can keep pace with
open-weight frontier. Each Marin milestone cashes or fails that
bet publicly.

---

## Disagreements / debates

### Against Anthropic (structural, not personal)
Anthropic never open-sources weights; FMTI places them below
open-weight competitors on transparency indicators. The public
disagreement: Anthropic's "safety requires closed" thesis vs.
Liang's "openness is essential for safety."

### Against closed-lab benchmark self-reporting
The third-party-evaluation paper is the formal institutional
response. He does not name-and-shame; he builds the alternative.

### Against static-benchmark culture
HELM Classic → HELM Lite → AutoBencher is a standing critique
cashed quarterly.

### Against "safety-as-closed" framing (Dario Amodei posture)
> *"Not only is there no trade-off between openness and safety,
> but openness is essential for safety."*

This is his most load-bearing public disagreement. Not framed as a
personal fight — framed as a policy principle.

### Productive tension with Karpathy / Howard
Liang wants rigor; they want to ship. **Cooperative not
adversarial:** Karpathy is a Simile AI individual backer alongside
Liang.

---

## Predictions / bets

1. **Scaling-law preregistration (Feb 2026):** explicit loss
   prediction at 1e23 FLOPs, on GitHub. Falsifiable.
2. **Open-source catches up:** Marin 32B beats OLMo 2; implicit
   prediction that fully-open matches open-weight frontier within
   a generation.
3. **Benchmark half-life ~2 years:** HELM Classic → Lite →
   AutoBencher is dated evidence. Each release is a data point.
4. **FMTI will fall further without regulation:** 58 → 40 trend
   will continue absent a floor.
5. **Third-party evaluation becomes required infrastructure:**
   In-house evaluation is structurally insufficient; legal safe
   harbor for red-teamers becomes necessary.
6. **No trade-off between openness and safety:** as open models
   proliferate, catastrophic misuse should NOT scale
   proportionally. Testable claim he stakes public credibility on.
7. **Foundation-model framing (2021–):** the term stuck; the
   category is now load-bearing across academia, industry, policy.
   Bet cashing.

---

## Signature refusals

Things he has been asked about but has not publicly endorsed:

- **"AI pause" petitions.** Not a signatory.
- **Compute-threshold-based liability regimes.** Opposed on
  evidence grounds.
- **"Safety requires closed models."** Explicitly rebutted.
- **Vendor-curated benchmark claims.** Counterexample work is
  HELM.
- **"Foundation models are just bigger models."** The term was
  chosen to mark a category distinction.
- **AGI timelines / superintelligence framings.** Not his
  register; he measures what exists.

---

## Last reviewed

- Reviewed: 2026-04-17
- Source pass: 1 research agent (positions / X / recent window) +
  primary-source verification against CRFM blog, HELM, FMTI
  papers, Marin tweets.
- Status: embodiment-grade — verbatim positions with sources.
