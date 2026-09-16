# Launch gate — run 3, wave 4: the assembly

Performed against [`../../../2026-08-12-launch-gate.md`](../../../2026-08-12-launch-gate.md).

**This gate carries the same structural weakness as wave 3's: I wrote the brief it gates.** What
follows is the mechanical part — links opened, variables traced to the plan's own table,
arithmetic redone from the station list rather than copied. The judgment part is missing and
[`assembly.md`](../../build-briefs/assembly.md) says so at the top.

**One thing this gate cannot do is the thing that matters most.** Every other brief was gated
before anything was built from it. This one is gated before the parts it assembles exist. If a
part comes out of wave 2 or wave 3 different from what its own brief promised, this brief is
wrong in a way no reading of it can reveal.

## Links

Every relative link in [`assembly.md`](../../build-briefs/assembly.md) resolves.

## The instance count, derived rather than copied

From the plan's parts table: torso 1, head 1, and two each of upper arm, forearm, hand, thigh,
shin and foot. That is 14 printed instances of 8 unique parts, which is what the plan says.

**If the limbs collapsed to two unique parts** — the question
[`limbs.md`](../../build-briefs/limbs.md) puts to its builder — the instance count does not
change, but the unique-part count drops to 6 and the bill of materials disagrees with the plan's
table. The brief tells the agent to report both numbers and not reconcile them. Two agents are
building that half of the answer tonight.

## The mates, counted off the joints rather than off the brief

| Joint | Where | Mate |
| ----- | ----- | ---- |
| neck | head to torso | Ball |
| shoulders | upper arm to torso | Ball |
| hips | thigh to torso | Ball |
| wrists | hand to forearm | Ball |
| ankles | foot to shin | Ball |
| elbows | forearm to upper arm | Revolute |
| knees | shin to thigh | Revolute |

Two of each of those except the neck. That gives **9 Ball** and **4 Revolute**, which is what the
brief's table says, and 13 joints, which is what the plan says.

## Arithmetic redone from the station table

| Brief says | Recomputed | |
| ---------- | ---------- | - |
| the robot stands 150 mm | top of head 150 − ground 0 | the station table's own total |
| the arms reach mid-thigh | shoulder 108 − mid thigh 48 = 60, and `2 × #armSeg + #handL` = 60 | the plan derives the hand length from this equality, so it cannot fail unless a part missed its own dimension |
| the wrist sits at hip height | wrist 60, hip 60 | falls out of the same relation |
| the feet sit 4 mm outboard of the shins | `#footHalf` 16 − `#legX` 12 | both have rows in the plan's table |
| ball swing 78° proud, 42° at the neck | not recomputable here | both are predictions from the plan's tilt working; neither has been measured on anything |

## What this gate found

- **The brief's suggested build order has a step nobody has tried**: make one arm a subassembly,
  then insert the subassembly again for the other side. Whether Onshape will mirror an instance
  or wants a second subassembly is written as an open question, which is the right place for it.
- **The Width mate has no count in the mates table** — it says "per hinge", which is 4. That is
  correct but it reads as vaguer than it is. Left alone; the brief's point is that a Width mate is
  not optional decoration, and a number would not carry that.
- **The detent cannot be tested here and the brief says so.** In CAD a revolute mate turns freely.
  Run 3's hinge build makes this sharper than the brief knew: the land between valleys measured
  0.053 mm, so the click is in question on a printer as well as absent in CAD. See
  [`decisions-waiting.md`](decisions-waiting.md).

## What is deliberately left open

The brief carries these rather than resolving them, because resolving them is a design decision:

- the stand-off at the shoulder and hip
- whether the feet's 4 mm outboard offset is absorbed as a permanent lean at the ankles
- whether the bill of materials should say 6 unique parts or 8
