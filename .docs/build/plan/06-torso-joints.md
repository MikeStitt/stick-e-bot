# 6. The torso gains shoulders and studs

Starts from a torso box. Ends with a torso carrying two shoulders, five ball studs, and a named
mate connector at the center of each stud.

**The longest Part Studio tutorial in the robot, and the one that changes most from stickbot.**

## The steps

### The numbers this tutorial adds

**One row for the studio and eight for the tab, and none of them opens the tutorial.** Each goes in
at the step that first reads it, which is the step directly under it in the table below.
`#ball` and `#stand` are already in `robot sizes`, where tutorial 4 put them, and nothing here
types them again.

| variable | expression | at the robot's size | where | typed at |
| -------- | ---------- | ------------------- | ----- | -------- |
| `#shoulder_half` | `#torsoW / 2` | 36 | `body` | `shoulders.pivot_variables` |
| `#shoulder_drop` | `#torsoH / 12` | 8 | `body` | `shoulders.pivot_variables` |
| `#yaw` | `30 deg` | | `body` | `shoulders.yaw_variable` |
| `#tilt` | `53 deg` | | `body` | `shoulders.profile_variables` |
| `#shoulder_len` | `#torsoH * 13 / 48` | 26 | `body` | `shoulders.profile_variables` |
| `#boss_len` | `#shoulder_len - #stand` | 16 | `body` | `shoulders.profile_variables` |
| `#boss_d` | `#ball * 4 / 3` | 16 | `body` | `shoulders.profile_variables` |
| `#limbD` | `#torsoH / 4` | 24 | `robot sizes` | `studs.hip_variables` |
| `#hip_half` | `#torsoW / 2 - #limbD / 2` | 24 | `body` | `studs.hip_variables` |

**Not one of the eight is typed except the two angles.** `#tilt` and `#yaw` are the shoulder's
own decision and there is nothing to derive them from; everything else is a fraction of the torso.

**`#limbD` is a studio row and it waits until the hips.** It is read here and by the limbs, the
foot and the gripper, and a tab that declares a name the studio also carries shadows the row —
[`onshape`](../../../.claude/skills/onshape/SKILL.md) § *Modeling standards*. `hip stud
location` is the first feature in the robot that has to know how thick a limb is, and `#hip_half`
is written from it, so the two go in together there.

**The shoulders need four of theirs at one step and that is the sketch's doing.**
`torso shoulder profile` dimensions the boss as well as the shoulder, so `#tilt`,
`#shoulder_len`, `#boss_len` and `#boss_d` are all read by the one sketch. Splitting them would put
a rule in front of the geometry that explains it.

**draft9p0 typed `#stand`, `#shoulder_len`, `#shoulder_drop` and `#boss_d`,** and every one of them
is right at the robot's size only because somebody retyped it when the robot doubled. `#boss_d` is
the one that bites: the pad is 16 while the ball it carries is `#torsoH / 8`, so the shoulder around
the ball goes 2.0 at `#torsoH` 96, 0.5 at 120, and nothing at all at 128. Written as `#ball * 4 / 3`
it holds a sixth of the ball's diameter at any size.

**The two angles stay typed, and that is not the same defect.** An angle is what stays the same when
a length changes, and `#tilt` and `#yaw` are the two numbers this tutorial puts on screen for a
student to change.

**The torso's width places both, and its height places neither.** `#hip_half` is a half-width less
a half-limb because that is what puts a leg's outer surface flush with the torso's side.
`#shoulder_half` is the side face itself; the stud then runs out from that face at its own angle
and carries the ball 13.55 mm clear of it.

**draft9p0 built `#hip_half = #torsoH / 4`, and it measures correct.** The torso is 0.75 as wide as
it is tall and the limb is a quarter of the height, so the right expression and that one are the
same function of `#torsoH` — driving the height never separates them. Driving `#torsoW` to 90 does:
the shoulders go to ±45, the hips stay at ±24, and the body hangs 21 mm over each one.
[`../../experiments/runs/2026-08-25-draft9p1/a7-hip-shoulder.md`](../../experiments/runs/2026-08-25-draft9p1/a7-hip-shoulder.md)
has the arithmetic and the four other names declared in more than one tab.

