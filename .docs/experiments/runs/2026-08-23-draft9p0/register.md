# draft9p0 — the register

What was built, what it measures, what changed under the plan, what the user has asked to change,
and what is still open. The plan is [`plan.md`](plan.md); the build's own log is
[`b1/notes.md`](b1/notes.md) and the requirements it could not meet are
[`b1/unmet.md`](b1/unmet.md).

**All fourteen tutorials are built, versioned and written, and the robot stands.** The model has
been read back and checked against the sheets — that is B2, in
[`b1/b2-readback.md`](b1/b2-readback.md) — and driven from its variable table and put back, which is
B3, in [`b1/b3-driving.md`](b1/b3-driving.md). **Every phase of the plan has been run**, though
Phase C was run as a build with a log rather than through the take harness — see *Phase C did not
use the take harness* below. What follows says what the finished model measures and what it still
gets wrong.

## Where the work is

| | |
| --- | --- |
| document | `stickbot-draft9p0`, `0f4b79a78707651ae20df5b2` |
| workspace (live) | `d7b87030a78288b62a42de72` |
| last version | `t14 legs`, `737db64e2567c96e2d3de63f` |

| element | eid |
| ------- | --- |
| `stickbot` (Assembly) | `546a5e79d793ec8ac2bc902e` |
| `robot sizes` (Variable Studio) | `97046dd200d2da1151f9008b` |
| `body` | `02e4961f71e6767fb7d7d639` |
| `head` | `661eb771f054d4d12b351fbf` |
| `ball and socket` | `f16153ba9741661febc6ba0a` |
| `foot` | `19accde64ded8a3a4e3cf429` |
| `hinge` | `d7401eebccc0e7c8681f5bac` |
| `u limb` | `a820d29c079b23a14a2b2385` |
| `l limb` | `454ab6f22f9df4f86778b537` |
| `gripper` | `614e820e82591f54aad4a4eb` |

`stickbot` and `stickbot-for-bot-review` were not written to. Nothing was pushed: the run was asked
to hold everything local, and it did.

## State and version, tutorial by tutorial

`state` is this run's, not the plan file's. `version` is the named Onshape version the tutorial
ended on, which is what a later page cites.

| # | Tutorial | state | version | page |
| - | -------- | ----- | ------- | ---- |
| 1 | variables and torso | built, one frame | — | `torso.rst`, hero only, rolled back |
| 2 | the head | built, one frame | — | `head.rst`, hero only, rolled back |
| 3 | the assembly, two parts | built, one frame | — | `assembly.rst`, hero only, rebuilt |
| 4 | the ball and socket | built, one frame | — | `ball-and-socket.rst`, hero only |
| 5 | the head gains its socket | built, one frame | — | `head-socket.rst`, hero only |
| 6 | the torso grows its joints | built, framed | — | `torso-joints.rst`, 10 frames |
| 7 | the head is mated | built, framed | `t7 head mated` `acc35f11ec85129825dfdbee` | `mate-head.rst`, 4 frames |
| 8 | the foot | built, framed | `t8 foot` `3d7b30559398005be8c9909f` | `foot.rst`, 15 frames |
| 9 | the hinge | built, framed | `t9 hinge` `dcb3dcc42e49e130ce163031` | `hinge.rst`, 17 frames |
| 10 | the upper limb | built, framed | `t10 u limb` `7d293115a90ebec16359ccf7` | `upper-limb.rst`, 10 frames |
| 11 | the lower limb | built, framed | `t11 l limb` `b5617bfbc551a3949f4cf02a` | `lower-limb.rst`, 12 frames |
| 12 | the gripper | built, framed | `t12 gripper` `5324ccf7cef995c69366e6a6` | `gripper.rst`, 9 frames |
| 13 | one arm, then the other | built, framed | `t13 arms` `0be0c433c7c1f3f8847ea7e5` | `arms.rst`, 15 frames |
| 14 | one leg, then the other | built, framed | `t14 legs` `737db64e2567c96e2d3de63f` | `legs.rst`, 21 frames |

**Tutorials 1 through 6 have no version of their own.** The first version this run published is
`t7`, so those six tutorials are recoverable only through `t7`, which contains all of them.
Publishing per tutorial started once the parts began to be worth losing, which is later than the
*Recovery point* gate asks for.

**A hundred and twenty-six frames sit under `images/` and a hundred and twenty-one are used.**
The capture run's own frames are in [`b1/frames/`](b1/frames/); the retakes below were shot later
and written straight into `instructions/stickbot-draft9p0/source/images/`. No page names a frame
that is not on disk, and Sphinx builds the guide with no warning.

**Five frames the capture run could not use have been retaken.** Each retake is shot with the
feature tree rolled back to the step the frame is about, and each ring is drawn on the pixel
Onshape's own status bar gives for that connector rather than placed by eye. Every rollback was
undone and the undo checked against the face count REST reports:

| Frame | Why the first one failed | What the retake does |
| ----- | ------------------------ | -------------------- |
| `hinge/blade.pattern_axis.closeup` | its ring was drawn beside the part, not on it | rings the stub axle's end face, status bar reading y −6.6 mm |
| `u-limb/move_fork.closeup` | zoomed so far in it was a gray wall with a triad on it | the bottom view, where the end disc faces the camera |
| `l-limb/move_stud.source.closeup` | did not say which of its two triads the ring marked | shot in `ball and socket`, where the stud carries one connector and nothing overlaps it |
| `torso-joints/connectors.r_shoulder.closeup` | read identically to the left one | replaced by `connectors.r_shoulder`, shot from the robot's own right |
| `torso-joints/connectors.r_hip.closeup` | the same | replaced by `connectors.r_hip` |

Two of the three retakes taught something the page did not say. The l limb's **From** connector
cannot be photographed in its own tab at all: the derive drops the ball stud on that tab's origin,
which is inside the blade, so nothing of the stud is on screen — the page now says so. And the u
limb's `mate for fork` sits on a downward-facing disc, which the default isometric cannot see.

