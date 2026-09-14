# A11 — one rest pose, and a width mate since withdrawn

Three things the assembly needed, and two of them turn out to be the same thing.

## The width mate is withdrawn

**The requirement is withdrawn and the rest of this section is the case that was made for it.** A
Revolute leaves one rotation and nothing else, so no blade can slide in its fork. B9 counted the
assembly's degrees of freedom and [`register.md`](register.md) carries the arithmetic.

All four hinges in draft9p0 are a bare Revolute, so every lower limb can slide sideways in its
fork: 0.6 mm of clearance each side, which means the blade's detent bumps do not line up with the
ear's valleys and an arm can be pushed off center by hand.

`assembly.md` has always been explicit — *"A Width mate is not optional decoration on a hinge"* —
and neither `13-assembly-arms.md` nor `14-assembly-legs.md` had a width step in its table. The
build followed the step tables. **Two sources wanted it and the one that drives the tutorial did
not**, which is the same shape of failure as the gripper's mouth in A10.

**It goes in at the first elbow and rides the copies.** Tutorial 13 copies the upper limb, the
lower limb and the gripper to make the second arm, carrying the elbow and wrist mates; tutorial 14
copies a limb pair to make each leg, carrying the elbow mate as a knee. So one width mate picked
from a menu becomes four, which is the argument both tutorials are already making about their
copies — and it costs one step and one pair of frames.

## The rest pose is every mate at zero

**A posed assembly cannot be measured, and draft9p0 was saved posed.** Its foot centers came back
at x +26.05 and −31.42. That is not an asymmetric robot; it is the last drag. Every joint below the
hip is a free Ball or a free Revolute, so the feet are wherever they were left. The same mistake
reached the standing height once already: a bounding box of the posed robot read 431.97, because
both feet were tilted and a tilted 96 × 48 sole puts a corner lower than its own ball center by
more than the foot is deep.

**So the check needed a pose before it could be run at all,** and the pose is the plainest one:
every ball with its stalk on the socket's own axis, every revolute straight. At rest the assembly's
stations are the plan sheet's stations, which is what makes the sheet something to check against.

| | at rest |
| --- | --- |
| hips | z −58, x ±24 |
| knees | z −106 |
| ankles | z −154, x ±24 |
| foot centers | x ±32 |
| sole | z −178 |
| neck ball | z +58 |
| top of the head | z +139.05 |

**The sheet draws one thing out of the rest pose and says so.** The elbows are bent 45° so the
figure reads as a robot rather than a diagram. At rest they are straight and each arm lies along
its own shoulder stud, 33.13° from vertical. The assembly is saved at rest; posing is something you
do for the hero frames and then undo.

## The feet were never asymmetric

`FOOT_X` is `LEG_X + #foot_h / 3`, so each foot sits 8 outboard of its shin — and the offset is in
the part, not in the pose: the foot's ball is 8 inboard of the foot's own center. At rest both feet
are at x ±32 and their inner edges at ±8, a 16 mm gap.

**Nothing decided that gap and nothing went wrong.** It is the half-size robot's 4 mm doubled,
which is what a driving dimension is supposed to do. The register's *"the feet no longer touch, and
nobody decided that"* is right that nobody decided it and wrong to read it as a change: the stance
is proportionally identical at both sizes.

## Found while reading: A2's numbers never left `ball and socket`

A2 tightened `#fit` to 0.08, which moved `#grip` from 3.6 to 1.9465 and the cavity from 6.8 to
6.08. Three numbers downstream of that are still the draft9p0 ones in five documents:

| | draft9p0 | now |
| --- | --- | --- |
| ball swing, per side | ±31.86° | **±41.76°** |
| the cone | 63.7° | **83.5°** |
| standing height | 315.4 | **317.05** |
| top of the head | +137.4 | **+139.05** |

**The swing went up, past the point the arm clears the torso.** `torso.md` argues the shoulder no
longer interferes, on 1.52° of margin: the arm's far end first crosses the body at 33.38° and the
joint stopped at 31.86°. It now stops at 41.76°, which is 8.4° *past* that, so the margin is gone
and what limits the arm is the torso rather than the socket. The claim is withdrawn in
`assembly.md` and the check becomes the interesting one on the list.

**`ball-and-socket.md` has the swing at ±41.33° and the formula it cites gives ±41.76°.** It writes
`acos(grip / cavity) − 30°`, and the 30 is `asin(#stalk / 2 / #cavity)` rounded — that term is
29.57° at `#cavity` 6.08 and would be exactly 30 only if the cavity were the stalk's diameter. The
two agree at the second decimal by accident of rounding, and the sheet's own derivation is the one
to keep.

`assembly.md` is corrected here, and `head.md`, `torso.md`, `ball-and-socket.md` and
`sketches/README.md` in the commit after it. Two files are left alone on purpose:
`design-into-cad.md` is a completed run's plan whose steps are marked done, and the rows in
`sketches/README.md`'s two tables describe what each published sketch shows rather than what the
design is — republishing those sketches is A12's row.

**`torso.md` also had A7's defect,** writing `#hipHalf = #torsoH / 4` in its numbers table. A7
reached `make_plans.py` and the plan pages and not this brief. Corrected in the same pass.
