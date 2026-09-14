# Getting the design into the CAD

After run 3 we changed the initial sketches and then the briefs. The design moved and the CAD did
not. The sketches were re-drawn, the shoulder was angled, the
hinge was rebalanced, and the briefs were corrected against measurement — none of which reached a
part studio. Run 4 copied run 3's geometry, added mate connectors, and assembled it; every sketch
and extrude in it is still run 3's. See
[`runs/2026-08-13-run4/build-notes.md`](runs/2026-08-13-run4/build-notes.md).

This file is the plan for closing that gap. It is deliberately two sections in one: a **high-level
plan** that does not change, and a **low-level plan** whose steps are chosen while the work is
running, from what each part turns out to contain.

It is the procedure, not the checks. [`build-and-verify.md`](build-and-verify.md) is the wave
cycle, [`build-briefs/README.md`](build-briefs/README.md) is what a part is held to, and the
Constitution governs sessions, versions, and branches.

## Done means

Every number and every shape the sketches and the briefs assert is **either in the CAD or written
down as an unresolved conflict**, and the assembly is rebuilt from the repaired parts.

We examine each part and the assembly in detail until we understand what every one of its features
is. We confirm from those features that it looks like the part the sketches and briefs asked for,
and specifically that it matches the developmental sketches the briefs were constructed from. We
measure the dimensions and confirm they match the briefs and the initial sketches.

For the assembly we confirm that its dimensions, orientation, parts and mates are right against
the briefs and the initial sketches.


---
# The high-level plan

## Authority

When two sources disagree, this is the order, and it does not get renegotiated per part.

| Rank | Source                                           | What it settles                                                                                                      |
|------|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| 1    | [`sketches/`](sketches/), [`build-briefs/`](build-briefs/), our evaluation of if the robot assembles and articulates per the design intent | pose, station, which way a part faces, what the figure looks like, each part's own numbers and its acceptance checks |
| 2    | the CAD | **nothing** — it is the thing under test |


**Sketch and brief can disagree with each other**, and when they do neither wins automatically —
that is a conflict for you to resolve in a way that achieves our design intent.

**They share a rank deliberately.** Ranking them would make one of them unchangeable, and an
unchangeable source turns every conflict into work squeezed around it. The figure's height is the
worked example: while 150 mm was a requirement the design bent to reach it, and once the parts
were allowed to fall where the joints put them the problem got smaller. No part of the design
intent is sacred. **How much work a constraint is causing is evidence about the constraint**, not
only about the work.

**A brief row marked *measured* or *built* is a record, not a target.** Some rows came back out of
the CAD rather than out of the design — the foot's collar reads `5.5 → 7.35 | plan, then built`,
because the collar's proud length is set by the plate and the foot cannot reach 5.5. Repairing to
a row like that models backwards from an accident, or chases a number the part cannot hold. Read
the **Source** column first: `plan` and `derived` are targets, `proposed` is a target nobody has
challenged, and `built` and `measured` are history.

## The phases

Mark each phase 'Done.' as completed.

0. **Copy.** Done. Nine documents copied to run 5, recorded in
   `runs/2026-08-13-run5/run5-documents.json`. All of this work happens in run 5.
1. **Gather a list of changes.** Done. `git diff 5ff5f3d..HEAD` over the briefs and the
   sketches, written to `runs/2026-08-13-run5/changes-since-run3.md`.
2. **State the target.** Done. `instructions/robot-guide/make_target.py` writes
   `runs/2026-08-13-run5/target.json` from **both** sources: every design constant out of
   `make_plans.py` by introspection, and every numbers-table row out of the briefs by parsing
   — 91 numbers, the figure's stations, each joint in the frame its part is modeled in, and 64
   brief rows carrying their **Source**, classified target against record. Nothing is typed in,
   so neither half can drift. Briefs with no numbers table are named rather than dropped.
3. **Audit.** Done. All six parts measured and rendered in four views;
   `runs/2026-08-13-run5/audit.md` carries the deltas classified by route, and
   `measured.json` the raw faces and solids. Two parts need no repair.
4. **Deconflict.** Done. `runs/2026-08-13-run5/deconflict.md` — the hinge stack checked
   surface by surface across both halves, four things resolved, two registered.
5. **Repair.** Done. S1 through S5, each measured on solved geometry and written up in
   `runs/2026-08-13-run5/repairs.md`.
6. **Evaluate the parts.** Done. The three axes below, on the parts, in
   `runs/2026-08-13-run5/evaluation.md`.
7. **Re-assemble.** Done. Fourteen instances from `run 5` versions, thirteen mates, all `OK`,
   published as the `run 5 assembled` version of `lesson-run5`.
