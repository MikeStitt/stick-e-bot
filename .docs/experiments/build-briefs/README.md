# Build briefs — what every one of them asks for

A brief is **a specification, not a lesson.** Build the part in Onshape, find the click path
that works, and write down what actually happened. The lesson is written from your notes
afterwards. Where a brief's step does not work as written, that is the finding — record what
you did, what you expected, and what happened, then deviate as little as needed and label it.

Read [`../../onshape-gui-howto.md`](../../onshape-gui-howto.md) before driving the browser, and
[`../../../.parts/onshape.md`](../../../.parts/onshape.md) for the modeling standard.

## A convention shared by two parts lives here, and only here

If two parts have to agree about something, this file settles it and the briefs do not restate
it. A brief says what is true of **its own part**; anything that only means something when two
parts meet — an axis, a sign, a station, a fit, a naming rule — belongs in a section below.

The failure this prevents is not disagreement, it is **invisible** disagreement. A convention no
single brief owns gets decided independently by each brief, every decision looks correct inside
the brief that made it, and nothing is wrong until the parts are assembled. Run 5 hit this twice:
the head and the feet faced opposite ways because no file said which sign of Y was forward, and
the hip through ground stations were five millimeters out because this README carried a copy of a
table `make_plans.py` computes.

So, when you find yourself picking a value because the brief did not give you one:

- If the value only affects your part, pick it, mark it **proposed** in the numbers table, and say
  what you did with it.
- If any other part can see it, **stop and add it here**, then reference it from the brief. Do not
  copy it into the brief — a copy is the failure, not the fix.
- If a number is computed somewhere already, link to the file that computes it instead of writing
  the number down.

## Every part is built standalone

Each brief builds **one part in its own document**, not the shared Part Studio. The real robot
is one Part Studio hung off one layout sketch, with every part modeled in place at its own
station — see [`../../robot-build-plan.md`](../../robot-build-plan.md). That model is assembled
from proven click paths; these briefs are how a click path gets proven.

So: build at the origin, not at the part's station. Where a brief needs a station height it
says so and gives the number.

## Coordinates

Onshape is **Z-up**. Top = XY, Front = XZ, Right = YZ. "Vertical" is Z; "fore-and-aft" is Y.

**The robot faces −Y.** Its front is the side Onshape's own Front view looks at, so the front
elevation and the Front view are the same picture. Every part that has a front and a back — the
head's face, the foot's toe, the shoulder's forward lean — puts it on −Y. This sign is the kind of
thing each brief will otherwise decide for itself, and run 5 assembled a figure with its head and
its feet pointing opposite ways before anyone noticed.

The robot's origin is the **center of the torso**. Every station is computed in
`src/stickbot/make_plans.py`, which holds them at module level so anything measuring
the CAD can import them rather than copy the arithmetic. **Import them.** The table below is a
printout, not a source; where it disagrees with the file, the file is right.

```
python -c "import sys; sys.path.insert(0, 'instructions/robot-guide'); import make_plans as p;
           print(p.SOLE_Z, p.ANKLE_Z, p.KNEE_Z, p.HIP_Z, p.SH_Z, p.NECK_Z, p.HEAD_T, p.HEIGHT)"
```

| Station | z | Station | z |
| ------- | -- | ------- | -- |
| ground, `SOLE_Z` | −178 | shoulder ball, `SH_Z` | +19.235 |
| ankle, `ANKLE_Z` | −154 | neck, `NECK_Z` | +58 |
| knee, `KNEE_Z` | −106 | top of head, `HEAD_T` | +137.4 |
| hip, `HIP_Z` | −58 | whole figure, `HEIGHT` | 315.4 |

Right-hand limbs only: the shoulder ball at x = 49.551 and y = −7.824, legs at x = 24 (`LEG_X`).

These are the draft9p0 stations, at twice the size, and **nothing has been built to them yet.**
The figure is 315.4 rather than a doubled 316.3, because the joint kept its own numbers while
everything around it grew. The 1× stations that run 5 measured on an assembled figure are in this
file's history; do not read across from them.

## Every number says where it came from

Each brief's numbers table carries a **Source** column:

| Source | Means |
| ------ | ----- |
| plan | [`../../robot-build-plan.md`](../../robot-build-plan.md) — a variable, or a station derived from one |
| built | measured on a model in a previous run |
| derived | arithmetic on the rows above it, and it moves when they move |
| proposed | **written for the brief and never checked.** A starting value. Say what you did with it |

A brief with no proposal in it is a brief nobody had to think about. A proposal presented as a
settled number is how a robot gets built to a figure somebody invented at a keyboard — which has
already happened once here, and is why this column exists.

