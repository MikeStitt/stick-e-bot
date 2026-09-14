# C2 — `#fit` and `#torsoH` driven, and put back

[`c1-readback.md`](c1-readback.md) shows the model agrees with the source at one size. This shows it
is driven. Two variables were typed into `robot sizes`, the whole model was measured over REST after
each change, and both were typed back. **Both round trips came back exact, ten parts of ten, to the
fourth decimal.**

The scripts are [`scripts/c2_open.py`](scripts/c2_open.py), which reports where the rows sit on
screen, and [`scripts/c2_drive.py`](scripts/c2_drive.py), which types one value, waits for the
regeneration and then measures. Each run writes its own `c2-<tag>.json`, and every number below is
read out of those files rather than off the screen.

## The assembly is live this time, and that had to be shown first

9p1's [`c2-driving.md`](../../2026-08-25-draft9p1/c/c2-driving.md) could not measure the robot's
height under a drive, because B9 had pinned all fourteen instances to versions and the assembly was
deaf to the table. B5 moved this document's instances onto its own workspace, so the drive should
now reach the assembly, and a constant height would otherwise prove nothing at all: a deaf assembly
holds its height too.

**`#torsoH` 96 → 120 is the discriminator, and the assembly followed it.** The standing height went
to **346.7500** and every station moved:

| station | at 96 | at 120 |
| --- | --- | --- |
| the neck | +103.0000 | +117.2500 |
| the shoulders | ±49.5509, +19.2355 | ±51.6356, +26.0409 |
| the hips | ±24.0000, −58.0000 | ±21.0000, −70.0000 |
| the ankles | ±24.0000, −154.0000 | ±21.0000, −163.5000 |

So the assembly answers the table, and the `#fit` result below is a measurement rather than a
silence.

## `#fit` 0.08 → 1 → 0 → 0.08

`#fit` was driven to twelve and a half times its design value and then to nothing at all.

| | `#fit` 0 | `#fit` 0.08 | `#fit` 1 |
| --- | --- | --- | --- |
| `#grip` measured | 1.6800 | 1.9465 | 3.9777 |
| the socket's mouth, z | 1.6800 | 1.9465 | 3.9777 |
| **the socket's root, z** | **−9.0000** | **−9.0000** | **−9.0000** |
| the socket, mouth to root | 10.6800 | 10.9465 | 12.9777 |
| **the slit's floor, z** | **−3.0000** | **−3.0000** | **−3.0000** |
| the tabs' free length | 4.6800 | 4.9465 | 6.9777 |
| **the standing height** | **317.0000** | **317.0000** | **317.0000** |

Each `#grip` is its formula to the fourth decimal: √(6.00² − 5.76²) = 1.6800,
√(6.08² − 5.76²) = 1.9465, √(7.00² − 5.76²) = 3.9777.

**Not one joint station moved at any of the three values.** The neck stayed at +103.0000, the hips
at ±24.0000 and −58.0000, the ankles at −154.0000, the shoulders, elbows, knees and wrists all
likewise, and the assembly's box stayed x ±61.5509, y −64.0000 … 32.0000, z −178.0000 … 139.0000 at
every value. The height is 317.0000 by construction: the sole is `#foot_h` below an ankle that does
not move, and the head's crown is +36.0000 above a neck that does not move.

### What A2 bought, against 9p1's before picture

9p1's table is the contrast, and the row to read is the socket's root:

| | 9p1 root, z | 9p1 socket height | 9p1p1 root, z | 9p1p1 socket height |
| --- | --- | --- | --- | --- |
| `#fit` 0 | −9.3200 | 11.0000 | −9.0000 | 10.6800 |
| `#fit` 0.08 | −9.0535 | 11.0000 | −9.0000 | 10.9465 |
| `#fit` 1 | −7.0223 | 11.0000 | −9.0000 | 12.9777 |

**The invariant swapped ends.** In 9p1 the socket kept one height and its root travelled 2.2977 as
the fit went from nothing to 1; here the root is pinned and the socket's height travels instead.
That is exactly what A2 asked for, and the two consequences it was asked for are both measured:

- **The slit's floor is at z −3.0000 at every fit.** In 9p1 the floor was `#collar − #wall` below a
  moving mouth, so it sat at −6.3200, −6.0535 and −4.0223. A depth that moves with the printer's
  clearance is a depth nobody can draw. Here it is `#ball / 4` below the ball's center and it is the
  same number at every fit.
- **Three `#grip` terms came out of two tabs.** B3 removed the compensations in `foot` and `u limb`
  that existed only to cancel a moving root. In 9p1 the sole and the fork held still *because* those
  terms cancelled the travel; here they hold still because nothing travels.

### The clause of A2 that does not hold, stated as measured

The plan's Phase C says A2's claim is that "the standing height, every joint station and every
part's overall size hold while only the mouth moves." **The first two hold and the third does not.**
The socketed parts still change their overall size with the fit, by the same 2.0312 that 9p1
measured:

| part | `#fit` 0 | `#fit` 0.08 | `#fit` 1 | what moved |
| --- | --- | --- | --- | --- |
| `Foot` | −24.0000 … 1.6800 | −24.0000 … 1.9465 | −24.0000 … 3.9777 | the top |
| `Gripper` | −24.0000 … 1.6800 | −24.0000 … 1.9465 | −24.0000 … 3.9777 | the top |
| `u limb` | −60.0000 … 1.6800 | −60.0000 … 1.9465 | −60.0000 … 3.9777 | the top |
| `head` | −46.6800 … 36.0000 | −46.9465 … 36.0000 | −48.9777 … 36.0000 | the bottom |
| `Socket body` | −9.0000 … 1.6800 | −9.0000 … 1.9465 | −9.0000 … 3.9777 | the top |
| `torso`, `blade`, `fork`, `l limb`, `Ball stud` | | | | nothing |

A socket's mouth is part of the part it belongs to, so a mouth that moves is an overall size that
moves; the two cannot both hold, and the plan's sentence asked for both. What matters for a robot
that has to stand up is the station, and the station is at the end where the mouth is not. **The
five parts that do not move are exactly the five with no socket on them.** The ball never changes
size when the fit changes: `#ball` is 12 and the ball measures r 6.0000 at every value.

`head` is the row that moves the other way, because its socket is the only one that points down. Its
faces read root at local z −36.0000, ball center at −45.0000, slit floors at −42.0000 and mouth at
−46.9465, so the root is flush with the head's underside and the collar hangs below it. The crown at
+36.0000 is fixed and the mouth is what travels. **[`../b/b3-consumers.md`](../b/b3-consumers.md)
had these two labels the wrong way round**, calling +67.0000 the mouth and +56.0535 the root; they
are the root and the mouth, and the table has been corrected. The measurement either side of it was
right, and correcting the labels does not move a number.

### One more thing the fit does, which is worth knowing before printing

The slit's floor is the strip between the cavity and the collar, so the fit eats it from the inside.
The cavity at z −3.0000 is `√((#ball / 2 + #fit)² − (#ball / 4)²)`, and the four floors measure:

| `#fit` | the cavity at the floor | each floor's area |
| --- | --- | --- |
| 0 | 5.1962 | 6.1001 |
| 0.08 | 5.2884 | 5.9521 |
| 1 | 6.3246 | 4.2888 |

Each is 1.6 across, so the strip is about 1.6 × (9 − the cavity). It closes when the cavity reaches
the collar's r 9.0000, which is a `#fit` of 3.4868; that is more than forty times the design
clearance and no printer will ask for it. **At a fit of exactly zero the cavity and the ball are
both r 6.0, so `bodydetails` reports one sphere where there are usually two.** That is a coincidence
of the number and not a missing face.

## `#torsoH` 96 → 120 → 96

The second drive proves `#collar` is genuinely derived now rather than typed at a value that
happened to be right.

| | at 96 | at 120 |
| --- | --- | --- |
| `#ball` | 12.0000 | 15.0000 |
| `#wall` | 3.0000 | 3.7500 |
| `#collar`, as built | 9.0000 | **11.2500** |
| the socket's root, z | −9.0000 | **−11.2500** |
| the slit's floor, z | −3.0000 | **−3.7500** |
| the collar's outside | r 9.0000 | r 11.2500 |
| the cavity | r 6.0800 | r 7.5800 |
| `Ball stud`'s underside, z | −6.0000 | −7.5000 |
| `torso`, z | ±64.0000 | ±77.5000 |
| the standing height | 317.0000 | 346.7500 |

`#collar` = `#ball / 2 + #wall` = 15 / 2 + 120 / 32 = **11.2500**, and the root sits at exactly
−11.2500 without anybody typing it. The slit's floor is `#ball / 4` = 3.7500 below the ball's center
at both sizes. The cavity is `#ball / 2 + #fit`, and `#fit` stays 0.08 through the change because it
is a printing clearance and does not scale; that is why the cavity goes to 7.58 and not to 7.6.

Typed back to 96, all ten parts returned to the boxes C1 measured and every station returned to its
own number, with no residue.

## How it was done

- `robot sizes` opened at its own element URL; the value cell clicked, ⌘A, the number typed, Enter,
  and twenty-five seconds for the regeneration.
- The table read back over REST after every change, so the value under test is the one Onshape
  holds and not the one that was typed.
- Every part's bounding box, the socket's faces, the assembly's bounding box and all fourteen
  instance transforms read after every change, and compared offline against
  [`c1-raw.json`](c1-raw.json).
- The `features` endpoint was not touched at any point. It was answering 429 with a `retry-after` of
  eighteen hours when this phase started, and everything above is available from `bodydetails`,
  `parts`, `boundingboxes`, `variables` and `assemblies`. See
  [`../../../../.parts/onshape.md`](../../../../.parts/onshape.md) § *Read what a refusal says
  before waiting on it*.