Five frames are still unused, and they are sound ones the page had no room for —
`arms/pose.straight`, `legs/copy2.tree.before`, `legs/copy2.tree.after`, `legs/mate.ankle.pick1`,
`legs/pair.bent.closeup`. `legs/copy2.tree.after` is also clipped before the two bracketed mate
names, which is why `legs/copy2.paste.graphics` carries that lesson instead.

The three close-ups were the *reframe often* lesson arriving as evidence: a close-up taken without
checking what is in the frame is a frame that cannot be used later, and the cost is not visible
until the page is being written. Retaking them cost one capture pass per tab.

## What the model measures

Every number below was measured off the model, not computed from the plan. The full B2 read-back —
ten bounding boxes, the radius census, the cut-face stations and the per-part wall table — is in
[`b1/b2-readback.md`](b1/b2-readback.md); what follows is what it settled.

| part | volume | extent |
| ---- | ------ | ------ |
| `torso` (with its five studs) | 343120.267 mm³ | 72 × 48 × 96 before the studs |
| `head` | 263585.819 mm³ | x ±36, y −33 … +30, z ±36 |
| `Ball stud` | 1028.968 mm³ | ball r 6.000, stalk r 3.000 |
| `Socket body` | 1531.591 mm³ | collar r 9.000, z −7.4 … +3.6, mouth Ø11.538 |
| `u limb` | 40171.463 mm³ | x, y ±12, z −112.4 … +3.6 |
| `l limb` | 40056.825 mm³ | x, y ±12, z −108 … +12 |

**The chain of joint centres closes without a number being typed twice.** The head's socket cavity
centre is at −43.4 in its own tab, the torso's neck ball at +58 in its, and the Ball mate makes
them one point — which puts the top of the head at **137.4**, exactly where `make_plans.py` puts
it. That is the whole argument for building each part around its own joint centre, and it is now
measured rather than asserted.

**The finished robot stands 421.8 mm, and the plan sheet says 315.4.** Every station below is a
measurement off the parts, not a number off the assembly's bounding box:

| station | z, as built | from |
| --- | --- | --- |
| head top | +137.4 | `head`, and `HEAD_T` agrees exactly |
| hip ball | −58.0 | `body` |
| knee pin | −158.4 | the `u limb` pin axis, at z −100.4 in its own studio |
| ankle ball | −260.4 | the `l limb` ball stud, at z −102 in its own studio |
| sole | −284.4 | the `foot` box, z −24.0 … 3.6 — `FOOT_H` exactly |

137.4 + 284.4 = **421.8**. The whole of the 106.4 mm gap against the sheet is the two limb
segments: 100.4 and 102 where `LEG_SEG` is 48. That is the `#limbSeg` defect below and nothing
else. **`FOOT_H` is right, `HEAD_T` is right, and the hip station is right.**

**An earlier draft of this register said 431.97, read off the assembly bounding box. That number is
wrong and it is worth saying why.** The bounding box of a posed assembly is not a standing height.
Both feet are tilted — 12.74° and 9.60°, measured off their occurrence transforms — and a tilted
96 × 48 sole puts a corner lower than its own ball centre by more than `FOOT_H`. The 34.4 mm that
looked like a deep foot was that corner. The same mistake would have been caught by the rule this
register already states two paragraphs down about the feet not being symmetric: *a posed assembly
cannot be measured*. It applies to the height as much as to the symmetry.

**The variable table drives the whole robot, and drives it back.** `#torsoH` was set to 120 and to
96 again, and `#torsoW` to 90 and back to 72; after each round trip every bounding box, every radius
and count, every cut-face z and every face area matched what B2 had measured, to six decimal places.
At 120 the ball went 6.000 → 7.500 and every jointed part followed it — cavity 6.800 → 8.300, collar
9.000 → 10.500, limb 12.000 → 15.000, foot 48 × 96 → 60 × 120. The whole account is in
[`b1/b3-driving.md`](b1/b3-driving.md).

**The printed wall is 2.20, measured as material on five parts.** The plan asks for it to be
measured in B2 as the thinnest wall in the part, and `head`, `Socket body`, `Foot`, `u limb` and
`Gripper` each read exactly **2.200** between the r9.0 collar and the r6.8 cavity. `COLLAR_WALL` is
named 3.0 and that is the wall off the ball; `#fit` eats 0.8 of it and 2.20 is what prints. The
measurement has to be taken within one part — across a whole studio the thinnest concentric pair in
`ball and socket` is 0.800, which is `#fit`, a clearance between two parts that never touch as
plastic.

**The head is 63 mm deep where `HEAD_D` is 60.** The defect is below; B2 is where it was found.

**The socket's frame carried into four tabs unchanged.** `ball and socket` puts the ball centre on
the origin, so a Derived at **Base origin** lands the joint where it belongs in `head`, `foot`,
`u limb` and `gripper` with nothing to move it. That deleted a step from tutorial 8 and two from
tutorials 10 and 11 — the transform-by-connector each of those plan files calls for is a no-op.

## Resolved

- **The 2× robot builds.** Every part above regenerated `OK` at `#torsoH` 96, and the assembly
  closed. Nothing about the doubling broke geometry.

- **The blade's slit is out, settled by printing rather than by arithmetic.** The printed joints
  from `stickbot-for-bot-review` work without it. `make_plans.py` now draws a solid blade in both
  hinge views, the joints-to-scale figure and `detail_hinge`'s two extra views are gone, and the
  sheets are frozen as r5. `SLIT_W` stays in the file because the **socket's** relief slits still
  use it.

- **The solid blade's cantilever numbers are worse on paper than the split blade's, and are
  reported as such.** The ear now gives the whole 1.0 mm of travel on its own: **51.30 MPa**
  against PETG's 50, and **36.34 kgf** to press together, where the split blade read 19.2/20.1 MPa
  and 13.6 kgf. The printed parts beat the estimate, which is what settles it. If a 2× joint turns
  out too stiff in the hand, the number to move is `STUB_PROUD` against `GAP`, not the slit.