8. **Evaluate the robot.** Done. Same file — every station matches `make_plans.py`.
9. **Register.** Done. `runs/2026-08-13-run5/register.md`.

Run the phases in order, in this top-level agent, which does all of the CAD itself. It may give
analysis, research, evaluation and thinking to sub-agents.

**Do not stop between phases.** Finishing a phase is not a place to report and wait — mark it
Done, commit, and start the next one in the same breath. The run goes from phase 0 to phase 9
without being told to continue. This holds whether or not anyone is watching: an unattended run
and an attended one differ in who is reading, not in whether the work proceeds.

There is no question worth stopping for, because there is somewhere else for every question to go.
A conflict goes in the register with what it turns on and what the options cost; a decision that
is not mine gets its cheap answer written down and the work routes around it. Stopping to ask
converts a question that costs a paragraph into one that costs the rest of the run.

## The three evaluation axes

The user's three questions, and how each is actually answered rather than asserted.

| Axis | Answered by |
| ---- | ----------- |
| **Matches the sketches** | station and pose measured off the assembly — joint centers, overall height, arm span, which plane each part's length runs in — compared against `make_plans.py`'s own numbers, not against a reading of the drawing |
| **Matches the briefs** | each brief's *Acceptance checks* section, performed and recorded per part. They exist for this and were written to be measured, not inferred |
| **Works as a printable robot** | the three sub-axes below |

"Works" is the one that has no checklist yet, so it gets one:

- **Printable.** No wall below one nozzle width anywhere in the part; overhangs and bridges
  identified per part with the print orientation named; no feature that only exists in the model
  because the model has no gravity.
- **Assemblable.** Every ball can enter its socket — which means every socket collar is slit —
  and every press fit has an interference that is deliberate and stated. A joint that cannot be
  put together once is a failure even if it measures perfectly.
- **Functional.** Each joint reaches the range the sketch draws it at without fouling the part
  next to it, and each spring feature sits far enough below PETG's yield to survive a print that
  came out thick. The ranges and the margins are in the briefs; this axis is where they get
  checked against the assembled geometry rather than against a hand calculation.

## What gets resolved and what gets written down

**I resolve** a conflict when all three hold: the brief row is a target rather than a record, the
change moves no driving variable, and the fix does not trade one stated goal against another.
Slitting a collar, changing a thickness the brief already settled, rebuilding a feature to numbers
that are already derived — those are work, not decisions.

**I write down** — and do not decide — anything that moves a driver (`#torsoH`, `#hipHalf`,
`#legX`), anything where the sketches and the briefs disagree with each other, anything that
changes the part count or introduces handedness, and any fix that buys one axis by spending
another. Each entry carries what is known, what it turns on, what the options cost, and the cheap
answer, per the unattended rule in [`build-and-verify.md`](build-and-verify.md).

**A third case exists and has bitten once already:** work I did not attempt, recorded as though it
had been a decision. It is neither resolved nor a genuine conflict, and calling it parked is a
false record. If it was not attempted, the register says so in those words.

## Where the work lives

Repairs go into the **run 5 documents' workspaces**. Run 4 is left alone: it is the record of what
an assembly built from unrepaired parts measured, and run 5's instructions are what the teacher
and student will follow, so run 5 is the copy worth having.

---

# The low-level plan

The high-level plan is fixed. Everything from here is chosen at audit time, because what a repair
costs depends entirely on how the feature that needs repairing was built — and that is not known
until it is read.

## Repair routes

Every delta the audit finds is classified by the route that can fix it. Which route applies is a
property of how the part was built, not of the delta, and it is read off the feature tree.

| Route | Applies when | Cost |
| ----- | ------------ | ---- |
| **Variable** | the number is driven by a variable in the studio | one edit, propagates |
| **Feature parameter** | the number is a feature's own parameter — an extrude depth, a fillet radius, a pattern count | one call per feature |
| **Sketch entity** | the number lives in a sketch's geometry or its dimensions | the sketch's entities and constraints are rewritten together |
| **New feature** | the geometry does not exist at all, as with a collar that was never slit | insert at the right point in the tree, not at the end |
| **Rebuild** | the construction cannot express the target — a solid blade that has to become two tabs | delete and re-author the affected span |
| **GUI** | the API route fails, or the edit is faster by hand | screenshot it; run 5 needs the pictures anyway |

## The steps

Written by phases 1–4 and worked through in phase 5. Reasoning is not repeated here — each step
points at the file that carries it. Mark a step **Done** as it completes.

