# Run 5 — repairs

Run 5 changes geometry. Where run 4 copied run 3 and measured it, run 5 opens each part and makes
the model match its brief, one step at a time, measuring after every step. This file is the record
of what was cut and what it measured afterwards. The plan it follows is
[`../../design-into-cad.md`](../../design-into-cad.md).

Every number here came off solved geometry. Nothing is read back from a feature parameter, because
a parameter read-back and a tree of `OK` states have each passed separately on an edit that moved
nothing. S1 through S3 measured through `POST .../featurescript`; by S4 that endpoint was returning
429 and the numbers come from `massproperties`, `boundingboxes` and rendered views instead.

## S1 — the torso's shoulder stud

The brief asks for a stud that leaves the side face at 53° below horizontal and 30° toward the
front, 13 mm from the face to the ball center, whose first 8 mm is a Ø8 boss coaxial with the
stalk. Runs 3 and 4 carried a plain Ø3 stalk leaving the side face square.

**The profile.** Rebuilt as boss, stalk and ball on one axis: six entities in the loop plus the
side face kept as a construction line, so the brief's 13 mm and 8 mm are dimensioned from the face
rather than from the origin.

**Getting it onto the axis.** `STUD_D` is `R_z(−30°) ∘ R_y(+53°)` applied to `+X̂`, so the stud is
two rotations of a profile drawn flat, not one general rotation. Two mate connectors at the root
supply the axes — one turned `ABOUT_X` by −90° to aim its Z along +Y for the drop, one left along
+Z for the swing — and two `transform` features of type `ROTATION` turn the revolve about them.

**The boss runs 8 mm back as well as 8 mm forward.** The first attempt rooted the boss's back cap
at the side face, and the rotation put exactly half the Ø8 disc outside x = 18: a flat crescent of
25.133 mm² on the outside of the shoulder, which is π·4²/2. Running the boss back into the torso
puts that cap inside the block. There is no shorter boss that avoids the cut — a cap fully inside
x ≤ 18 needs at least 6.55 mm of back, a cap fully below z = 24 needs at most 1.99 mm, and those
cannot both hold. **The flush cut is part of the design, not a repair to it.**

**The cut.** Everything standing above the top face is removed by one extrude, `Trim above the top
face`, on a sketch of two circles on the Top plane: Ø80 outside, Ø12 around the neck. The Ø12
leaves the neck stud standing and nothing else — above z = 24 the shoulder material starts at
x = 10.4, so the annulus clears it by a wide margin. The cut starts 24 mm up and runs 40 mm.

It has to sit **after** the shoulder fillets. The fillet at the boss-to-torso junction is concave,
so it *adds* material, and that flare is most of what stands proud; cutting before it just lets it
grow back. A first attempt used the torso's own footprint as the profile and left the outboard
part of the flare behind, out to x = 25.583, because the footprint stops at x = 18.

### Measured after S1

| | |
| --- | --- |
| bodies | 1 |
| volume | 42890.161 mm³, of which the trim took 300.797 |
| shoulder ball centers | (±24.775, −3.912, +9.618) |
| neck ball center | (0, 0, +29) |
| hip ball centers | (±12, 0, −29) |
| highest point that is not the neck | z = 24.000 |

The mirror carried the rotated stud without a further edit.

### What S1 found

- **The brief put the shoulder ball 4 mm too high.** It read `z = +13.618`, which is 24 − 10.382 —
  measured down from the top face instead of out from the root at z = +20. Corrected to `+9.618`,
  which is what the model measures.
- **The scar rule was stated per mm of diameter and is per mm of radius.** The brief's own 14.64 mm
  for a Ø8 boss is 3.66 × 4, not 3.66 × 8.
- **The swing arc is not free.** The brief claimed the arm clears the torso everywhere in the arc,
  at 0.73 mm at the tightest. Swept properly, the arm clears at rest — 0.776 mm at the zero pose,
  reading it as a plain Ø12 rod — but its far end crosses the torso from 33.38° of the 37.09° the
  ball allows, and at full tilt the deepest overlap is 1.597 mm, 24 mm out along the arm, with 85%
  of directions still clear. The shoulder end itself never binds: 1.372 mm at rest, 0.413 mm of
  overlap at the worst point of the cone. What limits the pose is the arm crossing the body.
