# draft9p1p1 — three shapes settled, in a copy of 9p1

draft9p1 made the model and the design source agree and proved the agreement by measurement. **Three
shapes are still wrong in a way that measuring could not catch, because the source and the model
agree about all three.** The socket's relief slit stops being a slot partway down and becomes a
blind pocket; `#collar` is measured from a mouth that moves, so a printing clearance moves the
robot's height; and the gripper's clip has a round top where it should have a flat square one. A
fourth item is source-only — the sheets place the feet 8 mm outboard of their legs and the model
never did.

This draft copies `stickbot-draft9p1`, settles the four on paper, edits the copy, and measures it.
**It captures nothing and writes no guide page.** Its product is what draft9p2 builds from.

## The declaration

| Field | Value |
| ----- | ----- |
| `draft` | `draft9p1p1` |
| `parent` | `draft9p1` |
| `from` | `version stickbot-draft9p1 Recovery point`, `8504f457723606c65c2ab48f` |
| `takes` | none |
| `gates` | Model inspected, Recovery point, Links resolve, Prose style, Spelling |
| `requirements` | all of `req.model`; `req.carry.register`; `req.page`, `req.shot`, `req.guide` and `req.log` deferred to draft9p2 and not in play here |

**The name carries a third level, and the user set it.**
[`drafts.md`](../../../build/drafts.md) § *What a draft declares before it starts* says the user
decides when a draft bumps `M` and that it otherwise bumps `N`; it describes no third position.
[`../2026-08-25-draft9p2/plan.md`](../2026-08-25-draft9p2/plan.md) is already written and is a much
larger draft — build from empty, capture every step, audit each one. This draft is a repair to 9p1's
geometry that 9p2 wants in front of it, so it takes 9p1's number rather than 9p2's.

**`takes` is empty for the reason 9p1's was.** Every step is going to be performed and photographed
in 9p2, from empty. Frames taken here would show a model no page will ever show.

**Gates not claimed.** *Steps reproduce* — this draft writes no steps. *Names are real* — no page
here names a tool. *Floor & ceiling* and *Reading level* — no session material.

## No guide directory, on purpose

`instructions/stickbot-draft9p1p1/` is not created, for the reason
[`../2026-08-25-draft9p1/plan.md`](../2026-08-25-draft9p1/plan.md) § *draft9p1 has no guide
directory* gives: a draft that retakes nothing and moves geometry would produce a complete guide
whose every picture shows a robot it has just stopped building. draft9p0's guide stays where it is,
and draft9p2 still declares `parent: draft9p0` for its pages while taking its model from here.

## What is wrong, and why 9p1 did not catch it

**Phase C compared the model against the design source, and on all three of these they matched.** A
comparison finds disagreements; it does not find a shape both documents describe the same wrong way.
The three came out of reading and of the user looking at the model, which is the check
[`../../../../constitution.md`](../../../../constitution.md) calls *Model inspected* doing the work
measurement cannot.

- **The slit stops being a slot partway down.**
  [`../2026-08-25-draft9p1/c/c1-readback.md`](../2026-08-25-draft9p1/c/c1-readback.md) measured the
  relief faces at r 5.0 and the slit floor at z −6.0535. Above z −3.4592 the cavity is wider than
  r 5.0 and the cut goes clean through the tab wall; below it the cut is a blind pocket in the ring
  that holds the tabs together, bounded by its own r-5.0 face. The 8.0 mm cut is **5.4057 of slot
  and 2.5943 of pocket**, and the pocket is what lets the tabs flex further than they should.
- **`#collar` is measured from a mouth that moves, so the fit moves the robot's height.**
  [`../2026-08-25-draft9p1/c/c2-driving.md`](../2026-08-25-draft9p1/c/c2-driving.md) drove `#fit`
  from 0.08 to 1 and measured the socket staying 11.000 tall while the tops of `Foot`, `Gripper` and
  `u limb` each rose 2.0312. A clearance that exists for the printer has no business changing how
  tall the robot stands. [`../../../README.md`](../../../README.md) § *TODO — measure `#collar` from
  the ball's center* holds the proposal and what it follows through to.
