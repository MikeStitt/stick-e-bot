# B4 — the gripper's platform becomes the slab's own width

A3's three edits, made in `clip profile` and the feature tree above it. The three body-top features
are deleted, the slab is `#collarR` each side of the clip's axis instead of `#clipR`, and a 45°
chamfer carries that width down onto the mouth's upper lip. The gripper goes from ten features to
seven and gains no feature at all.

## The three body-top features are gone

Deleted bottom up, each by right-click on its tree row and **Delete**, so that no feature was ever
left referencing a deleted one:

| feature | what it did |
| --- | --- |
| `trim the body top` | removed the ring around the disc, `#collarR - #clipR` deep |
| `round the body top` | added the inner disc to the same depth |
| `body top outline` | drew the two circles, `2 * #collarR` and `4 * #collarR` |

What is left is `copy socket`, `clip profile`, `clip body`, `plane to cut top of clip`,
`remove top of clip`, `combine parts` and `mate to robot` — the reference's own construction, doing
the work A3 said it would keep doing.

## The slab was dimensioned on one side and constrained on the other

A3 read the sketch as having one dimension holding the slab **each side** of the axis. It has one
dimension holding the **left** side, and the right side is held by a **tangent** between the right
edge and the clip circle. A vertical line tangent to a circle of radius `#clipR` sits at `#clipR`,
so the two sides agreed at 5 and the asymmetry never showed.

Retyping the dimension moved the left edge to 9 and left the right edge at 5. Three edits made the
slab 18 across:

| what | before | after |
| --- | --- | --- |
| the slab, left of the axis | `#clipR` | **`#collarR`** |
| the right edge to the clip circle | tangent | **deleted** |
| the slab, across | — | **`2 * #collarR`** |

Deleting the tangent left the right edge under-defined by exactly one degree of freedom, and the
width dimension took it back. The sketch ends fully defined.

## The chamfers are Onshape's own sketch chamfer

Onshape carries **Chamfer** beside **Fillet** in the sketch toolbar, and it takes an expression for
each leg. Both legs of both chamfers are `#collarR - #clipR`, which is 4, so each chamfer is at 45°
without an angle being typed anywhere. The tool trims the corner and writes the two legs as
construction lines, so the corners at `#clipR` that A3 wanted are made by the chamfer rather than
found in the sketch.

`clip profile` after the edits, in sketch coordinates where y is the model's z:

| entity | from | to |
| --- | --- | --- |
| the top of the slab | −9.0000, 0.0000 | 9.0000, 0.0000 |
| the left edge | −9.0000, 0.0000 | −9.0000, −13.7000 |
| the left chamfer | −9.0000, −13.7000 | −5.0000, −17.7000 |
| the mouth's upper lip | −5.0000, −17.7000 | −1.0161, −17.7000 |
| the mouth's lower lip | −4.8280, −20.3000 | −1.0161, −20.3000 |
| the right edge | 9.0000, 0.0000 | 9.0000, −13.7000 |
| the right chamfer | 9.0000, −13.7000 | 5.0000, −17.7000 |
| what is left of the right lip | 4.8280, −17.7000 | 5.0000, −17.7000 |

The clip circle is r 5.0000 and the bore r 1.6500, both on the axis at 0.0000, −19.0000, and
neither was touched.

## What the part measures

Read from `bodydetails` and `boundingboxes` after the sketch was accepted. The gripper's bounding
box is **18.0000 across X, 18.0000 across Y** and 25.9465 tall, from z −24.0000 to z +1.9465.

| face | where | area |
| --- | --- | --- |
| the platform, in four corner pieces | z −9.0000 | 4 × 17.4, **69.6** |
| each chamfer | 45°, through z −15.7000 | 101.8 |
| each side of the slab at full width | y ±9.0000, centered z −6.8500 | 84.6 |
| the mouth's upper lip | z −17.7000 | 71.7 and 3.1 |
| the mouth's lower lip | z −20.3000 | 68.6 |
| the clip's crown | r 5.0000 on the axis at z −19.0000 | 282.7 |

**The platform is four pieces because the collar is tangent on all four sides.** An 18 × 18 square
with a Ø18 circle inscribed in it touches at four points and leaves four corners, 324 − 254.4690 =
69.5310 of them, against the 69.6 measured. That is A3's relationship, reached by dimension.

**The run at full 18 is 4.7000.** Each side face is 84.6 across 18, so it is 4.7000 tall, from the
cut plane at z −9.0000 down to the top of the chamfer at z −13.7000. A3 predicted 4.7000 after A2
and that is what it measures.

**The mouth is still `#mouth`.** The upper lip is at z −17.7000 and the lower at z −20.3000, 2.6000
apart, and the crown's cylinder survives whole because the chamfer's nearest approach to the axis is
5.1662 against a crown radius of 5.

## Found while doing it

- **A dropped websocket closes the sketch and keeps the edit.** Onshape put up *"Onshape is not
  connected. Your document is saved. Click here to reconnect."* partway through, and the dimension
  typed before it survived. Clicking the link restores the session; nothing had to be retyped.
- **`n` looks normal to the plane from whichever side the camera is on.** Pressing it after a
  reconnect gave the mirrored view, with the nav cube reading *Left* instead of *Right*. Pressing it
  again flips back, and checking the cube is cheaper than working out which way the picture reads.
- **`sketches?includeGeometry=true` answers while `features` is spent**, and it returns the sketch's
  geometry but not its constraints. It also returns the last computed state, so it shows nothing
  while the sketch is open in the editor.