### S0 — prove the sketch-entity route — **Done**

Proved on `ball-socket-run5`, which no assembly instance references. The route works, and it is
not where it looks like it should be.

A sketch is a `BTMSketch-151`. Its `parameters` carry only `sketchPlane` and `disableImprinting`;
the geometry lives in the feature's own `entities` and `constraints` fields, in **meters**.

**Edit the dimension constraint, not the entity.** Setting `entities[0].geometry.radius` from
0.0047 to 0.0055 answered 200 and read back 0.0055 — and moved nothing, because a `DIAMETER`
constraint drives that circle and the solver puts the geometry back. Setting that constraint's
`length` expression from `9.4 mm` to `11 mm` moved the volume 2305.3461 → 2432.2462, and
restoring it came back to 2305.3461 exactly.

**So the entity's stored radius is stale cache, not the solved value**, and reading it back proves
nothing. This defeats read-back-plus-200 as a check: both passed on the edit that did nothing.
Only the measured quantity caught it. Every step below measures something that must move.

### S1 — torso: the shoulder stud and the neck boss — **Done**

Per [`audit.md`](runs/2026-08-13-run5/audit.md). Hardest, so it goes first. Built and measured in
[`repairs.md`](runs/2026-08-13-run5/repairs.md), which also carries the four findings. S1e closed
the other way: the neck boss cannot buy the tilt it exists for, so it is not built.

- **S1a** Shoulder stud on a doubly-rotated axis: 53° below horizontal, 30° toward the front,
  rooted on the side face at x = ±18, z = +20. The part has no plane for this — it needs a mate
  connector or a construction plane before it needs a sketch.
- **S1b** Ø8 boss, 8 long, coaxial with the stalk; then Ø3 stalk for the last 5; then the Ø6 ball.
  Ball lands at (±24.775, −3.912, +9.618).
- **S1c** Cut the boss flush where it crosses the torso's top face at z = +24.
- **S1d** Mirror to the left shoulder — mirror the part, not the feature.
- **S1e** Neck boss Ø12 on the top face, on the axis. New feature.
- **S1f** Measure the least clearance between the upper arm and the torso across the full
  ±37.09° swing. This is the check the geometry exists to pass.

### S2 and S3 — the two limb halves, together — **Done**

Measured in [`runs/2026-08-13-run5/repairs.md`](runs/2026-08-13-run5/repairs.md). S3c turned out to
be two features rather than one, and that record says which.

They meet inside one joint and the stack is checked in
[`deconflict.md`](runs/2026-08-13-run5/deconflict.md). Repairing one alone leaves a joint that
cannot close, so neither is Done until both measure.

- **S2a** `limb-socket-clevis`: slot half-width 1.8 → 2.8, so the ear becomes 3.2.
- **S2b** Remove the ear's outer planes at ±3.0 and ±2.5 — the ear's outer surface is the Ø12
  cylinder and has no outer plane at all.
- **S2c** Round ends r5.81 → r6, putting the fork tip at z = −30.
- **S2d** Stub inner face ±1.0 → ±2.0, keeping it 0.8 proud of the new ear face.
- **S2e** Slot root to z = −13, which is 11 behind the pin axis.
- **S3a** `limb-blade-ball`: blade half-thickness 1.5 → 2.5.
- **S3b** Detent valley floors ±1.05 → ±2.05; land follows the blade face to ±2.5.
- **S3c** Round end r5.81 → r6, blade tip at z = +6, blade's limb ending at z = −10.
- **S3d** The slit: 0.8 wide, 16 deep, down the blade's middle, open at the tip, leaving two 2.1
  tabs. New feature.

### S4 — foot — **Done**

Measured in [`runs/2026-08-13-run5/repairs.md`](runs/2026-08-13-run5/repairs.md).

- **S4a** Re-sketch the outline with its length along **Y**, symmetric about the Right (YZ) plane
  by `Symmetric` constraint rather than by dimensioning both sides.
- **S4b** Four relief slits, 0.8 wide, cut through the collar for its **whole 7.35** proud length
  — the slit follows the collar it is cut into, not `COLLAR_L`.

### S5 — the brief that is wrong, not the model — **Done**

- **S5a** `hinge.md` says run 3 built 13 detent valleys. It built 24 a side, and `STEP` 15 divides
  360 into exactly 24. Correct the brief.

### S6 — versions — **Done**

One named version per repaired part, cut after its measurements pass. The assembly cites versions,
never workspaces — so the two parts run 5 did not touch, the head and the hand, get one as well.
All six are named `run 5` and their ids are in
[`runs/2026-08-13-run5/run5-documents.json`](runs/2026-08-13-run5/run5-documents.json).

