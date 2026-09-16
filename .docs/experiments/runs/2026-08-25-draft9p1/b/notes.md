# Phase B build notes — stickbot-draft9p1

The ids are in [`../b0-copy.md`](../b0-copy.md). This file records what each row edited, what it
measured, and where a dialog did not behave as
[`../../../../onshape-gui-howto.md`](../../../../onshape-gui-howto.md) says.

## B1 — `robot sizes`

The studio went from four rows to eleven. The four it had are unchanged apart from the rename.

| | expression | mm |
| --- | --- | --- |
| `#torsoH` | `96 mm` | 96 |
| `#torsoW` | `72 mm` | 72 |
| `#torsoD` | `48 mm` | 48 |
| `#limbCenter` | `48 mm` | 48 |
| `#ball` | `#torsoH / 8` | 12 |
| `#limbD` | `#torsoH / 4` | 24 |
| `#wall` | `#torsoH / 32` | 3 |
| `#stand` | `#ball * 5 / 6` | 10 |
| `#collar` | `11 mm` | 11 |
| `#fit` | `0.08 mm` | 0.08 |
| `#grip` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball) ^ 2)` | 1.94648 |

Read back over REST as expressions rather than as the numbers the cells display, because a cell
that shows 12 mm cannot tell you whether it holds `#torsoH / 8` or a typed 12.

**Renaming a variable in a Variable Studio carries its readers with it.** The plan's B1 row expects
the opposite — *a variable renamed out from under an expression fails the feature, not the table* —
so this was checked rather than assumed. `#limbSeg` was read in one place, the `limb` extrude's
depth in `u limb` and in `l limb`. Both read `#limbCenter` immediately after the rename, with no
edit and no error, and both parts still build. The check is still worth doing; the failure it
guards against is not the one that happens.

**The rows are typed in dependency order.** `#ball` before `#stand` and `#grip`, because both are
expressions on it. Whether a Variable Studio needs that order was not tested — typing them in an
order that cannot fail is cheaper than finding out.

**A Value cell took two double clicks on the first row and one afterwards**, which is what
draft9p0's notes record and is a refinement of the how-to's *two double clicks from cold*: the
table is cold, not the row. The empty placeholder Name cell took a single click, as documented.

**The local declarations still shadow the studio.** `ball and socket` declares `#fit = 0.8 mm` and
`#grip = 3.6 mm` in its own tab, so the joint is still built at draft9p0's numbers until B2 deletes
them. Every tab regenerated after B1 and the eight bounding boxes are unchanged, which is the
evidence that B1 moved no geometry.

## B2 — `ball and socket`

The tab went from nineteen features to fourteen. Nothing was added and no dimension was retyped.

**The A2 rearrangement needed no geometry edit.** A2 asks that the socket's height stop depending
on `#grip` so the ball can become the free variable.
[`../../../build-briefs/ball-and-socket.md`](../../../build-briefs/ball-and-socket.md) already has
`collar blank` extruding `#grip` one way and `#collar - #grip` the other, and the built feature
already read those two expressions, so the total is `#collar` whatever `#grip` does. The socket was
built to A2 before A2 was written. What held the tab at draft9p0's numbers was five local
declarations shadowing the studio, and deleting them was the whole edit.

| deleted from the tab | it now reads | mm |
| --- | --- | --- |
| `#ball` | `robot sizes` | 12 |
| `#collar` | `robot sizes` | 11 |
| `#wall` | `robot sizes` | 3 |
| `#fit` | `robot sizes` | 0.08 |
| `#grip` | `robot sizes` | 1.94648 |

Five stay in the tab, which is what A13 asks for — `#stalk`, `#slit`, `#stud_len`, `#slit_in` and
`#slit_out` are read nowhere else.

**What the joint measures afterwards**, against the brief's acceptance numbers:

| | brief | measured |
| --- | --- | --- |
| ball radius | 6 | 6.0000 |
| cavity radius | `#ball / 2 + #fit` = 6.08 | 6.0800 |
| collar diameter | `2 × #collarR` = 18 | 18.0000 |
| mouth diameter | `0.96 × #ball` = 11.52 | 11.5200, in four arcs |
| mouth height | `#grip` = 1.9465 | z 1.9465 |
| collar bottom | `#grip - #collar` = −9.0535 | z −9.0535 |
| slit floor | `#collar - #wall` below the top = −6.0535 | z −6.0535 |
| thinnest wall | `#collarR - cavity` = 2.92 | 2.92 |
| `Ball stud` volume | 1028.968 mm³ | 1028.968 mm³ |

The volume is the brief's own arithmetic and it lands exactly, which is the evidence that the merge
scope is right — a stud merged into the socket, or a socket merged into the stud, would not.

### The slit sketch goes black

U3 asks that the slit profile's center of rotation be coincident with the origin. The brief's route
is to drag from the origin, which cannot move, so what comes away under the pointer is the pattern's
center, then constrain the two together. The drag worked and put the center 7.049 mm out.

**The origin is not where the sketch draws it.** The first Coincident attempt selected only one
point and the sketch stayed blue. Hovering pixel by pixel found why: the click had been landing on
the ball's spherical face, which sits in front of the origin along the view direction. Hiding
`Ball stud` exposed it, and a second hover sweep read `Point: 0.00000 / 0.00000 / 0.00000` at a
pixel fifty down from the one the drag had started at.

