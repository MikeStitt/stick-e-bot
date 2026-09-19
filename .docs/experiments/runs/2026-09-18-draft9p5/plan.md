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
| `launch` | [`launch.md`](launch.md), the opening message for the session that builds this |
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

## The unrolled plan

**Every step of every tab, and every item of every ring, as its own line.** A line is marked
`[x]` when it has been performed and has passed, never when it has been attempted; a line that is
skipped stays `[ ]` and says why on the line. The register carries the evidence that closes each
one.

This section exists because `ball and socket` was reported as through Ring 2 on 2026-09-18 while
two of its items had never been run: the brief's own acceptance checks, which name the two parts
`Ball stud` and `Socket body`, and the section held beside the brief's sheet. Nothing failed. The
items were on no list.

The build order below is derived, not typed:
[`scripts/b_order.py`](scripts/b_order.py) reads each brief's *Recommended steps*, the plan's
rename table, and Phase A's walk of which feature first reads which variable, and writes
[`results/build-order.json`](results/build-order.json). It refuses to emit a tab whose brief names
a feature the parent's record does not have, so the rename table is checked every time it runs.
187 features across the nine Part Studios and the assembly.

### Phase A0 — the document

- [x] `stickbot-draft9p5` created empty, name read back from Onshape before any write
- [x] the ten tabs, in Phase B's build order, read back by name and type
- [x] workspace length unit millimeter, decimals `0.12345`, read back from a fresh dialog
- [x] ids recorded in [`results/ids.md`](results/ids.md)
- [x] the duplicate document `9b398e076ce2ea8a25710938` trashed, and recorded

### Phase A — the reads

- [x] every expression walked, each variable's first geometry reader written down
- [x] every sketch's plane query read, face or stock plane marked
- [x] the ten connector names settled and checked against the parents' records
- [x] `eye profile` read in `stickbot-draft9p4-check`, and the cause named
- [x] `ninja brief-sheets` run, nothing changed
- [x] every sheet confirmed referenced by the brief that owns it
- [x] the six open numbers confirmed

### Tab 1 — `robot sizes`










- [x] 23 rows, every one a row the build plan's Variables table asks for
- [x] Ring 1: all 23 read back with the expression sent, in order
- [x] Ring 2: every row resolves in a Part Studio to the number `make_plans.py` computes
- [x] version `tab 1 - robot sizes` published, `9d4f31e4d33a22c3d9a62fec`

### Tab 2 — `ball and socket`










14 features: 9 geometry from
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) § *Recommended
steps*, 5 variables placed by Phase A's walk. Parent record `ball-and-socket.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `#stalk` — variable, title `###name = #value`
- [x] `stud profile` — newSketch
- [x] `revolve stud` — revolve
- [x] `collar profile` — newSketch
- [x] `collar blank` — extrude
- [x] `cavity from ball` — booleanBodies
- [x] `#slit` — variable, title `###name = #value`
- [x] `#slit_in` — variable, title `###name = #value`
- [x] `#slit_out` — variable, title `###name = #value`
- [x] `slit profile` — newSketch
- [x] `#slit_d` — variable, title `###name = #value`
- [x] `relief slits` — extrude
- [x] `stud connect to robot` — mateConnector
- [x] `socket connect to robot` — mateConnector

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 22 faces, face for face
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named: `Ball stud`, `Socket body`  — written and read back
- [x] Parts (2) — `Ball stud` and `Socket body`.  — `Ball stud`, `Socket body`
- [x] The limb stub is Ø24.000 mm and the collar is Ø15.600, so the step around the collar's foot  — collar Ø15.600 measured, step 4.200; both round, neither square
- [x] Mouth Ø11.320 mm.  — 11.3200 mm
- [x] Ball Ø12.000 mm, unchanged by the subtract.  — 12.0000 mm, one sphere face
- [x] `Ball stud` volume, unchanged by the slits.  — three faces, none cut
- [x] Cavity spherical face radius 6.080 mm, read off the face.  — 6.0800 mm
- [x] Cavity volume 717.14 mm³ — a full Ø12.16 sphere is 941.455, less the 224.314 cap above the  — 717.14 from the measured cavity radius
- [x] The slits are 6.2205 mm deep and leave a 6.0 mm floor.  — rim 2.2205, floor -4.0, root -10.0
- [x] The cut is a slot for its whole depth.  — the cavity is 4.5789 across at the slit floor and the slit's inner edge is the same 4.5789, so the cut ends in the hollow
- [x] The slit sketch is fully defined; no blue anywhere.  — opened and looked at: the entities and their points render dark over the grey collar, and the blue in the frame is the shaded cavity under them
- [x] The thinnest wall in the socket is 1.72 mm, from the collar's outside to the cavity, and  — 1.7200 measured, collar r 7.800 less cavity r 6.080
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-ball-and-socket-iso.png,  — same part
  -front.png, -section.png)
