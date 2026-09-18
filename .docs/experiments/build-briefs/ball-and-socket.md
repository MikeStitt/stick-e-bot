# Build brief — the ball and socket

**Before you write the report: publish a named version, and open the report with a "Where the
work is" section** — document name, document id, element id, version name and id, the version
link, and the workspace link labeled as live. See
[`../../../.claude/skills/onshape/SKILL.md`](../../../.claude/skills/onshape/SKILL.md). The model outlives this text only if
someone can find it.

**This is a specification, not a lesson.** Your job is to build it in Onshape, find the click
path that works, and write down what actually happened. The lesson gets written from your notes
afterwards.

**Runs 1 and 2 built this joint. This text has not been built from since run 2 corrected it**,
so the brief is what is under test, not the design.

**The numbers moved twice, and the second set is built.** They doubled for draft9p0 when the
robot doubled. draft9p1p4 then changed the socket again so that it holds a ball: the wall went
3.0 to 1.8 mm, the mouth 11.52 to 11.32 mm, the grip 1.9465 to 2.2205 mm, and the slits 4.9465 to
6.2205 mm deep. The doubling is worked out in
[`../runs/2026-08-23-draft9p0/plan.md`](../runs/2026-08-23-draft9p0/plan.md), the spring in
`src/stickbot/socket_spring.py`, and
[`../runs/2026-09-02-draft9p1p4/build-notes.md`](../runs/2026-09-02-draft9p1p4/build-notes.md)
measured the built socket against every row below.

Build **both halves in one Part Studio**, because the point of the exercise is the fit between
them.

## The drawings

| Picture | What it settles |
| ------- | --------------- |
| [`images/brief-socket.svg`](images/brief-socket.svg) | the joint in section, dimensioned, sitting in a limb. **The authority on every number** |
| [`images/cad-ball-and-socket-iso.png`](images/cad-ball-and-socket-iso.png) | the stud seated in the socket, in three dimensions |
| [`images/cad-ball-and-socket-section.png`](images/cad-ball-and-socket-section.png) | the same pair cut on the Front plane, so the cavity, the mouth and the slits are visible |
| [`images/cad-ball-and-socket-front.png`](images/cad-ball-and-socket-front.png) | the pair square on |

The three `cad-` frames are the reference CAD, not the specification;
[`README.md`](README.md) § *Where the `cad-*.png` frames came from* says which document, workspace
and version each was taken at.

## Read this before you build: run 1 got the socket the wrong way up

`grip` is **how far the cavity center sits below the mouth face**, with the socket's material
**above** the center. Run 1's brief said that and then told the builder to put the socket
rectangle *above* the origin, which is the opposite part — a shallow dish that cannot retain a
ball at all.

**The acceptance check cannot tell the two apart**, because 2 × √(6.08² − 2.2205²) is the same
either way. What distinguishes them is the cavity volume: the right one is a sphere less the cap
above the mouth plane, **717.14 mm³**; the wrong one is just that cap, **224.31 mm³**.
**Measure the volume, not only the mouth.**

## The idea being tested

**The socket is the ball, grown by the clearance.** Rather than drawing a second sphere and
hoping it stays concentric with the first, the ball is modeled once as its own part and then
subtracted from the socket body using **Boolean → Subtract with Offset**. The cavity is then
derived from the ball, so the two cannot drift apart, and the clearance is one number in one
field.

That whole approach rests on a claim from Onshape's help page:

> **Subtract → Offset**: *"Create a gap between the selected faces and remaining parts or
> surfaces."* Fields: **Offset all**, **Faces to offset**, **Offset distance**. Plus a **Keep
> tools** checkbox.

**Run 2 settled this: the offset does apply uniformly over a sphere.** It measured the mouth at
Ø5.802586 against Ø5.803 predicted, on the Ø6 ball this joint had then. Forum threads report
non-uniform offsets on other geometry; they do not apply here. Do not spend the run re-deciding
it. Take the mouth measurement anyway — it is how you find out whether your own model is right.

## The numbers

