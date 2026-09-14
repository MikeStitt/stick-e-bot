# Reorganization plan — folders, and losing the sponge

Written 2026-08-11. **Executed 2026-08-12**, every step of Phase 0 through Phase 2; each is
marked **Done** below. One row of the routing table was deliberately not carried out; see the
note under that table. The reviewer pass that was Phase 3 has not been run and is now a todo in
[`README.md`](README.md); the section describing it stays here.

The phasing below was written while three agents were building in Onshape and using
`robot-guide/source/index.rst` and `.docs/build-log/`. They had landed before execution
started, so the phase order was kept for its own sake rather than to stay out of their way.

## What is wrong now

Four separate tangles, which is why this looks bigger than it is.

**1. `parts/` holds two unrelated kinds of thing.** `lesson-design.md` and `onshape.md` are
parts of the Constitution — the contract. `session-1-layout-and-torso/` is session material.
They live in one folder because the Constitution's own layout section put them there.

**2. There are two products, and the retired one owns the tooling.** `guide/` is the
SpongeBob guide: generated, not written — `model.py` builds through the API, `capture.py`
drives the GUI and records element rectangles, `annotate.py` marks up, `render_rst.py` writes
the RST from `content.py`, Sphinx builds it. Forty screenshots. It is superseded by the robot.

But `guide/` also holds `agent_browser.py`, `browser.py`, `onshape_session.py` — and
**`guide/.venv`, which every Python command in this repository invokes**, including the
commands the three running agents are using right now.

**3. A standard is filed as a working note.** `.docs/modeling-practice.md` opens with *"This is
the standard every model in this project must meet."* That is contract text sitting in the
notes folder.

**4. Two documents both claim to be Session 1.** `parts/session-1-layout-and-torso/` teaches
the layout sketch and the torso. `robot-guide/source/index.rst` teaches one-sketch-three-
features and the face. Only the first has a `lesson-design.md` partner — which is why the
second has no floor, no ceiling, no clock and no rubric. They were never missing; that half of
the document was never written.

## The target

**Nothing that gets spell-checked *automatically* lives in a hidden directory.** codespell skips
hidden directories silently, so a hidden folder and an automatic spelling gate cannot both be
true. Decided: the automatically checked content is visible, and the checker keeps its safe
default. Hidden content is checked by hand, when we decide to.

```
.parts/                    the Constitution's parts — contract, read only what you need
  lesson-design.md
  onshape.md
  modeling-practice.md     promoted out of docs; it declares itself a standard

instructions/              draft final products — what a student or a teacher is handed
  robot-guide/             source and the built site both

tools/                     the browser and API machinery, shared by everything
docs/                      background for class users — how things work, what things are
.docs/                     for the people building the class, and for agents
  experiments/             what we tried, and what it taught
    session-1-layout-and-torso/
    build-briefs/
    build-log/
    inspect/
    runs/
    reports/
    spongebob-guide/       the retired generated guide, kept as the experiment it was
```

`parts/` therefore becomes `.parts/`. It also loses `session-1-layout-and-torso/` and gains
`modeling-practice.md`, which is less work than the earlier draft of this plan proposed.

`experiments/` is **not** top level. An experiment is class-development work, so the audience
rule puts it with the developers, under `.docs/`.

### The rule that decides which folder

- **`.parts/`** — text that says how work *must* be done. Binding. Changing it changes the
  contract.
- **`instructions/`** — instructions for the people using the class: what a student follows
  while clicking, and what a teacher follows to run the session.
- **`docs/`** — background for those same people. Documents about how something works or what
  something is, in more detail than `README.md` carries. Not instructions.
- **`.docs/`** — for the people *building* the class, and for agents. Working notes: design
  decisions, findings about tools, state.
- **`.docs/experiments/`** — a thing we built to find something out. An experiment's value is its
  report; the artifact is a by-product. Includes builds that were superseded.

Applied to what exists today:

