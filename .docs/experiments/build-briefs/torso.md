# Build brief — the torso

Read [`README.md`](README.md) first: deliverables, coordinate frame, and the settled Ø24 rule.

**This brief has never been gated or built from, and it was written without review.** Where a
number is marked `proposed` nobody has checked it. Build to it, measure what you get, and say
where the brief was guessing.

**Every size here doubled for draft9p0, and the arm-versus-torso conclusion has now changed
twice.** The interference between the arm and the torso is a pure 2× — torso, arm and stud all
scaled together — so every *angle* in that analysis is unchanged while every *distance* doubled.
The joint's own swing is the thing that keeps moving: 37.09° at half size, 31.86° at draft9p0 when
`#grip` rose, and **41.76°** now that A2 has tightened `#fit` to 0.08. At 31.86° the joint ran out
of travel before the arm reached the body and the interference was headroom. At 41.76° it does not,
so the section below is a real limit again, and it is the first thing this run should check.

The torso is a box carrying **five ball studs** — neck, two shoulders, two hips. It is the only
part in the robot with a left and a right inside a single part, and that is what it exists to
teach.

## The frames

| Frame | What it shows |
| ----- | ------------- |
| [`images/cad-body-iso.png`](images/cad-body-iso.png) | the torso with its five ball studs and two shoulder bosses |
| [`images/cad-body-front.png`](images/cad-body-front.png) | square on, so the shoulder and hip stations line up |
| [`images/cad-body-section.png`](images/cad-body-section.png) | cut on the Front plane, through the neck and hip studs |

**The reference CAD, not the specification.** [`README.md`](README.md) § *Where the `cad-*.png`
frames came from* names the document, workspace and version each was taken at.

## The idea being tested

**Make the shape its own part, copy the part, let Boolean do the merging.** A ball stud made
with **Add** is already fused into the torso and there is nothing left to copy — which is the
mistake that sends people to the forums. Made with **New**, it is a part: it can be mirrored to
the opposite shoulder, and one **Union** at the end fuses everything.

Every limb is modeled once and inserted twice by the assembly, so nothing about the arms, legs,
grippers or feet is mirrored at all. The torso is the only place a mirror is needed, which makes it
the only place the lesson can be taught.

Two failure modes the build plan already knows about, both worth watching for:

- **A patterned Add that touches nothing fails quietly, per instance.** Onshape reports "Boolean
  failed" without erroring the whole feature, and the instances land as stray separate parts. A
  part count at the end is how you catch it.
- **The seed part counts as one of the tools**, so a patterned part auto-merges with its
  original wherever the two intersect.

## The numbers

| Name | mm | Source | What it is |
| ---- | -- | ------ | ---------- |
| height | 96 | plan | `#torsoH` — **the driver**; every other dimension in the robot is a fraction of it |
| width | 72 | plan | `#torsoW` = `#torsoH * 3/4`, across the shoulders |
| depth | 48 | plan | `#torsoD` = `#torsoH / 2`, front to back |
| ball | 12 | plan | `#ballD` = `#torsoH / 8` — every ball joint on the robot |
| stalk | 6 | plan | `#stalkD` = `#ballD / 2` |
| shoulder half-spacing | 36 | plan | `#shoulderHalf` = `#torsoH * 3/8` — the torso's own side face |
| hip half-spacing | 24 | plan | `#hipHalf` = `#torsoW / 2 − #limbD / 2` — a half-width less a half-limb, so the leg is flush with the side. `#torsoH / 4` gives the same 24 and is the wrong number — [`../runs/2026-08-25-draft9p1/a7-hip-shoulder.md`](../runs/2026-08-25-draft9p1/a7-hip-shoulder.md) |
| stand-off | 10 | r2 | how far a ball center stands off the face it grows from. Set by the collar's sweep: the rim traces a sphere of radius `√(7.8² + 2.2205²)` = 8.110 about the ball, so 10 clears it |
| neck boss | none | derived | the plan asked for a boss on the top face. It cannot buy the tilt it exists for, so it is not built. See below |
| shoulder stud | see below | r2 | **settled.** Not perpendicular to the side face, and not a plain stalk |
| hip stud | plain stalk | r2 | Ø6, standing 10 off the bottom face. A recess into the torso was considered and dropped: it buys no swing, because the 41.76° limit is set inside the socket by the mouth rim meeting the stalk |