- **A mate connector with no Owner part does not exist outside its Part Studio.** The torso's five
  connectors were built without one. They worked inside `body`, drove transforms, drew their
  triads, and the assembly tree showed the `torso` instance with **no expand chevron at all**. The
  repair is per connector and takes about a minute each. Ticking *Owner entity* is not enough — the
  tick only reveals the field, and something has to go in it.

- **Not every connector wants an owner.** The three that only drive a transform inside `body` are
  better left without one, so the assembly tree is not five near-identical rows to pick wrongly
  from. That distinction is now written into the guide rather than applied as a blanket rule.

- **A concave sphere does not offer its centre.** Every convex sphere in this document gives a mate
  connector its centre for free. The socket's cavity does not, which is why the head's page picks
  the cavity face and the limb pages pick a pair of edges instead. Both picks in a pair must be the
  same kind of entity: an edge paired with a face averages a circle centre against a face centroid
  and lands between them.

- **A feature pattern of a Remove extrude fails silently until *Reapply features* is ticked**, and
  `Feature mirror` needs the same tick for the head's second eye. In the mirror's case Onshape
  names its own fix in the error text.

- **Onshape has no sketch slot tool in the rectangle group.** The group is Corner / Center point /
  Aligned. The Slot tool is its own button, it draws a preview rather than a result, and **Escape
  discards it silently** while Enter keeps it. That cost one full rebuild of the head's mouth.

- **A Blind extrude's `Starting offset` measures back toward the sketch plane.** Offset 27 with
  depth 3 on the Front plane cut a sealed void inside the head with the correct volume removed and
  nothing visible on the face. Volume alone does not catch it; the cut face's coordinates do.

- **Both of tutorial 3's open questions are answered.** The insert dialog inserts on a single click
  of a Part Studio row and stays open, so "separately" is simply what happens and there is no
  "together" to choose. And a mid-drag frame of the tab move is capturable but not worth taking —
  Onshape reorders the strip live, so it is nearly identical to the after frame.

- **The head's eyes are the plan's Ø20 circles, not run 3's ellipses.** That settles a conflict
  between the brief and run 3 in the plan's favor, and it costs Stage 3 its only home for the
  Ellipse tool. Something else has to teach Ellipse or the tool leaves the course.

- **The gripper's width can be built from the collar's numbers but not from its geometry.** The
  width runs along the extrude axis, and an extrude depth cannot reference another body's diameter.
  The honest construction is `#collarR = #ball / 2 + #wall` and a symmetric extrude of
  `2 * #collarR` — a shared expression, not a shared face.

## Defects found, and where they are recorded

- **`#limbSeg` and `ARM_SEG`/`LEG_SEG` do not mean the same thing.** `make_plans.py` measures a
  segment joint centre to joint centre; the model extrudes `#limbSeg` of stock and then stands each
  joint off the end face — 7.4 for a socket, 45 for a fork, 44 for a blade, 10 for a ball stud. A
  48 segment would need **negative** stock on both limbs. The minimum these joints admit is 52.4
  above the elbow and 54 below it, with no rod between them at all. draft9p0 built what the plan
  files say to build, which gives segments of 100.4 and 102. **That minimum is arithmetic about
  standing the joints off the end face, and U6 below withdraws the method rather than the number**
  — carved into the segment as the sheets draw them, the same joints cost about 21 and 20.

  **This is older than the doubling, and doubling made it far worse than twice as bad.** All four
  limbs were measured read-only over REST on 2026-08-24. `stickbot-for-bot-review`'s segments are
  **28.26** and **29.11** against a 1× sheet that said 24 — an overshoot of 4.26 and 5.11.
  draft9p0's are **100.4** and **102** against a 2× sheet that says 48 — an overshoot of **52.4 and
  54**, about twelve times as large. The parts are 3.28× and 3.17× the reference overall while the
  limb's diameter is 24 against 12, exactly 2.000×. The fix is one variable and it is the user's
  call which way it goes; nothing else in the model has to move. Written up in
  [`10-u-limb.md`](../../../build/plan/10-u-limb.md) and
  [`11-l-limb.md`](../../../build/plan/11-l-limb.md), which is where the plan says a disagreement
  goes.

- **The robot stands 421.8 mm where the plan page says around 320.** Built from measured stations,
  in *What the model measures* above. All 106.4 mm of the difference is the limb defect above and
  is fixed by the same one variable — no other station is out.
  [`plan.rst`](../../../../instructions/stickbot-draft9p0/source/plan.rst) says *around 320 mm* and
  [`index.rst`](../../../../instructions/stickbot-draft9p0/source/index.rst) says *around 420*.
  **They disagree on purpose**: the index states what this build measures, the plan page states
  what the sheets draw, and the two only agree again once `#limbSeg` is settled.

- **Neither knee has a Width mate, and neither elbow does either.** All four hinges are a bare
  Revolute, so each lower limb can slide sideways inside its fork.
  [`assembly.md`](../../build-briefs/assembly.md) is explicit — *"A Width mate is not optional
  decoration on a hinge"* — and asks for one per hinge at 0.6 mm clearance each side. Neither
  `13-assembly-arms.md` nor `14-assembly-legs.md` has a Width step in its table, so the build
  followed the step tables and the brief lost. Run 4 skipped it too. `arms.rst` and `legs.rst` both
  end by saying the mate is missing and what it would do, which is the honest thing a page can do
  about a joint it did not build.

- **The whole assembly is saved posed, and the feet are not symmetric.** Foot centres sit at
  x +26.05 and −31.42. `assembly.md` asks for feet 8 mm outboard with their inner edges at x ±8,
  which cannot be read off a posed model — every joint below the hip is a free Ball or a free
  Revolute, so the feet are wherever the last drag left them. The two z values agreeing to 0.45 mm
  is the part of that check the pose does support. **The acceptance check needs to name a pose**
  before it can be run at all.

