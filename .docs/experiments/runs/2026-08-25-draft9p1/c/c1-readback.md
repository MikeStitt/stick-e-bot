# C1 — the model read back and checked against `make_plans.py`

Every number here was fetched from Onshape over REST on 2026-08-26 against the Main workspace of
`stickbot-draft9p1`, and compared with the constants in
[`make_plans.py`](../../../../../instructions/robot-guide/make_plans.py). Nothing was typed in from
a sheet, from a build brief, or from an earlier note.

This repeats 9p0's [B2](../../2026-08-23-draft9p0/b1/b2-readback.md) against a source that Phase A
changed. It covers what B2 covered — bounding boxes, the collar's outside diameter, the mouth, the
thinnest wall in each part, and the z of every planar cut face — and then the numbers Phase A
moved, each measured on its own.

The whole fetch is kept in [`c1-raw.json`](c1-raw.json): every part, every body's faces, every part
bounding box, the assembly definition with its mates and mate connectors, and the assembly's
bounding box, exactly as Onshape answered. Any number below can be rechecked without opening the
CAD.

The scripts are in [`scripts/`](scripts): `c1_read.py` fetches, `c1_boxes.py` compares the boxes
against `make_plans.py`, `c1_faces.py` builds the face inventory, `c1_zfaces.py` pulls the cut-face
stations, `c1_walls.py` measures the walls, `c1_counts.py` counts the repeated faces, and
`c1_stations.py` reads the assembly.

The reads all went through `/api/partstudios/d/…/e/…/bodydetails`, `/api/parts/…/boundingboxes` and
the assembly endpoints. B2's finding still holds: `bodydetails` belongs to the Part Studio, not to
the `parts` collection, and none of this needs the feature endpoints, which stay rate limited.

## Part bounding boxes

| studio | part | x | y | z |
| --- | --- | --- | --- | --- |
| `body` | torso | −55.551 … 55.551 | −24.000 … 24.000 | −64.000 … 64.000 |
| `head` | head | −36.000 … 36.000 | −33.000 … 30.000 | −47.000 … 36.000 |
| `ball and socket` | Ball stud | −6.000 … 6.000 | −6.000 … 6.000 | −6.000 … 10.000 |
| `ball and socket` | Socket body | −9.000 … 9.000 | −9.000 … 9.000 | −9.053 … 1.946 |
| `foot` | Foot | −24.000 … 24.000 | −64.000 … 32.000 | −24.000 … 1.946 |
| `hinge` | blade | −12.000 … 12.000 | −12.000 … 12.000 | −26.400 … 12.000 |
| `hinge` | fork | −12.000 … 12.000 | −12.000 … 12.000 | −12.000 … 27.400 |
| `u limb` | u limb | −12.000 … 12.000 | −12.000 … 12.000 | −60.000 … 1.946 |
| `l limb` | l limb | −12.000 … 12.000 | −12.000 … 12.000 | −54.000 … 12.000 |
| `gripper` | Gripper | −9.000 … 9.000 | −9.000 … 9.000 | −24.000 … 1.946 |

What agrees, exactly:

- **`torso` is 72 × 48 × 96** — `TORSO_W`, `TORSO_D`, `TORSO_H`. Its z ±64 is the 96 box plus a
  ball at each end, `STAND` 10 and `BALL / 2` 6. Its x ±55.551 is the shoulder stud reaching out
  past the box.
- **`head` x = 72** is `HEAD_W` and its rim at z −47 is `HEAD_RIM` measured from the neck.
- **`head` y = 63 is `HEAD_D` 60 plus `#face` 3.** 9p0 read the same 63 and called it a defect
  because nothing in the source accounted for the extra 3. A8 gave that 3 a name and a single home:
  `#face` is the one number the eye stands proud by and the mouth cuts in by. The box agrees with
  the source now.
- **Every limb and hinge part is 24 across**, which is `LIMB`.
- **`u limb` z −60 … 1.946** is `GRIP` above the shoulder center at one end and
  `LIMB_CENTER + NOSE`, 48 + 12, at the other.
- **`l limb` z −54 … 12** is `NOSE` above the elbow pin and `LIMB_CENTER + BALL / 2`, 48 + 6, below
  it.
- **`Gripper` z −24.000** is `GRIPPER_L` below the wrist center.
- **`Foot` is 48 × 96**, `FOOT_W` × `FOOT_L`, with its sole `FOOT_H` 24 below the ankle center.

Three boxes moved since 9p0, and each moved for a reason Phase A or Phase B recorded:

- **The socket sits at −9.053 … 1.946 where 9p0 read −7.400 … 3.600.** It is the same 11.0 long.
  A2 made `#fit` a clearance rather than a scale factor, so `GRIP` fell from 3.6 to 1.9465 and the
  whole collar came down with it. **The socket's height did not change**, which is the point A2
  was making.
- **The hinge's blade and fork are each 5.6 shorter** — 26.4 and 27.4 where 9p0 read 44.0 and 45.0.
  B7 changed `#rod` from `#limbD` 24 to `#ear` 6.4. That is the shank behind the joint, not the
  joint.
