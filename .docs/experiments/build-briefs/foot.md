# Build brief — the foot

Read [`README.md`](README.md) first: deliverables, coordinate frame, and the settled Ø24 rule.

**Every number here moved on 2026-08-23 and none of them has been built.** The foot is a clean
2×; the joint inside it is not, because `#grip` and `#fit` did not scale. Two of the open
questions below changed answer because of it, and one of them changed answer for a reason nobody
decided — read them.

The foot carries the **ankle socket** and stands on the ground. Two are printed; only the right
one is modeled, and it is drawn symmetric so that one part serves both ankles.

## The frames

| Frame | What it shows |
| ----- | ------------- |
| [`images/cad-foot-iso.png`](images/cad-foot-iso.png) | the sole, the rounded toe and heel, and the ankle socket |
| [`images/cad-foot-bottom.png`](images/cad-foot-bottom.png) | the sole from below |
| [`images/cad-foot-section.png`](images/cad-foot-section.png) | cut on the Right plane, through the ankle socket and the tread |

**These are the reference CAD, not the specification.** [`README.md`](README.md) § *Where the
`cad-*.png` frames came from* names the document, workspace and version each was taken at, and
what is wrong with the part it shows.

## The idea being tested

**A plan shape belongs on a plan-parallel face.** The foot's outline is something you see from
above, so it is sketched on the **Top** plane and built upward — not on Front and rotated. This
is the course's sketch-plane set piece, and the foot is the clearest case in the whole robot:

> **Sketch on the face that is parallel to the shape you want to draw, and perpendicular to the
> direction you want to build in.**

Pick the wrong plane and the projection is a foreshortened shadow that is geometrically correct
and not what you meant. **If you can, build it wrong once on purpose and screenshot the
symptom** — the lesson needs a picture of the failure, not only of the success. Say clearly
which screenshots are the deliberate mistake.

The second idea is the same one the gripper carries: **the foot is symmetric about its own
fore-and-aft centerline**, so it has no handedness and one part serves both sides. A heel spur
or an angled tread would break that and cost a whole extra part.

## The numbers

| Name | mm | Source | What it is |
| ---- | -- | ------ | ---------- |
| length | 96 | plan | `#footL`, `#torsoH` — the foot is as long as the torso is tall |
| width | 48 | plan | `#footW`, `#torsoH / 2` |
| ankle height | 24 | plan | `#ankleH` — ground to the ankle ball center |
| plate | 12 | **proposed** | how thick the foot is before the fillets |
| top fillet | 8 | **proposed** | heavy, so it reads as a boot rather than a slab |
| socket collar Ø | 18.0 | derived | 2 × (ball 6.0 + wall 3.0) — see [`ball-and-socket.md`](ball-and-socket.md) |
| socket collar length | 9.0 | derived | `#collar` = `#ball / 2 + #wall`, the ankle ball's center to the collar's root — [`ball-and-socket.md`](ball-and-socket.md) |
| ankle boss, proud of the plate | 14.2205 | derived | `#grip + #plate` = 2.2205 + 12. Of that, 12.2205 is the collar itself and **2.0 is a pedestal the foot puts under it**, which is `#plate − #collar`, where `#collar` is now `#stand` = 10. Earlier drafts read that pedestal as the foot failing to reach a collar length of 11.0; it is not a failure, it is the foot standing its socket high enough to clear a 12 mm plate |
| sole ribs | 6 wide × 2 deep | **proposed** | `#rib_w` and its depth, across the sole, linear pattern |
| tread repeat | 12 | derived | `2 × #rib_w` — groove and land. It divides the 96 sole **eight** times, which is the count |
| tread offset | **3** | derived | `#rib_w / 2`, so the groove is centered in its own repeat |

