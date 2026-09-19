# Phase A — the six open numbers

Read on 2026-09-18 from the parents' records by
[`../scripts/a_open_numbers.py`](../scripts/a_open_numbers.py). Four are already right in the parent
and draft9p5 carries them; two are corrections this draft makes.

| What | What the parent holds | draft9p5 |
| ---- | --------------------- | -------- |
| `#wall` | `#torsoH * 3 / 160` | carried |
| #118, the two ball and socket connectors | `stud connect to robot` CENTER, `socket connect to robot` CENTROID | both built CENTROID |
| #125, `torso shoulder profile` | stands on the model, plane query `JJC` | carried |
| #142, `blade to robot connector` | present, built from a one-entity origin query | carried, and measured in Ring 2 |
| #168, `l limb`'s `limb section` | stands on the model, plane query `SYGmP`, no start offset | carried |
| #215, `sole groove` | the defect is in the parent | draft9p5 builds it right |

## What each one turns on

- **#118 is a correction.** The task as written was backwards against the settled joint, and its
  resolution folded into `.docs/build/plan/04-ball-and-socket.md` is that both connectors are
  inferred CENTROID. The parent still has the stud on CENTER, so draft9p5 builds both CENTROID and
  reads `entityInferenceType` back off the feature. Neither face can tell the two apart by
  measurement: a disc's center and its centroid are the same point, which is why the check is the
  parameter and not the geometry.
- **#142 is confirmed present, not confirmed placed.** The record says the connector exists in
  draft9p1p6 and is built from a one-entity query; it does not say where that puts it. A mate
  connector's position comes from the query and the inference, so the place it lands is measured on
  the built model. Ring 2 on `hinge` measures it against the reference position the task names,
  which is `(0, 0, -26.4)` mm with z `(0, 0, -1)`.
- **#215 is the one still pending**, and it is `task.foot.sole_groove` in the move plan.
  `sole groove` in the parent cuts up into the foot instead of down through the sole, so the foot
  has eight tunnels above an unbroken sole where it should have eight open notches. The acceptance
  check is the one the task names: the sole at z -24 mm is nine faces, not one, and no face stands
  at z -20 mm. The parent's feature reads depth `#rib_d` with both the depth and the start offset
  set to the opposite direction; which of its parameters is the wrong one is decoded at the `foot`
  tab, where the feature is built.
