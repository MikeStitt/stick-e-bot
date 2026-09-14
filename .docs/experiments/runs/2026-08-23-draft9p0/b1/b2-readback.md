# B2 — the model read back and checked against `make_plans.py`

Every number here was fetched from Onshape over REST on 2026-08-24 against the `t14 legs`
workspace, and compared with the constants in
[`make_plans.py`](../../../../../instructions/robot-guide/make_plans.py). Nothing was typed in from a
sheet or from an earlier note.

The plan asks for five things: bounding boxes, the collar's outside diameter, the mouth, the
thinnest wall anywhere in each part, and the z-extent of every cut face. All five are below.

The whole fetch is kept in [`b2-raw.json`](b2-raw.json) — every part, every body's faces, and every
bounding box, exactly as Onshape answered — so any number here can be checked without going back to
the CAD. The scripts are in [`scripts/`](scripts): `2000_b2_read.py` fetches,
`2002_b2_check.py` compares against `make_plans.py`, `2004_walls.py` measures the walls,
`2003_feet.py` reads the foot transforms, and `2001_probe.py` is the four-way probe that found
which `bodydetails` path answers.

**Use `/api/partstudios/d/…/e/…/bodydetails`.** The `parts` collection has no `bodydetails` of its
own — `/api/parts/…/e/…/bodydetails` answers 404, and
`/api/parts/…/e/…/partid/{pid}/bodydetails` works but returns the whole studio anyway. The
feature endpoints were rate limited throughout and none of this needed them.

## Part bounding boxes

| studio | part | x | y | z |
| --- | --- | --- | --- | --- |
| `body` | torso | −55.55 … 55.55 | −24.00 … 24.00 | −64.00 … 64.00 |
| `head` | head | −36.00 … 36.00 | −33.00 … 30.00 | −47.00 … 36.00 |
| `ball and socket` | Ball stud | −6.00 … 6.00 | −6.00 … 6.00 | −6.00 … 10.00 |
| `ball and socket` | Socket body | −9.00 … 9.00 | −9.00 … 9.00 | −7.40 … 3.60 |
| `foot` | Foot | −24.00 … 24.00 | −64.00 … 32.00 | −24.00 … 3.60 |
| `hinge` | blade | −12.00 … 12.00 | −12.00 … 12.00 | −44.00 … 12.00 |
| `hinge` | fork | −12.00 … 12.00 | −12.00 … 12.00 | −12.00 … 45.00 |
| `u limb` | u limb | −12.00 … 12.00 | −12.00 … 12.00 | −112.40 … 3.60 |
| `l limb` | l limb | −12.00 … 12.00 | −12.00 … 12.00 | −108.00 … 12.00 |
| `gripper` | Gripper | −9.00 … 9.00 | −9.00 … 9.00 | −24.00 … 3.60 |

What agrees, exactly:

- **`torso` y = 48** is `TORSO_D`. Its z ±64 is the 96 box plus a ball at each end, 48 + 10 + 6,
  where 10 is `STAND` and 6 is `BALL / 2`.
- **`head` x = 72** is `HEAD_W`, and its z stack is right to the millimeter: rim at −47 is
  `HEAD_RIM`, the underside at −36 is `HEAD_RIM + COLLAR_L`, the top at +36 is `HEAD_T` minus the
  neck offset. `HEAD_T` = 137.4 in the assembly, and the assembly reads 137.40.
- **`Socket body` z −7.4 … 3.6** is `GRIP` above the ball center and `COLLAR_L` below that.
- **`Foot` 48 × 96** is `FOOT_W` × `FOOT_L`, and **its z −24.0 … 3.6 is `FOOT_H` exactly.**
- **`Gripper` z −24.0 … 3.6** is `GRIPPER_L` below the wrist center.
- **Every limb and hinge part is 24 across**, which is `LIMB`.

One box does not agree:

- **`head` y is 63 where `HEAD_D` is 60.** The box runs −33 … 30, so the extra 3 is all on the
  front face — the eyes stand proud of it. The sheet draws the head as a 60-deep box and does not
  account for anything standing off it, so either the sheet gains the eyes or `HEAD_D` is not the
  head's depth. Nothing depends on it today; it is wrong on the drawing, not in the print.

## The collar, the mouth, and the wall

| | sheet | model |
| --- | --- | --- |
| collar outside radius | `COLLAR_R` 9.000 | cylinder r9.000, axis Z, on the ball center |
| cavity radius | `CAVITY` 6.800 | sphere r6.800, centered on the ball center |
| ball radius | `BALL / 2` 6.000 | sphere r6.000, same center |
| fit | `FIT` 0.800 | 6.800 − 6.000 |
| mouth across | `MOUTH` 11.538 | see below |

