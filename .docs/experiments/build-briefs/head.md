# Build brief — the head

Read [`README.md`](README.md) first: deliverables, coordinate frame, and the settled Ø24 rule.

**Every number here moved on 2026-08-23 and none of them has been built.** The robot doubled and
the joint did not, so the head's own sizes are a clean 2× while `#grip`, `#fit` and the shell wall
stayed where they were — which is why the neck's tilt comes out *worse* than the half-size figure's
rather than the same. Where a value is still a run 3 measurement of the half-size part, it says so.

Run 3 built this and corrected it in three places: the shell opens the **back**, not the underside;
the recess does **not** buy the tilt this brief claimed; and the socket had no relief slits.

**The neck socket is now the standard collar**, the same Ø15.6 collar standing 12.2205 proud, four
relief slits that every other socketed part carries — decided 2026-08-13 and built into head
`run 5.1` on 2026-08-14
([build notes](../runs/2026-08-13-head-collar/build-notes.md)). Runs 3 to 5 built it as
a cavity bored into a boss instead, which is why that head had no slits, why shelling around
the boss leaves a 0.4 mm ring, and why the neck tilted as little as it did. The boss is gone.
Everything below is written to the collar; where a run measured the bored version, it says so.

The head is one part. It carries the **neck socket** on its underside and a face — two eyes and
a mouth — on its front. Shelling it removes most of the plastic; how much is worked out below.

## The frames

| Frame | What it shows |
| ----- | ------------- |
| [`images/cad-head-iso.png`](images/cad-head-iso.png) | the arch, the domed top, the two eyes and the mouth slot |
| [`images/cad-head-right.png`](images/cad-head-right.png) | from the right, where the eyes stand 3 mm proud of the face |
| [`images/cad-head-section.png`](images/cad-head-section.png) | cut on the Right plane, through the neck socket |

**The reference CAD, not the specification.** [`README.md`](README.md) § *Where the `cad-*.png`
frames came from* names the document, workspace and version each was taken at.

## The idea being tested

**A profile drawn from arcs and lines, tangent throughout, then given a face.** The head is the
robot's only free-form shape: everything else is a cylinder, a box or a joint. Stage 3 of the
build plan earns **Arcs**, **Tangent**, **Ellipse**, **Slot** and **Shell** here and nowhere
else, so if the head cannot be built this way the curriculum loses five tools at once.

**Shell is the part worth watching.** On the half-size head run 3 measured it removing 27535 mm³
of a 33340 mm³ solid — 83% of the plastic. **The head doubled and the wall did not**: 1.2 is three
perimeters at a 0.4 mm nozzle whatever size the robot is. So the solid grew eightfold while the
wall, which is thickness × area, grew only fourfold, and the fraction removed goes *up*: run 3's
5805 mm³ of wall implies about 4840 mm² of surface, four times that is 19350, times 1.2 is roughly
23200 mm³ of wall inside a 266720 mm³ solid — **about 91%**. That is arithmetic on an old
measurement, not a new one; measure it and report what you get. Shell also interacts with
everything cut into the part — eyes standing proud, a mouth cut in, and a socket cavity underneath
— and the order those happen in decides whether it succeeds.

## The numbers

