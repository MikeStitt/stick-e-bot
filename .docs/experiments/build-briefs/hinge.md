# Build brief — the hinge, the fork and the blade

**Revised on 2026-09-08 to a 15° step.** draft9p1p5 was printed and is good in the hand, and this
draft asks the same joint for twice as many detents. Twenty-four wedges, a longer axle, a tighter
bore, closer faces, and a ring that runs right out to the limb's flat. What it costs is a pointed
crest and a 75 N pinch. The run is
[`../runs/2026-09-08-draft9p1p6/plan.md`](../runs/2026-09-08-draft9p1p6/plan.md).

**Rewritten on 2026-09-04 around the wedge detent.** Everything before this rewrite described a
detent made of 45° cones dropping into holes bored through the fork prong. That joint was built,
printed and measured, and it held 210 N·mm where it was drawn for 454. The printer had put supports
in the valley holes and they could not be picked out; 0.235 mm of residue in a valley, one extrusion
width, accounts for the whole loss. There are no holes in the joint now except the bore.

The design source is [`make_plans.py`](../../../src/stickbot/make_plans.py), the numbers
a person reads are in [`../../robot-build-plan.md`](../../robot-build-plan.md), and the record of
how the joint got here is [`../../reviews/hinge/`](../../reviews/hinge/), which is frozen on the
joint it reviewed and says at its end what changed.

**Before you write the report: publish a named version, and open the report with a "Where the work
is" section** — document name, document id, element id, version name and id, the version link, and
the workspace link labeled as live. See
[`../../../.claude/skills/onshape/SKILL.md`](../../../.claude/skills/onshape/SKILL.md).

**This is a specification, not a lesson.** Build it in Onshape, find the click path that works, and
write down what actually happened.

Build **both halves in one Part Studio**, because the point is whether the fork prongs straddle the
blade blank and the axle lands in the bores.

## The idea being tested

- - The **fork** is two fork prongs, on the limb nearer the torso. - The **blade** is a flat blade
  blank on the limb further out, sitting between the fork prongs. - The blade carries an **axle**
  standing proud of both its faces; each fork prong is **bored through** on the same line. Pinch the
  two leaves together, slide the blade blank in, let go, and the axle springs into the bores. - Both
  mating faces carry a **ring of wedges**. A detent is one member's wedge sitting between two of the
  other's, so the joint clicks between positions and holds a pose.

The two parts are named `fork` and `blade`. The blade blank, the fork prongs and the leaves are
named parts of them, not parts of their own.

## What changed from the joint before this one, and why

- - **The detent is a protrusion on both members, not a protrusion into a hole.** A hole through an
  fork prong prints with support in it. A protrusion has nothing to clean out. This is the whole
  reason for the change and every other difference follows from it. - **The two faces no longer
  touch.** They used to seat on each other across a 0.15 fit. They now stand `GAP` 0.90 apart, which
  is one wedge plus 0.15 of air over its tip, and nothing bears except wedge on wedge. - **Assembly
  is a pinch, not a press.** Squeezing the two leaves toward each other until the axle clears the
  fork prong's face takes **75.2 N**. Pushing the blade blank down the slot the old way would take
  **182.7 N** on this geometry and rises the whole way in. The joint is sized on the pinch. - **The
  leaves taper**, 4.20 at the root to 1.50 at the tip. The taper is nearly free: taking the tip from
  3.00 to 1.50 costs 7% of the detent torque, and giving the root 3.00 to 4.20 buys 35%. - **The
  joint has backlash, and it did not before.** 2.29° at a detent, which is 15% of a step. Backlash
  is set by `T_PRINT` and a radius, not by the pitch, so halving the step barely moved it and it
  doubled as a share of one step.

## The drawings

| Drawing | What it settles |
| ------- | --------------- |
| the hinge detail on [`plan-parts.svg`](../../../instructions/robot-guide/source/images/plan-parts.svg) | the section along the limb, and one fork prong's face square on with both rings on it |
| [`images/brief-roots.svg`](images/brief-roots.svg) | where each limb's rod stops, which is the thing earlier builds got wrong |
| [`images/brief-fork.svg`](images/brief-fork.svg) | why the fork is drawn as full slices of the limb and not as a rectangle |
| [`images/brief-detent.svg`](images/brief-detent.svg) | the wedge ring and one wedge square on, to scale |

