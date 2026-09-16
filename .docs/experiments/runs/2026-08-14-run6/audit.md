# Run 6 — the audit

Phase 5 of [`plan.md`](plan.md). Every rebuilt part measured off its **named version** — not a
workspace — through `bodydetails`, `boundingboxes`, `massproperties` and `features`. The numbers are
in [`measured.json`](measured.json), run 5's in
[`../2026-08-13-run5/measured.json`](../2026-08-13-run5/measured.json), the design's own numbers in
[`target.json`](target.json).

Every difference between the two runs is classified here as one of three things, in these words:

- **run 5 defect** — run 5 had it wrong, the rebuild has it right.
- **run 6 regression** — run 5 had it right, the rebuild does not.
- **deliberate** — [`design-note.md`](design-note.md) or a brief says to build it this way.

Nothing is waved through because it is small: where a face count or an area moved and the cause is
not obvious, the cause is worked out below or the entry says it was not established.

## What the rebuild hits exactly

Said first. Against [`target.json`](target.json), measured on the versions:

| number | target | measured |
| ------ | ------ | -------- |
| `SH_X`, `ARM_PLANE_Y`, `SH_Z` | shoulder ball at (±24.7754, −3.9118, +9.6177) | (±24.7754, −3.9118, +9.6177) |
| `BOSS_D` | Ø8 shoulder boss | two cylinders r 4.0000 |
| `LEG_X`, `HIP_Z` | hip balls at (±12, 0, −29) | (±12.0000, 0.0000, −29.0000) |
| `NECK_Z` | neck ball at (0, 0, +29) | (0.0000, 0.0000, +29.0000) |
| `S` | Ø6 balls | five spheres r 3.0000 |
| `TORSO_W`, `TORSO_D` | 36 × 24 block | planes at x ±18.0000, y ±12.0000 |
| `HEAD_W`, `HEAD_H` | 36 × 36 head | x ±18.0000, z −18.0000..+18.0000 |
| `HEAD_T`, `HEAD_B` | top 69.15, base 33.15 with the neck ball at +29 | socket centre 22.1500 below the head's centre, which puts them there |
| `CAVITY`, `GRIP`, `MOUTH` | cavity r3.2, rim 1.35 above the ball centre, mouth Ø5.8026 | every socket: r 3.2000, +1.3500, Ø5.8026 |
| `COLLAR_WALL` | 1.5 | 4.7000 − 3.2000 on every collar |
| `SLIT_W` | 0.8 | slit walls at ±0.4000 on every slit collar |
| `BLADE` | 5.0 thick | blade planes at y ±2.5000 |
| `SLOT` | 5.6 | fork slot planes at y ±2.8000 |
| `STUB` | 2.0 | stub planes at y ±2.0000 |
| `LIMB` | Ø12 | r 6.0000 on both limbs, and nothing outside it |
| `BUMP_R`, `BUMP_D` | detent bumps Ø0.8 on r4.8 | 48 spheres r 0.4000, every centre 4.8000 from the hinge axis |
| `VALLEY_D`, `VALLEY_DEEP` | valleys Ø1.0 × 0.45 | 48 cylinders r 0.5000, floors 0.4500 down |
| `FOOT_H` | ankle 12 above the ground | sole at z −12.000 with the ball centre on the origin |
| `GRIPPER_L`, `CLIP_R` | 12 long, clip r5 | z +1.3500 to −12.0000, cylinders r 5.0000 |

Every part is a single body, and every part's own acceptance list is checked in
[`build-notes.md`](build-notes.md) rather than repeated here.

## The one thing missing from every part

**No run 6 part carries a mate connector.** Run 5's six parts carry twelve between them — `Socket`
on the foot and the hand, `Neck socket` on the head, `Hinge` and `Ball` on the blade limb, `Socket`
and `Hinge` on the clevis limb, and `Neck`, `Shoulder R`, `Shoulder L`, `Hip R`, `Hip L` on the
torso. Run 6's parts carry none: phase 4 built geometry and stopped there.

**Classification: run 6 regression**, and it is the one that has to be cleared before phase 6.
[`design-note.md`](design-note.md) already says what the connectors cost — a Boolean Union drops the
connectors of every part it consumes, so each one is re-made on the host against merged geometry —
and phase 6 assembles from named versions, so the versions cited in `build-notes.md` will each need
a successor once the connectors are placed.

## torso

| Delta | run 5 | run 6 | Classification |
| ----- | ----- | ----- | -------------- |
| shoulder ball centre | (±23, 0, +24) | (±24.7754, −3.9118, +9.6177) | **run 5 defect** — 14.4 mm out, and run 5's own audit routed it to a rebuild |
| shoulder boss | absent | two cylinders r 4.0000 | **run 5 defect** — `torso.md` gives the Ø8 coaxial boss |
| bounding box in x | ±26.0000 | ±27.7754 | follows the shoulder move |
| side face at x ±18 | 1148.4657 mm² plus a 3.5343 mm² half-disc left coplanar with it — 1152.0000 together, the full 48 × 24 | one face, 1071.9773 mm² | follows the boss: run 5's stalk sits *on* an untouched side face, run 6's Ø8 boss enters it and takes an 80.0227 mm² ellipse out |
| volume | 42115.1051 | 42890.0333 (+774.9282) | follows the boss and the moved studs |
| neck boss | absent | absent | **deliberate** — `torso.md`: "it cannot buy the tilt it exists for, so it is not built" |
| mate connectors | `Neck`, `Shoulder R`, `Shoulder L`, `Hip R`, `Hip L` | none | **run 6 regression** |