| Name | mm | Source | What it is |
| ---- | -- | ------ | ---------- |
| across | 72 | plan | `#headW` = `#torsoW`. The head is as wide as the body — [`../runs/2026-08-25-draft9p1/a8-head-numbers.md`](../runs/2026-08-25-draft9p1/a8-head-numbers.md) |
| tall | 72 | plan | so the head runs z ±36 about its own center |
| deep | 60 | plan | `#headD` = `#torsoD * 5 / 4`, so the underside plan is 72 × 60 and it hangs 6 over each face |
| socket center | z = −45.05 | derived | `36 + #collarL − #grip` below the head center |
| collar rim, the part's lowest point | z = −47.0 | derived | `36 + #collarL`. The mouth is in this face |
| socket collar Ø | 18.0 | derived | `2 × (6.0 + 3.0)` — [`ball-and-socket.md`](ball-and-socket.md) owns it |
| socket collar length | 9.0 | derived | `#collar` = `#ball / 2 + #wall`, the neck ball's center to the collar's root |
| socket collar, proud | 12.2205 | derived | `#collar + #grip`, the rim to the underside, where `#collar` is `#stand` = 10 |
| relief slits | 4 × 1.6, 4.9465 deep | plan | cut down from the collar's top face to `#ball / 4` below the ball's center, leaving a 6.0 floor |
| socket cavity r | 6.8 | derived | `#ballD`/2 + `#fit`, inside the collar |
| shell thickness | 1.2 | run 3 | **not built, and never has been.** Three perimeters at a 0.4 mm nozzle. Whether the head is shelled at all is undecided |
| eyes | 16 × 8 ellipses at x = ±12, z = +8, the major across, **no pupils** | plan | `#eyeX`, `#eyeUp`, `#eyeRx`, `#eyeRy`. The eye stands 3 proud; the mouth cuts 3 in |
| mouth | 40 × 10 slot, r5 ends | plan | `MOUTH_W`, `MOUTH_H`; its top edge sits 13 below the head center |

**The depth is driven, and that is a requirement rather than an observation.** `#headD` is written
against `#torsoD` and is never typed, so the head follows the body's depth and keeps its 6 mm
overhang each side by construction. The half-size robot had a head 63 deep against a body 48 —
[`../runs/2026-08-25-draft9p1/a8-head-numbers.md`](../runs/2026-08-25-draft9p1/a8-head-numbers.md)
untangles where that came from — and a typed depth is how the two stop tracking each other.
[`../runs/2026-08-25-draft9p1/register.md`](../runs/2026-08-25-draft9p1/register.md) asked whether
the rule was the right one; the user settled it on 2026-08-27.

**The face has a home now, and it did not before.** Until the head doubled, the eyes and the mouth
existed only as literals inside the drawing code, which is exactly the way a number gets left
behind when everything around it grows. They are variables in `make_plans.py` today, written
against `#headW` so they follow it. Build to those. Run 3 built a different face — 10 × 7 ellipses
at z = +6 and a 20 × 4 slot at z = −6 on the half-size head — and that disagreement was never a
decision, so do not read it across.

Model the head about its own center; the assembly places it. Run 4 seats it on the neck ball and
measures where it lands, so these are results rather than targets:

| Station | Global z | Where it comes from |
| ------- | -------- | ------------------- |
| collar rim | +56.05 | ball center less `#grip` — the lowest point of the part |
| head underside | +67.00 | the ball center plus `#collarL`; the collar stands between the two |
| head center | +103.00 | the underside plus half of 72 |
| top of the head | +139.00 | and the ground falls at −178, so the figure is **317.00** tall |

`make_plans.py` computes all four and that file settles any disagreement. The collar stands
12.2205 between the rim and the underside where the bored socket runs 3 to 5 built stood only its
recess, so the underside is at +68.00 rather than +58.05 and the top of the head at +140.00 rather
than +130.05. Nothing below the neck moved.

**The underside is placed off the ball's center, not off the rim**, which is what makes the figure
317.00 rather than 317.05 and keeps it there when the fit changes. A rim moves with `#grip` and
`#grip` moves with the printer's clearance; the ball's center does not move at all. Settled
2026-08-27 — [`ball-and-socket.md`](ball-and-socket.md) owns the rule.

r1 aimed the half-size head's center at +48 and its top at +66 to make that figure exactly 150.
Both numbers are gone: the stations are stacked now and the total is whatever they add up to. Do
not adjust anything to recover a round figure — that 317.00 is round is a coincidence of where
the collar's root landed, and nothing was tuned to reach it.