**A pixel count of blue ink is not enough to tell a selection from a miss.** Two attempts were read
as failures on the ink count alone when the real fault was elsewhere — the second was a click at
the coincident item's coordinates without opening the flyout first, which landed on empty canvas
and cleared the selection. Onshape says what it has selected: with one entity the corner panel
reads `Point:`, with two it reads `Min dist:`. Reading that panel before applying the constraint is
what turned the guessing into a check.

Blue ink measured 2842 px before the constraint and **0 px after**, and `i` applied it. Both part
volumes are unchanged across the constraint, which is the evidence that pinning the pattern center
moved no geometry.

## B3 — `hinge`

A4 asks that every protrusion be on the blade and every hole in the fork, so that nothing on the
fork stands proud of the face the blade's axle has to cross during mating. Half of that was already
true: the axle is on the blade and the bore goes through the ear, and
[`../../../build-briefs/hinge.md`](../../../build-briefs/hinge.md) records that as settled. The detents
were the other way round, and B3 turned them over.

**The swap is eight edits and no new features.** The blade's four detent features and the fork's
four are a mirror image of each other, so each group became the other group in place. The two
circular patterns are `FEATURE` patterns keyed on feature id, so neither had to be touched or
re-picked.

| was | is | what changed |
| --- | --- | --- |
| `click lock valley sketch` | `blade bump outline` | Ø `#valley_d` → Ø `#bump_d` |
| `click lock valley` | `blade bump` | Remove → Add, `#valley_deep` → `#tooth_proud`, direction out |
| `round valley rim` | `dome blade bump` | rim edge → crown edge, `#rim_break` → `#bump_d / 2` |
| `24 valleys` | `24 blade bumps` | name only |
| `click bump outline` | `ear valley outline` | Ø `#bump_d` → Ø `#valley_d` |
| `click bump` | `ear valley` | Add → Remove, `#tooth_proud` → `#valley_deep`, direction in |
| `dome click bump` | `round ear valley rim` | crown face → rim edge, `#bump_d / 2` → `#rim_break` |
| `24 bumps` | `24 ear valleys` | name only |

### Where every surface ended up

Measured off `bodydetails` as planes normal to the hinge's thickness axis, and as sphere centers:

| | brief | measured |
| --- | --- | --- |
| blade faces | ±5.00 | ±5.0000 |
| dome centers | crest 1.2 proud, cap r 0.8, so ±5.40 | ±5.4000, 24 a side |
| crest tips | ±6.20 | ±6.20 |
| axle faces | 1.6 proud of the blade | ±6.6000 |
| ear inner faces | ±5.60 | ±5.6000 |
| valley floors | ±6.50 | ±6.5000, 24 a side |
| valley bore | Ø `#valley_d` | r 1.0000, 48 |
| axle bore | Ø `#pocket_d` | r 2.2000 |
| round ends | r 12 on both members | 12.0000 on both |

From those: **0.60 of interference per side** at the land (6.20 against 5.60) and **0.30 of
clearance** at the floor (6.50 against 6.20), which are the brief's two numbers exactly.

**The dome is a real hemisphere, and the area proves it.** A cap of r 0.8 has a curved area of
2πr² = 4.021 mm². Each of the 48 sphere faces measures 4.021 mm².

### The snap direction, re-derived against the new arrangement

**The ears still open, and they still open 1.0 mm.** The axle stands to ±6.60 and the ear's inner
face is at ±5.60, so the ears must spread 1.00 per side for the axle to reach the bore. The crests
ask for only 0.60. The larger number governs and it is the axle's, exactly as it was before the
swap, so no spring figure in the brief changes. The blade carries no slit, so the ears give all of
it.

**What the swap does change is which member carries the finer feature.** Pitch at r 9.60 is
2π × 9.60 / 24 = 2.5133. The bumps are Ø1.6 and leave 0.9133 of flat between neighbors; the valleys
are Ø2.0 and leave 0.5133. Those two numbers did not change, they swapped members — the 0.5133 land
is now on the ear. By the same trade the blade's rim improved: its bumps reach r 10.40 against an
r12 end, a **1.60 rim**, where the valleys it used to carry reached r 10.60 for **1.40**. The 1.40
rim is now the ear's.

### What the GUI did that the how-to does not say

- **The "Direction" checkbox in Extrude is not a flip.** It opens an *Extrude direction* field
  asking for a reference, and ticking it puts the feature into error until something is picked.
  The flip is the arrow button beside the end-condition dropdown, whose tooltip reads *Opposite
  direction*.
- **Onshape says which way an extrude is pointing, if you read the banner.** An Add pointing into
  its own body reports *Boolean resulted in no geometry change*; a Remove pointing away from the
  target reports *Selected tools and targets do not intersect*. Both cleared on the flip, which is
  a cheaper check than judging a 1.2 mm feature by eye at fit-to-screen zoom.