- **`u limb` and `l limb` are 60 and 54 long where 9p0 read 112.4 and 108.** A1 replaced
  `#limbSeg`, a length, with `#limbCenter`, a station. Each limb now reaches exactly one joint
  spacing and no further.

## The collar, the mouth, and the wall

| | source | model |
| --- | --- | --- |
| collar outside radius | `COLLAR_R` 9.0 | cylinder r 9.0000 |
| collar length | `COLLAR_L` 11.0 | z −9.0535 … 1.9465 |
| cavity radius | `CAVITY` = `BALL` / 2 + `FIT` = 6.08 | sphere r 6.0800 |
| ball radius | `BALL` / 2 = 6.0 | sphere r 6.0000 |
| stalk radius | `STALK` / 2 = 3.0 | cylinder r 3.0000 |
| how deep the center sits | `GRIP` 1.9465 | top face at z 1.9465 |
| mouth | `MOUTH` 11.52 | top annulus 129.460 mm² |
| slit width | `SLIT_W` 1.6 | walls at ±0.8 |
| how far a slit reaches in | — | relief faces at r 5.0 |
| slit length | source comment says 11.0 | floor at z −6.0535, so 8.0 |

**The mouth is proved by area, not by a diameter.** Onshape reports no diameter for a hole that is
an edge rather than a face, so the check is the area of the ring the mouth leaves. A collar of
radius 9.0 with a mouth of radius 5.76, less four slits 1.6 wide crossing it, comes to 129.50 mm².
The model reports 129.460 mm², and the 0.04 is the slit ending on the collar's round outside rather
than on a straight line. `MOUTH` is 11.52 exactly, and the ring is on top, so **every socket in the
robot opens upward**.

The thinnest wall in each part, measured as the radius gap between two faces on one axis:

| part | thinnest wall | what it is |
| --- | --- | --- |
| `head`, `foot`, `u limb`, `Gripper`, `Socket body` | 2.9200 | collar r 9.0 over cavity r 6.08 |
| `Ball stud`, `l limb` | 3.0000 | ball r 6.0 over stalk r 3.0 |
| `Gripper` clip | 3.3500 | clip r 5.0 over bore r 1.65 |
| `torso` | 3.0000 | ball r 6.0 over stalk r 3.0 |
| `hinge` fork, `u limb` fork | 9.8000 | ear r 12.0 over bore r 2.2 |
| `hinge` blade, `l limb` blade | 10.0000 | knuckle r 12.0 over axle r 2.0 |

**The thinnest wall anywhere in the robot is 2.92 mm**, and it is in every part that carries a
socket. `COLLAR_WALL` is 3.0, but that 3.0 is measured over the ball, and the cavity is the ball
plus `FIT`. The wall a printer sees is 3.0 − 0.08.

## The z of every planar cut face

| part | z, with the area at that z in mm² |
| --- | --- |
| `torso` | −48.000 (3399.451), 48.000 (3513.459) |
| `head` | −47.000 (129.460), −39.000 (25.524), −36.000 (2594.628), −23.000 (90.000), −13.000 (90.000) |
| `Socket body` | −9.053 (254.469), −6.053 (25.524), 1.946 (129.460) |
| `Ball stud` | 10.000 (28.274) |
| `Foot` | −24.000 (1761.451), −22.000 (1808.348), −12.000 (1605.924), −6.053 (25.524), 1.946 (129.460) |
| `blade` | −26.400 (452.389), −20.000 (234.215) |
| `fork` | 21.000 (258.697), 27.400 (452.389) |
| `u limb` | −36.000 (258.697), −9.053 (197.920), −6.053 (25.524), 1.946 (129.460) |
| `l limb` | −38.000 (424.115), −12.000 (234.215) |
| `Gripper` | −20.300 (68.615), −17.700 (74.805), −13.053 (93.957), −6.053 (25.524), 1.946 (129.460) |

Read across the rows and the same three z values keep coming back: **1.946, −6.053 and −9.053 are
`GRIP`, the slit floor and the collar's root**, and they are identical in the head, the foot, the
upper limb and the gripper. One socket, drawn once, reused five times.

The areas are the check, not decoration:

- **`torso` at −48** is 3399.451, which is 72 × 48 less two hip stalks, 3456 − 2π × 3², exactly.
- **`fork` at 21.000** is the slot's root. The fork's tip is at −12, `NOSE` below the pin, so the
  slot is 33 deep — `SLOT_DEEP` exactly.
- **`blade` at −20.000** is where the knuckle ends. The blade's nose is at +12, so it stands 32
  out — `BLADE_OUT` exactly. Below −20 is 6.4 of shank, which is `#ear`.
- **`l limb` at −38.000** is 424.115, a Ø24 rod less the Ø6 stalk leaving it, π(12² − 3²), exactly.
- **`u limb` at −9.053** is 197.920, the ring where the Ø24 rod meets the Ø18 collar,
  π(12² − 9²), exactly.
- **`Gripper` at −20.300 and −17.700** are the two lips of the clip, 2.6 apart, which is
  `CLIP_MOUTH`.

## The joint stations, measured