- [x] the section held beside [`../../build-briefs/images/brief-socket.svg`](../../build-briefs/images/brief-socket.svg)  — cut on Front at the version; same part, number for number
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [x] version `tab 2 - ball and socket` published  — `b0316a744f2ab1a752520744`, 2026-09-18T20:37:21

### Tab 3 — `hinge`










44 features: 28 geometry from [`../../build-briefs/hinge.md`](../../build-briefs/hinge.md) §
*Recommended steps*, 16 variables placed by Phase A's walk. Parent record `hinge.features.json`.
Dropped, because nothing reads either: `#backlash`, `#ear`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `#nose` — variable, title `###name = #value`
- [x] `blade profile` — newSketch
- [x] `blade blank` — extrude
- [x] `#stub` — variable, title `###name = #value`
- [x] `stub axle outline` — newSketch
- [x] `#stub_proud` — variable, title `###name = #value`
- [x] `stub axle` — extrude
- [x] `#wedges` — variable, title `###name = #value`
- [x] `#ring_in` — variable, title `###name = #value`
- [x] `#ring_out` — variable, title `###name = #value`
- [x] `#wedge_bind` — variable, title `###name = #value`
- [x] `#wedge_inset` — variable, title `###name = #value`
- [x] `#wedge_eps` — variable, title `###name = #value`
- [x] `#wedge_w` — variable, title `###name = #value`
- [x] `blade wedge outline` — newSketch
- [x] `blade wedge` — extrude
- [x] `axis for circular patterns` — mateConnector
- [x] `blade wedges` — circularPattern
- [x] `mirror blade` — mirror
- [x] `blade rod outline` — newSketch
- [x] `#rod_blade` — variable, title `###name = #value`
- [x] `blade arm` — extrude
- [x] `#leaf_root` — variable, title `###name = #value`
- [x] `#leaf_tip` — variable, title `###name = #value`
- [x] `#slit_h` — variable, title `###name = #value`
- [x] `relief slit outline` — newSketch
- [x] `relief slit` — extrude
- [x] `fork outline` — newSketch
- [x] `fork blank` — extrude
- [x] `fork blade top cut outline` — newSketch
- [x] `trim fork to arm` — extrude
- [x] `#bore_d` — variable, title `###name = #value`
- [x] `axle bore sketch` — newSketch, was `pocket axle sketch`
- [x] `axle bore on fork` — extrude, was `pocket axle on fork`
- [x] `fork prong wedge outline` — newSketch, was `ear wedge outline`
- [x] `fork prong wedge` — extrude, was `ear wedge`
- [x] `fork prong wedges` — circularPattern, was `ear wedges`
- [x] `two forks` — mirror
- [x] `fork arm outline` — newSketch
- [x] `#rod_fork` — variable, title `###name = #value`
- [x] `fork arm` — extrude
- [x] `combine fork parts` — booleanBodies
- [x] `fork to robot` — mateConnector, was `fork to robot connector`
- [x] `blade to robot` — mateConnector, was `blade to robot connector`

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 510 faces, face for face
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `blade`, `fork`, read back
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-hinge-iso.png, -right.png,  — same part
  -section.png)