| Frame | What it shows |
| ----- | ------------- |
| [`images/cad-hinge-iso.png`](images/cad-hinge-iso.png) | the fork and the blade, engaged |
| [`images/cad-hinge-right.png`](images/cad-hinge-right.png) | the two meshing: the blade's leaves inside the fork's prongs |
| [`images/cad-hinge-section.png`](images/cad-hinge-section.png) | the blade cut on the Right plane, through both stub axles |

**These are the reference CAD, not the specification.** [`README.md`](README.md) § *Where the
`cad-*.png` frames came from* names the document, workspace and version each was taken at, and
what is wrong with the part it shows.

All four sheets are generated by `make_brief_sheets.py` from `make_plans.py`, so they carry the
settled joint. Re-run `ninja brief-sheets` if you doubt one; `brief-fork.svg` and
`brief-detent.svg` were a joint generation behind until 2026-09-18, when nothing referenced them.

## The one idea that shapes everything: slices, not a rectangle

**Every layer of the fork is a full slice of the Ø24 limb.** Do not draw a rectangular paddle inside
the circle and cut it off at some width; let each face run out to the Ø24 arc, so the ends follow
the limb's own surface.

This is not styling. A rectangle inside a circle has corners, and the corners bind before the faces
do. Slices have no corners, so there is no fit constraint left to satisfy.

## The numbers

Every row is `make_plans.py`. Import it rather than copying it: `BLADE`, `LEAF_ROOT`, `LEAF_TIP`,
`SLIT`, `T_PRINT`, `WEDGES`, `WEDGE_H`, `WEDGE_C`, `WEDGE_W`, `BACKLASH`, `GAP`, `SEAT`, `EAR`,
`CLIMB`, `STUB`, `STUB_PROUD`, `BORE_D`, `NOSE`, `FLAT`, `LIMB_FLAT`, `RING_IN`, `RING_OUT`,
`RING_CON`, `BLADE_OUT`, `SLOT_DEEP`, `TAB_FREE`, `EAR_FREE`, `ROD_ARM`, `ROD_FORK`, `ROD_BLADE`.

