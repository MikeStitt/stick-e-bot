# Task definitions into the repository

The repository cites task numbers 107 times and defines none of them. The definitions live in the
Claude Code task store, which is keyed by session id and is not in git. This file says what was
measured, what moves into the repository, and what stops the references going dangling again.

## What was measured, 2026-09-16

| | |
| --- | ---: |
| References to a task number, in tracked files | 107 |
| Distinct numbers referenced | 31 |
| Files holding at least one reference | 42 |
| Records in the task store, numbered 25 to 217 | 193 |
| Description text held only in the store | 72 KB |

- **The store is `~/.claude/tasks/<session-id>/NNN.json`**, one file per task, holding `id`,
  `subject`, `description`, `activeForm`, `status`, `blocks` and `blockedBy`. Every one of the 193
  records has a description, the longest 1,842 characters, and 40 records carry a dependency.
- **It is keyed by session, not by repository.** Only `c7e95b50-...` exists, and that session's
  working directory is the archive. The `stick-e-bot` session `c8ce147b-...` has no task directory
  at all, so every number in this repository resolved to nothing for it.
- **Two references are already dangling.** `.docs/build/plan/12-gripper.md:118` and
  `.docs/build/plan/14-assembly-legs.md:96` both write `[task #29](../../robot-build-plan.md)`, and
  `robot-build-plan.md` does not contain the word *task*.
- **The 193 records stand at 177 completed, 15 pending and one in progress.**

### Finding a reference takes a careful pattern

A naive `#\d+` returns 287 matches and 180 of them are not tasks.

- **HTML entities.** `&#216;` is the diameter sign, `&#176;` is degrees, `&#215;` is a multiply
  sign, `&#177;` is plus-or-minus, `&#183;` is a middle dot and `&#178;` is a superscript two.
  These are most of the noise, and they are dense in `make_plans.py`, the hinge review and the
  explanatory sketches.
- **CSS colors.** `#111;` and `#555;` in `src/stickbot/agent_browser.py` and run1's `capture.js`.
- **Intra-document references.** run3's `hand/build-notes.md` writes *see #4 below*, and
  head-collar's `shots/steps.log` writes *input #7 reads '1 mm'* and *Neck socket #0*. Thirteen
  mentions across two archived files, none of them a task.

What survives is `(?<![&0-9A-Za-z_#])#(\d{1,3})(?![0-9A-Za-z_;])`, with numbers below 25 dropped:
the store starts at 25 and nothing below it is a task.

## Where the references are

| Where | Mentions | Numbers | Files |
| ----- | -------: | ------: | ----: |
| Live, `.docs/` outside `experiments/` | 25 | 19 | 7 |
| Archived, under `.docs/experiments/` | 82 | 22 | 35 |

| Live file | Mentions |
| --------- | -------: |
| `.docs/2026-09-13-draft9p4-state.md` | 15 |
| `.docs/reviews/hinge/changes.md` | 3 |
| `.docs/build/plan/04-ball-and-socket.md` | 2 |
| `.docs/build/plan/06-torso-joints.md` | 2 |
| `.docs/build/plan/00-manifest.md` | 1 |
| `.docs/build/plan/12-gripper.md` | 1 |
| `.docs/build/plan/14-assembly-legs.md` | 1 |

- **Thirteen of the 31 referenced numbers are still open**: #27, #29, #60, #129, #139, #177, #203,
  #204, #208, #209, #214, #215 and #216.
- **Eighteen are closed** and are cited as history: #26, #28, #56, #58, #59, #118, #119, #122,
  #125, #138, #140, #141, #142, #158, #168, #169, #184 and #213.
- **Three open tasks are cited by nothing**: #205, #206 and #207, tutorials 11, 12 and 13.

## Two jobs, not one

A closed task and an open one need different homes, and the repository has already ruled on one of
them.

- **An open task belongs in the plan that will do it.** draft9p4's plan says so in Phase P, *fold
  tasks #118, #119, #125 and #169 into the files they fall in, so they are steps rather than a list
  somebody has to remember*, and task #188 recorded it done. This plan applies that ruling to the
  open numbers rather than building a second tracker beside it.