## The drawings are part of the brief

Where a brief has a sheet in [`images/`](images/), read it before the numbers table. A table says
what the sizes are; a sheet says what the shape is, and every failure so far has been a shape
failure that passed its numbers — a socket built upside down, relief slits that did not cut
through, a fork drawn as a rectangle, a detent that cannot cam.

The sheets are generated by `src/stickbot/make_brief_sheets.py` from the same
constants as the student plan sheets. **Do not redraw a sheet by hand and do not edit the SVG** —
change the script and re-run it, or the sheets and the plan will disagree. Each sheet is written
as both `.svg` and `.png`; they are the same drawing.

`images/run2-*.png` are renders of what run 2 actually built. They are there to show you the
joint, and where a caption says so, to show you the defect being fixed. They are not the
specification.

## Where the `cad-*.png` frames came from

`images/cad-*.png` are the reference CAD, one part at a time, surveyed on 2026-09-18 and
recorded here so any of them can be taken again. A frame that cannot be re-taken from its own
record is not finished.

Each part names the document it was found in, the workspace to re-capture from, and the version
the frame was actually taken at. The version is what the picture shows; the workspace is where
the tab lives now, and it can move.

| Part | Document | Workspace | Version | Tab |
| ---- | -------- | --------- | ------- | --- |
| body, head, ball and socket, foot | `stickbot-draft9p4` `fe052e606c96bb7cc5aaf59f` | `0ff70e8921be572d630dd9cc` | `tutorial 8 - the foot` `7d52c006c01d272fd24cd706` | `body` `ef7be6f2a79aa87fdeb1d6ab`, `head` `95fe567f38e1c8c891bc94a3`, `ball and socket` `db77856cb0dc97213496331a`, `foot` `2a9178a3cd70f34183b13f41` |
| hinge, u limb, l limb | `stickbot-draft9p1p6` `500752af84dc92deea53f9e4` | `f30bf96cfeece59f61e0e7b2` | `F done - Phase F proved` `80c22eb7b8b0342ac03f8a6d` | `hinge` `62fca6aa5a67b51adcb2318c`, `u limb` `f3f8362fd5e9f31ee2fa5eb2`, `l limb` `261b7ee66567bab16d145c83` |
| gripper | `stickbot-draft9p1p1` `4b2e0d48efd37d3327a90afb` | `a1af16872d25103815f1c32a` | `Recovery point` `0f4e9b6b36b5c1a6f45197e1` | `gripper` `32166c7b3d22572c0e7dd0c3` |

**draft9p1p6's workspace no longer holds what its version holds.** Read at the workspace on
2026-09-18, the `hinge` tab is missing the `fork` part and `u limb` is missing everything past its
socket: 252 of the version's hinge faces and 249 of its upper-limb faces have no counterpart
there. The version is intact. Re-capture the hinge and the two limbs from the version, not the
workspace.

**The gripper's frames are the nearest CAD, not an agreeing one.** Its socket collar is Ø18,
which is the wall `make_plans.py` carried before `COLLAR_WALL` became `TORSO_H * 3 / 160`. No
gripper has been built since.

### Taking a frame again

The plain views are `shadedviews`, server-side, 1000 × 1000:

```
GET /api/partstudios/d/{did}/v/{vid}/e/{eid}/shadedviews
    ?viewMatrix={isometric|front|right|top|bottom}&outputHeight=1000&outputWidth=1000
    &pixelSize=0&edges=show&showAllParts=true
```

The `cad-*-section.png` frames come from the GUI's Section view, because `shadedviews` cannot
section: [`../../onshape-gui-howto.md`](../../onshape-gui-howto.md) § *Section: the GUI does it
and `shadedviews` does not* holds the route and the view keys. Each frame is cropped to the
canvas, with the view cube left in and the right-hand toolbar strip cut off.

| Frame | Plane | View | px per mm |
| ----- | ----- | ---- | --------- |
| `cad-ball-and-socket-section.png` | Front | Front | 23.967 |
| `cad-body-section.png` | Front | Front | 6.150 |
| `cad-head-section.png` | Right | Right | 8.049 |
| `cad-foot-section.png` | Right | Right | 7.124 |
| `cad-u-limb-section.png` | Front | Front | 10.895 |
| `cad-l-limb-section.png` | Front | Front | 9.887 |
| `cad-gripper-section.png` | Front | Front | 21.970 |
| `cad-hinge-section.png` | Right | Right | 8.833 |

**The hinge's section is on the Right plane, not the Front.** Its pin axis is Y, so the Front
plane is perpendicular to the pin and cuts the gap between the blade's two leaves: that section
shows a flat arch and no joint. The Right plane cuts along the blade and gives the two leaves,
the relief slit between them, both stub axles and the wedge rings edge-on.