- **`#wall` is declared in three tabs with two different meanings, and they agree only at 96.**
  `ball and socket` says `3 mm`; `foot` and `gripper` say `#torsoH / 32`. Both `foot` and `gripper`
  build their own collar as `#ball / 2 + #wall` and wrap it around a socket *derived* from
  `ball and socket`, whose collar used the literal 3 — so at 96 both collars are 9.000 and merge
  into one face, and at 120 the part's own collar is 11.250 around a socket of 10.500. The foot
  grows a sixth cylindrical face and a 0.75 mm ledge at z −7.4; the gripper's x follows its own
  collar to 22.500 while its y follows the derived socket to 21.000, so the part changes shape
  rather than size. The fix is one line in each of two tabs, not three sketches. Task #28 already
  has the gripper's overhang fore and aft; this is the same part failing in the other axis, from a
  different cause.

- **The hips are placed by `#torsoH` and the shoulders by `#torsoW`**, written side by side in the
  `body` tab as `#hip_half = #torsoH / 4` and `#shoulder_half = #torsoW / 2`. Both look right at the
  built size. Drive `#torsoW` to 90 and the shoulders move out to ±45 while the hips stay at ±24, so
  the body overhangs each hip by 21 mm. This is the one of these where the wrong variable is written
  down in plain sight.

- **The head tab holds no variables at all**, alone among the eight Part Studios, and its width
  follows `#torsoH` — 72 at 96 and 90 at 120, while driving `#torsoW` leaves it untouched. At the
  built size `0.75 × #torsoH` and `#torsoW` are both 72, so nothing in the tab or on the model says
  which one the head depends on.

- **The torso's shoulder pads are a typed `#boss_d = 16 mm` that never follows.** The margin around
  a shoulder ball is 2.0 at 96 and 0.5 at 120, and at `#torsoH` = 128 the ball would be r8.0 and the
  pad would vanish into it.

  All four are in [`b1/b3-driving.md`](b1/b3-driving.md), with the expressions they were read from
  in [`b1/b3-variables.json`](b1/b3-variables.json). **Three of them cannot be seen at 96 by any
  measurement of the built robot**, because two definitions that evaluate the same are
  indistinguishable from one. Driving the variable is the only check that separates them.

- **The head measures 63 mm deep where `HEAD_D` is 60.** The head's box runs y −33 … +30, and all
  3 mm of the excess is on the front face: the eyes stand proud of it and the sheet draws the head
  as a plain 60-deep box. Nothing in the model depends on the number — the head is built from its
  own joint centre — so this is wrong on the drawing rather than in the print, and it is one more
  argument for the head's depth becoming a real variable instead of a literal typed twice. Found by
  B2, which is the only check that reads a part's own extent, and confirmed by B3: the head measures
  63 deep at `#torsoH` 96 and 63 deep at 120, while its width goes 72 → 90.

- **The hinge's snap direction disagreed between the brief's table and the model, and the model
  won.** draft9p0 built the axle on the **blade** with the bore through the **fork**, following
  the plan's step tables and the brief's *Which side the snap is on*; `make_plans.py` and the
  brief's numbers table both still drew stub-on-ear with a pocket in the blade. A7 was scoped to
  the slit and did not touch it. Settled 2026-08-24 in favour of what was built, on the printing
  argument the brief already carried: a bore straight through an ear needs no ceiling over it,
  where a blind pocket does, and the spring arithmetic is identical either way — the ear is the
  only member that bends, and `MOVE` is `STUB_PROUD - GAP` whichever side the axle is on. The
  sheet, the brief and `09-hinge.md` now say the same thing. Task #56, closed.

- **The gripper body does not follow the socket's outside profile**, so it overhangs — and the
  overhang changes sign around the joint. Measured on the built part: the Ø18 collar stands 4.0
  proud of the 10-deep clip fore and aft, in two crescents of 42.106 mm² that taper to nothing at
  x ±7.4833; at the ends the 18-long clip stands proud of the round collar instead, in four tongues
  of 2.436 mm² reaching 5 of overhang at x ±9. No stem width reaches flush, because a round collar
  and a straight-sided slab cannot share an outline. Known before the run; task #28.

- **`gripper.md` says the mouth opens forward at +Y, and the robot faces −Y.** The build followed
  the brief first and the finished part gripped behind itself; measuring the lips caught it and
  `clip profile` was rebuilt to open −Y. `build-briefs/README.md` settles the frame in one line —
  "The robot faces −Y" — so the brief's "(+Y)" is the stale half. Reported, not edited: it belongs
  to whoever next revises the briefs.

- **Three source disagreements on the gripper, found by reading before building.** `make_plans.py`
  draws the bore fore-and-aft while `12-gripper.md`'s acceptance list wants it parallel to X;
  `make_plans.py`'s stem is a literal 6 that never doubled, against the planned `2 * #clipR`; and
  the mouth's sign above. The build followed `gripper.md` on the first, `2 * #clipR` on the second
  and the README on the third. The first two belong to B2 and neither has been settled.

- **The elbows have no Width mate, and `assembly.md` says they must.** The brief is explicit — *"A
  Width mate is not optional decoration on a hinge"* — and asks for the blade held centered in the
  fork with 0.6 of clearance each side. The step table in
  [`13-assembly-arms.md`](../../../build/plan/13-assembly-arms.md) does not list one, and run 4
  skipped them too. draft9p0 followed the step table. Without it each Revolute leaves the blade
  free to slide along its own axis, so an arm can be pushed sideways in the fork. The page says so
  in as many words. Two sources want it and the one that drives the tutorial does not.

- **The assembly's instances were inserted from the workspace, not from a version.**
  `assembly.md` says *"You insert from versions, not from workspaces"*, and the Insert dialog's
  **Current document** tab offers no version picker — clicking "Main" opens nothing. Every instance
  in `stickbot` therefore follows the live workspace, including the torso and the head from
  tutorial 3, so a change to a Part Studio changes the robot underneath it. Fixing it means
  re-inserting every instance and rebuilding every mate. Recorded, not fixed.

