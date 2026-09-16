# Moving the contract into `.claude/` — 2026-09-14

The constitution and its parts reach context today by ritual, and the ritual does not reliably
fire. This plan moves them to where Claude Code injects them from disk on every request, so the
contract and the active plan are present whether or not anybody remembers to read them. It changes
no rule in the constitution except where the move itself requires one.

## The problem

[`../CLAUDE.md`](../CLAUDE.md) tells Claude to re-read
[`../.claude/rules/constitution.md`](../.claude/rules/constitution.md) and the relevant parts at
every session start and every compaction. Across draft9p4 that ritual came due about 35 times. The
active plan was not read.

A file re-read after a compaction comes back as a bare path once it passes roughly 5,000 tokens.
The draft9p4 plan is 10,342 tokens. So the one document the run could not proceed without was the
one most certain to be missing.

`CLAUDE.md` and `.claude/rules/*.md` are injected from disk at request time instead. They are not
subject to the re-read limit, and they do not depend on a ritual.

## The agreement is not part of any plan

Following the constitution is not a step inside plan execution. It binds the work: an investigation
with no plan open, a one-off fix, a conversation. So the agreement stays in `CLAUDE.md`, at the
repository root, ahead of anything about plans, and it is asked for at every session start and every
compaction whether or not a plan is active.

What drops out of the ritual is only the re-read. Re-reading `constitution.md` in full was a
workaround for the file not being in context. Once it is injected on every request the re-read is
redundant; agreeing to it is not.

[`../.claude/rules/parts/plan-activation.md`](../.claude/rules/parts/plan-activation.md) says how a
plan becomes active and how it stops being active, and nothing else. The contract applies either
way.

## What is proven

- **A rules file and its `@` import both arrive after a compaction, at plan size.** Tested
  2026-09-14. A 52-token `.claude/rules/active-plan.md` importing a 10,342-token `plan.md` returned
  the whole plan, with sentinels at lines 1, 204 and 408 all present. The sentinel values were
  generated without being printed, so quoting them is evidence of injection rather than recall.
- **`@` imports nest, at least three deep.** Tested 2026-09-14.
  `.claude/rules/nest-probe.md` imported `nest-a.md`, which imported `nest-b.md`, which imported
  `nest-c.md`. The three imported files sit in `.claude/probe/`, outside the rules tree, so they
  could arrive no other way. All three sentinels came back, each as its own block of injected
  instructions, and all three matched the answer key. So a plan can pull in its own parts, and a
  part can pull in another.
- **A broken `@` import is silent.** In the same window `.claude/rules/active-plan.md` arrived with
  its `@../../plan.md` line unexpanded, because the test copy had been deleted. No error, no
  placeholder, nothing in the injected text to distinguish it from a file that has no import. A
  pointer at a moved or renamed plan fails exactly this way.
- **`.claude/rules/` loads recursively.** The documentation states that all `.md` files under it
  "are discovered recursively", and that rules without `paths:` load "with the same priority as
  `.claude/CLAUDE.md`". Confirmed in the project tree on 2026-09-14: a fifth sentinel in
  `.claude/rules/subdir-probe/depth-probe.md` arrived with no `paths:` frontmatter and nothing
  pointing at it. So nothing placed under `.claude/rules/` can be kept out of context.
- **A project `CLAUDE.md` may live at `./CLAUDE.md` or `./.claude/CLAUDE.md`.** The two are
  equivalent, so the choice is about who finds the file rather than what it does.
- **Skills are the documented mechanism for material that should not always load.** "For
  task-specific instructions that don't need to be in context all the time, use skills instead,
  which only load when you invoke them or when Claude determines they're relevant to your prompt."
- **A skill's body loads on invocation and is re-injected after a compaction.** Observed once in the
  2026-09-14 session: `artifact-design` was invoked before a boundary and its body was present
  afterward. One data point, not a guarantee.
- **`ninja check` follows the files.** `check_wrap.py` and `check_spelling.py` build their lists
  from `git ls-files -- '*.md'`, and that pathspec reaches into `.claude/`; verified against the
  untracked `.claude/rules/active-plan.md`. Neither tool needs changing.
- **`check_reading_level.py` never covered the contract.** Its globs are `instructions/**/*.rst`,
  `instructions/**/*.md` and `docs/*.md`. `.parts/` was never in scope, and its `lesson-design.md`
  exclusion is for the instructor's file under `instructions/`. The move does not touch it.