| Name | mm | Source | What it is |
| ---- | -- | ------ | ---------- |
| ball | 12 | plan | `#ball` = `#torsoH / 8` — the ball's diameter |
| stalk | 6 | plan | `#stalk` = `#ball / 2` — the neck the ball sits on |
| fit | 0.08 | plan | `#fit`, **not scaled — the printer decides**. The Offset distance. draft9p0 built 0.8; three live sources disagreed about where that came from, and 0.08 supersedes all of them — [`../runs/2026-08-25-draft9p1/a2-fit.md`](../runs/2026-08-25-draft9p1/a2-fit.md) |
| ball loss | 0.10 | plan | `#ballLoss`, what a printed ball loses on its radius. **Not scaled — the printer decides**, like the fit. It is the one protrusion loss this printer has been measured for: the hinge's axle came out 0.10 short a side. The mouth is drawn twice this much narrower so that the printed joint grips what the drawn one was meant to, and a caliper across a printed ball replaces it |
| cavity | 12.16 | derived | ball + 2 × fit. **Do not draw this.** It must come out of the offset |
| grip | **2.2205** | derived | `√((cavity / 2)² − (mouth / 2)²)`, on radii, because every other value in this column is a diameter. How far the cavity center sits **below** the mouth face — see the warning. It is no longer a chosen number: the mouth is chosen and this follows, so that changing the fit changes how deep the ball sits and nothing else |
| mouth | **11.32** | plan | `0.96 × #ball − 2 × #ballLoss` — the dimension the rest of the joint is built around, held whatever the fit is, because it is the snap. It is 94% of the ball as drawn and 96% of the ball as printed, and 96% is the snap that was chosen. Run 2 measured Ø5.802586 against 5.803 predicted on the Ø6 joint, so the arithmetic is trusted; draft9p1p4 measured Ø11.32 at this size |
| retention | 0.680 drawn, **0.480 printed** | derived | ball 12.000 less mouth 11.320, **on diameter** — what actually holds the ball. The printed ball is 0.2 mm smaller on diameter and the mouth prints as drawn, so what the printed joint holds by is 0.480, and each of the four tabs springs out half of it, 0.240. It does not move with the fit, which is the point of dimensioning the mouth |
| wall | 1.8 nominal, **1.72 real** | plan | `#torsoH * 3 / 160`, the socket wall, measured from the **ball's** surface rather than the cavity's. The material actually between the collar and the hollow is `#wall − #fit` = 1.72, because the fit comes out of the wall and not off the collar. **Quote 1.72 wherever this is quoted as a printed thickness.** It was 3.0, and thinning it is half of what makes the joint snap: the wall and the slit depth are the socket's spring, and `src/stickbot/socket_spring.py` is where that is worked out |
| collar Ø | 15.6 | derived | `#ball + 2 × #wall`. It moves if the ball or the wall moves, and **not if the fit moves** — that is the point of leaving the fit out of it. The study's FeatureScript computed `collarR = cavityR + WALL`, which put the fit in twice over and is superseded |
| collar length | **10.0** | derived | `#collar` = `#stand` — the ball's center to the bottom of the socket, which is exactly what the stud reaches the other way, so both halves of the joint give up the same length of limb to it. It is measured from the center and not from the mouth, so the fit moves the hollow and leaves the robot's height alone. It was `#ball / 2 + #wall`, which made the socket as deep as it was wide for no reason beyond that and left the two halves 7.8 mm and 10 mm |
| collar, proud | 12.2205 | derived | `#collar + #grip` — rim to root, which is the height a drawing sees and the only number the fit still reaches. A collar stands proud rather than bored flush so its tabs have free length and the ball has somewhere to swing: the joint reaches ±39.01°, against far less into a flat face. That is the mouth rim limiting the stalk, `asin(mouth / cavity) − asin(stalk / cavity)` = 68.58° − 29.56°, where the halves cancel because all three are diameters, which is `BALL_SWING` in `make_plans.py`. **±31.86° was the draft9p0 figure and ±41.76° was draft9p1's**; narrowing the mouth to hold the ball is what spends the difference |
| slits | 4 × 1.6, **6.2205 deep** | plan | cut from the collar's top face down to `#ball / 3` below the ball's center — z −4.0 — leaving a 6.0 mm floor, a ring joining the four fingers that springs them closed again. The depth is `#slit_d` = `#grip + #ball / 3`. The floor was `#ball / 4` and the depth 4.9465 mm; the extra 1.2740 mm of free length is the other half of the spring, because a finger's opening goes as the square of its length while its stiffness goes as the cube |
| `#slit_in` | 3.679 | derived | how far from the axis each slit's inner end stops, as `√((#ball / 2 + #fit)² − (#ball / 3)²) − #wall / 2`. It has to clear two things and clears both. Inside the **mouth** radius of 5.66 mm, by 1.9811 mm, or the mouth cannot open. Inside the **cavity** where the slit bottoms out, or the bottom of the cut is a pocket instead of a slot — that radius is 4.5789 mm here, and because the expression subtracts half a wall from it the margin is `#wall / 2` = 0.9 mm at any fit rather than a figure that has to be rechecked |
| `#slit_out` | 12 | derived | `#ball` — how far from the axis each slit's outer end runs. The slot has to finish outside a collar of radius 7.8 mm, and 12 mm clears it by 4.2 mm |

