# draft9p1 — the register

draft9p1 captured nothing and wrote no guide page. It settled the design source on paper, edited
the model until it matched, and proved the match by measurement. Its product is one Onshape
document that agrees with `make_plans.py` everywhere the two were compared, and a version named
`Recovery point` for draft9p2 to start from.

This register is written to be read beside
[draft9p0's](../2026-08-23-draft9p0/register.md). Every defect that register recorded is named
below with what happened to it, and the ones that turned out to be wrong are withdrawn in writing
rather than dropped.

## Where the work is

| | |
| --- | --- |
| document | `stickbot-draft9p1`, `a1a859f4bfdfe42d372aff90` |
| workspace | Main, `d3a590c94880f445e3c56902` |
| last version | `Recovery point`, `8504f457723606c65c2ab48f` |

| element | eid |
| ------- | --- |
| `stickbot` (Assembly) | `4515305b332af7d4379b81b3` |
| `robot sizes` (Variable Studio) | `8e21e5ac45ee843a1c536e1b` |
| `body` | `6f635a750e13ccbf30d05ba2` |
| `head` | `915098789c7845370c86c914` |
| `ball and socket` | `365f6106c79b2ef1684bf939` |
| `foot` | `95448bc5d270c9d8370bf3cf` |
| `hinge` | `f2f0dbd682ff7413d3ce2443` |
| `u limb` | `3f27ca39a14117e276b7c449` |
| `l limb` | `fa98530f59d5f18889fe7c00` |
| `gripper` | `7ef73a118e1331213bc1554f` |

| version | id | what it holds |
| --- | --- | --- |
| `Start` | `8e4b28cc2cf504aef52a7a9a` | the copy of `stickbot-draft9p0` at `t14 legs`, before any edit |
| `parts built` | `6eae7c37deee3f58facbbf83` | every Part Studio at the end of B1 to B8 |
| `ankle centered` | `e6fd823965e71c15d9e267cb` | the foot's `mate to robot` connector moved onto the origin |
| `Recovery point` | `8504f457723606c65c2ab48f` | the measured, driven and inspected model |

`stickbot` `5dc85bc34f28cf4f6cee1f26`, `stickbot-for-bot-review` `111f975041ddb104a6028d45` and
`stickbot-draft9p0` `0f4b79a78707651ae20df5b2` were read and never written to. Nothing was pushed:
this run was asked to hold everything local, and it did.

**There is no `instructions/stickbot-draft9p1/`,** which the plan says on purpose. draft9p0's guide
stays where it is, and draft9p2 declares `parent: draft9p0` for its pages while taking its model
from here.

## What Phase A decided, and on what evidence

Twelve files in this directory, one per row. A4 has no file: it is a change to `make_plans.py` and
to [`../../build-briefs/hinge.md`](../../build-briefs/hinge.md), and its argument is in commit
`a56e0f6`.

| | decision | the evidence it turned on |
| --- | --- | --- |
| [A1](a1-limb-center.md) | `#limbSeg` becomes `#limbCenter` and means joint center to joint center | `make_plans.py:87` already said each joint takes about 21 mm of a 48 mm segment. The name was the only thing that disagreed |
| [A2](a2-fit.md) | `#fit` 0.08, socket height invariant, ball position free | Two readings of the requirement were worked out in full; B breaks the part when a student edits it, so A was adopted |
| [A3](a3-eye-ellipse.md) | the eye is a 16 × 8 ellipse at `#eyeX` ±12 and `#eyeUp` +8 | Read off the example over REST. Which document is the example dissolved: both carry the same profile |
| A4 | every protrusion on the blade, every recess in the fork | A bump 1.2 proud of a face at ±5.00 and an axle standing to ±6.60 both crossed the ear's inner face during mating. The fork now presents flat face and holes |
| [A5](a5-foot-tread.md) | the tread is phased off `#rib_w / 2`, land at both ends | Two phases were worked; A leaves solid material at heel and toe |
| [A6](a6-wall.md) | `#wall` is `#torsoH / 32` and lives in the Variable Studio | Three tabs declared it with two meanings that agree only at 96 |
| [A7](a7-hip-shoulder.md) | the torso's width places the hips | The design source never had this defect; the model had it. Driving `#torsoH` could not find it because both meanings move together |
| [A8](a8-head-numbers.md) | the head gets twelve variables, `#headD` follows `#torsoD`, no pupils | The head's 63 mm depth is `#headD` 60 plus `#face` 3, and `#face` is one number for the eye's proud and the mouth's cut |
| [A9](a9-typed-numbers.md) | `#boss_d` and three more become expressions; `upper rounds` is `#headW / 6` | `#boss_d` was a third wider than the ball it carries, typed and never following |
| [A10](a10-gripper.md) | the bore runs left-right, the mouth opens the way the robot faces, the body is the collar's diameter | The mouth's angle is a result of the other three, not a fourth number |
| [A11](a11-assembly.md) | one width mate placed once, a rest pose at every mate zero, symmetric feet | Two of its three claims did not survive B9 and are withdrawn below |
| [A13](a13-variables-table.md) | the Variables table republished at the size the robot is built at | The Constitution's design source had never received draft9p0's doubling |
| [A12](a12-sheets-and-sketches.md) | the sheets frozen as `r6`, every sketch carrying a moved number republished | Runs last, because A2, A6 and A9 decide what several numbers become |

**A2 was the one item that could have held up the phase, and it did not.** The rearrangement it
asks for was already in the brief: `collar blank` extrudes `#grip` one way and `#collar - #grip` the
other, so the total is `#collar` whatever `#grip` does. **The socket was built to A2 before A2 was
written.** What held the tab at draft9p0's numbers was five local variables shadowing the studio.

## What Phase B edited

The whole log is [`b/notes.md`](b/notes.md); [`b0-copy.md`](b0-copy.md) records the copy.

| | tab | what changed |
| --- | --- | --- |
| B0 | — | `stickbot-draft9p0` at `t14 legs` copied into `stickbot-draft9p1`, with its whole feature history |
| B1 | `robot sizes` | `#limbSeg` renamed, `#fit` set, seven rows promoted. Renaming carried its readers with it and no geometry moved |
| B2 | `ball and socket` | nineteen features to fourteen. Five shadowing locals deleted; the slit sketch's pattern center pinned to the origin |
| B3 | `hinge` | eight edits, no new features. The blade's four detent features and the fork's four traded members |
| B4 | `body` | six of nine variables became expressions and none of them changed a number |
| B5 | `head` | a tab that declared nothing now declares twelve, and every one evaluates to the number it replaced. The eye became an ellipse |
| B6 | `foot` | four shadowing locals deleted, the tread phased, and a pedestal that had been buried in the socket brought out to abut it |
| B7 | `hinge`, `u limb`, `l limb` | the joints carved into the segment. `#rod` from `#limbD` 24 to `#ear` 6.4, and each rod derived from `#limbCenter` |
| B8 | `gripper` | the body's top rounded to the collar's own circle, proved flush by there being one face rather than two |
| B9 | `stickbot` | fourteen instances re-pointed at versions, thirteen mates kept, the rest pose set, and both feet centered |

**Most of Phase B was deletion.** Nine of the ten rows removed a local variable, a typed number or a
feature rather than adding one, and the two tabs that gained rows — `robot sizes` and `head` —
gained expressions that evaluate to what was already there. That is what made the phase checkable:
a change that moves no volume is a change whose volume can be checked.

**Three things Phase B found that Phase A had not:**

- **`#grip` had never been given A2's number in the `foot` tab.** It carried 3.6, which is neither
  draft9p0's value nor its doubling. Deleting it shortened `foot pedestal` by 1.65 mm and **the
  foot's volume did not change**, because the material the pedestal lost was material the derived
  socket was already occupying. The union had welded the two and no feature ever went red.
- **`l limb`'s `limb section` was sketched on a face of `add blade`** — the shank's end face, which
  is exactly the stacking A1 removes. It is on the Top plane now, so the pin is the sketch's origin.
- **The foot's `mate to robot` connector sat on a wall of the socket's snap slit,** at x 0.8, so
  both feet inherited the same offset and their inner edges both landed at −0.8. Re-pointing it at
  the Part Studio origin put both ankle connectors at (0, 0, 0).

## What Phase C measured

Three files: [`c/c1-readback.md`](c/c1-readback.md), [`c/c2-driving.md`](c/c2-driving.md) and
[`c/c3-inspection.md`](c/c3-inspection.md). The raw fetch is
[`c/c1-raw.json`](c/c1-raw.json) and the scripts are [`c/scripts/`](c/scripts).

- **The robot stands 317.0535 mm**, against `HEIGHT` 317.05351599030456 in the source. The height
  is Onshape's own bounding box over fourteen instances placed by mates rather than by numbers.
- **Every joint station is one `#limbCenter` from the last.** −58, −106, −154 step by 48, and the
  sole is `#foot_h` below the ankle at −178, which is `SOLE_Z`.
- **The thinnest wall anywhere is 2.9200 mm**, and it is in every part that carries a socket:
  `COLLAR_R` 9.0 over a cavity of `BALL / 2 + FIT` = 6.08.
- **The mouth is 11.52 exactly**, proved by the area of the ring it leaves — 129.460 mm² measured
  against 129.50 arithmetic, the difference being the slit ending on the collar's round outside.
- **`#limbCenter` 48 → 60 moved exactly two parts, each by exactly 12**, and left the other eight
  untouched. Typed back to 48, all ten returned to their measured boxes.
- **`#fit` 0.08 → 1 → 0 left the socket 11.000 mm tall at every value**, with `#grip` measuring its
  formula to the fourth decimal at each. The parts that followed the fit are the five that carry a
  socket; the four that carry a ball did not move.
- **The model was opened and turned through five orientations**, and the version `Recovery point`
  was published.

## draft9p0's defects, closed by name

| draft9p0's defect | what happened |
| --- | --- |
| `#limbSeg` and `ARM_SEG`/`LEG_SEG` do not mean the same thing | **closed.** A1 renamed it and B7 carved the joints into the segment. `u limb` measures 60 and `l limb` 54, and both stations are 48 apart |
| The robot stands 421.8 mm where the plan page says around 320 | **closed.** It stands 317.0535, and the sheets draw 317.05351599030456. The whole 106.4 was the two limb segments, and A2 moved the last 1.65 of it by raising `#grip` |
| Neither knee has a Width mate, and neither elbow does either | **withdrawn.** See below |
| The whole assembly is saved posed, and the feet are not symmetric | **closed in part.** Every instance is at identity rotation on its station, and both feet are at x ±24. The 16 mm gap the sheets draw needs a handed foot and is open |
| `#wall` is declared in three tabs with two different meanings | **closed.** A6 made it `#torsoH / 32` in the Variable Studio, and B1, B2 and B6 deleted the locals |
| The hips are placed by `#torsoH` and the shoulders by `#torsoW` | **closed.** A7 and B4. The hips measure ±24 from `#legX` and the shoulders ±49.551 from `#shX` |
| The head tab holds no variables at all | **closed.** B5 gave it twelve, each evaluating to the number it replaced |
| The torso's shoulder pads are a typed `#boss_d = 16 mm` that never follows | **closed.** A9 and B4. The boss measures r 8.0000 and is an expression |
| The head measures 63 mm deep where `HEAD_D` is 60 | **closed as a decision, not an error.** A8 named the extra 3 `#face`, one number for the eye's proud and the mouth's cut. The box still reads 63 and the source now says why |
| The hinge's snap direction disagreed between the brief's table and the model | **closed.** A4 re-derived it against the new arrangement: the axle's 1.0 spread still governs, larger than the bump's 0.6, and every spring figure is unchanged |
| The gripper body does not follow the socket's outside profile | **closed in the model, open on the sheets.** B8 rounded the top to the collar's own circle. `make_plans.py` still draws the old slab |
| `gripper.md` says the mouth opens forward at +Y, and the robot faces −Y | **closed.** A10 states the facing once, against the robot's own facing |
| Three source disagreements on the gripper | **closed.** A10 settled all three; B8 measured the bore at Ø3.300, the outer at Ø10.000 and the mouth at 2.600 |
| The elbows have no Width mate, and `assembly.md` says they must | **the brief is now the thing that is wrong.** See the withdrawal below |
| The assembly's instances were inserted from the workspace, not from a version | **closed.** B9 re-pointed all fourteen with *Change to version… → Update all*, keeping every instance id and all thirteen mates |
| `upper rounds` was built at r12 where the plan types 6 | **closed.** A9 made it `#headW / 6`, which is 12, and the model measures r 12.0000 |
| The head's Ø8 pupils were not built | **closed.** A8 dropped them. There was nothing in the model to delete |

The five remaining defects in draft9p0's register are about its guide — captions, alt text, figure
counts and spelling. This draft writes no guide page and leaves them where they are.

## Withdrawn

- **The Width mate is withdrawn, and A11's premise with it.** A11 says all four hinges are a bare
  Revolute so every lower limb can slide sideways in its fork. The arithmetic closes without a
  slide: thirteen free instances give 78 degrees of freedom, nine Ball mates remove 27 and four
  Revolutes remove 20, leaving **31, which is 9 × 3 + 4 × 1 and all rotational**. There is no
  translation for a Width mate to take. The 0.6 mm of clearance A11 describes is a fit in the
  solid, not a degree of freedom. The requirement is out of
  [`../../build-briefs/assembly.md`](../../build-briefs/assembly.md),
  [`../../../robot-build-plan.md`](../../../robot-build-plan.md),
  [`../../../build/plan/13-assembly-arms.md`](../../../build/plan/13-assembly-arms.md) and
  [`../../../build/plan/14-assembly-legs.md`](../../../build/plan/14-assembly-legs.md), and
  [A11](a11-assembly.md) carries the withdrawal at its head.
- **A11's "each arm lies along its own shoulder stud, 33.13° from vertical" is withdrawn.** The
  torso's shoulder connector is at (49.551, −7.824, 19.235) with its Z along the torso's Z, so a
  Ball mate at zero hangs the arm vertically. At rest the arm clears the torso by 9.102 mm.
- **A11's "the feet were never asymmetric" is withdrawn.** They were, by 1.6 mm, and B9 found the
  cause: a mate connector on a slit wall rather than on the origin. draft9p0's defect was real and
  A11 was reading the sheets rather than the model.
- **A5's account of what draft9p0 built is withdrawn.** A5 works the offset 64 forward and concludes
  five of the eight grooves were cut in empty air. All eight were on the sole: 64 is measured from
  the origin to the toe edge, not from the heel. The row A5 adopts is unaffected; what it rejects
  is what draft9p0 actually built.
- **The suspicion that `BLADE_OUT` and `SLOT_DEEP` had gone stale is withdrawn.** The hinge's
  bounding box shrank 5.6 at both ends, which looked like drift. C1 measured the blade standing 32
  out of its shank and the fork's slot 33 deep, both exactly. The whole 5.6 is B7's `#rod` change
  behind the joint.
- **The gripper brief's 2.20 mm wall is withdrawn as a defect.** 2.20 is `9.0 − 6.8`, and 6.8 is the
  ball's radius plus a `#fit` of 0.8. A2 set `#fit` to 0.08, so the wall is 2.92. The number in the
  brief predates A2 rather than describing a fault in the part.

## Gates

| Gate | State |
| ----- | ----- |
| Model inspected | met — [`c/c1-readback.md`](c/c1-readback.md) measured it and [`c/c3-inspection.md`](c/c3-inspection.md) looked at it, in five orientations, with the frames kept |
| Recovery point | met — `Recovery point` `8504f457723606c65c2ab48f`, and three named versions on the way to it |
| Links resolve | met — every relative link in this directory resolves |
| Prose style | met — `ninja check` is clean |
| Spelling | met — `ninja check` is clean |
| `req.model.one_document` | met — one document, one tab per part, the joint a tab and not a document |
| `req.model.design_intent` | met — `#limbCenter` driven 48 → 60 → 48 and `#fit` driven 0.08 → 1 → 0 → 0.08, both round trips exact across all ten parts |
| `req.carry.register` | met — this file, written against draft9p0's by name |

**Gates this draft does not claim,** and says so in its plan: *Steps reproduce*, because it writes
no steps; *Names are real*, because no page here names a tool; *Floor & ceiling* and *Reading
level*, because there is no session material.

## What is still open

- ~~Whether the foot gets its 8 mm offset and becomes handed.~~ **Settled on 2026-08-26: it does
  not.** `FOOT_X` is `LEG_X + #foot_h / 3` = 32 in the source and the feet measure ±24 in the
  model, and it is the source that gives up the offset. The feet are not handed and they are
  allowed to touch when the legs and ankles hang straight down —
  [`../../../robot-build-plan.md`](../../../robot-build-plan.md) carries both. The model needs no
  edit; `make_plans.py` and the sheets do, in draft9p1p1.
- **Whether `make_plans.py` gets the gripper's real body.** `clip()` and `clip_front()` still draw
  an 18 × 24 slab while `clip_front()`'s own docstring already claims the flushness B8 built. The
  sheets and the model disagree about one part.
- **The socket's slit is 8.0 long and the source comment says 11.0.** `make_plans.py` line 73 calls
  `SLIT_W` *"the socket's relief slit, four of them, the collar's whole length"*. The model stops
  the slit `#wall` above the collar's root, leaving a solid ring that holds the four tabs together.
  The model is right; the comment and the sheet label at line 414 are not.
- **Whether 2.92 mm of wall holds a snap fit at this size, and whether the mouth at 96% of the ball
  goes together by hand.** Both are print questions and nobody has printed the 2× robot. This is
  draft9p0's open question carried forward unchanged, with a wall 0.72 thicker than it measured
  there.
- ~~Whether the head's depth wants to be driven rather than declared.~~ **Settled on 2026-08-27: it
  is driven, and stays driven.** `#headD` = `#torsoD * 5 / 4` in the model and `HEAD_D` =
  `TORSO_D * 5 / 4` in the source, so nothing needs building; what changes is that the rule is now
  a requirement rather than the way it happens to be written.
  [`../../build-briefs/head.md`](../../build-briefs/head.md) carries it.

## What draft9p2 inherits

A version, a design source and a log. Not a guide and not a frame.

- **The model** is `stickbot-draft9p1` at `Recovery point` `8504f457723606c65c2ab48f`.
- **The design source** is `make_plans.py` and the `r6` sheets, which C1 shows the model agrees with
  everywhere the two were compared, and the four places above where they do not.
- **The log** is [`b/notes.md`](b/notes.md), which records what each dialog did as well as what each
  feature became. Twenty-odd of its notes are Onshape behavior that cost this run time to learn and
  that 9p2 does not have to learn again.
