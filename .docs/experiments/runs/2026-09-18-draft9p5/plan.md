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

### Every tab measured against the three rulings a record can answer

The nine construction records on disk were scored on 2026-09-18. `body`, `head`, `foot`, `gripper`
and the assembly come from draft9p3's `reference/`, which reads draft9p1p1; the four joint tabs come
from draft9p4's `reference/`, which reads draft9p1p6.

| Tab | Features | Variables | Titles typed over | Longest run of variables | Names still saying *connector* |
| --- | -------: | --------: | ----------------: | -----------------------: | ------------------------------: |
| `body` | 33 | 8 | 0 | 8 | 8 |
| `head` | 26 | 12 | 0 | 12 | 0 |
| `foot` | 24 | 13 | 0 | 10 | 0 |
| `gripper` | 15 | 8 | 0 | 8 | 0 |
| `ball and socket` | 14 | 5 | 5 | 5 | 0 |
| `hinge` | 46 | 18 | 8 | 18 | 2 |
| `u limb` | 9 | 0 | 0 | 0 | 0 |
| `l limb` | 9 | 0 | 0 | 0 | 0 |
| assembly | 13 | 0 | 0 | 0 | 0 |

- **Six tabs open with a block of variables**, 61 rows in all, where the ruling types each one
  immediately above the first feature that reads it. Every part except the two limbs and the
  assembly fails this, and the two limbs pass only because they declare none.
- **Two tabs have typed variable titles.** `ball and socket` has `stalk`, `slit`, `slit_in`,
  `slit_d` and `slit_out`; `hinge` has `nose`, `ear`, `stub`, `stub_proud`, `bore_d`, `slit_h`,
  `rod_blade` and `rod_fork`. Thirteen rows a student cannot reproduce.
- **Ten mate connector names still end in the word the ruling drops.** Eight on `body`, two on
  `hinge`. The column counts names, not connections.

**Two Onshape things are easy to read as one, and only one of them is a mate.** A `mate` is an
assembly constraint joining two instances; there are **13**, all in the `stickbot` assembly, and
they are the robot's thirteen joints — neck, two shoulders, two elbows, two wrists, two hips, two
knees, two ankles. A `mateConnector` is a coordinate system placed on a part in a Part Studio;
there are **23** across the eight parts. It is not a joint and not a mate. It is where a mate will
later attach, or an axis for a pattern.

The 23 do not reduce to the 13 and are not meant to. A joint needs a connector on each of the two
parts it joins, and several connectors are not joint ends at all: `axis for circular patterns` on
the hinge is a pattern axis, and `socket mount point`, `mate for fork` and `mate for ball stud`
mark where a derive or a transform lands.

**That split is what the naming ruling turns on.** A connector that is a joint end takes the
joint's name — `neck`, `left shoulder`, `elbow end`. A connector that marks a placement takes
`mate for …`. Neither takes the word *connector*, because the feature list already says what it
is.
- **No tab anywhere carries a default feature name.** That ruling already passes, so draft9p5 has
  to keep it rather than fix it.

The two rulings a record cannot answer — whether each variable sits above its first reader, and
whether each sketch stands on a face — need the expression walk and the plane queries, and they are
Phase A work rather than a table.

### The hinge, where two constructions exist and neither is finished

`stickbot-draft9p4-check`'s `hinge` was built to the newer rules and stopped part way: all fifteen
of its variables are on the template and interleaved with the geometry, one before the first sketch
rather than eighteen. What it lacks is `fork arm outline`, `fork arm`, `combine fork parts` and both
mate connectors, so its fork is two loose solids of 125 faces where draft9p1p6's is one of 252.

