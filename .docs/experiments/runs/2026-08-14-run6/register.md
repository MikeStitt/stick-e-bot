# Run 6 — the register

What was resolved, what was not, and what was never attempted, in those words. The measurements
are in [`audit.md`](audit.md), [`evaluation.md`](evaluation.md), [`measured.json`](measured.json)
and [`replan-measured.json`](replan-measured.json); this file says where each thing stands and, for
the open ones, what it turns on.

## Resolved

Each of these has a measurement or a built, published artifact behind it.

- **Every station in the standing frame.** Read as mate connector world positions off
  `robot-run6-2026-08-15` (`cab79923d9e94d9f908d359f`) and compared against
  [`target.json`](target.json): hips, knees, ankles, sole, neck, shoulder balls, `HEAD_T` 69.1500
  and `HEIGHT` 158.1500 — including the two the head collar moved this run, which run 5 missed by
  5.5.
- **The torso is built front-first and it changed no geometry.** The rebuilt torso measures the
  same box as run 5's, which was a check in phase 5 rather than an assumption, and the 6p2 torso
  matches its own run 6 version face for face.
- **Every socket is slit, including the head's.** All four socketed parts read four cavity faces,
  four collar cylinders and four rim faces — the signature of a collar cut into tabs.
- **The thinnest wall in the parts is named and placed.** The 0.2531 land between neighboring
  detent valleys, which is the one number below a 0.4 mm nozzle. The tooth gap at 0.4531 clears one
  nozzle width.
- **The zero-pose arm clearance is +0.7754**, measured off the assembly against the torso brief's
  expected +0.776.
- **A Boolean union takes its name and its mate connectors from the first tool in the list.**
  Settled in phase 0 on two blocks in both selection orders
  ([`spike-boolean-mate.md`](spike-boolean-mate.md)) and first used for real on the gripper in 7a.
- **The joints reuse.** `Derived → Transform → Boolean Union`, from a named version of the joint
  document, on all six parts that carry a joint. The gripper went from ten features to four.
  `Derived` is reached from the **Alt + c** tool search and from no toolbar flyout, and a Part
  Studio takes one `Derived` per source and configuration — extra copies are `Transform ▸ Copy in
  place`, which is how the torso gets its five balls off one derive.
- **The hinge reuses as cleanly as the ball and socket, and it brings limb with it.** Not one of
  the fork's forty-eight detent teeth shows in the difference against run 6. Each half arrives with
  a length of limb attached, so the host part's own stock shortens to suit: the socket-clevis limb's
  rod is 3.85 and the blade-ball limb's is the 4 between its two ends.
- **The head's socket is upside down**, and its derive takes two transforms: a rotate of 180° about
  the head's own dome and a translate of z −22.15.
- **The foot's 7.35 collar.** The standard socket does not drop into the foot unchanged — it hangs
  1.85 clear of the plate — so the foot gets a `Pedestal under the socket` of its own. 7.35 is the
  standard 5.5 socket standing on 1.85 of foot, and the disagreement [`audit.md`](audit.md) carried
  between `foot.md` and `design-note.md` was two right answers about different things.
- **Neither joint document carries a mate connector**, so a derive brings none and the cut takes the
  host's own away. Every 6p2 part is given its phase-6 connectors again after the merge.
- **Five hand-built sockets did not stay the same socket.** Measured on the gripper: run 6's
  from-scratch slits cross the axis and the joint's stop short of it, which is one cavity face
  against four and 24.1627 mm³ of volume. The derived part is the faithful one. This is the
  replan's own case, measured rather than asserted.
- **Run 5's one open item is closed by the rebuild.** Its torso's `Shoulder R` and `Shoulder L`
  connectors sat at the old (±23, 0, +24) stations. Run 6's torso is built fresh with all five
  connectors placed on their own balls, and the assembly reads the shoulders at
  (±24.7754, −3.9118, +9.6177).
- **The guide exists, from a build that was performed.** `instructions/robot-guide2/` carries the
  two joints, the six parts and the assembly, every page written from the shots taken while the
  step happened, plus [`lesson-design.md`](../../../../instructions/robot-guide2/lesson-design.md)
  for the split, the floor, the ceiling and the recovery version.