| Now | Goes to | Because |
| --- | ------- | ------- |
| `parts/lesson-design.md` | `.parts/` | contract |
| `parts/onshape.md` | `.parts/` | contract |
| `.docs/modeling-practice.md` | `.parts/` | declares itself a standard |
| `parts/session-1-layout-and-torso/` (all three files) | `.docs/experiments/` | superseded by `robot-guide/` |
| `robot-guide/test-report-1.md`, `-2.md` | `.docs/experiments/reports/` | reports |
| `robot-guide/` (the Sphinx project) | `instructions/` | the live product |
| `.docs/build-briefs/`, `build-log/`, `inspect/`, `runs/` | `.docs/experiments/` | specs and output of experiments |
| `guide/` (SpongeBob) | `.docs/experiments/spongebob-guide/` | superseded, and it *was* an experiment |
| `guide/*.py` browser and API tooling | `tools/` | shared; not part of either guide |
| `.docs/browser-access.md`, `onshape-api.md` | stays | read by whoever drives the browser or the API |
| `.docs/verification-lessons.md` | stays | read by whoever builds next |
| `.docs/taught-path.md` | `.docs/experiments/` | a draft click path, never walked by a human |
| `.docs/project.md`, `robot-build-plan.md` | stays; `docs/` gets a new page written from them | the originals are development state |
| `.docs/session-state.md` | delete | the agents have landed; it was a handoff before a clear |

**The `session-state.md` row was not carried out.** Looking at the file before deleting it,
which the Constitution requires, showed it is the **only** registry of the robot's Onshape
document ids and named versions — `ball-socket-run2`, `hinge-run2`, `lesson-run2` and their
published version ids. `project.md` holds the sponge's ids, not the robot's. The row's reason
justifies dropping the handoff framing, not the registry, so the file stays until the ids have
somewhere else to live.

## Losing the sponge

**Scope it to the contract and the notes. Do not rewrite the retired guide.**

Of roughly sixty occurrences across seventeen files, about forty-five are inside `guide/`
itself — `content.py` alone holds twenty-five. That guide *is* about SpongeBob. Rewriting it
into a robot would be work with no reader, since it is being retired. It moves to
`.docs/experiments/spongebob-guide/` with a header saying it is superseded and why, and its text
stays as it is.

That leaves a small, real job:

| File | Hits | What changes |
| ---- | ---- | ------------ |
| `constitution.md` | 4 | title, opening paragraph, the trademark note, the version footer |
| `README.md` | 5 | course-at-a-glance framing |
| `.docs/project.md` | 4 | "What we're building" |
| `.docs/README.md` | 4 | state-of-play prose, and the summary paragraph |
| `.docs/robot-build-plan.md` | 2 | passing references |
| `.docs/taught-path.md`, `verification-lessons.md`, `modeling-practice.md` | 1 each | passing references |

The trademark paragraph in `constitution.md` **goes away entirely** rather than being
reworded. An original robot action figure carries no rights-holder problem, so the rule it
exists to enforce has nothing left to enforce. Losing it is the point, not a side effect.

## Traps

**`guide/.venv` is load-bearing.** Every documented command in this repo is
`guide/.venv/bin/python`. Moving it invalidates commands in `.docs/browser-access.md`, both
READMEs, `robot-guide/Makefile`, and the instructions the three running agents are following.
It moves last, in its own commit, with every reference fixed in that same commit.

**`parts/` in `guide/model.py` is not our folder.** Two hits there are Onshape API URL paths
(`/parts/d/{did}/w/{wid}/...`). A blind find-and-replace across the repo breaks the API client.

**Link-fixing is the bulk of the work, not the moves.** `parts/` is referenced by path in
`constitution.md` (6), `README.md` (3), `.docs/README.md` (2), `.docs/project.md` (1),
`CLAUDE.md` (1), `robot-guide/README.md` (1). Each move needs its references fixed in the same
commit, or the Constitution points at files that are not there.

