# draft9p1p5 — the wedge hinge

**This draft replaces the hinge's detent mechanism.** The teeth and the valley holes go; twelve
pie-slice wedges stand proud of both mating faces in their place, the tongue's leaves taper, and the
axle grows. Nothing else about the robot moves.

This plan supersedes the one written on 2026-09-04 for a draft that closed draft9p1p4's open
constructions. That draft is folded in as Phase E, because the tabs it touches are the tabs this one
rebuilds and doing them twice would be wasted work.

## Why the mechanism is being replaced

The printed draft9p1p2 hinge holds `210 N·mm`, against `454 N·mm` as drawn. The whole shortfall is
in the valley: the joint achieves `0.208 mm` of its `0.450 mm` climb, which is what a valley mouth
of `Ø1.23 mm` instead of `Ø1.70 mm` would give. Mike's reading is that the support material printed
into the valley holes has not come out, and the `0.235 mm` of radial obstruction that fits the
measurement is one extrusion width — the signature of a torn support interface rather than a design
error.

**The design answer is to have no holes.** A protrusion on both faces needs no support and has
nothing to clean out. That is the whole reason for the change; the rest of this plan is the
consequence.

## What Mike settled

- **Twelve wedges per face**, on both the blade and the fork, proud of both.
- **A detent target of `500 N·mm`**, on the frictionless basis the old `454 N·mm` was quoted on.
- **A pinch of no more than `40 N`** to assemble the joint. Assembly is now a pinch on the two
  leaves rather than a push down the slot, so insertion force stops being a design constraint and
  this replaces it.
- **The axle and its bore stay `Ø4.0 mm` into `Ø4.4 mm`.** Only how far the axle stands proud moves.
- **Backlash is accepted.** The wedges clear each other at a detent, so the joint is free through
  the flank clearance before anything touches.

## The one number that had to move

**The wedges are `0.75 mm` proud, not the `0.65 mm` Mike was willing to accept.** At `0.65 mm` the
best a `40 N` pinch can buy is `431 N·mm`, which misses the target by 14%. The reason is structural:
the pinch and the detent are both governed by the same piece of leaf, between its root and the pin,
so thickening the leaf raises both together and cannot break the tie. Only the wedge height can.
Climb is `h − c` while the axle's extra demand is `h + engagement − c`, so a taller wedge earns
climb faster than it costs engagement.

It stops paying at about `0.85 mm`, where the top face has been eaten by its own 45 degree ramps and
the leaves run out of slit during the pinch. `0.75 mm` is the last height with both.

## The settled numbers

Every one of these is a consequence of the four Mike settled plus `h`, `c` and the leaf's two
thicknesses. Nothing here is typed twice.

| Quantity | Value | Where it comes from |
| -------- | ----- | ------------------- |
| wedges per face | 12 | settled; a detent every `30°` |
| wedge proud, `h` | 0.75 mm | the only free height; see above |
| tip clearance, `c` | 0.25 mm | at least `2t`, so the tips still clear at `t 0.10 mm` of over-print |
| face gap at a detent | 1.00 mm | `h + c` |
| climb | 0.50 mm | `2h − g`, which is `h − c` |
| slot, `#seat` | 12.00 mm | `#blade + 2 × #gap` |
| ear | 6.00 mm | `(#limbD − #seat) / 2` |
| flat off the axis | 10.3923 mm | `sqrt((#limbD / 2)² − (#seat / 2)²)`, and it moved because the slot did |
| ring outer radius | 9.9923 mm | `#flat − 0.4`, leaving `0.4 mm` of face outboard |
| ring inner radius | 6.00 mm | chosen; it clears the `Ø4.4 mm` bore with `3.8 mm` of boss |
| where the fit is set | 9.4923 mm | `r_o − g/2`, half way up the gap, where the radial drafts have taken least |
| what the 45° drafts lean | 6.0388° | `2 asin(g/2 / r_bind)`; both members lean away from each other |
| flank clearance a side | 1.2072° | `2t / r_bind`, the angle a flank needs where the two come closest |
| wedge angular width | 19.8316° | `180°/N + lean − ε`, which is wider than a half step and has to be |
| leaf at its root | 4.20 mm | sized so the pinch lands on the cap |
| leaf at its tip | 1.50 mm | as thin as the print allows; the taper is nearly free |
| slit at the root | 1.60 mm | `#blade − 2 × leaf root` |
| slit at the tip | 7.00 mm | `#blade − 2 × leaf tip` |
| axle proud | 2.10 mm | `2h + 0.60 mm` of engagement left while riding |
| axle, bore | 4.0 mm, 4.4 mm | unchanged |

**What it does, by the model in `tools/`:**

| | Value | Against |
| --- | ----- | ------- |
| detent torque | 490 N·mm | the `500 N·mm` target, 2% under, and inside the model's own accuracy |
| the same with `µ 0.35` | 1018 N·mm | what a hand feels leaving a detent |
| holding margin | 19× | the `26 N·mm` the arm's weight asks of the elbow |
| pinch to assemble | 39.2 N | the `40 N` cap, with the finger at `x 30 mm` |
| twist-off | 923 N·mm | `8.2 lbf·in`, and a floor; the same hand turns it at `1018 N·mm` |
| twist to let go | 8.4° | wrung about the limb, from straight |
| backlash | 2.41° | 8% of a `30°` step |
| stress at a detent | 10.7 MPa | `50 MPa` yield |
| stress at the pinch | 20.1 MPa | the same, and this is the governing case |
| engaged while riding | 0.60 mm | it has to stay above zero at every detent crossing |

## What is assumed, and can be overruled

- **The finger lands at `x 30 mm`**, two millimeters short of the blade's tip. At the tip itself the
  pinch is `35.9 N`; two millimeters further in, at `x 28 mm`, it is `43.2 N` and over the cap. The
  leaf is sized for the middle of that.