- **`upper rounds` was built at r12 where the plan types 6.** The 6 is typed rather than derived,
  so A2's scale pass did not touch it. Whether it should have doubled is undecided, and the head
  page says so.

- **The head's Ø8 pupils were not built.** No step, no depth. Undecided.

- **Two figure captions were wrong, and both were found by opening the picture.** `hinge/tree.png`
  read *forty-nine features* where the picture reads **fifty-three**. `torso-joints/hero.png` was
  captioned *five studs* and showed one: the three planes were on, a construction plane's label sat
  on the torso's corner, and from a corner the box stands in front of the other four studs. It was
  retaken as a **Front** view with the planes hidden, where all five read, and the caption now says
  why that view. Task #26 exists for exactly this.

- **A third caption was wrong, and the model was wrong about it too.**
  `hinge/blade.pattern_axis.medium` was captioned as a construction axis and showed a half-finished
  **Mate connector** dialog on the stub axle's face. The model has no construction axis: the
  feature named `axis for circular patterns` is a mate connector on that face, and both the blade's
  24 valleys and the fork's 24 bumps turn about it. The hinge page, the build brief and the frame
  now all say mate connector. It was found while retaking the close-up beside it, which is an
  argument for auditing figures in pairs.

- **Every caption that asserts a count was then checked against its picture**, which is 44 of the
  guide's 116 figures — every `Features (N)`, every `Instances (N)` and `Mate features (N)`, and
  every count written out in words. All of them agree. The assembly counts also chain: 5 instances
  and 4 mates at the start of the arms page reach 14 and 13 at the end of the legs page, and every
  intermediate figure sits on that chain. The rest were audited afterwards, below.

- **All 121 figures were then opened and read against their own alt text and caption**, which is
  every figure the guide references — `before-you-start.rst`, `habits.rst` and `index.rst` carry
  none. Twenty-nine disagreed. Twenty-one were wrong in prose only and are fixed: three dialogs
  named that had already been accepted, a first mate pick named as the wrong part, a groove placed
  at the heel instead of the toe, a version count, a *Closer still* on a frame further out than the
  one above it, a mirror the picture cannot show, a slit count, a connector pair counted twice
  because the move made the two coincident, a copy and its original the wrong way round, a leg
  swung sideways described as swung forward, and the superseded 431.97 mm height now named as the
  assembly bounding box it is.

  **Two of the twenty-nine were the same picture used twice under different names.**
  `torso-joints/connectors.medium.png` is byte-identical to `studs.combine.png`, and
  `foot/connector.png` was byte-identical to `foot/hero.png`. A duplicate passes every check that
  reads a caption against a picture, because the picture it is read against is a real picture — it
  just is not this figure's. Comparing file hashes across a page's images is the check that finds
  it, and it costs nothing.

  **Three mismatches are the end-state frame standing in for a mid-build one** — the same class #59
  had to reshoot. `l-limb/ends.medium.png` is captioned *before either connector goes on* and its
  own feature tree ends in `wrist end`. The end-state frame is the cheapest one to take and the
  easiest one to caption wrongly.

  **Two frames carry a stray "Go to documents" tooltip**, from a pointer left on the Onshape logo
  when the shutter fired. Parking the mouse in `gui.EMPTY` before every frame is what the helper
  does now; these two predate it.

  **Five of the eight frames that needed the camera were retaken; three could not be, and the
  reason is that a pose is state this build treated as scenery.** Geometry can be recovered from a
  rolled-back tree, which is how the heroes for tutorials 1 to 3 were shot. A pose cannot be
  recovered from anything: dragging a joint overwrites it, and the version that could have held it
  is already published. `t13 arms` is the only legless state on record and its saved pose is the
  folded-across one, so the arms page cannot get the arms-down hero its caption was written for;
  `t14 legs` holds a stride, not the square stand the finished-robot frame shows. A page that
  shoots a pose has to take every frame of that pose before it drags the next one. Listed with what
  each still shows in [`b1/unmet.md`](b1/unmet.md).

  **A version view cannot stand in for a workspace frame.** Opening a version read-only puts a
  *"Versions are view only"* banner across the top of the canvas with no × on it, which rules out
  the obvious workaround.

  **Three errors are frozen in published version descriptions** — *ball centre* in `t10`, *wrist
  centre* in `t12`, and the 431.97 mm height in `t14`. A version description cannot be edited after
  it is published, so these are permanent, and they are written down here so they are not
  rediscovered as live defects. The guide now says in `legs.rst` that the number in `t14` is the
  assembly's bounding box and not the robot's height.

- **`ninja check` failed on fourteen British spellings this run did not write, and now does not.**
  They were in `pre-plan.md`, two `robot-guide4` pages, `.docs/onshape-gui-howto.md`,
  `plan/01-torso.md`, `plan/02-head.md` and `.docs/experiments/sketches/slit-reach.py`, dating from
  2026-08-21 and 2026-08-23. Fixed on 2026-08-24, one named line at a time. `pre-plan.md` needed
  more than a word swap: its own paragraph about the failing gate quoted three of the failures as
  examples, so the paragraph was rewritten rather than corrupted, and the stale line numbers it
  cited went with it.

  **The lesson is in how long they survived.** Every one of them was reported by `ninja check` on
  every run for days, and the report was read as background noise because it was never empty. A gate
  that is always red is a gate nobody reads.

**Six page and frame conventions came in at zero, from one cause.** This draft's plan names
`robot-guide4`'s `ball-and-socket.rst` as the source of *"the conventions the other two pages lost:
toolbar close-ups, view keys, video links"*. draft9p0 took the prose from all three of that guide's
pages and the conventions from none of them. Counted across the whole guide:

