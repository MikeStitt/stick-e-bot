# Open work

**Every unit of work this repository knows about that no plan is doing.** Work a plan will do is
named in that plan; this is where the rest lives, and the Constitution's Working Rule *Name a unit
of work; do not number it* points here.

Each item carries a dotted name and nothing else identifies it. **Do not number anything.**
[`tasks.md`](tasks.md) is the dictionary the numbers already cited in this repository resolve
against; it is history and nothing appends to it.

An item leaves this file when a plan takes it, and the plan carries the same name.

## Held for a draft that has not run

These four came in from [`tasks.md`](tasks.md), where they were the last entries written before the
numbers closed for good. Each kept the name it already had.

- **`task.reproduce.draft9p4`** — *Steps reproduce* did not close on tutorials 4, 5, 6, 8 and 9.
  Waits on the guide draft that follows draft9p5.
- **`task.capture.tutorials_1_to_5`** — re-open the capture against the guide draft.
- **`task.hinge.ear_rename`** — rename `EAR`, `EAR_FREE`, `EAR_MOVE` and `EAR_STRESS` in
  `make_plans.py`, where the design source and the briefs already say *fork prong*. No plan holds
  it, and where the rename stops is the open question: `hinge_spring.py` carries the same word
  through its public interface, and `make_plans.py` prints it as drawing text, so renaming the
  constants alone leaves every SVG byte-identical.
- **`task.briefs.section_retakes`** — retake `cad-body-section.png` and `cad-l-limb-section.png`.
  Both carry a selection highlight from the session that shot them, and `l limb`'s section is cut
  on the Front plane where the Right plane shows the blade. The plane wants deciding before the
  retake.

## `task.model.design_intent` — the big one

Every sketch in the model is built through the REST API from absolute coordinates with `constraints:
[]`. Under-defined, magic-numbered, and exactly the habit the course exists to prevent — see
[`modeling-practice`](../.claude/skills/modeling-practice/SKILL.md). The guide therefore
*demonstrates* the anti-pattern while *describing* the right thing, which is the worst combination
available.

**This is now work, not research.** `BTMSketchConstraint` and the `LENGTH` dimension were read back
off a rectangle drawn and dimensioned by driving the GUI — see [`onshape-api.md`](onshape-api.md).
Constrained sketches can be written through the API today.

Two gates when it is done: every sketch reports **fully defined**, and changing one driving variable
produces a correctly proportioned figure rather than a pile of parts. Both are checkable from a
script, so build them into the capture run rather than eyeballing them.

## The model, the guide and the curriculum

- **`task.guide.walk_the_path`** — **Nobody has walked the click-path.** A script did. Pacing,
  wording, whether a twelve-year-old finds the Depth box — all unknown until someone runs a session.

- **`task.guide.fillet_range`** — **The fillet radii are the fragile dimensions.** A radius has to
  fit the face it rounds, so the guide's claim that any size of figure works with these steps is
  only tested at one size. Either test the range or stop claiming it.

- **`task.guide.mirror`** — **Mirror is unverified and unused.** The build does everything twice by
  hand, which is the wrong lesson; Mirror is currently parked as a stretch task. Its `command-id` is
  known (`SKETCHMIRROR`, `mirror`), its dialog is not.

- **`task.guide.appearance_wording`** — **The appearance menu wording is unverified.** The highlight
  matches `[Aa]ppearance` loosely because the exact item text was never read.

- **`task.readme.model_links`** — `README.md`'s reference-model links are still `_TODO_`. The
  document IDs are in [`project.md`](project.md).

- **`task.docs.second_page`** — **`docs/` needs its second page.** The first is
  [`what-you-are-building.md`](../docs/what-you-are-building.md) — the robot, Onshape's vocabulary,
  and versions, written for a student and clean at grade 8. What is not covered yet: anything about
  printing the parts, and anything about the assembly.

