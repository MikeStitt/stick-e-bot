# Run 5 — the register

What was resolved, what was not, and what was never attempted, in those words. Measurements are in
[`repairs.md`](repairs.md) and [`evaluation.md`](evaluation.md); this file says where each thing
stands and, for the open ones, what it turns on.

## Resolved

Each of these has a measurement behind it, not an assertion.

- **The shoulder studs are on the doubly-rotated axis.** Five balls, all r 3.000, and the two
  shoulders at (±24.775, −3.912, +9.618) — the numbers `torso.md` asks for, to the thousandth.
- **The hinge's two halves match each other.** The blade's ball is r 3.000 at (0, 0, −24.000) and
  the fork's socket cavity is r 3.200 on the origin, so the joint's two ends are 24 apart, which
  is the station spacing the limbs are drawn to.
- **The foot's length runs along Y**, so the assembly's 90° turn came out.
- **The foot's toe is on −Y**, and `README.md` now states the sign for every part rather than
  leaving each brief to pick one. Not by run 5, which this line first credited: run 5 put the
  length on Y but left the toe on +Y, pointing out the robot's back, and closed the question
  anyway. Foot `run 5.1` turned it, and measures y −32.000 … +16.000 against run 5's
  −16.000 … +32.000.
- **The foot's relief slits cut the collar's whole 7.350 proud length.** The rim reads as four
  faces and the collar as four cylinders; the four slits took 46.048 mm³.
- **The foot's outline is tangent throughout.** Two `Tangent` constraints turned the outline black
  and the width to exactly 24.000.
- **`hinge.md` said 13 detent valleys and the model has 24 a side.** The brief now says 24, and
  this run measured 24 on each face at exactly 15.000°.
- **The robot assembles from named versions.** Thirteen mates, all `OK`, every instance inserted
  from a `run 5` version rather than a workspace —
  [`shots/s7-assembly-front.png`](shots/s7-assembly-front.png).
- **The station table in `build-briefs/README.md` was five millimetres out from the first joint
  down.** The parts match `make_plans.py`; the table did not, and now points at it.
- **The foot is as wide as the leg spacing, not wider.** `foot.md` asks whether the feet sit 4 mm
  outboard of the shins on a `#footHalf` of 16. Measured: the foot is x ±12.000 and `LEG_X` is 12,
  so the ankle sits on the leg's own axis. The 16 in that question is not in the part.
- **The torso's box is 36.000 × 24.000 × 48.000**, and no rollback was needed to say so. This run
  recorded the check as not attempted because the studs are on the finished part and the tree was
  never rolled back. They do not have to be: the block's six outer faces survive the studs, so the
  three opposed-plane spacings on the finished part *are* the box — 36.000 across X, 24.000
  through Y, 48.000 up Z, the last being `#torsoH`. The two ±Y faces are still unbroken
  rectangles of 1728.0 mm² = 36 × 48. Measured on `run 5` with `tools/measure_planes.py`.
- **The head's neck socket now has the four relief slits every other socket has** — built on
  2026-08-14 as head `run 5.1`, measured, and written up in
  [`../2026-08-13-head-collar/build-notes.md`](../2026-08-13-head-collar/build-notes.md). Not by
  the cheap answer this register proposed. Slitting the existing dome would have changed no
  station; what was built instead is the standard collar, 5.5 proud, so **the head moved up
  5.5 mm** and `HEAD_T` is +69.15. That was the change asked for, and the station table and the
  re-assembled figure both carry it.
- **The 0.400 mm annular slot inside the head's boss is gone**, and not by filling it. The collar
  replaced the boss, so the ring that shelling a 1.000 step left between r 4.400 and r 4.800 has no
  geometry to form in. The head's thinnest wall is now 1.2000 everywhere.
