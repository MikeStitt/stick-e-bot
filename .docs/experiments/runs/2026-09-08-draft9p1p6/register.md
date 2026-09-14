# draft9p1p6 — the register

What this draft built, what it proved, and what it leaves open. The measurements come from
[`check.py`](check.py), which imports `instructions/robot-guide/make_plans.py` and reads the model
back through `bodydetails`, `parts` and `boundingboxes`; [`build-notes.md`](build-notes.md) says how
each tab was edited and where the build departed from [`plan.md`](plan.md).

This draft writes no page. It is a CAD reference to print from and to inherit.

## Where the work is

| What | Value |
| ---- | ----- |
| document | `stickbot-draft9p1p6`, owned by Mike Stitt |
| document id | `500752af84dc92deea53f9e4` |
| workspace id | `f30bf96cfeece59f61e0e7b2` |
| version | `F done - Phase F proved`, id `80c22eb7b8b0342ac03f8a6d` |
| version microversion | `dd821b5b9c8498eb568aee67` |

- The version, to cite:
  <https://cad.onshape.com/documents/500752af84dc92deea53f9e4/v/80c22eb7b8b0342ac03f8a6d>
- The **live** workspace, for anyone who needs to edit rather than read:
  <https://cad.onshape.com/documents/500752af84dc92deea53f9e4/w/f30bf96cfeece59f61e0e7b2>

**Which of these were opened.** The workspace link was opened, in the agent's own browser, and the
twelve frames behind *What it looks like* below were taken from it. **The version link was not
opened.** Its id and name were read back over REST from `GET /api/documents/d/{did}/versions`
immediately after publishing, and the URL above is that id assembled into the document's URL rather
than a link that was followed.

**This one was printed.** Mike printed the fifteen degree joint from this design and reports it good
in the hand. That settles the three rows the printer decides: `#t_print` at 0.10 mm, `#wedge_h` at
0.75 mm and `#wedge_c` at 0.15 mm all stand in a part he has held.

| Tab | Element | Type |
| --- | ------- | ---- |
| `robot sizes` | `5e9a0328a109ff92f5f6e9aa` | Variable Studio |
| `ball and socket` | `88ea6b759912b789d6de4647` | Part Studio |
| `hinge` | `62fca6aa5a67b51adcb2318c` | Part Studio |
| `u limb` | `f3f8362fd5e9f31ee2fa5eb2` | Part Studio |
| `l limb` | `261b7ee66567bab16d145c83` | Part Studio |
| `ball with cylinder` | `a1992995b5a775f59d76d561` | Part Studio |
| `socket with cylinder` | `e7dca601f00ea49c3f212d0f` | Part Studio |

## What it looks like

![The hinge, seen down the joint axis: twenty-four wedges in a ring that runs out to the ear's
straight side, crests pointed over the inner part of the ring, the axle at the
center.](hinge-ring.png)

![The same hinge in isometric: the fork's ear carrying its ring, the blade behind it, the axle
standing proud.](hinge-iso.png)

## What was built

One document holding a Variable Studio and six Part Studios, with eight parts among them. It is a
copy of `stickbot-draft9p1p5` with five variable expressions changed and nothing redrawn.

| Tab | Parts | Runs from | to |
| --- | ----- | --------- | -- |
| `robot sizes` | | 23 rows | |
| `ball and socket` | `ball stud`, `socket body` | the socket's base at -10 mm | the stud's face at +10 mm |
| `hinge` | `blade`, `fork` | the blade's rod end at -38 mm | the fork's rod end at +38 mm |
| `u limb` | `u limb` | the fork's tip at -60 mm | the socket's rim at +2.2205 mm |
| `l limb` | `l limb` | the ball's far pole at -54 mm | the tongue's tip at +12 mm |
| `ball with cylinder` | `ball with cylinder` | the ball's far pole at -6 mm | the handle's far face at +22 mm |
| `socket with cylinder` | `socket with cylinder` | the handle's far face at -22 mm | the socket's rim at +2.2205 mm |

Every station is on the joint axis with the joint center at zero. These are draft9p1p5's stations
unchanged except across the rod: the limb's flat moved out with `#gap`, so all six studios now stand
between `x ±10.4494 mm` rather than `x ±10.3923 mm`. The joint changed, and nothing outside it
moved.

## Resolved

`check.py` runs 166 rows across the six Part Studios and all 166 agree.

