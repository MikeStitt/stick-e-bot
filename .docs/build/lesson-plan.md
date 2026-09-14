# The lesson plan — the order the robot is built in

This is the order of the work. What a step's identifier means, and what a step carries, is
[`steps.md`](steps.md); how a step is performed and captured is [`takes.md`](takes.md); what
each part's numbers are and why is [`../robot-build-plan.md`](../robot-build-plan.md). This file
says only what comes first.

**The leaf steps and the shots are in [`plan/`](plan/00-manifest.md)**, one file per tutorial, in
the order this file sets. Which frames have to be named ahead of a run and which the harness makes
on its own is [`shots.md`](shots.md).

Every step here is `state: proposed`. None of it has been performed in this order.

## The move

**The assembly exists before most of the parts do.** The torso box and the head shell are built,
placed in the assembly, and from then on every part is placed as soon as it exists. A student sees
a robot from the third step and watches it gain limbs, rather than building nine parts and
assembling them at the end.

Two things follow. Parts are built in the order the assembly needs them, so `cad.parts` and
`cad.assembly` interleave rather than forming two blocks. And a part is built twice — the head is
built without its socket and gains one later, the body is built as a box and gains shoulders and
studs later — because the joint it needs does not exist yet.

## The order

### The torso and the head

| Identifier | The step |
| ---------- | -------- |
| `cad.variables.studio` | make the Variable Studio, and tick *Insert into all Part Studios and Assemblies* |
| `cad.variables.sizes` | the three the torso is drawn from |
| `cad.parts.body.block` | the torso box, and nothing else |
| `cad.parts.head.shell` | the head, without its socket |
| `cad.assembly.place_body_head` | put both in the assembly |
| `cad.assembly.rename` | name the assembly `stickbot` |
| `cad.assembly.first_tab` | move it to the first tab |

### The ball and socket, and what it lets the torso and head become

| Identifier | The step |
| ---------- | -------- |
| `cad.parts.ball_and_socket.*` | the joint |
| `cad.parts.head.socket` | add the socket to the head |
| `cad.parts.body.shoulders` | add the shoulders to the body |
| `cad.parts.body.studs` | add the ball studs to the body |
| `cad.parts.body.connectors` | a mate connector at the center of each of the five studs |
| `cad.assembly.fix_body` | fix the body in the assembly |
| `cad.assembly.mate_head` | mate the head to the body |

### The remaining parts

| Identifier | The step |
| ---------- | -------- |
| `cad.parts.foot.*` | the foot |
| `cad.parts.hinge.*` | the hinge joint |
| `cad.parts.u_limb.*` | the upper limb |
| `cad.parts.l_limb.*` | the lower limb |
| `cad.parts.gripper.*` | the gripper |

**The gripper's steps are not settled.** Its body is the one part in the robot sized by the
socket rather than by the torso, and its width has to be built to follow the collar's outside
profile instead of being typed and checked afterwards. What has to change and why is in
[`../experiments/build-briefs/gripper.md`](../experiments/build-briefs/gripper.md).

### One arm, then the other by copy

| Identifier | The step |
| ---------- | -------- |
| `cad.assembly.place_arm` | place an upper limb and a lower limb |
| `cad.assembly.mate_shoulder` | mate the upper limb to a shoulder |
| `cad.assembly.mate_elbow` | mate the lower limb to the upper |
| `cad.assembly.place_gripper` | place a gripper |
| `cad.assembly.mate_wrist` | mate the gripper to the lower limb |
| `cad.assembly.copy_arm` | select upper limb, lower limb and gripper; copy; paste |
| `cad.assembly.mate_shoulder_2` | mate the new upper limb to the other shoulder |

### One leg, then the other by copy

| Identifier | The step |
| ---------- | -------- |
| `cad.assembly.copy_limb_pair` | copy a limb pair; paste |
| `cad.assembly.place_foot` | add a foot |
| `cad.assembly.mate_ankle` | mate the foot to the limb pair |
| `cad.assembly.mate_hip` | mate the upper limb to a hip |
| `cad.assembly.copy_leg` | copy the upper limb, lower limb and foot; paste |
| `cad.assembly.mate_hip_2` | mate the new upper limb to the other hip |

**The arm and the leg are copied differently, and the difference is the lesson.** The arm is
placed a piece at a time and copied once it is whole. The leg starts from a limb pair that is
already mated to itself, so the copy carries a working joint into the assembly and only the foot
and the hip are new.

