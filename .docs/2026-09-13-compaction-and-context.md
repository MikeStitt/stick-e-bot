# Compaction and what survives it — 2026-09-13

Written after the draft9p4 audit found that the *Steps reproduce* gate had stopped being checked
part way through the run. The question behind this file is why a rule the repository states plainly
stopped being followed, and what would make it stick. The answer turned out to be mostly about
compaction, so this records what compaction does, what it measured out at, and what Mike decided
to do about it. The run-side findings are in
[`2026-09-13-draft9p4-state.md`](2026-09-13-draft9p4-state.md).

## What we counted

The session transcript is
`~/.claude/projects/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-….jsonl`, 199,251 lines
going back to 2026-08-12. Every compaction writes a `compact_boundary` record into it, so the
counts below are read off that file, not estimated.

**288 compactions in the session. 35 of them since draft9p4 began.**

| Since | Compactions |
| ----- | ----------- |
| draft9p4 first named, 2026-09-08 23:19 | 35 |
| "please complete the steps in the draft9p4 plan", 2026-09-09 16:09 | 32 |
| "execute the draft9p4 plan", 2026-09-11 15:05 | 28 |
| the same, re-issued 2026-09-12 13:27 | 26 |
| "This time really keep going", 2026-09-13 01:36 | 15 |

By day that is 4, 4, 0, 5, 11 and 15. The run got busier and the boundaries got closer together.

A single boundary record, from 2026-09-13 13:12, carries the shape of the event:

```
trigger: auto     preTokens: 269229     postTokens: 15147
durationMs: 152648     cumulativeDroppedTokens: 72411527
preservedMessages: 5 uuids
```

So 269,229 tokens went in, 15,147 came out, five raw messages were kept, and the summarizing call
itself took 153 seconds. Across the session, 72,411,527 tokens have been dropped this way.

## The ritual did not fire

`CLAUDE.md` asks for a re-read of `constitution.md` and the relevant `.parts/` files at every
session start and every compaction, then a summary and an explicit re-agreement. Scanning the tool
calls in the opening turns after each of the 35 boundaries:

| What was read in the opening turns | Count |
| ---------------------------------- | ----- |
| `constitution.md` | 2 of 35 |
| the run's `plan.md` | 2 of 35 |
| both together | 1 of 35 |
| an explicit re-agreement written out | 1 of 35 |
| a `.docs/build/plan/*.md` tutorial sheet | 19 of 35 |

Widening the window to any point before the next boundary only reaches 13 of 35 for each of
`constitution.md` and `plan.md`, and those are mostly mid-window reads answering a specific
question rather than the ritual.

The pattern is consistent: pick up the task list, open the tutorial's build sheet, resume CADing.
The file that says what to build was read most windows. The two files that say how the work is
proved were not. The one full ritual, at 2026-09-13 07:13, read `constitution.md`, the `.parts/`
files and `08-foot.md`, and still did not read the run's `plan.md`, which is where the
*Steps reproduce* gate is defined.

`CLAUDE.md` was injected automatically at all 35 boundaries. The pointer was present every time.

## What is in context after a compaction

Confirmed against the Claude Code documentation and against the transcript.

| Mechanism | After compaction |
| --------- | ---------------- |
| System prompt and output style | still apply |
| Project-root `CLAUDE.md`, and `.claude/rules/*.md` with no `paths:` | re-injected from disk |
| Auto memory `MEMORY.md` | re-injected from disk |
| A plan written in plan mode | re-injected from disk |
| Rules with `paths:` frontmatter | reload only when a matching file is read |
| Nested `CLAUDE.md` in a subdirectory | reloads only when a file in that directory is read |
| Files read or edited | up to five re-read, most recently modified first |
| Skill bodies that were invoked | re-injected, 5,000 tokens each, 25,000 in total |
| Context a hook added earlier | summarized away with everything else |
| `SessionStart` hooks matching `compact` | run, and their output added |

Everything else is the summary, which arrives as one long user message; this session's was 25,001
characters.

**The five-file re-read has a size limit, and it is the finding that matters most here.** A file
over about 5,000 tokens comes back as a bare path with no content, labeled `Referenced file`. The
boundary we inspected shows it directly:

