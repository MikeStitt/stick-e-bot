# CLAUDE.md

<!--
The contract moved into .claude/ on 2026-09-14 so it is injected from disk on every request
instead of depending on a ritual re-read. Why, and what was measured:
.docs/2026-09-14-contract-into-claude-rules.md
-->

## Agree to follow the constitution, at every session start and every compaction

Whenever I (Claude) **start a new session** in this repository **or am compacted**, I MUST:

- **Summarize** the constitution, the parts that apply to the task at hand, and how they bear on
  what I am doing.
- **Explicitly agree** to follow them — so help me 'bot.

The agreement is not a step inside plan execution. It binds an investigation with no plan open, a
one-off fix and a conversation as much as it binds a run.

## Where the contract is

The authoritative development contract for this repository is
[`.claude/rules/constitution.md`](.claude/rules/constitution.md) (the "Constitution"). It supersedes
any conflicting guidance here — change a rule **there**, not in this file.

Everything under `.claude/rules/` is injected from disk on every request: the constitution, the
parts beside it, and the plan that [`.claude/rules/active-plan.md`](.claude/rules/active-plan.md)
imports. They are already in front of me, so there is nothing to re-read. The craft parts are skills
under `.claude/skills/`, and the constitution's Parts table says which work invokes which.