- **The neck boss cannot buy the tilt it exists for, so it is not built.** A boss of height `h` on
  the top face makes the boss-to-boss spacing `3.65 − h`, away from the 4 mm the head's 42°
  assumes; and the contact that binds is the head's outer underside at radius 23.43, which a boss
  at radius 6 does not move. Both briefs now say so.

## S2 and S3 — the hinge's two halves

Repaired as a pair, because the surfaces in
[`deconflict.md`](deconflict.md) are shared between them. Every one of these was an existing
dimension driven to a new value; only the slit is a new feature.

### Measured after S2, on `limb-socket-clevis`

| | |
| --- | --- |
| ear inner faces | y = ±2.8, from a slot driven 3.6 → 5.6 |
| ear outer faces | none — the ear's outer surface is the Ø12 cylinder |
| stub tips | y = ±2.0, on the pin axis at z = −24, r 1.0 |
| fork tip | z = −30.000, off a round end driven Ø11.62 → 12 |
| slot root | z = −13.000, which is 11 behind the pin axis |
| volume | 2040.644 mm³ |

The ±2.5 planes that S2b expected to remove with the ear survive, and they are not the ear: they
sit at z −4.15 to −1.957, up in the socket collar, and they are the relief slits. S2b is done.

The stub pins followed the ear face out to y = ±2.0 without being touched — they are constrained
to it rather than dimensioned from the origin, which is what the brief asks for and what let one
edit carry two surfaces.

### Measured after S3, on `limb-blade-ball`

| | |
| --- | --- |
| blade faces | y = ±2.5, from a blank driven 3 → 5 |
| valley floors | y = ±2.05, which followed the blade face on their own |
| pocket floors | y = ±1.5 |
| slit faces | y = ±0.4, leaving a **2.1** tab a side and **1.1** behind each pocket |
| blade tip | z = +6.000, off a round end driven Ø11.62 → 12 |
| the blade's own limb | starts at z = −10.000, so the blade stands 16 out |
| volume | 1949.102 mm³, of which the slit took 141.166 |

Both halves now agree at every surface `deconflict.md` lists.

### The blade's limb ending is not in the sketch that draws the blade

S3c reads as one step and is two features. `Blade profile` carries the profile's own 6.11, and
driving it to 10 moved nothing at all — the volume did not change by a thousandth, because the
blade blank is trimmed back to the limb and everything past the trim is thrown away. The station
that had to move is the `Limb` extrude's **starting offset**, and its depth has to come down by
the same amount or the limb grows out of its far end. Both were needed: the profile has to reach
z = −10 for the blade to meet the limb there.

### What the slit is

`Slit profile` is a rectangle on the **Right** plane, symmetric about the Front plane by
constraint, its root dimensioned **10** below the Top plane — the same 10 the tab cantilevers —
and 0.4 from the mid-plane. `Slit` extrudes it Remove, Symmetric, **Through all**, so nothing in
the feature depends on how wide the blade happens to be.

The rectangle's top is dimensioned 8 above the Top plane and that number is not a design
dimension. It is an overshoot. The round end reaches z = +6 at one point only, so a profile that
stopped at 6 would touch the surface and leave the slit closed at the tip instead of open.

## S4 — the foot

Two steps that share nothing: a re-sketch that turns the whole part 90°, and four slits cut into a
collar that already existed.

### S4a — the outline now runs along Y

`Foot outline` is a heel circle Ø16 and a toe circle Ø24 joined by two lines. Both centers are
constrained onto the Right plane's trace and the two side lines carry a `Symmetric` about it, so
the width is one dimension rather than two. The lines were left un-tangent here and S7 fixed that —
see below. Every feature downstream — plate, fillet, ball,
collar, socket, ribs — followed the new orientation without being re-picked, except the sole rib
profile, which had been drawn 26 × 3 along X and had to be transposed.

### Measured after S4

| | |
| --- | --- |
Stated after S7 turned the part around and constrained the outline, which is the shape that ships.

| | |
| --- | --- |
| bodies | 1 |
| width, along X | ±12.000 |
| length, along Y | −32.000 to +16.000, toe forward |
| height | −12.000 to +1.350 |
| plate | z −12 to −6 |
| collar | 7.350 proud, to z = +1.350 |
| sole ribs | 7 of them, 6 apart, cutting 1 mm up from z = −12 |
| volume | 4899.224 mm³, of which the four slits took 46.048 |

### S4b — the slits

