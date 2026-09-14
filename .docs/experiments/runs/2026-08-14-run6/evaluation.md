# Run 6 — evaluating the parts and the robot

The three axes from [`../../design-into-cad.md`](../../design-into-cad.md), on the six rebuilt
parts and then on the assembled figure. Phase 7 of [`plan.md`](plan.md).

## How these were measured

Parts off their named versions through `bodydetails`, `boundingboxes` and `massproperties` — the
numbers are in [`measured.json`](measured.json). The robot off the assembly version
`robot-run6-2026-08-15` (`cab79923d9e94d9f908d359f`) through the same three plus the root
assembly's own `occurrences`, whose transforms put each part's mate connectors into world
coordinates. `featurescript` answered this run where it was throttled out of run 5's, and every
mate connector location in [`build-notes.md`](build-notes.md) came from `evMateConnector`.

Stations are compared against [`target.json`](target.json), which
`instructions/robot-guide/make_plans.py` writes — not against a reading of a drawing.

## Matches the sketches

Every joint centre below is the world position of a mate connector, read off the assembly.

| Station | `target.json` | Assembly |
| ------- | ------------- | -------- |
| hip | (±12, 0, −29) | (±12.0000, 0.0000, −29.0000) |
| knee | −53 | (±12.0000, 0.0000, −53.0000) |
| ankle | −77 | (±12.0000, 0.0000, −77.0000) |
| ground, `SOLE_Z` | −89 | −89.0000 |
| neck | (0, 0, +29) | (0.0000, 0.0000, +29.0000) |
| shoulder ball | (±24.7754, −3.9118, +9.6177) | (±24.7754, −3.9118, +9.6177) |
| top of head, `HEAD_T` | +69.15 | +69.1500 |
| whole figure, `HEIGHT` | 158.15 | 69.1500 − (−89.0000) = **158.1500** |

**Every station in the standing frame matches**, including the two the head collar moved this run:
`HEAD_T` 69.15 and `HEIGHT` 158.15, which run 5's head missed by 5.5.

**The arms hang, and the drawing splays them.** `make_plans.py` draws the arm at `ARM_ANGLE`
33.1283°, putting the elbow at (37.8918, −10.4810) and the wrist at (32.9545, −33.9677). The
assembly's arms hang straight down from the shoulder balls: elbow at (±24.7754, −3.9118,
−14.3823), wrist at (±24.7754, −3.9118, −38.3823), gripper bottom at −50.3823. Both shoulders are
ball mates with no limits, so the solver leaves the arm wherever it was dropped; the segment
lengths agree — shoulder to elbow and elbow to wrist are 24.0000 in the assembly and `ARM_SEG` is
24 — and only the angle differs. The figure has no drawn pose to hold it at 33°, and nothing in
the assembly asks it to.

The centroid of the whole robot lands at (0.0000, −0.4665, −10.9004): **exactly zero in x**, which
says the pose is symmetric left-right as well as the geometry. Total volume 75665.8276 mm³, which
is the sum of the fourteen instances' own volumes to the fourth decimal.

## Matches the briefs

Each brief's *Acceptance checks*, performed on the rebuilt parts, are recorded per part in
[`build-notes.md`](build-notes.md), and every delta against run 5 is classified in
[`audit.md`](audit.md). What this section adds is the checks that need more than one part, or the
assembly, to answer.

### The same socket, built four times

