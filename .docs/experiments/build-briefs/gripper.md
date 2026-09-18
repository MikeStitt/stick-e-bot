# Build brief — the gripper

Read [`README.md`](README.md) first: deliverables, coordinate frame, and the settled Ø24 rule.

**The robot doubled on 2026-08-23 and this part barely did.** The bar is still 3.2, the clip is
still Ø10, and only the length and the socket grew. That is the thing this brief has always said
would happen, written as a hypothetical — *"if the robot were built twice the size the gripper
would still have to grip a 3.2 mm bar"* — and it has now happened for real. It changes two of the
decisions below, and nothing here has been built.

The gripper hangs off the wrist. It carries the **wrist socket** at the top and a **LEGO C-clip**
at the bottom — the thing the robot actually grips with. Two are printed; only the right one is
modeled, and it is drawn symmetric so that one part serves both sides.

**It was called a gripper and not a hand because it could not be wider than the wrist. It can be
now.** The argument was arithmetic on a Ø10 clip against a Ø12 limb: the first diameter that
flared past the wrist broke the socket unless the part grew by half, so the shape the numbers gave
was an end effector and the name followed the shape. See
[`decisions-waiting.md`](../runs/2026-08-12-run3/decisions-waiting.md) for that arithmetic.

**The wrist is Ø24 now and the clip is still Ø10**, because it grips a LEGO bar and LEGO did not
double. There is 7 mm of radius between them where there used to be 1, and the socket that used to
be the binding constraint is comfortably inside the limb. **The reason for the name has gone.**
Whether the part should now be hand-shaped is a design decision and this brief does not take it —
but it is no longer blocked by geometry, and saying so is the whole point of a brief that tracks
its own reasons.

## The idea being tested

**A part shaped so it has no handedness, and an interface sized by something outside the
model.** Two separate ideas, both worth a lesson:

1. **The C-clip opens forward, not outward.** A clip that opens outward makes the left gripper
   the mirror of the right and doubles the part count for nothing. Opening it forward makes the
   gripper symmetric about its own left-right centerline, so the same part serves both wrists.
   Getting the part count down by shaping the part is what a designer actually does, and it is
   invisible unless somebody says it out loud.
2. **`#barD` = 3.2 mm does not scale, and on 2026-08-23 it proved it.** Every other number in
   this robot is a fraction of the torso height. This one is a LEGO bar's diameter. The torso
   doubled and this row did not move, which is exactly what the lesson predicted and is now
   worth showing rather than asserting: put the r3 and the r4 plan sheets side by side and this
   is the one dimension that is the same on both.

**Those two ideas are why the part is shaped the way it is.** The gripper is the only part in the
robot whose defining dimension comes from outside, so it is the one part that cannot be
proportioned by dividing `#torsoH` — which is exactly why the doubling left it behind, and why the
question of whether it should now be hand-shaped is open above rather than closed here.

The clip is built with **Concentric** and **Sketch trim**: two circles sharing a center, trimmed
to leave a mouth the bar snaps through.

## The numbers

| Name | mm | Source | What it is |
| ---- | -- | ------ | ---------- |
| bar | 3.2 | plan | `#barD` — **set by LEGO, not by the robot** |
| clip bore | 3.3 | **proposed** | bar + a little; the clip must turn on the bar. **Do not apply `#fit` here.** It is 0.8 now, radially, so following the robot's own rule would give a 4.8 bore on a 3.2 bar — a bore half again as wide as the thing it grips. The fit belongs to the ball joint and to the printer, not to a LEGO interface. Run 3 built 3.3, and the model measures a bore of r 1.650 |
| clip outer | Ø10 | **proposed** | `CLIP_R` = 5.0, and it did not double, because it is set by the bar. The plan discusses `#clipR` but its variables table has no row for it — see the open question |
| clip wall | 3.35 | derived | (10 − 3.3) / 2, so it moves if the bore does |
| mouth | 2.6 | **proposed** | the gap the bar snaps through, narrower than the bar |
| gripper length | 24 | plan | wrist center to the bottom of the gripper — `#gripperL`, `#torsoH / 4`. Not `#gripL`: `#grip` is the socket's 3.6 and the two must not be confusable |
| body width | `2 × #collarR` = **18.0** | plan | the clip body along the bar's axis. It is the collar's own diameter, so the socket standing on it is flush all the way round. Typed as 9.4 once, stale twice — [`../runs/2026-08-25-draft9p1/a10-gripper.md`](../runs/2026-08-25-draft9p1/a10-gripper.md) |
| mouth angle | ±52.0° | derived | `asin(#mouth / #bore)` — where the two lips come 2.6 apart across the bore. Not a chosen angle |