- **The gripper's collar is cantilevered over 4 mm of air.**
  [`../2026-08-25-draft9p1/a10-gripper.md`](../2026-08-25-draft9p1/a10-gripper.md) settled the top
  of the body as the collar's own circle and B8 built it. Measured, the body is 18.0 across X and
  **10.0 across Y**, under a collar of Ø18. `stickbot-for-bot-review` carries the flat square
  platform this wants, made by cutting — and [`a/a3-gripper.md`](a/a3-gripper.md) measures both and
  finds its square is a coincidence of a clip wider than its collar, which stopped being true when
  the robot doubled.
- **The feet's 8 mm offset is in the sheets and never was in the model.** `FOOT_X` is
  `LEG_X + FOOT_H / 3` = 32 and both feet measure ±24.
  [`../../../robot-build-plan.md`](../../../robot-build-plan.md) now says the feet are not handed
  and are allowed to touch, so the source gives the offset up.

## The order, and why it is this order

**A2 is settled before A1, because A2 moves what A1 measures from.** Re-basing `#collar` on the
ball's center fixes the socket's root and lets its mouth move; the slit is cut from the top face
down and its floor is a `#wall` ring above the root. Settle the slit against a root that is about to
stop moving, and it gets settled twice.

**Nothing in Phase B starts until Phase A is committed**, which is 9p1's rule and the reason its
Phase B was edits rather than a rebuild.

## Phase A — the design source

The design source is
[`../../../../instructions/robot-guide/make_plans.py`](../../../../instructions/robot-guide/make_plans.py)
and the sheets it prints, [`../../../build/plan/`](../../../build/plan/00-manifest.md), and
[`../../build-briefs/`](../../build-briefs/).

| | What changes | Where |
| --- | --- | --- |
| **A2** | `#collar` becomes `#ball / 2 + #wall` = **9.0000**, the distance from the ball's center to the bottom of the socket, and is `collar blank`'s second extrude distance on its own. **`#fit` and `#grip` then change no robot dimension.** Every expression carrying a `#grip` term because the root moved loses it. | `make_plans.py`, `build-briefs/ball-and-socket.md`, `build-briefs/foot.md`, `build-briefs/limbs.md`, `.docs/README.md`, `plan/04-ball-and-socket.md` |
| **A1** | The slit is a slot for its whole depth, because its floor comes up to `−#ball / 4` — **z −3.0000**, where the cavity is still wider than the cut's inner edge. The depth becomes `#grip + #ball / 4` = **4.9465**. `#slit_in` stays 5.0 and the seed stays one slot to one side of the axis, patterned circularly 4 over 360°. | `make_plans.py`, `build-briefs/ball-and-socket.md`, `plan/04-ball-and-socket.md` |
| **A3** | The slab in `clip profile` is dimensioned `#collarR` instead of `#clipR`, so the socket stands on a flat 18 × 18 square made flush by the reference's own *plane to cut top of clip* and *remove top of clip*; a 45° chamfer of leg `#collarR − #clipR` necks it to the clip before the mouth, and B8's three rounding features come out. Settled in [`a/a3-gripper.md`](a/a3-gripper.md). | `make_plans.py`, `build-briefs/gripper.md`, `plan/12-gripper.md` |
| **A4** | `FOOT_X` becomes `LEG_X`. The feet sit at x ±24 with their inner edges together at x 0. | `make_plans.py`, `build-briefs/assembly.md`, `plan/14-assembly-legs.md` |
| **A6** | `gripper()` and `foot()` draw the socket's collar standing proud, and their docstrings stop calling the origin the joint center when the figure puts the mouth there. `GRIPPER_L` and `FOOT_H` are measured from the ball's center, which is where the model measures them. | `make_plans.py` |
| **A5** | The plan sheets are regenerated and frozen as `r7`, and every explanatory sketch carrying a number that moved is republished. | `make_plans.py` outputs, `../../sketches/` |

### A2 — `#collar` from the ball's center

`collar blank` extrudes `#grip` one way and `#collar − #grip` the other, so both the mouth at
`#grip` and the root at `#grip − #collar` move when the fit moves. **`#collar` becomes the second
extrude distance itself** — ball center to the bottom of the socket — so the root sits at
z −`#collar` whatever `#fit` and `#grip` do.