- **`c 0.25 mm` spends `0.05 mm` of margin on print offset.** Dropping it to `0.20 mm` raises the
  detent to `545 N·mm` and leaves the tips exactly touching at `t 0.10 mm` of over-print. The
  measured printer runs under rather than over, so this is a cheap `56 N·mm` if Mike wants it.
- **PETG at `E 2000 MPa` and `50 MPa` yield**, `µ 0.35` on the ramps, print offset `t ±0.10 mm`.

## What Mike still has to answer

- **The build route.** The permission to write geometry over REST was given for
  `stickbot-draft9p1p2` and `stickbot-draft9p1p4`, in those words. It does not carry here.
  **Phase D is GUI work unless a fresh grant arrives**, which is a different pace for the same
  edits.
- **The Variables table rows.** `.parts/onshape.md` says a run plan may argue for a row and does not
  create one. Phase A argues for the rows in the table below; the CAD cannot name them until they
  exist.

## Phase A — the design source

- **A1.** `instructions/robot-guide/make_plans.py`: the wedge block replaces `TEETH`, `STEP`,
  `VALLEY_D`, `TOOTH_FLAT`, `CONE_D`, `TOOTH_PROUD` and `BUMP_R`. `GAP`, `SEAT`, `EAR`, `FLAT`,
  `LIMB_FLAT`, `SLIT`, `LEAF` and `STUB_PROUD` take their new values or their new rules.
- **A2.** `tools/hinge_spring.py` gains what the analysis needed and the old model could not do: a
  variable-`EI` member, so a tapered leaf can be integrated, and a ring of wedges in place of a row
  of teeth. It reproduces `454 N·mm` on the old geometry, and that check stays in the file.
- **A3.** `.docs/robot-build-plan.md`: the Variables table loses `#valley_d`, `#tooth_flat`,
  `#cone_d`, `#tooth_proud` and `#bump_r`, and gains `#wedges`, `#wedge_h`, `#wedge_c`,
  `#ring_in`, `#ring_out`, `#leaf_root` and `#leaf_tip`. `#gap`, `#seat`, `#ear`, `#flat`,
  `#slit` and `#stub_proud` change value under the names they already have.
- **A4.** Regenerate the plan sheets and the brief sheets from `make_plans.py`.

## Phase B — the sketches and the brief

- **B1.** `detail_hinge` redrawn: the wedge ring in plan, the section through a detent and through
  the ride, the tapered leaf, the axle's engagement at both positions.
- **B2.** The hinge build brief rewritten to the settled numbers, including how the joint is
  assembled, because that changed from a push to a pinch.
- **B3.** The hinge review document reconciled, since it argues from the tooth and the valley.

## Phase C — copy the document

- **C1.** Copy `stickbot-draft9p1p4` to `stickbot-draft9p1p5` from its named version. Record the
  document id and every element id.
- **C2.** Check that no feature still references `stickbot-draft9p1p4`. A copy creates that defect
  and nothing else reports it.

## Phase D — the CAD

- **D1.** `robot sizes`: the Variable Studio rows, added, changed and removed.
- **D2.** `hinge`: the teeth and the valleys deleted, the wedge ring patterned on both faces, the
  leaves tapered, the axle lengthened, the slot widened.
- **D3.** `u limb` and `l limb`: re-read after the hinge changes, since both derive it and both
  carry the flat that `#seat` moved.
- **D4.** The two coupons, if they still make sense against a joint that is pinched rather than
  pressed.

## Phase E — draft9p1p4's open constructions, folded in

- **E1.** `l limb`'s rod starts on the blade's root face rather than at a `#tab_free` offset.
  Task #168. Its sketch is one of the ones D3 re-reads, so it costs nothing extra here.
- **E2.** `Ball stud` and `Socket body` take the lower-case convention the other six parts use.

## Phase F — prove it

- **F1.** `check.py` comes forward from draft9p1p4, with the hinge's rows rewritten to the wedge.
  Rows that describe teeth or valleys are deleted rather than made to pass.
- **F2.** Every sketch reads fully defined. `#torsoH` and `#limbD` driven and put back.
- **F3.** No reference leaves the document.
- **F4.** Look at it, per the *Model inspected* gate: the ring on both faces, the taper, and the
  axle standing `2.10 mm` proud.
- **F5.** Publish a named version.

## Phase R — the register

`register.md`, carrying where the work is, what was built, what is open, and the acceptance numbers.

## What this draft does not do

- It writes no student page and takes no frame. Teaching the wedge joint is a later draft's work.
- It does not repair draft9p3 or draft9p1.
- It does not touch `stickbot-draft9p1p4`, which stays as the proved reference this one is diffed
  against.

## What we do not know yet

- **Whether the crest prints as a flat.** The crest runs `0.83 mm` across at the ring's inner end
  and `1.70 mm` at its outer, which is two to four extrusion widths. Nothing in the model knows what
  a slicer will do with it, but the widths are no longer marginal; this entry read `0.612 mm` while
  the wedge was `13.0901°` across, and the wedge is `19.8316°`.
- **Whether `39 N` is a pinch a middle-schooler can hold** while sliding a blade into a slot with
  the other hand. The number is a calculation, not a measurement.
- **Whether the twist-off figure is conservative enough.** It is a floor twice over: the leaf is
  assumed to carry a corner load through to the pin without dishing, and the lever is the contact
  radius `9.2423 mm` when the wedge tips reach `9.9923 mm`. Taken at face value the joint wrings
  apart at `923 N·mm` and turns at `1018 N·mm`, which is close enough to parity to matter. How much
  better it really is needs a plate model or a printed part.