- `08-foot.md`, 4,613 tokens, came back as **full text**
- `09-hinge.md`, 7,004 tokens, came back as a **path only**
- `notes.md`, 23,056 tokens, came back as a **path only**
- `foot.rst`, large, came back as a **path only**

So the observed threshold sits between 4,613 and 7,004 tokens, which matches the documented figure
of about 5,000.

Two files that govern the work are in neither column. `constitution.md` is not re-injected, because
only `CLAUDE.md` is, and `CLAUDE.md` is a thin pointer whose content is an instruction to go read
the constitution. The run's `plan.md` is not re-injected either, and at 10,291 tokens it could not
come back whole through the file re-read even if it won one of the five slots.

## How big the files actually are

Measured with `messages.count_tokens` on `claude-opus-5`, which is Claude's own tokenizer. It runs
**1.42 times** `cl100k_base` on this prose, so any estimate made with `tiktoken` is about 40 percent
low.

| File | Claude tokens | Over 4,500 |
| ---- | ------------: | ---------- |
| `experiments/runs/2026-09-08-draft9p4/notes.md` | 23,056 | yes |
| `experiments/runs/2026-09-08-draft9p4/plan.md` | 10,291 | yes |
| `build/plan/06-torso-joints.md` | 7,894 | yes |
| `build/plan/09-hinge.md` | 7,004 | yes |
| `build/plan/04-ball-and-socket.md` | 6,996 | yes |
| `.parts/onshape.md` | 6,046 | yes |
| `build/plan/02-head.md` | 5,758 | yes |
| `constitution.md` | 5,572 | yes |
| `.parts/constitution-maintenance.md` | 4,835 | yes |
| `build/plan/08-foot.md` | 4,613 | yes |
| `build/plan/00-manifest.md` | 3,645 | no |
| `build/plan/01-torso.md` | 3,346 | no |
| `build/plan/05-head-socket.md` | 3,013 | no |
| `build/plan/12-gripper.md` | 2,826 | no |
| `build/plan/10-u-limb.md` | 2,657 | no |
| `build/plan/03-assembly-first-parts.md` | 2,401 | no |
| `build/plan/07-assembly-head.md` | 2,300 | no |
| `build/plan/14-assembly-legs.md` | 1,845 | no |
| `build/plan/13-assembly-arms.md` | 1,810 | no |
| `build/plan/11-l-limb.md` | 1,757 | no |
| `.parts/prose-style.md` | 1,563 | no |
| `.parts/modeling-practice.md` | 1,461 | no |
| `.parts/lesson-design.md` | 688 | no |
| `CLAUDE.md` | 275 | no |

Ten of the 23 documents are over 4,500 tokens. The constitution is one of them.

## What compaction frequency is and is not driven by

`autoCompactWindow` in `~/.claude/settings.json` is set to `300000`. Opus 5 on the Anthropic API
has a 1,000,000 token window, and the tuned default compacts at about 967,000 tokens. So the run
has been compacting at roughly 31 percent of what the model can hold, which is the direct cause of
the 35 boundaries. `/autocompact` accepts 100K to 1M.

Shrinking documents will not change this. One full window, the 2026-09-13 12:13 to 13:12 segment,
breaks down as:

```
tool_use inputs     25,531 tokens
tool results        32,068
user text            8,933   (mostly the 216-row task list, injected 3 times)
images               4,400   (only 4 images)
assistant text         325
                    ------
measured            71,257  of about 254,000 of growth
```

The gap is thinking blocks, whose text the transcript does not retain, plus the resent system
prompt and tool schemas. What the measurement does settle is the ranking: tool calls and their
results dominate, and documents are a minority share of one of those. `plan.md` at 10,291 tokens is
about 4 percent of a window fill. Trimming every plan document to 4,500 tokens would not move the
compaction rate in a way anyone could detect.

The two levers do different jobs:

- the **window size** decides how often a boundary is crossed
- the **document size** decides whether a given file can come back across one at all

Neither decides whether a gate gets checked. That is the delivery mechanism.

## Where Mike landed

These are Mike's decisions, recorded here so the work that follows has something to point at.