Put the **ball center on the origin**. Everything else is measured from there.

**The fit does not reach the outside of the part.** Since 2026-08-20 the collar's diameter is
`#ball + 2 × #wall`, so changing a printing clearance changes the hollow and nothing else — the
collar stays Ø15.6, and every part the socket is added to keeps the shape it had. The material
actually left outside the hollow is `#wall − #fit`, which is **1.72** at the current fit: four
perimeters at a 0.4 mm nozzle, so nothing is given up by measuring the wall from the ball instead
of from the cavity. It is 1.72 and not 1.8 that has to carry the tab, and 1.72 that B2 measures as
the thinnest wall in the part. At draft9p0's fit of 0.8 the same rule would leave 1.0.

**The slit's floor is fixed and its depth is not, which is the way round it has to be.** The floor
is `#ball / 3` below the ball's center — z −4.0 — and neither term moves with the fit, so the ring
under the tabs is 6.0 thick whatever the printer needs. The cut is then measured down from a top
face that does move, at z +`#grip`, so the depth is `#grip + #ball / 3` = 6.2205 today and grows
with the fit. Dimension the depth instead and the floor is what moves: that is what draft9p1p1's
model had, cutting a typed distance from the mouth, and it put the bottom of the cut below the
point where the cavity had closed to the slit's own inner radius, leaving a blind pocket in the
ring that is supposed to spring the tabs shut.

**The collar's diameter has one consumer outside this brief.** The gripper's body is sized to
support the socket sitting on it, so it follows this number and moves when it moves. What that
width is, and what it should become, is [`gripper.md`](gripper.md).

**Half these rows are not this table's to own.** The test is whether a tab outside the joint
dimensions something with the number. `#ball`, `#fit`, `#ballLoss`, `#grip`, `#stand` and
`#collar` all pass it, because the torso, the limbs, the foot and the gripper each build a stud or
a collar, so they are declared in the **Variable Studio**. So does `#wall`, as `#torsoH * 3 / 160`,
and the torso tutorial declares it before this one runs —
[`../runs/2026-08-25-draft9p1/a6-wall.md`](../runs/2026-08-25-draft9p1/a6-wall.md). What stays in
this Part Studio is `#stalk`, `#slit`, `#slit_in`, `#slit_d` and `#slit_out`, because nothing
outside the joint reads any of them. Declaring a local that repeats a studio row shadows the
studio's, which is the failure this rule is against.

**This table is where the joint's other numbers are decided.** It is not the only place they are
written down: since run 8p1 the model names them too, as `Variable` features whose values are set
from these rows, and the guide page carries them as a table and puts an expression in every
dimension box. A change to the fit, the wall or the slit width starts here, and reaches the model
as a new value on one variable and the page as a prose edit.

## Geometry, stated once so it cannot be read two ways

- **Ball center on the origin.** Everything is measured from there.
- **The socket's mating face is at z = +2.2205** (that is `grip` above the center).
- **All the socket's material is below that face.** The ball enters from above and is held
  because the mouth is narrower than the ball.
