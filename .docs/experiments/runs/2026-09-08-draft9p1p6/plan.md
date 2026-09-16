# draft9p1p6 — fifteen degree detents

**This draft halves the detent step and spends the printed joint's margin on holding it.** The
wedge ring goes from twelve wedges to twenty-four, its outer edge moves out to the limb's flat, the
crest is allowed to come to a point, the axle grows to `3.00 mm` proud into a bore `0.1 mm` larger
than itself, and the two faces close `0.1 mm`. The leaves and the rod stay where draft9p1p5 left
them.

**Closing the two faces moves the slot and the limb's flat with them.** The slot is the tongue plus
a gap each side, so taking `0.1 mm` off each gap takes `0.2 mm` off the slot; the ear is what the
slot leaves of the limb, so it gains `0.1 mm`; and the flat is cut where the ear's inner face
crosses the rod, so it moves `0.0571 mm` further out and the limb stands `20.8988 mm` top to bottom
instead of `20.7846 mm`. None of that was asked for and all of it follows, so it is named here
rather than discovered in the CAD.

draft9p1p5 is the baseline, and it is a printed one. Mike printed `u limb` and `l limb` from it on
Mon 8 Sep 2026 and reports the joint good in the hand. The commit is tagged `draft9p1p5`; the CAD is
Onshape `stickbot-draft9p1p5`, version `F done - Phase F proved`.

## What Mike settled

- **A detent every `15°`**, which is twenty-four wedges on each of the four faces.
- **The ring runs out to where it touches the fork's top and bottom edge**, so its outer radius is
  the flat itself rather than `0.4 mm` inboard of it.
- **The crest may come to a point.** Drawing a shape the printer will round is not a reason to draw
  a different shape. What the printer does to a point is something the print reports, not something
  the drawing decides.
- **The axle stands `3.00 mm` proud**, up from `2.10 mm`.
- **`0.1 mm` of total diameter margin between the axle and its bore**, down from `0.4 mm`.
- **The two faces close `0.1 mm`**, which is the same edit as taking `0.1 mm` off the air over a
  crest, because the gap is the wedge plus that air.
- **The pinch to insert may reach `100 N`**, up from `40 N`, because the printed joint went together
  much more easily than the model said it would and the model is the weaker evidence until a scale
  says otherwise.

**The priority is the fifteen degree step in the hand.** Where a number and the felt experience
disagree in this draft, the experience wins and the print settles it.

## What the printed joint already corrected

The pinch model overstates how far the leaf tips close, by `1.98 ×`. Drawn, the slit at the tip is
`7.00 mm`; the model closes it to `1.07 mm` at the travel insertion needs, and Mike measures
`4.00 mm` on the part. The likely cause is the load: the model puts a point force at `x 30 mm`,
which rotates the tip hard, where a finger pad spreads it and rotates it much less.

The consequence for this draft is that the slit is not the constraint it was calculated to be. On
the measurement, the tips do not touch until the axle stands about `3.57 mm` proud, so `3.00 mm`
clears with `1.55 mm` of slit to spare.

**Which way the force is wrong is not known.** The measurement fixes the deflected shape, not the
stiffness. A kitchen scale under a pinch, squeezed until the stubs clear, is the one reading that
would settle it, and Mike has said he will take it later.

## The settled numbers

Everything here follows from the seven Mike settled plus the wedge height, the leaf's two
thicknesses and the print offset, all of which stay at draft9p1p5's values.

| Quantity | draft9p1p5 | draft9p1p6 | Where it comes from |
| -------- | ---------- | ---------- | ------------------- |
| wedges per face | 12 | 24 | settled; a detent every `15°` |
| wedge proud, `h` | 0.75 mm | 0.75 mm | unchanged |
| air over a crest, `c` | 0.25 mm | 0.15 mm | settled; the faces close by the difference |
| face gap at a detent | 1.00 mm | 0.90 mm | `h + c` |
| climb | 0.50 mm | 0.60 mm | `2h − g` |
| slot, `#seat` | 12.00 mm | 11.80 mm | `#blade + 2g`, and it follows the gap |
| ear | 6.00 mm | 6.10 mm | `(#limbD − #seat) / 2` |
| flat off the axis | 10.3923 mm | 10.4494 mm | `sqrt(nose² − (seat/2)²)`, and it followed the slot |
| ring outer radius | 9.9923 mm | 10.4494 mm | settled; it is `#flat`, so the ring touches the edge |
| ring inner radius | 6.00 mm | 6.00 mm | unchanged; it still clears the bore |
| where the fit is set | 9.4923 mm | 9.9994 mm | `r_o − g/2` |
| where a flank bears | 9.2423 mm | 9.6994 mm | `r_o − h`, and the lever the detent acts on |
| the two 45° leans | 6.0388° | 5.1587° | `2 asin(g/2 / r_bind)` |
| flank clearance a side | 1.2072° | 1.1460° | `2t / r_bind` |
| wedge angular width | 19.8316° | 11.5127° | `180°/N + lean − ε` |
| backlash | 2.4144° | 2.2920° | `2ε`, now 15% of a `15°` step |
| axle proud | 2.10 mm | 3.00 mm | settled; `2h + 1.50 mm` still engaged while riding |
| bore | Ø4.4 mm | Ø4.1 mm | settled; `#stub + 0.1 mm` |
| axle engaged at a detent | 1.10 mm | 2.10 mm | `#stub_proud − #gap` |