**Move the constitution and the `.parts/` files into `CLAUDE.md` and `.claude/rules/**`.** Both of
those load at session start and are re-injected from disk after every compaction, with no read
required and no five-slot lottery. The documented size limit on that path is 4 MiB per file, not
5,000 tokens, so the 5,572 token constitution comes back whole. Cost: these are resident from the
first turn of every session, not only after a boundary. Constitution plus all five parts is 20,165
tokens, which is 6.8 percent of a 300,000 token window and 2 percent of a 900,000 one.

**Audit plans against the 5,000 token limit.** A ceiling of 4,500 Claude tokens sits just under the
largest file we have watched survive the re-read, 4,613 tokens, and well under the smallest we have
watched fail, 7,004. A check that measures every plan and part against it, and names what is over,
is the same shape as the other `ninja check` sweeps. Measuring with `tiktoken` is not good enough;
the 1.42 ratio means a file that looks like 4,000 tokens is really 5,700.

**The Bash preference stays, and the plan fix does not touch it.** The auto mode guidance to read
with `cat` and `head` rather than the Read tool has been in force for months, and Mike reports the
run got better when it went in. It also has a cost this file did not anticipate: the Read tool loads
a nested `CLAUDE.md` and `cat` does not, tested here on 2026-09-14, so tool choice decides whether
directory-scoped instructions arrive at all. Weighing one measured session against months of
observed performance is not a fair trade, and no apples-to-apples test is available from a
transcript. So the preference stands. What follows from it is narrow: a plan that loads only when a
directory is opened with the Read tool is not a route this repository can use, and the two routes
that do not care which tool is used, an unscoped file in `.claude/rules/` and a `SessionStart` hook,
are the ones to build on.

**Force the run's `plan.md` into context.** The idea on the table is a `CLAUDE.md` placed in the
directory tree that is executing the plan, so the run folder carries its own instructions.

## What is still open about forcing the plan in

Three routes, and they are not equally strong. Recording the differences so the choice is made with
them in view.

- **A nested `CLAUDE.md` in the run folder.** It loads when a file in that directory is read, and
  after a compaction it reloads on the same condition. That is weaker than the root file, which
  reloads unconditionally. In practice the run writes its logs into that folder constantly, so it
  would reload early in most windows; but the windows where it would not are exactly the ones the
  audit found, where the run folder was never opened. Worth knowing before choosing it.
- **An unscoped file in `.claude/rules/`.** Re-injected unconditionally, same as root `CLAUDE.md`.
  The strongest of the three. The cost is that it is resident in every session in every part of the
  repository, including work that has nothing to do with the run.
- **An `@path` import in the root `CLAUDE.md`.** One line per run, pointing at the live plan, which
  keeps the plan where it lives now. Imports are expanded at launch. Whether that expansion also
  happens on the post-compaction re-injection is **not documented and has not been tested here**,
  so it is an assumption, not a fact.

Either way `plan.md` at 10,291 tokens is too big to be the resident copy. The part that has to be
present is the gate table, the document roles and the phase list; the rest is reference that can be
read when needed. That is a split of about 120 lines out of 401.

**A cheap test settles the untested parts.** Put a file over 5,000 tokens in `.claude/rules/` with a
distinctive sentinel line at its end, and after the next compaction check whether the sentinel is in
context. The same trick with an `@path` import answers the import question. One boundary answers
both.

## What none of this fixes

Everything above is about making a rule present. None of it makes a rule enforced. The documentation
is direct on the point: `CLAUDE.md` and rules are delivered as context, not as configuration, and
adherence is not guaranteed. The audit bears that out; the pointer was present at all 35 boundaries
and was followed at two.

The mechanism that does not depend on judgment is a hook. A `PreToolUse`, `TaskCompleted` or `Stop`
hook runs as a shell command and can refuse. For this run the check is one grep: a tutorial does not
close until a log exists naming the reproduction document. That test would have failed on tutorials
4, 5, 6 and 8 on the day each was written.

The other hook worth having is `SessionStart` with the `compact` matcher, whose standard output goes
straight into the compacted context. Unlike `CLAUDE.md` and rules, it can carry things that change:
which gates are unproved right now, which tutorial is in flight, what the last log says. Static
contract in rules, live state from the hook.

Nothing in this file has been configured. No hook exists, no rule file exists, and the current
`autoCompactWindow` is still 300000.