Every instance in the assembly sits at identity rotation, so the station is the translation.

| instance | x | y | z | source |
| --- | --- | --- | --- | --- |
| `torso <1>` | 0 | 0 | 0 | fixed to the origin |
| `head <1>` | 0 | 0 | 103.054 | `NECK_Z` 58 plus the head's own 45.054 |
| `u limb <1>`, `<2>` | ±49.551 | −7.824 | 19.235 | `SH_X`, `SH_Z` |
| `l limb <1>`, `<2>` | ±49.551 | −7.824 | −28.765 | one `LIMB_CENTER` below the shoulder |
| `Gripper <1>`, `<2>` | ±49.551 | −7.824 | −76.765 | two below |
| `u limb <3>`, `<4>` | ±24.000 | 0 | −58.000 | `LEG_X`, `HIP_Z` |
| `l limb <3>`, `<4>` | ±24.000 | 0 | −106.000 | `KNEE_Z` |
| `Foot <1>`, `<2>` | ±24.000 | 0 | −154.000 | `ANKLE_Z` |

Every leg station is one `LIMB_CENTER` from the last: −58, −106, −154 step by 48, and the sole is
`FOOT_H` below the ankle at −178, which is `SOLE_Z`. **A1's claim is that a limb reaches exactly
one station, and the assembly is where that shows.**

The assembly's own bounding box:

| | model | source |
| --- | --- | --- |
| top | 139.0535 | `HEAD_T` 139.05351599030456 |
| sole | −178.0000 | `SOLE_Z` −178.0 |
| **height** | **317.0535** | **`HEIGHT` 317.05351599030456** |
| width across the arms | 123.1018 | 2 × `SH_X` + `LIMB` |
| depth | 96.0000 | the foot, `FOOT_L` |

**The robot's height comes out at what the sheets draw**, to four decimal places, from a box
Onshape computed over fourteen instances that were placed by mates rather than by numbers.

## The numbers Phase A moved

| decision | what it moved | measured |
| --- | --- | --- |
| A1 `#limbCenter` | limb length becomes a station | `u limb` 60, `l limb` 54; stations step by 48 |
| A2 `#fit` 0.08 | cavity 6.08, `GRIP` 1.9465, socket height unchanged | sphere r 6.0800, top at 1.9465, collar 11.0 |
| A3 eye ellipse | 16 × 8 ellipses at ±12 and +8, `#face` proud | two faces in x 4…20, z 4…12; area 201.062 = 2π × 8 × 4 |
| A4 hinge handedness | every protrusion on the blade, every recess in the fork | blade: axle r 2.0, 48 bumps r 0.8. fork: bore r 2.2, 48 valleys r 1.0 |
| A5 foot tread | grooves phased off `#rib_w` / 2, solid at both ends | 16 walls from y −61 to +29, 8 grooves 6 wide on a 12 step, 3 solid at each end, 2 deep |
| A8 head numbers | `#face` 3 owns the eye's proud and the mouth's cut | head 63 deep, mouth floor 3 in, eye 3 out |
| A8 pupils | decided against | no face inside the eye ellipse |
| A9 `#boss_d` | typed 16 becomes a variable | boss cylinders r 8.0000 |
| A9 upper rounds | agreed radius `HEAD_ROUND` 12 | fillet r 12.0000 |
| A10 gripper | `CLIP_R` 5.0, `CLIP_BORE` 3.3, `CLIP_MOUTH` 2.6, `CLIP_W` 18.0 | r 5.0000, r 1.6500, lips 2.6 apart, x ±9 |
| A11 rest pose | every instance square to the world | fourteen occurrences at identity rotation |

The mouth is the head's other A8 number and it lands exactly: the slot's edges are at z −13 and
−23, which is `MOUTH_DN` 13 and `MOUTH_H` 10, its ends are r 5 at x ±15, and its floor is
378.540 mm², which is 30 × 10 + π × 5² with nothing left over.

## What C1 caught that nothing else had

- **The socket's slit is 8.0 long, not the collar's 11.0.** `make_plans.py` line 73 calls
  `SLIT_W` "the socket's relief slit, four of them, the collar's whole length", and the sheet at
  line 414 labels it the same way. The model's slit floor is at z −6.0535, which is 3.0 above the
  collar's root — a solid ring, `COLLAR_WALL` thick, holding the four tabs together. The model is
  right and the comment is stale. The tabs' free length is 8.0.
- **The feet are at ±24 where `FOOT_X` is 32.** B9 found why: the foot's `mate to robot` connector
  was on a wall of the snap slit, and re-pointing it at the Origin put both feet on their hip line.
  The sheets draw the ankle inboard of the foot's own center, which needs a handed foot. That is a
  design-source decision, not a modeling error, and it is open.
- **`BLADE_OUT` and `SLOT_DEEP` are not stale.** The hinge's bounding box shrank by 5.6 at both
  ends, which looked at first like the two constants had drifted. They have not: the blade stands
  32 out of its own shank and the fork's slot is 33 deep, both exactly, and the whole 5.6 is B7's
  `#rod` change behind the joint. The suspicion is withdrawn.