| What | mm | Source |
| ---- | -- | ------ |
| the limb | 24 | plan — `LIMB`, and every face of both parts is a slice of this rod |
| the blade blank | 10.00 | plan — `BLADE`, across |
| one leaf, at its root | 4.20 | plan — `LEAF_ROOT` |
| one leaf, at the tip | 1.50 | plan — `LEAF_TIP` |
| the slit | 1.60 | derived — `SLIT` = `BLADE - 2 * LEAF_ROOT`, opening to 7.00 at the tip |
| a wedge, proud | 0.75 | plan — `WEDGE_H`, off its own face |
| air over a wedge tip | 0.15 | plan — `WEDGE_C`, and this one is inside `2 * T_PRINT`, on purpose |
| the printer's error | 0.10 | plan — `T_PRINT`, per surface, so clearances are checked against twice it |
| the gap | 0.90 | derived — `GAP` = `WEDGE_H + WEDGE_C`, face to face at a detent |
| the slot | 11.80 | derived — `SEAT` = `BLADE + 2 * GAP`, cut through the limb, the whole depth |
| the fork prong | 6.10 | derived — `EAR` = `(LIMB - SEAT) / 2`, whatever the slot leaves |
| the flat | 10.4494 | derived — `FLAT` = `sqrt(NOSE² - (SEAT / 2)²)`, off the limb's axis |
| the limb, top to bottom | 20.8988 | derived — `LIMB_FLAT` = `2 * FLAT` |
| the round end | 12 | derived — `NOSE` = `LIMB / 2`, on both parts, every end, about the pin |
| the blade blank stands out | 32 | plan — `BLADE_OUT` |
| the slot is cut | 33 | derived — `SLOT_DEEP` = `BLADE_OUT + 1`, from the fork's tip |
| the blade blank's root | 20 | derived — `TAB_FREE` = `BLADE_OUT - NOSE`, from the pin |
| the fork prong's root | 21 | derived — `EAR_FREE` = `SLOT_DEEP - NOSE`, from the pin |
| the forearm and shin rod | 18 | derived — `ROD_BLADE` = `LIMB_CENTER - STAND - TAB_FREE` |
| the thigh's rod | 17 | derived — `ROD_FORK` = `LIMB_CENTER - COLLAR_L - EAR_FREE` |
| the upper arm's rod | 32 | derived — `ROD_ARM` = `LIMB_CENTER + SHOULDER_INSET - EAR_FREE` |
| the axle | Ø4.0 | plan — `STUB`, one extrude 16.0 long across the blade blank, ±8.0 |
| the axle stands proud | 3.00 | derived — `STUB_PROUD` = `2 * WEDGE_H + 1.50`, off each blade blank face |
| the bore | Ø4.1 | derived — `BORE_D` = `STUB + 0.1`, through each fork prong |
| engaged at a detent | 2.10 | derived — `STUB_PROUD - GAP` |
| engaged riding a crest | 1.50 | derived — `STUB_PROUD - 2 * WEDGE_H` |
| the climb | 0.60 | derived — `CLIMB` = `2 * WEDGE_H - GAP` |
| wedges, per face | 24 | plan — `WEDGES`, 15° apart, which divides 90 exactly |
| the ring, outer | r 10.4494 | derived — `RING_OUT` = `FLAT`, so a wedge runs out to the cut |
| the ring, inner | r 6.00 | plan — `RING_IN` |
| where a flank bears | r 9.6994 | derived — `RING_CON` = `RING_OUT - WEDGE_H` |
| where the fit is set | r 9.9994 | derived — `WEDGE_BIND` = `RING_OUT - GAP / 2` |
| what the draft leans | 5.1587° | derived — `WEDGE_INSET` = `2 * asin(GAP / 2 / WEDGE_BIND)` |
| room for a flank | 1.1460° | derived — `WEDGE_EPS` = `2 * T_PRINT / WEDGE_BIND` |
| one wedge, across | 11.5127° | derived — `WEDGE_W` = `180° / WEDGES + WEDGE_INSET - WEDGE_EPS` |
| backlash | 2.2920° | derived — `BACKLASH` = `2 * WEDGE_EPS` |

Two of those are printer clearances rather than shape and do not scale with the robot: `T_PRINT`
0.10, which sets `WEDGE_W`, and the 0.05 a side in `BORE_D`. `WEDGE_C` is now 0.15, inside
`2 * T_PRINT` rather than outside it, so a crest that over-prints can land on the face opposite
instead of clearing it. What that costs is 0.05 of flank engagement, not a joint that will not
seat, and the printed part is what says whether it happens at all.

## How to cut a wedge, and how wide it has to be

A wedge is **one sketched annular sector, extruded `WEDGE_H` with a 45° draft inward**. Nothing
else. The 45° is what lets both flanks print without support, and drafting rather than lofting is
what makes the shape come out right on its own: a 45° draft is a planar inward offset of the sector
by 0.75, so the crest is the sector inset 0.75 all round, on all four sides.

### How wide, and why it is wider than half a step

**`WEDGE_W` is 11.5127°, and a half step is 7.5°.** A wedge is wider than the gap the mating ring
leaves at its own base plane. That looks wrong and is not, and getting it wrong is the one mistake
that quietly ruins this joint.

Both members are drafted, and each flank leans inward by its own height above its own face. The two
members lean **away from each other**, so by the time you are half way up the `GAP` each has leaned
0.45. Measure the fit anywhere else and the wedge comes out too narrow.

Three numbers say it:

- **`WEDGE_BIND` = `RING_OUT - GAP / 2` = r 9.9994.** Half way up the gap is also where the two
  radial draft ends have taken the least off the outer radius, so one height and one radius settle
  the whole fit.