| | draft9p0 | `robot-guide4` |
| --- | --- | --- |
| toolbar close-ups, `:class: button` | 0 | 15 |
| video links, *'Bot video of similar steps.* | 0 | 12 |
| step pictures written as `image::` rather than `figure::` | 0 of 121 | 194 of 198 |
| a tool named with its key, *(or press …)* | 0 | 3 |
| the key press as the action, *press **n** to look **n**ormal* | 1 | 6 |
| `.. step:` tags | 0 | 0 |

**One defect, not seventeen page defects.** No page is individually at fault and no page can be
individually repaired: the same hole would open again in the next draft, because what failed is
what a page is made of and not what any page says. The repair is one capture pass and one rewrite
of the step blocks, to the form
[`req.page.instruction_first`](../../../build/drafts.md) now states.

**`req.page.view_keys` is scored met on a reading the requirement does not support.** It asks that
the page where a view key was pressed tells the reader to press it and says what they will see.
`press **` appears once in the guide, in `habits.rst`. Stating the keys once on a habits page is a
different thing from telling a reader to press one where the build pressed it.

**`req.page.step_tag` has never been performed by any draft.** No `.. step:` tag appears in
`robot-guide2`, `robot-guide3`, `robot-guide4` or this guide, though
[`steps.md`](../../../build/steps.md) defines the identifier one would carry. This is not a
draft9p0 regression. It is a requirement claimed by every plan and met by nothing, and the next
plan that claims it has to say how a tag gets written.

**The prose counts what the tree holds, in 52 places across twelve of the seventeen pages.**
`req.page.no_counts` asks for no running tallies and nothing that has to be re-edited when an item
is added. *"Fifty-three features, two parts"* under the hinge's tree, *"Thirty-two features, one
part"* under the foot's, *"Fourteen instances, twelve mates"* on the legs page: each is a number a
student checks against their own screen, and each is wrong as soon as a feature is added or a plan
file changes. A few of the 52 are stable — Onshape has eight mate types whatever this robot does —
and the rest follow the model. The drawings had their counts removed for this reason; the pages
did not.

**Two single-site defects, named because they are not classes.** `gripper.rst` calls the gripper a
hand — *"a hand that grips behind itself"* — against `req.page.part_names`. And 31 numbered list
items across five pages stand without the approval
[`prose-style.md`](../../../../.parts/prose-style.md) requires for numbered lists in prose.

## Requirements unmet

**The Onshape session expired mid-build and needed the user to sign in again.**
`agent_browser.py` borrows its cookies from the signed-in browser and answered *"the borrowed
cookies carry no session"*; restarting it does not help. The user signed in, the run resumed and
tutorial 12 finished. Full account in [`b1/unmet.md`](b1/unmet.md).

| Requirement | State |
| ----------- | ----- |
| `req.model.one_document` | met — one document, one tab per tutorial, the joint a tab and not a document |
| `req.model.design_intent` | met — `#torsoH` driven 96 → 120 → 96, and `#torsoW` 72 → 90 → 72; both round trips came back identical |
| `req.page.hero` | met — every page has one. Tutorials 1 to 3 were shot afterwards, two from a rolled-back tree and one from an assembly built for the shot |
| `req.page.view_keys` | met, in `habits.rst`, and stated once rather than per page |
| `req.shot.toolbar` | **unmet** — no page carries a toolbar close-up. `robot-guide4` has fifteen |
| `req.shot.two_frame` | **unmet** — five medium-and-close-up pairs exist, against 197 features |
| `req.shot.planes_hidden` | **partly unmet** — `foot/outline_sketch.png` draws over a labeled Top plane and a second plane behind it |
| `req.shot.caption_moment` | met — all 121 figures read against their own caption; 21 prose fixes, five retakes, three that cannot be retaken |
| `req.shot.true_state` | met — the one violation, the head's mouth, was thrown away and reshot in the true order |
| `req.shot.one_use` | met — no two figures on any page share bytes |
| `req.shot.width` | **unmet** — `custom.css` delivers four-fifths-and-centered through `img.shot`, and the guide uses none |
| `req.guide.plan` | met — `plan.rst`, with the r5 sheets |
| `req.guide.before_you_start` | met |
| `req.guide.habits` | met — seven habits, the view-key table and the keystroke trap |
| `req.guide.size_once` | met — the height is on the plan page only, and it is stated as both numbers, 315.4 drawn and 421.8 built, because which one is right is still open |
| Recovery point | partly met — versions from `t7` on; tutorials 1 to 6 share `t7` |
| Steps reproduce | **not performed** — no page was rebuilt from its own text |
| Names are real | met — all 197 features across the nine Part Studios and the assembly read back over REST on 2026-08-24, and not one carries a default name |
| Links resolve | met — every relative link in this run's directory and in `.docs/build/` resolves. Fourteen in `b1/` did not until they were repaired, thirteen of them the same off-by-one in the path depth |
| Model inspected | met — [`b1/b2-readback.md`](b1/b2-readback.md) |
| Caption reads true | met — all 121 figures read against their own caption and alt text; twenty-one prose fixes, five retakes, three frames that cannot be retaken |
| Spelling | met — the fourteen failures that pre-dated this run were fixed, and `ninja check` is clean |
| Reading level | tracked, not adjudicated; the new pages sit where the rest of the guide sits |

**`req.shot` was claimed and never scored.** The plan's declaration claims all of `req.shot`,
nothing deferred. The table above did not carry a single one of its seven rows until 2026-08-25,
so the run closed reporting every claimed requirement accounted for while four were not. Two
structural causes sit under the four, and both are visible in the guide rather than in the log:

- **The guide writes `figure::` where `custom.css` expects `image::`.** The stylesheet says a step
  shot is a plain image at four-fifths width, because the instruction is the paragraph above it,
  and a figure is one of the two captioned overview pictures at the top of a page. This guide has
  **121 figures and no images**; `robot-guide4` has 194 images and 4 figures. Every step shot here
  is styled, and written, as an overview picture.