Unchanged and correct in both: five Ø6 balls on Ø3 stalks, hips at (±12, 0, −29), neck at
(0, 0, +29), the 36 × 24 × 48 block.

## head

The whole delta is one deliberate change and its consequences.
[`design-note.md`](design-note.md) replaces the head's own neck recess with the **standard socket
collar**, and `head.md` builds it.

| Delta | run 5 | run 6 | Classification |
| ----- | ----- | ----- | -------------- |
| neck | recess cylinder r 6.0000 and bump r 4.8000, both at z −17.0000 | collar cylinder r 4.7000 in four tabs, z −23.5000..−18.0000 | **deliberate** |
| socket centre | (0, 0, −16.65) | (0, 0, −22.15) | **deliberate** — 5.500 lower, the collar's proud length |
| bounding box in z | −18.0000 | −23.5000 | follows the collar |
| cavity | one sphere r 3.2000 | four spheres r 3.2000, and four r 4.4000 | **deliberate** — the slits cut the cup into four, and the shell gives the second surface |
| collar bore | none | four cylinders r 3.5000 | follows the shell: 4.7000 − 1.2000 |
| rim | recess floor at z −17.0000 and a chamfer at −15.8000 | four rim faces at z −23.5000 | **deliberate** |
| slits | none on the neck | eight walls at x or y ±0.4000, each running the collar's whole 5.500, and the shell repeats each of them 1.2 out at ±1.6000 | **deliberate** |
| volume | 5805.0435 | 6019.0314 (+213.9880) | follows the collar |
| mate connector | `Neck socket` | none | **run 6 regression** |

Unchanged in both: the 36 × 36 head with its r 18.0000 top round, the four r 3.0000 outline rounds,
the eyes, the mouth with its r 2.0000 ends, and the 1.2 shell — which shows up as the same three
paired radii in each run (3.0000/1.8000, 2.0000/3.2000, 18.0000/16.8000).

The station arithmetic closes on the new geometry: the socket centre is 22.15 below the head's
centre, the torso's neck ball is at +29, so the head's base lands at 33.15 and its top at 69.15 —
`HEAD_B` and `HEAD_T` exactly. Run 5's head, with its socket 5.5 higher, would put the top of the
figure at 63.65. **Measured against today's target, run 5's head is 5.5 short**, which is the same
finding stated from the other side.

## limb-socket-clevis

Run 5's audit routed five separate defects on this part. All five measure fixed, and the ear's
teeth — which run 5 did not have at all — are built.

| Delta | run 5 | run 6 | Classification |
| ----- | ----- | ----- | -------------- |
| slot half-width | y ±1.8000 | y ±2.8000 | **run 5 defect** — `SLOT` 5.6 |
| stub inner face | y ±1.0000 | y ±2.0000 | **run 5 defect** — `STUB` 2.0 |
| ear outer surface | planes at y ±3.0000 and ±2.5000 | none — the Ø12 cylinder carries it | **run 5 defect** |
| round end | cylinder r 5.8100 ×2 | r 6.0000 ×3 | **run 5 defect** |
| fork tip | z −29.8100 | z −30.0000 | follows the round end |
| slot root | z −17.8900 | z −13.0000 | **run 5 defect** — 11 behind the pin axis, as `hinge.md` gives it |
| detent teeth | none | 48 spheres r 0.4000 on r 4.8000, 24 an ear | **run 5 defect** — `hinge.md`: teeth on the ear, valleys on the blade |
| socket slit ends | planes at x ±2.5000, cavity one sphere face | none, cavity four sphere faces | **run 5 defect** — the same short slit the hand has |
| face count | 36 | 127 | follows the teeth |
| volume | 2084.1288 | 2041.9142 (−42.2146) | follows the slot, the ear and the teeth together |
| mate connectors | `Socket`, `Hinge` | none | **run 6 regression** |

Unchanged and correct in both: the socket collar as four r 4.7000 faces, relief slits 0.8 wide, the
cavity sphere r 3.2000 on the origin, the stub r 1.0000, the rim at z +1.3500.

## limb-blade-ball

