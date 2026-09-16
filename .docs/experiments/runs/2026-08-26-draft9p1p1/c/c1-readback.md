# C1 — the model read back

Every number below comes from one REST fetch, [`c1-raw.json`](c1-raw.json), taken by
[`scripts/c1_read.py`](scripts/c1_read.py) and judged offline by
[`scripts/c1_check.py`](scripts/c1_check.py). Nothing here was read off a dialog.

## Where the work is

| | |
| --- | --- |
| document | `stickbot-draft9p1p1`, `4b2e0d48efd37d3327a90afb` |
| workspace | Main, `a1af16872d25103815f1c32a` |
| version | `Recovery point`, `0f4e9b6b36b5c1a6f45197e1`, cut at the end of Phase C |
| live | [the workspace](https://cad.onshape.com/documents/4b2e0d48efd37d3327a90afb/w/a1af16872d25103815f1c32a) |

[`c3-inspection.md`](c3-inspection.md) records opening the version's own link and measuring it.

## The variable table

Eleven rows. Three are typed and eight are expressions; `#collar` is the row this draft moved
across that line.

```
torsoH 96 mm    torsoW 72 mm    torsoD 48 mm    limbCenter 48 mm
ball #torsoH / 8        limbD #torsoH / 4       wall #torsoH / 32
stand #ball * 5 / 6     collar #ball / 2 + #wall        fit 0.08 mm
grip sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball) ^ 2)
```

## Every part, in its own Part Studio

| part | x | y | z | z span |
| --- | --- | --- | --- | --- |
| `torso` | 111.1018 | 48.0000 | −64.0000 … 64.0000 | 128.0000 |
| `head` | 72.0000 | 63.0000 | −46.9465 … 36.0000 | 82.9465 |
| `Ball stud` | 12.0000 | 12.0000 | −6.0000 … 10.0000 | 16.0000 |
| `Socket body` | 18.0000 | 18.0000 | −9.0000 … 1.9465 | 10.9465 |
| `Foot` | 48.0000 | 96.0000 | −24.0000 … 1.9465 | 25.9465 |
| `blade` | 24.0000 | 24.0000 | −26.4000 … 12.0000 | 38.4000 |
| `fork` | 24.0000 | 24.0000 | −12.0000 … 27.4000 | 39.4000 |
| `u limb` | 24.0000 | 24.0000 | −60.0000 … 1.9465 | 61.9465 |
| `l limb` | 24.0000 | 24.0000 | −54.0000 … 12.0000 | 66.0000 |
| `Gripper` | 18.0000 | 18.0000 | −24.0000 … 1.9465 | 25.9465 |

Every one is what [A2's table](../plan.md) says it should be, to the digit. The socket's root is at
**z −9.0000** and `#collar` is 9, which is the whole of A2 in one number.

## A1 — the cut is a slot, and there is no face at r 5.0

`ball and socket` holds two bodies. Every curved face in the tab is one of **r 3.0, r 6.0, r 6.08,
r 9.0**: the ball stud's shank, the ball, the cavity at `#ball / 2 + #fit`, and the collar's
outside. **There is no face at r 5.0.** That face is what
[9p1's C1](../../2026-08-25-draft9p1/c/c1-readback.md) found bounding the cut where it ran past the
point at which the cavity had narrowed inside the slit profile, and it is the signature of a blind
pocket. Its absence is A1's claim, measured.

The slit's own faces read as four sets of three:

| face | where | how many | area each |
| --- | --- | --- | --- |
| the slit walls | x or y ±0.8000 | 8 | 15.5134 |
| the slit floors | z −3.0000 | 4 | 5.9521 |

The walls at ±0.8000 are `#slit_w` 1.6 across, and the floors are all at **z −3.0000**, which is
`#ball / 4` below the ball's center.

**The cavity is still outside the profile at the floor**, which is what makes the bottom of the cut
a slot bottom rather than a pocket bottom. The cavity's radius there is
`√((#ball / 2 + #fit)² − (#ball / 4)²)`: **5.2883** at the built fit and **5.1962** at a fit of
zero, against a profile inner edge of 5.0. The tighter margin, 0.1962, is the one that has to hold,
and it holds at the worst case rather than at the design case.

## The socket's other faces

| face | where | area |
| --- | --- | --- |
| the root | z −9.0000 | 254.4690 |
| the mouth, in four pieces | z +1.9465 | 4 × 32.3649, **129.4596** |
| the collar's outside | cylinder r 9.0000 | 587.3098 |
| the cavity | sphere r 6.0800 on the ball's center | 273.7633 |
| the ball | sphere r 6.0000 on the same center | 422.0850 |
| the shank | cylinder r 3.0000 | 90.5504 |

The mouth is in four pieces because the four slits cross it. Its 129.4596 is the annulus between
r 9.0 and the cavity's 5.7600 at that height, 150.2416, less the four slits at 1.6 × 3.2400 each.

**The gripper carries the same socket, face for face.** Its own `bodydetails` repeats the mouth's
4 × 32.3649, the cavity's 273.7633 and every one of the twelve slit faces at the same values. What
it does not repeat is the root's 254.4690: in the gripper the collar stands on the clip and the two
merge, so the disc is interior and only the four corners around it are surface.

**The thinnest wall is 2.9200**, `#collar` 9.0 over a cavity of `#ball / 2 + #fit` 6.08, unchanged
from 9p1 because neither number moved.

## A3 — the clip's top is flat and square

`Gripper` measures **18.0000 across X and 18.0000 across Y**, from z −24.0000 to z +1.9465.

| face | where | how many | area each |
| --- | --- | --- | --- |
| the platform | z −9.0000, in corner pieces | 4 | 17.3827 |
| the chamfers | 45°, through z −15.7000 | 2 | 101.8234 |
| the sides at full width | y ±9.0000, centered z −6.8500 | 2 | 84.6000 |
| the sides across the clip | x ±9.0000 | 2 | 175.1082 |
| the mouth's upper lip | z −17.7000 | 2 | 71.7098 and 3.0952 |
| the mouth's lower lip | z −20.3000 | 1 | 68.6146 |
| the clip's crown | cylinder r 5.0000 | 1 | 282.7433 |
| the finger bore | cylinder r 1.6500 | 1 | 132.7136 |

**The platform is four faces and not one**, which the plan's Phase C did not expect. It is flat and
it is square and it measures 18 both ways, and the Ø18 collar standing on it is inscribed tangent
on all four sides, so what is left uncovered is four corners: 324 − 254.4690 = 69.5310 against the
4 × 17.3827 = 69.5308 measured. One face would mean a collar narrower than its platform, which is
the reference document's proportion and not this robot's.

**The run at full width is 4.7000.** Each side face is 84.6000 over 18, from the platform at
z −9.0000 down to the top of the chamfer at z −13.7000, and A3 predicted 4.7000 once A2 set
`#collar` to 9.

**The mouth is still 2.6000 open**, its lips at z −17.7000 and z −20.3000, and the crown's cylinder
survives whole at r 5.0000.

## The assembly

| | |
| --- | --- |
| bounding box | x −61.5509 … 61.5509, y −64.0000 … 32.0000, z −178.0000 … 139.0000 |
| standing height | **317.0000** |
| instances | 14 |
| mate features | 13 |

| station | x | z |
| --- | --- | --- |
| the neck | 0 | +103.0000 |
| the shoulders | ±49.5509 | +19.2355 |
| the elbows | ±49.5509 | −28.7645 |
| the wrists | ±49.5509 | −76.7645 |
| the hips | ±24.0000 | −58.0000 |
| the knees | ±24.0000 | −106.0000 |
| the ankles | ±24.0000 | −154.0000 |

Hips, knees and ankles step by 48, which is `#limbCenter`, and the sole is `#foot_h` below the
ankle at −178.

**A4 — the feet are at x ±24 with their inner edges at 0.** `Foot` is 48.0000 across its own X,
centered on its origin, and each instance sits at x ±24.0000 at identity rotation, so the two soles
meet at x 0 and neither crosses it. The sheets now draw the same, and no model edit was needed.