**The tread's phase comes from the groove and nothing else.** Centering the groove in its repeat is
what leaves land at both ends of the sole, and it makes the two margins equal at 3 without either
being chosen. draft9p0 offset the pattern by `#foot_l − #heel_y`, which is 64 on a 96 sole: five of
its eight grooves are cut in empty air past the toe. A wrong phase regenerates green, so measure
the margins. The arithmetic and the phase that was not adopted are in
[`../runs/2026-08-25-draft9p1/a5-foot-tread.md`](../runs/2026-08-25-draft9p1/a5-foot-tread.md).

Build with the **ankle ball center on the origin**, the foot below it, so the ground is at
z = −24 and the plate's top face is at z = −12.

**The foot is longer forward than back.** 96 long with the ankle at a third from the heel gives
y +32 behind and y −64 in front, which is roughly where a person's ankle sits. Report whether that
looks right or whether the figure appears to be tipping forward. **Forward is −Y** — the robot
faces the side Onshape's Front view looks at, and [`README.md`](README.md) says so for every part.
Earlier versions of this brief put the toe on +Y and run 5 assembled a figure whose feet pointed
behind its head.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Sketch on the Top plane.** The outline is arcs and lines, tangent throughout: a rounded
   heel, two sides, a wider rounded toe. The foot's length runs **fore-and-aft, along Y**, so make
   it **symmetric about the Right (YZ) plane** — that is the fore-and-aft centerline — using
   **Symmetric** constraints, not by dimensioning both sides.
2. **Extrude** upward 12, **New**. Name the part `Foot`.
3. **Fillet** the top edges heavily, r8. Report which edges Onshape lets you take in one feature
   and whether the tangent chain is picked up automatically.
4. **Ankle socket** in the top face per [`ball-and-socket.md`](ball-and-socket.md). The collar
   lifts the socket mouth clear of the plate entirely — that is deliberate, and it is what lets
   the foot be any size and shape without the ankle caring. How far it stands proud is set by the
   plate, not chosen: see the acceptance checks.
5. **Sole ribs**: one rib across the sole — `#rib_w` wide in Y, running the sole's width in X,
   its near edge **`#rib_w / 2` in from the end of the sole** — then **Linear pattern** along Y at
   `2 × #rib_w`, `#foot_l / (2 × #rib_w)` of them, which takes the **Front** plane as its
   direction. Report whether it will take an edge instead. **Do not offset the pattern by anything
   that belongs to the heel.** The phase comes from the groove's own width and nothing else, which
   is what centers the groove in its repeat and leaves land at both ends.

## Acceptance checks

Measure these. Do not infer them.

- **Parts (1)** at the end.
- **Length 96.000, width 48.000**, off the model's bounding box.
- **Ground at z = −24.000** and the ankle ball center at the origin, so ankle height is 24.000.
- **The part is symmetric about its own fore-and-aft centerline.** Check it, do not assume it —
  mirror it about the **Right (YZ)** plane in a scratch feature and confirm it lands on itself.
  **If it is not symmetric the robot needs a left foot and a right foot**, and that is the whole
  reason the outline is drawn this way.
- **The outline is tangent throughout** — no corner where an arc meets a line. Look for a
  visible crease in the rendered image as well as checking the constraints.
- **Socket mouth Ø11.520** and **cavity volume 689.06 mm³**. The volume is what catches a socket
  built upside down.
- **The ankle boss stands `#grip + #plate` = 14.2205 proud** of the plate's top face, measured as
  a z-extent, and **2.0 of that is pedestal**. The collar itself is 12.2205, the same as on every
  other socketed part; `#pedestal` = `#plate − #collar` = 2.0 makes up the rest, and it is a whole
  number because the collar's root is now placed off the ball's center. Measure both: the boss as a
  z-extent, and the step where the pedestal meets the collar's root at z = −9.0. Do not move the
  plate to close it. See
  [`decisions-waiting.md`](../runs/2026-08-12-run3/decisions-waiting.md).