- **A fillet whose entity no longer exists does not always error.** When the blade's valley became
  a bump, the fillet on its rim silently re-resolved to the blade's whole outline edge and reported
  nothing. The fork's fillet, by contrast, said *did not regenerate properly … 1 missing selection*.
  Clearing the field and re-picking is the only safe move; a green tree is not evidence the
  selection is the one intended.
- **A face and an edge are one pixel apart at the wrong zoom.** Picking the valley's rim gave
  *Face of fork blank* until the pocket was zoomed to about a third of the canvas, after which the
  same click gave *Edge of ear valley*. The selection field names what was picked, so it is worth
  reading before setting the radius rather than after.
- **The feature list renders rows past the bottom of its own clip line.** A row found by its DOM
  rectangle can be one that nobody can see, and the double-click then lands in the Parts list. The
  list also coasts after a wheel scroll, so a coordinate has to be re-read after it settles.

## B4 — `body`

Four typed numbers became expressions and two locals went, and **the torso's volume is the same to
the last digit either side of it** — 343120.267 mm³ before and after. That is the point of the row:
nothing here is a shape change, it is six statements of what a number is for.

| | was | is | mm |
| --- | --- | --- | --- |
| `#hip_half` | `#torsoH / 4` | `#torsoW / 2 - #limbD / 2` | 24 |
| `#shoulder_drop` | `8 mm` | `#torsoH / 12` | 8 |
| `#shoulder_len` | `26 mm` | `#torsoH * 13 / 48` | 26 |
| `#boss_d` | `16 mm` | `#ball * 4 / 3` | 16 |
| `#ball` | `#torsoH / 8`, declared here | read from `robot sizes` | 12 |
| `#stand` | `10 mm`, declared here | read from `robot sizes` | 10 |

`#shoulder_half` stays `#torsoW / 2`, which [`../a7-hip-shoulder.md`](../a7-hip-shoulder.md) found
was already right. `#boss_len = #shoulder_len - #stand` needed no edit and now follows both.

**`#limbD` did not have to be declared in `body`.** A7 said it would have to be, because A7 was
written before A13 promoted `#limbD` to the Variable Studio. B1 put it there, so `#hip_half` reads
it from the studio and `body` declares nothing.

**Six of nine variables in this tab are now expressions and none of them changed a number.** That
is what makes the row impossible to verify by looking at the model, and why the volume was recorded
before the first edit rather than after the last.

**The plan's B4 row names `upper rounds`, which is a feature of the `head` tab.** It is B5's, and
that is where it is done.

## B5 — `head`

**The tab declared no variables at all.** Every number in it was typed, or reached past the head
into `#torsoH`. Twelve rows go in ahead of the first sketch, and
[`../a8-head-numbers.md`](../a8-head-numbers.md) is where each expression was settled.

| | expression | mm |
| --- | --- | --- |
| `#headW` | `#torsoW` | 72 |
| `#headD` | `#torsoD * 5 / 4` | 60 |
| `#eyeX` | `#headW / 6` | 12 |
| `#eyeUp` | `#headW / 9` | 8 |
| `#eyeRx` | `#headW / 9` | 8 |
| `#eyeRy` | `#headW / 18` | 4 |
| `#face` | `#headW / 24` | 3 |
| `#mouthW` | `#headW * 5 / 9` | 40 |
| `#mouthH` | `#headW * 5 / 36` | 10 |
| `#mouthDn` | `#headW * 13 / 72` | 13 |
| `#chamfer` | `#headW / 12` | 6 |
| `#round` | `#headW / 6` | 12 |

Eleven are A8's. `#round` is A9's, and the plan puts it in the B4 row because it names `upper
rounds` as a `body` feature. `upper rounds` is a fillet on the head, so the edit is here.

## What each number was before

| feature | field | was | is |
| --- | --- | --- | --- |
| `head profile` | RADIUS | `#torsoH * 3 / 8` | `#headW / 2` |
| `head profile` | LENGTH | `#torsoH * 3 / 8` | `#headW / 2` |
| `head body` | depth | `60 mm` | `#headD` |
| `upper rounds` | radius | `12 mm` | `#round` |
| `lower head chamfer` | width | `6 mm` | `#chamfer` |
| `eye` | depth | `33 mm` | `#headD / 2 + #face` |
| `mouth` | depth | `3 mm` | `#face` |
| `mouth` | startOffsetDistance | `30 mm` | `#headD / 2` |
| `mouth profile` | LENGTH | `30 mm` | `#mouthW - #mouthH` |
| `mouth profile` | DISTANCE | `18 mm` | `#mouthDn + #mouthH / 2` |
| `mouth profile` | DISTANCE | `15 mm` | `(#mouthW - #mouthH) / 2` |
| `mouth profile` | DIAMETER | `10 mm` | `#mouthH` |

**Every one of these evaluates to the number it replaced.** The head's width was already 36 mm of
radius; what changed is that it is half the head's own width rather than three eighths of the
torso's height. Nothing moved, and the dimension labels stayed on the same pixels across all four
sketch edits, which is how the edits were confirmed without re-fitting the view.

## The eye is the only shape change

draft9p0 drew a circle Ø20 centred 16 mm across and 16 mm up. It reached z 26 against a fillet that
starts at z 24, so it ran into the round.
[`../a3-eye-ellipse.md`](../a3-eye-ellipse.md) took the ellipse off the example stickbot instead.