**The crest points itself.** At `11.5127°` across the base with 45° sides, the two sides meet before
reaching full height anywhere inboard of `r 7.478 mm`, so the ridge runs as a true point over most
of its length and keeps a flat only at its outer end, `0.45 mm` across at `r 9.70 mm` where the radial
draft cuts it off. Nothing forces the point; the pitch produces it. That is what the print is being
asked about.

## What it does, by the model in `tools/`

| | draft9p1p5 | draft9p1p6 | Against |
| --- | ---------- | ---------- | ------- |
| detent torque, frictionless | 490 N·mm | 641 N·mm | no target; the `500 N·mm` one was set for a `30°` step |
| the same at `µ 0.35` | 1018 N·mm | 1332 N·mm | what a hand feels leaving a detent |
| holding margin | 19 × | 25 × | the `26 N·mm` the arm's weight asks of the elbow |
| a hand 150 mm out | 0.33 kgf | 0.44 kgf | what it takes to move the elbow at the wrist |
| pinch to insert | 39.2 N | 75.2 N | the `100 N` cap, finger at `x 30 mm` |
| stress at the pinch | 20.1 MPa | 38.3 MPa | `50 MPa` yield, so `1.30 ×` where it was `2.49 ×` |
| stress at a detent | 10.7 MPa ear | 12.9 MPa ear, 8.4 MPa leaf | the same yield |
| twist to break open | 923 N·mm | 1889 N·mm | and both are floors |
| it lets go at | 8.4° | 13.3° | wrung about the limb, from straight |
| wedges carrying | 4 of 12 | 4 of 24 | the beams lift the rest clear either way |
| flank in contact | 15.513 mm² | 21.411 mm² | at the moment a detent starts to break |
| engaged while riding | 0.60 mm | 1.50 mm | it has to stay above zero at every crossing |
| slit left at the tip, pinched | 4.00 mm | 1.27 mm | scaled from Mike's measurement, not from the model |

**Doubling the ring bought no torque.** Hold the rest of the joint still and 12 wedges and 24 give
the same `641 N·mm`, because only four of them ever carry and the beams lift the rest clear either
way. The `31 %` gain over draft9p1p5 comes from somewhere else: closing `#gap` by `0.10 mm` raises
`#climb` to `0.60 mm`, so the pair has to open further to turn, and that is `24 %` of it; the ring
moving out to `#flat` is the other `5 %`. Twenty-four wedges buy the `15°` step, which is what Mike
asked for, and nothing else.

**The joint now holds together harder than it turns.** draft9p1p5 wrings apart at `923 N·mm` and
turns at `1018 N·mm`, so on the floor estimate it could let go of the pin before it left a detent.
draft9p1p6 turns at `1332 N·mm` and wrings apart at `1889 N·mm`, which puts the failure the right
way round with `1.42 ×` between them. The longer axle is what bought that.

**The pinch margin is the one that got worse.** `38.3 MPa` against `50 MPa` yield is `1.30 ×`, where
draft9p1p5 had `2.49 ×`. It is still the governing case and it is still inside yield, but a leaf
squeezed by a hand that does not stop at `75 N` has less room than it had.

## What is assumed, and can be overruled

- **The ring's inner radius stays `6.00 mm`.** Mike named the outer edge and said nothing about the
  inner one. Leaving it there keeps the ring radially longer than draft9p1p5's, which is where most
  of the extra flank contact comes from, at the cost of a low ridge over the innermost millimeter.
- **The wedge height stays `0.75 mm`.** It is the number the printed joint was built at, and holding
  it is what makes the print a comparison rather than a fresh start.
- **The finger lands at `x 30 mm`**, as before, and the same caveat applies: the model's pinch is
  not calibrated.
