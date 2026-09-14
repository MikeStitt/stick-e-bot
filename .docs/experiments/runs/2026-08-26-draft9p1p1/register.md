# draft9p1p1 — the register

**This is a point release, and it reads as a pair with
[draft9p1's register](../2026-08-25-draft9p1/register.md).** 9p1 rebuilt the robot's design intent
across thirteen rows and then measured it; three of the shapes it left behind were wrong in ways
only its own measurements could show, and this draft repairs those three and nothing else. Where an
item below says *carried*, 9p1's register is where it was written first and this file does not
restate it.

The three are the socket's relief slit, which was a blind pocket for its last 2.5943; `#collar`,
which was a typed 11 measured from a mouth that moves; and the gripper's clip, whose top B8 had
rounded to the collar's circle instead of cutting flat and square. Two design-source rows ride with
them: the feet's 8 mm offset, which the sheets carried and the model never had, and two figures that
drew the socket without its collar.

## Where the work is

| | |
| --- | --- |
| document | `stickbot-draft9p1p1`, `4b2e0d48efd37d3327a90afb` |
| workspace | Main, `a1af16872d25103815f1c32a` |
| copied from | `stickbot-draft9p1` at `Recovery point` `8504f457723606c65c2ab48f` |
| `Start` | `8a5484206371ce199e41968f`, the copy before any edit |
| **`Recovery point`** | **`0f4e9b6b36b5c1a6f45197e1`**, cut 2026-08-28, what 9p2 takes |

| tab | element id |
| --- | --- |
| `robot sizes` VARIABLESTUDIO | `f30d47abeacf3059ec4a3342` |
| `body` | `4e48e81a06c8d40b2a38b871` |
| `head` | `1562dee65e364ec088dda0ec` |
| `ball and socket` | `6dcfcf8856d4feea7faa440a` |
| `foot` | `c01ac56602d81451da6a5db5` |
| `hinge` | `184adaa7b3e7abc7bc4357c7` |
| `u limb` | `656816292447e8797ff0402d` |
| `l limb` | `88de5da8c7611f141a1a92a9` |
| `gripper` | `32166c7b3d22572c0e7dd0c3` |
| `stickbot` ASSEMBLY | `cd2278317279029435f010de` |

`stickbot`, `stickbot-for-bot-review`, `stickbot-draft9p0` and `stickbot-draft9p1` were read and
never written.

## What Phase A decided, and on what evidence

| | What it settled | The evidence |
| --- | --- | --- |
| **A2** | `#collar` becomes `#ball / 2 + #wall` = **9.0000**, measured from the ball's center to the socket's root, and is `collar blank`'s second extrude distance on its own. Every expression that carried a `#grip` term to cancel a moving root loses it. | 9p1's [`c2-driving.md`](../2026-08-25-draft9p1/c/c2-driving.md), which measured the socket's root at −9.3200, −9.0535 and −7.0223 as `#fit` went 0 → 0.08 → 1 |
| **A1** | The slit's floor comes up to `#ball / 4` below the ball's center, z **−3.0000**, so the depth is `#grip + #ball / 4` = **4.9465** and the cut is a slot for all of it. `#slit_in` stays 5.0 and the pattern stays 4 over 360°. | 9p1's [`c1-readback.md`](../2026-08-25-draft9p1/c/c1-readback.md), which found an r-5.0 face bounding the cut and a floor at z −6.0535 where the cavity had closed to r 0.567 |
| **A3** | `clip profile`'s slab is dimensioned `#collarR` rather than `#clipR`, so the clip's top is 18 × 18 with the Ø18 collar inscribed tangent on all four sides; a 45° chamfer of leg `#collarR − #clipR` necks it to the clip above the mouth, and B8's three rounding features come out. | [`a/a3-gripper.md`](a/a3-gripper.md), which measured `stickbot-for-bot-review` and found its square is a coincidence of a clip 1.6 wider than its collar, which stopped being true when the robot doubled |
| **A4** | `FOOT_X` becomes `LEG_X`. The feet sit at x ±24 with their inner edges together at x 0, and are not handed. | 9p1's C1, which measured both feet at ±24 while `make_plans.py` alone carried the 8 mm |
| **A6** | `gripper()` and `foot()` draw the socket's collar standing proud, and stop calling the origin the joint center when the figure puts the mouth there. `GRIPPER_L` and `FOOT_H` are measured from the ball's center. | Each part studio's own coordinates, where `gripper` and `foot` hold their cavity sphere at (0, 0, 0) and the figures put three different points on one |
| **A5** | The sheets are regenerated and frozen as `r7`, and the hip sketch republished. | |

**A2 was settled before A1, because A2 moves what A1 measures from.** Settling the slit against a
root that was about to stop moving would have settled it twice.

**Four decisions the plan was waiting on were the user's, and were made on 2026-08-27:** what
`#collar` becomes, how deep the slit goes, that the pattern stays circular, and that the head's
depth stays driven. The plan records them under *Settled on 2026-08-27*.

## What Phase B edited

Nothing was rebuilt. Six tabs were edited in place, each with its own note.

| | | |
| --- | --- | --- |
| **B0** | the copy, and every element id written down before an edit | [`b/b0-copy.md`](b/b0-copy.md) |
| **B1** | `robot sizes`: `#collar` stops being a typed 11 and becomes `#ball / 2 + #wall` | [`b/b1-variable.md`](b/b1-variable.md) |
| **B2** | `ball and socket`: `collar blank`'s second distance becomes `#collar`, and `relief slits` ends at `#grip + #ball / 4` | [`b/b2-socket.md`](b/b2-socket.md) |
| **B3** | `head`, `foot`, `u limb`, `l limb`: the expressions that carried a `#grip` term | [`b/b3-consumers.md`](b/b3-consumers.md) |
| **B4** | `gripper`: the slab dimensioned `#collarR`, the chamfer drawn, three rounding features deleted | [`b/b4-gripper.md`](b/b4-gripper.md) |
| **B5** | `stickbot`: the instances moved onto this document's own workspace, and the rest pose read | [`b/b5-assembly.md`](b/b5-assembly.md) |

**B5 ran first.** A workspace instance follows a Part Studio edit as soon as the edit is made, and
9p1's B9 had pinned all fourteen instances to versions, so the assembly arrived showing 9p1's parts.
Moving it first is what let B1 to B4 be watched rather than made blind, and it is what makes Phase
C's drive a measurement.

## What Phase C measured

The whole model over REST, judged offline, then driven, then looked at.
[`c/c1-readback.md`](c/c1-readback.md), [`c/c2-driving.md`](c/c2-driving.md),
[`c/c3-inspection.md`](c/c3-inspection.md).

- **A1 holds.** `ball and socket`'s curved faces are r 3.0, r 6.0, r 6.08 and r 9.0 and **there is
  no face at r 5.0**, at a fit of 0.08, 1 or 0. The four floors sit at z −3.0000 and the cavity
  there is 5.2883 at the built fit and 5.1962 at the worst case, both outside the profile's inner
  edge at 5.0.
- **A2 holds where it matters and not where the plan's wording asked.** The socket's root is
  z −9.0000 and the slit's floor z −3.0000 at every fit; **the robot stands 317.0000 at every fit
  and not one joint station moves.** What does not hold is the plan's third clause, that every
  part's overall size holds: `Foot`, `Gripper`, `u limb` and `Socket body` still move their mouths
  by the same 2.0312 that 9p1 measured, and `head` moves its mouth downward. A mouth is part of the
  part, so those two claims could never both be true; the station is the one worth having and the
  station is what holds.
- **The invariant swapped ends, and that is the actual gain.** 9p1 kept the socket 11.0000 tall and
  let its root travel 2.2977; here the root is pinned and the height travels. That is what puts the
  slit's floor at a drawable z and what let three `#grip` compensations come out of two tabs.
- **The assembly is listening.** `#torsoH` 96 → 120 moved the standing height to 346.7500 and every
  station with it, and `#collar` came out at 11.2500 = `#ball / 2 + #wall` without anybody typing
  it. 9p1 could not make this measurement, because its assembly was pinned to versions and a deaf
  assembly holds its height too.
- **A3 holds, and is one face short of what the plan expected.** The clip's top is 18.0000 × 18.0000
  and the run at full width is **4.7000**, which is A3's prediction to the digit. The platform is
  **four corner faces of 17.3827** rather than one, because the Ø18 collar is inscribed tangent on
  all four sides; one face would mean a collar narrower than its platform, which is the reference's
  proportion and not this robot's. The mouth is still 2.6000 open and the crown survives whole at
  r 5.0000.
- **A4 holds with no model edit.** `Foot` is 48.0000 across its own X and each instance sits at
  x ±24.0000, so the soles meet at exactly 0.
- **Both round trips are exact.** `#fit` 0.08 → 1 → 0 → 0.08 and `#torsoH` 96 → 120 → 96, ten parts
  of ten returned to the boxes C1 measured.

**Two labels were wrong and are corrected.** [`b/b3-consumers.md`](b/b3-consumers.md) called the
head's +67.0000 the socket's mouth and its +56.0535 the root. The head's socket is the only one that
points down, so those are the root and the mouth. No number moved.

**One design-source line survived A1's sweep** and was fixed here:
[`../../../build/plan/04-ball-and-socket.md`](../../../build/plan/04-ball-and-socket.md) still
described `relief slits` as cut *"down to the collar less one wall"*, which is 9p1's 8.0 and not
A1's 4.9465.

## draft9p1's open items, closed or carried

| 9p1 left open | now |
| --- | --- |
| whether the foot gets its 8 mm offset and becomes handed | **closed.** Settled 2026-08-26 that it does not; A4 took `FOOT_X` to `LEG_X` in `make_plans.py` and the three sentences that carried the consequence, and C1 measured the feet at ±24 with their inner edges at 0 |
| whether `make_plans.py` gets the gripper's real body | **closed.** A3 settled the shape against the reference and A5 redrew `clip()` and `clip_front()` once, against the shape that is now built |
| the slit is 8.0 long and the source comment says 11.0 | **closed.** `SLIT_D` is now `GRIP + BALL / 4` with the arithmetic in the comment beside it, and the sheet line that still said otherwise is fixed above |
| whether 2.92 of wall holds a snap fit, and whether the mouth at 96% of the ball goes together by hand | **carried.** Both are print questions and nobody has printed the 2× robot. Task #29 |
| whether the head's depth wants to be driven rather than declared | **closed.** Settled 2026-08-27: it is driven and stays driven, and [`../../build-briefs/head.md`](../../build-briefs/head.md) makes the rule a requirement rather than a coincidence |

## Withdrawn

- **"The fit moves the robot's height."** This draft's plan opens with it and 9p1's own C2 had
  already measured otherwise: at `#fit` 1 the sole, the fork and the gripper's clip all stayed where
  they were. What was true is narrower and is what A2 actually fixed: the socket's *root* moved with
  the fit, and three expressions in two tabs carried a `#grip` term whose only job was to cancel
  that. The height is now invariant because nothing travels rather than because the travel cancels,
  and the slit's floor is at a fixed z as a consequence.
- **"The clip's top is one flat square face."** Phase C's wording. It is four, and the four are what
  a tangent collar leaves.

## Gates

| Gate | State |
| ----- | ----- |
| Model inspected | met — [`c/c1-readback.md`](c/c1-readback.md) measured it and [`c/c3-inspection.md`](c/c3-inspection.md) turned it through six views, with six renders of the two changed parts |
| Recovery point | met — `Recovery point` `0f4e9b6b36b5c1a6f45197e1`, opened at its own URL and its assembly measured there at 317.0000 |
| Links resolve | met — every relative link in this directory resolves |
| Prose style | met — `ninja check` is clean |
| Spelling | met — `ninja check` is clean |
| `req.model.one_document` | met — one document, one tab per part, and B5 moved the assembly's instances inside it |
| `req.model.design_intent` | met — `#fit` driven 0.08 → 1 → 0 → 0.08 and `#torsoH` driven 96 → 120 → 96, both round trips exact across all ten parts, and `#collar` derived correctly at both sizes |
| `req.carry.register` | met — this file, written against 9p1's by name |

**Gates this draft does not claim,** for the reasons 9p1 gave: *Steps reproduce*, *Names are real*,
*Floor & ceiling* and *Reading level*. It writes no steps and holds no session material.

## What is still open

- **Whether 4.9465 is the flex the joint wants.** The depth is now the tabs' free length and nothing
  else, which is what makes it a number worth choosing. It is 3.0535 shorter than 9p1's cut, and the
  ring under the tabs went from 2.9465 to 6.0000, so the tabs are both shorter and sprung harder.
  Nobody has flexed one. Task #29.
- **Whether 2.92 of wall holds a snap fit, and whether a mouth at 96% of the ball goes together by
  hand.** Carried unchanged from 9p1 and from 9p0 before it. Task #29.
- **`slit-reach.html` is incomplete rather than wrong.** It stops short of showing the cut's whole
  reach. Extending it was offered during Phase A and has had no answer.
- ~~`.docs/onshape-api.md` § *Rate limits* says "Recovery is minutes, not seconds".~~ **Closed on
  2026-08-28.** That section and `.docs/onshape-gui-howto.md` now carry both lengths, and `api()`
  in [`../../../../tools/onshape_session.py`](../../../../tools/onshape_session.py) reads
  `retry-after` and stops instead of laddering.
  [`../../../README.md`](../../../README.md) § *Pipeline improvements worth making* carries the
  sweep of the eight earlier attempts and why each missed.

## What draft9p2 inherits

A version, a design source and a log. Not a guide and not a frame.

- **The model** is `stickbot-draft9p1p1` at `Recovery point` `0f4e9b6b36b5c1a6f45197e1`.
- **The design source** is `make_plans.py` and the `r7` sheets, which C1 agrees with everywhere the
  two were compared.
- **The log** is [`b/`](b), six notes recording what each dialog did as well as what each feature
  became, and [`c/scripts/`](c/scripts), which reads and drives the model without touching the
  `features` endpoint.

**9p2's plan is already amended.**
[`../2026-08-25-draft9p2/plan.md`](../2026-08-25-draft9p2/plan.md) was written before 9p1's
register existed; it was re-pointed at this document on 2026-08-27, and its Phase P closes by
rereading this file. Phase D's amendment obligation is discharged there rather
than here.