| | was | is |
| --- | --- | --- |
| shape | circle | ellipse |
| across | 16 | `#eyeX` 12 |
| up | 16 | `#eyeUp` 8 |
| wide | Ø20 | `#eyeRx * 2` 16 |
| tall | Ø20 | `#eyeRy * 2` 8 |
| top reaches | 26 | 12 |

The sketch holds five constraints and is fully defined: HORIZONTAL on the major axis, which Onshape
infers from the draw order, then the two diameters and the two centre distances.

**The pupils were never in the model.** A8 decided against them and there was nothing to delete.

## Measured

`bodydetails` reads the eye twice, once per side, as an `extruded` wall and an elliptical crown:

| | measured | what it is |
| --- | --- | --- |
| crown centres | (±12, −33, 8) | `#eyeX` either side, `#face` proud of the face, `#eyeUp` up |
| crown area | 100.531 mm² | π × 8 × 4, the ellipse |
| wall area | 116.261 mm² | the ellipse's perimeter × `#face` |
| head extent | 72 × 63 × 83 | `#headW`, `#headD` + `#face`, the arc to the stalk |
| mouth floor | y −27 | `#face` in from the face at −30 |
| mouth flats | z −13 and −23 | `#mouthDn` down, `#mouthH` apart |
| fillet cylinders | r 12, four of them | `#round` |
| chamfer planes | z −36 and −30 | `#chamfer` |

**The face is on −Y.** That is what makes the eye's depth `#headD / 2 + #face` and the mouth's
start offset `#headD / 2`: both are measured from the Front plane at the head's middle.

## What the dialogs did

- **Part Studio variables are added through the right-rail Variable table panel**, in the section
  named for the tab. New rows land at the rollback point, so the rollback bar goes above the first
  feature first. "Roll to here" on the first feature lands one row too low, because it rolls to
  *include* what was clicked.
- **The panel scrolls.** After eight rows the blank Name row falls below the visible area and the
  next add silently does nothing.
- **Type the expression, press `Tab`, then click the tick.** Clicking the tick while the variable
  autocomplete is still open reverts the edit and reports no error. After `Tab` the field shows the
  resolved value rather than the expression, which is not a failure.
- **The Ellipse tool is inside the Center point circle dropdown.** Draw order is centre, major-axis
  end, minor-axis end.
- **Which ellipse dimension you get depends on where you put the label, not what you click.**
  Clicking the major-axis end and placing up-and-right gave `MINOR_DIAMETER`; the same click placed
  directly above the centre gave the major diameter. The first attempt was numerically right by
  coincidence — `#eyeRx` is 8 and the minor radius is 4 — and only reading the constraint type back
  over REST showed it was the wrong constraint.
- **A deleted sketch curve does not orphan the extrude that used it.** `eye` queried the circle's
  region and picked up the ellipse's region unedited, because the sketch still has exactly one
  region. `second eye`, a feature mirror, followed.

## B6 — `foot`

The plan's B6 row is one line, *the groove pattern's phase*. It is one dimension, and the tab needed
four more edits before it was reading the numbers the draft had settled.

## Four locals that shadowed the Variable Studio

[`../a13-variables-table.md`](../a13-variables-table.md) names `foot` as a tab that reads `#ball`,
`#wall`, `#collar` and `#grip` from `robot sizes`. It declared all four itself.

| | local | studio | effect of deleting the local |
| --- | --- | --- | --- |
| `#ball` | `#torsoH / 8` | `#torsoH / 8` | none |
| `#wall` | `#torsoH / 32` | `#torsoH / 32` | none |
| `#collar` | `11 mm` | `11 mm` | none |
| `#grip` | `3.6 mm` | A2's expression, 1.9465 | `#collar_down` and `#pedestal` move |

The first three were the same number written twice. Deleting them left the foot at **38818.933 mm³,
the figure it had before**, which is the whole check: `#collar_r = #ball / 2 + #wall` resolved
against the studio without being touched.

**`#grip` had never been given A2's number.** It carried 3.6, which is neither draft9p0's 48 mm
value nor its doubling. `#collar_down = #collar - #grip` went 7.4 to 9.05352 and
`#pedestal = #plate - #collar_down` went 4.6 to 2.94648.

## The pedestal had been buried in the socket

Deleting `#grip` shortened `foot pedestal` by 1.65352 mm and **the foot's volume did not change** —
still 38818.933 mm³. A Ø18 slab that thick is 420.68 mm³, so the material the pedestal lost was
material the derived socket was already occupying.

That is what the stale number was doing. The socket's collar is `#collar` tall and hangs
`#collar_down` below the mouth, so its underside sits at −9.05352. The pedestal is meant to fill
from the plate's top face at −`#plate` up to that underside, which is what
`#pedestal = #plate - #collar_down` says. Built at 4.6 it ran to −7.4 and pushed 1.65 mm into the
socket; the union welded the two and no feature ever went red. **Now they abut, and the arithmetic
that names the pedestal is true of the part.**

## The phase

| | expression | mm |
| --- | --- | --- |
| was | `#foot_l - #heel_y` | 64 |
| is | `#foot_l - #heel_y - #rib_w / 2` | 61 |