### The shoulders, from construction geometry a student can see

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.body.shoulders.pivot_variables` | `#shoulder_half` and `#shoulder_drop`, which place the lines | two variables |
| `cad.parts.body.shoulders.pivot_sketch` | the lines the shoulder pivots about | `pivot lines` |
| `cad.parts.body.shoulders.yaw_variable` | `#yaw`, the angle the next dialog asks for | `#yaw` |
| `cad.parts.body.shoulders.plane` | the plane the profile is drawn on, at `#yaw` | `plane for shoulder` |
| `cad.parts.body.shoulders.profile_variables` | `#tilt`, `#shoulder_len`, `#boss_len`, `#boss_d` | four variables |
| `cad.parts.body.shoulders.profile_sketch` | the shoulder's profile | `torso shoulder profile` |
| `cad.parts.body.shoulders.revolve` | revolve it | `shoulder` |
| `cad.parts.body.shoulders.connector` | a connector on the shoulder | `mate for shoulder stud` |
| `cad.parts.body.shoulders.mirror` | the second shoulder | `mirror shoulder` |
| `cad.parts.body.shoulders.trim_sketch` | what to cut back | `trim shoulder pattern` |
| `cad.parts.body.shoulders.trim` | cut it | `trim shoulder cut` |

**The chain is the lesson, not an accident of how it got built.** Four features to place one
shoulder looks long next to a transform carrying two typed offsets. The long way puts the
shoulder's angle on screen where a student can see it and change it; the short way hides the same
decision inside numbers nobody can read back.

**Stickbot has no rotation point, rotation plane or rotate-about-z, and this table used to ask for
all three.** Reading the built model feature by feature settled it: `#yaw` is the angle field of
`plane for shoulder`, which stands on the pivot line, and `#tilt` is a dimension in
`torso shoulder profile`. Both numbers are still on screen where the argument above wants them, in
three features fewer. [`../lesson-plan.md`](../lesson-plan.md) § *Geometry a student can see, not
numbers they cannot* says the same thing.

**`torso shoulder profile` stands its rectangle on a projected edge, and this draft builds it that
way.** `stickbot-draft9p1p1`'s sketch holds five lines and draft9p3's holds four. The missing one is
construction, projected from an edge the sketch already has in front of it, and the reference stands
the shoulder rectangle on it with a midpoint and an angle of `90° - #tilt`. draft9p3 reached the
same rectangle by other means, so the two bodies are the same shape face for face and only the
reason for the shape differs. The projected edge is what
[`onshape`](../../../.claude/skills/onshape/SKILL.md) § *Anchor each sketch to the geometry
that gives it meaning* asks for: a rectangle standing on an edge follows the torso when the torso
moves, and one placed by arithmetic has to be recomputed. That is task #125, and it is why this
tutorial retakes `torso shoulder profile` alongside the studs rather than carrying it.

**Stickbot calls it `shoulder. rotation plane`.** The stray period is a typo, not a name.

### The studs

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.body.studs.hip_variables` | `#limbD` in `robot sizes`, then `#hip_half` in the tab | two variables |
| `cad.parts.body.studs.hip_sketch` | where the hips go | `hip stud location` |
| `cad.parts.body.studs.hip_connector` | a connector there | `mate for hip stud` |
| `cad.parts.body.studs.neck_sketch` | where the neck goes | `neck stud location` |
| `cad.parts.body.studs.neck_connector` | a connector there | `mate for neck stud` |
| `cad.parts.body.studs.derive` | bring the ball stud in | `copy ball stud` |
| `cad.parts.body.studs.neck` | move one onto `mate for neck stud` | `move neck stud` |
| `cad.parts.body.studs.hip` | copy one onto `mate for hip stud` | `copy for hip` |
| `cad.parts.body.studs.shoulder` | copy one onto `mate for shoulder stud` | `copy for shoulder` |
| `cad.parts.body.studs.mirror` | the hip and the shoulder on the other side | `duplicate shoulder and hip` |
| `cad.parts.body.studs.combine` | union all five into the torso | `add neck to body` |