`Relief slit profile` is one rectangle on the Top plane, 0.8 wide by `Symmetric` about the Front
trace, its inner edge dimensioned **2.5** from the origin and its outer edge **6.0**. The 2.5 is
inside the 2.901 mouth radius, which is what lets the mouth open;
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) gives 2.5 out to
6.0 as the working band. `Relief slit` extrudes it Remove, 6 down and 1.35 up, merge scope the foot
alone so the cut cannot reach the ball. `4 relief slits` is a **feature** pattern of that extrude,
360° and 4 instances, about the collar's own rim edge.

### What S4 found

- **A patterned Add that touches nothing fails quietly, per instance.** `Sole ribs` marched its
  instances −Y off the heel end and landed one rib, with no error anywhere in the tree. This is the
  failure [`../../build-briefs/torso.md`](../../build-briefs/torso.md) warns about, met on a part
  that brief does not cover. Onshape also **rejects a negative pattern distance** outright — the
  field turns pink — so the way back is the flip-direction icon, not a minus sign.
- **A model edge is pickable as a dimension reference even with imprinting off.** The slit's inner
  dimension anchored itself to the collar's outer circular edge instead of the Right plane's trace,
  which put the slit 2.5 mm outside the collar while reading 2.5 in the field. It was re-dimensioned
  from the origin point.
- **A drag test is not a constraint test, and S4a got this wrong.** The outline's two side lines
  never turned black, and a 76 px drag moved nothing, which was read here as "blue but rigid". They
  were under-defined: chords, not tangents, held in place only by where they happened to be
  solved. The drag was resisted by the solver's preference for the current solution, not by a
  constraint. S7 flipped the outline's dimensions and the lines re-solved into a shape 0.322 mm too
  wide, which is how it was caught. **Blue means under-defined. Believe the color, not the drag.**
- **The slit's depths were right and its directions were not, and only the volume said so.** The
  extrude read Blind 1.35 with a second end of Blind 6 — 7.35 in total, exactly the collar's proud
  length — but the first direction ran down and the second ran up, so the pair spanned z −1.35 to
  +6 and half of it was in empty air. The tree was green, the dialog read correctly, and the front
  render showed a notch that could pass for foreshortening. What caught it was arithmetic: a cut
  through that annulus over z ±1.35 is 3.45 mm³ and over the whole 7.35 is 11.51, and the model had
  given up 3.457. Swapping the two depths — 6 down, 1.35 up — gave 11.512.
- **`Direction` in the extrude dialog is not a flip.** It is a checkbox that asks for a direction
  *reference*, and ticking it with nothing to reference errors the feature. The flip is the arrow
  beside the `Blind` dropdown.

## S5 — the brief was wrong, and it is fixed

`hinge.md` said run 3 built 13 valleys across the blade's 180°. Measured on the model: 24 valleys
on each face at exactly 15° spacing, spanning the full 360° — and the feature that cuts them is
named `24 detent valleys`. The brief now says what the model does.

## S7 — the assembly

Fourteen instances of six parts, every one inserted from its `run 5` version rather than a
workspace.

### The robot faces −Y and the foot points +Y

Nothing in [`../../build-briefs/README.md`](../../build-briefs/README.md) says which sign of Y is
forward. It says only that fore-and-aft is Y, and each brief then picked a direction on its own.
Two picked −Y and one picked +Y, and no part ever measured against another until they were put in
one assembly.

The head decides it. Its bounding box runs y −16.5 to +15.0: the flat back face that Shell opens is
at +15, the profile front is at −15, and the −16.5 is the eyes standing 1.5 proud of it. The torso
agrees — S1 measured the shoulder ball at y = −3.912, and `torso.md` calls that "forward". Onshape's
own Front view looks at the −Y side, so a robot that faces −Y is the one whose front elevation is
the Front view.

The foot is the outlier. It measures y −16 to +32, heel behind and toe in front of a **+Y** front,
and [`../../build-briefs/foot.md`](../../build-briefs/foot.md) states that choice in as many words.
So the figure as first assembled stands with its feet on backwards.

This is the second orientation fault found in the same part in two steps, and it has the same root:
**a shared convention that no single brief owns gets decided independently by each part, and the
error is invisible until they meet.** S4a caught the axis; S7 caught the sign. `README.md` now
states the sign, because that is the file the parts share.

### Turning the foot around, and what it exposed