**The dimension is from the sketch origin, not from the end of the sole.**
[`../a5-foot-tread.md`](../a5-foot-tread.md) is written in sole coordinates, where the offset is
`#rib_w / 2` and nothing else. In the model the origin stands at the ankle, `#foot_l - #heel_y` from
the toe, and the pattern seeds at the toe and steps toward the heel. So the term that locates the
toe stays and the phase term is added to it — the same shape as `foot outline`'s
`#foot_l - #heel_y - #toe_r`, which puts the toe circle's centre there.

`sole ribs` needed no edit: its count was already `#foot_l / (2 * #rib_w)`, which is eight.

## What the tread does now

| | was | is |
| --- | --- | --- |
| first groove | −64 to −58 | −61 to −55 |
| last groove | 20 to 26 | 23 to 29 |
| heel margin | 6 | 3 |
| toe margin | 0, flush with the toe edge | 3 |
| pieces of sole between and around the grooves | 8 | **9** |
| volume | 38818.933 mm³ | 38778.629 mm³ |

**The ninth piece of sole is the check.** With the run flush at the toe there were eight lands, one
before each groove. With land at both ends there are nine. A5 asks for a tread that starts and ends
with land, and the face count says it does without anyone reading a margin off a picture.

**draft9p0 was not as wrong as A5 records.** A5 works the offset 64 forward and concludes only the
first three grooves fall on the sole and the other five are cut in empty air. The built model has
all eight on the sole — 64 is measured from the origin to the toe edge, not from the heel, so the
run started at the toe and the error was the flush toe and the doubled heel margin. The row A5
adopts is unaffected; what it rejects as *B kept at eight grooves* is what draft9p0 actually built.

## B7 — `hinge`, `u limb` and `l limb`

[`../a1-limb-center.md`](../a1-limb-center.md) settles that a limb is 48 mm centre to centre and
derives the rod lengths from it. draft9p0 built 102.05 and 102.00. This row is the correction, and
it came down to one hinge variable, one distance A1 does not account for, and the two limb extrudes.

## `#rod` was a filler, and it is what put the limbs at 102

Each hinge part carries a plain Ø`#limbD` shank behind its knuckle whose only job was to butt onto
a limb's end face. `#rod` sets how long that shank is, and it was set to `#limbD`.

| | expression | mm | blade reaches | fork reaches |
| --- | --- | --- | --- | --- |
| was | `#limbD` | 24 | 44.0 | 45.0 |
| is | `#ear` | 6.4 | 26.4 | 27.4 |

A 44 mm blade on one limb and a 45 mm fork on the other is the whole of the recorded 52.4 and 54
minimum. A1 calls that minimum a consequence of stacking rather than a property of the joint, and
the table is the evidence: the only number that changed is the length of the filler. `#ear` is
`(#limbD - #slot) / 2`, the thickness of one fork ear, so the shank is now a web as thick as the
ears beside it.

## The rod stops one knuckle radius short of the pin

A1 derives the rod lengths along a line, and along a line a rod may start at the pin. The knuckle
is not on that line: it is a disc of radius `#nose` turning about the pin, and a Ø`#limbD` rod that
starts at the pin is inside it.

- On `l limb` the rod's first 12 mm stood where the fork's ears go.
- On `u limb` the rod ran to the pin and filled the fork's slot through the blade nose's whole
  sweep. The slot's wall fell from 555.131 mm² in `hinge` to 162.545 mm² in `u limb`, and the blade
  had nowhere to enter.

**So each rod stops `#nose` short of the pin, which is the circle the joint turns inside.** The
rod's end face and the knuckle are then concentric about the pin and touch along one line, so the
joint still turns. `#nose` is `#limbD / 2` and both limbs already read `#limbD`, so this needs no
new row anywhere — it is the model being made to fit a hinge that has not changed.

`fork to robot connector` moves with it. It sat on the shank's end face, which is where the rod
used to stop; it now sits on that same tangent plane at `#nose - (#slot_deep - #nose + #rod)`,
−15.4 mm. All three names are the hinge's own, so the fork's reach stays a hinge fact and the limb
never has to know it.

## What each limb is now

| | rod expression | mm | rod runs |
| --- | --- | --- | --- |
| `u limb` | `#limbCenter - #collar + #grip - #limbD / 2` | 26.94648 | −9.0535 to −36 |
| `l limb` | `#limbCenter - #stand - #limbD / 2`, begun `#limbD / 2` in | 26 | −12 to −38 |

| | station | measured z | centre to centre |
| --- | --- | --- | --- |
| `u limb` | shoulder or hip, ball centre | 0 | |
| `u limb` | elbow or knee, pin bore | −48 | **48** |
| `l limb` | elbow or knee, pin axle | 0 | |
| `l limb` | wrist or ankle, ball centre | −48 | **48** |

Both resolve to one part — `u limb` 18222.985 mm³ over −60 to 1.9465, `l limb` 17727.976 mm³ over
−54 to 12 — and the fork's slot wall is back to 364.094 mm², open the 24 mm the nose sweeps.

