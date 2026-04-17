# Source Index

This file is the quick audit surface for the council.

Use it to answer:

- which profiles are fully source-backed
- when each voice was last reviewed
- which first-party sources anchor each profile
- which voices also have generated recent-signal files

## Core voices

| Voice | Status | Reviewed | Sources | Key publications |
| --- | --- | --- | --- | --- |
| Andrej Karpathy | fully source-backed | 2026-04-14 | karpathy.ai, bearblog, GitHub, X | Software 2.0, Animals vs Ghosts, Verifiability, autoresearch |
| Chip Huyen | fully source-backed | 2026-04-14 | huyenchip.com, O'Reilly, X | AI Engineering book, Common Pitfalls, Agents, Distribution Shifts |
| Jeremy Howard | fully source-backed | 2026-04-14 | Answer.AI, fast.ai, X, GitHub | ULMFiT, ModernBERT, SB-1047 opposition |
| Pete Steinberger | fully source-backed | 2026-04-14 | steipete.me, GitHub, X, Lex Fridman | Just Talk To It, Claude Code Is My Computer. Joined OpenAI Feb 2026 |
| Simon Willison | hand-authored, needs-refresh | 2026-04-17 | simonwillison.net, GitHub, X, `llm` CLI | Datasette, `llm` CLI, "prompt injection" coinage, annotated model releases |
| Nigam Shah | fully source-backed | 2026-04-14 | Stanford Medicine, Shah Lab, Google Scholar, CHAI | MedHELM, Recurring Local Validation, FURM, Delivery Science |
| Jonathan H. Chen | fully source-backed | 2026-04-14 | Stanford Profiles, HealthRex Lab, X, LinkedIn | MedAgentBrief, MedAgentBench, GPT-4 physician RCT, NOHARM |
| Danielle Bitterman | fully source-backed | 2026-04-14 | bittermanlab.org, AIM Harvard, X | TRIPOD-LLM, Clinical-Grade Evaluation, hallucination severity data |
| Douwe Kiela | fully source-backed | 2026-04-14 | contextual.ai, X, Google Scholar | Original RAG paper, RAG 2.0, GLM |

## Specialist extensions

| Voice | Status | Reviewed | Sources | Key publications |
| --- | --- | --- | --- | --- |
| Fei-Fei Li | fully source-backed | 2026-04-14 | Stanford HAI, World Labs, X, Substack | Nature 2020 (ambient intelligence), HAI "Humans in Charge", CA Frontier AI Report |
| Harrison Chase | fully source-backed | 2026-04-14 | blog.langchain.com, X, GitHub | Context engineering, Your Harness Your Memory, Ambient Agents, Deep Agents |
| Percy Liang | fully source-backed | 2026-04-14 | CRFM, HELM, X, Google Scholar | HELM, MedHELM, FMTI, AutoBencher, Marin |
| Ethan Mollick | hand-authored, needs-refresh | 2026-04-17 | oneusefulthing.org, Wharton, X, Co-Intelligence book | Co-Intelligence (2024), Navigating the Jagged Technological Frontier (HBS/BCG) |
| Aidan Gomez | hand-authored, needs-refresh | 2026-04-17 | cohere.com, X, LinkedIn, "Attention Is All You Need" | Transformer paper (2017), Command/Embed/Rerank, Cohere for AI, North agent platform |
| Bob Wachter | hand-authored, needs-refresh | 2026-04-17 | UCSF Profile, X, book | The Digital Doctor (2015), NEJM "hospitalist" (1996), Understanding Patient Safety |

## Archived voices

These voices were removed from the active council on 2026-04-17. Reference
profiles remain in `references/` for historical context.

| Voice | Status | Last active | Reason archived |
| --- | --- | --- | --- |
| Yann LeCun | fully source-backed | 2026-04-14 | Predictable LLM-skeptic contrarianism; JEPA work has not shipped consumer product |
| Chris Olah | fully source-backed | 2026-04-14 | Mechanistic interpretability rarely load-bearing at current product stage |
| Jan Leike | fully source-backed | 2026-04-14 | Alignment-science lens mostly abstract at current council scope |
| Demis Hassabis | fully source-backed | 2026-04-14 | Frontier-strategy lens operates on decade horizons; limited actionability |

## Grounding protocol

All profiles updated 2026-04-14 follow the [grounding protocol](grounding-protocol.md):
- Each voice includes sourced publications with URLs
- Quotable positions are attributed to specific works
- Sourced evidence is separated from persona inference

## Notes

- `fully source-backed` means the profile includes explicit publications, sourced quotes, and current-signal distillation from first-party and official sources.
- If a profile is older than 90 days, refresh it before relying on `Current signals`.