**The mouth is not a face, so it cannot be read off a radius census.** It is the circle where the
plane at `GRIP` cuts the cavity sphere, and the socket's faces are a plane at z 3.6 and a sphere of
r 6.8 — which give √(6.8² − 3.6²) × 2 = **11.538**, `MOUTH` exactly. The check is real; it just
needs the two surfaces rather than one.

**The wall the plan asks about is 2.20, and it is 2.20 in every socketed part.** Measured as the
gap between concentric surfaces within one part:

| studio | part | thinnest | between |
| --- | --- | --- | --- |
| `head` | head | **2.200** | cyl r9.0 / sph r6.8 |
| `ball and socket` | Socket body | **2.200** | cyl r9.0 / sph r6.8 |
| `foot` | Foot | **2.200** | cyl r9.0 / sph r6.8 |
| `u limb` | u limb | **2.200** | cyl r9.0 / sph r6.8 |
| `gripper` | Gripper | **2.200** | cyl r9.0 / sph r6.8 |
| `body` | torso | 2.000 | cyl r8.0 / sph r6.0 — a boss around a solid ball, not a wall |
| `ball and socket` | Ball stud | 3.000 | sph r6.0 / cyl r3.0 — the ball proud of its stalk |
| `l limb` | l limb | 3.000 | the same |
| `hinge` | fork | 9.800 | cyl r2.2 / cyl r12.0 — the stub inside the nose |
| `hinge` | blade | 10.000 | the same, the pocket |

`COLLAR_WALL` is named 3.0 and that is the wall off the **ball**. The printed thickness is off the
**cavity**, and `FIT` eats 0.8 of it: 9.0 − 6.8 = 2.20. The plan already says to quote 2.20 as the
printed thickness, and this is the measurement it asked for.

**Restrict the pair search to one part.** Across a whole studio the thinnest pair in
`ball and socket` comes out 0.800 — the cavity against the ball — which is `FIT`, a clearance
between two parts that never touch as plastic. In `hinge` it comes out 0.200, the detent bumps
against their valleys, which is the snap fit and again spans two parts. Both are real numbers and
neither is a wall.

**What this method cannot see.** It is exhaustive over concentric cylinders and spheres and blind
to everything else — a flat cut face approaching a curved one, two parallel planes, a fillet
running out. `tessellatedfaces` reaches those and was not run. So: **the thinnest concentric wall
in each part is 2.20; the thinnest wall of any kind is not established.**

## The z of every planar cut face

Planes whose normal is along Z, by studio:

| studio | z |
| --- | --- |
| `body` | −48.0, 48.0 |
| `head` | −47.0, −39.0, −36.0, −23.0, −13.0 |
| `ball and socket` | −7.4, −4.4, 3.6, 10.0 |
| `foot` | −24.0, −22.0, −12.0, −4.4, 3.6 |
| `hinge` | −44.0, −20.0, 21.0, 45.0 |
| `u limb` | −79.4, −7.4, −4.4, 3.6 |
| `l limb` | −92.0, −20.0 |
| `gripper` | −20.3, −17.7, −7.4, −4.4, 3.6 |

The recurring −7.4 / −4.4 / 3.6 triple is the socket collar, and it appears unchanged in `head`,
`foot`, `u limb` and `gripper` — which is the Derived-at-Base-origin claim, confirmed a fifth time.

**No cut came out at half its depth.** The check that motivated this — run 2's slit — has no
counterpart here: every z above is a station the sheets name, and there is no face at half of one.
The slit itself is gone, taken out in A7.

## The joint stations, measured

The pin axes and ball centers, each read off its own studio, are what the robot's height is
actually made of:

| station | z | read from |
| --- | --- | --- |
| head top | +137.4 | `head` |
| hip ball | −58.0 | `body` |
| knee pin | −158.4 | the `u limb` pin axis, at −100.4 in its own studio |
| ankle ball | −260.4 | the `l limb` ball stud, at −102 in its own studio |
| sole | −284.4 | the `foot` box, −24.0 below the ankle |

**421.8 mm standing**, against `HEIGHT` = 315.4. The whole 106.4 is the two limb segments, 100.4
and 102 against `LEG_SEG` = 48. Every other station agrees with the sheet.

## What B2 caught that nothing else had

- **The `431.97` in an earlier draft of the register and of `legs.rst` was wrong.** It was the
  assembly's bounding box, and the assembly is posed: both feet are tilted, 12.74° and 9.60°,
  measured off their occurrence transforms. A tilted 96 × 48 sole drops a corner further below its
  ball center than `FOOT_H` does, and that corner was being read as the floor. Corrected in both
  files, and `legs.rst` now teaches the rule rather than falling for it.
- **`FOOT_H` is right.** The register briefly carried a defect saying the foot was 34.6 deep. It is
  24.0. Withdrawn.
- **The head is 3 mm deeper than `HEAD_D`**, because the eyes stand proud. New, small, and on the
  drawing rather than in the part.