**Neither rod is one of A1's four stock lengths.** A1 reads 53, 51.6 and 38, which are the segment
measured from station to station; the extrude is what is left after the socket takes `#collar` at
one end and the knuckle takes `#nose` at the other. A1 quotes `make_plans.py:87` saying each joint
*takes about 21 mm of a 48 mm segment, and the other end of that segment is a COLLAR_L socket*, and
that sentence is the one the model agrees with.

**The shoulder inset of 5 is gone rather than settled.** A1 gives the upper arm
`#limbCenter + inset` and the thigh `#limbCenter + #grip`, and calls the 5 a typed number with
nothing behind it. There is one `u limb` Part Studio and it serves both, so it builds one length,
derived from `#limbCenter`.

## `l limb` sketched on a plane instead of a face

`limb section` was on a face of `add blade` — the shank's end face, which is exactly the stacking
A1 removes. It is on the Top plane now, so the pin is the sketch's origin and the rod is placed by
its starting offset rather than by whatever the hinge happens to reach.

## What the dialogs did

- **An extrude's flip is `Opposite direction`, on the End type row.** The row labelled `Direction`
  is a custom direction vector: ticking it leaves an empty query and turns the feature red.
- **A starting offset measures the depth from the offset plane, not from the sketch plane**, and it
  carries its own `Opposite direction`. Set the offset first and the depth after.

## B8 — `gripper`

A10 settled four rows and B8 found three of them already built. The bore runs along X, the mouth
opens −Y, the mouth is 2.6 across, and `clip body` already carried `2 * #collarR` behind the 18 mm
the dialog displays. The one row left was the fourth, and it is the one A10 wrote a paragraph
about: **the top of the body is the collar's own circle, not a slab wide enough to sit under it.**

## A round collar and a straight-sided slab cannot share an outline

The body was 18 across and 10 deep, and the collar standing on it is Ø18. Seen from above the two
outlines meet at exactly two points. Everywhere else one of them is outside the other: the collar
overhangs the body 4 mm fore and aft, and the body's four corners stick out past the collar, at
`sqrt(9² + 5²)` = 10.30 from the axis against the collar's 9.

**So making the top flush takes both an add and a remove.** Widening the body fore and aft does not
help on its own, because the corners stay outside; trimming the corners does not help on its own,
because the collar still overhangs. One sketch on `plane to cut top of clip` carries both circles —
`2 * #collarR` and `4 * #collarR`, concentric on the origin — and its two regions drive the two
extrudes. Onshape read the inner region as `Add` by itself and the outer ring had to be told
`Remove`.

## The height of the round top is the collar's overhang

A10 does not give one, and nothing else in the part does either. `#collarR - #clipR` = 4 is the
amount the collar overhangs the clip, which is the quantity the round top exists to absorb, and it
is written from two numbers the tab already declares. It puts the neck at z −13.0535, which is
0.95 above the clip's crown and 4.6 clear of the mouth's upper lip.

## The proof that it is flush is that there is one face, not two

| | | |
| --- | --- | --- |
| cylinder | r 9.0000, area 796.962 mm² | one face, z 1.9465 down to −13.0535 |
| clip outer | r 5.0000, axis −X from x 9 | Ø10.000 |
| clip bore | r 1.6500, axis −X from x 9 | Ø3.300 |
| socket cavity | sphere r 6.0800 at the origin | |

A full Ø18 cylinder 15.0 tall has 848.230 mm² of skin. The four slits take 4 × 1.6 of the
circumference over their 8.0 mm, which is 51.200, and 848.230 − 51.200 = 797.030 against a measured
796.962. **The collar and the body below it are one cylindrical surface** — Onshape merged them,
which it can only do if they are coaxial and the same radius.

The old annular step at z −9.0535 is gone from the model. The step at z −13.0535 that replaces it
reads as six faces: two lunes of 42.106 mm², which is the Ø18 disc less the 18 × 10 rectangle,
halved; and four slivers of 2.436 mm², which is the rectangle less the disc, quartered.

| | mm³ |
| --- | --- |
| was | 4111.177 |
| lunes added over 4 mm | +335.66 |
| corners trimmed over 4 mm | −37.78 |
| is | **4409.053** |

## Measured

| check | wanted | measured |
| --- | --- | --- |
| parts | 1 | 1 |
| clip bore | Ø3.300 | Ø3.300 |
| clip outer | Ø10.000 | Ø10.000 |
| mouth | 2.600 | 2.600, lip faces at z −20.3 and −17.7 |
| mouth angle | ±52.0° | the bore face is 132.714 of 186.611 mm², so 104.0° is missing |
| gripper length | 24.000 | bbox z −24.0 to 1.9465, wrist center on the origin |
| bore axis | parallel to X | axis −1, 0, 0 |
| symmetric about YZ | | x-planes at ±9.0000, ±5.0000 and ±0.8000, areas equal to four places |

**The thinnest wall is 2.920 at the socket collar, and the brief asks for 2.20.** 2.20 is
`9.0 - 6.8`, and 6.8 is the ball's radius plus a `#fit` of 0.8. A2 set `#fit` to 0.08, so the cavity
measures r 6.0800 and the wall is `9.000 - 6.080`. The number in the brief predates A2 rather than
describing a defect in the part.