- **A closed task needs somewhere to resolve.** `2026-08-29-draft9p3/notes.md:2002` ends a
  paragraph with *Task #125.* and nothing else. That sentence says nothing unless #125 is written
  down somewhere, and folding a finished task into a plan does not give it that.

## Phase 1 - export the ledger, done 2026-09-16

`.docs/tasks.md` holds every number from 25 to 217: the subject, the status, the description, and
the `blocks` and `blockedBy` links where there are any. One entry per number, written once from the
store.

- **All 193, not the 31 that are cited.** A ledger holding only what is currently referenced has to
  be re-derived every time somebody writes a new citation, and the gate below would then reject a
  legitimate reference to a number that was simply never quoted before. Exporting everything is one
  mechanical pass and it never needs repeating. The cost is about 90 KB in a 27 MB repository.
- **The exporter is a throwaway.** It reads the store and writes the file, and it runs once. The
  Constitution's probe-script exception covers it, so it lives in the session scratchpad rather
  than in `src/stickbot/`. It graduates only if the answer to the open question below is that the
  store stays upstream of the repository.
- **Two gates will run over the new file the moment it is tracked.** `check_wrap.py` builds its
  list from `git ls-files -- '*.md'` and skips only three `.docs/experiments/` prefixes, so the
  exporter wraps every description at 100 columns. `check_spelling.py` will read 72 KB of prose
  that has never been through it, and a British spelling found there is fixed in the export rather
  than in the store.
- **The ledger records status as it stood at export.** It says what each number meant; whether it
  is ever updated again is the open question below.

## Phase 2 - make the live references resolve, done 2026-09-16

- **Fix the two dangling links.** `12-gripper.md` and `14-assembly-legs.md` point `[task #29]` at
  `robot-build-plan.md`, which does not define it. They point at `.docs/tasks.md` instead.
- **Give `.docs/2026-09-13-draft9p4-state.md` its own words.** Lines 201 to 208 are the whole *what
  is left* section and they are written as bare numbers; the carried six, #27, #29, #60, #129,
  #139 and #177, carry no description at all. Each line gains the sentence that says what the work
  is, the way lines 172 and 173 already do.
- **Fold the sixteen open tasks into the plans that own them.** Thirteen are cited and three, #205,
  #206 and #207, are cited by nothing. Phases 4 and 5 of
  [`2026-09-14-move-to-stick-e-bot.md`](2026-09-14-move-to-stick-e-bot.md) are where most of them
  land. Each open number is either written into a plan as a step or recorded as dropped.

## Phase 3 - say where the rule lives, done 2026-09-16

A Working Rule, not a sentence beside the Quality Gates: *Name a unit of work; do not number it*
carries both halves, the naming convention and where a cited number resolves. Constitution 5.9.0,
with its changelog entry in the `constitution-maintenance` skill. No config companion, so
maintenance step 5 has nothing to exercise; `ninja check` was run and watched green on all five.

## Settled by Mike, 2026-09-16

- **Stop coining numbered tasks.** The ledger closes at #217 and is pure history. A new finding is
  written into the plan that will act on it, which is what draft9p4's Phase P had already ruled for
  open work.
- **A unit of work carries a dotted identifier name**, in the style the plans already use for steps
  and requirements: `task.foot.sole_groove` beside `audit.page` and `cad.parts.body.block`.
- **No gate.** The proposed `stickbot-check-tasks` is dropped. It would check that every cited
  number resolves, and with the numbers closed the set it checks cannot grow, so the defect it
  guards against has no way to recur.

## What this does not do

- **It does not renumber anything.** The 107 existing references stay as they are written.
- **It does not rewrite the archived records.** Their `#125` keeps meaning what it meant, and
  `.docs/tasks.md` is what says so.
- **It does not recover tasks 1 to 24.** The store starts at 25, and nothing in the repository
  cites a number below it.