- **PETG at `E 2000 MPa` and `50 MPa` yield**, `µ 0.35` on the ramps, print offset `t ±0.10 mm`.

## What Mike still has to answer

- **The build route. Answered on 2026-09-08: Mike granted REST for `stickbot-draft9p1p6` by
  name.** The earlier permission was given for `stickbot-draft9p1p2` and `stickbot-draft9p1p4` and
  did not carry; this is a fresh grant and it covers this document only. Phase D writes geometry
  over REST, and it writes it the way `.parts/onshape.md` requires: by editing the features
  draft9p1p5 already holds, with their constraints, patterns and mirrors intact, not by emitting
  fresh geometry because emitting is cheaper.
- **The Variables table rows.** Phase A argues for the rows; the CAD cannot name them until they
  exist.

## Phase A — the design source

- **A1.** `instructions/robot-guide/make_plans.py`: `WEDGES`, `WEDGE_C`, `RING_OUT`, `STUB_PROUD`
  and `BORE_D` take their new values or their new rules. Every number downstream of them is already
  derived and moves on its own.
- **A2.** `tools/hinge_spring.py`: `hold` returns how many wedges carry, not how many projections
  carry. The model lumps wedges by where they land on the beam's axis, and two of draft9p1p5's
  projections each hold two wedges, so the count it reported was 2 where the joint carries on 4.
  The torque was never affected. draft9p1p5's register and the hinge review both carry the low
  count and are corrected by name in A4 and B3.
- **A3.** `.docs/robot-build-plan.md`: the Variables table takes the new values under the names it
  already has. No row is added or removed; this draft changes what the rows say, not which rows
  exist.
- **A4.** Regenerate the plan sheets and the brief sheets from `make_plans.py`.

## Phase B — the sketches and the brief

- **B1.** `detail_hinge` redrawn to twenty-four wedges: the ring in plan, the section through a
  detent and through the ride, the axle at both positions.
- **B2.** The hinge build brief to the settled numbers, including the pinch budget, which moved.
- **B3.** The hinge review reconciled, since it argues from a `30°` step and quotes the low carrying
  count.

## Phase C — copy the document

- **C1.** Copy `stickbot-draft9p1p5` to `stickbot-draft9p1p6` from its named version. Record the
  document id and every element id.
- **C2.** Check that no feature still references `stickbot-draft9p1p5`. A copy creates that defect
  and nothing else reports it.

## Phase D — the CAD

- **D1.** `robot sizes`: the changed rows.
- **D2.** `hinge`: the ring repatterned to twenty-four on both faces, the outline redrawn to the new
  width and outer radius, the axle lengthened and its bore tightened.
- **D3.** `u limb` and `l limb`: re-read after the hinge changes, since both derive it.
- **D4.** The two coupons, re-read for the same reason.

## Phase F — prove it

- **F1.** `check.py` comes forward from draft9p1p5 with the hinge's rows rewritten.
- **F2.** The document-wide face census holds with `#torsoH` and `#limbD` driven and put back. This
  is the gate that caught draft9p1p5's missing coincident, and a pixel read of sketch color is not
  a substitute for it.
- **F3.** No reference leaves the document.
- **F4.** Look at it: twenty-four wedges a face, the ring reaching the flat, the ridge coming to a
  point, the axle `3.00 mm` proud.
- **F5.** Publish a named version.

## Phase R — the register

`register.md`, carrying where the work is, what was built, what is open, and the acceptance numbers,
and naming the commit and tag the way draft9p1p5's does.

## What this draft does not do

- It writes no student page and takes no frame.
- It does not repair draft9p3 or draft9p1.
- It does not touch `stickbot-draft9p1p5`, which stays as the printed reference this one is diffed
  against.
- It does not chase task #177, the blade's lost wedge above `#limbD 34 mm`, which is outside the
  design range.

## What we do not know yet

- **Whether the printer resolves a pointed ridge**, and what it leaves when it does not. This is the
  question the draft exists to ask, and only a print answers it.
- **Whether `0.1 mm` of total diameter margin lets the axle into its bore at all.** `0.05 mm` a side
  is inside one print offset, so the fit may be an interference rather than a clearance. Nothing in
  `tools/hinge_spring.py` models a radial press fit; it treats the axle as in the bore or out of it.
- **Whether backlash at 15% of a step reads as slop.** It was 8% of a `30°` step and the printed
  joint is good; the absolute figure improves slightly and the fraction does not.
- **Whether the pinch is what the model says.** The one calibration that would settle it is a scale
  reading Mike has not taken yet.