- The socket is a **collar Ø15.6 standing 12.2205 mm proud** of whatever it is added to, so its
  tabs have free length to flex. In this test build, stand it on a **Ø24 limb stub 20 mm long**,
  its top face at z = −10.0. That is the limb this joint really sits in.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Sketch on the Front plane.** A closed profile to the right of the vertical axis: an arc of
   radius 6 centered on the origin, a stalk of half-width 3 running **upward** from the ball,
   and a small base at the top of the stalk. Close it with a line on the vertical axis — that
   line is the revolve axis.
   - **The base is scaffolding, not a robot feature.** On the robot the stalk grows out of a
     torso face; here it needs something to stand on. Runs 2 and 3 both used **Ø10 × 10** at half
     this size; use **Ø20 × 20**, or say what you used instead. The volume check below counts it,
     so write down what you built.
   - **The stalk goes UP, away from the socket.** The socket's material is below the mouth face
     and the ball drops in from above, so a stalk below the ball would be buried inside the
     socket. Run 2's brief said "rising from" a base at the bottom, which is the wrong way up.
   - **Draw the arc first, then the lines.** Dropping an arc onto a line's free endpoint
     constrains it to the line rather than the point, and the sketch looks fully defined when it
     is not. Run 1 lost 18 minutes to exactly this.
   - **The join between stalk and ball is not dimensioned.** Make the arc's **upper** endpoint
     coincident with the **bottom** of the stalk and let the solver find it. An earlier version
     of this line said lower-to-top, which is the wrong way up: it survived the correction that
     turned the stalk around, and run 3 caught it.
2. **Revolve**, **New**, full revolve. Name it `Ball stud`.
3. **The limb stub**: sketch a **Ø24 circle** centered on the axis on the Top plane, and extrude
   it **20 mm downward** with a starting offset that puts its **top face at z = −10.0**, **New**.
   Name it `Socket body`. Earlier runs stood the socket on a 20 × 20 pad and got a part that
   looks nothing like the robot's — this is a limb, because on the robot it is a limb.
4. **The collar**: sketch a Ø15.6 circle centered on the axis **on the stub's top face** — the
   face at z = −10.0 that step 3 just made, not a default plane — and extrude it
   **12.2205 upward**, **Add** to `Socket body`. That lands the rim at z = +2.2205, which is
   `#grip` above the ball
   center and is what every socketed part in the robot measures. The collar is narrower than the
   limb it stands on, so there is a step all the way round.
5. **Boolean → Subtract.** Tools = `Ball stud`. Target = `Socket body`. Tick **Offset**, then
   **Offset all**, set **Offset distance** 0.08, and tick **Keep tools** — without it the ball is
   consumed. The dialog also carries **Reapply fillet**; leave it alone, but expect to see it.