## `make_plans.py` still draws the slab

`clip_front()` draws the body as a plain 18 × 24 rectangle and `clip()` draws a 10-deep stem
running the whole way to the wrist, so neither sheet shows the round top. `clip_front()`'s own
docstring says the body is *"the collar's own diameter, so the top of the part is flush with the
socket standing on it all the way round"*, which is the thing A10 settled and the thing the drawing
does not do. A10 changed a shape rather than a number and A12 regenerated the sheets from the
numbers, so r6 carries the old body. **The sheets and the model disagree about the gripper**, and
correcting the drawing is design-source work rather than a B row.

## B9 — `stickbot`

The row asks for four things: Width mates on the elbows and the knees, instances taken from a named
version rather than the workspace, the rest pose, and the feet symmetric. Three are built and
measured. The fourth is withdrawn, because reading the assembly back showed there is nothing at a
hinge for a Width mate to hold.

## Hiding every instance is what made the tab workable

With all fourteen parts drawn, the assembly tab held its renderer between 70 and 200 percent of a
core. One read of the tree took 63.6 s, and a screenshot ran past the 60 s default and failed.
Right-click any instance, choose **Hide all instances**, and the same read takes 0.0 s. Every edit
below was made with the parts hidden, and they were shown again at the end.

The feature-list window is a Part Studio fact. `ftree.rows` clips to y 150–655 because that is
where a Part Studio's list ends; an assembly's list runs the full window height, and the thirteen
mate rows sit between y 651 and 963. An assembly tree also needs no scrolling — every row is
already on screen — so the rewind-and-wheel search that finds a Part Studio feature is the wrong
tool and never returns on a busy tab.

## Change to version… re-points fourteen instances and keeps thirteen mates

`../../2026-08-23-draft9p0/b1/notes.md` recorded the same deviation three tutorials running:
*"inserted from the workspace again"*, because the Insert dialog's **Current document** tab lists
Part Studios from the workspace and offers no version picker. Every instance in this assembly
arrived that way, and the REST instance record carried no version key at all.

The fix does not need the fourteen re-inserts and thirteen re-mates that `Replace instances…` or
delete-and-reinsert would cost. Select `torso <1>`, shift-click `u limb <4>` to take all fourteen,
right-click, and the menu offers **Change to version…**. That opens the Reference manager on a row
reading *stickbot-draft9p1 — Main ⇒ parts built*, and **Update all** re-points the lot. Afterwards
every instance record carries `documentVersion`, every instance keeps its id, all thirteen mates
survive, and each tree row is annotated *"Versioned part from current document"*.

| | |
| --- | --- |
| `Start` | `8e4b28cc2cf504aef52a7a9a`, from B0 |
| `parts built` | `6eae7c37deee3f58facbbf83`, every Part Studio at the end of B1–B8 |
| `ankle centered` | `e6fd823965e71c15d9e267cb`, the foot's connector moved |

The toolbar's **Update all references to latest versions** opens the same Reference manager, which
is the route for the second version. A version is renamed from the Versions and history panel by
right-clicking its row and choosing **Properties…** — there is no Rename item.

## `torso <1>` was already fixed

`assembly.md` lists two things run 4 did not do, and says both are still open. One of them is not:
`torso <1>` reads `fixed=True` and the tree shows *"Part is fixed"*. It is held by **Fix** rather
than by the Fastened mate the brief's table asks for, which is the same constraint by a different
name and leaves nothing for B9 to build.

## The feet were 1.6 apart because the connector caught the slit wall

The foot's socket is a snap-fit, so a slit runs through it. `bodydetails` reads the slit as planar
faces at x ±0.8 and a wider relief at x ±5.0, and the socket cavity as a sphere of r 6.0800 at the
Part Studio origin. **`mate to robot` had its origin entity on a face of the slit**, so the
connector sat at x 0.8 rather than on the ball's center.

Both feet are the same part inserted the same way up, so both inherited the same +0.8. That does
not tilt the robot; it slides one foot inboard and the other outboard.

| | foot center | inner edge |
| --- | --- | --- |
| left, before | x 23.2 | −0.8 |
| right, before | x −24.8 | −0.8 |
| left, now | x 24.0 | 0 |
| right, now | x −24.0 | 0 |

The repair is one field. `mate to robot` is *On entity*, and its origin entity moves from *Face of
add socket* to the Part Studio **Origin**, which is where the socket ball's center is by
construction — the derived socket is placed there. The connector keeps its orientation, Z up and X
along X, so the ankle mate does not need rebuilding. `Origin` is picked by clicking the row in the
feature list while the field is open; the chip then reads *Vertex of Origin*.

**The offset the sheets draw is not in the part.** `make_plans.py` has `FOOT_X = LEG_X + FOOT_H/3`
and mirrors it per side, so the sheet puts the feet at x ±32 with their inner edges at ±8 and a
16 mm gap; `a11-assembly.md` says the same and adds that *"the offset is in the part, not in the
pose: the foot's ball is 8 inboard of the foot's own center"*. The built foot's bounding box is
x −24…+24 about a socket at x 0. It has no offset and no handedness, so at rest the two feet meet
on the center plane. Giving the part the 8 makes the foot handed — a foot rotated 180° about Z to
flip its offset points its toe backward — which is a second part, a second print and a second BOM
line. That is a design decision and it belongs to the source, not to a B row.

