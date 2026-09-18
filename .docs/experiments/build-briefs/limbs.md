# Build brief — the limbs

Read [`README.md`](README.md) first: deliverables, coordinate frame, and the settled Ø24 rule.

**Every number here moved on 2026-08-23 and none of them has been built.** The robot doubled.
The limb's own sizes are a clean 2×; the joint's are not, because `#grip` and `#fit` did not
scale. Where a run 3 measurement of the half-size part is still quoted, it says so.

This one brief covers the upper arm, forearm, thigh and shin, because once the limb is a Ø24
cylinder they are the same two parts. See *Four limbs, two parts* below — that is a finding, not
a decision, and it is the first thing to report on.

## The frames

| Frame | What it shows |
| ----- | ------------- |
| [`images/cad-u-limb-iso.png`](images/cad-u-limb-iso.png) | the upper limb: socket at one end, fork at the other |
| [`images/cad-u-limb-right.png`](images/cad-u-limb-right.png) | from the right |
| [`images/cad-u-limb-section.png`](images/cad-u-limb-section.png) | cut on the Front plane, through the socket and the axle bore |
| [`images/cad-l-limb-iso.png`](images/cad-l-limb-iso.png) | the lower limb: blade at one end, ball stud at the other |
| [`images/cad-l-limb-right.png`](images/cad-l-limb-right.png) | from the right |
| [`images/cad-l-limb-section.png`](images/cad-l-limb-section.png) | cut on the Front plane, through the blade and the stud |

**The reference CAD, not the specification.** [`README.md`](README.md) § *Where the `cad-*.png`
frames came from* names the document, workspace and version each was taken at.

## The stock

| Name | mm | Source | What it is |
| ---- | -- | ------ | ---------- |
| limb | 24 | plan | `#limbD` = `#torsoH / 4`. **A cylinder.** Joints are sized to fit inside it |
| segment | 48 | plan | `#armSeg` = `#legSeg` = `#torsoH / 2`. Both arm and leg segments |

Every limb is a **Ø24 cylinder, 48 long**, with a joint portion at each end. Nothing about the
limb's own body varies. Do not invent a section — see [`README.md`](README.md).

## Four limbs, two parts

| Limb | Top of the limb | Bottom of the limb |
| ---- | --------------- | ------------------ |
| **Upper arm** | shoulder socket | elbow fork |
| **Thigh** | hip socket | knee fork |
| **Forearm** | elbow blade | wrist ball stud |
| **Shin** | knee blade | ankle ball stud |

The shoulder and hip sockets are the same joint. The elbow and knee forks are the same joint.
So **the upper arm and the thigh are one part, and the forearm and the shin are one part** —
two unique limbs printed four times each, not four printed twice.

**Run 3 built both halves and found no geometric obstacle.** Neither part is handed — each is
symmetric about Front and about Right, the blade-ball's by construction and because its 24 × 15°
detent ring maps onto itself — so one printed part serves left or right as well as arm or leg.
The socket's ball joint absorbs any clocking between the collar slits and the hinge axis. The
only way the four diverge is a **load** argument, which no measurement settles: a shin carries
weight and a forearm does not.

**Report this, do not act on it.** If it holds, the robot has six unique parts rather than
eight, and the assembly's bill of materials changes. That is a design decision.

Build them as **two documents**: `limb-fork-run<N>` and `limb-blade-run<N>`. If
you find a reason they cannot be the same part, that reason is the most valuable thing in your
report.

## Geometry, stated once so it cannot be read two ways

Build with the **top joint's center on the origin** and the limb running **downward**, so the
bottom joint's center is at z = −48. That is the joint briefs' own frame and it makes both
joint portions reusable.

- - A **socket** is a collar Ø15.6 standing 12.2205 proud — see
  [`ball-and-socket.md`](ball-and-socket.md). Its material sits **below** its mouth face; on a limb
  top that points down into the limb, and the ball drops in from above. - A **ball stud** is Ø12 on
  a Ø6 stalk, the stalk running **into** the limb. - A **fork** and a **blade** are both full slices
  of the Ø24 cylinder — see [`hinge.md`](hinge.md). The fork spans the whole limb: slot 11.2, fork
  prongs 6.8, blade blank 10.0. The blade blank's corners land **on** the Ø24 surface, which is why
  the limb must be round.

## Suggested build order

Our best guess, not a tested path. Deviate where it does not work and say so.

1. **Sketch on the Top plane**: a Ø12 circle centered on the origin. Top is the plane parallel
   to the section and perpendicular to the build direction.
2. **Extrude the round stock, and it does not run the full 24.** Where it starts and stops is set
   by the joint at each end, not by the segment length:
   - **A socket top** wants the limb's top face at **z = −`#collar`** = −9.0, which is the
     socket's root, so the collar reaching up to the mating face at +`#grip` = +2.2205 stands the
     12.2205 the acceptance check asks for. Write it as the variables and not as the numbers: the
     root is placed off the ball's center and does not move with the fit, and the mating face does
     — [`ball-and-socket.md`](ball-and-socket.md) owns both.
   - **A blade top** wants the stock to stop **20 from the hinge axis** — `TAB_FREE`, per
     [`hinge.md`](hinge.md), because the blade blank occupies everything above that.
   - **A fork bottom** wants the stock to stop **21 from the hinge axis** — `EAR_FREE`. Earlier
     builds ran the rod on to the pin and filled the slot back in; [`hinge.md`](hinge.md) says
     what that costs.
   - The three rods that come out of those four ends are **32** on the upper arm, **18** on the
     thigh, and **18** on the forearm and the shin. `make_plans.py` derives all three.

   Run 3 hit this as a flat contradiction: this brief said "extrude the segment downward" and
   `hinge.md` said where to stop, and the builder followed `hinge.md`. **New**, and name the part
   for the limb it is.