- **`WEDGE_INSET` = `2 * asin(GAP / 2 / WEDGE_BIND)` = 5.1587°**, the two leans together.
- **`WEDGE_EPS` = `2 * T_PRINT / WEDGE_BIND` = 1.1460°**, the room a flank needs there.

`WEDGE_W` = 7.5 + 5.1587 − 1.1460 = **11.5127°**, and `BACKLASH` = 2 × 1.1460 = **2.2920°**.

A wedge fitted at its own base plane instead comes out `WEDGE_INSET` too narrow and leaves **12.61°
of play** at a detent. That is most of a 15° step. The joint would turn freely through nearly all of
its travel and barely detent at all.

### What the crest looks like

The 0.75 inset is a length, and the arc it eats is an angle, so the crest narrows going inward. At
24 wedges it runs out before it reaches the inner radius, and that is the change this draft makes:

| at radius | the crest is |
| --------- | ------------ |
| r 9.6994, its outer edge | 0.447 wide |
| r 9.00 | 0.307 |
| r 8.00 | 0.105 |
| r 7.478 | a point |
| r 7.00 | a ridge, 0.702 tall |
| r 6.00, the ring's inner edge | a ridge, 0.602 tall |

**Inboard of r 7.478 the wedge is a ridge, not a table.** The two flanks meet before they reach
`WEDGE_H`, so from there in the top is a knife edge whose height falls away to 0.602 at `RING_IN`.
That is drawn on purpose. Half the step halves the arc a wedge gets, and the choice was a pointed
crest or a shorter ring; the ring was kept, because the ring's outer end is where the lever is.

The printer will round that ridge. Print it and look at what came out; do not draw something else to
avoid finding out.

**Do not open the draft angle** to change the crest. 45° is what makes the flanks printable, and it
is also what sets `WEDGE_INSET`; change it and the width has to be re-derived.

## Which side of the joint each feature is on

**The axle is on the blade and the bore goes through the fork.** A hole straight through an fork
prong prints without a ceiling over it, where a blind pocket needs one, and the spring arithmetic
does not care which side the axle is on.

The old rule was that *every* protrusion is on the blade and every hole in the fork, so that nothing
on the fork could foul the axle. That rule is gone, because both members now carry wedges. The thing
it protected is still checked, and by a wide margin: the bore's radius is 2.05 and the ring starts
at 6.00, so the fork's wedges clear the axle by **3.95**.

Put the **hinge axis on the origin**, running fore-and-aft. Both limbs run vertically away from it,
the fork's limb upward and the blade's downward.

## The axle is sized against the wedge, not against the assembly

`STUB_PROUD` has to beat `2 * WEDGE_H`, which is 1.50. At 3.00 it does, by 1.50. That 1.50 is what
is still in the bore at the worst moment, when the joint is riding over a crest and the pair is open
as far as it ever gets, and at a detent 2.10 is engaged.

This constraint is new. The old joint never had to meet it, because its `GAP` was 0.15, smaller than
one tooth, so the pair opening to pass a tooth never threatened the pin. Here the faces stand nearly
a millimeter apart and the axle has to reach across all of it and still hold.

**Lengthening the axle is what the pinch costs.** How far the leaves have to be squeezed to assemble
is `STUB_PROUD - GAP`, and everything in the pinch is linear in it, so the 3.00 axle and the 75.2 N
pinch are one decision and not two. Do not shorten it to make the joint easier to assemble; the
assembly force is set by the leaves, and the leaves are what to change if it is too stiff.

## The leaves are what make it assemblable, and they are pinched, not pressed

The fork prong and the leaf are springs in **series**: the same force through both, sharing the
movement in inverse proportion to stiffness. But assembly does not load them in series at all. A
hand squeezes the two leaves toward each other, the fork prong takes no part, and the blade blank
slides in with the axle already clear. That is **75.2 N** with a finger 30 mm out from the blade
blank's root, against 182.7 N to push the same joint together the old way.