- **The fifteen degree joint is built, on both members.** Twenty-four wedges on each of four faces:
  crest tops at `y ±5.75 mm` on the blade's leaves and `y ±5.15 mm` on the fork's ears, one crest
  measuring 0.4972 mm². Each wedge's flanks are cones of half angle 45.000°, twenty-four at
  `r 10.4494 mm` and twenty-four at `r 6.0000 mm` off every one of the four faces, all leaning
  inward.
- **The ring runs right out to the limb's flat.** `RING_OUT` and `FLAT` are the same 10.4494 mm, so
  a wedge's outer end meets the cut that flattens the limb's top and bottom.
- **The crest comes to a point.** It is 0.447 mm wide at `r 9.6994 mm`, closes at `r 7.478 mm`, and
  inboard of that the wedge is a ridge whose height falls to 0.602 mm at `RING_IN`. That is drawn on
  purpose; what the printer leaves of it is what the print is being asked.
- **The joint closes on the numbers it was designed to.** Ear to tongue is 0.90 mm a side, the axle
  is engaged 2.10 mm in the bore, the pair opens 0.60 mm to ride a wedge, and 0.15 mm of air stands
  over a crest at a detent.
- **The axle is longer and the bore is tighter.** The stub stands 3.00 mm proud of each leaf and the
  bore is Ø4.10 mm against a Ø4.00 mm stub, which is 0.10 mm of diameter margin.
- **The leaves are tapered and the slit opens toward the tip.** The slit measures 0.80 mm a side at
  the tongue's root and 3.50 mm a side at its tip, and neither wall is square to the leaves.
- **The rod is a Ø24 mm cylinder with two flats**, on the hinge and on both limbs: 20.8988 mm across
  the chord, with an 11.8 mm flat at `x +10.4494 mm` and another at `x -10.4494 mm`.
- **Both limbs measure 48 mm between joint centers.**
- **Each coupon is half the ball joint on a limb-thick handle**, 22 mm from joint center to the
  handle's far face, both derived rather than drawn.
- **The whole document holds its face census when the robot's size is driven.** All eight bodies
  across the six studios were counted by surface type, then `#torsoH` was driven to 120 mm and
  `#limbD` to 30 mm and both put back. Every studio rebuilt with the same parts and the same faces
  at both driven sizes, no feature reported an error, and the way back is exact: every face count
  and every bounding box is what it was.

  | Body | Faces by surface type |
  | ---- | --------------------- |
  | `ball and socket` / socket body | 17 plane, 1 cylinder, 1 sphere |
  | `ball and socket` / ball stud | 1 plane, 1 cylinder, 1 sphere |
  | `hinge` / fork | 150 plane, 6 cylinder, 96 cone |
  | `hinge` / blade | 156 plane, 6 cylinder, 96 cone |
  | `u limb` | 166 plane, 7 cylinder, 96 cone, 1 sphere |
  | `l limb` | 156 plane, 7 cylinder, 96 cone, 1 sphere |
  | `ball with cylinder` | 2 plane, 2 cylinder, 1 sphere |
  | `socket with cylinder` | 18 plane, 2 cylinder, 1 sphere |

  Ninety-six cone faces is 24 wedges times two flanks times two faces.

- **The ring holds across the design range.** 96 cone faces on both hinge bodies at `#limbD` 18, 20,
  22, 24, 25, 26, 27, 28, 30, 32, 33 and 33.5 mm.
- **Nothing reaches outside the document.** `externalreferences` reports an empty list for all seven
  elements under both `elementExternalReferences` and `elementRevisionReferences`, no element has a
  workspace reference, and the only document and version the route names are this document's own.
  Every feature of all six Part Studios was also searched for draft9p1p5's document, workspace and
  element ids, with no hit.

### The forces the joint was sized for

Calculated, not measured. Mike's targets for this draft were a fifteen degree step in the hand and a
pinch to insert no greater than 100 N.

| What | draft9p1p5 | draft9p1p6 |
| ---- | ---------- | ---------- |
| detent torque, frictionless | 490 N·mm | 641 N·mm |
| detent torque at µ 0.35 | 1018 N·mm | 1332 N·mm |
| pinch force to insert, at x 30 mm | 39.2 N | 75.2 N |
| press force if pushed straight in instead | 93.5 N | 182.7 N |
| twist to break the joint open | 923 N·mm at 8.4° | 1889 N·mm at 13.3° |
| stress at a detent | 10.7 / 6.8 MPa | 12.9 MPa ear, 8.4 MPa leaf |
| stress at the pinch | 20.1 MPa | 38.3 MPa |
| yield | 50 MPa | 50 MPa |
| wedges carrying at any moment | 2 of 12 | 4 of 24 |

