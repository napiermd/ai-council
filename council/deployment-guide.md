# Deployment Guide

Use this when you want to deploy the AI Council inside another repository or
project workspace.

## Goal

Make the council easy to invoke from a live working repo without copying the
entire AI Council project into every workspace manually.

## Fast Install

From the `ai-council` repo:

```bash
./scripts/install.sh
ai-council doctor
ai-council list commands
```

This installs:

- `ai-council` onto `PATH` via `~/.local/bin`
- Claude commands into `~/.claude/commands/`
- Codex commands into `~/.Codex/commands/` and `~/.codex/commands/`

## Installed Slash Commands

- `/council`
- `/council-product`
- `/council-systems`
- `/council-clinical`
- `/ask-nigam`
- `/council-review`
- `/council-paper`
- `/council-pr-review`
- `/council-sqs`

## CLI Quickstart

```bash
ai-council help
ai-council doctor
ai-council list voices
ai-council list packs
ai-council list commands

ai-council prompt systems "Should this agent stack keep a planner?"
ai-council prompt clinical "Would this evaluation survive hospital deployment?"
ai-council prompt paper "What is the weak claim in this memo?"
ai-council prompt pr-review "Should this be approved?"

ai-council review docs/design.md
ai-council sqs-review docs/AI_COUNCIL_INTEGRATION.md
ai-council review --tail 80 docs/design.md
ai-council review --full docs/design.md
```

`review` and `sqs-review` inline the target file with line numbers, truncated by
`AI_COUNCIL_MAX_REVIEW_LINES` by default, or overridden with `--lines`, `--tail`,
or `--full`.

## Recommended Deployment Pattern

In the target repo:

1. Add this repo as a reference dependency, submodule, or nearby sibling repo.
2. Install the CLI and command pack with `./scripts/install.sh`.
3. In that repo's local instructions, point to the council assets you want to use.
4. Start from a session pack or review command instead of improvising the council every time.

## Smallest Viable Reference Set

If you want the smallest viable deployment, reference:

- `council/roster.md`
- `council/session-template.md`
- `council/invocation-patterns.md`
- `council/response-rubric.md`

If the work is clinical, also reference:

- `council/ask-nigam.md`

## Suggested External-Repo Instruction Snippet

```text
For strategic product, agent, or clinical AI questions, use the AI Council repo
as an external reference.

Load:
- ai-council/council/roster.md
- ai-council/council/session-template.md
- ai-council/council/invocation-patterns.md
- ai-council/council/response-rubric.md

If the question is clinical, also load:
- ai-council/council/ask-nigam.md

Load only the specific voice profiles needed for the question.
Do not activate the whole council by default.
```

## Fastest Operating Pattern

For another repo:

1. Pick a pack from `packs/`
2. Copy its prompt block
3. Fill in your decision, current direction, and constraints
4. Ask for 2-4 voices only
5. Judge the output with `response-rubric.md`

## Pack Mapping

- `packs/founder-product-pack.md`
- `packs/agent-systems-pack.md`
- `packs/clinical-ai-pack.md`
- `packs/stanford-academic-pack.md`

## What Good Deployment Looks Like

- You can invoke the council in under 60 seconds.
- The active voices are obvious.
- The answer changes the decision.
- The council feels like pressure and clarity, not performance.
