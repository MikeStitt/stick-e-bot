# 14. One leg, then the other by copy

Starts from a robot with two arms. Ends with a whole robot that moves.

**The leg is copied differently from the arm, and the difference is the lesson.** The arm was
placed a piece at a time and copied once it was whole. The leg starts from a limb pair that is
*already mated to itself*, so the copy carries a working joint into the assembly before anything
else happens, and only the foot and the hip are new.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.assembly.copy_limb_pair` | select the upper and lower limbs of an arm; copy; paste | two instances, and the elbow's revolute mate carried with them — it becomes a knee |
| `cad.assembly.place_foot` | insert a foot from the workspace | one instance |
| `cad.assembly.mate_ankle` | ball mate, foot to the lower limb's `wrist end` | `left ankle` |
| `cad.assembly.mate_hip` | ball mate, upper limb's `shoulder end` to the torso's `left hip` | `left hip` |
| `cad.assembly.copy_leg` | select the upper limb, the lower limb and the foot; copy; paste | three instances, and the knee and ankle mates carried with them |
| `cad.assembly.mate_hip_2` | ball mate, the new upper limb to the torso's `right hip` | `right hip` |

**Both copies here arrive named for the arm they came from**, and the reference carries them as
`left knee`, `right knee` and `right ankle`. [`13-assembly-arms.md`](13-assembly-arms.md) says why
renaming is part of the paste step.

**The same limb parts do both jobs.** A limb's ends are called `shoulder end` and `elbow end`
because that is where they were first used; in a leg the same connectors serve the hip and the
knee. Nothing about the part changes, and saying that plainly is cheaper than renaming anything.

**By the end, more mates in the robot arrived by copy than were placed by hand.** The elbow and
wrist on the second arm, and the knee on both legs and the ankle on the second, were never
picked by anybody.

**The assembly is saved at rest**, every ball with its stalk on the socket's own axis and every
revolute straight. Pose it for the hero frames and undo the pose before the version is published.
draft9p0 was saved posed, and its foot centers read x +26.05 and −31.42 — numbers that describe the
last drag rather than the robot. At rest the feet are at x ±24, each sole centered on its own
leg, and their inner edges meet at x 0.

## The shots this tutorial needs by name

### The copies

Both copies get the before-and-after treatment from
[`13-assembly-arms.md`](13-assembly-arms.md) — instance list, mate list, graphics area, each side
of the paste. Beyond that:

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the copied limb pair, floating, still bent at the knee | the frame that says the joint came with it | |
| the same pair dragged at the knee, before it is mated to anything | proof, not assertion, that the carried mate works | |
| the pair as it arrives against the pair as it ends up | it arrives in the arm's orientation and the hip mate turns it | |

**The floating-but-jointed pair is the frame this whole tutorial is built around.** Two parts, not
attached to the robot, hinged to each other, and nobody made that hinge.

### The mates

The two-frame rule as before. The hip connectors are the same five ball centers as
[`06-torso-joints.md`](06-torso-joints.md), and by now the medium view is the whole robot, which
is what makes *which* hip answerable.

### The end

| Shot | Why |
| ---- | --- |
| the finished robot | the hero of the entire guide |
| the robot in two or three poses | the reason for building it |
| the mate list, whole | thirteen mates, and where each came from |
| the version dialog | the version the printed robot is made from |

## Manipulating joints

**The lesson plan asks for a tutorial or two here on how to move the joints, and does not say what
is in them.** That is honest — nobody has looked yet. What is unknown:

- what dragging a ball mate looks like, and whether it can be captured as a sequence
- what the degrees-of-freedom display shows, and whether it is legible in a frame
- whether mate limits are worth teaching at all on this robot
- whether posing is a tutorial or the last section of this one

**This is not a "shoot generously" case.** It is a question to answer before it can be planned:
somebody has to open the assembly and drag things before there is anything to write down.

## What we do not know yet

**Whether copying a limb pair carries the shoulder mate.** It should not, because the torso is not
in the selection. If it does, the pasted pair arrives attached to a shoulder and has to be
detached, which is a different lesson and a worse one.

**Whether a leg copied from an arm needs turning.** The arm points outward and the leg points
down. If the ball mate at the hip does not turn it, something else has to, and that step does not
exist in this plan yet.

**Whether the robot stands.** Two feet, a fixed torso and nine ball mates is a lot of freedom.
Whether the assembly holds a pose or collapses is the first thing to find out, and it is the same
question the print asks in [task #29](../../robot-build-plan.md).