- **The two feet touch, and they are meant to.** The foot is x ±12.000 and the legs are at
  x = ±12.000, so both inner edges land on x = 0.000 — and the contact is one point, not an edge,
  because the two r12.000 toe arcs are circles of equal radius with their centers 2r apart. This
  register carried it as a conflict turning on `#hipHalf` with "let them splay" as the cheap
  answer. It is neither: touching is reachable from many joint combinations rather than being a
  property of the straight-down pose, and straight down is the pose drawings are dimensioned from,
  because a rotated foot is no longer orthogonal to X, Y and Z. Decided, with the reasoning, in
  [`../../build-briefs/foot.md`](../../build-briefs/foot.md).

## Not resolved

Each carries what is known, what it turns on, what the options cost, and where it stands.

### The torso's `Shoulder R` and `Shoulder L` mate connectors are at the old stations

**Known.** They sit at (±23, 0, +24), which is where the square studs were before S1. The balls
are at (±24.775, −3.912, +9.618). S1 moved the geometry and left the connectors. Opened in the
Part Studio on 2026-08-14: both are **On entity → Origin** with a typed **Move** of (23, 0, 24)
and (−23, 0, 24). They are offsets from the origin point, not attachments to the ball, which is
why moving the geometry could not carry them along.

**Two of seven, not all of them.** The Part Studio holds seven mate connectors. `Shoulder drop
axis` and `Shoulder swing axis` are construction geometry — `Drop the shoulder 53` and `Swing the
shoulder forward 30` rotate about them — and deleting either would take the 53°/30° shoulder axis
with it. `Neck`, `Hip R` and `Hip L` are at their correct stations. Only the two named here are
wrong.

**Turns on** nothing in the assembled figure. Run 5 placed two new connectors on the ball faces in
the assembly itself, and the two shoulder mates use those, so the figure is mated at the right
spot. The defect is in the torso Part Studio alone, and it is a trap for the next assembly rather
than a fault in this one.

**Options.** Attach the two to the ball faces so they follow the geometry, which is right and
re-cuts a torso version the assembly already references. Give them corrected typed offsets, which
matches how `Neck`, `Hip R` and `Hip L` are built and leaves the same trap set one station over.
Delete them, which leaves three joints with a named connector and the shoulders without.

**Where it stands: carried into run 6, on purpose.** Not fixed in run 5 and not to be fixed there.
How the joints are modeled is being reworked, and that rework decides which of the three options
is even the right shape. Fixing it first would re-cut a referenced version to install an answer
run 6 may replace.

## Never attempted

Not decisions, and not conflicts. These are checks the briefs ask for that this run did not
perform.

- **The thinnest wall in five of the six parts**, which four of the six briefs ask for by name.
  This was recorded here as blocked — `bodydetails` returns faces, not the distance between two of
  them, and the Feature Script endpoint that would answer it returned 429 for the whole second half
  of the run. **It was not blocked.** The head-collar run took the check on the head with
  `featurescript` still throttled, by pairing `bodydetails` with `GET .../tessellatedfaces`, which
  answers 200; the method is in *Measuring* in
  [`onshape-gui-howto.md`](../../../onshape-gui-howto.md), and the head's answer is 1.2000.
  Torso, both limb halves, hand and foot have still not been measured. **This first said there was
  nothing stopping it, which was a claim rather than a check.** Checked since: `bodydetails` comes
  back for the torso and both wall searches run on it, so the shell walls of all five are reachable
  today. The tessellation is the part that needs care — it must be streamed rather than pulled
  through `page.evaluate`, and its tolerance sized to the part, or the request does not finish.
- **Print orientation, overhangs and bridges**, for every part. The *Printable* axis asks for the
  orientation to be named and the overhangs identified; neither was done for any part.
- **Joint ranges and the shoulder clearance.** No joint was driven through its swing. The torso
  brief's clearance figures — +0.776 at the zero pose, −1.597 at the worst point of the cone — were
  not checked against the assembled geometry.
- **Seating a ball.** Not attempted, and not attemptable here: Onshape solves rigid bodies, so a
  mate closes whether or not a real ball would pass the mouth. Nothing in this run tells anyone
  whether any of the four sockets works.
- **The figure's pose.** Both shoulders, both hips, both ankles and both wrists are ball mates
  with no limits, so the arms rest where the solver left them — one out level, one hanging. Arm
  span was not measured because there is no pose to measure it in.