- **The four habits are one habit, and the merge held.** *Look at the view cube*, *read the
  dimension back*, *read the field back* and *check New / Add / Remove* became **read the dialog
  back before you tick it**, and it fires at the point of use on every page rather than reading as
  a list to skim.

## Not resolved

Each carries what is known, what it turns on, and where it stands.

### No page of `robot-guide2` has been rebuilt from its own words

**Known.** Every page was written from a build that was performed, in the order it was performed,
with a shot per click. That is not the same test. The Constitution's rebuild gate asks for an empty
document driven only by the written steps, and it has not been run on the joints, on any part, or
on the assembly.

**Turns on** somebody walking each page in the GUI with the page as the only input, which is
another full build of the robot.

**Where it stands.** Stated as unmet in
[`README.md`](../../../../instructions/robot-guide2/README.md) and in `lesson-design.md`, so
nothing downstream reads the guide as proved.

### The session split is not clocked

**Known.** The four sessions are balanced on how many clicks each page captures — one `.. figure::`
per click or dialog. That measures length, not difficulty. The run's own step logs carry wall clock
for every build, but they are an agent driving a headless browser and include finding tools, fixing
its own mistakes and querying the API between steps.

**Turns on** somebody teaching it and clocking each session at student pace.

**Where it stands.** `lesson-design.md` states the *Fits the clock* gate unmet and carries no
student-pace number, and the two sessions with nothing to cut are named so the overrun has a
published version to fall back on.

### The brief does not pin the socket's slit topology

**Known.** [`ball-and-socket.md`](../../build-briefs/ball-and-socket.md) requires the slit's inner
end to sit inside the mouth radius, and both a slot that crosses the axis and four slots that stop
short satisfy that. Two builds from the same brief produced two different parts, and phase 5 passed
both because [`target.json`](target.json) does not pin topology either.

**Turns on** which one the joint is: the joint documents use four slots that stop short, so the
collar's floor stays in one piece.

**Where it stands.** The parts agree now, because they all derive from the joint. The brief still
permits the other one.

### `foot.md` does not carry the pedestal

**Known.** The brief says the ankle collar's proud length is set by the plate and gives 7.35 as a
consequence. What was built is a standard 5.5 collar on a 1.85 pedestal that belongs to the foot,
which reaches the same 7.35 by a different route and keeps the collar standard.

**Turns on** nothing measured — the built answer is settled. It is the brief that has not been
brought into line.

**Where it stands.** Open, and it is a documentation edit, not a build.

### Whether the detent band prints as bumps or as a smooth ring

**Known.** The land between neighboring valleys is 0.2531, below a 0.4 mm nozzle. It is a land
between two dimples on a face, not a wall between two voids — there is full blade behind it — so it
is a resolution question rather than a strength one.

**Turns on** printing one.

**Where it stands.** Open, and not answerable in CAD. `hinge.md` already asks it.

## Never attempted

Not decisions, and not conflicts. These are checks the briefs ask for that this run did not perform.

- **Print orientation, overhangs and bridges**, for every part. No part names an orientation and
  nothing identifies an overhang. This is the same gap run 5 left.
- **Joint ranges, and the shoulder clearance at the worst point of the cone.** No joint in either
  assembly was driven through its swing. The torso brief expects −1.597 there; the four revolute
  mates carry no limits and the nine ball mates carry none either, so the assembly will not report
  a range or a collision on its own.
- **The ear spring's margin.** `EAR_STRESS` 19.0484 MPa and `EAR_MOVE` 0.2038 mm are hand
  calculations in `make_plans.py`. The geometry they rest on is built and measured — ear 3.2000
  thick, `EAR_FREE` 11, teeth on r 4.8000 — but a stress is not something `bodydetails` returns.
- **Seating a ball.** Onshape solves rigid bodies, so a mate closes whether or not a real tab would
  flex. What is checkable is that the flexure exists — the slits are there, they run the collar's
  whole proud length, and the tab count is four everywhere — and that is what was checked.
- **Printing any part.** Nobody has printed the robot, so no fit, no flex and no detent click has
  been felt rather than measured.
- **The figure's pose.** Every ball mate is unlimited, so the arms rest where the solver left them.
  Arm span was not measured, because there is no pose to measure it in.
