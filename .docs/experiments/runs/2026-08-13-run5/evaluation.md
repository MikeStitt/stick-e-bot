# Run 5 — evaluating the parts and the robot

The three axes from [`../../design-into-cad.md`](../../design-into-cad.md), on the six repaired
parts and then on the assembled figure. Every number was measured after the S1–S4 repairs and the
S6 versions.

## How these were measured

`POST .../featurescript` returned 429 for the whole second half of this run, so nothing here comes
from a Feature Script query. `GET .../parts/d/{d}/w/{w}/e/{e}/partid/{p}/bodydetails` is not rate
limited and returns every face with its surface type, radius, origin, axis, area and box. That is
what the acceptance checks were run against. Sizes come from `boundingboxes`, volumes from
`massproperties`, stations from the assembly's `occurrencetransforms`.

## Matches the sketches

`instructions/robot-guide/make_plans.py` computes the stations. The assembly was measured against
its variables, not against a reading of the drawing.

| Station | `make_plans.py` | Assembly |
| ------- | --------------- | -------- |
| hip, `HIP_Z` | −29 | −29.000 |
| knee, `KNEE_Z` | −53 | −53.000 |
| ankle, `ANKLE_Z` | −77 | −77.000 |
| ground, `SOLE_Z` | −89 | −89.000 |
| neck, `NECK_Z` | +29 | +29.000 |
| top of head, `HEAD_T` | +63.65 | +63.650 |
| whole figure, `HEIGHT` | 152.65 | 152.650 |
| leg, `LEG_X` | ±12 | ±12.000 |
| shoulder ball | (±24.775, −3.912, +9.618) | (±24.775, −3.912, +9.618) |

**Every station matches.** Arm span is not on this list because both shoulders are ball mates and
the arms rest wherever the solver leaves them — the figure has no drawn pose to match.

## Matches the briefs

One part per section, the brief's own *Acceptance checks* in its own words.

### All six

**Parts (1)** in every studio: `Torso`, `Head`, `Hand`, `Foot`, `Upper arm / thigh`,
`Forearm and shin`. Nothing stray, nothing left unmerged.

### Torso

| Check | Got |
| ----- | --- |
| bounding box, with the studs | 55.550 × 24.000 × 64.000 |
| five balls, each Ø6.000 | five spheres, r 3.000, area 105.52 mm² each |
| hips | (±12.000, 0, −29.000) |
| neck | (0, 0, +29.000) |
| shoulders | (±24.775, −3.912, +9.618) |
| shoulder boss cut flush at z = +24 | boss cylinder tops out at 24.000; top face at 24.000 |
| symmetric about YZ | yes — every face maps to a face of the same type, area and mirrored box |

The five balls come back with the *same* area to two decimals, which is what catches a mirror that
lands a stud correctly and fails to union it.

The brief asks for **36.000 × 24.000 × 48.000 before the studs are added**, and that is not what
was measured: the box above is the finished part. The 24.000 in y and the 48.000 in z are still
readable from it — the top and bottom faces are at z ±24.000 and the side faces at x ±18.000 —
but rolling the tree back to take the box the brief describes was not done.

### Head

| Check | Got |
| ----- | --- |
| 36.000 across, 36.000 tall | x ±18.000, z ±18.000 |
| socket center below head center | 16.650 |
| top of head, placed | +63.650, figure 152.650 |
| underside recessed behind the boss | z −18.000 to −17.000, a step of **1.000** |
| socket cavity, right way up | sphere r 3.200 at (0, 0, −16.650), area 91.48 mm² |
| shell over the socket | dome r 4.400 over cavity r 3.200 — **1.200** |
| symmetric about YZ | yes |

The cavity's 91.48 mm² is the area a sphere of r 3.2 has left when a Ø5.803 mouth is cut in it and
nothing else is. A socket built the wrong way up leaves a different area, which is why this is the
check that catches it.

### Foot

| Check | Got |
| ----- | --- |
| length 48.000, width 24.000 | y −32.000 to +16.000, x ±12.000 |
| ground, ankle center | z −12.000, ankle on the origin |
| collar stands proud | z −6.000 (plate top) to +1.350 — **7.350** |
| relief slits | rim at z +1.350 is **four** faces, and the collar is four cylinders at r 4.700 |
| sole ribs | groove floors at z −11.000 in **seven** faces, 419.303 mm²; sole pads at −12.000 |
| symmetric about its fore-and-aft centerline | yes |
| volume | 4899.224 mm³ |

### Hand

Socket cavity r 3.200 on the origin; collar rim at z +1.350 in **four** faces; C-clip at r 5.000.
Volume 530.449 mm³.

### Upper arm / thigh

Socket cavity r 3.200 on the origin; collar rim at z +1.350 in **four** faces; limb r 6.000.
Volume 2040.626 mm³.

### Forearm and shin

Ball r 3.000 at (0, 0, −24.000) — Ø6.000, the station 24 below the pin axis. Limb r 6.000. The
detents measure **24 bumps on each of the two blade faces, exactly 15.000° apart, on a circle of
radius 4.800** — which is `STEP` and `BUMP_R` from `make_plans.py`, and settles the 13-valley
claim S5 removed from the brief. Volume 1949.102 mm³.

## Works as a printable robot

### Printable

Not answered. The thinnest wall in each part is an acceptance check on four of the six briefs and
none of them was measured this run: `bodydetails` gives faces, not the distance between two of
them, and the Feature Script endpoint that would give a minimum-distance query is out of quota.
One wall is known to fail from the head's own brief — the **0.400 mm annular slot** between the
dome over the socket at r 4.400 and the boss's inner wall at r 4.800, which this run measured and
which is narrower than the 0.4 mm nozzle can fill.

Print orientation is not named for any part, and no overhang or bridge was identified.

### Assemblable

**Three of the four sockets are slit and the fourth is not.** The foot, the hand and the upper
arm / thigh each show their collar as four cylindrical faces at r 4.700 and their rim as four
faces at z +1.350. The head's neck socket shows neither: it is one dome, and a render of the
underside shows an unbroken ring around the mouth.

This is not new — [`../../build-briefs/head.md`](../../build-briefs/head.md) already carries it as
an open question, and says why: the socket is bored into a boss standing 1 mm proud, so there is
no free tab length to slit. What this run adds is the measurement rather than the argument, and an
answer to the brief's question. **A ball cannot be seated in the model's own geometry**, because
the model has no flexure: Onshape solves rigid bodies, so the only assembly test available is
whether the mate closes, and a mate closes whether or not a real ball would go in. Every other
ball on the robot passes through a collar that is cut into four tabs; the head's passes through a
continuous rim.

### Functional

Not answered. Joint ranges were not driven. Every joint but the two knees and the two elbows is a
ball mate with no limits set, so the assembly will not report a range or a collision, and nothing
here checks a swing against the part next to it. The torso brief's clearance check — a Ø12 arm
against the torso across the whole cone, expected +0.776 at the zero pose and −1.597 at the worst
point — was not attempted.