Build with the **torso centered on the origin**, which is also the robot's global origin. That
puts the torso's faces at:

| Face | Station |
| ---- | ------- |
| top, and the shoulder station | z = +48 |
| bottom, and the hip station | z = −48 |
| sides, where the shoulder studs root | x = ±36 |

**Three joint centers land exactly on the torso's own faces** — the neck and the two hips, each a
stalk standing 10 off the face it grows from. The torso is the part that sets everything else, and
the figure's height is whatever those stations add up to: **317.00 mm**, printed by the plan
rather than aimed at. r1 set 150 as a target and fitted the stations to it; every revision since
stacks them and reports the sum. **That it is round now is a coincidence and not a target** — it
came out at 317.05 until draft9p1p1 placed the head's underside off the neck ball's center. Do not
adjust anything to hold it there, and note that it is not a doubling of the 158.15 the same stack
gave at half the size either, because the joint keeps its own numbers.

The shoulders are the exception, and they are not on a face.

## The shoulder stud — settled in r2, and none of it is obvious

The stud does **not** leave the side face square, and it is not all one diameter.

| | |
| --- | --- |
| direction | **53° below horizontal, 30° toward the front** |
| length | **26 mm** from the side face to the ball center, along that axis |
| roots at | **8 mm below the torso's top face**, on the side face at x = ±36 |
| first 16 mm | **Ø16 boss**, coaxial with the stalk |
| last 10 mm | **Ø6 stalk**, then the Ø12 ball |
| ball ends up | **13.551 out** from the side face and **20.765 below** the root |

Three things about it are worth more than the numbers:

- **The boss is coaxial with the stalk, not normal to the side face.** This is the whole trick. A
  boss square to the face hangs below the ball, so the arm hits it on the way in — measured worse
  than no boss at all. Everything a coaxial boss occupies sits *behind* the ball along the stud
  axis, and the socket only ever reaches forward of that, so it cannot cost a degree of swing.
- **The boss is cut off flush where it crosses the torso's top face.** Leaving a vertical face at
  this angle it traces an ellipse 3.66 mm tall for every mm of radius, which runs past the top of
  a 96 mm torso. Cutting it there takes only the part that was never in the arm's way — which is
  what lets the boss be as fat as it needs to be without the shoulder growing a horn.
- **26 mm is set by the torso, not by the joint.** The arm is a Ø24 rod, not a line. With the ball
  standing the usual 10 clear, the rod fouled the torso through the first 12.19° of its travel. At
  26 the ball stands 13.551 clear and the arm is free at rest — **1.551 mm** at the zero pose,
  reading the arm as a plain Ø24 rod.
- **The arc is not free, and the reason is A2 rather than the doubling.** Torso, arm and stud all
  doubled together, so the angle at which the arm's far end first crosses the torso is unchanged at
  **33.38°**. The joint's own limit went 37.09° → 31.86° when `#grip` rose, and → **41.76°** when
  A2 tightened `#fit`. At 31.86° the joint ran out of travel 1.52° short of the body and the
  interference did not occur; at 41.76° it reaches **8.38° past** it, so what stops the arm is the
  torso. **This is arithmetic on an exact 2×, not a measurement.** Take the swept-cone check below
  rather than trusting it, and report which face the arm lands on.

**No run has built this yet.** Runs 3 and 4 both carry a plain Ø3 stalk leaving the side face
square, ball center measured at (±23, 0, +24) on the half-size robot — the shoulder this section
was written to replace.
The run 4 assembly stands up fine on it, because at zero pose the arm points straight out and
touches nothing; what it cannot do is swing. Build the stud above and the difference will show up
in the one check below.