**The pinch and the detent are not independent, and that is what makes the joint hard to size.**
Both are the same leaf bending over the same span, root to pin. A leaf thick enough to hold a detent
is a leaf too stiff to pinch, and thickening it raises both together. Only `WEDGE_H` separates them:
it sets how far the pair must open to turn without touching how far it must close to assemble. That
is why the wedge is 0.75 proud and not the 0.65 first asked for; at 0.65 the joint can only reach
431 N·mm under a 40 N pinch.

**The pinch budget is 100 N, raised from 40 N**, and the joint sits at 75.2 N inside it. Nothing was
measured to justify the raise; the printed draft9p1p5 joint pinches far more easily than the model
says it should, and 100 N is the number to design against until a kitchen scale says otherwise.

**How much slit is left at full pinch is the one number this model gets wrong.** It answers −4.32,
meaning the leaves would have to pass through each other. It is wrong: on draft9p1p5 it answered
1.07 where Mike measured 4.00 with the axle riding a crest, so it overstates how far the tips close
by 1.98 times. Divide this draft's closure by that and the tips stand about **1.27 apart** at full
pinch. That is a prediction and not a measurement, and it is the first thing to put a caliper on
when the part comes off the printer. Which way the *force* is wrong is not known; only the
deflection has been measured.

## Each limb's rod must stop at its own root

This is the one thing every earlier build got wrong, and it is worth its own section.

Each limb unions a rod onto its half of the joint. If that rod runs on to the pin it fills the slot
back in, and both members end up rooted 12 from the pin instead of 20 and 21. It is then a different
joint that happens to look the same.

Each rod is `LIMB_CENTER`, less how far its far joint's center stands off the rod's own end face,
less its hinge member's root. The robot has three combinations, so it has three rod lengths: **32 on
the upper arm** (`ROD_ARM`, whose shoulder socket is in a side face), **17 on the thigh**
(`ROD_FORK`), and **18 on the forearm and the shin** (`ROD_BLADE`). Check every one of them with a
bounding box, every time.

## Build in two stages, and stop between them

### Stage 1 — the mechanical joint, no wedges

- - A limb rod Ø24 for each half, one above the axis and one below. The blade's rod stops **20 from
  the axis**; the fork's stops **21 behind it**. - The **blade**: 10.00 thick, its width the full
  chord, with a round end of radius 12 centered on the hinge axis, standing 32 out of its own limb.
  - The **slit**: up the middle of the blade blank the whole way from the round end to the blade
  blank's root, **1.60 at the root opening to 7.00 at the tip**, leaving two tapered leaves. - The
  **fork**: two fork prongs either side of a 11.80 slot, each fork prong a full slice of the limb,
  same r12 round end. The fork prong's outer surface **is** the Ø24 cylinder; there is no outer
  plane on it. - The **flats**: top and bottom of both limbs cut to `FLAT` 10.4494 off the axis,
  20.8988 across. - The **axle** Ø4.0 across the blade, coaxial with the hinge axis, so it stands
  3.00 proud of each blade blank face. The slit cuts it rather than it bridging the slit. - The
  **bores** Ø4.1 through each fork prong, coaxial. That is 0.05 a side, inside one `T_PRINT`, so
  whether it comes out a clearance or an interference is a question about the printer.

**Check stage 1 before going on:**

- - **Parts (2)**, and they do not intersect. Ear inner face to blade blank face: **0.90**,
  everywhere. - The axle sits **2.10** inside the bore. - The bore is a bore: from the fork prong's
  inner face at 5.90 out to its outer surface at 12.00. - **The blade's own limb clears the fork's
  prong tips when the joint folds.** The tips sweep 12 from the axis and the blade's rod ends at 20,
  so there is 8 to spare. - Bounding-box every rod. 32, 17 and 18, and not one of them 12 longer.

### Stage 2 — the two rings of wedges

- - **24 wedges on each face of the blade blank**, and **24 on each fork prong's inner face**, all
  four rings on the same radii and the same 15° pitch. - Each is an annular sector `RING_IN` 6.00 to
  `RING_OUT` 10.4494, `WEDGE_W` 11.5127° across, extruded `WEDGE_H` 0.75 with a 45° inward draft. -
  The blade's rings and the fork's rings are **phased a half step apart**, 7.5°, so the parts as
  drawn sit at a detent rather than crest on crest.