**`.docs/` is not renamed, but most of it still moves.** Decision 3 keeps the folder hidden, so
the 75 references to `.docs/` do not all have to be rewritten. What moves is what goes down into
`.docs/experiments/`: 1008 of the 1019 tracked files under `.docs/` — 584 in `build-log/`, 397
in `runs/`, 25 in `inspect/`, 2 in `build-briefs/`. That is a Phase 1 move, not a Phase 0 one,
because it breaks two things that are not files:

- the **cron watchdog** (job `8ae3fefe`) hardcodes `.docs/build-log/*/` in its prompt, and must
  be recreated against the new path in the same breath as the move;
- the agents' own instructions name `.docs/build-log/<dir>/` and `.docs/build-briefs/`, so the
  move has to wait until they have landed their reports.

Nine tracked files spell one of the moving paths literally — one outside `.docs/` and four
inside for `build-log/`, two inside for `build-briefs/`, one either side for `taught-path.md`.
Relative references from inside `.docs/` do not carry the prefix and were not counted, so that
is a floor rather than the total.

## Tooling

Three additions. Everything in this section was **run, not read about**; the numbers are
measurements.

### uv

**`uv 0.9.21` is already installed** at `~/.local/bin/uv`, with `uvx`. Python is 3.14.3.
Nothing needs installing to start.

What the repo has today is `guide/requirements.txt` — four unpinned lines (`playwright>=1.44`,
`pillow>=10.3`, `sphinx>=7.3`, `sphinx-rtd-theme>=2.0`) and a hand-made `guide/.venv`. There is
no `pyproject.toml` and no lock file, so the environment is not reproducible: a rebuild next
month resolves different versions.

The switch:

1. `pyproject.toml` at the repo root with those four dependencies, plus a dev group holding
   `codespell` and `textstat`.
2. `uv lock` to pin them, and commit `uv.lock`.
3. `uv sync` creates `.venv` at the root, replacing `guide/.venv`.
4. Every documented command changes from `guide/.venv/bin/python …` to `uv run python …`.

**Trap: `uv sync` does not install the browser.** Playwright's Chromium is a separate binary
fetched by `playwright install chromium`. A fresh clone that runs only `uv sync` gets a working
import and a failing browser — which looks like a login problem and is not. It goes in the
README as a second, explicit step.

**This is the most disruptive change in the plan and it comes last.** `guide/.venv/bin/python`
appears in both READMEs, `.docs/browser-access.md`, `robot-guide/Makefile`, and in the
instructions the three running agents are executing right now.

### codespell — the spell checker

`uvx codespell` needs no install. It carries a **builtin `en-GB_to_en-US` dictionary**, which
is exactly the British-spelling ban rather than a generic typo pass:

```sh
uvx codespell --builtin en-GB_to_en-US <files>
```

Measured against the live files:

| File | Findings |
| ---- | -------- |
| `.docs/robot-build-plan.md` | 36 |
| `robot-guide/source/index.rst` | 24 |
| `robot-guide/make_plans.py` | 19 |
| `parts/session-1-layout-and-torso/onshape-steps.md` | 9 |
| the two plan `.svg` files | 6 |
| four other files | 13 |

**Two gaps found by testing it, both of which would have caused silent false all-clears:**

1. **codespell skips hidden directories.** Passing `.docs` as a directory returns **0**
   findings; passing `.docs/*.md` by glob returns **54**. The default invocation would report
   the repo clean while missing the largest working document in it.

   **Resolved by naming the hidden files, not by working around the tool.** The folders are
   sorted by audience (Decision 3), so `.parts/` and `.docs/` stay hidden and the check target
   passes `.parts/*.md` and `constitution.md` by name. Everywhere else the checker keeps
   codespell's default behavior, which is what correctly excludes `.git/`, `.claude/` and
   `.idea/`. `.docs/` is checked by hand, on demand.
2. **codespell does not know the compounds.** The simple forms it does know are listed here
   — `centre`, `colour`, `modelled`, `metres` <!-- codespell:ignore -->
   — but the compound built on the first of them passes clean, and it appears
   **23 times** across the checked files, mostly naming the vertical axis a student is told to
   click. Fixed by a project dictionary (`-D`), now `tools/dictionary.txt`.