- **A dialog can only be photographed while it is open.** The frames were taken after a feature was
  accepted, on the graphics area, so there was nothing left to show. That is the same cause as the
  missing toolbar close-ups, and it is why `req.shot.toolbar` is at zero rather than merely thin.

**`Names are real` was scored against the model, not against the frames.** All 197 features read
back over REST carry a name nobody defaulted. Two sketch frames — `hinge/blade.profile_sketch.png`
and `foot/outline_sketch.png` — show `Sketch 1` in the feature tree and in the open dialog, because
the rename happened after the shot. The gate reads the document; the student reads the picture.

**Phase C did not use the take harness.** The plan asks for fourteen takes per
[`takes.md`](../../../build/takes.md) — a `Take` per part, a `Step` per leaf, `shows` on every
frame, `key()` on every keystroke and a verdict per step. What this run did instead was drive
Onshape from hand-written scripts and keep one long log, [`b1/notes.md`](b1/notes.md). The outputs
a take owes are all there: frames, a log, a named version per tutorial from `t7` on, and the
differences against the plan, which are the defects above. What is missing is everything that makes
those outputs checkable by something other than reading them — no frame carries what it is meant to
show, no step carries a verdict, and the guards `takes.md` requires were in force only where a
script happened to implement one. `tools/gui_steps.py` exists and no script in
[`b1/scripts/`](b1/scripts) imports it.

**That is why *Steps reproduce* is not merely unperformed but unperformable from this run's
record.** A take from `empty` is the only start that settles whether the words work, and there is no
step-level record here to compare a rebuild against. The next run that wants that gate has to
perform it, not reconstruct it.

**B2 ran, and it is written up in [`b1/b2-readback.md`](b1/b2-readback.md).** All five checks the
plan asks for — bounding boxes, collar diameter, mouth, thinnest wall, and the z-extent of every
cut face — were read off the model over REST and compared with `make_plans.py`. **No cut came out
at half its depth**, which is the failure the check exists to catch. It found one new thing, the
head's depth below, and it caught two things this register had itself got wrong: the 431.97 height
and a foot defect that was never real. The read-back is what withdrew both.

## User requirements, dictated 2026-08-25

Five changes to the CAD structure, taken down as notes and not acted on. Each is stated against
what the model does today, read off `make_plans.py` and [`b1/notes.md`](b1/notes.md), so the change
is described against what is there rather than against memory. None has been designed: the
arithmetic each one needs is what the next run owes.

**U1 — the eye profile is an ellipse, not a circle.** Take the profile from the example stickbot,
scale it 2× and position it 2×, so the eye clears the head's fillet instead of running into it.
Today `make_plans.py` draws each eye as a circle, `EYE_R = HEAD_W * 5 / 36`, and the built head
follows the sheet. Two things are to be read off the example rather than guessed: which document is
the example, `stickbot` `5dc85bc34f28cf4f6cee1f26` or `stickbot-for-bot-review`
`111f975041ddb104a6028d45`; and which of the head's rounding features the eye runs into.

**U2 — `#fit` goes to 0.08, and the CAD math absorbs it locally.** Dimension the joint at an
extreme fit, likely 0, so that the socket's height does not move when `#fit` moves, and the ball's
position is the free variable that recovers a reasonable range of motion. A clearance change does
not ripple into any other robot dimension. Widening the slits, shrinking the socket height, or
both, are the consequences to work through. This one is owed detailed drawings and a detailed plan.

- `#fit` is 0.8 today, so 0.08 is a tenfold tightening.
- `#grip` 3.6 was derived against `#fit` 0.8. The cavity is `#ball / 2 + #fit` and the mouth is
  `2 × √(cavity² − grip²)`, so the mouth goes from Ø11.54 — 96% of the ball — to Ø9.80 at a fit of
  0.08, and Ø9.60 at 0. A mouth at 80% of the ball is a different snap fit entirely, so `#grip` is
  re-derived rather than carried across.
- The current design already localizes `#fit`, but into the wall: `COLLAR_R = BALL / 2 +
  COLLAR_WALL`, with the comment that `FIT` comes out of the wall *"and nothing else, so the
  outside stays put when FIT changes"*. That is what leaves 2.20 of real material against a nominal
  3.0, which B2 measured. U2 localizes it differently — socket height fixed, ball position free —
  so the wall rule is superseded, not added to.

**U3 — no sketch is left blue, and the guide teaches why.** A defect and a requirement together.

- The defect: the ball's slit profile sketch is blue — under-defined — and its center of rotation
  is not coincident with the origin. Both are wrong in the model, not only in the prose.
- The check: a fully defined sketch is part of the definition of done, verified rather than noticed
  by eye. **Blue is measurable** — run 8p1's harness counted it on the canvas, 3882 pixels before
  the constraint and 0 after — so the gate does not have to wait on whether `featureStatus` tells
  the truth about it.
- Blue and black are what a student sees on screen; under-defined and fully defined are what the
  words mean. The guide says both.
- U1 is the same family: an eye profile is also a profile located against a feature it has to
  clear. What the guide says about locating a profile against the origin serves both.

**The steps exist, and they were found rather than written fresh.** They are
[`../../../../instructions/robot-guide4/source/ball-and-socket.rst`](../../../../instructions/robot-guide4/source/ball-and-socket.rst)
lines 551 to 594, a section called *Where the last bit of blue is hiding*, with five step frames
and a toolbar close-up already on disk: `bs-42-the-pattern-s-centre-dragged-off-the-origin`,
`bs-43-the-origin-picked`, `bs-44-the-pattern-s-centre-picked-as-well`, `tb-coincident` and
`bs-45-the-slit-sketch-fully-defined`. The page names the freedom before it removes it — a circular
pattern turns its copies about a center point, and that point arrives sitting on the origin without
being held to it — then drags from the origin, clicks the origin, shift-clicks the center, and
takes **Coincident** (`i`).