Build it, then **measure the least clearance between the arm and the torso across the swing** and
report it. That is the check this geometry exists to pass.

## Geometry, stated once so it cannot be read two ways

- **Neck stud**: on the top face, on the axis, growing **upward**. The head's socket comes down
  over it, so the ball enters that socket from below.
- **Shoulder studs**: rooted on the side faces at x = ±36, **8 mm below the top**, growing
  **down and forward** along the 53°/30° axis above — not outward, and not on a face station.
- **Hip studs**: on the bottom face at x = ±24, growing **downward**.
- Four of the five are the same stalk-and-ball profile at a different station. **The shoulders are
  not** — they carry the Ø16 boss and they leave at an angle, so they are their own feature. Model
  one shoulder and mirror it; model one of the others and repeat its profile.
- The torso carries **all five**, left and right. Only the *limbs* are modeled once and copied by
  the assembly; a printed torso needs both shoulders and both hips on it.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Sketch the torso** on the Top plane: 72 × 48, centered, and extrude symmetric 96, **New**.
   Name it `Torso`. Report whether you dimensioned it or used **Symmetric** — the plan makes a
   point of the torso being centered rather than cornered.
2. **Fillet** the vertical edges if the sheets show them rounded. Say what you found on the
   sheet rather than choosing.
3. **One ball stud** at the **hip**, not the shoulder: a stalk-and-ball profile on the joint
   point, the join between stalk and ball found by **constraint** rather than dimensioned, then
   **Revolve, New**. See [`ball-and-socket.md`](ball-and-socket.md) — the stud half is the same
   part. Start at the hip because it is the plain case; the shoulder is the awkward one.
4. **Mirror the stud part** to the opposite hip. Mirror the *part*, not the feature.
5. **Repeat the profile for the neck.**
6. **The shoulder**, which needs an axis before it needs a sketch. Build the 53°/30° direction as
   real geometry — a mate connector or a plane rotated twice — then put the Ø16 boss, the Ø6 stalk
   and the ball on that axis, coaxial, 26 mm out from the side face. Mirror the part.
7. **Cut the boss flush** where it crosses the torso's top face. A single Extrude Remove up from
   z = +48 takes both shoulders at once.
8. **One Boolean → Union** at the end, torso plus all five studs.
7. Rename every feature and part, and check.

## Acceptance checks

Measure these. Do not infer them.

- **Parts (1)** at the end. Any stray part is a Boolean that touched nothing — see above.
- **72.000 × 48.000 × 96.000** off the bounding box, before the studs are added.
- **Five balls, each Ø12.000.** Measure all five, not one: a mirror can land a part correctly and
  still fail to union.
- **Ball centers at their stations**, measured off the model. Hips at x = ±24, z = −58; neck on
  the axis at z = +58. **Shoulders at x = ±49.551, z = +19.235, y = −7.824** — that is the root at
  (±36, 0, +40) plus 26 mm along the 53°/30° axis, and the y is the reason the arm plane sits
  forward. Report the actual coordinates rather than confirming the expected ones.
- **The shoulder boss is cut flush at z = +48** and nothing stands proud of the top face.
- **Least clearance between a Ø24 arm and the torso, across the whole swing.** Expect **+1.551 mm**
  at the zero pose, and **contact inside the cone**, because the joint reaches 41.76° and the arm
  crosses the body at 33.38°. Report the least clearance, the angle it occurs at, and the angle
  contact begins. This is the check the 26 mm stud length exists to pass,
  and it is the only one here that can fail while every dimension measures correctly.
- **The part is symmetric about the YZ plane.** Mirror it about YZ in a scratch feature and
  confirm it lands on itself. This is the one part in the robot where that check can fail.
- **Thinnest wall anywhere in the part**, and where it is.
- **Every mate connector sits on the geometry it is named for**, and open each one to see how it
  got there. A connector placed **On entity → Origin** with a typed **Move** is a coordinate that
  was correct when it was typed; it does not follow the stud when a feature above it moves, and it
  keeps reading as usable after it has gone stale. Report the origin entity and the offset for
  each, not just the position — a connector at the right station by arithmetic passes a position
  check and still fails this one. Separate the connectors that other features are built on from
  the ones the assembly mates to, because the first kind cannot be deleted.

