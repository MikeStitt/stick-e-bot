# draft9p1p4 — edit the six joints current, so a later draft can inherit and teach them

**This draft copies four tabs out of documents that already build them well, edits them to the
design as it now stands, and adds a printable coupon for each half of the ball joint.** What it
hands on is CAD a later draft can inherit, edit, and write step files from.

**It edits; it does not rebuild.** A tab whose numbers are stale is a program with bugs, not a
program to throw away. The construction that draft9p3 and draft9p1 already carry is the thing of
value here: sketches anchored to geometry, joints derived rather than resketched, features named as
they were made. The numbers on top of it are what moved.

## Why this draft exists

draft9p3 built the robot tutorial by tutorial and got as far as the upper limb. It never reached the
lower limb. In the days since it stopped, every joint number moved:

- the hinge was settled end to end and rebuilt around a 0.15 fit, a slit tongue and cone teeth
- the socket wall went 3.0 to 1.8, the grip 1.946 to 2.221, and the mouth 11.52 to 11.32
- the axle dropped from 1.6 proud to 1.30, engaging 1.15
- the limbs were cut flat top and bottom to 21.6774, so a limb prints on a face
- `#collar` became `#stand`, so both halves of a ball joint reach the same distance
- the slot's raised land came out and the ear's whole inner face came forward to where it was

**No document holds that joint set on construction anybody would want a student to copy.** This
draft is where the six studios come current at once, in one place, without giving up the
construction that got them here.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p1p4` |
| `parent` | `stickbot-draft9p3` for the ball and socket, the hinge and the upper limb; `stickbot-draft9p1` for the lower limb |
| `from` | `empty`, then copied into tab by tab; see *What is copied* |
| `takes` | seven tabs only: `robot sizes`, `ball and socket`, `hinge`, `u limb`, `l limb`, `ball with cylinder`, `socket with cylinder` |
| `gates` | *Model inspected*, *Recovery point*, *Prose style*, *Spelling*. **No pages, no frames, no tutorials, no capture.** |
| `requirements` | `req.model.design_intent`, `req.model.anchored`, `req.model.named_features`, `req.model.visible_geometry`, `req.model.derive`, `req.model.same_structure`, `req.log`. `req.page`, `req.shot`, `req.guide` and `req.audit` do not apply |

**`req.model.one_document` is knowingly deferred.** It says the whole robot is built in one document
called `stickbot`. This draft builds six joint studios and no robot, because the joints have to be
right before the robot is worth assembling around them.

**`req.model.same_structure` is claimed, not deferred, and editing in place is how.** It requires
the construction to match the reference feature for feature. Every edit here is to a number, a
name, or a defect already written up; where an edit has to change the construction, the register
says which feature moved and why, so the next draft diffs against a known change rather than a
surprise.

## Mike's permission for this run, and the standard it does not relax

On 2026-09-02 Mike lifted *"GUI only for geometry"* for this run, in these words:

> You can use the computer API to do the work, but the resulting CAD must me the constitutions
> requirements for human onshape CAD quality.

So this draft may call `POST /api/partstudios/.../features` and anything else that writes. The
standard it has to reach is the *Modeling standards* section of
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md):

> Build the model the way a careful human would build it: fully defined sketches anchored to
> geometry that already exists, starting at the origin and working outward, every length driven by a
> named variable, symmetry expressed as a mirror and repetition as a pattern, each part made once
> and derived where it is reused, so that changing any driving dimension rebuilds the whole thing
> correctly. That holds whatever the route. The REST feature API authors constraints, mate
> connectors, mirrors, patterns and derived features as readily as the GUI does; it costs more calls
> per feature, and a script that skips them for that reason has emitted geometry rather than built a
> model.

Three things follow, and none of them is optional:

- **The permission is for this run and this document.** It does not carry to draft9p3, to any guide,
  or to a later draft.
- **Every other Onshape rule stands.** Port 9223 only. `stickbot-draft9p1p1` stays read only.
  Nothing closes a page it did not open.
- **Reading back is still how anything is proven.** `featureStatus` says OK for features that
  produced nothing.

## What is copied, and from where

Read off Onshape on 2026-09-02, not off the record.

| Tab | Source | Document | Element |
| --- | ------ | -------- | ------- |
| `robot sizes` | written fresh from `make_plans.py` | -- | -- |
| `ball and socket` | `stickbot-draft9p3` | `50b2d87357670c07c2fbcb89` / `a49825ea9aa838bdfae7b78d` | `45e967b1779a75776404e8e0` |
| `hinge` | `stickbot-draft9p3` | same | `965ca787810d0eb0f3aefcf1` |
| `u limb` | `stickbot-draft9p3` | same | `a9f1f5d3718ed1746fdf0e47` |
| `l limb` | `stickbot-draft9p1` | `a1a859f4bfdfe42d372aff90` / `d3a590c94880f445e3c56902` | `fa98530f59d5f18889fe7c00` |
| `ball with cylinder` | new | -- | -- |
| `socket with cylinder` | new | -- | -- |

**The lower limb is the one substitution, and draft9p3 forces it.** draft9p3 has no `l limb`; its
tutorial 11 was never run. draft9p1's is the same construction as draft9p3's `u limb` — ten
features, `add blade | limb section | limb | mate for ball stud | add ball stud | move ball stud |
combine parts` — so it is the closest thing to what draft9p3 would have built.

**Provenance is a version; the model is not.** draft9p3 is cited at `tutorial 10 - the upper limb`,
`f94cbf2e4657300be13507d2`, and draft9p1 at `Recovery point`, `8504f457723606c65c2ab48f`. That
satisfies *Cite named versions, never live workspaces*, which governs what a document says. It does
not reach inside the model: `.parts/onshape.md` requires every reference **inside** a model to name
an element in its own workspace, so a copied tab that still derives from its old document is a
defect B0 finds and B2 through B5 fix.

**draft9p1p2 and draft9p1p3 are not sources, and may not become sources.**
[`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) names the first of them as the
counterexample the standard exists to prevent: *"four tabs of typed coordinates, no constraint
anywhere, the fork and the socket each built twice, and no way to change a driving length except to
re-run the script that wrote it."* draft9p1p3 was Mike's attempt to repair that and was abandoned as
hopeless. Both carry the settled joint's numbers, and their numbers are not the reason to open them;
`make_plans.py` holds those. Read them for nothing.