### S7 — assembly — **Done**

Rebuilt from the new versions and re-mated: thirteen mates, all `OK`. The foot's 90° turn came out,
because S4a puts the part's length on the axis the assembly wanted. The shoulders needed two new
mate connectors, placed in the assembly rather than the torso. Measured in
[`runs/2026-08-13-run5/repairs.md`](runs/2026-08-13-run5/repairs.md).

### S8 and S9 — evaluate and register — **Done**

The three axes on the parts and then on the robot are in
[`runs/2026-08-13-run5/evaluation.md`](runs/2026-08-13-run5/evaluation.md), and what was resolved,
what was not, and what was never attempted are in
[`runs/2026-08-13-run5/register.md`](runs/2026-08-13-run5/register.md).

## What the API is known to do

Stated precisely, because it was once asserted here more broadly than it had been tested.

| Operation | Endpoint | Status |
| --------- | -------- | ------ |
| add a feature | `POST .../partstudios/d/{d}/w/{w}/e/{e}/features` | **proven** — run 4's mate connectors |
| update a feature's parameters | `POST .../features/featureid/{fid}` | **proven** on an extrude — see below |
| rewrite a sketch's entities and constraints | same endpoint, different payload | **proven** — see below |
| insert a feature mid-tree | `POST .../features/rollback`, then add, then move the bar back | **proven** — S1 put four features between a revolve and its mirror |
| read every feature's parameter spec | `GET .../featurespecs` | **proven** — how S1 learned `transform` without opening the GUI |
| delete a feature | `DELETE .../features/featureid/{fid}` | proven on assembly features; the id must be percent-encoded, because ids contain `/` |
| read every face's surface, radius, axis, area and box | `GET .../parts/d/{d}/w/{w}/e/{e}/partid/{p}/bodydetails` | **proven** on all six parts, and **not rate limited** while `featurescript` was 429 — it answered most of the acceptance checks |

**A feature is always added at the rollback bar**, and the bar has its own call. `rollbackIndex`
passed in the add body is ignored without complaint — the feature lands at the end and the answer
is still `200`.

The update test, run on the `ball-socket` study document because no assembly instance references
it: the `Socket collar` extrude's depth was round-tripped unchanged, then driven 1.35 → 9.5, then
restored. All three answered `200`, the parameter read back changed, and total solid volume moved
2305.3461 → 2681.2635 → 2305.3461 mm³. The study is back where it started.

**A `200` is not the test.** The first attempt measured overall height, which sat at exactly 150.0
before and after because a reference body sets it — the call looked successful and proved nothing.
Every repair re-reads the changed parameter *and* measures a quantity that must move.

### Sketches

A sketch is a `BTMSketch-151`. Its `parameters` carry only `sketchPlane` and `disableImprinting`;
the geometry lives in the feature's own `entities` and `constraints`, in **meters**.

**Edit the dimension constraint, not the entity.** Setting `entities[0].geometry.radius` from
0.0047 to 0.0055 answered 200 and read back 0.0055 — and moved nothing, because a `DIAMETER`
constraint drives that circle and the solver puts the geometry back. Setting that constraint's
`length` expression from `9.4 mm` to `11 mm` moved the volume 2305.3461 → 2432.2462, and restoring
it came back to 2305.3461 exactly. **The entity's stored radius is stale cache, not the solved
value**, so reading it back proves nothing — both checks passed on the edit that did nothing.

A whole profile can be replaced in one call, entities and constraints together. Two things bite:

- **A line's stored `pntX/pntY/dirX/dirY` is the infinite line; the ends come from the
  constraints.** Author the loop and let it solve.
- **A distance constraint carries a side.** Copying one and swapping which end it measures from
  put a line 16 mm from where it was asked to go, and the sketch still solved, and every feature
  still read `OK`. It was the region's *area* that gave it away.

## Building it through the GUI instead

The feature endpoints are on a **daily quota**, and S1 spent it. `GET` and `POST` on `.../features`
answer `429` with `retry-after` in the tens of thousands of seconds and `x-rate-limit-remaining: 0`,
and that counter runs down with the clock rather than resetting on a retry — so backing off inside
a request does nothing. Only that endpoint is throttled: `featurescript`, `massproperties`,
`shadedviews` and the document endpoints all still answer `200`, **so the build moves to the GUI
and the checking stays exactly where it was**. Nothing about the standard of proof changes.

The app is driven on 9223 through Playwright over CDP, the same connection the REST calls use.