- **`task.guide.salvage_two`** — **Session 1's lesson-design exists now**, at
  [`../instructions/robot-guide/lesson-design.md`](../instructions/robot-guide/lesson-design.md),
  and it carries the teaching half salvaged from the old session. Two salvage items still belong in
  `source/index.rst` rather than the plan: the *Symmetric was not ticked* failure, and the decision
  on construction geometry — the page refers to a rule about it at line 309 and never teaches it.

- **`task.constitution.review_findings`** — **The constitution review's 19 findings are
  unremediated.** The adversarial review ran on 2026-08-12 against `e8508af`, `fffec7c` and
  `cb5ab99`, and nothing was applied — the last commit touching `constitution.md` or `.parts/`
  predates it. The findings, the three I contested, how a second round ruled on them, and the
  outstanding list are in
  [`2026-08-12-constitution-review-report.md`](2026-08-12-constitution-review-report.md). The
  cheapest item on that list is re-wrapping `constitution.md` to 100 columns: while it is red,
  `ninja check` never reaches the spelling and reading-level gates.

- **`task.guide.videos`** — **The build videos are a record of a build, not a lesson.**
  `instructions/robot-guide4/` now links a clip at the end of each block of steps, captured by
  `rec.py` as CDP event frames while the harness drove Onshape. They are honest and they are not yet
  teaching: the pointer jumps rather than moves, values appear in boxes already fully typed, there
  are long dead waits where the harness was blocked on a server round trip, and nothing names what
  is happening or why. The link text says *similar steps* because that is all they are — the clip
  covers the same ground as the pictures above it, not the same clicks in the same order. What would
  make them work for a student: a pointer that travels and pauses where a hand would, typing shown
  as typing, the dead time cut, a caption or a title card per step, and a decision about whether
  each clip covers one step or one section. Until then the pictures are the instruction and the clip
  is a second look. See
  [`experiments/runs/2026-08-19-run8p1/register.md`](experiments/runs/2026-08-19-run8p1/register.md).

- **`task.review.professional_pass`** — **The reviewer pass has not been run.** A different review
  from the one above, and Phase 3 of the reorganization. A reading pass, not a script: **Fable**
  reads the repository's prose — `.claude/rules/`, `.claude/skills/`, `instructions/`, `docs/`,
  `.docs/` and both READMEs — and flags three things.
    - **Unprofessional statements.** Snark, in-jokes, dismissiveness — anything that would not
      survive being read aloud to the class, or to a parent.
    - **Judgments based on age.** Text that sorts people by age and then uses the sorting to
      decide something. The same move made with grade level is in scope.
    - **Judgments based on status.** The same move made with standing rather than age —
      seniority, credentials, prior tool experience, or whether someone counts as a beginner.

  **What is flagged** — an age, grade, or standing substituting for a capability, an audience, or
  a permission. **What is not** — naming who is actually in the room. "Students range from
  middle-schoolers who have never opened a CAD tool to high-schoolers with some Fusion behind
  them" reports the roster. "A fourteen-year-old would not follow this" judges a person by their
  age. The first is a fact about the class; the second is a guess about a reader.

  **What it produces.** Every file is committed first, so Fable's changes land as a clean diff
  against a known state. Fable then edits in the working tree — the diff is the proposal — and
  writes `.docs/<YYYY-MM-DD>-professional-review-report.md` recording what it changed and why.
  **Nothing it writes is adopted by being written**: the diff gets read hunk by hunk, keeping what
  is right and reverting what is not, and the report is what explains a hunk when the change alone
  does not.

- **`task.checks.generator_status`** — **Every drawing generator is labeled `controlling`,
  `illustrative` or `superseded`**, in its own opening, with the version or date it belongs to.
  `make_plans.py` controls; `make_brief_sheets.py` and `hinge_spring.py` illustrate; the hinge
  review's three generators and the three studies under `experiments/sketches/` are superseded, each
  frozen at its own snapshot. The rule is
  [`../memory/deciding-is-never-done.md`](../memory/deciding-is-never-done.md) and the argument
  behind it is [`2026-09-16-derived-figures.md`](2026-09-16-derived-figures.md). What is still open
  there: a verdict that fails a check rather than sitting in a heading.