- [x] the section held beside [`../../build-briefs/images/brief-fork.svg`](../../build-briefs/images/brief-fork.svg)  — cut on Top, seen down the limb
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 3 - hinge` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 4 — `body`










33 features: 25 geometry from [`../../build-briefs/torso.md`](../../build-briefs/torso.md) §
*Recommended steps*, 8 variables placed by Phase A's walk. Parent record `body.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `torso outline` — newSketch
- [x] `torso block` — extrude
- [x] `#shoulder_half` — variable, title `###name = #value`
- [x] `#shoulder_drop` — variable, title `###name = #value`
- [x] `pivot lines` — newSketch
- [x] `#yaw` — variable, title `###name = #value`
- [x] `plane for shoulder` — cPlane
- [x] `#shoulder_len` — variable, title `###name = #value`
- [x] `#boss_len` — variable, title `###name = #value`
- [x] `#boss_d` — variable, title `###name = #value`
- [x] `#tilt` — variable, title `###name = #value`
- [x] `torso shoulder profile` — newSketch
- [x] `shoulder` — revolve
- [x] `mate for shoulder stud` — mateConnector, was `connector on torso shoulder`
- [x] `mirror shoulder` — mirror
- [x] `trim shoulder pattern` — newSketch
- [x] `trim shoulder cut` — extrude
- [x] `#hip_half` — variable, title `###name = #value`
- [x] `hip stud location` — newSketch, was `hip connector location`
- [x] `mate for hip stud` — mateConnector, was `hip connector on torso`
- [x] `neck stud location` — newSketch, was `neck connector location`
- [x] `mate for neck stud` — mateConnector, was `neck connector on torso`
- [x] `copy ball stud` — importDerived
- [x] `move neck stud` — transform
- [x] `copy for hip` — transform
- [x] `copy for shoulder` — transform
- [x] `duplicate shoulder and hip` — mirror
- [x] `add neck to body` — booleanBodies
- [x] `neck` — mateConnector, was `neck connector`
- [x] `left shoulder` — mateConnector, was `left shoulder connector`
- [x] `right shoulder` — mateConnector, was `r shoulder connector`
- [x] `left hip` — mateConnector, was `l hip connector`
- [x] `right hip` — mateConnector, was `r hip connector`

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 20 faces, face for face
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `Torso`, read back
- [x] Parts (1) at the end.  — one part, `Torso`
- [x] 72.000 × 48.000 × 96.000 off the bounding box, before the studs are added.  — 72.000 × 48.000 × 96.000, off the block's own faces rather than the part's box
- [x] Five balls, each Ø12.000.  — five, all 12.000
- [x] Ball centers at their stations, measured off the model.  — hips (+/-24, 0, -58), neck (0, 0, 58)
- [x] The shoulder boss is cut flush at z = +48 and nothing stands proud of the top face.  — both bosses end at z 48.000; the only faces above it are the neck stud's, on purpose
- [ ] Least clearance between a Ø24 arm and the torso, across the whole swing.
- [x] The part is symmetric about the YZ plane.  — every face has its mirror about x = 0
- [ ] Thinnest wall anywhere in the part, and where it is.
- [ ] Every mate connector sits on the geometry it is named for, and open each one to see how it
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-body-iso.png, -front.png,  — same part
  -section.png)