**Quoting a banned word is legitimate, and the checker cannot tell.** This document has to name
the words it bans; the guide has to quote UI labels verbatim. Both forms of
`codespell:ignore` on the offending line work — tested — and the HTML-comment form is the one
to use in Markdown because it disappears when rendered:

```markdown
It knows centre, colour and modelled.  <!-- codespell:ignore -->
```

A real mistake on a line without the marker is still caught, so this suppresses a line rather
than a word. Use it sparingly and only for quotation.

### textstat — reading level

No spell or prose tool was installed system-wide (`codespell`, `aspell`, `hunspell` and `vale`
are all absent), so `uv run --with textstat` is the zero-setup option and it works today.

Whole-file scores for `robot-guide/source/index.rst`, RST markup stripped:

| Measure | Value |
| ------- | ----- |
| Flesch-Kincaid grade | **4.4** |
| Flesch reading ease | 84.5 |
| Gunning fog | 6.9 |

**The whole-file number is not the useful output.** Grade 4.4 says the document is easy, and it
mostly is — but the average hides the paragraphs that are not. Scoring paragraph by paragraph
finds them:

| Grade | Paragraph |
| ----- | --------- |
| 12.0 | "The side faces are the honest check now: the front faces have had the panel…" |
| 10.1 | "A Center point rectangle placed on the origin is held there by the origin itself…" |
| 9.0 | "You are going to draw one sketch, from the front, containing three rectangles…" |
| 8.6 | "To deselect, click an empty patch of background…" |

The grade-10.1 paragraph is the one the earlier review flagged independently, for a different
reason — it explains why the course never uses **Fix** without saying what goes wrong if you
do. Two methods landing on the same paragraph is worth more than either alone.

So the check reports **the worst paragraphs, not the average**, with a threshold. Grade 8 is a
sensible ceiling for a middle-school reader; anything above it is a paragraph to look at, not
an automatic failure — a long list of short verbatim UI labels can score high and read fine.

**Reporting a score is not the deliverable.** A grade number tells nobody which words to change.
So the reading level is handled the same way as the reviewer pass below: **Claude reads the
paragraphs above the threshold and proposes rewrites as a diff**, one commit's worth of
recommendations at a time, for the user to accept or reject per hunk. The script's job is to say
which paragraphs; the rewriting is a reading task and lands as reviewable changes.

### Where the checks live

A **`check` target**, run as one command, covering the three mechanical gates:

- prose wrapped at 100 columns, tables exempt (already a gate, currently checked by hand)
- codespell with the en-GB dictionary, plus the project dictionary for the compounds it does
  not know, over the visible folders **and** an explicit `.parts/*.md` and `constitution.md`
- textstat per paragraph, listing anything above grade 8 for the rewrite pass above

The runner is **ninja**, matching the sibling repo the user already runs `ninja check` in; `make`
would serve equally and neither is installed here yet. `uvx` needs no install, so the target
works in Phase 0 and keeps working after the Phase 2 uv migration.

## Reviewer pass — tone, and judgments about people

A reading pass, not a script. **Fable** reads the repository's prose and flags three things.

**1. Unprofessional statements.** Snark, in-jokes, dismissiveness — anything that would not
survive being read aloud to the class, or to a parent.

**2. Judgments based on age.** Text that sorts people by age and then uses the sorting to
decide something. The line that prompted this, removed from this plan's own folder rule:

> If a fourteen-year-old is not the reader, it does not belong here.

That used an age to decide where a file goes. Also in scope: `constitution.md`'s *"the account a
fourteen-year-old will be signed into"*, and the same move made with grade level.

**3. Judgments based on status.** The same move made with standing rather than age — seniority,
credentials, prior tool experience, or whether someone counts as a beginner.

**What is flagged** — an age, grade, or standing substituting for a capability, an audience, or
a permission.

**What is not** — naming who is actually in the room. "Students range from middle-schoolers who
have never opened a CAD tool to high-schoolers with some Fusion behind them" reports the roster.
"A fourteen-year-old would not follow this" judges a person by their age. The first is a fact
about the class; the second is a guess about a reader.