**The test is the robot's height.** The socket is added to the head, the foot, the upper limb and
the gripper, and each of those parts is as tall as its socket's root is deep. Fix the root and a
printing clearance stops reaching the standing height, which is 317.0535 today and moved 1.65 the
last time `#fit` was touched.

**The trade is named rather than hidden.** Today the tabs keep a constant free length and the parts
move; under this the parts keep their dimensions and the tabs' free length varies with the fit. A1
picks the tabs' length directly, so what varies is how much material sits under them rather than how
far they flex.

**`#collar` becomes `#ball / 2 + #wall`, which is the collar's own radius**, so the socket goes as
deep below the ball's center as the collar is wide from the axis. It stops being a typed number
altogether. The user settled it on 2026-08-27 against the two alternatives: 9.0535 holds today's
geometry exactly but is a number a student has to type into a table, and a re-pointed 11.0 keeps a
familiar figure while making every socketed part 1.9465 taller.

| | |
| --- | --- |
| the root, z | **−9.0000**, from −9.0535 |
| the socket, mouth to root | **10.9465**, from 11.0000 |
| the head, its underside and its top | **+67.0000 / +139.0000**, 0.0535 lower |
| `u limb`, its rod | **27.0000**, from 26.9465; 0.0535 longer, and the part itself unchanged |
| the foot, its mouth to its sole | **25.9465**, unchanged; `#pedestal` 2.9465 to 3.0000 |
| the gripper, its mouth to the clip | **25.9465**, unchanged; the run 4.6465 to 4.7000 |
| the standing height | **317.0000**, from 317.0535 |

**Only the head changes size at all.** Which way a part moves depends on which side of the root its
own material sits on, and on whether anything below the root absorbs the move. The head hangs above
a root that rose and has nothing under it, so it drops. Everywhere else something takes up the
0.0535: `u limb`'s rod grows by it from a start that rose by it, so the rod's far end does not move
and the part measures what it always measured; the foot and the gripper each carry a feature between
the root and the end of the part, the pedestal and the platform's run, and that feature absorbs it.

**What follows through:** `u limb`'s rod is `#limbCenter − #collar + #grip − #limbD / 2` and loses
its `#grip` term, and so does the foot's `#collar_down`. The foot's `#pedestal` is
`#plate − #collar_down` and follows without being edited.
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) already claims the
slit floor does not move — *"the floor sits at z −6.0535 and is 3.0 thick, whatever the fit is"* —
and that sentence is true of the proposal and false of the model.

### A1 — the slit is a slot, and its depth is the flex

**The slit exists to let the four tabs flex, and how far they flex is how deep it is cut.** That is
only true while the cut is a slot. Where it turns into a blind pocket in the ring under the tabs, it
is taking material out of the thing that springs them closed, and the tabs flex further than the
depth says they should.

**Today the cut is both.** The cavity is a sphere of radius `#ball / 2 + #fit` = 6.08 on the ball
center, so it is wider than the slit's r-5.0 inner face down to z −3.4592 and narrower below that.
The mouth is at z +1.9465 and the floor at z −6.0535, so the 8.0 mm cut is a through slot for
**5.4057** and a blind pocket for **2.5943**. At the floor the cavity has closed to r 0.567, which
is the far end of a pocket rather than the far side of a slot.

**The floor comes up to `#ball / 4` below the ball's center**, which the user settled on 2026-08-27.
That is z **−3.0000**, and the depth becomes `#grip + #ball / 4` = **4.9465** measured down from
the mouth. The cut is then a slot for all of it: the deepest point of the cut is still 3.0 above the
bottom of the cavity, so there is cavity on the inboard side of every part of it.

**One number does the whole job, and `#slit_in` stays at 5.0.** The profile was going to have to
reach the axis only because the cut ran past the point where the cavity narrowed to r 5. Stopping
the cut higher moves that point out of the way instead, and the profile can stay where it is. At the
floor the cavity's radius is `√((#ball / 2 + #fit)² − (#ball / 4)²)`, which is smallest when `#fit`
is zero — `#ball √3 / 4` = **5.1962**, still 0.1962 outside the profile's inner edge. At today's
0.08 it is 5.2883 and at the 1 mm C2 drove it to, 6.3246. The margin grows with the fit, so the fit
can move and the slit stays a slot.