### `paths:` frontmatter does gate loading, and still does not help here

[anthropics/claude-code#25005](https://github.com/anthropics/claude-code/issues/25005) reports that
`paths:` scopes where a rule applies rather than whether it loads. The documentation says the
opposite: path-scoped rules "only load into context when Claude works with matching files". The
issue is from February and was closed as a duplicate of
[#16352](https://github.com/anthropics/claude-code/issues/16352), which was closed stale in March;
the documentation page was updated 2026-09-10. The documentation is the authority.

`paths:` is still not usable in this repository, for a different reason: a path-scoped rule triggers
when Claude reads a matching file with the `Read` tool, and `cat` does not trigger it. Auto mode
prefers Bash, so the trigger would fire only sometimes. Skills do not have this problem, because
invoking one is an explicit act rather than a side effect of how a file was opened.

## What is not proven

- **Whether an invoked skill body survives more than one compaction.** One observation only.
- **Whether injection improves adherence.** The documentation targets under 200 lines per
  `CLAUDE.md` and warns that longer files "reduce adherence"; `constitution.md` is 261 lines.
  Injection guarantees presence, not obedience. This is a reason to keep the constitution lean
  rather than to let it absorb the parts.

## What it costs

Counted with the Haiku 4.5 counter. Treat the absolute figures as approximate and the ratios as the
point; an earlier count of `constitution.md` with a different model's counter gave 5,572.

| File | Tokens |
| ---- | -----: |
| `CLAUDE.md` | 209 |
| `constitution.md` | 4,191 |
| `.parts/onshape.md` | 4,662 |
| `.parts/constitution-maintenance.md` | 3,668 |
| `.parts/prose-style.md` | 1,162 |
| `.parts/modeling-practice.md` | 1,060 |
| `.parts/lesson-design.md` | 520 |
| `.claude/rules/active-plan.md` | 42 |
| Contract total | 15,514 |

Three layouts, by what lands in every request:

| Layout | Always on |
| ------ | --------: |
| All five parts as rules files | 15,514 |
| Four as rules, `constitution-maintenance.md` outside the rules tree | 11,846 |
| Four as skills, `prose-style.md` stays a rule | about 5,950 |

The third is the one chosen. Its figure is `CLAUDE.md`, the constitution, `prose-style.md`, a new
`plan-activation.md` of about 250 tokens, and four skill descriptions at roughly 35 tokens each. Add
the active plan at 10,342 and it comes to about 16,300 tokens per request, which is 5.4 percent of a
300,000-token window. There are no user-level rules on this machine, so the project's contract is
the whole always-on load, plus about 1,100 tokens of `MEMORY.md`.

## The layout

| From | To | Why |
| ---- | -- | --- |
| `CLAUDE.md` | unchanged, at the root | the agreement, where a person finds it |
| `constitution.md` | `.claude/rules/constitution.md` | always applies |
| `.parts/prose-style.md` | `.claude/rules/parts/prose-style.md` | applies to writing anything at all |
| new | `.claude/rules/parts/plan-activation.md` | how a plan is made active and unmade |
| `.claude/rules/active-plan.md` | unchanged | one `@` import naming the active plan |
| `.parts/onshape.md` | `.claude/skills/onshape/SKILL.md` | invoked before the first modeling step |
| `.parts/modeling-practice.md` | `.claude/skills/modeling-practice/SKILL.md` | invoked with the same trigger |
| `.parts/lesson-design.md` | `.claude/skills/lesson-design/SKILL.md` | invoked when writing a session plan |
| `.parts/constitution-maintenance.md` | `.claude/skills/constitution-maintenance/SKILL.md` | invoked before amending the contract |

`prose-style.md` stays a rules file because its trigger is writing anything at all. A thing that
always applies should not sit behind a decision to load it.

`CLAUDE.md` stays at the root rather than moving to `.claude/CLAUDE.md`. The two locations behave
identically, and the constitution is moving into a hidden directory; a root `CLAUDE.md` is the one
agent-facing file a person finds by opening the repository without knowing the convention.

## Settled decisions

- **Four parts become skills, and `prose-style.md` stays a rules file.** Settled 2026-09-14 by Mike.
- **The 25 archival references are left alone.** Settled 2026-09-14 by Mike. One sentence in the
  Archive section says that paths in archived records point at where files lived when written.
- **The agreement stays in `CLAUDE.md` and is not conditional on a plan.** Settled 2026-09-14 by
  Mike.

## Steps

- **A. Test whether `@` imports nest, and whether project rules recurse.** Done 2026-09-14. A chain
  of three imports starting outside the rules tree, plus a rule one directory down, plus a control
  in the top-level rules file so a missing sentinel could be attributed to the import rather than to
  the rules file: five sentinels, generated by a script that printed nothing, keyed to the
  scratchpad at mode 0600. One compaction returned all five, and all five matched the key. Both
  questions are answered under *What is proven*, and the five probe files are deleted.

- **B. Move the files.** `git mv` throughout, so `git log --follow` still answers. The four skills
  each become a directory holding `SKILL.md` with `name` and `description` frontmatter; the
  description is what decides whether the skill is invoked, so it is written with the same care as
  the part.

- **C. Rewrite the contract's internal links.** `constitution.md` carries 16 path references and the
  parts cross-reference each other 18 more times. The constitution's links to a part become
  `parts/...` or a skill name; the parts' links back become `../constitution.md`.

- **D. Write `.claude/rules/parts/plan-activation.md`.** It says:

  - Point `.claude/rules/active-plan.md` at the plan before doing any of its work. The file holds
    one `@` import naming the plan and nothing else. This is the first step of executing a plan,
    ahead of any reading or building.
  - Exactly one plan is active. Pointing at a new plan replaces the pointer; it does not add to it.
  - A plan stops being active only when Mike and Claude agree it has. Finishing the last step is not
    deactivation; saying so is.
  - On deactivation the file is emptied. An emptied pointer is the record that nothing is active; a
    stale pointer silently reintroduces finished work after every compaction.
  - Why it is a rules file: it is injected from disk on every request, so it survives compaction and
    is not subject to the roughly 5,000-token limit that turns a re-read file into a bare path.

  It says nothing about the constitution. The contract applies whether or not a plan is active.

- **E. Amend the constitution.** Four edits, plus the version bump and changelog entry that the
  `constitution-maintenance` skill requires:

  - The Parts table gains a column for how each part is reached, naming the skill to invoke and the
    work that triggers it.
  - The folder-by-reader table replaces the `.parts/` row with `.claude/rules/` and
    `.claude/skills/`.
  - Governance's link to the amendment workflow moves to the skill.
  - A new Working Rule requires the active-plan pointer when a plan is being executed. It does not
    make the contract conditional on a plan existing.

- **F. Rewrite `CLAUDE.md`.** It stays at the root and keeps the agreement, which comes first in the
  file so it cannot read as a step inside a larger procedure. It points at
  `.claude/rules/constitution.md`, says that the contract loads automatically, and asks for the
  agreement at every session start and every compaction whether or not a plan is active. The
  instruction to re-read the constitution in full is removed; the summarize-and-agree is kept. Block
  level HTML comments are stripped before injection, so any note for a human maintainer can go in
  one and costs no tokens.

- **G. Fix the 40 live references and leave the 25 archival ones.** Run records under
  `.docs/experiments/runs/` and `instructions/robot-guide` 1 to 3 record what was true when they
  were written, and the constitution keeps the archive read-only. One sentence in the Archive
  section says that paths in archived records point at where files lived when written.

  The active draft9p4 plan lives under `.docs/experiments/runs/` and is live, not archival. Its
  three references are read on every request once `active-plan.md` imports it, so a stale path there
  is the most visible one in the repository:

  - `plan.md:32`, the `gates` row, pointing at `../../../../constitution.md`
  - `plan.md:211`, Phase P's step to amend `../../../../.parts/onshape.md` § *Rename features*
  - `plan.md:397`, the last open question, citing `constitution.md` § *Where developmental draft
    products live*

- **H. Keep the rest of `.claude/` out of git.** `.claude/settings.local.json` and
  `.claude/scheduled_tasks.lock` are local. A `.gitignore` entry ignores `.claude/*` and re-includes
  `.claude/rules/` and `.claude/skills/`.

- **I. Prove it.** `ninja check` clean, a sweep finding no dead links, and
  `git ls-files -- '*.md' | grep '^\.claude/'` listing every moved file.

- **J. Point the pointer at the real plan and commit.** `.claude/rules/active-plan.md` imports
  `.docs/experiments/runs/2026-09-08-draft9p4/plan.md`; the root `plan.md` test copy is deleted. On
  a branch off `main`, staging explicit paths.

- **K. Verify.** Run `/context` and read the *Memory files* list, which names what actually loaded;
  that is cheaper than a compaction and catches a file that silently did not load. Then force one
  compaction and confirm the contract, the plan and the skill descriptions all arrive. Until that
  compaction the move is unproven, and this file says so.

## What this costs

- **Loading becomes a judgment for anything behind a skill.** That is the failure mode this plan
  exists to fix, and putting four parts behind skill descriptions reintroduces a weaker form of it.
  Two things make it stronger than the ritual it replaces: the requirement to invoke lives in the
  constitution, which is injected on every request and cannot fall out of context; and an
  invocation is a tool call in the transcript, so `grep` answers whether it happened. Nothing in the
  log today says whether `.parts/onshape.md` was read. If that is not enough, a `PreToolUse` hook
  can refuse the first Onshape call until the skill has been invoked.
- **The contract moves into a hidden directory.** A person opening the repository no longer finds
  `constitution.md` at the root. `CLAUDE.md` and `README.md` both have to carry them there.
- **A skill's description becomes load-bearing prose.** Whether a part reaches context depends on
  how well one line matches the work at hand.

## What happened, 2026-09-14

Every step is done on the branch `rework-constitution`. Step K ran last, because it needed a
compaction only Mike can force.

- **The files moved with `git mv`**, so `git log --follow` still answers. `.parts/` no longer
  exists.
- **Each skill carries `name` and `description` frontmatter.** The description is a quoted YAML
  scalar wrapped across lines, the shape an official plugin skill uses, so it obeys the 100-column
  rule without inventing a second wrapping convention for frontmatter.
- **The constitution is at 5.1.0.** The Parts table gained a column for how each part arrives and
  the obligation to invoke a skill before the work it governs begins; the folder-by-reader table
  names `.claude/rules/` and `.claude/skills/`; the Archive section says archived paths point at
  where files lived when written; Governance points at the skill. The changelog entry with the
  rationale is in the `constitution-maintenance` skill.
- **The `@` mentions in the constitution became backticked paths.** `@` is an import token in a
  rules file, and `@instructions/stickbot-draftMpN` is not a file.
- **34 dead links to the old paths remain in archived records**, across 24 files, which is what
  *Settled decisions* chose.
- **`ninja check` exits 0**, watched. Wrap and spelling are clean. The reading-level list is the
  same 200 paragraphs it was before, none of them in the contract.
- **`.claude/rules/active-plan.md` imports the draft9p4 plan**, and the import resolves.
- **The always-on load measures 14,275 tokens**, counted after the move on the same Haiku 4.5
  counter as the table above: `CLAUDE.md` 377, the constitution 4,443, `prose-style.md` 1,162,
  `plan-activation.md` 375, the pointer 31, and the draft9p4 plan it imports 7,887. The plan's
  10,342 came from a different counter, which is why the estimate above reads higher. The four
  skill descriptions add about 200 tokens more.
- **Two dead links in `.docs/onshape-gui-howto.md` predate this work** — `runs/2026-08-11-run1/` at
  line 11 and `build-log/` at line 13. They are not about the move and were left alone.

### What Step K's compaction proved

- **All six blocks arrived after the compaction**: `CLAUDE.md`, the constitution, `prose-style.md`,
  `plan-activation.md`, `active-plan.md`, and the draft9p4 plan through the import. No re-read, and
  nothing for the summary to carry. That is the whole point of the move, and it holds.
- **A skill directory added mid-session does not register until `/reload-skills`.** `/skill` listed
  none of the four, and the `Skill` tool answered `Unknown skill: lesson-design`, because the
  registry is built when the session starts and the directories were made after. The reload added
  all four. Restarting Claude Code would do the same.
- **The multi-line quoted description parses.** After the reload each skill's description arrived
  whole, reflowed onto one line, so the frontmatter shape does not have to fight the 100-column
  rule.
- **HTML comments in `CLAUDE.md` are stripped from the injected text.** The comment at the top of
  the file, pointing at this document, is on disk and is not in what arrives. It serves a person
  opening the file; it reaches no session. Anything a session needs to know belongs in the
  contract, not in a comment.