Scope: the repository's prose — `constitution.md`, `.parts/`, `instructions/`, `docs/`, `.docs/`
and both READMEs.

**What it produces.** Every file is committed first, so Fable's changes land as a clean diff
against a known state instead of mixing into the move commits. Fable then edits in the working
tree — the diff is the proposal — and writes `.docs/<YYYY-MM-DD>-professional-review-report.md`
recording what it changed and why.

**Nothing Fable writes is adopted by writing it.** The user reads the diff and takes it hunk by
hunk, keeping what is right and reverting what is not. The report is what explains a hunk when
the change alone does not.

## Phases

Sequenced so nothing touches a path a running agent is using.

**Phase 0 — safe now, while the agents run.** Touches nothing they read or write.

1. **Done.** `git mv parts .parts`, then `git mv .docs/modeling-practice.md .parts/`. Fix all
   references in the same commit.
2. **Done.** De-sponge `constitution.md`, `README.md`, `CLAUDE.md` and the `.docs/*.md` files.
   Delete the trademark paragraph.
3. **Done.** Update the Constitution's *Parts* section and its per-session layout to describe
   the new folders.
3a. **Done.** Copy `book-em-danno/.specify/memory/parts/constitution-maintenance.md` to
   `.parts/constitution-maintenance.md` verbatim (Decision 4), then make only the changes it
   needs to work here. Do it in this phase, before the later phases start amending the
   Constitution. Seven things in the copy do not fit as written:

   - it says `parts/` throughout, which here is `.parts/`;
   - its "never duplicate it into the agent-doc pointers" list names `CLAUDE.md`, `AGENTS.md`
     and `.github/copilot-instructions.md`; this repo has only `CLAUDE.md`;
   - it opens *"Read together with the constitution's Governance section"* and step 2 says
     *"Apply the semantic rule from Governance"* — this Constitution has no Governance section.
     Step 3b adds one, so both references resolve;
   - its step 2 updates a `**Last amended**` field; ours reads `**Adapted**`;
   - its step 5 cites a *Configuration is code* rule we do not have. The equivalent here is
     Working Rule 8 and *Verification is evidence* — a check target is amended once it has been
     run, not once it has been edited;
   - the Changelog is `book-em-danno`'s own history and does not transfer. Ours opens at the
     current **2.0.0 (2026-08-09)**;
   - *See also* points at `shared.md` and a `git-cliff` source-code changelog, neither of which
     exists here.

3b. **Done.** Bring `book-em-danno`'s **Governance** section into `constitution.md`, since the
   part copied in 3a is written as an expansion of it. It goes last, after *Parts*, and the
   version footer moves under it — the same place it sits in the source. Four changes:

   - the compliance bullet reads *"all pull requests and code reviews MUST verify adherence to
     these principles"*. This repo pushes only when asked and does not require PRs, so the
     obligation attaches to the work, not to a PR: adherence is verified before a change is
     called done.
   - the amendment bullet points at `parts/constitution-maintenance.md`; here `.parts/`.
   - the footer gains a **Last amended** field, which 3a's step 2 updates. Keep **Adapted** and
     **Source** — they record where this Constitution came from, which is a different fact.
   - the *Parts* table gains a row: *Amending the Constitution itself* →
     `.parts/constitution-maintenance.md`. And the always-read-core sentence near the top, which
     lists "the Working Rules below plus the Quality Gates and Branch Policy", names Governance
     too.
4. **Done.** Add the spelling and reading-level gates to the Quality Gates table, and write the
   check script with its project dictionary. `uvx` needs no install, so the script works before
   the uv migration and keeps working after it. Landed as three scripts behind one
   `ninja check`; the wrap gate, previously checked by hand, was scripted with them.
5. **Done.** Run the sweep on everything **except** `robot-guide/source/index.rst`, which the
   lesson test is reading. 118 British spellings across the repository.

**Phase 1 — once the three agents have landed their reports.**