The pinch is the case that runs closest to yield, at 1.30 times margin. The detent holds 51 times
what the elbow needs to carry the arm's weight, so the joint is not near its useful limit; the pinch
is.

**Doubling the ring bought no torque on its own.** Twelve wedges and twenty-four give the same
641 N·mm with everything else held. The 31 % rise over draft9p1p5 is 24 % from closing `#gap`, which
raises the climb to 0.60 mm, and 5 % from the ring moving out to the flat. What the twenty-four
wedges buy is the step Mike asked for.

## What is open

- **The blade loses a wedge at `#limbD` 34 mm.** The blade comes back with 94 cone faces there and
  the fork with 96; at 36 mm it is 90 and 92, and at 40 mm 82 and 84. No feature reports anything.
  draft9p1p5 held to 34 mm and broke at 35 mm, so the finer ring gives up a millimeter. 34 mm is
  1.42 times the built 24 mm, so it is outside the design range and was not chased.
- **The forces above are still calculations.** The print says the joint is good in the hand; it does
  not give a detent torque or a pinch force. The one measurement the printed draft9p1p5 gave
  corrected the leaf tip deflection by 1.98 times.
- **There is no coupon for the wedge ring.** The two coupons in this document are the ball joint's.
- **The pinch has never been measured.** Mike has said he will put a kitchen scale under one.
- **The `hinge` tab still mixes two variable naming conventions.** Ten variables carry the GUI's
  `###name = #value` template as their feature name and six carry a bare name. This draft had the
  REST grant that would close it and `plan.md` does not ask for it, so it was left rather than
  folded in.
- **`l limb`'s rod may reproduce volume the derived blade's own arm already occupies.** Inherited
  from draft9p1p5, not run to ground, and not checked at all for `u limb`.

## Requirements

`req.carry.register` asks which requirements were met, missed and deferred.

| Requirement | Standing |
| ----------- | -------- |
| `req.model.one_document` | Met. Seven tabs in one document, no reference leaving it. |
| `req.model.derive` | Met. The ball joint is drawn once in `ball and socket` and derived into the limbs and both coupons; the hinge's two parts derive into the limbs. |
| `req.model.design_intent` | Met. All eight bodies hold their face census under a driven `#torsoH` and `#limbD`, and the hinge holds its across `#limbD` 18 mm to 33.5 mm; the whole of Phase D was five expressions, which is what a model with design intent costs to change. |
| `req.model.named_features` | Met for the model. This draft takes no teaching frames. |
| `req.model.same_structure` | Met. |
| `req.model.anchored` | Met but for the lower limb's rod, which offsets from a plane where a face was available. Inherited from draft9p1p4. |
| `req.model.visible_geometry` | Met everywhere except that same offset. |
| `req.model.posed` | Not in play. This draft builds no assembly. |
| `req.carry.conventions` | Not in play. This draft writes no page. |

## What the next draft inherits

The version above, and four things that cost this draft time:

- **A Variable feature stores one expression per variable type, and the model reads the one the type
  names.** Writing the generic `value` parameter is accepted, reads back, keeps every feature status
  green and drives nothing. Write `lengthValue`, `angleValue` or `numberValue` to match
  `variableType`.
- **A default that reaches somebody else's session is the failure.**
  `onshape_session.CDP_URL` was 9222, the signed-in browser a person is using, and only
  `onshape_gui.connect()` moved it to 9223. This draft's Phase C and Phase D ran there before a
  capture of a sign-in screen gave it away. The default is 9223 now and 9222 is named when it is
  wanted; earlier drafts' `check.py` scripts pick the fix up without an edit.
- **Ask the model, not the feature.** `getVariable` at the end of the tree, or a face census off
  `bodydetails`, tells a change that reached the geometry from one that did not. A feature list
  answers with what was written to it either way.
- **Onshape's copy and version routes drop the `d/`.** `POST /documents/{did}/workspaces/{wid}/copy`
  and `POST /documents/{did}/versions` answer; the `/d/{did}/w/{wid}/` forms beside them 404. A
  `GET` on the same shape tells them apart before a write does.

[`../../onshape-gui-howto.md`](../../onshape-gui-howto.md) carries all four.