The head, the hand, the foot and the clevis limb each carry the standard socket, built
independently from [`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md)
in four different studios:

| part | cavity faces | collar faces | cavity area |
| ---- | ------------ | ------------ | ----------- |
| head | 4 | 4 | 71.5694 mm² |
| hand | 4 | 4 | 71.5694 mm² |
| foot | 4 | 4 | 71.5694 mm² |
| limb-socket-clevis | 4 | 4 | 71.5694 mm² |

**The four areas agree to the fourth decimal.** Four independent builds of the same brief landing
on the same number is the strongest statement available about the brief being followable, and the
face *count* is what catches a cup left joined under its slits — run 5's hand and clevis both read
one cavity face where these read four.

### The detent band, measured rather than derived

24 valley cylinders r 0.5000 on each of the blade's two faces, every centre 4.8000 from the hinge
axis, neighbouring centres **1.2531** apart. 24 tooth spheres r 0.4000 on each ear face, on the
same circle at the same spacing.

| what | measured | comes to |
| ---- | -------- | -------- |
| land between neighbouring valleys | 1.2531 − 1.0 | **0.2531** |
| gap between neighbouring teeth | 1.2531 − 0.8 | **0.4531** |

[`../../build-briefs/hinge.md`](../../build-briefs/hinge.md) names the land as the thinnest wall in
the part and gives it as **0.053**. That number needs `VALLEY_D` 1.2; today's `VALLEY_D` is 1.0, so
the land as built is 0.2531. The brief's figure is stale rather than wrong-in-kind — it is the same
subtraction with the older valley — and the brief itself says every tooth-band number has to be
re-derived after the rim break. **Recorded, not repaired**: changing a brief's number is a decision.

## Works as a printable robot

### Printable

**The walls that are readable off the model.**

| wall | where | measured |
| ---- | ----- | -------- |
| socket collar | head, hand, foot, clevis limb | 4.7000 − 3.2000 = **1.5000** |
| head shell | over the neck socket | 4.4000 − 3.2000 = **1.2000** |
| blade tab | blade limb | 2.5000 − 0.4000 = **2.1000** either side of the slit |
| land between detent valleys | blade limb | **0.2531** |
| gap between detent teeth | clevis limb | **0.4531** |
| clevis ear, at the chord | clevis limb | tapers to **zero** — the brief's own number, not measured here |

**One number is below a 0.4 mm nozzle: the 0.2531 land between neighbouring valleys.** It is a land
between two dimples on a face, not a wall between two voids — there is full blade behind it — so it
is a resolution question rather than a strength one, and it is the same question
[`../../build-briefs/hinge.md`](../../build-briefs/hinge.md) already asks: whether the band prints
as discrete bumps or as a smooth ring. It cannot be answered in CAD. The tooth gap at 0.4531 clears
one nozzle width, just.

**The clevis ear's taper to zero is the design**, stated in
[`../../build-briefs/limbs.md`](../../build-briefs/limbs.md): the ear is a slice of the Ø12
cylinder, so its inner face at \|y\| = 2.8 meets the cylinder and thins out, falling below one
nozzle width over the last 0.231 mm. That is the brief's derivation and it was not re-measured
here; what the model does confirm is the geometry it rests on — the ear's inner faces at y ±2.8000
and nothing on the part outside r 6.0000. The brief asks for the taper and the collar to be
reported separately, and they are, above.

**Run 5's failing wall is gone.** Run 5 measured a 0.400 annular slot in the head, between a dome
at r 4.400 and a boss inner wall at r 4.800. Run 6's head carries the standard collar instead —
outer r 4.7000, bore r 3.5000, four tabs — and that pair of surfaces no longer exists in the part.

**Print orientation, overhangs and bridges: not attempted.** No part names an orientation, and
nothing here identifies an overhang. This is the same gap run 5 left, and naming an orientation is
a decision about how the model will be made, so it goes to [`register.md`](register.md) rather than
being settled here.

### Assemblable

**Every ball can enter its socket, because every collar is now slit.** All four socketed parts read
four cavity faces, four collar cylinder faces and four rim faces — the signature of a collar cut
into tabs — and the head is among them. Run 5's head was the one continuous rim in the robot, and
[`audit.md`](audit.md) classifies the change as deliberate: the head's own neck recess was replaced
with the standard collar.

**The clearances are the brief's own, measured on the parts:**

| fit | measured |
| --- | -------- |
| ball in cavity | ball r 3.0000 in cavity r 3.2000 — **0.200** radial |
| blade in slot | blade at y ±2.5000 in slot at y ±2.8000 — **0.300** a side |
| relief slit | 0.800 wide, running the collar's whole proud length on every socket |

**A mate closing is not an assembly test.** Onshape solves rigid bodies, so the thirteen mates
close whether or not a real tab would flex. What is checkable in CAD is that the flexure exists —
the slits are there, they run the full collar, and the tab count is four everywhere — and that is
what was checked.

**The foot's collar still stands 7.3500 proud against 5.5 everywhere else.** [`audit.md`](audit.md)
carries this as unresolved: `foot.md` and `design-note.md` disagree about whether the foot gets a
socket pad, so the foot's tabs are 1.85 longer and flex differently from every other socket. Not a
measurement problem — a decision, and it goes to the register.

### Functional

**One clearance is answered, and it is the one the torso brief asks for.** With the arms hanging,
the upper limb's axis is at x = ±24.7754 and the limb is Ø12, so its inner surface reaches
\|x\| = 18.7754 against the torso's side face at 18.0000: **+0.7754 clearance at the zero pose**,
against the brief's expected +0.776. The legs are flush by design — `LEG_X` 12 with a Ø12 limb puts
the leg's outer surface exactly on the torso's 18.0000 side face, and the measurement agrees.

**The rest of that check is not answered.** [`../../build-briefs/torso.md`](../../build-briefs/torso.md)
expects −1.597 at the worst point of the shoulder cone; reaching it means driving the ball mate
around its cone and measuring at each step, and no joint in this assembly was driven. The four
revolute mates carry no limits, and the nine ball mates carry none either, so the assembly will not
report a range or a collision on its own.

**Nothing here checks the ear spring.** `EAR_STRESS` 19.0484 MPa and `EAR_MOVE` 0.2038 mm are hand
calculations in `make_plans.py`; the geometry they describe is built and measured — ear 3.2000
thick, `EAR_FREE` 11, teeth on r 4.8000 — but a stress is not something `bodydetails` returns. The
axis stays open, with the geometry it depends on now confirmed.

## What this run answers that run 5 could not

- **Every station**, including `HEAD_T` and `HEIGHT`, which run 5 was 5.5 short on.
- **Every socket is slit**, including the head's.
- **The thinnest wall in the parts**, with the one number below a nozzle width named and placed:
  the 0.2531 land in the detent band.
- **The zero-pose arm clearance**, +0.7754, measured off the assembly rather than calculated.

Still not answered, in the register's words rather than as a decision: print orientation, joint
ranges, and the ear spring's margin.