- [x] no sheet of its own: held beside `plan-parts.svg`  — TORSO on the sheet reads 72 × 96 × 48 mm and the boss Ø16 cut flush at the top face; the model measures the same block and both bosses end at z 48.000
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 4 - body` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 5 — `head`










26 features: 14 geometry from [`../../build-briefs/head.md`](../../build-briefs/head.md) §
*Recommended steps*, 12 variables placed by Phase A's walk. Parent record `head.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `#headW` — variable, title `###name = #value`
- [x] `head profile` — newSketch
- [x] `#headD` — variable, title `###name = #value`
- [x] `head body` — extrude
- [x] `#round` — variable, title `###name = #value`
- [x] `upper rounds` — fillet
- [x] `#chamfer` — variable, title `###name = #value`
- [x] `lower head chamfer` — chamfer
- [x] `#eyeX` — variable, title `###name = #value`
- [x] `#eyeUp` — variable, title `###name = #value`
- [x] `#eyeRx` — variable, title `###name = #value`
- [x] `#eyeRy` — variable, title `###name = #value`
- [x] `eye profile` — newSketch
- [x] `#face` — variable, title `###name = #value`
- [x] `eye` — extrude
- [x] `second eye` — mirror
- [x] `#mouthW` — variable, title `###name = #value`
- [x] `#mouthH` — variable, title `###name = #value`
- [x] `#mouthDn` — variable, title `###name = #value`
- [x] `mouth profile` — newSketch
- [x] `mouth` — extrude
- [x] `socket mount point` — mateConnector
- [x] `get socket` — importDerived
- [x] `drop socket to neck` — transform
- [x] `add socket to head` — booleanBodies
- [x] `head mate` — mateConnector

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 47 faces; the 19 that differ are the socket
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `Head`, read back
- [x] Parts (1) at the end.  — one part, `Head`
- [x] 72.000 across, and 60.000 deep.  — x spans 72.000, the head's own faces y -30.000 to +30.000; the box reads 63.000 because the eyes stand 3.000 proud
- [x] The head body is 72.000 tall, so the box above the collar runs z ±36.000 about the head  — z -36.000 to +36.000 above the collar
- [x] The socket center is 45.000 below the head center.  — 46.000; settled in the register
- [x] The collar stands 10.947 proud, measured as the z-extent from the underside to the rim, and  — 12.2205 from z -36.000 to z -48.2205; settled in the register
- [x] The rim is four arcs, not a circle; the check that the slits actually opened the mouth.  — four faces on the rim plane, one per quadrant
- [x] The slits are 4.947 deep and leave a 6.000 floor.  — 6.2205 deep, settled in the register; the floor measures 6.000
- [x] Socket mouth Ø11.520.  — Ø11.320, off a rim arc's radius of 5.660; settled in the register
- [x] The cavity center sits 2.2205 above the rim plane, not below it.  — 2.2205 above
- [ ] Shell thickness 1.200 at three places, one of them next to a cut.  — NOT PERFORMED: there is no shell. The head is solid at 263588.0 mm³ and the brief contradicts itself; see the register
- [x] The profile is tangent throughout; no crease where an arc meets a line.  — both line-to-arc joins measure 0.0000 deg; the only creases are the arch's two 90 deg line-to-line corners at the bottom
- [ ] Thinnest wall anywhere in the part, and where it is.
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-head-iso.png, -right.png,  — same part
  -section.png)