6. **Relief slits**, four of them, 1.6 wide, cut 6.2205 down from the collar's top face so the
   mouth can open, leaving a 6.0 floor. Sketch **one slot to one side of the axis** and
   **Circular pattern** about the joint axis, **4 over 360°**; runs 2 and 3 both settled what that
   pattern wants for an axis, and it is written out below.
   - **The pattern is circular, and that is a requirement rather than a convenience.** It is what
     the step teaches, so the seed is the one a circular pattern can carry. The crossed-slot
     alternative below is recorded because it was live until 2026-08-27, not because it is
     available.
   - **The seed decides the count.** A slot drawn straight *through* the axis is already two
     slits, so it wants **2 instances over 90°**; four over 360 asks for two duplicates. A slot
     drawn to **one side** of the axis is one slit, and wants **4 over 360°**, which is also the
     default. Pick the seed first and the count follows from it.
   - **The shallow floor is what lets the seed stay to one side.** A cut that ran deeper would
     pass the point where the cavity narrows to the slit's own inner radius and turn into a
     pocket, and the only fix would be a profile reaching the axis — which is the crossed slot,
     and the end of the circular pattern. Stopping at `#ball / 3` below the center, with
     `#slit_in` set half a wall inside the cavity's radius there, keeps 0.9 mm of clearance at
     any fit, so the profile stays where it is.
   - **The tool decides whether you get an angle at all.** A **feature** circular pattern has an
     angle field, so either seed works. A **sketch** circular pattern has none: it arrives as a
     full circle and the only thing you set is the instance count, so a through-axis seed would
     put its second copy on top of its first. With that tool the seed has to be **one slot to one
     side of the origin, patterned 4 over 360°**. Runs 6 and 8p1 built it that way.
   - **A sketch pattern's center is loose, and the sketch stays blue until it is pinned.** The
     pattern turns its copies about a center point that arrives sitting on the origin without
     being held to it. Run 8 read that blue as the tool's limit; run 8p1 overturned it by
     constraining the point, and the canvas went from **3882 blue pixels to 0**. The move is
     **drag from the origin** — the origin cannot move, so what comes away under the pointer is
     the pattern's center — then click the origin, shift-click the center, and **Coincident**
     (`i`). A selection box over the two does not work: it picks up one point and the blue stays
     where it was. Do not undo the drag first, because Coincident snaps the pattern back on its
     own and an undo puts both points back on one pixel where neither can be picked. The step is
     written out with its frames in
     [`../../../instructions/stickbot-draft9p4/source/ball-and-socket.rst`](../../../instructions/stickbot-draft9p4/source/ball-and-socket.rst),
     under *Draw four slits*, at the Coincident near line 748.
   - **A `Feature pattern` needs `Reapply features` ticked.** Without it, it fails with *Could not
     create all instances as entered*, which is Onshape naming the fix in the error.
   - **The slit's inner end must sit inside the mouth radius, or the mouth never opens.** The
     mouth radius is half the mouth, which is dimensioned — 5.66, and it no longer moves when the
     fit does. A slit stopping outboard of it leaves the mouth a continuous circle, the
     tabs cannot spread, and the *four arcs* check below cannot pass. Run 8p1 satisfies it with
     a dimension, which is the form this rule asks for: `#slit_in` is measured from the
     origin at **3.679 mm**, against a mouth radius of **5.66 mm**, so it reaches 1.9811 mm
     inside the mouth.
     A slot pinned instead by its inner edge's **midpoint on the origin** satisfies the rule by
     construction, and costs the collar's floor its unbroken middle.
   - **The safe-feeling choice here is the wrong one.** The instinct is to start the slot
     *outside* the ball, at 6.0 or 6.8, to avoid cutting through it. That produces run 1's
     "decorative" slits. You have to deliberately drive the cut through the ball's volume and
     then defend the ball with the merge scope, below.
   - **Set `Merge scope` to `Socket body`.** Left at merge-with-all, the Remove reaches radius
     3.679 mm while the ball is radius 6.0 mm, so it cuts four slots into the ball as well — and
     every headline check in this brief still passes afterwards.
7. Rename both parts, and check.

## Acceptance checks

Measure these. Do not infer them.

- **Parts (2)** — `Ball stud` and `Socket body`.
- **The limb stub is Ø24.000 mm** and the collar is Ø15.600, so the step around the collar's foot
  is 4.2 mm wide. If either is square, stop and say so.
- **Mouth Ø11.320 mm.** Once the slits are cut this is four arcs, not a circle: measure one arc's
  radius and double it. At working zoom the mouth is about 60 px across and picking one specific
  arc is fiddly — clicking anywhere on a mouth arc gives a `Point: X / Y / Z` readout instead,
  which settles the radius as √(X² + Y²) and the mating face height at the same time. Either is
  acceptable; say which you used.
- **Ball Ø12.000 mm**, unchanged by the subtract.
- **`Ball stud` volume, unchanged by the slits.** Take it before the slits and again after; the
  two must match. This is the only check that catches a Remove whose merge scope was left at
  merge-with-all, which cuts four slots into the ball. Every other number in this list still reads
  correctly when that has happened: the part count, the ball diameter, the cavity, the mouth, and
  the slit z-extent. **There is no figure to check against at this size.** Run 7p1 and run 8 both
  measured 128.6210 mm³ on the Ø6 joint with a Ø10 × 10 base; every length in that part doubles,
  so a Ø20 × 20 base predicts eight times it, 1028.968 mm³ — but the base is scaffolding and this
  run has not built it. Record what you measure and what your base was, and this row gets a
  measured value.
- **Cavity spherical face radius 6.080 mm**, read off the face.
- **Cavity volume 717.14 mm³** — a full Ø12.16 sphere is 941.455, less the 224.314 cap above the
  mouth plane. **If you measure 224.31 mm³ you have built the socket upside down**; that is the
  run 1 failure and the mouth measurement will not catch it.