- **The feature list's context menu is the whole toolkit.** It carries `Rename`, `Edit…`,
  `Suppress`, `Roll to here` and `Delete`. Two things hide it: it only opens on the row's
  `span.os-list-item-name`, and it does not open at all while a feature dialog is up — the
  right-click is swallowed and the list looks like it has no menu.
- **The rollback bar cannot be dragged.** `div.ns-list-item-rollbackbar` has no event listeners at
  all; its holder has `click` and feature rows have `click`, `dblclick`, `mousedown`. Every
  synthetic drag on it fails while looking like it worked, because the feature list and the parts
  list share a splitter that resizes under the same gesture. **`Roll to here` on the context menu
  is the way to insert mid-tree.**
- **Read a dialog by what its controls say, not by where they sit.** Ticking one option reflows
  everything below it, so a coordinate captured before a click is wrong after it. Checkboxes are
  `label.os-param-checkbox`, numbers are `input.os-param-number`, and the icons are `use` elements
  keyed by href — `#svg-icon-flip-direction` beside the end-condition dropdown, and
  `#svg-icon-ok-button` to accept. Some carry `href` and some `xlink:href`; read both.
- **"Direction" does not mean reverse.** In Extrude it opens a query for a custom direction entity,
  and leaving it empty puts the feature in error. Reversing is the flip icon by the dropdown.
- **A dialog does outlive the session that opened it.** An earlier note here said the opposite. A
  sketch stayed open across a dozen reconnections while it was drawn, dimensioned and accepted, so
  a step can be taken and then read off a screenshot before the next one. What does not survive is
  a half-typed value: `Escape` closes the field and leaves the dimension at its old number.

Drawing a sketch, rather than editing a dimension in one, adds these:

- **Pick the model out of the way first.** Hide the part and any construction plane whose edge-on
  trace lands near a sketch line. Nothing in a sketch can be selected by name, so an ambiguous
  pixel is an ambiguous pick, and the tree tells you afterwards what you actually got.
- **A sketch has no axis of its own to select.** The vertical line through the origin is the
  **Front plane's trace**, and that is what a `Symmetric` constraint ends up mirroring about — which
  is the right answer here, because the Front plane *is* the blade's mid-plane.
- **The visibility eye is only in the page while its row is hovered.** Hover the row, then click
  `span.ns-visibility-icon`. Without the hover the element does not exist and the click times out.
- **An under-constrained sketch moves when you drive one of its dimensions.** Setting the slit's
  root to 10 shifted its free sides from ±3.46 to ±2.60 and its free top with them. Re-read
  coordinates from a fresh screenshot after every dimension, not once at the start.
- **A dimension between the rectangle's two sides came back with no field at all**, twice, from two
  different pick points; the same two lines each took a dimension against the Front plane's trace
  on the first try, plane picked first. With `Symmetric` already holding, one half-width against
  the trace is enough.
- **`has_text` matches a substring.** Asking for `Limb` opens `Limb section`. Match the whole name.

### Everything a repair is checked against must be measured

Nothing above is trusted from a status. The `200`, the parameter read-back, and a tree of `OK`
feature states have each passed, separately, on a change that moved no geometry. Every step
measures a quantity that must move.

## Order of work

1. **Prove the sketch route first**, on a study document, before any real repair depends on it.
   This is not "do the easy work first" — it is one throwaway experiment that decides whether
   most of the repairs are API edits or GUI work, and it is cheap only while nothing rides on it.
2. **Hardest first.** Solve the hard thing while the clock and the options are both open, so that
   easy work done early does not constrain it.
3. **Joint-carrying parts before joint-consuming parts.** A socket or a hinge that changes moves
   every part that mates to it; a part that only carries a joint moves nothing.
4. **The assembly after all of them**, never in the same sitting as a part it assembles.

## Checkpointing

Each part is a checkpoint: version cut, notes appended, register updated, committed. The work must
survive being stopped between any two parts, because it will be.

## Nothing stops the run

Every phase runs to its end, every step in it, on every part. A finding is recorded and the work
continues. **It never ends a step, a part, or the run.**

This is not a tolerance for sloppiness, it is the opposite. Stopping early is a judgment about
what "done" is worth, made by whoever is holding the tools, and it is the one judgment this plan
does not delegate. A robot whose parts collide is an acceptable outcome when the collision is
written down and everything else was carried through and checked. An audit that halted at its
first finding is not, because the problems it never reached are invisible, and nothing in the
record shows that nobody looked.

Run 4 is the worked example: three fixable defects found, the bar judged unreachable, the
remaining parts never examined — so what else is wrong with them is still unknown.