**The collar rows come from [`ball-and-socket.md`](ball-and-socket.md) and are not this brief's to
change.** The head is the sixth part to carry that socket and it carries it unaltered: same Ø15.6,
same 12.2205 proud, same four 1.6 slits. What is
different here is only which way up it faces — see step 7.

Between run 3 and run 5 this brief said the opposite, and the reasoning is worth keeping because
it is the shape of a mistake that can recur. The head needed a boss on its underside for the
neck's tilt; once the boss was there, boring the socket into its face was the obvious next step;
and the brief then wrote down the consequences of that — a 2.6 mm rim, no free tab length, no
slits — as if they were requirements. **They were consequences.** The boss and the collar were
never compared; one displaced the other.

Build with the **head center on the origin** and report the global stations separately. The head
is placed in the assembly; modeling it around its own center keeps the sketch dimensions
readable.

## The neck is a tilt problem, and the collar is what buys the clearance

The head does not lose its neck travel in the joint. It loses it to its own underside meeting the
torso's top face:

- The head's underside is 72 × 60, so its far corner is **46.86 mm** from the neck axis.
- The ball joint itself is good for **±41.76°** — `BALL_SWING` in `make_plans.py`, set by the
  mouth rim meeting the stalk and by nothing on this part. It was ±37.09° before the robot doubled
  and ±31.86° at draft9p0, which kept `#grip` while everything else grew; A2 tightened `#fit` to
  0.08, `#grip` fell to 1.9465, and the swing came back with more than it started with. Task #159
  later took the wall to 1.8 mm and `#grip` to 2.2205.
- Whatever stands between the head's underside and the torso's top face is the whole budget.

**The collar is 12.2205 mm of that standing between them, where the boss was 2.0.** The head's
socket
center sits `#grip` = 2.2205 inside its mouth face, and the ball center stands `#stand` = 10 off
the torso's top face, so with the socket bored flush the underside cleared the torso by

    #stand − #grip + recess = 10 − 2.2205 + 2.0 = 9.78

and with the collar it clears by `#stand + #collarL` = **20.0**. That is the change: the head's
underside goes from +58.05 to +67.00 and the gap it swings in nearly doubles.

### What that is worth in degrees is not settled

Under the two-flat-plates model this brief has always used, `asin(clearance / 46.86)` goes from
**12.4°** to **24.0°**. Take that as the comparison, not as the answer.

**And note which way doubling moved it.** The clearance and the corner both doubled, so this angle
should have come out unchanged at 11.4° and 23.0°. It came out larger, because `#grip` is
subtracted from the clearance and it did not double: 1.35 became 1.9465 rather than 2.7. The neck
of the big robot tilts **more** than the neck of the small one. draft9p0 had this the other way
round, at 10.3° and 21.8°, because `#grip` was 3.6 there.

**The two-plates model is wrong here, and nobody has replaced it.** The torso's top face is
72 × 48 and the head's underside is 72 × 60, so the head's fore-and-aft corners hang 6 mm past the
torso's edge and never meet that face at all — they swing down its back instead, where what stops
them is the torso's back face. Working the real limit needs the joint driven in the assembly, and
[`../runs/2026-08-13-run5/register.md`](../runs/2026-08-13-run5/register.md) lists joint ranges
under **Never attempted** for the whole robot. Report the angle you can drive the assembly to, and
say which face stopped it.

**Chamfer the collar rim.** Once contact is rim-on-face rather than plate-on-plate, a small area
carries the stop.

The four ways to buy more, none of them chosen: accept what the collar gives, chamfer or round the
underside corners hard, make the head's underside plan smaller than 72 × 60, or lengthen `#stand`
— which costs the same millimeter at every other joint in the figure.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Sketch the profile on the Front plane** — arcs and lines, **tangent throughout**, symmetric
   about the vertical axis. 72 across. Report whether Onshape's **Tangent** constraint holds the
   chain when you drag it, or whether the sketch is only tangent-looking.
