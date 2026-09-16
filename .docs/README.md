# .docs — working notes

Notes from building the course material and the reference model. These are **working notes, not the
contract** — the contract is [`.claude/rules/constitution.md`](../.claude/rules/constitution.md). If
a note here ever conflicts with the Constitution, the Constitution wins and the note is stale.

Each file marks what was **verified** (performed and observed) versus **unverified** (believed but
not checked), because the difference is the whole point of the Quality Gates.

This page is also the working list. Not every file in this folder is named here — the ones below
are the ones the current work points at.

## What needs doing, and what needs improving

State of play for the robot, at the end of run 2 (2026-08-11): Session 1 is
`instructions/robot-guide/source/index.rst`, a Sphinx page covering the body and the face. Part
one has been built twice, Part two once, and each was corrected after the run that tested it —
so **no part has been rebuilt from the text as it now stands**, and a run 3 would be its first
test. The run 2 model measures right — eyes r5, mouth 20.000 overall, neck Ø12 — at version
`run2-session1-complete`; the ball-and-socket and hinge joints are built at named versions too,
with ids in [run 2's folder](experiments/runs/2026-08-11-run2/README.md).

**Run 3 was launched, mis-briefed and thrown out** (2026-08-12). Its three agents read a brief
README claiming an open conflict over limb sections that did not exist; `#limbD` had been
settled at 12 the previous day. They were stopped, and the documents `ball-socket-run3` and
`lesson-run3` are deleted. The briefs have since been rewritten —
[`experiments/build-briefs/limbs.md`](experiments/build-briefs/limbs.md) replaces the four
invented limb briefs, and every numbers table carries a Source column. What the launcher does
before the next attempt is [`2026-08-12-launch-gate.md`](2026-08-12-launch-gate.md);
[`experiments/run3-launch.md`](experiments/run3-launch.md) holds the old prompts and is stale
against both.

## The big one — design intent

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

## Measure `#collar` from the ball's center, so `#grip` stops moving parts

**Done on 2026-08-27 as
[draft9p1p1's A2](experiments/runs/2026-08-26-draft9p1p1/plan.md), in the design source.**
Recorded here because [A2](experiments/runs/2026-08-25-draft9p1/a2-fit.md) got half of what it was
after and the other half was still available. `#collar` is now `#ball / 2 + #wall` = **9.0**, which
is the collar's own radius: the socket goes as deep below the ball's center as it is wide from the
axis. The model still has to be edited — that is Phase B. What follows is why.

`collar blank` extrudes `#grip` one way and `#collar - #grip` the other, so the socket is `#collar`
tall from a mouth at `#grip` down to a root at `#grip - #collar`. **A2 asks that a printing
clearance not ripple into any other robot dimension, and both of those ends move when `#grip`
moves.** [C2](experiments/runs/2026-08-25-draft9p1/c/c2-driving.md) drove `#fit` from 0.08 to 1 and
measured it: the socket stayed 11.000 tall at every value, and the tops of `Foot`, `Gripper` and
`u limb` each rose 2.0312 with `#grip`.

**So `#collar` is now the distance from the ball's center to the bottom of the socket**, and it
goes in `collar blank`'s second position on its own rather than as `#collar - #grip`. The root is
fixed, only the mouth moves, and the parts the socket is added to keep their dimensions when the
fit changes.

What it follows through to:

- The socket's overall height becomes `#collar + #grip` = 10.9465 rather than a constant, so the
  trade is named rather than hidden: before, the tabs kept a constant free length and the parts
  moved; now the parts keep their dimensions and the tabs' free length varies with the fit.
- `#collar - #grip` appears three times in the model and always means *the ball's center to the
  root*, so all three become plain `#collar`: `collar blank`'s second direction, the foot's
  `#collar_down`, and — inside a longer expression — `u limb`'s rod, which is
  `#limbCenter - #collar + #grip - #limbD / 2` and loses its `#grip` term.
- **No consumer sketches on a socket face**, checked over the API on 2026-08-27: `head`, `foot`,
  `u limb` and `gripper` each take the socket by `importDerived` and place it with a mate connector
  or a transform. So re-basing moves expressions and nothing else, and there is no rebuild order to
  get right.
- The slit floor does **not** follow from this on its own, and an earlier version of this section
  said it did. A2 fixes the root; the floor hung off the mouth at `#grip` and would have kept
  moving. It took [A1](experiments/runs/2026-08-26-draft9p1p1/plan.md) dimensioning the floor at
  `#ball / 4` below the ball's center to fix it, and that also
  [made the cut a slot for its whole depth](experiments/build-briefs/ball-and-socket.md).

**The test it has to pass is the robot's height**: `#fit` and `#grip` change no dimension of the
robot once the socket's root stops moving. In the design source it now passes — the figure comes
out 317.000 rather than 317.0535, and it stays there at any fit. Phase C measures the same thing at
the model.

## Carry the useful half of the old Session 1 into the new one

`experiments/session-1-layout-and-torso/` (**A**) was superseded on 2026-08-10 by the commit
that wrote `instructions/robot-guide/source/index.rst` (**B**) — *"Rewrite session 1 to start
from a design plan, and build it as a Sphinx page"*. B has had two test runs since; A has not
been touched since it was written. Before A is retired, four things in it have no counterpart in B.

**Its whole teaching half.** B has no `lesson-design.md` at all — no clock, floor, ceiling or
rubric. Worth carrying across specifically:

- **"Draw it badly on purpose."** The instructor draws visibly crooked, then the room watches
  geometry move as constraints land. B has no instructor guidance of any kind, and this transfers
  straight to B's torso rectangle.
- **The three across-the-room assessment questions**, especially the third — *can the student say
  what would happen if one driving line moved?* B's "Change one number" section already performs
  that demonstration with no assessment framing around it.
- **The ceiling items** — Equal instead of separate dimensions, deliberate over-constraint to find
  the redundant one, driving dimensions from a variable.

**Construction geometry, which B assumes and never teaches.** A teaches it — `q` to toggle, `v`
Vertical, `h` Horizontal. B uses none of them, but `index.rst:309` says *"this is the argument for
the rule about construction geometry: do not draw a construction line where a real edge already
is."* Either teach the rule in B or drop the sentence that depends on it.

**Two warnings B lacks.** `shift+s` is **Point**, not Sketch — A warns, B just says to use the
toolbar. And "the block only grew one way — Symmetric was not ticked", which is in A's failure
table and missing from B's fourteen-entry one.

**The drag test as a habit.** A makes it a ritual: every sketch, every time. B drags a corner at
Step 2 and mentions blue endpoints, but never establishes it.

**Do not carry A's "Tab, not Enter" note.** B's second test run found dimensions need **Enter** —
Escape silently discards the typed value, which produced a 34.8 mm torso instead of 48. Tab applies
only inside feature dialogs. A's version is wrong.

## Coverage and correctness

- **Nobody has walked the click-path.** A script did. Pacing, wording, whether a twelve-year-old
  finds the Depth box — all unknown until someone runs a session.
- **Steps 3 onwards are photographed by opening features for editing**, not by creating them. Same
  dialog, same real values, but never a half-finished selection. This is the main thing to revisit
  if the middle sessions feel thin. Steps 1 and 2 are driven click by click.
- **The fillet radii are the fragile dimensions.** A radius has to fit the face it rounds, so the
  guide's claim that any size of figure works with these steps is only tested at one size. Either
  test the range or stop claiming it.
- **Mirror is unverified and unused.** The build does everything twice by hand, which is the wrong
  lesson; Mirror is currently parked as a stretch task. Its `command-id` is known
  (`SKETCHMIRROR`, `mirror`), its dialog is not.
- **The appearance menu wording is unverified.** The highlight matches `[Aa]ppearance` loosely
  because the exact item text was never read.
- `README.md`'s reference-model links are still `_TODO_`. The document IDs are in
  [`project.md`](project.md).
- **`docs/` needs its second page.** The first is
  [`what-you-are-building.md`](../docs/what-you-are-building.md) — the robot, Onshape's
  vocabulary, and versions, written for a student and clean at grade 8. What is not covered
  yet: anything about printing the parts, and anything about the assembly.
- **Session 1's lesson-design exists now**, at
  [`../instructions/robot-guide/lesson-design.md`](../instructions/robot-guide/lesson-design.md),
  and it carries the teaching half salvaged from the old session. Two salvage items still belong
  in `source/index.rst` rather than the plan: the *Symmetric was not ticked* failure, and the
  decision on construction geometry — the page refers to a rule about it at line 309 and never
  teaches it.
- **The constitution review's 19 findings are unremediated.** The adversarial review ran on
  2026-08-12 against `e8508af`, `fffec7c` and `cb5ab99`, and nothing was applied — the last
  commit touching `constitution.md` or `.parts/` predates it. The findings, the three I contested,
  how a second round ruled on them, and the outstanding list are in
  [`2026-08-12-constitution-review-report.md`](2026-08-12-constitution-review-report.md). The
  cheapest item on that list is re-wrapping `constitution.md` to 100 columns: while it is red,
  `ninja check` never reaches the spelling and reading-level gates.
- **The build videos are a record of a build, not a lesson.** `instructions/robot-guide4/` now
  links a clip at the end of each block of steps, captured by `rec.py` as CDP event frames while
  the harness drove Onshape. They are honest and they are not yet teaching: the pointer jumps
  rather than moves, values appear in boxes already fully typed, there are long dead waits where
  the harness was blocked on a server round trip, and nothing names what is happening or why.
  The link text says *similar steps* because that is all they are — the clip covers the same
  ground as the pictures above it, not the same clicks in the same order. What would make them
  work for a student: a pointer that travels and pauses where a hand would, typing shown as
  typing, the dead time cut, a caption or a title card per step, and a decision about whether
  each clip covers one step or one section. Until then the pictures are the instruction and the
  clip is a second look. See
  [`experiments/runs/2026-08-19-run8p1/register.md`](experiments/runs/2026-08-19-run8p1/register.md).
- **The reviewer pass has not been run.** A different review from the one above, and Phase 3 of
  the reorganization. A reading pass, not a script: **Fable** reads the repository's prose —
  `.claude/rules/`, `.claude/skills/`, `instructions/`, `docs/`, `.docs/` and both READMEs — and
  flags three things.
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
- **Every drawing generator is labeled `controlling`, `illustrative` or `superseded`**, in its own
  opening, with the version or date it belongs to. `make_plans.py` controls; `make_brief_sheets.py`
  and `hinge_spring.py` illustrate; the hinge review's three generators and the three studies under
  `experiments/sketches/` are superseded, each frozen at its own snapshot. The rule is
  [`../memory/deciding-is-never-done.md`](../memory/deciding-is-never-done.md) and the argument
  behind it is [`2026-09-16-derived-figures.md`](2026-09-16-derived-figures.md). What is still open
  there: a verdict that fails a check rather than sitting in a heading.
- **The task numbers are closed at #217, and what each one meant is in
  [`tasks.md`](tasks.md).** They were coined in a Claude Code task store keyed by session id, which
  is not in git; the repository cites them 107 times across 42 files. New work carries a dotted
  identifier name instead, written into the plan that will do it, and the move is recorded in
  [`2026-09-16-tasks-into-the-repo.md`](2026-09-16-tasks-into-the-repo.md).
- **Four Stage 5 teaching routes lost their home when the limbs became cylinders.** `#limbD` is
  12 and every limb is a Ø12 cylinder, so the limb rows in the Stage 5 build order —
  [`robot-build-plan.md:609`](robot-build-plan.md) and `:611` — no longer describe a part anyone
  will model. What that costs, against the coverage table:
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
- **Two constitution amendments are pending, both from the same failure.** Read
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
- **Session 1's two documents are reconciled.** `instructions/robot-guide/` supersedes
  `experiments/session-1-layout-and-torso/` — what to salvage from the older one is above, under
  *Carry the useful half of the old Session 1 into the new one*.

## Pipeline improvements worth making

- **`show_result` reopens the document** to get a known camera, which costs a 16 s page load each
  time. Correct, but it is most of the runtime of a capture run. A cheaper deterministic camera
  would pay for itself.
- **Onshape rate-limits hard.** A burst of feature writes earns a 429 on that endpoint family that
  took over an hour to clear on one occasion, blocking all capture work. Writes are paced now, but
  do not plan a working session around many rebuilds.
- **Handling a 429 is written, and the history says why it took eight tries.** Done on 2026-08-28.
  The rule is [`onshape`](../.claude/skills/onshape/SKILL.md) § *Read what a refusal says before
  waiting on it*; the mechanism is `api()` in
  [`../src/stickbot/onshape_session.py`](../src/stickbot/onshape_session.py), which now keeps the
  response headers, honors a short `retry-after`, and raises at once rather than spending a ladder
  to discover the answer is hours away.

  **Verified against a live 429 on 2026-08-28.** `features` answered `retry-after: 522` with
  `x-rate-limit-remaining: 0`, and `api()` raised in 0.10 s naming both, where the old ladder
  would have spent 110 s and five requests to reach a message that was wrong on two counts. In
  the same pass `bodydetails`, `parts` and `assemblies` answered 200 with 486, 500 and 1000 calls
  left, which is the per-family limit measured from the healthy side. The sweep of what came
  before:

  - **08-10, `5263ee7`, the client's `api()`.** Assumed one kind of 429, minutes long, and
    laddered 5 s to 480 s, 955 s in all. It was the first handling of any kind: before it a 429
    read as a `DELETE` that quietly did nothing and a feature list with no `features` key.
  - **08-10, `b5d2aec`, the same function.** Cut the ladder to 5, 15, 30, 60 because *"an
    unbounded backoff turns a rate limit into something indistinguishable from a freeze"*. The
    reasoning holds. The message did not: it hard-coded *"account-wide on the feature endpoints
    and clears in minutes"*, and that sentence is what every later reader believed.
  - **08-10, `be1b460`, `wait_and_capture.py`.** Polled every 60 s and gave up after an hour. A
    runner that waits, for a limit whose answer is a different route.
  - **08-10, `08a50d2`, the same runner.** Polled every 300 s and gave up after six hours, on the
    theory that the polling itself was holding the block open. Six hours does not outlast
    eighteen. Retired on 08-12 with the pipeline that used it.
  - **08-13, `60377ea`, `design-into-cad.md`.** Right, and complete: a daily quota, `retry-after`
    in the tens of thousands of seconds, counting down with the clock, one endpoint throttled
    while the rest answer, so move to the GUI. Prose only. It landed in `.docs/experiments/`,
    which the Constitution files as archive, and no code and no part changed.
  - **08-14, `013b57f`, `onshape-gui-howto.md`.** Took 83 s from the one end-to-end pair in run
    3's torso log and made it the recovery time. One measurement of the short mode, generalized.
  - **08-14, `905fff0`, the same file, hours later.** Corrected itself: two kinds, waiting inside
    a session worked neither time, plan a route that avoids `/features`. Still prose only.
  - **08-24, `15441c6`, tutorial 11's build log.** Backed off every time and it did not clear, so
    `featureStatus` was never read; the acceptance check fell back to looking for error badges in
    the tree frame.
  - **08-27, draft9p1p1 Phase C.** Measured all of it from scratch again, and re-planned a phase
    around never touching `features`.

  **The cause is not that nobody knew.** It was right in the tree on 08-13, fourteen days before it
  was measured again, and re-derived on 08-14. What failed each time is that the finding landed in a
  working note while the client went on asserting the opposite in the message it raised, and the
  client is what the next person read. A finding about a tool has to reach the tool.
- **Arc and circle have never been drawn from a script.** Rectangle and dimension have. Same shape
  of problem, and needed if more steps are to be driven click by click.
- **The browser profile lives in a session scratchpad**, so the login does not survive. Move it
  somewhere durable, or get an API key from `dev-portal.onshape.com` and stop depending on a
  signed-in window.
- Three stale Onshape documents can be deleted once nothing points at them — see
  [`project.md`](project.md).

## Future work — print orientation, and the edge treatments that depend on it

**Not adopted. Recorded because it blocked a decision we tried to take on 2026-08-11.**

We went looking for a standard fillet size for a 0.4 mm nozzle and found the question is not
answerable on its own. Every useful source qualifies its advice by which way the feature faces
on the plate:

- **Vertical corners are already filleted at about 0.2 mm** — half the nozzle diameter — whether
  drawn or not. Protolabs Network: *"Because FDM printing nozzles are circular, corners and
  edges have a radius equal to the nozzle size."* So nothing below ~0.4 mm is worth drawing.
- **Downward-facing fillets print badly** and want to be chamfers instead. Hydra Research: *"do
  not use downward facing fillets… they may come out with poor aesthetic/surface quality."*
- **Edges on the build plate want a 45° chamfer**, sized 0.3–1.0 mm depending on layer height.

Candidate numbers, if we ever adopt them: **0.5 mm × 45° for a cosmetic edge break, R1.0 as the
minimum drawn fillet, and nothing under 0.4 mm drawn at all.**

**Why it is not adopted:** "upward" and "downward" are properties of the print, not of the
model. Until each part carries a **declared print orientation**, an edge rule cannot be applied
— the same fillet is fine on one face and ugly on the opposite one.

**The bigger instance of the same problem is structural, not cosmetic.** A snap-fit tab flexed
about an axis parallel to the layer lines peels them apart and fails well below the calculated
strain; flexed within a layer it does not. That applies directly to the ball socket's four tabs
and to the hinge's sprung ears, and neither brief says which way up the part is printed. The
hinge report's 2.2 % ear strain and the socket's tab calculations both quietly assume the
favorable orientation.

**What adopting it would take:** a declared orientation per part, shown on the parts drawing;
edge treatments chosen per edge against that orientation; and the tab-bearing parts oriented so
their tabs flex in-layer.

Sources: [Protolabs Network](https://www.hubs.com/knowledge-base/how-design-parts-fdm-3d-printing/),
[Hydra Research](https://www.hydraresearch3d.com/design-rules),
[NExT Lab](https://ms-kb.msd.unimelb.edu.au/next-lab/3d-printing/design-guidelines),
[3DVerkstan](https://support.3dverkstan.se/article/38-designing-for-3d-printing).

## Decisions taken, worth not re-litigating

- **Highlights come from the DOM.** No pixel coordinates anywhere. This is what keeps the
  annotations correct across window sizes and Onshape's redesigns, and it was the single most
  useful decision in the project.
- **Every shot verifies itself.** A click that should select something is checked against Onshape's
  own measurement readout; a highlight target that is not on screen raises rather than quietly
  vanishing.
- **The builder only ever goes forwards.** Rebuilding the figure per step would be ~500 feature
  writes and a guaranteed rate limit; building forwards is 22.
- **Screenshots notice, measurements conclude.** See
  [`verification-lessons.md`](verification-lessons.md) — three wrong diagnoses in one session came
  from treating a surprising picture as evidence of its own cause.