**Check stage 2:**

- Face to face is 0.90 and crest to crest is 1.50, so at a detent a crest clears the opposite face
  by **0.15**, which is `WEDGE_C` and is 0.05 inside `2 * T_PRINT`.
- A wedge is **wider than half a step**, 11.5127° against 7.5°, and that is right. Check it: at r
  9.9994, half way up the gap, the clearance to the facing flank comes to **0.200**, which is
  `2 * T_PRINT`. A wedge fitted at its base plane instead leaves 12.61° of play and the joint
  barely detents.
- There is **2.29° of play** at a detent before a flank touches. That is the price of a joint that
  goes together at all.
- The crest is **0.447 wide** at r 9.6994 and closes to a point at r 7.478, so the inner two thirds
  of the ring is a ridge rather than a flat. Count the faces: a wedge that came out with a
  full-width flat top all the way in did not get its draft.
- **96 wedges in the Part Studio.** Two rings of 24 on the blade, two on the fork.
- The ring runs right out to the edge of the face: `RING_OUT` and `FLAT` are the same 10.4494, so a
  wedge's outer end meets the limb's top and bottom cut.

## What it should measure when it is right

| | |
| --- | --- |
| pinch to assemble | **75.2 N**, with a finger 30 mm out from the blade blank's root, against a 100 N budget |
| worst stress pinching | leaf **38.3 MPa**, against PETG's 50, and this is the governing case |
| detent hold | **641 N·mm** frictionless, **1332** at µ 0.35, and only 4 of the 24 carry |
| worst stress holding | fork prong 12.9, leaf 8.4 MPa |
| twist-off | **1889 N·mm** at 13.3°, and it is a floor |
| at the hand, 150 mm out | 0.44 kgf, which is 25× the 26 N·mm the arm needs to not droop |
| the step | **15°** |
| backlash | **2.29°** |
| slit left at full pinch | about **1.27**, predicted, not modeled — see above |

Only four of the twenty-four carry, in either load case, because both members are beams: lifting the
wedge on the short lever lifts everything outboard of it by more than that wedge's own climb. Adding
the wedges up as independent springs overstates it several times over. **Doubling the ring bought
no torque at all**: hold the rest of the joint still and 12 wedges and 24 give the same 641 N·mm.
The 31% this draft gains over draft9p1p5 comes from two other changes; closing `GAP` 0.10, which
raises `CLIMB` to 0.60 and makes the pair open further to turn, is 24% of it, and the ring moving
out to `FLAT` is the other 5%. Twenty-four wedges buy the 15° step and nothing else. Use
`src/stickbot/hinge_spring.py`; do not re-derive it with a formula. Run that file on its own and it
reproduces the old joint's 454 N·mm and 7.16 kgf, so a difference you see is the design's and not
the model's.

**The twist-off number is a floor twice over.** The leaf is assumed to carry a corner load through
to the pin without dishing, and the lever is the contact radius when the wedge tips reach further
out.
Taken at face value the joint wrings apart at 1889 N·mm and turns at 1332, so it now holds together
harder than it turns, by 1.42 times. On draft9p1p5 those two were the wrong way round. Both are
still worth measuring on a printed part.

## What would make this design fail

- - **The rod buries the root.** Covered above. It is the failure with the biggest number attached.
  - **The draft is left off, or opened past 45°.** A wedge with a square top has no self-relieving
  inner end, its tip bears and wears, and its flanks need support to print. - **The two rings are
  phased together instead of a half step apart.** The parts then sit crest on crest, every
  measurement is 0.60 out, and it looks like a fit problem. - **`WEDGE_C` cut further.** It is
  already 0.15, inside `2 * T_PRINT`, so a crest that over-prints can land on the face opposite and
  the faces get held apart by the wrong thing. That is accepted here and it is what the print is
  for; taking it lower is not. - **The axle shortened below `2 * WEDGE_H`.** The joint lets go of
  the pin every time it crosses a detent and the blade walks out of the fork. - **Merge scope
  defaulted.** See the tool lessons below. It is the most common way this Part Studio comes out
  looking right and measuring wrong. - **The weak axis.** The blade blank's sideways strength is
  6144 N·mm against the fork's 6493. That is a child picking the robot up by its forearm, and it is
  the weakest thing in the joint. It is accepted, and the two members are within 6% of each other
  rather than a factor of two apart.