**The pattern therefore stays circular, which is the second thing the user settled.** A slot to one
side of the axis is one slit patterned **4 over 360°**, and that is what
[`../../build-briefs/ball-and-socket.md`](../../build-briefs/ball-and-socket.md) describes and what
the sketch already holds — `slit profile` has four rectangles and exactly one `CIRCULAR_PATTERN`
constraint. The crossing slot the brief costed as the alternative would have been two slits over
90°, a mirror standing in for a rotation, and there would be nothing circular left to teach.

| | now | after A1 and A2 |
| --- | --- | --- |
| the floor, z | −6.0535 | **−3.0000** |
| the cut, deep | 8.0000 | **4.9465** |
| of that, slot | 5.4057 | **4.9465** |
| of that, pocket | 2.5943 | **0** |
| the ring under the tabs | 2.9465 | **6.0000** |

**The tabs lose 3.0535 of free length, and that is the point.** The depth was letting them flex
further than the design says, by taking material out of the ring that springs them closed. Whether
4.9465 is the flex the joint wants is a question for Phase C at the model; it is now a number that
means the tabs' free length and nothing else.

**This arithmetic is off the variable table and C1's measurements, not a measurement of its own**,
and A2 moves the root under it. A1 is worked after A2 settles and checked at the model in Phase C.

### A3 — the socket stands on a square, made flush by a cut

**Read and settled before this plan was finished.** The measurements, the reference's whole feature
tree and eight rendered views are in [`a/a3-gripper.md`](a/a3-gripper.md).

**The reference's construction copies and its shape does not.** `stickbot-for-bot-review` cuts the
clip's own crown flat with an offset-zero plane on the socket's root, and the chord comes out 9.4080
across a body 9.4000 wide under a collar of Ø9.4 — square, and the collar's diameter, with nothing
typed to make it either. It works because the clip's Ø11 is 1.6 wider than the collar. `#barD` does
not scale, so the clip did not; the collar doubled to Ø18, and a chord across a Ø10 crown reaches
10.0 at the very most.

**So the square becomes the body's own plan shape, and the cut only makes it flush.** `clip profile`
already draws a slab dimensioned `#clipR` each side of the clip's axis, which is the whole reason
the body is 10 wide fore-and-aft while the extrude gives 18 across. **That dimension becomes
`#collarR`**, the top of the body becomes 18 × 18, and the Ø18 collar is inscribed in it tangent on
all four sides — the reference's relationship, reached by dimension instead of by chord.
`plane to cut top of clip` stays an offset-zero plane on the root and `remove top of clip` stays a
split, so the click path a student follows is the reference's click path; what changes is which
solid is under the knife.

**The neck is a 45° chamfer onto a corner the sketch already has.** Two lines run from the slab's
sides down to the corners at `#clipR` across and `#mouth / 2` above the clip's axis, where the
mouth's upper lip already ends. Their leg is `#collarR − #clipR`, an expression the file already
uses. [`../../build-briefs/gripper.md`](../../build-briefs/gripper.md) rules out a body 18 deep
fore-and-aft because it *"would close the mouth off"*, and that is about the body beside the mouth
rather than above it: below the upper lip this body is the clip circle and nothing else, exactly as
it is now, so the throat between the lips stays `#mouth`.

**What is left at full width is the number Phase C watches.** The run is
`#gripperL − #collarR − #mouth / 2 − #collar`, which is 4.6465 today and **4.7000** once A2 sets
`#collar` to 9.

**Three features come out.** `body top outline`, `round the body top` and `trim the body top` are
what B8 added to round the body's top to Ø18 for its first 4 mm, and the slab's corners come back
below them. Deleting them takes the gripper from ten features to seven.

**This row absorbs the open item 9p1 left**, that `clip()` and `clip_front()` in `make_plans.py`
still draw the 18 × 24 slab while `clip_front()`'s docstring already claims the flushness B8 built.
The sheets are redrawn once, against the shape settled here, rather than twice.

