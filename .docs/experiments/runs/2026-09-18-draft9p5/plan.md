# draft9p5 — a full set of models built over the API, with the construction correct

**This draft builds every part again, over REST, so that one document holds the whole robot with
a feature tree that obeys every ruling made since the parts were last built.** What it hands on is
a model a brief can cite for how a part is made, not only for what shape it comes out.

## Why this draft exists

The survey of 2026-09-18 found the shape in good order and the construction scattered. Eight parts
live across three documents, none of the three was built after the rulings that now govern a
feature tree, and the newest construction of the one part that was rebuilt is unfinished. There is
no document a brief can point at and say *build it like this*.

## What changes about REST

draft9p4's plan ends its REST section with **Not the CAD**: every sketch, extrude, mirror, pattern,
derive, mate connector and variable was made in the GUI at the clicks a page would print, because a
page is written from the frames of a feature being made. This draft is not writing pages, so that
reason does not apply to it. REST builds the model here, and the guide's pages are written later
from a model that is already right.

## The rulings a construction is judged against

Each was settled after the model it now judges was published. None of them is a matter of taste and
none of them changes a shape.

| Ruling | Settled | Source |
| ------ | ------- | ------ |
| A variable feature keeps Onshape's title, `###name = #value` | 2026-09-08 | draft9p4 plan, *The variable naming rule* |
| A sketch stands on a face of the robot; a stock plane only where the sketch needs the torso's center | 2026-09-09 | draft9p4 plan, *What is settled before the take starts* |
| A variable is typed immediately before the first feature that reads it | 2026-09-11 | draft9p4 plan, *Variables arrive at the step that needs them* |
| `#ear` and `#backlash` are not declared, because nothing reads either | 2026-09-11 | the same walk |
| A connector is named for the joint it is, without the word *connector* | 2026-09-11 | draft9p4 plan, *What we do not know yet* |
| Every feature that is not a variable gets a typed name | task #138 | draft9p3 hinge fix |
| `relief slit` is the last feature on the blade | 2026-09-17 | [`../../../2026-09-17-reorg-drawings-and-notes.md`](../../../2026-09-17-reorg-drawings-and-notes.md) |

**The first of these is not a preference.** A student cannot type over a variable's title: the
Variable dialog has no rename pencil, the variable's tree row has no *Rename*, and `F2` on it does
nothing. All three were driven on 2026-09-09. A model carrying typed variable titles shows a state
no click path reaches.

## What is wrong with each construction available

### The hinge, and it is the only part whose construction has been compared

Measured 2026-09-18 from `/features` on both tabs.

| | `stickbot-draft9p1p6` at `F done - Phase F proved` | `stickbot-draft9p4-check`, workspace |
| --- | --- | --- |
| features | 46 | 38 |
| variables | 18 | 15 |
| variable titles typed over | 8 | 0 |
| variables before the first geometry feature | 18 | 1 |

- **draft9p1p6 has the finished shape and the older tree.** Its eight typed titles are `nose`,
  `ear`, `stub`, `stub_proud`, `bore_d`, `slit_h`, `rod_blade` and `rod_fork`. All eighteen
  variables sit in one block above the first sketch. It still declares `#ear` and `#backlash`. Its
  two connectors are `fork to robot connector` and `blade to robot connector`, carrying the word
  the ruling drops.
- **draft9p4-check has the newer tree and an unfinished fork.** Every one of its fifteen variables
  is on the template, and they interleave with the geometry rather than opening the tab. What it
  does not have yet is `fork arm outline`, `fork arm`, `combine fork parts` and both mate
  connectors, so its fork is two loose solids of 125 faces each where draft9p1p6's fork is one
  solid of 252. Its blade is whole and matches draft9p1p6's face for face.
- **Nothing is in draft9p4-check that is not in draft9p1p6.** It is a subset, built to newer rules
  and stopped part way.

So draft9p5 takes the shape from draft9p1p6 and the build order from draft9p4-check, and finishes
the fork.

### Every other part's construction is unexamined

**This is the largest gap in what is written here.** The survey compared shape across all eight
parts and compared construction on the hinge alone. `body`, `head`, `ball and socket`, `foot`,
`u limb`, `l limb` and `gripper` have not been read against the rulings above, and nothing here
should be read as saying they pass.

What is known about them is where they live and what is wrong with their **shape**:

| Part | Where the shape is | What is wrong with the shape |
| ---- | ------------------ | ---------------------------- |
| body | `stickbot-draft9p4` at `tutorial 8 - the foot` | nothing found |
| head | the same | nothing found |
| ball and socket | the same | nothing found |
| foot | the same | the tread grooves are closed voids inside the sole, and the sole renders smooth from below — task #215 |
| hinge, u limb, l limb | `stickbot-draft9p1p6` at `F done - Phase F proved` | nothing found |
| gripper | `stickbot-draft9p1p1` at `Recovery point` | the socket collar is Ø18 against the settled Ø15.6; the part predates the wall change |

Two open questions on the limbs were not measured by the survey and are not answered anywhere:
task #177, the blade losing a wedge per face at `#limbD` 34 mm and above; and whether `l limb`'s
rod reproduces volume the derived blade's arm already occupies, with `u limb` never checked at all.

### Two documents come with a warning

- **`stickbot-draft9p1p6` is sound, and the survey said otherwise for a few hours.** Its `hinge`
  and `u limb` first read at 258 and 24 faces against the version's 510 and 270, and the survey
  concluded the workspace had lost the fork. Re-read the same day, both match the version exactly,
  every feature reports OK, and the rollback bar is at the bottom in both. Read a tab twice and
  require the two to agree before drawing anything from one of them.
- **`stickbot-draft9p4-check` holds work draft9p4's plan did not put there.** Its logs say
  tutorials 4, 5, 6, 8 and 9 were *built* in it, where the plan reserves it for `audit.page`. The
  consequence for draft9p4 is task #221; the consequence here is that the check document is a real
  source of construction and not a copy of the build document. Its `head` differs from the build
  document's, its eyes 1.5 % oversize — task #222 — and its `hinge` is a different joint entirely.

## What is not yet written

The declaration, the phases, the gates claimed, how a part is proved, and where the guide's pages
come from afterwards. This file currently holds only what the survey established about the source
material.