### The five connectors

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.body.connectors.neck` | at the neck ball's center | `neck` |
| `cad.parts.body.connectors.l_shoulder` | at the left shoulder ball's center | `left shoulder` |
| `cad.parts.body.connectors.r_shoulder` | at the right shoulder ball's center | `right shoulder` |
| `cad.parts.body.connectors.l_hip` | at the left hip ball's center | `left hip` |
| `cad.parts.body.connectors.r_hip` | at the right hip ball's center | `right hip` |

**These five are broken in stickbot** — all five report *Cannot resolve entities. 2 missing
selections*, all five are hidden, and all five sit after the Boolean that took their references
away. Rebuilding them onto the ball centers fixes them and takes work out of the assembly, which
then mates to a connector that already exists and is already named.

**One of the two features named `r shoulder connector` is the right hip.** It is renamed here.

## What changes from stickbot, and what it costs

**The shoulders come before the studs.** Stickbot builds the hip and neck studs first. The lesson
plan puts the shoulders first so that the construction chain is not interrupted, and so the studs
are one continuous run of the same move repeated.

**That splits stickbot's mirror.** `duplicate shoulder and hip` mirrors both at once, which is
only possible because both already exist. With the shoulders built first, the shoulder is
mirrored in its own section and the studs are mirrored in theirs. Whether the trim cut still
reaches both shoulders after that is the first thing to check when the reorder is performed.

## The shots this tutorial needs by name

**Requirements in play.** `req.model.derive` — the joint is brought in from the studio that
owns it, never resketched here.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the whole construction chain visible at once | the point of building it this way, and no per-click frame shows it | |
| the rotation plane, with the angle dimension on screen | the number a student would change | |
| the derived stud where it arrives, before it is moved | same argument as the head's socket | |
| each transform's two connectors, medium and close-up with a ring | five of these, and picking the wrong one is silent | `req.shot.two_frame` |
| the five ball centers, medium and close-up with a ring | the connectors go on points that are invisible from outside the ball | `req.shot.two_frame` |
| the five connectors in the tree, named, no error | the repair, shown as a repair | |
| the tree, the version dialog | | |

**The five ball centers are the hardest picks in the robot.** The point is inside a sphere, it is
one of several points near it, and there are five of them that differ only by where they are on
the torso. The medium view has to place the student on the robot and the close-up has to say which
dot — this is the case the two-frame rule was written for.

### What the tables above do not say, and draft9p2 got wrong

The record of how `stickbot-draft9p1p1` builds this tab is
[`../../experiments/runs/2026-08-29-draft9p3/reference/body.json`](../../experiments/runs/2026-08-29-draft9p3/reference/body.json)
for what each feature stands on and
[`body.sketches.json`](../../experiments/runs/2026-08-29-draft9p3/reference/body.sketches.json)
for where every line in every sketch landed, and the two together are what the take follows. Four
of its thirty-three features are places a builder reading only the tables above lands somewhere
else, because a name and a move do not say what a feature stands on:

- **`mirror shoulder` merges into `torso block`.** It mirrors the loose `shoulder` solid
  across `Right`, adds it, and names the torso as what to merge into, so both bosses belong
  to the torso before the trim reaches them. `trim shoulder cut` stands on `torso block`
  alone, so a boss left standing beside it would keep the 4.8 mm it reaches above the top
  face.
- **`trim shoulder cut` cuts `torso block`.**
- **`add neck to body` unions the five studs into `torso block`,** and the shoulders are already
  part of it by then, so they are not in the tool list.
- **`pivot lines` is drawn on `Front` and dimensioned from `Origin`,** and not from the `Right`
  plane.

Each of those reaches the same shape either way, which is why draft9p2 built all four differently
and every measurement it took agreed.

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 6 - the torso gains shoulders and studs** (`406a5f7c2fad62d0fe900b26`). Everything
draft9p3 had left in the `body` tab after `torso block` was taken back, and the tab was built again
by following the written page, step for step.

**The tab ends with thirty-nine features and one part.** `torso` has **20 faces**; eight planes,
seven cylinders and **five spheres of radius 6 mm**, and it measures x ±55.5509 mm, y ±24 mm,
z ±64 mm. The five spheres sit on (0, 0, 58) mm, (±24, 0, −58) mm and
(±49.5509, −7.8236, 19.2355) mm, which is the neck, the two hips and the two shoulders.

**Nine mate connectors answer, and five of them are the ones the robot is mated by.**
`mate for shoulder stud` sits at (44.339, −4.8145, 27.2218) mm, the end of the boss;
`mate for hip stud` and `mate for neck stud` sit on the torso's underside and top at
(24, 0, −48) mm and (0, 0, 48) mm; `stud connect to robot` comes across with the derive. Then
`neck`, `left shoulder`, `right shoulder`, `left hip` and `right hip` sit on the five ball centers
above.

**`robot sizes` gains one row, `limbD = #torsoH / 4`**, typed by the step that first reads it.
`#hip_half` is a `body` variable and reads `#torsoW / 2 - #limbD / 2`.

**`torso outline` was showing in the build document, and it cost two picks.** Its right edge runs
up the torso's side under the pivot line, so the two are the same pixels. The Plane dialog took
`Edge of torso outline` where the check document's frame reads `Edge of pivot lines`, and `Use`
projected the whole 96 mm side rather than the 8 mm line. The plane comes out in the same place
either way, because a line-angle plane holds the whole line, but the profile does not: the reader
is meant to hang the rectangle off the projected line's lower end. The sketch was hidden, the
plane's entity swapped in place, and `torso shoulder profile` and `shoulder` drawn again. The
reader's own document hides that sketch when tutorial 1 extrudes it, which is why the check
document never met this.

**`stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)) carries its own version
**tutorial 6 - the torso gains shoulders and studs** (`3535351b4fa643231b6a3eb8`), taken where the
page's frames were shot. Read back side by side, the two documents agree on the feature list, the
part count, the face count, the bounding box, the five ball centers and all nine connector origins.

**Two things are true of that check version and not of the check workspace.** It was published
before the four stud rows were dragged into their alternating order, so it lists
`hip stud location, neck stud location, mate for hip stud, mate for neck stud` where the workspace
and the build document both read `hip stud location, mate for hip stud, neck stud location,
mate for neck stud`. It was also published before `pivot lines` was repaired, so its two placing
dimensions hold `#torsoW / 2` and `#torsoH / 12` rather than `#shoulder_half` and
`#shoulder_drop`. Onshape offers no way to delete a version.

