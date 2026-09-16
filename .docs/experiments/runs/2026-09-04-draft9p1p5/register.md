# draft9p1p5 — the register

What this draft built, what it proved, and what it leaves open. The measurements come from
[`check.py`](check.py), which imports `instructions/robot-guide/make_plans.py` and reads the model
back through `bodydetails`, `parts` and `boundingboxes`; [`build-notes.md`](build-notes.md) says how
each tab was edited and where the build departed from [`plan.md`](plan.md).

This draft writes no page. It is a CAD reference for a later draft to inherit, edit and print from.

## Where the work is

| What | Value |
| ---- | ----- |
| document | `stickbot-draft9p1p5`, owned by Mike Stitt |
| document id | `e5bdf1e586fb6c868066df22` |
| workspace id | `e051660ad432c2cfabda245b` |
| version | `F done - Phase F proved`, id `1f07c2dd2dd2e9f71653e336` |
| version microversion | `3dbeeb7e2749ce6f6e6aaf58` |
| commit | `6f26185c`, tagged `draft9p1p5` |

- The version, to cite:
  <https://cad.onshape.com/documents/e5bdf1e586fb6c868066df22/v/1f07c2dd2dd2e9f71653e336>
- The **live** workspace, for anyone who needs to edit rather than read:
  <https://cad.onshape.com/documents/e5bdf1e586fb6c868066df22/w/e051660ad432c2cfabda245b>

**Which of these were opened.** The workspace link was open in the browser for the whole build; every
number below was read out of that page. **The version link was not opened.** Its id and name were
read back over REST from `GET /api/documents/d/{did}/versions` immediately after publishing, and the
URL above is that id assembled into the document's URL rather than a link that was followed.

**This one was printed.** Mike printed `u limb` and `l limb` from this design on Mon 8 Sep 2026 and
reports the joint good in the hand. That makes this the baseline the next draft departs from, so the
commit above carries the annotated tag `draft9p1p5`, holding the design source, the sketches, the
briefs, the analysis and the requirements as the printed parts were built from.

| Tab | Element | Type |
| --- | ------- | ---- |
| `robot sizes` | `488fdaefc4a17161539cd730` | Variable Studio |
| `ball and socket` | `f4b91f8171bbdb4a1f2887e2` | Part Studio |
| `hinge` | `fabf61fe1595cea004e698fc` | Part Studio |
| `u limb` | `be352936e6f596171a1a6b56` | Part Studio |
| `l limb` | `09f2d53343884f37576b8cda` | Part Studio |
| `ball with cylinder` | `4154b7a2226e8d0fa60f7ea4` | Part Studio |
| `socket with cylinder` | `02f1a0ea965ace742efad3a8` | Part Studio |

## What was built

One document holding a Variable Studio and six Part Studios, with eight parts among them. It is a
copy of `stickbot-draft9p1p4` with the hinge's toothed ring replaced by a wedge ring.

| Tab | Parts | Runs from | to |
| --- | ----- | --------- | -- |
| `robot sizes` | | 23 rows | |
| `ball and socket` | `ball stud`, `socket body` | the socket's base at -10 mm | the stud's face at +10 mm |
| `hinge` | `blade`, `fork` | the blade's rod end at -38 mm | the fork's rod end at +38 mm |
| `u limb` | `u limb` | the fork's tip at -60 mm | the socket's rim at +2.2205 mm |
| `l limb` | `l limb` | the ball's far pole at -54 mm | the tongue's tip at +12 mm |
| `ball with cylinder` | `ball with cylinder` | the ball's far pole at -6 mm | the handle's far face at +22 mm |
| `socket with cylinder` | `socket with cylinder` | the handle's far face at -22 mm | the socket's rim at +2.2205 mm |

Every station is on the joint axis with the joint center at zero. All six studios stand between
`x ±10.3923 mm` and `y ±12 mm`, or `x ±12 mm` on the two coupons. These are draft9p1p4's stations
unchanged: the joint changed, and nothing outside it moved.

## Resolved

`check.py` runs 166 rows across the six Part Studios and all 166 agree.