## The rest pose is reached by making each mate Fastened and then putting it back

A Ball mate has no values to type, so there is no numeric way to send one to zero. What does work
is the mate type list: change the mate to **Fastened**, which aligns both connectors completely and
solves, then change it back to Ball or Revolute in the same dialog and accept. The parts stay where
the Fastened solve put them, because the solver starts from the positions it already has.

The list is at a fixed place once the dialog is open — the Mate type row at (343, 121), and the
options below it at Slider 152, Cylindrical 178, Revolute 204, Pin slot 230, Planar 256, Ball 282,
Fastened 308, Parallel 334. Thirteen mates, top down, took about six minutes.

Every instance now sits at identity rotation, which is what makes the pose readable: the whole
robot is the plan sheet's stations with no rotation anywhere.

| | translation, mm |
| --- | --- |
| `torso <1>` | 0, 0, 0 |
| `head <1>` | 0, 0, 103.054 |
| `u limb <1>` and `u limb <2>` | ±49.551, −7.824, 19.235 |
| `l limb <1>` and `l limb <2>` | ±49.551, −7.824, −28.765 |
| `Gripper <1>` and `Gripper <2>` | ±49.551, −7.824, −76.765 |
| `u limb <3>` and `u limb <4>` | ±24, 0, −58 |
| `l limb <3>` and `l limb <4>` | ±24, 0, −106 |
| `Foot <1>` and `Foot <2>` | ±24, 0, −154 |

**The arms hang straight down, not along the studs.** A11 says that at rest *"each arm lies along
its own shoulder stud, 33.13° from vertical"*. The torso's shoulder connector is at
(49.551, −7.824, 19.235) with its Z along the torso's Z, so the position a Ball mate aligns to is
vertical. 33.13° is the stud's angle, and the connector was not built on the stud's axis. At rest
the arm clears the torso by 9.102.

## There is no slide at a hinge, so the Width mate is withdrawn

A11's case for the Width mate is that *"all four hinges in draft9p0 are a bare Revolute, so every
lower limb can slide sideways in its fork"*. Onshape's own documentation says a Revolute mate
provides one degree of freedom, rotation about Z, and the elbow and knee mates are built on mate
connectors at (0, 0, 0) and (0, 0, −48) on each limb's own axis. Coincident connectors leave no
translation to take away.

The assembly's own arithmetic closes on that exactly. Thirteen instances are free of the fixed
torso, so the assembly starts with 78 degrees of freedom.

| | mates | each removes | removed |
| --- | --- | --- | --- |
| Ball | 9 | 3 | 27 |
| Revolute | 4 | 5 | 20 |

78 − 47 leaves 31, and 31 is exactly 9 × 3 rotations at the balls plus 4 × 1 at the revolutes.
**Every remaining degree of freedom in this assembly is a rotation.** A Width mate takes two
degrees of freedom off a pair of faces that can still slide; here there are none, and adding one
would be a redundant constraint on a joint that is already located.

The 0.6 mm of clearance each side that A11 describes is real, and it is why the printed blade can
be pushed off center by hand. It is a fit in the solid, not a degree of freedom in the model, and a
mate cannot remove it. Whether the tutorial should teach a Width mate step is a question for
`assembly.md` and A11, and it is recorded for the register rather than settled here.

## Measured

| check | wanted | measured |
| --- | --- | --- |
| instances | 14 | 14, every one carrying `documentVersion` |
| mates | 13 | 13, 9 Ball and 4 Revolute |
| subassemblies | 0 | 0 |
| standing height | 317.05 | **317.0535** |
| top of the head | +139.05 | +139.0535 |
| sole | −178 | −178.0 |
| neck ball | +58 | the torso's connector is 0, 0, 58 |
| hips | z −58, x ±24 | ±24, 0, −58 |
| knees | z −106 | ±24, 0, −106 |
| ankles | z −154, x ±24 | ±24, 0, −154 |
| foot centers | x ±32 | **x ±24**, the part carries no offset |
| widest | | x ±61.5509, which is the arm at 49.551 plus its own 12 |
| deepest | | y −64 to +32, which is the foot's own 96 |
| degrees of freedom | | 31, all of them rotations |

## What the dialogs did

- The mate type list sits at a fixed place in the dialog and does not move with the mate's type,
  so a Ball and a Revolute are edited by the same coordinates.
- Onshape's context menu uses none of `[role="menu"]`, `.dropdown-menu`, `.context-menu`,
  `.os-context-menu` or `ul.menu`. Sweeping `li,a` finds it; sweeping `li,a,div,span` forces a
  layout per element and never returns.
- The Width mate is at (598, 58) on the assembly toolbar, past Parallel and Tangent. **Assembly
  mirror** is at (874, 58), which is the tool a handed foot would be built with.
- Two Playwright processes on one page fight over the scroll and the right-click. One at a time.
- A page that answers `evaluate` while `mouse` and `screenshot` hang is a wedged renderer, not a
  slow one. Restarting `agent_browser.py` re-borrows the session cookies and clears it.