## Captured

**`instructions/stickbot-draft9p4/source/torso-joints.rst`**, written from the 169 frames in
`instructions/stickbot-draft9p4/source/images/torso-joints/`, captured across 31 steps in
`stickbot-draft9p4-check`. `ninja check` comes back clean with no paragraph above grade 8, Sphinx
builds the page with no warning, and `src/stickbot/page_sweeps.py`'s four sweeps come back clean:
every frame on disk is used, every frame the page names is on disk, no picture stands above its
sentence, and all 31 view keys the take pressed are named in the blocks that show them.

**The eight frames of `parts.body.numbers` and `parts.body.variables` are deleted.** Those two
steps typed nine numbers before the page drew anything, and this draft types each at the step that
first reads it, so neither step exists any more. Four short sections take their place:
`shoulders.pivot_variables`, `shoulders.yaw_variable`, `shoulders.profile_variables` and
`studs.hip_variables`, the last of which opens `robot sizes` for `#limbD` and then comes back to
the tab for `#hip_half`.

**`pivot lines` did not read the two variables the step above it makes.** The take typed
`#torsoW / 2` and `#torsoH / 12` into the two dimensions `#shoulder_half` and `#shoulder_drop` are
for, which reaches the same geometry and leaves both variables dead. The sketch was edited in place
rather than redrawn, because `plane for shoulder` and `torso shoulder profile` both stand on the
line's own id. Read back afterwards, the torso is the same 1 solid and 20 faces in the same
bounding box, with the same five ball centers and the same nine connector origins.

**One promoted frame did not go on the page and is set aside in the attempt directory.**
`parts.body.shoulders.pivot_sketch-07` was taken before the canvas repainted, so its label still
read the 30.03066 the box opened on rather than the 36 typed into it. The step runs 01 to 08.

**The repair's own frames are not the ones on the page.** They were shot in a tab that already
holds every later feature, so their feature list reads 37 rows where a reader at that step has
nine. No frame in either set shows a dimension's stored expression, so attempt 4's are true of the
repaired sketch as well.

**Five page-level corrections came out of the take rather than out of the plan.**

- **`torso shoulder profile` projects the pivot line in with `Use`** and stands its rectangle on
  the copy, which is what task #125 asked for. The rectangle is then held by one `Midpoint`
  constraint and three dimensions: `2 * #boss_len`, `90 deg - #tilt` and `#boss_d / 2`.
- **`mirror shoulder` arrives on `Add` with the torso already in its merge scope**, so the page
  has nothing to tell the reader to set. Both bosses join the torso the moment `Right` is picked.
- **`trim shoulder pattern` is a center point rectangle held by `Vertical` on the origin**, and its
  three dimensions are `#torsoH / 2` down to the torso's top, `#boss_d` tall and
  `#torsoW + 4 * #boss_d` wide.
- **The three transforms all pick `Ball stud` out of the parts list**, not the stud already placed.
  The neck's and the shoulder's need `Flip primary axis`; the hip's does not, because a leg's ball
  already points down.
- **Every `Mate connector` dialog that lands on a sketch point is named before anything is picked.**
  The dialog keeps the name while the pick is made, and the point is easier to hit with the name
  box already filled.

## What we do not know yet

**Whether the trim survives the reorder** is settled: it does. Built in draft9p3 with the
shoulders before the studs, `trim shoulder cut` reaches both bosses and leaves the torso 48 mm
tall at the top, with the cut's own parameters the same as 9p1p1's.

**Whether `pivot lines` should be anchored to the torso at all** is settled: it stays on `Front`.
A sketch stands on a face of the robot, and a stock plane is used where the sketch needs the torso's
center, which is where the planes are and where no face is. The shoulder pivots about a line on the
torso's centerline in y, so `Front` is that case. In 9p1p1 the sketch stands on `Origin`, `Top`,
`Front`, `#shoulder_half` and `#shoulder_drop`, and not on `torso block`; draft9p3 followed it and
this draft follows it too. Settled 2026-09-09. The run's
[`notes.md`](../../experiments/runs/2026-08-29-draft9p3/notes.md) § *`pivot lines` is drawn on
`Front` and dimensioned from `Origin`* carries the argument, and what the page owes the reader in
exchange.

**Whether five near-identical connector steps want five sets of frames or one worked example and
four short ones** is settled: five full sets. The take shot five frames for each of the five, and
the page carries all twenty-five. The four after the neck's are three sentences each, so the page
grows by pictures rather than by prose, and no student has to guess which ball a step means.