- **The wedge joint is built, on both members.** Twelve wedges on each of four faces: crest tops at
  `y ±5.75 mm` on the blade's leaves and `y ±5.25 mm` on the fork's ears, one crest measuring
  3.1538 mm². Each wedge's flanks are cones of half angle 45.000°, twelve at `r 9.9923 mm` and
  twelve at `r 6.0000 mm` off every one of the four faces, all leaning inward. There are no valleys
  and no holes; the ring stands proud on both sides and meets its opposite number in air.
- **The joint closes on the numbers it was designed to.** Ear to tongue is 1.00 mm a side, the axle
  is engaged 1.10 mm in the bore, the pair opens 0.50 mm to ride a wedge, and 0.25 mm of air stands
  over a crest at a detent.
- **The leaves are tapered and the slit opens toward the tip.** The slit measures 0.80 mm a side at
  the tongue's root and 3.50 mm a side at its tip, so 1.60 mm across at the root and 7.00 mm at the
  tip, and neither wall is square to the leaves.
- **The slot has one wall a side and no step.** One face at `y +6 mm` and one at `y -6 mm`, each
  running from the fork's tip at -12 mm to its root at 21 mm.
- **The rod is a Ø24 mm cylinder with two flats**, on the hinge and on both limbs: 20.7846 mm across
  the chord, with a 12 mm flat at `x +10.3923 mm` and another at `x -10.3923 mm`.
- **Both limbs measure 48 mm between joint centers.**
- **Each coupon is half the ball joint on a limb-thick handle**, 22 mm from joint center to the
  handle's far face, both derived rather than drawn.
- **The model survives its driving dimensions.** `#limbD` driven to 18, 20, 22, 24, 25, 26, 27, 28,
  30, 32 and 34 mm, and `#torsoH` to 72, 84 and 120 mm, returns 48 cone faces on each of the
  hinge's two bodies at every size with no feature reporting an error. Forty-eight is twelve wedges
  times two crest walls times two faces.
- **The whole document holds its face census when the robot's size is driven.** All eight bodies
  across the six studios were counted by surface type at `#torsoH` 96 mm and again at 120 mm, and
  all eight came back identical, with no feature reporting an error in either state; driving back
  to 96 mm reproduces the first census exactly. This is the test that catches the class of defect
  `ear wedge outline` had, because a free length in a sketch surfaces as a face appearing or
  disappearing downstream.

  | Body | Faces by surface type |
  | ---- | --------------------- |
  | `ball and socket` / socket body | 17 plane, 1 cylinder, 1 sphere |
  | `ball and socket` / ball stud | 1 plane, 1 cylinder, 1 sphere |
  | `hinge` / fork | 78 plane, 6 cylinder, 48 cone |
  | `hinge` / blade | 84 plane, 6 cylinder, 48 cone |
  | `u limb` | 94 plane, 7 cylinder, 48 cone, 1 sphere |
  | `l limb` | 84 plane, 7 cylinder, 48 cone, 1 sphere |
  | `ball with cylinder` | 2 plane, 2 cylinder, 1 sphere |
  | `socket with cylinder` | 18 plane, 2 cylinder, 1 sphere |

- **Every sketch reads fully defined**, which took a repair: `ear wedge outline` was missing the
  coincident tying one line's end to the outer circle. [`build-notes.md`](build-notes.md) § *F2* has
  the diagnosis and why the colors-only read that first passed this gate was unsound. That read is
  not what this claim rests on; the census above is.
- **Nothing reaches outside the document.** `externalreferences` reports an empty list for all seven
  elements under both `elementExternalReferences` and `elementRevisionReferences`, no element has a
  workspace reference, and the only document and version the route names are this document's own.

### The forces the joint was sized for

Calculated, not measured. Mike's two targets were a detent torque near 500 N·mm and a pinch force no
greater than 40 N.

| What | Value |
| ---- | ----- |
| detent torque, frictionless | 490 N·mm |
| detent torque at µ 0.35 | 1018 N·mm |
| pinch force to insert, at x 30 mm | 39.2 N |
| press force if pushed straight in instead | 93.5 N |
| twist to break the joint open, at 8.4° | 923 N·mm |
| stress at a detent | 10.7 MPa in an ear, 6.8 MPa in a leaf |
| stress at the pinch | 20.1 MPa |
| yield | 50 MPa |
| wedges carrying at any moment | 2 of 12 |