**This table lists only what the gripper adds.** The wrist socket's numbers live in
[`ball-and-socket.md`](ball-and-socket.md) and are not restated here, because a number restated
in two files is a number that will disagree with itself.

## The body is sized by the socket, and this is the only part where that happens

**The gripper was widened so the clip body fully supports the bottom of the socket.** Before that
the socket overhung the body it stood on. The model built the body **9.4** across, which was
exactly the collar's outside diameter at the time — measured, not inferred: `clip body` was a
symmetric extrude of 9.4, and the part measured 9.4 across that axis.

**Settled: the width is `2 × #collarR` both ways, and the top of the part is a flat 18 × 18
square.** Two things were wrong with it as built, and both come from the same cause.

- **It was not flush.** The top of the gripper meets the socket edge to edge now: the body's top is
  a square of the collar's diameter, coaxial with the socket and tangent to it on all four sides,
  rather than a slab that happens to be wide enough to sit under it. A square and not a disc,
  because a square is what a rectangular profile extruded to the same width gives, and the collar
  standing on it is flush all the way round either way. Below that top a **45° chamfer of leg
  `#collarR − #clipR`** necks the body fore-and-aft to the clip's own Ø10 and lands on the mouth's
  upper lip, so below the lip the part is the clip circle and nothing else and no width of 18 is
  ever beside the mouth. Settled in
  [`../runs/2026-08-26-draft9p1p1/a/a3-gripper.md`](../runs/2026-08-26-draft9p1p1/a/a3-gripper.md),
  which measures the reference robot's own construction alongside it.
- **It was a typed number, and it went stale twice.** The collar moved to Ø9.0 and 9.4 did not
  follow, leaving a 0.4 overhang; then the collar moved again, to Ø18.0, and 9.4 was barely half of
  what it had to support. A number that goes stale twice in two design changes is not going to
  stop, which is why this is an expression and not a measurement.

**This is the only place the collar's diameter drives another part's dimension.** Everywhere else
the socket is added to something already big enough to hold it — a Ø24 limb, the torso, the head,
the foot — so the collar can change without anything following. The gripper is the exception
because it is the one part narrower than the joint it carries — and it is *more* of an exception
now, because the collar doubled while the clip stayed put.

**The gripper's CAD steps change with it.** Whatever order the gripper is built in has to make
the body's width follow the socket's outside profile, rather than draw a width and check it
afterwards.

**Two of that brief's checks do not hold on this part, and you should expect them not to.** The
gripper's collar does not stand on a Ø24 round limb, so the annular step round the collar foot is
not the 3.0 that brief describes; on the half-size part it was irregular, about 1.7 in x and near
nothing in y, and the collar's bottom edge came back as **eight arcs, not four**. Expect it to be
irregular again, and expect it to be *worse*: a Ø18.0 collar on a Ø10 clip body overhangs the clip
in every direction, where the Ø9.4 collar sat inside it. Measure the step and report its shape
rather than a single number. Everything else in that brief applies unchanged.

Build with the **wrist center on the origin** and the gripper running **downward**, so the bottom
of it is at z = −24 and the clip's center sits between them.

**The mouth is deliberately narrower than the bar.** 2.6 against 3.2 is 0.6 mm of interference,
which is what makes it snap rather than fall off. Whether that is the right number is a print
question, not a CAD question — model it and report it, do not tune it.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Sketch on the `Right` (YZ) plane and extrude the clip `Symmetric` along X.** The mouth is a
   gap trimmed *in* the profile, so the direction it opens always lies in the sketch plane and can
   never be the extrude direction — the mouth opens forward (−Y, the way the robot faces) and the
   gripper runs down (−Z), and `Right` is the only plane containing both. Extruding symmetrically
   about that plane makes the part symmetric about its own left-right centerline by construction,
   so it cannot be built handed, and puts the bar's axis along X so the robot grips a bar that runs
   left-right. (`Symmetric` depth is the TOTAL, so `2 * #collarR` gives x −9 … +9. The clip's own
   diameter did not double; the width it is extruded to did, because that follows the collar.)
2. **Two circles on one center**, Ø3.3 and Ø10, held **Concentric**. Place the center wherever the
   clip lands once the socket is placed — report what drove it. It was z = −7 on the half-size
   part; the socket above it is longer now, so do not assume −14.