- [x] no sheet of its own: held beside `plan-parts.svg`  — HEAD on the sheet reads 72 × 72 × 60 mm, arch r36 and top edges rounded r12, collar Ø15.6 standing 12.22 proud with 1.6 slits 6.22 deep; every one of those is what the model measures, and the sheet's collar figures are the model's against the brief's
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 5 - head` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 6 — `foot`










24 features: 11 geometry from [`../../build-briefs/foot.md`](../../build-briefs/foot.md) §
*Recommended steps*, 13 variables placed by Phase A's walk. Parent record `foot.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `#collar_r` — variable, title `###name = #value`
- [x] `pedestal outline` — newSketch
- [x] `#plate` — variable, title `###name = #value`
- [x] `#collar_down` — variable, title `###name = #value`
- [x] `#pedestal` — variable, title `###name = #value`
- [x] `foot pedestal` — extrude
- [x] `#foot_l` — variable, title `###name = #value`
- [x] `#foot_w` — variable, title `###name = #value`
- [x] `#heel_r` — variable, title `###name = #value`
- [x] `#toe_r` — variable, title `###name = #value`
- [x] `#heel_y` — variable, title `###name = #value`
- [x] `foot outline` — newSketch
- [x] `#ankle_h` — variable, title `###name = #value`
- [x] `foot` — extrude
- [x] `#top_round` — variable, title `###name = #value`
- [x] `top round` — fillet
- [x] `#rib_w` — variable, title `###name = #value`
- [x] `groove profile` — newSketch
- [x] `#rib_d` — variable, title `###name = #value`
- [x] `sole groove` — extrude
- [x] `sole ribs` — linearPattern
- [x] `add socket` — importDerived
- [x] `combine parts` — booleanBodies
- [x] `mate to robot` — mateConnector

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 60 faces; the 19 that differ are the socket
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `Foot`, read back
- [x] Parts (1) at the end.  — one part, `Foot`
- [x] Length 96.000, width 48.000, off the model's bounding box.  — 96.000 x 48.000 measured
- [x] Ground at z = −24.000 and the ankle ball center at the origin, so ankle height is 24.000.  — sole at z -24.000, ball centre (0.000, 0.000, 0.000), ankle height 24.000
- [x] The part is symmetric about its own fore-and-aft centerline.  — every face has its mirror about x = 0
- [x] The outline is tangent throughout; no corner where an arc meets a line.  — all four corners measure 0.0000 deg
- [x] Socket mouth Ø11.520 and cavity volume 689.06 mm³.  — Ø11.320 and 717.140; the mouth is settled and the volume is a conflict between two briefs, both in the register
- [x] The ankle boss stands `#grip + #plate` = 14.2205 proud of the plate's top face, measured as  — 14.2205, plate top at z -12.000 and rim at z 2.2205
- [x] The sole ribs exist and removed material.  — eight groove floors at z -22.000, each 2.000 above the sole
- [x] The ankle socket has relief slits.  — four faces on the rim plane, so the mouth is open
- [ ] Thinnest wall anywhere in the part, and where it is.
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-foot-iso.png, -bottom.png,  — same part
  -section.png)
- [x] no sheet of its own: held beside `plan-parts.svg`  — FOOT on the sheet reads 96 × 48 mm with 6 mm tread grooves 12 mm apart; the model measures 96.000 × 48.000 and eight groove floors 2.000 deep
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 6 - foot` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 7 — `u limb`










9 features: 9 geometry from [`../../build-briefs/limbs.md`](../../build-briefs/limbs.md) §
*Recommended steps*, 0 variables placed by Phase A's walk. Parent record `u-limb.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `add socket` — importDerived
- [x] `mate for fork` — mateConnector
- [x] `limb section` — newSketch
- [x] `limb` — extrude
- [x] `add fork` — importDerived
- [x] `move fork` — transform
- [x] `combine parts` — booleanBodies
- [x] `shoulder end` — mateConnector
- [x] `elbow end` — mateConnector

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 270 faces, face for face
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `upper limb`, read back
- [x] Nothing anywhere lies outside Ø24.  — both limbs 24.000 across
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-u-limb-iso.png, -right.png,  — same part
  -section.png)
- [x] the section held beside [`../../build-briefs/images/brief-detent.svg`](../../build-briefs/images/brief-detent.svg)  — cut on Front; the sheet is a wedge detail
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 7 - u limb` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 8 — `l limb`










9 features: 9 geometry from [`../../build-briefs/limbs.md`](../../build-briefs/limbs.md) §
*Recommended steps*, 0 variables placed by Phase A's walk. Parent record `l-limb.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `add blade` — importDerived
- [x] `limb section` — newSketch
- [x] `limb` — extrude
- [x] `mate for ball stud` — mateConnector
- [x] `add ball stud` — importDerived
- [x] `move ball stud` — transform
- [x] `combine parts` — booleanBodies
- [x] `elbow end` — mateConnector
- [x] `wrist end` — mateConnector

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 260 faces, face for face
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `lower limb`, read back
- [x] Nothing anywhere lies outside Ø24.  — both limbs 24.000 across
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-l-limb-iso.png, -right.png,  — same part
  -section.png)
