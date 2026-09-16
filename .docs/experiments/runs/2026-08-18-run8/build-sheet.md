# Run 8 — the settlements, and the joint as numbers

The plan left four things to settle before the build. They are settled here, and the recipe below
is what gets built. Nothing in it was retyped from the page: it was read back out of
`run7p1-ball-and-socket` feature by feature, with every `#name` replaced by what it evaluates to.

## S-1 — the seed and the count

**One slot running outward from the origin, patterned 4 over 360°.**

Drawn with **Corner rectangle**, which brings its own horizontal and vertical constraints. Then a
**midpoint** constraint holding the inner short edge's middle on the origin, a **length**
dimension along it and **0.8** across it. That is four degrees of freedom killed by one constraint
and two dimensions, and the slot goes black.

The pattern's pivot is the origin — the spike saw the pivot square land there with no pick asked
for — so the four copies come out at 90° to each other and their inner ends meet in a small square
over the mouth of the hollow. The brief's rule that *the slit's inner end must sit inside the
mouth radius* is satisfied by construction: the inner end is the origin.

## S-2 — the outer end against the rim

**The slot is 5.0 mm long**, against a collar radius of 4.7 mm. The reason a reader can hold: the
slot has to run off the edge of the collar, so it is drawn a little longer than the collar's
radius rather than exactly to it. 4.7 would touch the rim at one point and leave 0.017 mm of
collar uncut across the slot's width; 5.0 leaves 0.3 mm of the slot hanging in the air, which cuts
nothing and is what makes the cut obviously complete.

## S-3 — the depth

**The model wins: the cut is 4.0 mm deep, downward from the collar's top face, and it leaves a
1.5 mm floor.** Read back from run 7p1: `relief slits` is a one-direction `BLIND` extrude,
`depth` 4 mm, `oppositeDirection` true. The collar runs from −4.15 to +1.35, so the cut runs +1.35
down to −2.65 and the floor is −4.15 to −2.65, which is 1.5 mm — one wall thickness, the ring that
pulls the four fingers closed again.

The brief's *"the slits are 5.5 mm deep, not 2.7 — it must run the collar's whole length, −4.150
to +1.350"* is therefore wrong and gets replaced. The failure it was written for is real: in run 1
the depth went **both ways** from the sketch plane, so half of it stood in the air above the face
and only half of it cut. The tell for that failure, written against this design:

> Measure the slit's floor. From the bottom of the cut to the bottom of the collar must be
> 1.5 mm. If it comes out 3.5 mm, the extrude went both ways from the face and only 2 mm of it
> went into the collar.

Only a print settles whether a 1.5 mm floor lets the mouth open far enough to swallow the ball.
That is a question for the first print, not for this run.

## S-4 — the numbers that replace the variables

| typed where | value | where the number comes from |
| --- | --- | --- |
| arc radius, `stud profile` | 3 | half the ball |
| top line length, `stud profile` | 1.5 | half the stalk |
| origin to top line, `stud profile` | 5 | how far the stud's top face stands above the ball's center |
| circle diameter, `collar profile` | 9.4 | the ball, plus the 0.2 gap each side, plus the 1.5 wall each side |
| depth, `collar blank` | 1.35 | how far the collar reaches up past the ball's center |
| second end position, `collar blank` | 4.15 | the rest of the collar's 5.5 height |
| offset distance, `cavity from ball` | 0.2 | the gap the ball turns in |
| slot length, `slit profile` | 5 | a little past the collar's 4.7 radius — S-2 |
| slot width, `slit profile` | 0.8 | how wide a relief slit is |
| depth, `relief slits` | 4 | the collar's 5.5 less one 1.5 wall — S-3 |

Two numbers the page used to hold as expressions now vanish rather than become numbers: `#collar`
5.5 and `#grip` 1.35 were only ever typed as `#collar - #grip`, which is 4.15.

## The recipe, as read back from run 7p1

Document `run8-ball-and-socket` on 9223. Sketch coordinates below are in mm.

| # | feature | what it is |
| --- | --- | --- |
| 1 | `stud profile` | sketch on **Front**: arc centered on the origin, radius 3, from below the origin round to the upper right; three lines closing it — up from the arc's top end at x = 1.5, left along y = 5, down the axis at x = 0. Dimensions: arc radius **3**, top line length **1.5**, origin to top line **5** |
| 2 | `revolve stud` | revolve, **New**, the region, axis is the sketch's vertical line, **Full revolve**. Part renamed `Ball stud` |
| 3 | `collar profile` | sketch on **Top**: circle on the origin, diameter **9.4** |
| 4 | `collar blank` | extrude, **New**, depth **1.35**, second end position **4.15**. Part renamed `Socket body` |
| 5 | `cavity from ball` | boolean **Subtract**, tools `Ball stud`, targets `Socket body`, **Offset** and **Offset all** on, offset distance **0.2**, **Keep tools** on |
| 6 | `slit profile` | sketch on the collar's **top face**: corner rectangle running outward from the origin, inner edge's midpoint on the origin, length **5**, width **0.8**; four sides selected, **Circular pattern**, count **4** |
| 7 | `relief slits` | extrude, **Remove**, depth **4**, running **down** into the collar, merge scope `Socket body` |

`Features (7)` under *Default geometry*, and two named parts. The tree the page shows is ten rows
shorter than run 7p1's `Features (18)`.

## S-5 — the pattern's copies stay blue

Found during the build, not before it. `slit profile` reports *"slit profile [Sketch] is not fully
defined"*. The seed slot is black: its four sides carry the midpoint constraint, the length and
the width, and its four degrees of freedom are gone. The three copies are blue. A sketch circular
pattern drives its copies through one `CIRCULAR_PATTERN` constraint, and Onshape does not count
that constraint as defining them.

Nothing about the geometry is loose — the copies sit at 90° to each other and rebuild there every
time — so the sketch is used as it is. What changes is what the page may promise. Run 7p1's two
crossed bars went fully defined and the page said so; this sketch cannot, and the frame that used
to be called `bs-36-two-crossing-bars-fully-defined` has no successor with that name. The reader's
check becomes what they can see: **the slot you drew turns black, the three copies stay blue, and
the sketch closes clean.**

## What the acceptance checks become

Measured, not inferred, when the build is done:

| check | expected |
| --- | --- |
| parts | 2 — `Ball stud`, `Socket body` |
| ball diameter | 6.000 |
| mouth diameter | 5.803 — √(3.2² − 1.35²) doubled |
| cavity radius | 3.200 |
| `Ball stud` volume | 128.6210 mm³ — the brief said 935.2249, which was the Ø12 ball |
| cavity volume | 109.48 mm³ |
| slits | 4, each 0.8 wide |
| slit floor | 1.5 — S-3 |
| sketch state | `stud profile` and `collar profile` fully defined; `slit profile` black on the seed, blue on the three copies — S-5 |
| `slit profile` pattern | one `CIRCULAR_PATTERN` constraint, `patternc1` = 4, four seed entities |