**Two route facts come with the steps, and both cost a run to learn.** A selection box over the two
points picks up only one, and Coincident after it leaves the blue where it was; and the undo
between the drag and the constraint has to go, because Coincident snaps the pattern back on its own
and an undo puts both points on one pixel where neither can be picked. Both are in
[`../2026-08-19-run8p1/register.md`](../2026-08-19-run8p1/register.md), and the deviation is the
worked example in [`../../../build/takes.md`](../../../build/takes.md).

**The break was in the brief, not in the guide.** Run 8p1 overturned run 8's *"a sketch circular
pattern does not define its copies"* and wrote the fix into the guide page, but never into
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md), which taught the
two circular patterns at length and never mentioned the center. B1 built from the brief, so the
model took the loose center; D1 wrote the page from the build log, so the teaching went with it.
This guide's ball-and-socket page carries two admonitions about the seed and the missing green
tick, one picture, and the words *blue*, *center point* and *Coincident* nowhere. **The brief now
carries the step and an acceptance check for it**, so the next build cannot lose it the same way.

**U4 — every protrusion is on the blade, every recess on the fork.** The click-lock valleys move to
the fork and the click bumps move to the blade, so the bumps never run into the axle stub while the
joint is being mated. The rule is the requirement and the swap is its consequence: stated as a
rule, it survives a later change to which part carries the axle.

- Today the blade carries the axle stub and the fork's ears carry the bumps. `STUB` is *"the axle
  across the blade, into a bore through each ear"* and `TOOTH_PROUD` is *"how far a bump stands off
  the ear's inner face"*, so the blade already holds one protrusion and the fork one recess, and
  the detents are the pair facing the wrong way.
- The reconcile of the hinge's snap direction under *Resolved* was settled against the old
  arrangement, so its answer is re-derived rather than carried forward.
- The detents are visible in the hinge frames, so this is a re-CAD and a re-shoot, not a text edit.

**U5 — the foot's groove pattern is derived from the foot's length.** `#foot_l - #heel_y` is
arbitrary and wrong: it borrows a dimension from the heel that has nothing to do with the tread.
The math instead leaves a full run of solid material at both ends of the foot and cuts no groove at
either end. The repeat divides the foot length evenly, and the first groove is phased off zero —
`0`, or `0 + repeat − width`, or whatever comes out even. A first groove sitting past the end of
the foot makes no sense to a human reading the model.

- The repeat is already an even divisor. `#rib_w` is 6, the repeat is 12, and the count is typed as
  `#foot_l / (2 * #rib_w)`, which comes to 8. The offset alone is wrong: `#foot_l - #heel_y`
  evaluates to 64, and the sole runs from +32 at the heel to −64 at the toe, so the first groove
  lands on the toe tip.
- Whether the requirement is equal margins at both ends or only solid material at both ends changes
  the arithmetic, and the two candidate phases give different answers. The number comes with the
  drawing.
- This is the design-intent rule catching a live violation. `#foot_l - #heel_y` is a magic
  coordinate wearing variable names, and it fails the test a driving dimension exists to apply:
  move `#heel_y` and the tread shifts for no reason a student could explain.
- The blast radius is the foot sheet, the foot brief and the foot page's frames, because the tread
  is in every picture of the sole.


**U6 — `#limbSeg` is renamed `#limbCenter` and means joint center to joint center.** That settles
the open question, and it settles it the way the sheets already draw it. `clevis()` puts the pin
axis *at* the station and rounds the end `NOSE` beyond it; `blade()` does the same and roots the
blade `BLADE_OUT − NOSE` back into the limb. `make_plans.py` says so in its own words at line 90:
*"Both fit: each takes about 21 mm of a 48 mm segment, and the other end of that segment is a
`COLLAR_L` socket."* The name was the only thing that ever disagreed.

- **The joints are carved into the segment, not stacked on the end of it.** That is the build
  change U6 forces, and it is where the 106.4 mm went. At 48 center to center the upper limb
  spends 7.4 on the socket and about 21 on the fork, leaving roughly 19.6 of rod; the lower limb
  spends about 20 on the blade and 10 on the ball stud, leaving about 18. Both are comfortably
  positive.
- **The recorded minimum of 52.4 and 54 does not survive the rename.** It is arithmetic about the
  as-built method — joints standing 7.4, 45, 44 and 10 clear of the end face of a full-length rod
  — and under that method 48 really is impossible. Carved into the segment the same joints cost
  about 21 and 20, so **48 stands and no number on the sheets has to move.**
- **`ARM_SEG` is used two ways inside `make_plans.py` and only one of them survives.** Line 762
  spaces the stations by it, which is center to center and stays. Line 688 labels the drawn part
  `Ø24 × 48 mm`, which is a stock length and becomes wrong the moment the name says centers. That
  label has to be derived from `#limbCenter` less the two joint costs.
- The blast radius is `make_plans.py` and the sheets it prints, the two limb briefs
  [`10-u-limb.md`](../../../build/plan/10-u-limb.md) and
  [`11-l-limb.md`](../../../build/plan/11-l-limb.md), the Onshape variable table, both limb Part
  Studios, and every limb frame — the rod gets visibly shorter. The robot comes back to 315.4.

## What is still open

**Whether `#grip` 3.6 leaves enough travel, and whether 2.20 of real wall is enough behind it.**
B2 settled that the wall really is 2.20 of material and not the nominal 3.0, on every socketed
part. Whether 2.20 holds a snap fit at this size is a print question and this run did not print.
Doubling does not change the strain but it does change the force, which is what a student's fingers
feel.

**Whether the head's depth becomes a fifth variable.** It is typed twice today, and B3 showed it is
the one dimension of the head that does not move when the robot is driven.

**Whether tutorials 1 to 5 are re-run for step frames.** They now have their steps, their traps,
their numbers and a hero apiece, but no frame of any single step — a hero can be recovered from a
rolled-back tree and a step cannot. The guide's index says so on its front page rather than
letting a reader find out. Re-running the five is the only way to close it, and it is five pages
of clicking, not a repair.