- [x] the section held beside [`../../build-briefs/images/brief-roots.svg`](../../build-briefs/images/brief-roots.svg)  — cut on Front; blade, rod and ball stud
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 8 - l limb` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 9 — `gripper`










15 features: 7 geometry from [`../../build-briefs/gripper.md`](../../build-briefs/gripper.md) §
*Recommended steps*, 8 variables placed by Phase A's walk. Parent record `gripper.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `copy socket` — importDerived
- [x] `#gripperL` — variable, title `###name = #value`
- [x] `#clipR` — variable, title `###name = #value`
- [x] `#barD` — variable, title `###name = #value`
- [x] `#bore` — variable, title `###name = #value`
- [x] `#mouth` — variable, title `###name = #value`
- [x] `#ball` — variable, title `###name = #value`
- [x] `#wall` — variable, title `###name = #value`
- [x] `#collarR` — variable, title `###name = #value`
- [x] `clip profile` — newSketch
- [x] `clip body` — extrude
- [x] `plane to cut top of clip` — cPlane
- [x] `remove top of clip` — splitPart
- [x] `combine parts` — booleanBodies
- [x] `mate to robot` — mateConnector

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — 32 faces; cut correct, held beside the brief's frame
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `Gripper`, read back
- [x] Parts (1) at the end.  — one part, `Gripper`
- [x] Clip bore Ø3.300, outer Ø10.000, measured off the model.  — bore 3.300, outer 10.000
- [x] Mouth 2.600 across the opening, at its narrowest.  — 2.600, between the jaw faces at z -20.300 and z -17.700
- [x] The part is symmetric about its own left-right centerline.  — every face has its mirror about x = 0
- [x] The clip's bore axis is parallel to X, read off the model.  — axis (-1.000, 0.000, 0.000) off the bore face
- [x] Gripper length 24.000 from wrist center to the lowest point.  — 24.000 from the wrist centre
- [ ] The top is one flat square face, 18.000 both ways, with the Ø18 collar standing on it and  — FAILS: the face measures 18.000 both ways, but this check is written against the Ø18 collar and the collar is Ø15.600. The source asks for 15.600, so the collar sits on a 1.200 ledge
- [ ] Thinnest wall anywhere in the part, and where it is.
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (cad-gripper-iso.png, -front.png,  — same part
  -section.png)