### A4 — the feet stop being offset

`FOOT_X = LEG_X + FOOT_H / 3` is the only place the 8 mm lives; the model has never had it. Three
live sentences carry the consequence and change with it —
[`../../build-briefs/assembly.md`](../../build-briefs/assembly.md)'s rest-pose row and its *"the
feet are symmetric at rest, at x ±32"*, and
[`../../../build/plan/14-assembly-legs.md`](../../../build/plan/14-assembly-legs.md)'s *"At rest the
feet are at x ±32 and their inner edges at ±8"*.

**No model edit follows.** The feet already measure ±24 with their soles touching, so A4 is a
design-source row with no Phase B counterpart, and Phase C confirms rather than checks it.

### A6 — the sheets draw the collar, and two docstrings stop lying

**The model puts each part's joint on its origin and the sheets say they do too, and for two parts
the sheets do not.** Measured in each part studio's own coordinates, `gripper` and `foot` each hold
their cavity sphere at exactly **(0, 0, 0)**; `l limb` puts the elbow's blade there and hangs its
ball at z −48; `head` is the one part modeled about its own center, which
[`../../build-briefs/head.md`](../../build-briefs/head.md) says it is. So the guideline is kept
everywhere in the model, and the gripper has only one joint to keep it with — the clip grips a
foreign bar and does not articulate.

**`socket()` draws from the face, and two callers treat it as if it drew from the center.** The
helper opens a cavity *through a face at (x, y)*, putting the mouth on the point it is handed and
the ball's center `GRIP` inside. `gripper()` calls `socket(0, 0, "up")` and then says its origin is
the wrist joint center — two points 1.9465 apart. `foot()` does the same thing with the same claim.

| | model, measured | the figure today |
| --- | --- | --- |
| the ball's center | z 0 | y +1.9465 |
| the socket's mouth | z +1.9465 | y 0 |
| the body's top face | z −9.0535, the collar's root | y 0 |
| the bottom of the clip | z −24.0 | y +24 |
| mouth to clip bottom | **25.9465** | **24** |

**One point in the figure is doing three jobs**, and in the model those three are spread over 11 mm.
What a reader sees is a gripper with no collar under it and a part that measures 1.9465 short. The
foot is the same: its sole measures z −24.0 from the ball's center, so `FOOT_H` is right and the
figure hangs it off the mouth.

**`limb()` is the counter-example, and it is right.** It uses the same helper, takes the rod's top
*face* as its origin, and adds `top_at = GRIP` back into the rod's length, so joint center to joint
center still comes out at `#limbCenter`. It never claims the origin is a joint. The fix for the
other two is to say what they draw and to draw the collar, not to change the helper.

**Nothing downstream is wrong.** `HEAD_RIM = NECK_Z − GRIP` and `SOLE_Z = ANKLE_Z − FOOT_H` both
measure from ball centers, and the parts sheet places each figure at a page position rather than a
station, so the offset never reaches the elevation. This is a figure fix with no arithmetic behind
it.

**It rides with A2 because A2 sets how far proud the collar stands.** `#collar` becomes 9, so the
collar a reader has never seen drawn is drawn once, at its settled height, rather than twice.

## Phase B — the model

**B0 — copy, and record what the copy is.** `stickbot-draft9p1` is copied at `Recovery point`
`8504f457723606c65c2ab48f` into a new document, `stickbot-draft9p1p1`. Every tab's element id is
written down before any edit, the way
[`../2026-08-25-draft9p1/register.md`](../2026-08-25-draft9p1/register.md) § *Where the work is*
records them. `stickbot`, `stickbot-for-bot-review`, `stickbot-draft9p0` and `stickbot-draft9p1`
stay read-only for the whole draft.

**The edit order follows the derive graph**, because a derived body updates under its consumer.
`ball and socket` is derived into `head`, `foot`, `u limb`, `l limb` and `gripper`.

- **B1 — `robot sizes`.** `#collar`'s new meaning and its new number, plus whatever A1 leaves in the
  table. Every rename is checked against the dimensions that read it.
- **B2 — `ball and socket`.** `collar blank`'s second position, the slit profile and its pattern
  count. The sketch ends fully defined.