**`cad-hinge-section.png` carries the blade alone.** The tab lays its two parts end to end rather
than engaged, with the blade's rod end at z = −38 mm and the fork's at z = +38 mm, so one section
cannot hold both. `cad-hinge-right.png` is the picture of them meshing.

**Its scale was measured off the frame, not read from the camera.** `onshape_screen.camera`
returned nothing on this tab across two runs, so `zoom_to`'s target of 9 px per mm is not what the
frame is known to be at. The Ø24 mm rod spans 212 px in the saved image, which is 8.833 px per mm.

## Every limb is a Ø24 cylinder

`#limbD` = `#torsoH / 4` = 24. **Settled 2026-08-11, and the joints are sized to fit inside the
limb — never the limb grown to fit a joint.** The hinge's fork is drawn as *full slices of the
Ø24 limb*, so its geometry is derived from that circle: the blade's full chord at ±5.0 is 21.817,
and its corners land **on** the Ø24 surface.

The nozzle sets the floor, not the sizes, and it does not scale with the robot — so at twice the
size the same wall is twice as many perimeters and the floor is further away than it was. The ear
is 6.4 because that is what makes it as strong as the tab it presses against, not because of any
number of passes. Where a dimension has a reason, the reason is in the part's own brief.

Do not invent a section for a limb. If a brief seems to want one, that brief is wrong — say so
rather than picking a number.

The build plan's Stage 5 lists four *teaching routes* for the limbs — sloppy quadrilateral,
ellipse, loft, filleted box — so that each limb teaches a different tool. **Those are tools, not
sections.** Where a route cannot produce a Ø24 cylinder, the route gives way, not the diameter.
Report it if you hit one.

## What every report must contain

Write `build-notes.md` — **not** `report.md`, which the Write tool refuses.

1. **Where the work is**, as the opening section: document name, document id, element id, a
   **published named version** with its id, the version link, and the workspace link labeled as
   live. Publish the version before you write. Say plainly whether you opened the links or only
   assembled them from ids.
2. **The click path that actually worked**, step by step, with real UI names, and the screenshot
   filename beside each step.
3. **Every acceptance measurement**, what you got against what was expected, and how you
   measured it.
4. **What did not work**: wrong assumptions in the brief, steps in the wrong order, anything
   that took more than two attempts.
5. **What the brief never said** that you had to work out for yourself.
6. **A retrospective**, answering three questions: what went well, what went poorly, and what
   would you change about the brief, the how-to, or the way you were briefed. Answer as
   yourself, about this run. This is a required deliverable, not a courtesy — you cannot be
   asked afterwards, because an agent that has finished cannot be reached.

## Screenshots are half the deliverable

**Drive the browser through
[`../../../src/stickbot/gui_steps.py`](../../../src/stickbot/gui_steps.py), not through bare
`page.mouse.click` calls.** Its `Steps` object takes each click with a sentence saying what you are
clicking, and writes the frame and both `steps.log` lines itself:

- `NN-a-select-<what>.png` — the moment something is **selected**, before you commit it. The
  selection must be visible: highlighted geometry, a filled dialog field.
- `NN-b-done-<what>.png` — the same step completed.
- `NN-x-<what>.png` — anything that surprised you.

`NN` is a counter that only goes up, so two frames never collide and the numbers are the order
things happened in. Run 5 keyed its screenshots by name instead, reused the names, and each frame
overwrote the last — that run has no click path recorded, only one reconstructed afterwards from
its scripts.

Zoom or crop where it helps. A screenshot in which the thing under discussion is 20 px wide
teaches nothing.

## Render every part on its own, and look at it

Before you write anything up, render each part **alone**, from at least three angles, using
`shadedviews` — [`../../onshape-gui-howto.md`](../../onshape-gui-howto.md), *Rendering the model,
and looking at it*. Say what you saw, and say if it does not match what the numbers implied.

This section exists because of two specific failures. A socket's relief slits were reported as
present and were, in the agent's own later words, "decorative". A hinge fork was invisible in
all four standard whole-model views because the parts overlapped along the camera axis, and
nobody noticed the joint had never been looked at.

## Measure, do not infer

Never claim a verification you did not perform: no menu name you did not see on screen, no
dimension you did not measure, no timing you did not clock. If you could not check something,
say you could not.

An acceptance check can pass on a wrong part. A relief slit came out 2.7 mm deep against 5.5
specified and every headline number still passed, because nothing measured the cut's z-extent.
Where a brief asks for an extent or a wall thickness, that is why.