## What has moved since draft9p3, by tab

Read off `make_plans.py` at `e6078514~1` against `HEAD`, not transcribed.

**`ball and socket`**

| Name | draft9p3 | now |
| ---- | -------- | --- |
| `COLLAR_WALL` | 3.0 | 1.8 |
| `COLLAR_R` | 9.0 | 7.8 |
| `COLLAR_L` | 9.0 | 10 |
| `COLLAR_PROUD` | 10.95 | 12.2205 |
| `MOUTH` | 11.52 | 11.32 |
| `GRIP` | 1.9465 | 2.2205 |
| `SLIT_D` | 4.9465 | 6.2205 |
| `SLIT_IN` | -- | 3.6789 |

**`hinge`** — the joint was replaced rather than adjusted, which makes this the longest tab by far.

| Name | draft9p3 | now |
| ---- | -------- | --- |
| `GAP` | 0.60 | 0.15 |
| `SLOT` | 11.2 | gone; the slot is `SEAT` 10.3 the whole way |
| `EAR` | 6.4 | 6.85 |
| `STUB_PROUD` | 1.6 | 1.30, engaging 1.15 |
| `TEETH` | -- | 24, 15&#176; apart |
| `VALLEY_D` | 2.0 | 1.70, straight through the ear |
| `TOOTH_PROUD` | 1.2 | 0.60, a 45&#176; cone flat-topped at 0.8 |
| `SLIT` | -- | 4.0, splitting the tongue into two 3.0 leaves |
| `TAB_FREE`, `EAR_FREE` | 12 and 12 | 20 and 21 |
| `MOVE` | 1.0 | 0.45 |
| `FLAT`, `LIMB_FLAT` | -- | 10.8387 and 21.6774 |

**`u limb` and `l limb`** — `ROD_FORK` 17, `ROD_BLADE` 18 and `ROD_ARM` 32 are new names, and both
limbs are cut flat top and bottom on the same section the hinge uses.

**The gripper's `CLIP_W` and the robot's `HEIGHT` also moved.** Neither tab is in this draft.

## Phase A — the briefs come current before any CAD

Every number in the build comes from `make_plans.py` by import. The brief is corrected first,
because `.parts/onshape.md` makes its Variables table the only thing that can create a variable:
*"a number is a variable when it has a row there, and is not one otherwise."*

- **A1.** `.docs/robot-build-plan.md`: `#wall` reads 3 where the model builds 1.8; the `#slit_in`
  and `#slit_out` notes cite a collar radius of 9.0 that is now 7.8; there is no `#seat` row, and
  the ear row references one.
- **A2.** Add the rows the six studios need and the table lacks, so B1 has names to use. Every one
  of them is argued for here and created there; a run plan may ask for a row and does not make one.
- **A3.** Sweep the rest of the brief for numbers those six studios depend on. Report anything
  outside them rather than fixing it.
- **A4.** `.docs/experiments/build-briefs/hinge.md` is archive and two revisions stale. Leave it,
  and put one line at its top naming what supersedes it.
- **A5.** `ninja plan hinge-figures check`, and read the hinge sheet as rendered.

Phase A closes when `make_plans.py` and the brief agree on every row the six studios use.

## Phase B — the edits

Seven tabs. Read each one back before starting the next; a wrong number found at B3 costs one tab
and the same number found at C costs six.

- **B0.** Create `stickbot-draft9p1p4`. Copy the four tabs in. Record every element id in
  `build-notes.md`, and record for each copied tab whether any feature still references its old
  document, which is the defect a copy creates and nothing else reports.
- **B1.** `robot sizes`, written fresh from the corrected table. No Part Studio redeclares a name
  this studio holds; `.parts/onshape.md` records five such locals in draft9p1's `ball and socket`
  and four in its `foot`, each shadowing a row that had moved without them.
