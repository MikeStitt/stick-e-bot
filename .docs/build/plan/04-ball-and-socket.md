# 4. The ball and socket

Starts from an assembly holding two floating parts. Ends with a Part Studio holding the ball stud
and the socket, and a mate connector on each.

**This tutorial has been published once and is being retaken, not written fresh.**
[`ball-and-socket.rst`](../../../instructions/robot-guide4/source/ball-and-socket.rst) is the
existing page. Three things stale it, and they are why the retake is a full one rather than a
patch.

- **`#fit` moves to 0.08, and `#grip` stops being a chosen number.** Every dimension downstream
  changes, so every frame showing a measured cavity, mouth or collar is wrong. That row has moved
  more than once and the sources that record it disagree; draft9p1 settles it in
  [`../../experiments/runs/2026-08-25-draft9p1/a2-fit.md`](../../experiments/runs/2026-08-25-draft9p1/a2-fit.md).
  The mouth is now the dimension, at `0.96 × #ball - 2 × #ballLoss` = Ø11.32, and the ball's depth
  follows it, so the snap holds whatever the fit is. The swing is ±39.01°.
- **The collar's diameter becomes `#ball + 2 × #wall`, Ø15.6 at `#wall` 1.8 mm.** The published
  page computes it the other way, and the arithmetic is on screen.
- **The limb stub goes.** The published page builds a Ø12 × 10 stub to sketch the collar on.
  Stickbot extrudes the collar straight from the Top plane through the ball's center, so the studio
  holds only the two mating pieces and there is no scaffolding to explain away.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.ball_and_socket.tab` | make a Part Studio and name it `ball and socket` | the element — no feature |
| `cad.parts.ball_and_socket.stud.variables` | `#ball` and `#stand` in `robot sizes`, `#stalk` in the tab | three variables |
| `cad.parts.ball_and_socket.stud.profile_sketch` | arc, three lines, three dimensions | `stud profile` |
| `cad.parts.ball_and_socket.stud.revolve` | revolve it about the axis | `revolve stud` |
| `cad.parts.ball_and_socket.collar.wall_variable` | `#wall` in `robot sizes`, which the circle is about to ask for | `#wall` |
| `cad.parts.ball_and_socket.collar.profile_sketch` | a circle on the Top plane, Ø`#ball + 2 × #wall` | `collar profile` |
| `cad.parts.ball_and_socket.collar.grip_variables` | `#fit`, `#ballLoss`, `#grip`, `#collar` in `robot sizes` | four rows |
| `cad.parts.ball_and_socket.collar.extrude` | `#grip` up, `#collar` down | `collar blank` |
| `cad.parts.ball_and_socket.cavity` | subtract the stud with offset `#fit`, keep tools | `cavity from ball` |
| `cad.parts.ball_and_socket.slit.variables` | `#slit`, `#slit_in` and `#slit_out` in the tab | three variables |
| `cad.parts.ball_and_socket.slit.profile_sketch` | one slot, patterned to four, then the pattern's center dragged off the origin and pinned back to it | `slit profile` |
| `cad.parts.ball_and_socket.slit.depth_variable` | `#slit_d` in the tab | `#slit_d` |
| `cad.parts.ball_and_socket.slit.extrude` | cut `#slit_d` down from the top face | `relief slits` |
| `cad.parts.ball_and_socket.stud.connector` | the stud's mate connector | `stud connect to robot` |
| `cad.parts.ball_and_socket.socket.connector` | the socket's mate connector | `socket connect to robot` |

### The numbers this joint adds

**A number two tabs read is a row in `robot sizes`; a number one tab reads is that tab's own.**
That is the rule tutorial 2 followed for the head's twelve, and seven of this joint's numbers are on
the studio side of it. The torso, the limbs, the foot and the gripper all build a collar or a stud.

**`cad.parts.ball_and_socket.variables` is gone**, and the four steps in the table above replace
it. It typed eleven numbers into an empty tab before anything was drawn.