2. **Extrude** it symmetric about the plane, **New**. Name the part `Head`.
3. **Fillet** the edges the profile could not round.
4. **Eyes**: two **ellipses** on the front face, held **Equal** to each other and **Symmetric**
   about the head's centerline. Extrude them **proud**, Add. Report what Onshape's ellipse tool
   asks for and in what order.
5. **Mouth**: a **Slot** across the face, extrude **Remove**.
6. **Neck socket collar**: a Ø15.6 circle on the underside, centered on the neck axis, extruded
   **12.2205 proud**, Add. There is no recess and no boss — the underside is flat and the collar
   stands on it. Build it per [`ball-and-socket.md`](ball-and-socket.md), which owns every number
   in it.
7. **The cavity, and which way up.** Material sits **above** the mouth face here, because the head
   sits on top of the ball and the ball enters from below. **This is the joint's other
   orientation**: read that brief's warning about upside-down sockets and work out which way up you
   need before you cut anything. The mouth is in the collar's end face at z = −47.0, and the
   cavity center is 2.2205 above it.
8. **Four relief slits**, 1.6 wide, cut 8.0 through the collar wall and leaving a 3.0 floor, so the
   mouth can open. **The collar is upside down here**, so the slits are cut from the end nearest
   the head's body, not from the rim — read that brief's step 6 with this part's orientation in
   hand. The slit's inner end must sit inside the mouth radius or the mouth never opens — that
   brief's *four arcs* check is what proves it, and it is the check run 1 failed with slits it
   later called "decorative".
9. **Shell** last, thickness 1.2, **opening the back face** (y = +30). Not the underside.

### Why the shell opens the back

Run 3 tried the underside four ways and every one failed with *"Could not shell part with
selections"* — at 1.2 and at 0.9, with and without the boss face, and with the socket suppressed.
Its diagnosis was topological: the recess removed the whole underside **except** the Ø12 boss, so
handing that face to Shell left the wall growing inward from the boss with no material path to the
side walls.

**That diagnosis was made against a part this brief no longer describes.** The recess is gone and
the underside is now one flat face with a collar standing on it, so whether Shell would take the
underside now is untested. Do not assume either way.

**Open the back.** That is the path run 3 proved, it keeps a floor under the collar, it still
prints without support, and it faces the opening away from the viewer. If you try the underside,
say what happened.

**Shell goes last, and that is a rule, not a preference.** Shell measures its wall from whatever
faces exist at the moment it runs, so any cut made after it eats that wall silently — with no
error. Run 3 moved Shell before the boss and all 20 features stayed green while the floor thinned
to **0.200 mm** and the socket broke clean through it into the head. Nothing goes red. That is the
whole problem.

## Acceptance checks

Measure these. Do not infer them.

- **Parts (1)** at the end. Two parts means the socket or the collar came out separate.
- **72.000 across, and 60.000 deep.**
- **The head body is 72.000 tall**, so the box above the collar runs z ±36.000 about the head
  center. The whole part is **82.947** tall, −46.947 to +36.000, because the collar hangs below.
- **The socket center is 45.000 below the head center.** That is the one number the assembly needs
  from this part, because seating the head means putting that point on the neck ball. It is
  `36 + #collar`, and it is a whole number because the collar's root is placed off the ball's
  center. Placed, the top of the head lands at **+139.00** and the figure comes out **317.00** tall.
- **The collar stands 10.947 proud**, measured as the z-extent from the underside to the rim, and
  its outside is **Ø15.600**.
- **The rim is four arcs, not a circle** — the check that the slits actually opened the mouth.
  Measure one arc's included angle; four equal arcs separated by four 1.6 gaps.
- **The slits are 4.947 deep and leave a 6.000 floor.** Measure the z-extent of a slit's cut face
  and the material left beyond it. A Remove extrude can arrive with `oppositeDirection` set and put
  half the cut into empty air with every feature still green.