## Open questions to report on

The three that used to be here — the stand-off, the boss diameter and protrusion, and whether the
shoulder stud lines up with the arm — were all settled by r2 and are stated above. The stand-off
is 10 everywhere and it is *in* the height sum, which is part of why the figure comes out where it
does rather than at a number anyone chose. What is still open:

- **The arm does not follow the stud forward.** It hangs in a plane parallel to the front plane,
  7.82 mm forward of center, which is what makes the front elevation read true length. The ball
  takes up the difference — 17.51° of the 41.76° it allows, an angle that has never scaled while
  the swing moved twice. That leaves **24.25°** of swing in the fore-and-aft direction, against
  19.58° on the 1× robot and 14.35° at draft9p0, and the full arc in the drawn plane. Nothing has
  checked whether a student can tell those two apart when posing the robot.
- **The neck boss cannot buy the tilt it was asked for, so it is not built.** The head's 42°
  assumed two boss faces 8 mm apart. Put a boss of height `h` on the torso's top face and the
  spacing becomes `#stand − #grip − h` = `6.4 − h`, which gets *smaller*, never 8. Worse, the
  contact that actually binds is not the boss pair at all: it is the head's outer underside, which
  sits 8.4 above the top face at a radius of 46.86 and touches at **10.3°**. Doubling should have
  left that angle alone — both lengths in it grew — and it did not, because `#grip` is subtracted
  from the clearance and `#grip` grew faster. A boss moves neither of those two surfaces, so the
  10.3° stands whether it is there or not. The argument goes away; the neck stays a plain stalk.
  The height at which the boss pair would start binding first was 2.47 on the 1× robot and **has
  not been recomputed** for the new `#grip`; it does not need to be while no boss is built. See
  [`head.md`](head.md).
- **Cutting the boss flush at the top face leaves an elliptical scar** on the torso's top. It is
  29.28 mm tall for a Ø16 boss, on a top face 72 × 48. Nobody has looked at whether that reads as
  deliberate or as a mistake, and it is the first thing anyone will see — and it is now a scar
  covering rather more of the face than it did.

## Recommended steps

**The feature order to build, and the name each feature carries.** Variables are not in the
table: each is added immediately above the first feature that reads it, which
[`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *Phase A* works
out. The verification is in that plan's § *The verification loop*.

| Step | Feature | Name |
| ---: | ------- | ---- |
| 1 | `newSketch` | `torso outline` |
| 2 | `extrude` | `torso block` |
| 3 | `newSketch` | `pivot lines` |
| 4 | `cPlane` | `plane for shoulder` |
| 5 | `newSketch` | `torso shoulder profile` |
| 6 | `revolve` | `shoulder` |
| 7 | `mateConnector` | `mate for shoulder stud` |
| 8 | `mirror` | `mirror shoulder` |
| 9 | `newSketch` | `trim shoulder pattern` |
| 10 | `extrude` | `trim shoulder cut` |
| 11 | `newSketch` | `hip stud location` |
| 12 | `mateConnector` | `mate for hip stud` |
| 13 | `newSketch` | `neck stud location` |
| 14 | `mateConnector` | `mate for neck stud` |
| 15 | `importDerived` | `copy ball stud` |
| 16 | `transform` | `move neck stud` |
| 17 | `transform` | `copy for hip` |
| 18 | `transform` | `copy for shoulder` |
| 19 | `mirror` | `duplicate shoulder and hip` |
| 20 | `booleanBodies` | `add neck to body` |
| 21 | `mateConnector` | `neck` |
| 22 | `mateConnector` | `left shoulder` |
| 23 | `mateConnector` | `right shoulder` |
| 24 | `mateConnector` | `left hip` |
| 25 | `mateConnector` | `right hip` |

**All eight connectors are renamed.** The names above are the settled ones; the old ones are in
[`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *The names to build
under*.