- **The slits are 6.2205 mm deep and leave a 6.0 mm floor.** They run from the collar's top face
  at +2.2205 down to −4.0, in a collar that runs −10.0 to +2.2205. **Measure the floor**: from the
  bottom of the cut to the bottom of the collar must be 6.0 mm. If it comes out 12.2 mm, the
  extrude went both ways from the face and only part of it went into the collar — that is run 1's
  failure, and when it happens **every other check in this list still passes**.
- **The cut is a slot for its whole depth.** At the floor the cavity's radius is 4.5789 mm, outside
  the slit's inner edge at 3.679 mm, so the bottom of the cut opens into the hollow rather than
  closing into the ring. Look down a slit from outside and you should see the ball; if the last
  millimeter is a blind step, the depth was dimensioned from the mouth instead of the floor being
  fixed.
- **The slit sketch is fully defined — no blue anywhere.** The seed's four dimensions do not
  finish it: the pattern's center has to be constrained as well, per step 6. Run 8p1 measured this
  as blue pixels on the canvas, 3882 before the constraint and 0 after, so it is checkable rather
  than a matter of eye.
- **The thinnest wall in the socket is 1.72 mm**, from the collar's outside to the cavity, and
  not the nominal 1.8. That is the number the tab has to carry.

## Render it and look at it

Render the socket **on its own**, from at least three angles, and look at the images — see
[`../../onshape-gui-howto.md`](../../onshape-gui-howto.md), *Rendering the model, and looking at
it*. Say in your notes whether the collar actually stands proud, whether each slit stops short of
the collar's root and opens into the cavity along its whole length, and whether the mouth looks
like something a ball could be pushed into. Run 1
reported relief slits as present when they
were, in its own later words, "decorative".

**Then hold your render next to [`images/brief-socket.svg`](images/brief-socket.svg) and say
whether they are the same shape.** Not the same numbers — the same shape. That comparison is what
would have caught the square pad.

## If the offset fails

Say so loudly and stop guessing. The fallback design is two concentric arcs sharing one center
point in one sketch, revolved separately — which costs a sketch and makes concentricity depend
on a variable rather than on construction. Do not build the fallback; just report.

## The two circular patterns, and which one you are holding

**The pattern is the method, not a stretch.** Step 6 cuts the slits with a circular pattern; two
crossed slots are the fallback if the pattern fights you, not the plan. Earlier versions of this
brief listed the pattern here as optional, which contradicted step 6.

Onshape has two tools with that name and they behave differently:

- **Sketch circular pattern**, in the sketch toolbar, shares a button with **Linear pattern**. It
  takes selected sketch entities, no axis and no angle: it arrives as a full circle at three
  instances with a `3x` tag, and the count is the only thing you set. It has **no green tick** —
  double-click the tag, type the count, press **Enter**, then move to white space and click. This
  is what run 8 used, and what the guide page teaches.
- **Feature circular pattern**, in the feature toolbar, takes a real axis. Runs 2 and 3 both
  answered the axis question the same way, so treat it as settled and build on it: the axis must
  be picked **explicitly**, it takes a **cylindrical face** — the limb stub's own outer face
  works — and it will **not** take a default plane. Run 3 adds the part that costs time: **the
  refusal is silent.** The field simply stays empty, with no error and no message. Nothing on
  screen says the pattern is unarmed, so check the field rather than the dialog's border.

## Recommended steps

**This is the feature order to build, and the name each feature carries.** It is the order a
proven model was built in, with the renames that have been settled since applied. Variables are
not in the table: each one is added immediately above the first feature that reads it, which is
what [`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *Phase A*
works out by walking the expressions. Do not open a tab with a block of numbers.

The verification after each feature and after the tab is one loop for every part, and it lives in
[`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *The verification
loop*. It is not repeated here.

| Step | Feature | Name |
| ---: | ------- | ---- |
| 1 | `newSketch` | `stud profile` |
| 2 | `revolve` | `revolve stud` |
| 3 | `newSketch` | `collar profile` |
| 4 | `extrude` | `collar blank` |
| 5 | `booleanBodies` | `cavity from ball` |
| 6 | `newSketch` | `slit profile` |
| 7 | `extrude` | `relief slits` |
| 8 | `mateConnector` | `stud connect to robot` |
| 9 | `mateConnector` | `socket connect to robot` |