3. **Trim** to leave the mouth: cut both circles where the opening is, and close the two ends.
   Report exactly what Sketch trim removes when you click an arc that is crossed twice, because
   that is the step a student will lose time on.
4. **Extrude** the clip, **New**. Name the part `Gripper`.
5. **Wrist socket** in the top face per [`ball-and-socket.md`](ball-and-socket.md), material
   below its mouth face, ball entering from above.
6. Blend the clip into the socket body so it is one solid, not two touching lumps. The reference
   robot does it by cutting rather than by rounding: a construction plane offset **zero** from the
   socket's root, then **Split part** and delete the crown above it. That leaves the clip's top
   flat and exactly at the root, and nothing has to be dimensioned to make it flush.

## Acceptance checks

Measure these. Do not infer them.

**This list is not the whole list.** The wrist socket carries its own checks in
[`ball-and-socket.md`](ball-and-socket.md), minus the two exceptions named above, and they are
performed on this part. An earlier version of this paragraph said run 3 ticked its way down this
list and shipped a socket with no relief slits — it did not. Run 4 measures the hand's collar as
**four** cylindrical faces, which is what a collar cut into four tabs looks like. The foot is the
part that has no slits; see [`foot.md`](foot.md).

- **Parts (1)** at the end.
- **Clip bore Ø3.300**, **outer Ø10.000**, measured off the model. **These are the two checks on
  the whole robot whose expected values did not change on 2026-08-23.** If either comes out
  doubled, something applied the scale factor where it does not belong.
- **Mouth 2.600** across the opening, at its narrowest. Measure the actual gap, not the sketch
  dimension — a trim that took the wrong arc gives a mouth that measures right on one side.
- **The part is symmetric about its own left-right centerline.** Check it: mirror the part about
  the YZ plane in a scratch feature and confirm it lands on itself, or measure the same feature
  at +x and −x. **If it is not symmetric the robot needs two of them and the part count goes
  up**, so this check is the whole reason the clip faces forward.
- **The clip's bore axis is parallel to X**, read off the model. The mirror check above does not
  catch a clip built on `Front` with its mouth opening downward: that profile is symmetric about
  x = 0, so it mirrors onto itself and passes every other check on this list, while the bore runs
  fore-and-aft and the robot grips a bar pointing away from itself.
- **Gripper length 24.000** from wrist center to the lowest point.
- **The top is one flat square face, 18.000 both ways**, with the Ø18 collar standing on it and
  flush all the way round. Measure both edges: a body that measures 18 across the bar and 10
  fore-and-aft is the defect draft9p1p1 exists to fix, and it passes every other check on this
  list. Measure the chamfer too — 4.000 of leg at 45°, ending on the mouth's upper lip — and the
  run of full width left above it, which is `#gripperL − #collarR − #mouth / 2 − #collar` = 4.700
  and is the number to watch if any of those four move.
- **Thinnest wall anywhere in the part**, and where it is. Not the clip wall: 3.35 is the thickest
  thing here, and nominating it is how the real answer gets missed. Expect **2.92** at the socket
  collar, which is `9.0 − 6.08` and is the same number on every socketed part in the robot. Run 3
  measured 1.500 there on the half-size part.

## Open questions to report on

- **`#clipR` has no row in the plan's variables table**, so Ø10 is a proposal and never was a
  variable. Whether it becomes one — and at what value — is open, and the old answers no longer
  apply: Ø12 made the clip flush with a Ø12 limb, which is now Ø24, and Ø14 broke a socket that
  has since grown. Anything up to about Ø24 is geometrically available now. What has *not* changed
  is that a wider clip does not grip a wider bar, so extra diameter buys stiffness and looks, and
  nothing else.
- **Reopened: the socket collar now overhangs the clip.** It was answered on the half-size part —
  run 4 measured the clip at r 5.000 on x = +3 and the collar at r 4.700 on the axis, so the clip
  was the wider of the two and the collar overhung nothing. At Ø18.0 against Ø10 the collar is
  much the wider, which is the same problem the body-width TODO describes and is the reason that
  TODO is now the first thing to fix rather than a tidy-up.
- Does the clip need a chamfer on its leading edges so the bar cams it open, rather than being
  levered open? The same argument was made for the hinge stub and it mattered there.

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
| 1 | `importDerived` | `copy socket` |
| 2 | `newSketch` | `clip profile` |
| 3 | `extrude` | `clip body` |
| 4 | `cPlane` | `plane to cut top of clip` |
| 5 | `splitPart` | `remove top of clip` |
| 6 | `booleanBodies` | `combine parts` |
| 7 | `mateConnector` | `mate to robot` |