The foot is symmetric about its own fore-and-aft centerline, so the turn is a mirror of four
numbers in `Foot outline` and nothing else: the Ø16 and Ø24 swap ends, and so do the 8 and the 20
that place their centers. **No entity had to be dragged across an axis** — swapping which circle is
which does the mirror, and every intermediate state stays solvable if the far circle is moved out
before the near one is moved in.

Two features did not follow:

- **The sole ribs kept marching the way they always had**, which was toward the heel once the heel
  changed ends. `Sole rib profile` moved from 10 to 26 off the centerline, which is the mirror of
  its old station, and the seven ribs land back across the whole sole.
- **The outline came back 24.322 wide instead of 24.** The two side lines were never tangent —
  they were chords whose endpoints happened to sit near the tangent points, and re-solving the
  dimensions moved them somewhere else that satisfied everything the sketch actually said. Two
  `Tangent` constraints turned the whole outline black and the width to exactly 24.000.

The width is the check that caught it, and it caught it only because `boundingboxes` is exact:
the head measures 36.000 across and −16.5 to +15.0 in Y, both to the thousandth, on a part made
of arcs and fillets. **A bounding box that disagrees with the brief by 0.3 mm is a real defect,
not tessellation noise.**

### Measured after mating

| What | Got |
| ---- | --- |
| mate features | 13, all `OK`; 2 assembly mate connectors |
| ground | z = −89.000 |
| top of head | z = +63.650 |
| figure height | 152.650 |
| torso, on its own | x ±27.775, y ±12.000, z ±32.000 |
| hips | z = −29, knees −53, ankles −77 |
| shoulder balls | x ±24.775, y −3.912, z +9.618 |
| volume, all fourteen instances | 75512.993 mm³ |

### What the assembly found

- **A mate that reports 200 on creation can still be in error, and the reason is the query
  type.** Eleven mates were posted with `BTMIndividualQueryWithOccurrence-626` and a path of
  `[instance id, mate connector id]`. Onshape accepted every one, rewrote the type to
  `BTMIndividualOccurrenceQuery-626`, and set all eleven to `ERROR`. Hovering the error icon in
  the tree gives the message the API withholds: `Mate cannot resolve mate connectors.` A part
  studio's mate connector is `BTMPartStudioMateConnectorQuery-1324`, whose `path` is the
  occurrence alone and whose `featureId` is the connector. An assembly's own mate connector is
  `BTMFeatureQueryWithOccurrence-157`, with an empty `path`. The way to learn either is to build
  one mate in the GUI and read the feature back.
- **The dialog named both connectors while the mate was broken.** Opening the failed mate showed
  `Neck socket` and `Neck` in its list, in red. The names resolve off the ids; the mate resolves
  off the query type. **A filled dialog is not a working reference.**
- **The torso's `Shoulder R` and `Shoulder L` connectors are not on the shoulder balls.** They sit
  at x ±23, y 0, z +24 — the square-stud stations from before S1 — and Onshape's readout says so
  when the connector is selected. The balls S1 built are at x ±24.775, y −3.912, z +9.618, so the
  connectors are 14.382 too high, 1.775 inboard and 3.912 behind. S1 moved the geometry and left
  the connectors where they were. Two new mate connectors were placed on the ball faces in the
  assembly, which needs no new version of the torso and does not disturb the eleven mates already
  referencing it.
- **Nothing was fixed, so a drag moved the whole robot.** A mouse drag aimed at posing an arm
  landed on empty space, and the assembly — every instance of it, mates and all — translated
  37.292 in x and 12.012 in z. The mates stayed `OK` the whole time, because a rigid translation
  of everything satisfies all of them. Undo put it back; `Fix` on the torso stops it happening
  again.
- **The assembly matches `make_plans.py` and the shared README's station table does not.**
  `make_plans.py` computes `HIP_Z` −29, `KNEE_Z` −53, `ANKLE_Z` −77, `SOLE_Z` −89, `HEAD_T` 63.65
  and `HEIGHT` 152.65, and the assembly measures every one of them. The table in
  [`../../build-briefs/README.md`](../../build-briefs/README.md) says hip −24, knee −48, ankle −72
  and ground −84, which is a 5 mm shift from the first joint down. The parts are right and the
  table is stale.
- **Both shoulders are ball mates, so the arms rest wherever the solver leaves them.** After
  mating, the left arm stands out level and the right hangs down with the hand turned forward.
  Neither pose is a fault and neither is chosen; the joint has three rotational degrees of
  freedom and no limits.