**A copied set of mated parts arrives already mated, and showing that is the point.** So the
detailed operations are written to place and mate as few parts individually as they can: four
parts are placed one at a time — an upper limb, a lower limb, a gripper and a foot — and
everything else arrives by copy, needing only the one mate that attaches it to the torso.

## The tutorial is the coarse unit

**A tutorial starts and ends when the work moves from one Part Studio or the assembly to the
next**, so the order above already draws them and no step needs a field saying which one it is in.
What a tutorial is, and why it did not take the name *step*, is [`steps.md`](steps.md).

**Each joint is one tutorial**: `cad.parts.ball_and_socket` is one and `cad.parts.hinge` is
another. Each is a single Part Studio holding two related parts, and each teaches moving the joint
it just built as well as building it.

## Variable Studios

**The numbers more than one Part Studio reads want a home outside any one of them.** Onshape
variables are scoped to a Part Studio, so `#torsoH`, `#torsoW` and `#torsoD` cannot live in the
body's tree and be read from the head's. A **Variable Studio** is the document-level element that
holds them — what it is and how it behaves, all of it measured rather than read off the help, is
[`../onshape-gui-howto.md`](../onshape-gui-howto.md) §3b.

**It opens the body's tutorial rather than taking one of its own.** A tab created after the
studio's *Insert into all Part Studios and Assemblies* box is ticked inherits the variables, so
building it before the torso means every later tab simply has `#torsoH`, `#torsoW` and `#torsoD`
without anyone doing anything. That is why it can come first, and coming first is the whole of what
it needs; a sitting spent only on a table of numbers would teach less than the same numbers
arriving just before the first thing that uses them.

**The studio arrives holding three rows, not twenty-three.** It takes rows at any point in the
build, so the other twenty are typed in the tutorial that first reads them, and inside that
tutorial at the step that first reads them. What that rule is, and which tutorial types what, is
[`plan/00-manifest.md`](plan/00-manifest.md) § *A variable is typed at the step that first reads
it*.

**It does not break the tab rule.** A tutorial ends when the work moves from one Part Studio or
the assembly to the next, and a Variable Studio is neither, so opening one does not close a
tutorial. This is an initial plan: if the four numbers turn out to need more explaining than the
torso's own tutorial can carry, they can take a tutorial of their own without anything else
moving.

## Geometry a student can see, not numbers they cannot

**`cad.parts.body.shoulders` keeps stickbot's construction geometry.** Pivot lines, a plane
standing on one of them at `#yaw`, the profile drawn on that plane at `#tilt`, then the revolve.
Every link of it is on screen: a student can see where the shoulder's angle comes from and change
it. The short way — a transform carrying typed offsets — hides the same decision inside numbers
nobody can read back.

**Both angles stay visible in four features, not seven.** An earlier reading of stickbot called for
a rotation point, a plane through it and a sketch rotating about z as well. The built model has
none of them: `#yaw` is the angle of `plane for shoulder` and `#tilt` is a dimension in the profile
sketch, so the shorter chain shows the student the same two numbers in the same two places.

**This applies wherever the two compete.** `head`'s *drop socket to neck* carries a typed
`dz = -22.15 mm`, which is the hidden kind. Every other consumer moves its joint with
`TRANSFORM_MATE_CONNECTORS`, onto a connector that is visible in the tree and moves when the part
moves.

## The five mate connectors on the torso

**Each of the torso's five studs — neck, two shoulders, two hips — carries a mate connector at
the ball's center**, placed in the Part Studio rather than in the assembly. The assembly then
mates to a connector that already exists and is named, instead of picking geometry each time.

This is also the repair for the five broken connectors the audit found: they are the same five,
they lost their references to a Boolean, and re-attaching them to the stud centers both fixes them
and takes work out of the assembly. One of the two features named `r shoulder connector` is the
right-hip connector and is renamed with it.

## What this does not decide

**How long a tutorial takes.** The boundaries are implied by the order above, but nothing here
says which of them fill a class hour and which run short.

**The joints do not go in a folder.** They were considered and dropped, so
`cad.parts.ball_and_socket` and `cad.parts.hinge` keep the identifiers they already have and
nothing carries a `was`.

**What the parts are.** The numbers, and the two decisions taken from the audit — `#fit` at 0.02
and the rebalanced hinge as an experiment — are in
[`../2026-08-20-stickbot-audit.md`](../2026-08-20-stickbot-audit.md) and the briefs it points at.