- **Socket mouth Ø11.520**.
- **The cavity center sits 2.2205 above the rim plane**, not below it. This is the check that
  catches a socket built the wrong way up, and this head's socket is the wrong way up **on
  purpose**, so state the sign you expect *before* you measure. It used to be written as a volume
  — cavity 1132.65 mm³ against a wrong-way-up 184.44, which are the two pieces the rim plane cuts a
  r6.8 sphere into. Those are still the right figures for the region, but **the four slits open
  the cavity to the outside, so it is no longer an enclosed volume anything can measure.** Two
  numbers off `bodydetails` — the cavity sphere's origin and the part's `lowZ` — say the same
  thing and survive the slits.
- **Shell thickness 1.200** at three places, one of them next to a cut. Run 3 measured 1.200 at
  the floor, the front wall, the mouth floor, both eye faces, both sides, the top arc, the outline
  rounds and the socket dome — so anything that is not 1.200 is a real finding.
- **The profile is tangent throughout** — no crease where an arc meets a line. Look at the
  rendered image as well as the constraints.
- **Thinnest wall anywhere in the part**, and where it is. A throttled `featurescript` is not a
  reason to skip this one — see *Measuring* in [`onshape-gui-howto.md`](../../onshape-gui-howto.md)
  for the ways to take it without one. Report the close approaches that turn out to be a slit or a
  step as well, because a search that only reports thicknesses cannot be checked.

## Open questions to report on

The eyes and mouth have sizes, and Shell survives the cavity — on the half-size head it offset the
sphere outward to r 4.400 and left the cup as a 1.2 mm dome. Both from run 3; at this size the
offset lands at r 8.000 and the dome is still 1.2, because the wall does not scale.

**The collar closed two of the three questions that were open here.** The socket now has the same
four relief slits every other socket has, so there is no longer a head-only rigid cup; and the
0.400 mm annular ring measured on the half-size head is gone with the boss that caused it, because
shelling a flat underside leaves no step for a ring to form in. Neither was fixed on its own
terms — both were consequences of the boss, and they went when it did.

What is still open:

- **Nothing has tested whether a ball goes into any socket on this robot**, this one included.
  Onshape solves rigid bodies, so a mate closes whether or not a real ball would pass the mouth.
  Report whether you can seat a ball in the model's own geometry, and say plainly if you cannot.
  This is not a head problem; it is on every socketed part.
- **The neck's real tilt limit.** The two-flat-plates model gives 21.8° and is wrong, because the
  head's underside is 6 mm deeper fore-and-aft than the torso's top face and its corners swing past
  that face rather than onto it. Drive the joint in the assembly, report the angle, and name the
  face that stopped it.
- **Whether Shell will now take the underside.** Run 3's four failures were diagnosed against the
  recess, which no longer exists. Untested either way.

## Recommended steps

**The feature order to build, and the name each feature carries.** Variables are not in the
table: each is added immediately above the first feature that reads it, which
[`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *Phase A* works
out. The verification is in that plan's § *The verification loop*.

| Step | Feature | Name |
| ---: | ------- | ---- |
| 1 | `newSketch` | `head profile` |
| 2 | `extrude` | `head body` |
| 3 | `fillet` | `upper rounds` |
| 4 | `chamfer` | `lower head chamfer` |
| 5 | `newSketch` | `eye profile` |
| 6 | `extrude` | `eye` |
| 7 | `mirror` | `second eye` |
| 8 | `newSketch` | `mouth profile` |
| 9 | `extrude` | `mouth` |
| 10 | `mateConnector` | `socket mount point` |
| 11 | `importDerived` | `get socket` |
| 12 | `transform` | `drop socket to neck` |
| 13 | `booleanBodies` | `add socket to head` |
| 14 | `mateConnector` | `head mate` |
