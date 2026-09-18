---
name: constitution-maintenance
description:
  "The amendment workflow for the contract, and the dated changelog. Read before changing
  .claude/rules/constitution.md, any file under .claude/rules/parts/, or any of these skills."
---

# Constitution — Maintenance part

Read this part **only** when you are amending the constitution itself
(`.claude/rules/constitution.md` or any file under `.claude/rules/parts/`). It
records the maintenance plan — how amendments are made and versioned — and holds
the full **Changelog** moved out of the always-read core so that core stays lean.
Read together with the [constitution](../../rules/constitution.md)'s Governance
section.

**Amendments**: any change to this constitution MUST be documented with a version
bump and rationale.

**Versioning**: semantic. MAJOR — principle removals or incompatible
redefinitions. MINOR — new principles or material expansions. PATCH — wording
clarifications and typo fixes.

## Maintenance plan

Amending the constitution is itself governed work; treat the rules below as the
checklist for any change to `constitution.md` or a part.

- **Propose the words and get agreement before editing.** Show the exact text being removed and the
  exact text replacing it, and wait for user agreement. An amendment is the user's
  decision; drafting it is not the same as making it.
- **Edit the right home.** Behavioral rules and the always-read core live in
  `.claude/rules/constitution.md`; per-work-type detail lives in
  `.claude/rules/parts/` and in the skills. Change a rule in exactly one place —
  never duplicate it into the agent-doc pointer (`CLAUDE.md`), which says so
  itself.
