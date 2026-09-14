# Run 5 — the audit

Phase 3 of [`../../design-into-cad.md`](../../design-into-cad.md). Every part measured through the
FeatureScript endpoint and looked at in four rendered views. Measurements are in `measured.json`,
the target in `target.json`, the renders in [`shots/`](shots/).

Nothing here is inferred from the change list. Where the two agree it is said so; where the audit
found something the change list did not anticipate, it is marked **new**.

## What every part got right

Said first, because the repair list below is long and most of the robot is correct. Ball radius
3.000 and cavity radius 3.200 everywhere. Every socket rim sits at `#grip` = 1.35 above its ball
center. The hand's collar is four cylindrical faces — a properly slit collar. The torso's hips are
plain Ø3 stalks standing 5 off the bottom face, which is what the brief settled. The head carries
its Ø12 neck recess (an r6.0 cylinder) and its socket center measures −16.650 exactly.

## torso — rebuild the shoulder, add the neck boss

Measured: balls at (±23, 0, +24), (±12, 0, −29) and (0, 0, +29); **five cylinders, all r1.5**, and
nothing else. Five Ø3 stalks and no boss of any kind anywhere on the part.

| Delta | Target | Measured | Route |
| ----- | ------ | -------- | ----- |
| shoulder ball center | (±24.775, −3.912, **+9.618**) | (±23, 0, +24) | rebuild |
| shoulder stud direction | 53° below horizontal, 30° forward | square to the side face | rebuild |
| shoulder boss | Ø8, 8 long, coaxial, cut flush at the top face | absent | rebuild |
| shoulder stalk | Ø3, the last 5 mm | Ø3 the whole way | rebuild |
| shoulder root | side face at x = ±18, z = +20 | z = +24 | rebuild |
| neck boss | Ø12 on the top face, on the axis | absent | new feature |

The shoulder ball is **14.4 mm** from where the design puts it. This is not a dimension edit; the
stud leaves on a doubly-rotated axis that the part has no plane for.

## limb-socket-clevis — rebuild the fork

Measured: Y-normal planes at ±0.4, ±1.0, ±1.8, ±2.5, ±3.0; cylinders r1.0 ×2, r4.7 ×4, r5.81 ×2,
r6.0 ×1; cavity sphere r3.2 on the origin; bbox z −29.81 … +1.35.

| Delta | Target | Measured | Route |
| ----- | ------ | -------- | ----- |
| slot half-width | 2.8 | 1.8 | sketch |
| ear thickness | 3.2 | 1.2 | sketch |
| ear outer surface | **the Ø12 cylinder — no outer plane at all** | planes at ±3.0 and ±2.5 | rebuild |
| round end | r6 | r5.81 | sketch |
| fork tip | z = −30 | z = −29.81 | follows the round end |
| stub inner face | ±2.0, being 0.8 proud of a 2.8 ear | ±1.0 | sketch |
| slot root | z = −13, so 11 behind the pin axis | to confirm during repair | sketch |

Correct already: the socket collar is four r4.7 faces, the relief slits are 0.8 (planes at ±0.4),
the stub is r1.0 — `STUB` 2.0 across — and the cavity is on the origin.

## limb-blade-ball — rebuild the blade, add the slit

Measured: Y-normal planes at ±0.5, ±1.05 ×24, ±1.5; cylinders r0.5 ×48, r1.1 ×2, r1.5, r5.81,
r6.0; ball r3.0 at (0, 0, −24); bbox z −27 … +5.81.

| Delta | Target | Measured | Route |
| ----- | ------ | -------- | ----- |
| blade half-thickness | 2.5 | 1.5 | sketch |
| detent valley floors | ±2.05 | ±1.05 | sketch |
| round end / blade tip | r6, tip at z = +6 | r5.81, tip at +5.81 | sketch |
| blade's limb stops at | z = −10 | to confirm during repair | sketch |
| **the slit** | 0.8 wide, 16 deep, down the blade's middle, open at the tip, leaving two 2.1 tabs | **absent — the blade is solid** | new feature |

Correct already: 24 valleys of r0.5 at 15°, the two r1.1 pockets, and the ball on its station.

**New — not in the change list.** The detent is **24 valleys per side**, not the 13 that run 4's
notes recorded. The feature is named "24 detent valleys" and 48 r0.5 cylinders are present, 24 a
side. Run 4 counted faces on one visible arc and wrote down the count it saw.

## foot — add the slits; two conflicts

| Delta | Target | Measured | Route |
| ----- | ------ | -------- | ----- |
| ankle socket relief slits | four, 0.8 wide, the collar's length | **none** | new feature |
| collar length | set by the plate | 7.35 | **no repair** — a record, not a target |

The collar is **one** cylindrical face of r4.700 with an area of **217.053 mm²**. A full cylinder
of that radius and 7.35 long is 2π × 4.7 × 7.35 = 217.05. The face is the entire circumference to
six figures, so there is no slit anywhere in it and this is the one joint on the robot that cannot
be pressed together. The top render shows a plain bore.

**Conflict — the foot's axis.** [`foot.md`](../../build-briefs/foot.md) sketches the outline on the
Top plane with its length fore-and-aft along Y. The model runs it along **X**, x −16 … +32, and the
assembly turns each foot 90° about Z to compensate. Both work; they disagree about what the part
looks like to anyone reading the brief. For phase 4.

**Conflict — the foot is not symmetric.** Two r4.000 cylinders at (5.14, 5.94) and (7.10, −6.22)
are not a mirror pair, and the top render shows the two end blends landing differently. The brief
requires symmetry about the fore-and-aft centerline so that one part serves both sides. Fixing the
sketch is cheap; deciding whether the asymmetry was ever intended is not mine.

## head — no repair

Socket cavity r3.200 at (0, 0, −16.650), the Ø12 neck recess present as an r6.0 cylinder, shell
measured, bbox z ±18 for a 36 tall head. Everything the change list anticipated is already true.

**New.** A second spherical face of r4.400 shares the socket's center — the shell carrying the
cavity outward by its 1.2 wall. Expected for a shelled part, and worth recording so a later audit
does not read it as a second socket.

The head's open item is not a head defect: its tilt argument needs the torso's neck boss, which
the torso does not have. It closes when the torso is repaired.

## hand — no repair

Collar four r4.7 faces, clip r5.0, bore r1.650, socket on the origin. The bore is the open
question the brief already carries — 3.3 as built against 3.6 by the radial `#fit` convention. The
row is marked `proposed` and asks the builder to say which was used and why, so this is a decision
for phase 4, not a repair.

## Summary by route

| Part | Route | What |
| ---- | ----- | ---- |
| torso | rebuild + new feature | the shoulder stud; the neck boss |
| limb-socket-clevis | rebuild | fork thickness, slot, ear outer surface, round ends |
| limb-blade-ball | rebuild + new feature | blade thickness, detent stack, round ends; the slit |
| foot | new feature | four relief slits |
| head | none | — |
| hand | none | — |

Three questions go to phase 4 rather than to a repair: the foot's axis, the foot's symmetry, and
the gripper's bore convention.