6. **Done, in step 5's sweep.** Sweep `robot-guide/source/index.rst`, and `make_plans.py` —
   including the six strings that are **drawn on the plan sheets**, which means re-rendering
   both PNGs. The agents had landed, so holding `index.rst` back bought nothing; it needed no
   corrections, `make_plans.py` needed 22, and both PNGs were re-rendered and read back.
7. **Done.** Create `.docs/experiments/` and `instructions/`. Move
   `parts/session-1-layout-and-torso/` in (Decision 1), the two test reports into
   `.docs/experiments/reports/`, and `build-briefs/`, `build-log/`, `inspect/`, `runs/` down
   from `.docs/` into it. Fix the `.docs/build-log/` references in the agents' instructions in
   the same commit.
8. **Done.** Move `robot-guide/` — source and built site both (Decision 2) — to `instructions/`,
   fixing its `Makefile` and `README.md`.
9. **Done.** Write the missing `lesson-design.md` for the robot session — clock, floor, ceiling,
   rubric — which is the gap the review found. Check it against the reading-level threshold as
   it is written, rather than afterwards. It records the clock as **unmet**: 92 minutes at agent
   pace, and student pace unmeasured.
9a. **Done.** Create `docs/` and write its first page, from `.docs/project.md` and the
   curriculum-coverage half of `.docs/robot-build-plan.md`. Those two stay where they are; this
   is a rewrite for a different reader, not a move. Same reading-level check as it is written.

**Phase 2 — deliberate, and on its own.** The riskiest phase; nothing else should be in flight.

10. **Done.** Add `pyproject.toml` and `uv.lock`; `uv sync` a root `.venv`.
11. **Done.** Extract `tools/` from `guide/`, and fix **every** command reference in both
    READMEs, `.docs/browser-access.md` and `robot-guide/Makefile` — `guide/.venv/bin/python`
    becomes `uv run python`. Document `playwright install chromium` as its own step.
12. **Done.** Delete `guide/requirements.txt` and `guide/.venv`, only after a fresh `uv sync`
    has been shown to drive the browser. A fresh Chromium 151.0.7922.34 was launched and driven
    before either was removed.
13. **Done.** Move `guide/` to `.docs/experiments/spongebob-guide/` with a superseded header.

The reviewer pass that was Phase 3 is now a todo in [`README.md`](README.md), since it is a
reading pass over the repository rather than a step of this reorganization. What it looks for
is above, under *Reviewer pass — tone, and judgments about people*.

## Decisions taken

**1. Which document is Session 1? — `robot-guide/source/index.rst`.** It supersedes
`parts/session-1-layout-and-torso/`, which was written on 2026-08-10 and replaced the same day
by the commit *"Rewrite session 1 to start from a design plan, and build it as a Sphinx page"*.
The older folder has had one test run and no edits since; the Sphinx page has had two runs and
sixteen commits. It goes to `.docs/experiments/`. The parts of it that have no counterpart in
the new session — the teaching half, construction geometry, two warnings, the drag test — are
listed in [`README.md`](README.md) under *Carry the useful half of the old Session 1 into the
new one*, to be carried across before it is retired.

**2. Does `instructions/` hold the RST source, or the built site as well? — both.** A teacher
who is handed `instructions/` gets something they can read without running Sphinx.

**3. Hidden or visible folders — decided by audience, not by the checker.** `.parts/` and
`.docs/` are hidden because of who reads them; `docs/` and `instructions/` are visible for the
same reason. codespell skips hidden directories, so the check target names `.parts/*.md` and
`constitution.md` explicitly — see *Where the checks live*.

**4. How the Constitution gets amended — adopt the sibling repo's part, do not write a new
one.** `.parts/` gains `constitution-maintenance.md`, **copied verbatim** from
`book-em-danno/.specify/memory/parts/constitution-maintenance.md` and changed only where it
does not fit this repo. It carries the five-step amendment checklist, semantic versioning for
the version footer, and a dated changelog entry per amendment giving the rationale. That part is
written as an expansion of a **Governance** section, so `constitution.md` takes that section
from the same source. Today there is no rule for changing the rules.