| variable | expression | at the robot's size | typed at |
| -------- | ---------- | ------------------- | -------- |
| `#ball` | `#torsoH / 8` | 12 mm | `stud.variables` |
| `#stand` | `#ball * 5 / 6` | 10 mm | `stud.variables` |
| `#wall` | `#torsoH * 3 / 160` | 1.8 mm | `collar.wall_variable` |
| `#fit` | `0.08 mm` | 0.08 mm | `collar.grip_variables` |
| `#ballLoss` | `0.10 mm` | 0.10 mm | `collar.grip_variables` |
| `#grip` | `sqrt((#ball / 2 + #fit) ^ 2 - (0.48 * #ball - #ballLoss) ^ 2)` | 2.2205 mm | `collar.grip_variables` |
| `#collar` | `#stand` | 10 mm | `collar.grip_variables` |

**`#fit` and `#ballLoss` are typed with `#grip` rather than where they are first read on their
own.** `#grip` is written from both of them, so neither can wait for `cavity from ball`, which is
the first feature to name `#fit` in a dialog. One number and the terms it is made of go in
together.

**`#wall` moves here from tutorial 1, where nothing read it.** It is a `robot sizes` row rather
than this tab's own because `foot` and `gripper` each build their own collar from it, so three tabs
read it, and Onshape scopes a variable to its Part Studio. That scoping is why those tabs had to
declare their own at all, and the Variable Studio is the only thing that fixes it.
[`../../experiments/runs/2026-08-25-draft9p1/a6-wall.md`](../../experiments/runs/2026-08-25-draft9p1/a6-wall.md)
has what the disagreement cost. It is `#torsoH * 3 / 160`, 1.8 mm at the robot's size, and not the
3.0 mm the plan carried until draft9p1p4 halved the socket wall to buy insertion force;
`make_plans.py` has read `COLLAR_WALL = TORSO_H * 3 / 160` since.

**`#ballLoss` is a printing number, like `#fit`.** It is what a printed ball loses on its radius,
and it is in the table because the mouth is drawn small enough that the printed pair comes out at
0.96 of the ball. `#grip` is the row that reads it.

**`#stand` moves here from tutorial 6.** It is how far the stud stands off the face it is built on,
and the stud is built here. [`06-torso-joints.md`](06-torso-joints.md) reads it for `#boss_len` and
adds `#limbD` alone.

**The tab keeps five local rows, and four of them are expressions.** draft9p1p1 declared
`#stalk = 6 mm`, `#stud_len = 10 mm`, `#slit = 1.6 mm`, `#slit_in = 5 mm` and `#slit_out = 12 mm`.
Every one was typed, so every one was right at the robot's size and at no other. This is what they
are now.

| variable | expression | at the robot's size | typed at |
| -------- | ---------- | ------------------- | -------- |
| `#stalk` | `#ball / 2` | 6 mm | `stud.variables` |
| `#slit` | `1.6 mm` | 1.6 mm | `slit.variables` |
| `#slit_in` | `sqrt((#ball / 2 + #fit) ^ 2 - (#ball / 3) ^ 2) - #wall / 2` | 3.679 mm | `slit.variables` |
| `#slit_out` | `#ball` | 12 mm | `slit.variables` |
| `#slit_d` | `#grip + #ball / 3` | 6.2205 mm | `slit.depth_variable` |

- **`#stud_len` is gone.** It was `#stand` under a second name.
- **`#slit_d` is new.** It is how deep the slits cut, and it replaces the `#grip + #ball / 4` the
  step table used to carry inline. The floor is `#ball / 3` below the ball's center, so the ring
  that springs the tabs shut is 6.0 mm thick whatever the printer needs, and the depth is measured
  down from a top face that does move.
- **`#slit_in` is the cavity's own radius at the slit's floor, less half a wall.** The slot has to
  start inside the mouth and inside the cavity where the cut bottoms out, or the bottom of the cut
  is a pocket instead of a slot.
- **`#slit_out` is `#ball`.** The slot has to finish outside a collar of radius
  `#ball / 2 + #wall` = 7.8 mm, and `#ball` = 12 mm clears it by 4.2 mm.
- **`#slit` stays, and stays typed** like `#fit`. Both are printing numbers rather than fractions
  of the robot.

**The drive test for this tab moves `#torsoH`.** Every row here hangs off it, and `#torsoW`, which
drives the head, reaches none of them.

**The collar goes `#collar` down, not `#collar - #grip`.** The socket runs from `-#collar` to
`+#grip`, so it is 12.2205 mm tall at the robot's size and its floor is a full disc of radius
7.8 mm. The older arithmetic is what draft9p1p1 replaced, and the reference is what this draft
follows.

