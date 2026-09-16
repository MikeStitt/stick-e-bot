# A13 — the Variables table at the size the robot is built at

[`../../../robot-build-plan.md`](../../../robot-build-plan.md) is the design source, and its
Variables section described the 48 mm robot. draft9p0 doubled the robot in `make_plans.py` and in
the build briefs and never came back here. A1 renamed one row; this row republishes the rest and
answers the three questions A6, A7 and A10 handed forward.

## What the numbers become

| | was | is |
| --- | --- | --- |
| `#torsoH` | 48 | 96 |
| `#torsoW` | 36 | 72 |
| `#torsoD` | 24 | 48 |
| `#ball` | 6 | 12 |
| `#stalk` | 3 | 6 |
| `#wall` | 1.5 | 3 |
| `#collar` | 5.5 | 11 |
| `#slit` | 0.8 | 1.6 |
| `#stud_len` | 5 | 10 |
| `#slit_in` | 2.5 | 5 |
| `#slit_out` | 6 | 12 |
| `#fit` | 0.2 | 0.08 |
| `#grip` | 1.35 | 1.9465 |

`#limbCenter` is 48 and A1 already put it there. The last two are not doublings: A2 settled `#fit`
at 0.08 and made `#grip` an expression on it.

## The rule decides which side of the table a number is on

The two groups used to be *four that drive the size* and *ten the joint is built from*, which is a
split by what a number is about. A6 replaced that with a split by where a number is read: **a
dimension read by two Part Studios is declared in the Variable Studio.** Applying it to the tab
variables A7 read back off draft9p0 moves six more names up beside `#wall`:

| name | tabs that read it | what it becomes |
| --- | --- | --- |
| `#ball` | `body`, `ball and socket`, `foot`, `gripper` | `#torsoH / 8`, one row |
| `#limbD` | `body`, `hinge`, `u limb`, `l limb` | `#torsoH / 4`, one row |
| `#stand` | `body`, `l limb` | `#ball * 5 / 6`, one row |
| `#collar` | `ball and socket`, `foot` | typed 11, one row |
| `#grip` | `ball and socket`, `foot` | the A2 expression, one row |
| `#fit` | `ball and socket`, and `#grip`'s expression | `**not scaled**`, one row |

**`#stand` is the one A7's read-back could not have found.** Nothing in draft9p0's `l limb` reads
it, because draft9p0 stacked each joint on the end of a full-length rod. A1's correction extrudes
the shin at `#limbCenter - #stand`, which is a second tab reading a number declared in `body`, so
the rule reaches it the moment B7 builds it.

**`#fit` follows `#grip` rather than the rule.** One tab reads it. It goes up because `#grip` is an
expression on it and `#grip` has to resolve in the studio.

**Five stay in `ball and socket`** — `#stalk`, `#slit`, `#stud_len`, `#slit_in`, `#slit_out`.
Nothing outside the joint builds geometry from any of them.

**Which tutorial types each row in is left to the build plan.** Rows go into a Variable Studio at
any point, so this is not the same question as which studio owns them.
[`../../../build/plan/01-torso.md`](../../../build/plan/01-torso.md) keeps its five.

## What the sweep found that was not a doubling

- **`#collar` is typed and has nothing behind it.** 5.5 and 11, with no expression that gives both.
  It is the same failure as A9's `#boss_d`: driving `#torsoH` up grows the ball and leaves the
  collar where it was. No row in this draft settles it, and the table says so.
- **The blade row records the other hinge.** `blade thickness | 3 | #torsoH / 16` gives 6.0 at the
  built size. `make_plans.py` draws 10.0 and draft9p0 built 10.0;
  [`../../build-briefs/hinge.md`](../../build-briefs/hinge.md) carries both in one table and calls
  the row unsettled. The design source had been quietly holding the `stickbot-for-bot-review`
  number the whole time.
- **The ear row was the ear that failed.** `ear thickness | 1.2 | not scaled` — 1.2 is what run 5
  printed and what splayed. The ear is `(#limbD - #slot) / 2`, 6.4. The 1.2 that survives in the
  model is `#tooth_proud`, a detent bump's stand-off, which is a different feature.
- **Hip half-spacing and leg centerline were two rows for one number.** Both 12, derived two ways.
  One expression, `#torsoW / 2 - #limbD / 2`, and A7 already settled it.
- **The arm centerline row describes an arm the robot does not have.** 27 = shoulder half-spacing +
  a limb radius + 3 mm of air is an arm hanging square to the torso. The arm hangs 33.13° off
  vertical on an angled stud, so the row went and the shoulder stud's own length replaced it.
- **`#clipR` gets its first row**, in the proportions table. One tab reads it, so the rule leaves it
  there; A10 asked only that it stop being the one number in the robot with no row at all.

## The height stack, republished

The stack was `150 mm` with every station on a whole millimeter, and it was the argument for a
torso divisible by 24. Below the hip it still is:

| Station | mm from ground |
| --- | --- |
| ankle | 24 |
| knee | 72 |
| gripper, bottom, elbow bent 45° | 86.58 |
| mid thigh | 96 |
| wrist | 110.06 |
| hip | 120 |
| elbow | 157.04 |
| shoulder | 197.24 |
| neck | 236 |
| top of head | 317.05 |

**Above the hip nothing is whole, and the shoulder stud is why.** The stud leaves the side face 53°
below horizontal and 30° toward the front, and no angle outside 0, 30, 45, 60 and 90 resolves into
whole millimeters. That is the cost of the shoulder, stated: it buys the arm a clear arc and it
takes the stack's roundness.

**The arms still reach mid-thigh, to 0.74 mm.** Shoulder to the bottom of the gripper is
`2 × #limbCenter + #gripperL` = 120 along a straight arm, which at 33.13° off vertical drops 100.49
and lands at 96.74 against a mid-thigh of 96. The relation was set on a vertical arm and the angled
stud cost it three quarters of a millimeter.

## Found while sweeping, and fixed here

**The feature plan's stage 5 said stubs on the ears and pockets in the blade.** That is the
arrangement A4 reversed on the user's instruction. It is one line in a table nobody had reread since
the swap, and it now reads axle and bumps on the blade, bores and valleys in the fork.

**The risks list said the socket holds by 0.197 mm of retention.** That is the 48 mm joint at
`#grip` 1.35. It is 0.48 mm of interference now.