- **B3 — the socket's consumers.** `head`, `foot`, `u limb` and `l limb`: the expressions that
  carried a `#grip` term because the root moved. Each part's overall height is measured before and
  after, because A2's whole claim is that these stop moving.
- **B4 — `gripper`.** The clip's top cut flat and square, and the consumer edits B3 makes
  everywhere else.
- **B5 — `stickbot`.** The instances move onto this document's own workspace, and the rest pose and
  the stations are read. It runs before B1, because a workspace instance follows a Part Studio edit
  as soon as the edit is made and the four edits above are otherwise made blind. 9p1's B9 pinned
  these instances to a version, which is why the copy's assembly arrived showing 9p1's parts;
  [`b/b5-assembly.md`](b/b5-assembly.md) records the move and [`b/b0-copy.md`](b/b0-copy.md)
  records why a copy could not make it.

**Every sketch this phase touches ends fully defined,** and **features are named in their dialog
titles as they are made**. Both are 9p1's rules and both are what 9p2 photographs.

## Phase C — read it back and prove it

C repeats 9p1's Phase C against a source that has changed again, and adds the three checks this
draft exists for.

- **`#fit` is driven and the robot's height does not move.** 9p1's
  [`c2-driving.md`](../2026-08-25-draft9p1/c/c2-driving.md) is the before picture: at `#fit` 1 the
  tops of `Foot`, `Gripper` and `u limb` each rose 2.0312. The same drive is repeated, and A2's
  claim is that the standing height, every joint station and every part's overall size hold while
  only the mouth moves. **This is the measurement that decides whether A2 worked.**
- **The slit is a slot for its whole depth.** Read the slit's faces out of `bodydetails` and show
  that no face at r 5.0 bounds the cut — that is the face C1 found — and that the cavity is still
  wider than the cut's inner edge at the floor, which is what makes the bottom a slot bottom.
- **The gripper's clip top is one flat square face** measuring 18 both ways against the Ø18 collar
  standing on it, with the run at full width positive and the mouth shown still open — the two lips
  2.6 apart, which is where C1 found them.
- **The feet measure ±24 with their inner edges at 0**, against sheets that now draw the same.
- **The variable table is driven and put back**, so a `#collar` or `#fit` change is shown to move
  the robot rather than break it.
- **The model is opened and turned.** *Model inspected* is a gate this draft claims, and reading a
  report about a model is not looking at it.
- **A named version is published**, which is *Recovery point* and is what 9p2 starts from.

## Phase D — register, and what 9p1p1 hands on

`register.md` records what Phase A decided and on what evidence, what Phase B edited, what Phase C
measured, and every item 9p1's register left open — closed or carried, by name, so the two read as a
pair. What 9p2 inherits is a version, a design source and a log; not a guide and not a frame.
9p2's plan is amended in this draft's Phase D where it names 9p1's version as the model it takes.

## What we do not know yet

- **Whether re-basing `#collar` breaks the consumers' sketches or only their dimensions.** A
  dimension that reads a variable follows it; a sketch built on a face whose z moves may not.
- **Whether 4.9465 is the flex the joint wants.** The depth is now the tabs' free length and nothing
  else, which is what makes it a number worth choosing — and nobody has flexed one. Phase C measures
  what A1 builds; a printed joint is task #29's.

## Settled on 2026-08-27

Three of this list's items were choices rather than investigations, and the user made them.

| | settled |
| --- | --- |
| what `#collar` becomes | `#ball / 2 + #wall` = **9.0000** — A2 |
| how deep the slit goes | floor at `#ball / 4` below the ball's center, z **−3.0000** — A1 |
| which pattern to teach | **circular**, which is the 4-over-360 form already built — A1 |
| the head's depth | **driven**, which `#headD = #torsoD * 5 / 4` already does — no row |

**The head's depth needs no work here.** It is 9p1's register open item, and both the model's
`#headD` and `make_plans.py`'s `HEAD_D` are already `#torsoD * 5 / 4`. The requirement makes that a
rule rather than a coincidence, so it is written into
[`../../build-briefs/head.md`](../../build-briefs/head.md) and the register item is closed.
