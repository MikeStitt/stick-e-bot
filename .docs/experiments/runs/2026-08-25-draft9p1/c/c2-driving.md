# C2 — `#limbCenter` and `#fit` driven, and put back

The readback in [`c1-readback.md`](c1-readback.md) shows the model agrees with the source at one
size. This shows it is driven: two variables were typed to new values in `robot sizes`, the whole
model was measured over REST after each change, and both were typed back. **Both round trips came
back exact — ten parts of ten, to the fourth decimal.**

The table as Onshape holds it, read from `/api/variables/…/variables` rather than off the screen:

| variable | expression |
| --- | --- |
| `#torsoH` | `96 mm` |
| `#torsoW` | `72 mm` |
| `#torsoD` | `48 mm` |
| `#limbCenter` | `48 mm` |
| `#ball` | `#torsoH / 8` |
| `#limbD` | `#torsoH / 4` |
| `#wall` | `#torsoH / 32` |
| `#stand` | `#ball * 5 / 6` |
| `#collar` | `11 mm` |
| `#fit` | `0.08 mm` |
| `#grip` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball) ^ 2)` |

Four of the eleven are typed numbers and seven are expressions. `#fit` is typed because A2 made it a
printing clearance, which does not scale with anything.

## `#limbCenter` 48 → 60 → 48

At 60 mm, **exactly two parts moved, and each by exactly 12:**

| part | at 48 | at 60 |
| --- | --- | --- |
| `u limb` | z −60.000 … 1.9465 | z −72.000 … 1.9465 |
| `l limb` | z −54.000 … 12.000 | z −66.000 … 12.000 |

The other eight parts — torso, head, ball stud, socket, foot, blade, fork, gripper — did not move
by any amount at all. **That is what A1 bought.** `#limbSeg` was a rod length, so changing it
changed a rod and left the joint wherever the rod ended. `#limbCenter` is the distance from one
joint to the next, so changing it moves the far joint and the rod follows. Nothing else in the
robot has an opinion about it.

Both limbs grew from the joint end and not the socket end: `u limb`'s socket stayed at 1.9465 and
its fork went from −60 to −72; `l limb`'s blade stayed at 12 and its ball went from −54 to −66.

Typed back to 48 mm, every one of the ten parts returned to the box C1 measured, with no residue.

### The assembly did not follow, and that is B9's doing

The assembly's bounding box read 317.0535 at `#limbCenter` = 60, which is the same height as at 48.
B9 re-pointed all fourteen instances at the versions `parts built` and `ankle centered`, so the
assembly is looking at frozen geometry and a workspace edit does not reach it. The assembly follows
again the moment its references are updated, which is what the **Update all references to latest
versions** button on the assembly toolbar is for.

This is worth knowing before it surprises somebody: **a version-linked assembly is deliberately deaf
to the variable table.** It is the right trade for a robot a class is going to open — nobody's build
changes under them — but it means the drive has to be measured in the Part Studios, which is where
it was measured.

## `#fit` 0.08 → 1 → 0 → 0.08

`#fit` was driven to twelve and a half times its design value and then to nothing at all. **The
socket is 11.000 mm tall at every one of the three.**

| `#fit` | `#grip` measured | socket top | socket bottom | socket height |
| --- | --- | --- | --- | --- |
| 0 mm | 1.6800 | 1.6800 | −9.3200 | **11.0000** |
| 0.08 mm | 1.9465 | 1.9465 | −9.0535 | **11.0000** |
| 1 mm | 3.9777 | 3.9777 | −7.0223 | **11.0000** |

Each `#grip` is its formula to the fourth decimal: √(6.00² − 5.76²) = 1.6800, √(6.08² − 5.76²) =
1.9465, √(7.00² − 5.76²) = 3.9777. **`#collar` owns the socket's height and `#fit` owns only where
the ball's center sits inside it.** That is the whole of A2's claim, and this is the measurement
that carries it.

What moved at `#fit` = 1 mm, and what did not:

| part | what moved |
| --- | --- |
| `Socket body` | both ends, by 2.0312 — the whole collar hangs off the ball center |
| `Foot`, `Gripper`, `u limb` | the top only, by 2.0312 — the collar's rim rose, the sole and the joint stayed |
| `torso`, `head`, `blade`, `fork`, `l limb` | nothing |

The four parts that did not move are the four that carry a **ball** rather than a socket, and the
head, whose collar is sunk inside it and never reaches the bounding box. **The ball never changes
size when the fit changes** — `#ball` is 12 and the ball measures r 6.0000 at every fit. A2 called
the ball the free variable and the fit a clearance on the socket alone, and the parts sort
themselves into exactly those two groups.

Nothing about a joint station moved either. The feet stayed on the floor at −24, the fork stayed at
−60, and the gripper stayed at −24. **A fit change is invisible to the robot's dimensions**, which
is why a class can be told to reprint one socket at a different clearance without reprinting
anything else.

Typed back to 0.08 mm, all ten parts returned to the C1 boxes exactly.

## How it was done

- `robot sizes` opened at its own element URL, the value cell clicked, ⌘A, the number typed, Enter,
  and twenty seconds for the regeneration.
- The table read back over REST after every change, so the value under test is the one Onshape
  holds and not the one that was typed.
- Every part's bounding box, the socket's face radii, and the assembly's bounding box read after
  every change, and compared offline against `c1-raw.json`.
- The scripts are in [`scripts/`](scripts): `c2_vars.py` reads the table, `c2_drive.py` types and
  measures, and `c2_diff.py` says what moved.
