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

draft9p4's plan barred REST from building the model, for a draft that was writing pages. This draft
writes none. REST builds every feature here.

## The rulings a construction is judged against

Each was settled after the model it now judges was published.

| Ruling | Settled | Source |
| ------ | ------- | ------ |
| A variable feature keeps Onshape's title, `###name = #value` | 2026-09-08 | draft9p4 plan, *The variable naming rule* |
| A sketch stands on a face of the robot; a stock plane only where the sketch needs the torso's center | 2026-09-09 | draft9p4 plan, *What is settled before the take starts* |
| A variable is typed immediately before the first feature that reads it | 2026-09-11 | draft9p4 plan, *Variables arrive at the step that needs them* |
| `#ear` and `#backlash` are not declared, because nothing reads either | 2026-09-11 | the same walk |
| A connector is named for the joint it is, without the word *connector* | 2026-09-11 | draft9p4 plan, *What we do not know yet* |
| Every feature that is not a variable gets a typed name | task #138 | draft9p3 hinge fix |
| `relief slit` is the last feature on the blade | 2026-09-17 | [`../../../2026-09-17-reorg-drawings-and-notes.md`](../../../2026-09-17-reorg-drawings-and-notes.md) |

A student cannot type over a variable's title; the dialog has no rename pencil, the tree row has no
*Rename*, and `F2` does nothing.

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
- **A connector that is a joint end takes the joint's name**, and one that marks a placement takes
  `mate for …`. The eight Part Studios hold 23 `mateConnector` features; the assembly holds 13
  `mate` features, which are the thirteen joints.
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

### The head, where the eye reproduces 1.5 % oversize

`stickbot-draft9p4-check`'s head differs from `stickbot-draft9p4`'s in five faces each way, and
they are the eyes. Each eye's end face is 102.0857 mm² in the check document against 100.531 mm² in
the build document, which is π × `#eyeRx` 8 mm × `#eyeRy` 4 mm exactly. The check document's head is
the one built by following
[`head.rst`](../../../../instructions/stickbot-draft9p4/source/head.rst), so the page as followed
does not reproduce the eye it describes.

**The page is not obviously at fault.** `head.rst:510` has the reader dimension the ellipse
`#eyeRx * 2` and `#eyeRy * 2`, locate its center on `#eyeX` and `#eyeUp`, and read that it goes
black. There is no round on the eye and no draft on the extrude. Followed as written it gives
100.531 mm².

**`#headW` is not the difference.** The head's other faces match face for face, and the head box is
drawn from `#headW`, so `#eyeRx` and `#eyeRy` — `#headW / 9` and `#headW / 18` — resolve the same in
both documents.

**The area does not say what moved.** Two departures fit 102.0857 mm² exactly: both radii larger by
a factor of 1.0077, giving 8.0616 mm and 4.0308 mm; or both offset outward by 0.0411 mm, giving
8.0411 mm and 4.0411 mm. The 0.06 mm this was first written down as is the first of the two,
inferred from the area rather than measured off the sketch.

**Phase A reads the sketch and names the cause.** Where the cause is in the model or in the design
source, this draft fixes it. Where it is in the page's words, the register names the line and the
sentence to write instead, since this draft writes no pages.

**Ring 2's acceptance on `head`: each eye's end face is `math.pi * EYE_RX * EYE_RY`**, imported
from `make_plans.py`. No brief carries this number, so Ring 2 would not have caught it.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p5` |
| `document` | `stickbot-draft9p5`, created empty |
| `parent` | `draft9p1p6` for the four joint tabs' geometry, `draft9p1p1` for `body`, `head`, `foot`, `gripper` and the assembly, `draft9p4-check` for the hinge's build order |
| `from` | nothing. Every feature is added to an empty document |
| `builds` | `robot sizes`, `ball and socket`, `hinge`, `body`, `head`, `foot`, `u limb`, `l limb`, `gripper`, and the `stickbot` assembly |
| `by` | REST, for every feature. **Granted by Mike for `stickbot-draft9p5` by name, 2026-09-18** |
| `gates` | *Model inspected* and *Recovery point* — proposed, not agreed |
| `not claimed` | *Steps reproduce*, *Names are real*, *Links resolve*, *Floor & ceiling*, *Reading level* |

*Model inspected* is Ring 2; *Recovery point* is the named version at the end of each tab. The
five unclaimed gates ask for written steps, a link or a session, none of which this draft produces.

**Prose style and Spelling are on neither list**, because neither is run-scoped. `register.md` is
held to both, the same as everything else committed here.

## Where this draft's output goes

| What | Where |
| ---- | ----- |
| Phase A's answers, and every read a ring takes | `results/` |
| The ids of the document, its workspace and its ten tabs | `results/ids.md` |
| The scripts that drive REST | `scripts/` |
| Frames kept from Ring 2 and Ring 3 | [`../../build-briefs/images/`](../../build-briefs/images/) |
| The register | `register.md`, at this folder's root |

**`results/` holds no images.** The *Capture is out* gate refuses a tracked raster image anywhere
under `.docs/experiments/runs/`, so a frame worth keeping goes to the briefs' images folder and is
named in the brief that shows it. A frame not worth keeping is not committed.

**This draft writes no `reference/`.** It reads its parents' records where they sit:
[`../2026-09-08-draft9p4/reference/`](../2026-09-08-draft9p4/reference/) for the four joint tabs,
[`../2026-08-29-draft9p3/reference/`](../2026-08-29-draft9p3/reference/) for `body`, `head`, `foot`,
`gripper` and the assembly.

## Phase A0 — create `stickbot-draft9p5`

- **Create the document empty**, and in it the ten tabs the declaration names: the `robot sizes`
  Variable Studio, the eight Part Studios, and the `stickbot` Assembly. Nothing is copied and
  nothing is branched.
- **Record the ids** — document, workspace, and one element per tab — in `results/ids.md`.
- **Read the document's name back from Onshape before the first `POST`.** The REST grant names
  `stickbot-draft9p5` and no other document.

## Phase A — settle what cannot be measured from a record

Each of these is a read, and each writes its answer into `results/`.

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
- **Read `eye profile` in `stickbot-draft9p4-check`** with `read_sketches.py`, and that tab's four
  eye variables with `/features`. § *The head, where the eye reproduces 1.5 % oversize* says what
  the two candidate causes are and what each predicts for the ellipse's radii.
- **Run `ninja brief-sheets` and confirm nothing changes.**
- **Confirm every sheet is referenced by the brief that owns it.**
- **Confirm the six open numbers.** `#wall` reads `#torsoH * 3 / 160`; tasks #118, #125, #142, #168
  and #215 each name a specific parameter or query, and each is either already right in the parent
  or is a correction this draft makes.