- **The sole ribs exist and removed material.** Every other check on this list passes on a foot
  with no ribs at all, which is how run 3 nearly shipped one: the pattern regenerated into
  nothing and the volume did not move. Measure **the sole's two z levels** — rib faces at
  z = −24.000 and groove floors at z = −22.000 — and **the volume the ribs removed**, and report
  the rib count. **Count eight, and measure the land at each end: both are 3.0.** A pattern whose
  phase is wrong still regenerates green, and its volume moves by one groove at most, so the two
  margins are the check that catches it. Run 3 measured seven groove floors and 419.07 mm³ removed
  on the half-size foot, at a phase draft9p1 does not use; scaling that to eight ribs of twice
  every dimension gives about 3833 mm³. That is arithmetic — the rib count and the margins are what
  you should actually report.
- **The ankle socket has relief slits.** Run 4 measured the collar as a **single** cylindrical
  face — four slits would show as four. The limb's collar in the same run came back as four faces
  totaling 26.3 of a possible 29.5 circumference on the half-size part, which is what a slit
  collar looks like from the API. Without slits the whole circumference has to stretch to pass a
  Ø12 ball through a Ø11.520 mouth, and this is the one joint on the robot nobody can assemble.
- **Thinnest wall anywhere in the part**, and where it is. Earlier drafts nominated the plate edge,
  which is now 4 mm where the 12 mm plate meets its r8 top fillet. The socket collar is thinner:
  **2.20**, which is `9.0 − 6.8` and has nothing to do with the plate. Report both.

## Open questions to report on

- ~~The feet are wider apart than the legs, and the gap doubled with everything else.~~
  **Answered on 2026-08-26: the feet are not handed and the offset goes.** The ankle is on the
  foot's own left-right centerline, so `FOOT_X` is `LEG_X` and both feet sit at x ±24. The model
  already builds it that way; it is `make_plans.py` and the sheets that carry the 32.
  [`../../robot-build-plan.md`](../../robot-build-plan.md) holds the decision and the reason.
- ~~Do the r4 top fillets leave enough flat around the collar to sit on?~~ **Answered by run
  3: 0.443 mm of flat** on the half-size foot. Doubling gives 0.886, and the collar radius grew by
  less than double — 9.0 against 9.4 — so expect nearer **1.29**. That is arithmetic; measure it,
  because it is little enough that nobody should move either number without re-checking it.
- ~~The brief and the model disagree about which way the foot points.~~ **Answered by run 5.1.**
  Run 5 put the outline's length on Y, which took out the assembly's 90° turn, but left the toe on
  +Y and closed the question anyway. Run 5.1 turned it to −Y. The sign is stated once, above.
- ~~The foot is not symmetric.~~ **Answered by run 5**, by the same re-sketch: both circle centers
  sit on the Right plane's trace and the two side lines carry a `Symmetric` about it.
- ~~The two feet touch.~~ **They do, and that is the decision rather than a coincidence.** The
  old argument was that the plate is x ±12 in its own frame and the leg is at x = ±12, so both
  inner edges land on x = 0 and the two toe arcs are exactly tangent. Doubling kept the half-width
  at 24, and with the offset withdrawn the inner edges meet at x 0 again. Feet that touch when the
  legs and ankles hang straight down from the hips is a stance the design accepts, because every
  joint below the hip turns and some pose always brings them together.
- Is a 96 mm foot on a 315.4 mm figure goofy in the way the brief wants, or just big? Render it
  and say. The proportion barely moved — 0.32 of the figure before, 0.30 now — so if it read as
  goofy at the old size it should still.

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
| 1 | `newSketch` | `pedestal outline` |
| 2 | `extrude` | `foot pedestal` |
| 3 | `newSketch` | `foot outline` |
| 4 | `extrude` | `foot` |
| 5 | `fillet` | `top round` |
| 6 | `newSketch` | `groove profile` |
| 7 | `extrude` | `sole groove` |
| 8 | `linearPattern` | `sole ribs` |
| 9 | `importDerived` | `add socket` |
| 10 | `booleanBodies` | `combine parts` |
| 11 | `mateConnector` | `mate to robot` |