## What is open

- **The blade loses one wedge per face above `#limbD` 34 mm.** At 35 mm the blade comes back with
  11 wedges on each of its two faces instead of 12 while the fork keeps all twelve, and no feature
  reports anything. 35 mm is 1.46 times the built 24 mm, so it is outside the design range and was
  not chased. Which wedge goes, and to what, is unknown.
- **There is no coupon for the wedge ring.** The two coupons in this document are the ball joint's.
  A printable half-joint that tests the detent torque and the pinch force is the obvious next
  artifact and is left for Mike to call.
- **The forces in the table above are still calculations.** The print says the joint is good in the
  hand; the detent torque, the pinch force and the backlash all want a measurement before they are
  believed.
- **The `hinge` tab mixes two variable naming conventions.** The ten variables this draft added were
  made in the GUI, which stores a variable's name as the template `###name = #value`; the six older
  ones were made over REST under an override that does not carry to this document. It is cosmetic
  and no geometry depends on it, and closing it needs a REST grant.
- **`l limb`'s rod may reproduce volume the derived blade's own arm already occupies.** Seen in
  Phase E and not run to ground; not checked at all for `u limb`.
- **Two sketch dialogs were found open** in `u limb` and `l limb`, each rolling its tab's tree back
  behind `limb section`. Both were closed and `check.py` re-run clean, so nothing was lost, but a
  build that leaves a dialog open leaves a tab displaying a part the document does not have.
- **`#gap` changed meaning here**, from a fit to a space, and `#t_print`, `#wedge_h` and `#wedge_c`
  were added beside it. The print settles all three at the values in the table.
- **"Wedge Joint, Sized" is superseded.** That artifact carries pre-40 N numbers and the earlier
  13.09° wedge width; this document's `#wedge_w` computes 19.832°.

## Requirements

`req.carry.register` asks which requirements were met, missed and deferred.

| Requirement | Standing |
| ----------- | -------- |
| `req.model.one_document` | Met. Seven tabs in one document, no reference leaving it. |
| `req.model.derive` | Met. The ball joint is drawn once in `ball and socket` and derived into the limbs and both coupons; the hinge's two parts derive into the limbs. |
| `req.model.design_intent` | Met, after the repair. All eight bodies hold their face census under a driven `#torsoH`, and the hinge holds its across `#limbD` 18 mm to 34 mm; three dimensions in `fork blade top cut outline` are typed rather than named, and are draft9p1p4's three carried forward. |
| `req.model.named_features` | Met for the model. This draft takes no teaching frames. |
| `req.model.same_structure` | Met. |
| `req.model.anchored` | Met but for the lower limb's rod, which offsets from a plane where a face was available. Inherited from draft9p1p4. |
| `req.model.visible_geometry` | Met everywhere except that same offset. |
| `req.model.posed` | Not in play. This draft builds no assembly. |
| `req.carry.conventions` | Not in play. This draft writes no page. |

## What the next draft inherits

The version above, and four things that cost this draft time:

- **A pixel test can say a sketch is under-defined; it cannot say a sketch is not.** The test that
  earns that claim is driving the design's own dimensions and requiring the face census to hold,
  because that is what a free length shows up in.
- **A sketch edit is not on the server until the sketch is committed.** A REST read taken while the
  editor is open answers with the last committed geometry, so it cannot tell a constraint that took
  from one that did not, and it reads as failure either way. Four repairs were applied, checked
  against that read, and thrown away before the gate was moved to the screen.
- **`n` is not deterministic**, and a Back view mirrors every pixel offset a calibration rests on.
  Accept the view only when a known point lands where the calibration predicts.
- **The left rail's buttons carry no label of any kind.** Each one's `svg` `<use>` names its sprite
  instead, and `#svg-icon-create-version-button` is the one that publishes a version.

[`../../onshape-gui-howto.md`](../../onshape-gui-howto.md) carries all four.