| Delta | run 5 | run 6 | Classification |
| ----- | ----- | ----- | -------------- |
| blade half-thickness | y ±1.5000 | y ±2.5000 | **run 5 defect** — `BLADE` 5.0 |
| valley floors | y ±1.0500 | y ±2.0500 | follows the blade thickness — still 0.45 deep |
| round end | cylinder r 5.8100 | r 6.0000 ×3 | **run 5 defect** |
| bounding box in z | +5.8100 | +6.0000 | follows the round end |
| ball-end slit | none | walls at y ±0.4000, root plane at z −10.0000 | **run 5 defect** — run 5's audit routed "add the slit" |
| planes at x ±5.8100 and z −6.1100 | one and four | none | follows the blade and round-end rebuild — run 6's blade ends on the Ø12 cylinder, not on flats |
| volume | 2039.6356 | 1949.1024 (−90.5332) | follows the slit and the round end |
| mate connectors | `Hinge`, `Ball` | none | **run 6 regression** |

Unchanged and correct in both: 24 valleys a side at 15° on r 4.8000, Ø1.0 × 0.45 with an r0.1 broken
rim, the pocket r 1.1000, the ball r 3.0000 at (0, 0, −24), the Ø12 limb.

## hand

One delta, and it is the slit.

| Delta | run 5 | run 6 | Classification |
| ----- | ----- | ----- | -------------- |
| slit ends | planes at x ±2.5000 and y ±2.5000, 1.7327 mm² each | none | **run 5 defect** — `gripper.md` has the slit rectangle running clear past the collar both ways |
| slit walls | 10.3269 mm² each | 13.2928 mm² each | follows: run 6's slit crosses the whole collar |
| cavity | one sphere face, 80.1417 mm² | four sphere faces, 71.5696 mm² | follows: run 5's cup is still joined under the slits |
| collar foot at z −4.1500 | twelve faces, 20.4800 mm² | nine faces, 27.8400 mm² | follows the same cut |
| face count | 40 | 36 | follows |
| volume | 530.4489 | 520.4792 (−9.9697) | the material run 5's slit left under the cup |
| mate connector | `Socket` | none | **run 6 regression** |

Identical in both, to the fourth decimal: the clip (bore r 1.6500, outer r 5.0000 ×2, lips at
z −5.7000 and −8.3000 at 22.8715 mm² each), the collar's four r 4.7000 faces at 143.7456 mm²
together, and the rim's four 9.2966 mm² tabs. Run 5's slit reads correct at the rim and at the outer
wall, and only the cavity says it stopped short — which is why the cavity's face count is worth
measuring and not only its volume.

## foot

| Delta | run 5 | run 6 | Classification |
| ----- | ----- | ----- | -------------- |
| which way the foot points | length on X, toe at +32 | length on Y, toe at −32 | **run 5 defect** — run 5 assembled a figure whose feet pointed behind its head; run 5.1 turned it and `foot.md` states the sign |
| socket relief slits | none — collar one face, cavity one face, rim one face | collar four faces, cavity four, rim four | **run 5 defect** — `foot.md`: without slits this is the one joint nobody can assemble |
| collar cylinder | 217.0526 mm² | 193.5040 mm² | follows the slits |
| rim at z +1.3500 | 42.9534 mm² | 37.1864 mm² | follows the slits: the annulus less two 0.8 bands |
| plate's top face | 395.7004 mm² | 410.0822 mm² | follows the slits, and closes: 2 × 7.5100 − 0.64 = **14.3818**, against 410.0822 − 395.7004 = 14.3818 |
| volume | 4945.5031 | 4875.8691 (−69.6340) | the four slits |
| mate connector | `Socket` | none | **run 6 regression** |

Identical in both, to the fourth decimal: the sole's eight rib faces at z −12.000 totalling
473.3770 mm², the seven groove floors at z −11.000 totalling 419.0727 mm², the r4 top fillet's four
faces (two r 4.0000 at 348.2494 mm², one r 8.0000, one r 12.0000), and the collar's 7.3500 of proud
length. The foot's outline and its ribs came out of two
independent builds the same to four decimals, which is the strongest statement in this audit about
the briefs being followable.

## What the design note asked for and did not get

**The foot's socket pad is not built.** [`design-note.md`](design-note.md) proposes a pad of the
collar's own diameter under the ankle socket, so that the standard collar mounts on a face one
`grip` below its rim and the foot stops being the one non-standard socket.
[`foot.md`](../../build-briefs/foot.md) does not carry the pad — it says the proud length is set by
the plate, gives 7.35, and tells the builder to measure the gap and *not* move the plate to close
it. The build followed the brief.

So the measurement stands where run 3 and run 4 left it: **the collar stands 7.3500 proud against
the 5.5 every other socket uses**, and the two documents disagree about whether that is the design.
The gap is 1.85, the slits run that whole longer length, and the tab flex the joint depends on is
therefore not the same on the foot as on the head, the hand or a limb. **Not resolved by run 6** —
it needs the brief and the design note brought into line before either is built to again, which is a
decision, not a measurement.

The design note's two other items came through: the head's standard neck collar is built, and the
torso's shoulder connectors were left for the route the spike settled — which is now the general
connector gap above.

## Where this leaves phase 6

Assembly needs connectors, and no part has one. The geometry is ready: every joint measures to its
target, both limbs are Ø12 with nothing outside it, and both halves of both joints exist on the
parts that carry them. The work before assembly is placing connectors on merged geometry, part by
part, and publishing a version of each that carries them.