## The names to build under

**Every name below is what the new tab carries. The old name is listed so a record read from a
parent document can be matched to it.** The parents' reference records and the frames under
[`../../build-briefs/images/`](../../build-briefs/images/) all predate these, so a name that does
not appear in this table is unchanged.

### The joint's vocabulary

| Build it as | Not | Why |
| ----------- | --- | --- |
| `stub axle` | `axle stub` | already the CAD's name: `stub axle outline`, `stub axle`, `#stub`, `#stub_proud` |
| `axle bore` | `pocket axle` | the two features `pocket axle sketch` and `pocket axle on fork` |
| `blade leaf` | `blade ear`, `tab` | already what `#leaf_root`, `#leaf_tip` and `hinge_spring.py` call it |
| `blade blank` | `tongue` | already the CAD's name for the extrude that makes it |
| `fork prong` | `ear` | the whole of *ear* is retired |

### The features that change name

| Tab | Old | New |
| --- | --- | --- |
| `hinge` | `ear wedge outline`, `ear wedge`, `ear wedges` | `fork prong wedge outline`, `fork prong wedge`, `fork prong wedges` |
| `hinge` | `pocket axle sketch`, `pocket axle on fork` | `axle bore sketch`, `axle bore on fork` |
| `hinge` | `fork to robot connector`, `blade to robot connector` | `fork to robot`, `blade to robot` |
| `body` | `neck connector`, `left shoulder connector`, `r shoulder connector`, `l hip connector`, `r hip connector` | `neck`, `left shoulder`, `right shoulder`, `left hip`, `right hip` |
| `body` | `connector on torso shoulder`, `hip connector on torso`, `neck connector on torso` | `mate for shoulder stud`, `mate for hip stud`, `mate for neck stud` |
| `body` | `hip connector location`, `neck connector location` | `hip stud location`, `neck stud location` |

Everything else keeps the name its parent gave it. The step tables in the briefs already print the
new names, so a tab built from a brief needs no translation.

### The identifiers that have not moved

**`make_plans.py` still exports `EAR`, `EAR_FREE`, `EAR_MOVE` and `EAR_STRESS`, and the briefs
still cite them.** A brief may say *fork prong* in a sentence and `EAR` in the row beneath it; both
mean the fork's arm. Renaming them is task #225, not draft9p5's.

**`#ear` is not one of them.** That CAD variable is dropped, with `#backlash`.

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
- **Name the features first, then eyeball the CAD until you can tell that it matches the brief's
  feature or does not.** The list comes from the brief's *Recommended steps*. Each feature gets a
  view it is visible in, and a verdict.
- **Open every frame you keep**, and check that nothing is selected in it.
- **Eyeball the CAD against the brief's prose, not just its numbers.** The brief names what the
  part should be. Where the part and the brief disagree, say which is wrong; either can be.
- **Hold the section beside the tab's `brief-*.svg` sheet**, and compare them as two drawings of
  the same thing rather than as two sets of numbers. `ball and socket` has `brief-socket.svg`;
  `hinge`, `u limb` and `l limb` have `brief-fork.svg`, `brief-detent.svg` and `brief-roots.svg`.
  Say which sheet was used and what was compared on it. A sheet carries the shape, where a
  constant carries only the size.
- **A tab with no sheet says so.** `body`, `head`, `foot` and `gripper` have none, so their
  drawing check is the plan sheets, `plan-parts.svg` and `plan-assembly.svg`, which `make_plans`
  generates and which a ninja target keeps current.
- **Score the construction** against the rulings in the table above, by hand. There is no checker
  and one is out of scope until the models are right.
- **Publish a named version** before moving to the next tab, so the next tab derives from something
  that cannot move.

### Ring 3 — the robot, when every tab is in

- **Look at the assembled robot, front, side and isometric,** against
  [`../../build-briefs/images/plan-assembly.svg`](../../build-briefs/images/plan-assembly.svg).
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

Where the guide's pages come from after this draft.