**The top face is the mouth.** Nothing in the tab dimensions a mouth: the blank stops at `#grip`
above the ball's center, and a plane there cuts the cavity sphere at a radius of
`0.48 * #ball - #ballLoss`. That is what `#grip` solves for, and it is why the mouth cannot be
measured in a dialog. It is also why `#ballLoss` has to be a row rather than a number inside a
sketch: nothing downstream of `#grip` can see it.

**The two connector steps are new.** The published page ends at the finished socket. Every
consumer of this joint moves it by connector, so the connectors are part of the joint, not part of
whatever uses it.

**Both connectors are inferred the same way, and the way is `CENTROID`.** A mate connector dropped
on a face carries an inference type, and the settled joints put `CENTROID` on four of the five
robot connectors: the hinge's fork and blade, `u limb`'s `mate for fork`, `l limb`'s
`mate for ball stud`, and this tab's `socket connect to robot`. Only `stud connect to robot` reads
`CENTER`, so the stud is the one out of step, and one joint asks for one rule. Task #118 read it
the other way round against `stickbot-draft9p1p1`, before the settled joint made `CENTROID` the
majority.

**Neither face can tell the two apart, so the take has to read the field rather than the point.**
The stalk's top face is a Ø6 mm disc of 28.2743 mm² and the socket's root face is a Ø15.6 mm disc
of 191.1345 mm², and a disc's center and its centroid are the same point: both connectors land on
the axis at z +10 mm and z −10 mm whichever is inferred. `read_shape.py` cannot see the difference
and `diff_shape.py` will not report one. The step reads `entityInferenceType` back off the feature,
the way [`../takes.md`](../takes.md) asks a step to read back what it made.

**The reference's three typed constants are gone, and that settles task #119.**
`stickbot-draft9p1p1` typed `#stud_len = 10 mm`, `#slit_in = 5 mm` and `#slit_out = 12 mm`, and
draft9p3 spelled the same three out inside its sketches, so the two models agreed at `#torsoH`
96 mm and diverged at every other size. The open question was whether to match the reference or
record an agreed departure from it. draft9p1p4 answered it in the model: `#stud_len` is `#stand`,
`#slit_in` is the cavity's own radius where the slit bottoms out less half a wall, and `#slit_out`
is `#ball`. `stickbot-draft9p1p6` is this draft's reference for the joint, so there is no departure
left to record.

**A local that repeats a studio row is the defect the rule is against.** Onshape scopes a variable
to the Part Studio that declares it, so a tab that declares `#fit` shadows the studio's row: the tab
goes on using its own value, the row moves without it, and nothing turns red. The Variable Studio
takes rows at any point in the build, so a row is added on the page where it first means something
and there is still one table. [`onshape`](../../../.claude/skills/onshape/SKILL.md)
§ *Modeling standards* is the rule.

**Drag the pattern's center off the origin before pinning it.** A circular pattern's center is
sketch geometry that arrives sitting on the origin without being held to it, and that is where the
sketch's last blue hides. Two points on one pixel cannot be picked apart, so the drag is what makes
the second pick possible — and it is also what shows the reader the freedom, which is why it is a
step and not a workaround. [`../takes.md`](../takes.md) § *When a step does not work as written*
records the selection box that was tried instead.

## The shots this tutorial needs by name

**Requirements in play.** `req.model.one_document` — this tutorial is a tab in `stickbot`, and
the published page built it as a document of its own. `req.page.units` — the units go with it;
they are set in tutorial 1 and nowhere else. `req.shot.toolbar` and `req.page.video` — this is
the page that has them, and it is the one every later page is measured against.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| two heroes | the ball stud and the socket, used apart and shown apart | `req.page.hero` |
| the part list, both named | two parts in one studio is the thing to see | `req.model.named_features` |
| each connector's origin, medium and close-up with a ring | the ball's center is a point among sketch points | `req.shot.two_frame` |
| a section through the assembled joint at `#fit` 0.08 | what the real part looks like; the gap itself will not read at this fit, so the exaggerated frame goes with it | `req.shot.true_state` |
| the tree | at the end | |
| the version dialog | publishing | |