- **`task.curriculum.stage5_routes`** — **Four Stage 5 teaching routes lost their home when the
  limbs became cylinders.** `#limbD` is 12 and every limb is a Ø12 cylinder, so the limb rows in the
  Stage 5 build order — [`robot-build-plan.md:609`](robot-build-plan.md) and `:611` — no longer
  describe a part anyone will model. What that costs, against the coverage table:
  - **Parallel** (`:689`) and **Perpendicular** (`:690`) are earned only in **set-piece 1**, the
    sloppy quadrilateral squared by constraints, which was the shin.
  - **Sketch Fillet and Chamfer** (`:674`) is earned only on that same quadrilateral's corners.
  - **Loft** (`:707`) is earned only on the upper arm's ellipse-to-rounded-rectangle change of
    section.
  - **Ellipse** (`:665`) and **Lines and Rectangles** (`:661`) survive — the eyes and the torso
    rectangle each carry them without a limb.

  Each of the four needs one of three answers: rehome it on a part that still needs it, teach it
  on a scratch sketch that is not a robot part, or drop it from the curriculum and say so. This
  is a curriculum decision. **Do not shape a limb to keep a tool** — where a route cannot produce
  a Ø12 cylinder, the route gives way. See
  [`experiments/build-briefs/limbs.md`](experiments/build-briefs/limbs.md), which is written not
  to answer this.

- **`task.constitution.two_amendments`** — **Two constitution amendments are pending, both from the
  same failure.** Read
  [`constitution-maintenance`](../.claude/skills/constitution-maintenance/SKILL.md) before making
  them.
  - **Reading the specification is a verification step.** *Verification is evidence, not
    assertion* covers building the thing and looking at it; it does not say that the relevant
    specification and requirements MUST be read first. Add that, and attach it to the same list
    of activities as Working Rule 1 — before you plan, write, model, code **or direct**.
  - **`direct` belongs in every enumeration of what an agent does.** Working Rule 1 says "think
    before you write, model, or code"; the Quality Gates and *Verification is evidence* are
    written for someone doing the work with their own hands. Directing a subagent is none of
    those verbs, and it is how most of the work now happens. Every list of activities in the
    Constitution needs it.

  *Why:* three agents were launched against briefs written without reading the settled spec. The
  limbs had been fixed at Ø12 the previous day — decided in conversation, recorded in the hinge
  brief, in no document the launcher read — and the briefs invented sections that contradicted
  it. Nothing verified the direction, because no rule treats directing as work.

## The pipeline

- **`task.pipeline.camera`** — **`show_result` reopens the document** to get a known camera, which
  costs a 16 s page load each time. Correct, but it is most of the runtime of a capture run. A
  cheaper deterministic camera would pay for itself.

- **`task.pipeline.arc_circle`** — **Arc and circle have never been drawn from a script.** Rectangle
  and dimension have. Same shape of problem, and needed if more steps are to be driven click by
  click.

- **`task.pipeline.durable_profile`** — **The browser profile lives in a session scratchpad**, so
  the login does not survive. Move it somewhere durable, or get an API key from
  `dev-portal.onshape.com` and stop depending on a signed-in window.

- **`task.onshape.delete_stale_docs`** — Three stale Onshape documents can be deleted once nothing
  points at them — see [`project.md`](project.md).

- **`task.briefs.sphynx.to.md`** — Change the existing .docs/experiments/build-briefs/*.md to be
  .rst in .docs/experiments/build-briefs/source/*.rst that makes .md briefs that are used to
  build the CAD. The reasons is so that they stop getting hand editted numbers that go stale.

- **`task.briefs.remove.history.and.why`** — the briefs are filled with history and why that
  should have been in the plan. The briefs are instructions on what should be done, and we
  shouldn't fill the context of the CADer with extraneous history and why. If those are
  needed, they should be in the CAD.