## What earlier builds proved, so you do not retest it

- - Boolean and Mirror both need **Reapply features** ticked, or they fail with *"Could not create
  all instances as entered."* - **Merge scope must be set by hand on almost every Add and Remove.**
  Onshape defaults to *Merge with all*, which silently welds the two parts into one. **An empty
  scope is worse: it is accepted and does nothing at all**, with a preview that looks right. Run 3
  lost both the fork trim and the fork's slot that way and only mass properties caught it. Assert
  the field's text contains the part name before accepting. - **A feature's stored direction flag is
  the only way to tell a no-op click from a correct default.** Every feature built on an offset
  plane here needs the flip on, and the extrude dialog carries the flip over from the previous
  extrude, so it is not reliably off when the dialog opens and "click it once" is not a rule you can
  apply blind. - **The axle must be added before the fork prong is bored** — the parts genuinely
  interfere between those two features, so feature order is load-bearing. - With *Starting offset*
  enabled, the offset direction has **its own flip control**, separate from the main direction's.
  Getting this wrong put a rod straight through the fork and looked fine in preview. **Check
  bounding boxes after any offset extrude.** - **Midpoint would not apply** between a rectangle edge
  and a circle; **Tangent** does the same job and reads as better design intent.

## Recommended steps

**This is the feature order to build, and the name each feature carries.** It is the order a
proven model was built in, with the renames that have been settled since applied. Variables are
not in the table: each one is added immediately above the first feature that reads it, which is
what [`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *Phase A*
works out by walking the expressions. Do not open a tab with a block of numbers.

The verification after each feature and after the tab is one loop for every part, and it lives in
[`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *The verification
loop*. It is not repeated here.

| Step | Feature | Name |
| ---: | ------- | ---- |
| 1 | `newSketch` | `blade profile` |
| 2 | `extrude` | `blade blank` |
| 3 | `newSketch` | `stub axle outline` |
| 4 | `extrude` | `stub axle` |
| 5 | `newSketch` | `blade wedge outline` |
| 6 | `extrude` | `blade wedge` |
| 7 | `mateConnector` | `axis for circular patterns` |
| 8 | `circularPattern` | `blade wedges` |
| 9 | `mirror` | `mirror blade` |
| 10 | `newSketch` | `blade rod outline` |
| 11 | `extrude` | `blade arm` |
| 12 | `newSketch` | `relief slit outline` |
| 13 | `extrude` | `relief slit` |
| 14 | `newSketch` | `fork outline` |
| 15 | `extrude` | `fork blank` |
| 16 | `newSketch` | `fork blade top cut outline` |
| 17 | `extrude` | `trim fork to arm` |
| 18 | `newSketch` | `pocket axle sketch` |
| 19 | `extrude` | `pocket axle on fork` |
| 20 | `newSketch` | `fork prong wedge outline` |
| 21 | `extrude` | `fork prong wedge` |
| 22 | `circularPattern` | `fork prong wedges` |
| 23 | `mirror` | `two forks` |
| 24 | `newSketch` | `fork arm outline` |
| 25 | `extrude` | `fork arm` |
| 26 | `booleanBodies` | `combine fork parts` |
| 27 | `mateConnector` | `fork to robot` |
| 28 | `mateConnector` | `blade to robot` |

**The last five features are the ones draft9p4-check never reached.** Everything above them exists
in that document, built to the current rules; `fork arm outline` onward exists only in
draft9p1p6, whose tree is older. Build the whole list fresh.

**`relief slit` is the last feature on the blade** and the fork does not start until `fork
outline`. That is not a preference: cutting the slit earlier lets the stub axle bridge the two
leaves at the pin, which is the opposite of the two-leaf spring the joint depends on.