3. **The top joint portion** — socket or blade, per the table above.
4. **The bottom joint portion** — fork or ball stud.

Both joint portions have proven click paths in their own briefs. If either fights you when
attached to a real limb rather than a test pad, that is a finding: it is the first time either
has been built onto Ø24 stock rather than onto a test pad.

## Acceptance checks

Measure these. Do not infer them.

- **Nothing anywhere lies outside Ø24.** Say it that way, not as "24.000 over the whole length":
  the round stock does not run the full 48 — the joint at each end occupies the rest — so a
  length-wise reading of this check has nothing to measure.

  **An axis-aligned bounding box cannot perform this check.** On the half-size part run 3's
  untrimmed fork corners sat at radius 6.539 and the box still read 12.000 × 12.000, because the
  corners were off the axes. Measure the **radius at every 5° around the part**, or take the trim
  feature's volume delta and confirm it is non-zero. Both were done in run 3; the box alone would
  have passed a bad part. - **Segment 48.000** between the two joint centers. - **Socket mouth
  Ø11.520** and **cavity volume 689.06 mm³** — the volume is what catches a socket built upside
  down; the mouth measurement cannot tell the two apart. - **The socket collar stands 12.2205
  proud**, measured as a z-extent, and its slits are 6.2205 deep and leave a 6.0 floor. - **Ball
  Ø12.000**, center on the axis at the station. - **Slot 11.200**, fork prongs equal to each other
  at **6.800**; **blade blank 10.000**, with a **4.000** slit down it leaving two leaves of
  **3.000**. - **The land** on each fork prong's inner face: 20.8 along the slot, the whole face
  across, **0.400** proud, so the seat measures **10.400** and the slot **11.200**. - **The rod's
  own length**, by bounding box: **32** on the upper arm and **18** on the other three. This is the
  check that catches a rod run on to the pin. - **Thinnest wall anywhere in the part**, and where it
  is. **On the fork limb the honest answer is zero**, and that is the design rather than a mistake:
  the fork prong is a slice of the Ø24 cylinder, so it thins to nothing where its inner face at |y|
  = 5.6 meets the cylinder, at |x| = 10.6132 — the 21.226 chord. It falls below one nozzle width
  over the last **0.221 mm** of that, and note that this taper barely moved when the robot doubled:
  the nozzle sets it, not the limb. Report the taper, and report the socket collar separately; the
  collar's real wall is **2.20**, not the nominal 3.0, and run 3 measured 1.500 on the half-size
  part. Do not let either stand as the other's answer. - **The relief slits open into the ball bore,
  and that is correct.** At `#slit_in` = 5.0 they break through into the Ø12.16 cavity — the
  resulting edges sit at r3.459 = √(6.08² − 5.0²). Say so in your notes so nobody later "fixes" it.

## What this brief does not answer

Four teaching routes in the build plan's Stage 5 were written for limbs with four different
sections, and a Ø24 cylinder is none of them. **Do not try to satisfy them here.**
[`README.md`](README.md) settles which gives way — the route, not the diameter — and asks you to
report it if you hit one. The routes with no home left at Ø24:

- the sloppy quadrilateral, which is where **Parallel**, **Perpendicular** and **Sketch Fillet
  and Chamfer** are currently earned
- **Loft**, whose only home was the upper arm's ellipse-to-rectangle change of section

## Recommended steps

**The feature order to build, and the name each feature carries.** Variables are not in the
table: each is added immediately above the first feature that reads it, which
[`../runs/2026-09-18-draft9p5/plan.md`](../runs/2026-09-18-draft9p5/plan.md) § *Phase A* works
out. The verification is in that plan's § *The verification loop*.


**Both limbs are nine features and no variables of their own**, everything coming from a derive.
Build them after the tabs they derive from, and publish a version of each of those first.

### The upper limb

| Step | Feature | Name |
| ---: | ------- | ---- |
| 1 | `importDerived` | `add socket` |
| 2 | `mateConnector` | `mate for fork` |
| 3 | `newSketch` | `limb section` |
| 4 | `extrude` | `limb` |
| 5 | `importDerived` | `add fork` |
| 6 | `transform` | `move fork` |
| 7 | `booleanBodies` | `combine parts` |
| 8 | `mateConnector` | `shoulder end` |
| 9 | `mateConnector` | `elbow end` |

### The lower limb

| Step | Feature | Name |
| ---: | ------- | ---- |
| 1 | `importDerived` | `add blade` |
| 2 | `newSketch` | `limb section` |
| 3 | `extrude` | `limb` |
| 4 | `mateConnector` | `mate for ball stud` |
| 5 | `importDerived` | `add ball stud` |
| 6 | `transform` | `move ball stud` |
| 7 | `booleanBodies` | `combine parts` |
| 8 | `mateConnector` | `elbow end` |
| 9 | `mateConnector` | `wrist end` |