- **B2.** `ball and socket`. The eight rows above, the four tab variables draft9p3 is missing
  (#119), and the connect-to-robot connector that infers `CENTROID` where it wants `CENTER` (#118).
- **B3.** `hinge`. The settled joint, edited in over draft9p3's construction. Its fourteen variable
  features still carry Onshape's default `###name = #value`; each is renamed for what it holds.
  Build in two stages and read back between them: the mechanical joint with no teeth, then the
  valleys and the cones. `fork` and `blade` get their names here (#138), `BLADE_OUT` stops being
  typed where the rule beside it derives it (#140), and the two robot connectors stop being placed
  by two different rules (#141, #142).
- **B4.** `u limb`. `ROD_FORK`, the flats, and the shoulder profile's missing projected edge (#125).
- **B5.** `l limb`, copied from draft9p1. `ROD_BLADE` and the flats.
- **B6.** `ball with cylinder` — the ball stud derived from `ball and socket`, on a Ø `#limbD`
  cylinder, so a person can hold it.
- **B7.** `socket with cylinder` — the socket derived the same way, on the same cylinder, so the
  pair presses together. Neither coupon resketches a joint that already exists in another tab.
  Both stand the joint center 22 from the cylinder's far face, and they get that from `#stand` and
  `#collar` being equal rather than from a typed number.

**The recorded findings are fixed as the tabs are edited, not afterward.** Each is already written
up with its symptom. A fix that turns out to be wrong is recorded as a deviation and carried, the
way a take does.

## Phase C — prove it

Against `make_plans.py` by import, never by transcription.

**Every sketch reports fully defined.** Read with `tools/read_sketches.py`. A sketch that is not is
a defect in the tab that holds it, not a note for later.

**One driving dimension changes and the model stays proportioned.** This is the acceptance test in
[`../../../../.parts/modeling-practice.md`](../../../../.parts/modeling-practice.md), and it is what
this draft is for. Drive `#torsoH` and `#limbD` in `robot sizes`, rebuild all six studios,
re-measure, and put them back. A studio that comes back as a pile of disconnected parts fails the
draft, however right it looked at its first size.

**No reference leaves the document.** Every derive, every mate connector and every sketch reference
names an element in `stickbot-draft9p1p4`'s own workspace.

**The geometry agrees with the design source.** `check.py` from
[`../2026-08-30-draft9p1p2/`](../2026-08-30-draft9p1p2/) already holds most of these rows and is
brought forward; its `sk_slot` and its *relieved slot* row are corrected for the removed land first.
It is a check script, not a source of CAD, and nothing in `stickbot-draft9p1p2` is opened to write
it.

| What | Expected |
| ---- | -------- |
| parts in `hinge` | 2, named `fork` and `blade` |
| ear to tongue | 0.15 a side, everywhere the two touch |
| the slot | 10.3 from the fork's tip to its root, no step anywhere in it |
| axle engaged in the bore | 1.15 |
| valleys | 24, Ø1.70, through the ear, on r 8.8387 |
| teeth | 24, 45&#176; cones, base Ø2.00, flat top Ø0.80, standing 0.60 |
| tongue root, ear root | 20 and 21 from the pin |
| the flats | 21.6774 across the chord, each face 10.3 wide, on both limbs and on the hinge |
| joint center to joint center, both limbs | 48 |
| coupon joint center to the cylinder's far face | 22, on both coupons |
| every robot connector | on its own end face, on the axis, pointing out |
| features carrying a default name | none, in any tab |

**Then look at it.** Six studios opened and turned through several orientations, per the *Model
inspected* gate. A report about a model is not the model.

## What this draft does not do

- It does not build the torso, the head, the foot, the gripper or an assembly.
- It does not touch `instructions/`. No page teaches this joint set, and none should until the CAD
  it would be written from has passed Phase C.
- It does not export STLs. The deliverable is the construction; a print comes from a later draft
  that starts here.
- It does not repair draft9p3 or draft9p1. Both are left as they are, and the findings this draft
  fixes stay open against them.

## What we do not know yet

- **How much of draft9p3's hinge survives the settled joint.** Its construction is worth keeping and
  its joint is the one from before the sweep. If editing costs more than the construction is worth,
  B3 says so in the log and draws the tab from the origin out, which is a deviation and gets
  recorded as one.
- **What a copied tab's references point at.** A copy that still derives from draft9p3 regenerates
  clean and is wrong, which is the failure `.parts/onshape.md` describes. B0 measures it; nobody has
  measured it before.
- **Whether a constraint web posted over REST behaves like one drawn by hand.** Onshape accepts a
  feature that produced nothing, and accepts constraints that leave a sketch under-defined. The
  fully-defined read and the variable drive are how we find out.
- **What draft9p1p2 and draft9p1p3 should become.** Both are on the account, neither is a source,
  and one of them has no run directory in this repository at all. Deleting, archiving or registering
  them is a decision for Mike, not for this plan.