- **The Constitution states rules, not why.** Cut the argument for a rule; keep the rule.
  Researching or defending a rule's rationale is a separate task, done when
  asked. Applies to everything in `.claude/**`, except the [Changelog](#changelog) below.
  Permission to describe the **why*** in other documents does not grant
  permission `.claude/**`.
- **Bump the version.** Apply the semantic rule from Governance: MAJOR for
  principle removals or incompatible redefinitions, MINOR for new principles or
  material expansions, PATCH for wording clarifications and typo fixes. Update
  the `**Version**` and `**Last amended**` line in `constitution.md`.
- **Record it in the changelog.** Add a dated entry to the
  [Changelog](#changelog) below — newest first — stating what changed and
  _why_. The rationale is the valuable part; a bare "updated X" is not enough.
- **Update companions in the same commit.** If the change has an on-disk
  companion (e.g. the `check` target, its dictionary, or a hook that enforces
  the rule), change it in the same commit so the documented rule and its
  enforcement never drift apart.
- **Exercise config companions, don't just edit them** (Working Rule 8, and
  _Verification is evidence, not assertion_). A rule whose enforcement lives in
  config is only amended once the config has been _run_ and shown to behave as
  intended — editing the file is not verification. Run the `check` target and
  watch it catch what the new rule is meant to catch.

## Changelog

- **8.0.0 (2026-09-18)** — MAJOR: `parts/prose-style.md` gains **Turn a 'why' into a 'when'**, and
  stops permitting a reason in a rule's body.

  The body rule read *"Write the body only for what the title cannot carry — the reason the rule is
  not obvious, the exception, the symptom"* and now reads *"…, perhaps: the unobvious,
  clarifications, exceptions, or symptoms. Use good judgment. Shorter and tighter is better."* The
  new rule reads *"Turn a 'why' into a 'when'. A reason narrows a rule to the case that produced
  it; a scope does not. Where the why cannot be turned, track the need and ask the user, at the
  next opportunity, to agree it is needed."*

  Incompatible redefinition, so MAJOR: a rule body carrying its own reason was permitted by name
  and is now forbidden.

  _Why:_ a reason attached to a rule reads as the rule's scope, so the rule is taken to apply in
  the case that produced it and not elsewhere. Turning the why into a when says the same thing
  without the narrowing. The prohibition already existed in
  [`../../../memory/instructions-state-facts-not-importance.md`](../../../memory/instructions-state-facts-not-importance.md)
  — *"The Constitution states rules, not why"*, written 2026-08-12 — and the contract had been
  contradicting it since, which is how 7.0.0 came to carry an argument inside a rule.

  _Where the why still lives._ This changelog, by the carve-out the maintenance plan above now
  states. It is not injected on every request, so a reason kept here costs no context.

  _Companion changes, same commit._ The maintenance plan gains **The Constitution states rules, not
  why**, so the prohibition is in the checklist a writer reads rather than only in a memory.

  _Config companion, exercised._ `check_spelling.py` caught the en-GB spelling of *judgment* in the
  new text and it was corrected; `ninja check` green on all five, watched.

- **7.0.0 (2026-09-18)** — MAJOR: Branch Policy stops requiring a named version. It read
  *"Material that depends on a reference document MUST cite a named version, not the live
  workspace — a workspace moves under the class"* and now reads *"Cite a document by name and id,
  and then a workspace or a named version as the material needs. A cited workspace is not moved.
  That is a project policy and material may rely on it."*

  Incompatible redefinition, so MAJOR by the reading 5.0.0 and 6.0.0 used: material citing a
  workspace was failing this rule and now passes.

  _Why:_ Mike's ruling. The old rule read as though a workspace were unsafe in a way a git branch is
  not, and it is not — a repository can be moved or deleted exactly as a workspace can, and projects
  cite them anyway, because a project runs on an assumed order. Stating that cited workspaces are
  not moved is that order written down.

  It also cleared up a confusion of mine. An Onshape **named version** is a semantic name — `V1`,
  `F done - Phase F proved` — not a hash, so the old rule never asked for the thing I had described.

  _A requirement I invented, and Mike removed._ My first draft of this amendment added *"Cite a
  named version where the reader is outside that order: anything a student starts from, and any
  claim that has to stay checkable after the workspace has moved on."* Mike did not ask for it and
  did not agree to it; I wrote it into the Constitution and mentioned it afterwards. It is wrong on
  the facts as well: students will not start from a workspace and will not need documents to CAD,
  and if that ever changes the instructions and any example workspace are kept in sync rather than
  asking a student to track versions. It is gone, and the rule carries no carve-out.

  My draft also put the git-and-branches argument inside the rule, which
  [`../../../memory/instructions-state-facts-not-importance.md`](../../../memory/instructions-state-facts-not-importance.md)
  forbids: *the Constitution states rules, not why*. Mike cut it. The maintenance plan above now
  carries that rule, and a step requiring the words be proposed and agreed before they are written.

  _Companion changes, same commit._ The `onshape` skill's Discipline bullet *"Cite named versions,
  never live workspaces"* becomes *"Cite a workspace where the project's order holds, a named
  version where it does not"*, and the cross-reference further up that file follows. The skill's
  instruction to publish a named version before writing a run's report is untouched: that is a run
  producing its own recovery point, not a citation of someone else's document.

  _Config companion._ None. No check reads a citation. `ninja check` was run and watched green on
  all five.

- **6.0.0 (2026-09-17)** — MAJOR: the *Capture is out* gate's image clause narrows from a
  whole-tree default to one path. It read *"no tracked image outside
  `instructions/*/source/images/`"* and now reads *"no tracked images in
  `.docs/experiments/runs`"*.

  This is an incompatible redefinition, which is what makes it MAJOR by the reading 5.0.0 used: a
  repository tracking a raster in `.docs/reviews/hinge/source/images/` was failing this gate and now
  passes it.

  _Why:_ the clause was written to stop interim capture and it stopped engineering figures as a side
  effect. `.docs` held 28 tracked vector figures and could hold no raster at all, so the hinge
  review's eleven PNG renders were refused while the SVGs they came from were kept, and five renders
  the ball-and-socket brief cites by name did not survive the move into this repository. The survey
  of the CAD now planned needs shaded views beside the briefs, and a shaded view cannot be a vector.

  _Why that path and no other._ It is where the failure happened. The archive holds 13,962
  screenshots totaling 1,837 MB, and every one of them is under `.docs/experiments/runs/`, in
  fourteen run directories; run6 alone is 6,734 files and 936 MB. Nothing was ever lost to capture
  anywhere else, so nothing else needs the rule. A raster outside that path is an engineering
  figure, and an engineering figure is not capture.

  _Companion changes, same commit._ `.gitignore` denies raster and video under
  `.docs/experiments/runs/` rather than everywhere, and drops the `!instructions/*/source/images/**`
  negation it no longer needs; `src/stickbot/check_images.py` matches, and `build.ninja`'s
  description is unchanged because the gate still checks capture.

  _Config companion, exercised._ All three rules were run against planted violations. A frame
  force-added under `runs/2026-08-14-run6/` was named as *interim capture; frames belong in the
  scratchpad*; a tracked `build/probe.html` as *Sphinx output, rendered from source/*; a 6.0 MB file
  as *over the 5 MB ceiling*. Each exited 1, and each went green when removed. The same frame placed
  in `.docs/experiments/build-briefs/images/` passed, which is the case the narrowing exists for.

  _What the narrowing does not cover._ `.gitignore` also denies any `capture/` directory anywhere,
  and the gate does not, because the gate's words name one path. A raster force-added into a
  `capture/` outside `runs/` would pass. Nothing in the tree does that today.

- **5.10.0 (2026-09-16)** — MINOR: a new Working Rule, *Do not name a version in code that is not
  in a version-specific tree*, with its corollary that code which genuinely cannot be reused
  belongs in a tree named for its version.

  _Why:_ Mike's diagnosis, and it names a defect this repository had just produced twice. A routine
  is written for one version, the version is written into its prose, the routine is reused for the
  next version, and the prose is stuck. `hinge_spring.py` is the worked example: its `Hinge`
  docstring says the detent ring is given as a radius, a count and a climb *"so that the old
  tooth-and-valley joint can be expressed here too and used as a check"* — the interface was built
  version-neutral on purpose — while the module opened *"How hard the wedge hinge is to turn"*. The
  code serves both joints and the prose claimed one.

  The distinction the rule turns on is scope against history. *"draft9p0 offset the pattern by"* is
  history, explicitly past, and explains why a number is what it is; it stays. A line that reads as
  what the file is for does not.

  _Companion changes, same commit._ `hinge_spring.py` loses both version claims: it now opens *How
  hard a detent hinge is to turn* and its status line says it names no version because the geometry
  arrives in the `Hinge` it is handed. `memory/deciding-is-never-done.md` had told the reader to put
  the version beside the status in every file, which was wrong for evergreen code and is now
  qualified.

  _Audited, not assumed._ Every version name under `src/stickbot/` was read and judged against the
  rule. The rest are history and stay: four in `make_plans.py`, two in `onshape_gui.py`, one in
  `gui_steps.py`, and `hinge_spring.py`'s three references to the old joint, which are the reason
  the interface is general. `gui_steps.py`'s usage example names `draft10p9`, a draft that does not
  exist, which cannot be mistaken for a claim.

  _Config companion._ None. No check distinguishes scope from history, and inventing one was not
  attempted. `ninja check` was run and watched green on all five.

- **5.9.1 (2026-09-16)** — PATCH: *Where developmental draft products live* reads *an example
  completed CAD in Onshape* where it read *an example completed CAD at `_TODO_`*.

  _Why:_ Mike's ruling, 2026-09-16 — the Constitution does not track where a version of the
  stickbot lives, because that would make an amendment out of every change of workspace. The
  placeholder was an open obligation on this file, and three other documents were carrying asks
  against it.

  This is a PATCH rather than a principle removal. The line sits in a descriptive section, not in
  the Working Rules or the Quality Gates, and nothing that binds work changes. The *Recovery point*
  gate still wants a published named version for the next session to start from; what changes is
  that the Constitution is no longer where that version gets named.

  _Companion changes, same commit._ The three asks are withdrawn:
  [`../../../.docs/2026-09-14-move-to-stick-e-bot.md`](../../../.docs/2026-09-14-move-to-stick-e-bot.md)
  loses the third item of Phase 3, which closes that phase, and the clause in
  `task.draft9p4.assembly_legs`; draft9p4's deactivated plan loses the same ask from *What we do not
  know yet*; and `.docs/tasks.md` loses it from #208's entry, recorded in that file's header with
  the other repairs. `README.md`'s four `_TODO_` reference-model rows are untouched: those are the
  student-facing links themselves, blocked on the document being deliberately shared, and this
  ruling does not reach them.

- **5.9.0 (2026-09-16)** — MINOR: a new Working Rule, *Name a unit of work; do not number it*. An
  identifier is a dotted name in the style the plans already use for steps and requirements, and it
  is written into the plan that will do the work. The numbers are closed at #217 and
  [`../../../.docs/tasks.md`](../../../.docs/tasks.md) is what they resolve against.

  _Why:_ the numbers were coined in a Claude Code task store at `~/.claude/tasks/<session-id>/`,
  which is keyed by session, is not in git, and does not survive the session that made it. The
  repository cites them 107 times across 42 files and defined none of them, so every one of those
  citations was already unreadable to any session but the one that coined them; the session opened
  in this repository on 2026-09-15 had no task directory at all. Two citations were dangling
  outright: `.docs/build/plan/12-gripper.md` and `14-assembly-legs.md` both wrote
  `[task #29](../../robot-build-plan.md)`, and that file does not contain the word *task*.

  This is a new principle and removes none, which is why it is MINOR. Nothing about how a plan is
  activated changes, and the existing rule that an open task is folded into the file it falls in is
  unchanged; naming is what that rule was always missing.

  _Companion changes, same commit._ `.docs/tasks.md` holds all 193 records exported from the store,
  numbered 25 to 217, with subject, status, dependencies and description. Six descriptions had
  swallowed the closing tag of the tool call that wrote them and ran on into
  `</description> <parameter name="activeForm">`; the tail is trimmed and the header says which six.
  `robot-build-plan.md` § *Nothing here is settled until the whole robot is printed* is now
  `task.print.whole_robot` and the two dangling links point at it. The sixteen tasks that were open
  are named and placed in [the move plan](../../../.docs/2026-09-14-move-to-stick-e-bot.md)
  § *The open work, by name*, three of them recorded as superseded.

  _Config companion._ There is none, by decision: a sixth gate checking that every cited number
  resolves was proposed and dropped, because the numbers are closed and the set it would check
  cannot grow. `ninja check` was run and watched green on all five.

- **5.8.0 (2026-09-16)** — MINOR: a new Quality Gate, **Imports installed**. No tracked Python
  edits `sys.path`; the `stickbot` package is imported by name and paths into the tree come from
  `repo_root()`.

  _Why:_ an installed package makes `import` mean the same thing from any directory, and a single
  `sys.path.insert` undoes that silently — the wrong module imports fine. Thirteen of draft9p4's
  scripts inserted an absolute path to a different checkout, so they read one repository's modules
  while writing their output into it, and nothing said so. 5.7.1 removed the last of those; without
  a gate the next hurried script puts one back.

  Nothing is removed or redefined, which is why this is a MINOR.

  _Companion changes, same commit._ Phases 2 and 3 of
  [`../../../.docs/2026-09-16-python-packaging.md`](../../../.docs/2026-09-16-python-packaging.md).
  The hinge review's three figure generators and nineteen run scripts import `stickbot` and drop
  their `sys.path` lines; draft9p4's thirteen lose the absolute paths they read and wrote through.
  Four run folders that finished before the package existed are named in the check as exempt,
  because their scripts are a record of what was driven rather than code anyone runs again.

  _Config companion, exercised._ `stickbot-check-imports` is the gate, wired into `ninja check` as
  a fifth target. A `sys.path.insert` was planted in `.docs/reviews/hinge/make_figures.py`; the gate
  named the file and line and exited 1, and went green when it was removed. `ninja hinge-figures`
  regenerated all eleven figures and five tables byte-identical, which is what says the rewritten
  imports reach the same code.

- **5.7.1 (2026-09-16)** — PATCH: the probe-script escape hatch says a probe that proves useful
  moves into **the `stickbot` package** rather than into `tools/`, which no longer exists.

  _Why:_ the Python became an installed package. `tools/`'s thirty modules and the three
  design-source programs under `instructions/robot-guide/` are now `src/stickbot/`, installed
  editable by `uv sync`, so `import` resolves through the environment instead of through where a
  file happens to sit. Thirty-one live documents named the old paths and were repointed in the same
  commit.

  _Config companion, exercised._ `build.ninja`'s four check rules now call console scripts —
  `stickbot-check-wrap` and its three siblings — rather than `python3 tools/*.py`. Three of the four
  had been running on the system interpreter rather than the environment. `ninja check` was run and
  is green on all four, and both gates were run from an unrelated directory to confirm they no
  longer depend on the working directory.

- **5.7.0 (2026-09-16)** — MINOR:
  [`../../rules/parts/prose-style.md`](../../rules/parts/prose-style.md) gains § *Voice for
  student-facing text*. Playful, never judging, never talking down; a number
  belongs to the thing it measures and never to a person.

  _Why:_ the rule existed in one place, a bullet in `.docs/README.md` that also named
  a retired pipeline's `content.py` as the authority on it. Clearing that pipeline out took the
  bullet with it, and a grep of `.claude/rules/` and `.claude/skills/` for *playful, talking down,
  judging, tone, voice, light-hearted* returned nothing — so the rule had never been in the
  contract at all, and deleting the bullet left it stated nowhere that binds. Two memories touch
  it and neither carries it: `write-for-students-who-will-succeed` has *light-hearted* only in its
  description, and `plain-words-for-middle-schoolers` says *"this is not the same as talking down
  to them"* as an aside qualifying a different rule. A memory is a finding, not an obligation.

  It sits beside § *Reading level for student-facing text* because that section already carves
  student text out of the contract's own register, which is what this rule needs to say next.

  The second-person half generalized on the way in: the original read *"numbers belong to this
  this model, never mine or yours"*, which is a rule about framing rather than about the model.

  _Config companion, exercised._ None; no check reads tone. `ninja check` was run and is green.

- **5.6.1 (2026-09-16)** — PATCH: no document states a target for how long the figure takes to
  CAD. `lesson-design`'s description drops *the eight-hour clock*; `onshape` says FeatureScript
  does not belong *in this course* rather than *in these eight hours*.

  _Why:_ the number had no owner. `lesson-design` advertised the clock in its frontmatter and said
  nothing about it in its body, and 5.6.0 had just removed the constitution's only statement of it
  as out of altitude for a Working Rule. A target named in three summaries and defined nowhere is
  not a constraint, it is a number people quote.

  _Companion changes, same commit._ `README.md`, `.docs/project.md` and `.docs/README.md` describe
  the course without a duration. `.docs/README.md` loses two paragraphs written against the target:
  *the lesson does not fit the clock*, and a comparison of two proposals' estimated minutes.
  `instructions/robot-guide/lesson-design.md` loses § *The clock, and why it does not fit yet* —
  every sentence in it measured against the target, and it cited a *Fits the clock* gate and a
  90-minute rule that are not in the Constitution. Its floor-and-ceiling conclusion is kept; the
  agent-pace timings it reported remain in `steps.log` and test report 2, which that section named.

  _Config companion, exercised._ None. `ninja check` was run and is green.

- **5.6.0 (2026-09-16)** — MINOR: *Define success, then loop until it is verified* becomes
  **Define success and initial steps, then loop until successful**, and its body widens from
  teaching material to all work. It read *"say what the reader or student can do at the end, not
  what steps exist"*; it now reads *"don't blindly follow rigid steps; iterate and adjust the steps
  toward success."*

  _Why:_ every other Working Rule holds for code, prose, CAD and a conversation alike. This one had
  a general title over a body that only defined success for a document with a reader, so the rule
  had no operative content for a part, a script, an audit or a fix. The narrow form also said less
  than it looked like it did: `lesson-design` § *Checkpoints* already separates a visible result
  from an invisible one, which is the nearer question when writing a lesson.

  The obligation is unchanged and nothing is removed, which is why this is a MINOR. What is added
  is the initial-steps clause: success alone was never enough to start from.

  **`initial steps`, not `a plan`.** An earlier draft said *an initial plan*, and *plan* is a
  loaded word here — the Working Rule above it and
  [`../../rules/parts/plan-activation.md`](../../rules/parts/plan-activation.md) both mean a run
  plan with an `active-plan.md` pointer. This rule asks for neither.

  _Config companion, exercised._ None; no check enforces it. `ninja check` was run and is green.

- **5.5.2 (2026-09-16)** — PATCH: Layer 4 stops listing `.docs/session-state.md`, which is
  deleted. The `project.md` bullet now says a run's own ids are in its folder under
  `.docs/experiments/runs/`.

  _Why:_ the file was a snapshot titled *end of run 2*, and run 2 is overcome by events. It was
  spared once by the reorganization, on the ground that it was the only registry of the robot's
  Onshape ids. It was not: every did, published version id and element id it held is in
  `experiments/runs/2026-08-11-run2/`, in the same table shape run 1 uses. What else it carried was
  a design settled twice over since — Ø12 limbs, *round bumps beat wedges* — and conventions that
  are now two `ninja check` gates, two memories and the Branch Policy.

  _Companion changes, same commit._ `.docs/README.md` points at run 2's folder instead. Two links
  in `runs/2026-08-23-draft9p0/plan.md` now resolve to nothing and are left alone, which is what
  the Archive section says a record's paths mean.

  _Config companion, exercised._ None. `ninja check` was run and is green.

- **5.5.1 (2026-09-15)** — PATCH: two live rules stopped naming `.parts/`, which 5.1.0 retired.
  Maintenance step 1 now points at `.claude/rules/constitution.md`, `.claude/rules/parts/` and the
  skills. [`../../rules/parts/prose-style.md`](../../rules/parts/prose-style.md) § *Where RFC 2119
  applies* does the same, and gains the skills, which it had omitted while the Constitution's
  Governance section listed them.

  Changelog entries below still name `.parts/` and are left alone: a record points at where a file
  lived when it was written, which the Constitution's Archive section states.

  _Companion changes, same commit._ `CLAUDE.md`'s first line gains a full stop. The memory
  `claude-md-is-harness-not-contract` is deleted: it said the file exists to make the agent re-read
  the Constitution and is therefore outside the prose standard, and neither half is true any more —
  the re-read instruction went at 5.1.0, and the three-line file meets the standard.

  _Config companion, exercised._ None; no check enforces a path inside prose. `ninja check` was run
  and is green.

- **5.5.0 (2026-09-15)** — MINOR: the opening line binds an actor rather than a place.
  *authoritative for work in this repository* becomes *authoritative for work by you or any agent*.

  _Why:_ the contract had just been moved between repositories, and scoping it by directory says
  nothing about the same agent working somewhere else. Scoping it by who is doing the work makes it
  follow them. The list it supersedes is unchanged: ad-hoc conventions, verbal agreements, and
  conflicting guidance in `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md` or
  sub-directory READMEs.

  A material expansion rather than a redefinition, which is why this is a MINOR: nothing that was
  bound before is unbound now, and the obligations themselves are untouched.

  _Config companion, exercised._ None; no check enforces the scope line. `ninja check` was run and
  is green.

- **5.4.0 (2026-09-15)** — MINOR: **Write and fix only the live draft** joins § *Where
  developmental draft products live*. A superseded draft is a record of what the instructions were
  on the day it was made, so a defect in one is history rather than a bug.

  _Why:_ the rule existed only in a memory, `one-guide-is-the-end-state`, whose own facts had gone
  stale — it named `robot-guide4` as the live guide, and `robot-guide4` stayed in the
  archive. Checking it the way `limbs-are-twelve-mm-cylinders` was checked found the opposite
  answer: that one was a stale duplicate of the design source and was deleted, while this one was
  the only copy of a real rule that no file carried. The section it now sits in already said drafts
  are kept side by side to show the differences, and stopped short of saying not to edit the old
  ones.

  _Companion changes, same commit._ `one-guide-is-the-end-state` is deleted, the rule having a home.
  `trust-mike-or-read-the-docs` becomes `trust-the-user-or-read-the-docs`, finishing what 5.3.0
  started; its `name:`, its filename and both `[[links]]` moved together.
  `agent-browser-borrows-its-session` is cut back to the failure mode that no file carries — a 401
  from 9223 means restart the agent browser, not ask for a sign-in — and points at
  `.docs/browser-access.md` for the mechanics it used to restate. Its `type:` becomes `feedback`,
  which is what it always was.

  _Config companion, exercised._ None. No check enforces either rule; `ninja check` was run and is
  green.

- **5.3.0 (2026-09-15)** — MINOR: the memories become part of the contract. `MEMORY.md` joins
  `.claude/rules/`, the Parts table gains a row for it, and a new obligation says to operate per the
  memories. The bodies move to `memory/` at the repository root.

  _Why:_ they were in the harness's own store under `~/.claude/projects/<slug>/memory/`, keyed to
  the working directory. They are project knowledge — settled numbers, habits that cost a run, tools
  that behave unlike their documentation — so they belong with the project and have to survive it
  being moved or cloned. Moving to `stick-e-bot` is what surfaced it: the store is keyed to the old
  path and does not follow.

  _Why the bodies are not injected._ All 29 come to 12,232 tokens against a 14,275-token contract,
  so injecting them would roughly double what every request carries. The index is 1,283 tokens and
  carries a one-line hook per memory, which is enough to decide whether a body is worth reading.
  Whether that is enough in practice is being tried, not assumed.

  Nothing is removed or redefined, which is why this is a MINOR. Where a memory and
  `constitution.md` disagree, `constitution.md` wins.

  _Companion changes, same commit._ The memories no longer name one person: a role reference and a
  dated attribution alike now read *the user (Mike)*, so the contract does not hardcode who is at
  the other end. `trust-mike-or-read-the-docs` kept its filename and `name:` at this version,
  because those were its identity and two `[[links]]` resolved through them; 5.4.0 renames it.

  _Config companion, exercised._ The 29 bodies and the index become tracked Markdown, so
  `check_wrap.py`, `check_spelling.py` and `check_reading_level.py` pick them up from `git ls-files`
  with no change. All three were run over them.

- **5.2.0 (2026-09-14)** — MINOR: a new Quality Gate, **Capture is out**, and the Archive section
  gains the second archive. The repository moved to `stick-e-bot`; the old one stays on disk
  holding what was left behind.

  _Why:_ the old repository committed 12,977 screenshots totaling 1,651 MB, because a take wrote
  its interim capture into the same tree it published from. The rule against it was written down on
  2026-08-23 in a scratch file, with the exact `.gitignore` it needed and the 1.2 GB it would hide,
  and nobody acted on it for three weeks. Writing a rule down is what failed, so this one arrives
  as a gate that runs rather than a sentence to remember. Interim capture now goes to the session
  scratchpad and a frame reaches git only by being placed on a page.
  [`../../../.docs/2026-09-14-move-to-stick-e-bot.md`](../../../.docs/2026-09-14-move-to-stick-e-bot.md)
  holds what was measured and what moved.

  No rule is removed or redefined, which is why this is a MINOR.

  _Companion changes, same commit._ `README.md` describes the new layout. `check_spelling.py` and
  `check_wrap.py` drop the exclusions for a retired experiment and `old-constitution.md`, neither of
  which exists here. `.docs/reviews/hinge/make_figures.py` no longer hardcodes a dead session
  scratchpad; it reads `HINGE_FRAMES`. Eleven links broken by the carry were repointed or, where
  repointing would have changed what a sentence claims, turned into named references to the
  archive.

  _Config companion, exercised._ `src/stickbot/check_images.py` is the gate, wired into `ninja
  check` as a fourth target. It was run against two deliberately planted violations: a PNG
  force-added outside a guide's `source/images/`, and a 5.7 MB file. It refused both, naming each
  and its reason, and went green once both were untracked. `.gitignore` was exercised separately,
  before any file was copied: a probe under `instructions/*/source/images/` came back tracked while
  the same name under a `capture/` directory and at the repository root came back ignored.

- **5.1.0 (2026-09-14)** — MINOR: the contract moves into `.claude/`, and a new Working Rule
  requires the active-plan pointer. `constitution.md` becomes `.claude/rules/constitution.md` and
  `prose-style.md` becomes `.claude/rules/parts/prose-style.md`; the other four parts become skills
  under `.claude/skills/`. A new part,
  [`../../rules/parts/plan-activation.md`](../../rules/parts/plan-activation.md), says how a plan
  becomes active and how it stops being active. The Parts table gains a column for how each part
  arrives, and the obligation to invoke a skill before the work it governs begins.

  _Why:_ the contract reached context by a ritual re-read named in `CLAUDE.md`, and the ritual did
  not fire. Across draft9p4 it came due about 35 times, `constitution.md` was read twice, and the
  active plan was never read at all. A file re-read after a compaction comes back as a bare path
  once it passes roughly 5,000 tokens, so the 10,342-token run plan was the document most certain
  to be missing. Everything under `.claude/rules/` is injected from disk on every request, which is
  not subject to that limit and does not depend on anybody remembering.
  [`../../../.docs/2026-09-14-contract-into-claude-rules.md`](../../../.docs/2026-09-14-contract-into-claude-rules.md)
  holds what was measured and what was proven.

  No rule is removed or redefined, which is why this is a MINOR. The one new obligation is the
  pointer; the agreement to follow the constitution is unchanged and stays unconditional on a plan.

  _Companion changes, same commit._ `CLAUDE.md` keeps the agreement and drops the instruction to
  re-read a file that is now injected. `.gitignore` ignores `.claude/*` and re-includes `rules/`
  and `skills/`. Live references across `.docs/`, `README.md`, the draft9p4 plan and two tools were
  repointed; references in archived run records were left pointing at where the files lived when
  they were written, and the constitution's Archive section now says that is what they mean.

  _Config companion, exercised._ `check_wrap.py` and `check_spelling.py` build their file lists
  from `git ls-files`, so they followed the contract into `.claude/` without being changed. Both
  were run over the moved tree; the wrap check caught eight lines the new paths pushed past 100
  columns, which were re-wrapped. `check_reading_level.py` never covered the contract and is
  untouched. Nothing enforces the new Working Rule, so there is no companion to exercise for it.

- **5.0.0 (2026-08-18)** — MAJOR: *use a variable wherever a number repeats* is removed. A
  measurement becomes a variable **only when the build plan asks for it** — the Variables table in
  [`.docs/robot-build-plan.md`](../../../.docs/robot-build-plan.md) is the whole ask, and a number
  is a variable when it has a row there and not otherwise. A session plan, a build brief or a run
  plan may argue for a row; it does not create one. Every other measurement is typed, and a
  constraint or a reference carries the intent. Changed in [`onshape.md`](../onshape/SKILL.md) and
  [`modeling-practice.md`](../modeling-practice/SKILL.md).

  This is a principle removal and an incompatible redefinition, twice over: a model that types a
  repeated number, which the old rule rejected, now passes; and a model that declares a variable no
  row asks for, which the old rule required, now fails.

  _Why:_ the old rule decided a design question by standing rule rather than where the design is
  recorded, so it produced variables nobody asked for and nobody was responsible for keeping true.
  4.0.0 had already bolted on a bound, *not every variable is a scaling knob*, which was the
  everywhere rule over-reaching and being patched instead of narrowed. Naming the build plan as the
  single asker also gives the vocabulary one owner: a variable is a promise that a number means the
  same thing in every part that uses it, and that promise cannot be made by a document that sees
  one part.

  What does not change: constraints, fully defined sketches, anchoring each sketch to the geometry
  that gives it meaning, and the ban on a typed number standing in for a reference. The acceptance
  test in [`modeling-practice.md`](../modeling-practice/SKILL.md) still requires that changing one
  driving dimension reproportions the model rather than breaking it; it no longer assumes that
  dimension is a variable.

  _Companion change, same commit._ [`.docs/robot-build-plan.md`](../../../.docs/robot-build-plan.md)
  is the ask, so it was cut from 24 rows to the four numbers a student changes to make the robot
  their own: `#torsoH`, `#torsoW`, `#torsoD` and `#limbSeg`, the three torso numbers now independent
  of each other rather than expressions on the height. The other nineteen measurements moved to a
  **Proportions — recorded, not driven** table that keeps the ratio each came from, so promoting one
  later is a decision rather than a re-derivation. The 27 references to the retired names in the
  plan's prose became plain dimensions.

  _What this costs._ `run7p1-ball-and-socket` holds eight variables and not one of them now has a
  row. `#wall`, `#collar`, `#slit` and `#stud_len` never had one; `#ball` and `#stalk` were the
  plan's `#ballD` and `#stalkD` under other names; `#fit` and `#grip` are typed measurements from
  this commit on. Run 7's `M1` asked for all eight, and from this version an ask in a run plan is
  not an ask. So `instructions/robot-guide3/source/ball-and-socket.rst`, which teaches those eight
  as its opening move and shows them in 47 captured frames, no longer matches the contract.
  Rewriting it is open and is not decided here.

  No config companion enforces the rule, so maintenance step 5 has nothing to exercise; the check
  target was run and its state reported.

- **4.0.1 (2026-08-17)** — PATCH: `.parts/onshape.md` drops the sentence *a tool used once is a
  tool forgotten by the next week*. _Why:_ it was a maxim standing in for a reason, and it is not
  true of this course. Eight hours cannot introduce every feature a robot needs and then use each
  one twice; a tool that appears once and does its job is a tool the class got the use of. Quoting
  the maxim was about to decide whether **Shell** stays in the course, which is a judgment about
  the robot, not a rule that can be applied from a sentence.

  The obligation it was attached to — *reuse each one at least twice in the same session* — is
  unchanged, which is why this is a PATCH and not a principle removal.

- **4.0.0 (2026-08-17)** — MAJOR: `.parts/onshape.md` no longer says **sketch on planes over
  faces**. That principle is removed, not reworded, and the rule that replaces it can be violated
  by a model the old one approved, so it is an incompatible redefinition. The new rule is
  **anchor each sketch to the geometry that gives it meaning** — a plane when the shape is placed
  from the origin, a face or edge when it is placed from a part.

  _Why:_ the old rule was written on 2026-08-10 in `8630961`, the bulk rewrite that created the
  file, before anything in this repository had been modeled; the earliest run is dated the next day.
  It had no build behind it, and it hid a defect rather than preventing one. A sketch put on the Top
  plane because the collar happened to be extruded from the Top plane still depends on that collar —
  the dependency is simply no longer recorded anywhere, so moving the collar leaves a model that
  regenerates clean and is wrong. Avoiding faces is also what is expensive over the REST API rather
  than what is wrong in the UI, which is the failure
  [`modeling-practice.md`](../modeling-practice/SKILL.md) already names: _never let the tool dictate
  the pedagogy._ The two files had been pulling against each other, one condemning magic numbers
  while the other produced them.

  Carried in the same amendment: **not every variable is a scaling knob.** A joint's dimensions
  come from how the plastic bends, not from how big the robot is, so the change-one-number
  demonstration belongs on a major shape and never on a joint. Without it, _use a variable wherever
  a number repeats_ invites a student to scale a ball and break its fit.

  No config companion enforces either rule, so maintenance step 5 has nothing to exercise; the
  check target was run and its state reported.

- **3.2.1 (2026-08-12)** — PATCH: Working Rule 8 says what a step is — a
  software or hardware build, a calculation, an analysis, a compilation, a test,
  a validation, a verification — so "surface every skipped step" cannot be read
  as covering only the written instructions. The same edit restores two
  obligations 3.2.0 dropped, *every assumption you could not check* and *if a
  step failed, say so and describe it*, and removes two it had imported from the
  source that describe a file installer rather than this repo: *refused
  overwrite* and *missing dependency*.

- **3.2.0 (2026-08-12)** — MINOR: a written prose standard, and this file
  rewritten to obey it. `.parts/prose-style.md` names four sources — Kernighan
  for the register, Bloch's *Effective Java* for the shape of a rule, Strunk for
  omitting needless words, RFC 2119 for obligation vocabulary — and the seven
  rules that follow from them. It is now the first row of the Parts table,
  required for any writing, and a Quality Gate. _Why:_ the rules against
  overwriting were all unenforced prose, and the file kept growing by rewording.
  A standard that names what a rule looks like is checkable by a reader in a way
  that "be concise" is not.

  Applied to this file: six rule titles that were labels became the obligation
  itself, so a reader who stops at the bold lead still knows what to do —
  *Simplicity first* became **Build the simplest thing that solves the problem**,
  *Surgical changes* became **Touch only what the task requires**, and likewise
  for rules 1, 5, 6, 13 and 15. RFC 2119 words were capitalized where an
  obligation is actually being set. Three duplications were cut: the *Timing must
  be measured* note restated Working Rule 9, the `shadedviews` paragraph restated
  the bullet above it, and the Governance compliance bullet restated Branch
  Policy.

- **3.1.0 (2026-08-12)** — MINOR: the rules the source constitution carried were
  brought back to their original wording, widened from code to content (code,
  prose, or CAD) where the domain was the only thing that differed. _Why:_ a
  side-by-side of the two files showed the Working Rules had grown 67% — 426
  words to 712 — for the same obligations. The growth was rewording, not new
  rules, and rewording without a rule change is drift. Two principles were
  restored that adapting had dropped:
  - **Small, bounded, side-effect-free** (source rule 7), which had no
    counterpart here, generalized to sentences and paragraphs in prose and
    sketches in CAD.
  - **Documentation is part of the change** (source _Documentation Hygiene_),
    now Working Rule 13. A documentation gap is a defect, not a follow-up.

  Also carried forward: the source's **never force-push or rewrite published
  history** clause into Branch Policy, and its **scratch / probe script escape
  hatch** into the Quality Gates notes, where it documents what
  `tools/check_*.py` already skips. The rules renumbered 1–15; two rules had
  both been numbered 7.

- **3.0.0 (2026-08-12)** — MAJOR: the course subject changed to a
  150 mm articulated robot figure, and the **character and artwork** principle
  was **removed** rather than reworded. A principle removal is a major bump.
  _Why:_ that principle existed to keep a rights holder's character inside the
  classroom — no copyrighted reference art, nothing published or sold. An
  original robot has no rights holder, so the rule had nothing left to enforce
  and keeping a reworded version would have implied a constraint that no longer
  applies. Carried in the same reorganization:
  - **Governance** and this maintenance part, both adapted from the
    `book-em-danno` constitution. Before this there was no written rule for
    changing the rules, so amendments left no version bump and no rationale.
  - `parts/` became **`.parts/`** and gained `modeling-practice.md`, which opens
    by declaring itself the standard every model must meet — contract text that
    had been filed as a working note. Session material moved out to
    `instructions/`; the Parts section now describes both, plus the audience
    rule that decides which folder anything else goes in.
  - Working Rule 8 gained a **no grandstanding, no hyperbole** clause: claim
    success, justify a rule, or persuade a reader or subagent only from
    established, provable information.
  - Two new Quality Gates, **Spelling** and **Reading level**, with the
    on-disk companion they need: `build.ninja`'s `check` target over
    `src/stickbot/check_wrap.py`, `check_spelling.py`, `check_reading_level.py` and
    `src/stickbot/dictionary.txt`. Per maintenance step 5 it was **run**, not merely
    written — the first run found 118 British spellings and 2 over-long lines.
    The compound the plan sheets use for the vertical axis is not in the builtin
    dictionary and was caught only after `src/stickbot/dictionary.txt` was added, which
    is why the project dictionary exists at all.
- **2.0.0 (2026-08-09)** — the version this changelog opens at. Recorded from
  the footer rather than reconstructed: adapted from the **mostrobotpy
  constitution v1.0.0** and repurposed for this Onshape CAD course. It keeps
  that structure — a lean always-read core plus per-work-type parts, and the
  numbered Working Rules — and carries the rules this course needs: the
  eight-hour budget, floor and ceiling, a published recovery version per
  session, and Quality Gates that make a written step prove itself before it is
  called done. Entries before this one were not kept, so this is where the
  history starts.

## See also

- [`.claude/rules/constitution.md`](../../rules/constitution.md) — Working Rules, Quality Gates, and
  the Governance section this part expands.