**So the hinge takes its shape from draft9p1p6 and its build order from draft9p4-check.** Nothing is
in the check document that is not in draft9p1p6; it is a subset built to newer rules.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p5` |
| `document` | `stickbot-draft9p5`, created empty |
| `parent` | `draft9p1p6` for the four joint tabs' geometry, `draft9p1p1` for `body`, `head`, `foot`, `gripper` and the assembly, `draft9p4-check` for the hinge's build order |
| `from` | nothing. Every feature is added to an empty document |
| `builds` | `robot sizes`, `ball and socket`, `hinge`, `body`, `head`, `foot`, `u limb`, `l limb`, `gripper`, and the `stickbot` assembly |
| `by` | REST, for every feature |
| `gates` | *Model inspected* and *Recovery point* — proposed, not agreed |
| `not claimed` | *Steps reproduce*, *Names are real*, *Links resolve*, *Floor & ceiling*, *Reading level* |

**Two gates, and the two are the whole of what a CAD build can close.** *Model inspected* is
Ring 2 and *Recovery point* is the named version at the end of each tab. The other five ask for
something this draft does not produce: *Steps reproduce* and *Reading level* need written steps,
*Links resolve* needs a link, *Floor & ceiling* needs a session, and *Names are real* checks that a
tool, menu or field name matches Onshape's UI verbatim, where a REST build opens no menu and fills
no field. The API rejects a wrong `featureType` outright, which is a stricter check than a gate and
arrives sooner.

**Prose style and Spelling are not on either list.** They are not run-scoped: prose style binds
every word committed to this repository, and `ninja check` runs over the whole tree on every
commit. This draft's `register.md` is held to both, the same as everything else. Claiming them here
would imply they are optional elsewhere.

**`from` is deliberately empty.** Every draft since draft9p1 branched the one before it and
inherited its tree along with its shape. That is how thirteen typed variable titles survived four
drafts. A document built from nothing cannot inherit a defect.

## Phase A — settle what cannot be measured from a record

Before any feature is added. Each of these is a read, and each writes its answer into
`reference/` beside the records already there.

- **Walk every expression** in `robot-sizes.features.json` and each tab's, and write down the first
  geometry feature that reads each variable, following chains of variable-reads-variable. That is
  where each `assignVariable` goes in the new tree. draft9p4 did this walk once for the studio rows;
  this repeats it for every tab's own.
- **Read every sketch's plane query** and mark which stand on a face and which on a stock plane.
  The ruling allows a plane where the sketch needs the torso's center, so each one on a plane needs
  a reason written next to it or a face to move to.
- **Settle the ten connector names.** `body`'s eight become `neck`, `left shoulder`,
  `right shoulder`, `left hip`, `right hip`, `mate for shoulder stud`, `mate for hip stud` and
  `mate for neck stud`, with the two sketches under them `hip stud location` and
  `neck stud location`. `hinge`'s two become `fork to robot` and `blade to robot`.
- **Confirm the six open numbers.** `#wall` reads `#torsoH * 3 / 160`; tasks #118, #125, #142, #168
  and #215 each name a specific parameter or query, and each is either already right in the parent
  or is a correction this draft makes.

## Phase B — build, one tab at a time, in this order

The order is forced by the derives: a tab cannot be built before the tab it derives from.

| Order | Tab | Derives from |
| ----: | --- | ------------ |
| 1 | `robot sizes` | — |
| 2 | `ball and socket` | — |
| 3 | `hinge` | — |
| 4 | `body` | `ball and socket` |
| 5 | `head` | `ball and socket` |
| 6 | `foot` | `ball and socket` |
| 7 | `u limb` | `ball and socket`, `hinge` |
| 8 | `l limb` | `ball and socket`, `hinge` |
| 9 | `gripper` | `ball and socket` |
| 10 | `stickbot` | every part |

Each tab's feature order is in its brief, under *Recommended steps*.

## The verification loop

**A tab is not built until it has been through all four rings, and a ring that fails sends the work
back to the ring inside it.** The loop is what makes an unattended REST build safe: nothing here
depends on a person noticing something.

### Ring 1 — the feature, after every single `POST`

- **Read the feature back.** `/features` returns what Onshape stored; compare it to what was sent,
  parameter by parameter. A `200` means accepted, not correct.
- **Check `featureStates`.** It is an array of `{key, value}` pairs, not a map; read as a map every
  feature reads `?`. A feature that is `ERROR` or `WARNING` stops the tab.
- **Check `rollbackIndex` equals the feature count.** A bar parked in the tree makes every
  downstream read short, and a short read looks exactly like missing work. This is why.
- **For a sketch, read its entities and constraints back** with `read_sketches.py` before the next
  feature runs. draft9p4 found four defects this way that left a blade looking right and 0.03 mm and
  0.002 mm off center.

### Ring 2 — the tab, when its last feature is in

- **Measure it.** `read_shape.py`, then every acceptance number in the brief checked against what
  `make_plans.py` computes. Import the constants; do not copy them.
- **Diff it against its parent**, with `diff_shape.py` for what came out and `diff_features.py` for
  what each feature was told. A difference is either a correction this draft intends, and is named
  in the register, or it is a defect.
- **Look at it.** The hero views and the section, rendered and opened, against the frames in
  [`../../build-briefs/images/`](../../build-briefs/images/). A measurement never stands in for the
  picture: face counts, areas and bounding boxes can all agree while the shape is wrong.
- **Score the construction** against the rulings in the table above, by hand. There is no checker
  and one is out of scope until the models are right.
- **Publish a named version** before moving to the next tab, so the next tab derives from something
  that cannot move.

### Ring 3 — the robot, when every tab is in

- **The assembly's mates all resolve**, and the figure stands at the height `make_plans.py`
  computes.
- **Every joint moves through its range** without the parts interfering.
- **Export the print files** and confirm each part is one solid.

### Ring 4 — the record

- **`register.md` says what was built, what each ring caught, and what was done about it.** A ring
  that was skipped says so. A gate claimed in the declaration gets the evidence that closes it, by
  name.

## When this draft is done

**Every tab passes Ring 2, the robot passes Ring 3, and one named version holds all ten tabs.**
That version is what the briefs cite from then on, and draft9p1p6, draft9p1p1 and draft9p4-check
stop being reference material.

## What is not yet written

The declaration, the phases, the gates claimed, how a part is proved, and where the guide's pages
come from afterwards. This file currently holds only what the survey established about the source
material.