**[`shots.md`](../shots.md) §*A gap too small to photograph* applies again.** The rule says: turn
the gap up, shoot the section, turn it back, and let the captions say which is which. It was
written for a 0.02 gap and draft9p0 suspended it because 0.8 mm photographs. At 0.08 it does not —
that is a tenth of a millimeter on a Ø12 ball — so the pair of frames comes back. Take the honest
section first, then the exaggerated one, and caption both.

This is also the clearest case in the guide of a *teaching* number changing because a *printing*
number changed, and the caption should say so rather than presenting 0.08 as arbitrary.

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 4 - the ball and socket** (`2eb631c1bd1bccb0ee350d3f`). The `ball and socket` tab was
emptied of what draft9p3 left in it and built again by following the written page, step for step.

**The tab holds fourteen features and two solids.** In order: `#stalk`, `stud profile`,
`revolve stud`, `collar profile`, `collar blank`, `cavity from ball`, `#slit`, `#slit_in`,
`#slit_out`, `slit profile`, `#slit_d`, `relief slits`, `stud connect to robot`,
`socket connect to robot`. Five of the fourteen are Variable features, and they are the five
numbers that belong to this tab alone; the seven the robot shares are rows in `robot sizes`.
`Ball stud` has 3 faces and measures 12 × 12 mm across with its top at z 10 and the middle of its
ball at z 0. `Socket body` has 19 faces and measures 15.6 × 15.6 mm across, from z −10 to z 2.2205,
which is `#collar` below the middle of the ball and `#grip` above it.

**`robot sizes` carries ten rows at the end of this tutorial**: `#torsoH`, `#torsoW` and `#torsoD`
from tutorial 1, then `#ball`, `#stand`, `#wall`, `#fit`, `#ballLoss`, `#grip` and `#collar`, each
typed at the step that first needs it.

**Both mate connectors infer `CENTROID`, which closes an open question from draft9p3.** The stud's
hangs on `Face of revolve stud`, the flat top of the stalk at z 10, and the socket's on
`Face of collar blank`, the flat bottom of the collar at z −10. Neither is a plane offset from a
rim; both are the face's own middle, which is what the connector is asked for.

**`stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)) carries its own version
**tutorial 4 - the ball and socket** (`1e5a9d41d89dd90c6952d2e3`), taken where the page's frames
were shot. Read back side by side, the two documents agree on the feature list, on the ten rows and
on both solids' face counts and bounding boxes.

## Captured

**`instructions/stickbot-draft9p4/source/ball-and-socket.rst`**, written from the 95 frames in
`instructions/stickbot-draft9p4/source/images/ball-and-socket/`, captured across 21 steps in
`stickbot-draft9p4-check`. Sphinx builds the page with no warning; every frame on disk is used and
every frame the page names is on disk. `tools/page_sweeps.py`'s four sweeps come back clean.

**The carried page named five frames that no longer exist.** `parts.ball_and_socket.variables-01`,
`-03`, `-04`, `-05` and `-06` belonged to the single `variables` step that this plan broke up, and
20 frames on disk had nothing pointing at them. Its numbers were staler than its frames: an 18 mm
socket where it is 15.6, `#ball / 4` for the stalk where the sketch takes `#stalk / 2`, `#grip`
1.94648 where it is 2.2205, slit ends `#ball * 5 / 12` and `#ball` where they are `#slit_in` and
`#slit_out`, and a slit floor at 3 mm where it is 4.

**The whole page is this draft's own, so none of that carried through.**

## What we do not know yet

**Where 1.6 comes from is still open.** It is the slit's width in 9p1p1 and in draft9p0 before it,
and no page or audit says what set it. It is not a fraction of the ball: at `#torsoH` 96 it is
`#ball * 2 / 15`, which is not a number anybody chooses. A slit has to print open and stay springy,
so a printing number is the likely source. Until the design source answers, the row is typed and
the page groups it with `#fit` and `#ballLoss` as a number about the printer rather than about the
robot.

**The rest of this section is answered, and the answers are above.** The retention reads as a rim
standing over the ball rather than as a gap, which is why the exaggerated pair is needed and why
both close-ups are shot at the same scale on the same part. The mouth is shown by the section
rather than by a field, and its size is derived in prose beside the frame. 0.8 mm is the
exaggerated value, in a step of its own after the honest section, and the fit goes back to 0.08
before the version is published. The document and the units are set in tutorial 1, so the page
opens on the new tab and says nothing about either.