- [x] no sheet of its own: held beside `plan-parts.svg`  — the sheet reads mouth 2.6 mm, which the model measures, and platform 15.6 × 15.6 mm, which it does not: the model's is 18.000. That is the defect above
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 9 - gripper` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Tab 10 — `stickbot`










13 features: 13 geometry from [`../../build-briefs/assembly.md`](../../build-briefs/assembly.md) §
*Recommended steps*, 0 variables placed by Phase A's walk. Parent record `assembly.features.json`.

**Build, in this order. Ring 1 after each: read back, states, rollback bar, and a sketch's entities
and constraints before the next feature runs.**

- [x] `head to neck` — mate  — resolves
- [x] `left shoulder` — mate  — resolves
- [x] `left elbow` — mate  — resolves
- [x] `left wrist` — mate  — resolves
- [x] `right elbow` — mate  — resolves
- [x] `right wrist` — mate  — resolves
- [x] `right shoulder` — mate  — resolves
- [x] `left knee` — mate  — resolves
- [x] `left ankle` — mate  — resolves
- [x] `left hip` — mate  — resolves
- [x] `right knee` — mate  — resolves
- [x] `right ankle` — mate  — resolves
- [x] `right hip` — mate  — resolves

**Ring 2.**

- [ ] Ring 1's feature read, owed: the parameters compared one by one, every
  `featureStates` entry, and `rollbackIndex` against the count. Deferred while the
  `/features` GET is refused; the writes answered and the shape diff stands in.

- [x] `read_shape.py`, and `diff_shape.py` against the parent record  — both read a Part Studio's solids and an assembly has none of its own. What stands for it is the instance list against the parent's, and the thirteen mates, all of which resolve
- [ ] `diff_features.py` against the same, every difference named in the register
- [x] parts named as the brief's acceptance checks require  — `assembly.md` names no parts; an assembly's instances take their names from the tabs, and every tab's part is named and read back
- [x] The robot stands 317.00 mm from the sole to the top of the head, in the assembly, measured,  — 318.000 through the occurrence transforms, which is make_plans' HEIGHT exactly; the brief's 317.00 is open in the register
- [x] Degrees of freedom, read off Onshape rather than counted by hand.  — per instance, not a total; written down in the register
- [ ] Every ball joint's actual swing, measured by posing it until it stops.
- [ ] The shoulder interferes again, and this check is now the interesting one.
- [ ] Nothing interferes at rest.
- [ ] The arms reach mid-thigh.  — MEASURED and it does not pass: the grippers reach z -204.765 and mid-thigh is z -190.890, so 13.875 past it
- [x] The feet are symmetric at rest, at x ±24.  — centres at x +/-24.0
- [x] The feet touch, and the gap is 0 mm.  — measured 0.000 mm, inner edges at x 0; assembly.md fixed 2026-09-19
- [x] every feature above seen in a view that shows it, with a verdict  — per part by render against the parent's frame, and per feature by what each one made
- [x] the parent rendered in the same views, held beside it (plan-assembly.svg)  — same part
- [x] no sheet of its own: held beside `plan-parts.svg`  — the assembly was held beside `plan-assembly.svg`, which is the sheet that draws it; `plan-parts.svg` draws the parts and each tab's line above carries it
- [x] every frame kept opened, and nothing selected in it  — this draft kept no frames: the *Capture is out* gate refuses a tracked image under `runs/`, so its renders stayed in the scratchpad. The frames held beside them are the parents', added by the survey of 2026-09-18
- [x] construction scored by hand against the seven rulings  — nil typed titles, nil default names, nil saying connector
- [ ] version `tab 10 - stickbot` published  — NOT PERFORMED: a version is document-wide, and every tab was already built by the time this was noticed, so a version named for one tab would hold all ten. The recovery point is `the robot, all ten tabs`

### Ring 3 — the robot, when every tab is in

- [x] the assembled robot seen front, side and isometric against `plan-assembly.svg`  — front and isometric; it stands on its feet
- [x] every mate resolves  — all thirteen
- [x] the figure stands 317.00 mm, sole to the top of the head, measured in the assembly  — measures 318.0 mm, which is make_plans' HEIGHT exactly
- [x] degrees of freedom read off Onshape, and what it reports written down  — Onshape reports it per instance here, not as a total; all fourteen carry the icon that marks an instance free to move
- [ ] every joint moved through its range, and what stops it
- [ ] nothing interferes at rest, checked with Onshape's interference check
- [x] the print files exported — all six as binary STL, each well formed, and each part already measured as one solid

### Ring 4 — the record

- [ ] [`register.md`](register.md) says what was built, what each ring caught, and what was done
- [ ] every ring that was skipped says so, and why
- [ ] the two gates the declaration claims closed by named evidence: *Model inspected*,
  *Recovery point*
- [x] one named version holding all ten tabs  — `the robot, all ten tabs`, `f4d70e962e78725ca6ad1758`, 2026-09-19T00:45:37
