# Build log — the ball and socket

Built 2026-08-11 in Onshape, GUI only.

## Where the work is

The geometry lives on Onshape's servers, not in this repository. This section is the only
pointer to it.

| Field | Value |
| ----- | ----- |
| Document name | **`joint-ball-socket`** |
| Owner | mike@stitt.cc |
| Document id | `dc438a192a01922a9d1ee540` |
| Element | Part Studio 1 — `e9a1b71b3b016e4d3e47eda0` |
| **Cite this version** | **`v1-offset-test`** — `304ce0c9703dbfaa6b7ee4ee` |

**Named version** (what the measurements below were taken from):
<https://cad.onshape.com/documents/dc438a192a01922a9d1ee540/v/304ce0c9703dbfaa6b7ee4ee/e/e9a1b71b3b016e4d3e47eda0>

**Live workspace** (moves under you — do not cite it in course material):
<https://cad.onshape.com/documents/dc438a192a01922a9d1ee540/w/464772f981c008d77ef8ad24/e/e9a1b71b3b016e4d3e47eda0>

The version list holds only `Start` and `v1-offset-test`, so that one version is the whole
recovery story for this document. The ids were read from the live tab and from the versions
API; **neither URL has been opened**, so they are assembled from verified ids rather than
followed.

## Verdict

**It built, and Boolean → Subtract with Offset works. The offset applies uniformly over a sphere.**

> **Mouth measured Ø4.99600 mm. Expected Ø4.996 mm.**

Three independent measurements agree, each of which would fail differently if the offset were non-uniform:

1. Mouth circle where the cavity breaks the mating face: **Ø4.99600 mm**.
2. The cavity's spherical face reports **Radius 3.20000 mm** — read off the face, not inferred.
3. Socket volume implies a **mathematically exact Ø6.4 sphere**: measured **2227.40862 mm³** vs 2352 − (137.25835 − 12.66690) = 2227.4086. Agreement to 1 part in 10⁷.

The premise holds: the socket can be derived from the ball, clearance is one number in one field. **Do not build the fallback.**

**But the brief's build order does not build the joint it describes** — see the `grip` contradiction.

## Measurements

| What | Expected | Measured | Screenshot |
| ---- | -------- | -------- | ---------- |
| Mouth Ø (socket above origin, per brief step 3) | 4.996 | **4.99600 mm** | `16-b-done-mouth-measured.png` |
| Mouth Ø (socket gripping ball, corrected) | 4.996 | **4.99600 mm** | `22-b-done-mouth-measured-gripping.png` |
| Cavity spherical face radius | 3.200 | **3.20000 mm** | `17-a-select-cavity-face.png` |
| Ball radius after subtract | 3.000 | **3.00000 mm** | `18-b-done-ball-radius.png` |
| Mating face area (14×14 less mouth) | 176.3965 mm² | **176.39646 mm²** | `22-b-done-mouth-measured-gripping.png` |
| Socket volume, brief's geometry | 2339.3331 mm³ | **2339.3331 mm³** | `19-b-done-socket-volume.png` |
| Socket volume, corrected | 2227.4086 mm³ | **2227.40862 mm³** | `21-b-done-socket-volume2.png` |
| Parts | 2 | **2** — `Ball stud`, `Socket body` | `12-b-done-two-parts.png` |

Cavity by difference: brief's geometry 2352 − 2339.3331 = **12.6669 mm³**, exactly the spherical cap πh²(3r−h)/3 (r=3.2, h=1.2) = 12.66690. Corrected: 2352 − 2227.40862 = **124.5914 mm³**, exactly sphere-less-cap. Units were mm with **Display decimals 0.12345**, so all figures are five-decimal GUI readouts.

## The `grip` contradiction — read before writing the lesson

The brief defines `grip = 2` as "how far the cavity centre sits **inside** the socket's mating face", then step 3 says the socket rectangle's bottom edge is "2 mm **above** the origin". Those are opposites, and **the acceptance check cannot tell them apart**, because 2√(3.2²−2²) is the same either way.

Built as step 3 says, the mating face sits above the ball centre, the cavity is a 1.2 mm dish, the mouth is the *widest* part of the cavity, and the ball is not retained at all. The cavity volume of 12.667 mm³ is the giveaway — the brief itself predicts "a sphere minus the cap" (≈124.6 mm³), which is the other configuration.

**The rectangle's bottom edge must be 2 mm BELOW the origin.** That matches the sheet-2 section detail and is the only version needing relief slits. The fix was one edit: open Sketch 2, double-click the 2 mm dimension, type **−2**. Onshape accepts a negative distance and flips the rectangle across the axis; the dimension still displays `2` (`20-x-negative-dim.png`). Everything regenerated clean. For a class, dimension the rectangle's **top** edge to 10 instead — unambiguous, and doesn't rely on knowing that a minus sign flips a dimension.

## The click path that actually worked

1. **Create → Document…**, name `joint-ball-socket`, **Create**. `01-a/b`
2. **☰ → Workspace units…** → **Length default unit = Millimeter**, **Display decimals = 0.12345**, green ✓. `02-x-hamburger-menu.png`, `02-a`, `02-b`
3. Select **Front**, click **Sketch**, cursor over graphics, press **n** (View normal to). `03-a`, `03-x-normal-to-view.png`
4. **Draw the arc first.** Arc dropdown → **Center point arc** (menu also has *3 point arc* `a`, *Tangent arc*, *Elliptical arc*, *Conic*). Click the **origin** as centre — this pins the ball centre — then the start point on the axis, then sweep clockwise to the end. `04-x-arc-menu.png` *(reverse of the brief's order, and it matters)*
5. **Line**: close the profile from the arc's lower endpoint down the stalk, out along the base, back up the axis to the arc's upper endpoint. Hover each existing point until it highlights before clicking. `07-a-select-snap-arc-end.png`, `07-a-select-snap-base-corner.png`
6. **Dimension** (`d`) ×5: arc **R3**; stalk-to-axis **1.5**; base width **5**; base height **10**; origin-to-base-top **6**. All black. `05-a-select-radius-dim.png`, `07-b-done-sketch1-fully-defined.png`
7. ✓, then **Revolve** (`shift+w`): click the region → *Face of Sketch 1*; **click the "Revolve axis" field**, then the axis line → *Edge of Sketch 1*; **Full revolve** and **New** already set. ✓ `08-a-select-revolve.png`, `08-a-select-revolve-axis.png`, `08-b`
8. **Right-click `Part 1` → Rename** (menu opens *upward*; Rename is its top item). `09-x-part-context-menu.png`, `09-b`
9. **Front → Sketch**, **Center point rectangle** (`r`): centre **on the vertical axis** (that alone gives symmetry), then a corner. Dimension **14**, **12**, and origin-to-bottom **−2**. `10-x-rectangle-menu.png`, `10-b`
10. ✓, **Extrude** (`shift+e`): pick the region, **switch to New** (defaults to Add), tick **Symmetric**, depth **14**, ✓ then ✓ again. `11-a`, `11-b`
11. Rename to `Socket body`. `12-b`
12. **Boolean** → tabs **Union | Subtract | Intersect** → **Subtract**. Fields: **Tools**, **Targets**, **Offset**, **Keep tools**. `Ball stud` → Tools; **click Targets**, then `Socket body`. `13-x-boolean-subtract.png`, `13-a`
13. Tick **Offset** → reveals **Offset all**, **Faces to offset**, **Offset distance**, **Reapply fillet**. Tick **Offset all** (removes *Faces to offset*), **Offset distance = 0.2**, tick **Keep tools**, ✓. `14-a-select-offset-checked.png`, `14-x-offset-all.png`, `14-a-select-offset-02-keep-tools.png`, `14-b`

**Measuring** (undocumented in the brief): select one edge/face and read the **bottom-right of the graphics area** — an edge gives `Diameter:`, a spherical face `Radius:`, a planar face `Area:`. There is no dialog. Volume needs **Display mass and section properties** (bottom-right icon) → *Parts to measure*. To reach the mouth you must hide the ball **and** right-click any plane → **Hide all planes**, or the Top plane sits between camera and cavity and swallows every click (`17-x-face-selected-full.png` is that failure).

## What did not work

**1. The brief's sketch order silently produces an under-defined sketch.** Drawing the polyline first and dropping the arc onto its free start point does **not** create a point-to-point coincidence — Onshape constrained the arc's endpoint to the stalk *line*, leaving the line's own endpoint free to slide. The profile still shaded grey as a closed region and every line went black; **one blue dot** at the junction was the only sign (`05-b`). Dragging it proved it (`05-x-drag2-during.png`). Selecting the two overlapping points and applying **Coincident** (`i`) made it worse — whole sketch red, **"Sketch could not be solved."** (`06-x-overconstrained-full.png`). The repair that worked: delete the stalk line and redraw it, hovering each endpoint until highlighted. Cheaper: draw the arc first. For a class this is exactly the failure the "fully define every sketch" rule exists to prevent, and the symptom is one no student will spot unaided.

**2. Two parts both landed in Tools.** Clicking **Targets** while the Tools list was growing did not move focus. Remove with the × on the row, *then* click Targets, *then* pick. Deserves its own numbered step.

**3. Extrude defaults to Add, not New**, once a solid exists, with Merge scope preset to the existing part — would have welded socket to ball and left one part.

**4. The green ✓ needs two clicks** after typing in a numeric field (first commits the field, second the feature). Both extrudes.

**5. Renaming a part is not a double-click** (that opens the part context toolbar). Right-click → **Rename**, menu opens upward. **Ctrl+A does not clear the rename box** — first attempt produced `Ball studPart 1`. Use End + Backspace.

**6. Field labels differ from the help page the brief quoted.** The top-level checkbox is **Offset**, not "Offset all"; the three named fields appear only after ticking it, plus an undocumented **Reapply fillet**.

**7. "Hide" applies to the whole selection.** Hiding `Ball stud` while `Socket body` was still selected hid both, blank screen, no error (`22-x-state.png`).

**8. View controls:** right-drag rotates, **middle-drag pans**, `shift`+arrows do nothing, `n` = View normal to. The view menu has *Isometric/Dimetric/Trimetric*, *Zoom to fit*, *Section view…* but **no Top/Bottom/Front** — and "View normal to" on the Front plane gave me the **Back** view (once upside-down), costing several minutes.

**9. Onshape's REST API returned HTTP 429 for the entire session**, from the first call. Every number here is a GUI readout; the intended coordinate cross-check was impossible.

## What the brief never said

- **The base needs its own dimensions** — "three dimensions only" covers ball and stalk; the profile also needs base width, base height, and something to fix stalk length (I used 5 × 10 and origin-to-base-top = 6).
- **Which side of the origin the socket sits on** — the `grip` bug.
- **The revolve axis is a separate required field**; the sketch's closing line is accepted (*Edge of Sketch 1*).
- **Where the mouth is** — on the *underside*, with the ball protruding through it, so hide the ball first.
- **`Keep tools` really is load-bearing** — confirmed; both parts survive and the ball still measures Ø6.000.
- **A negative value in a distance dimension flips geometry across the axis.** Useful, and dangerous in a classroom.
- **Display decimals** — at the default `0.123` you cannot distinguish 4.996 from 4.9961.

## Stretch — relief slits and Circular pattern (done)

Rectangle on the Front plane, 2.2→8 mm from the axis, −2.5→+0.5 mm vertically (starts inside the mouth, finishes past the equator), **Extrude → Remove, Symmetric, 0.8 mm**, then patterned ×4. `24-b`, `25-a-select-slit-remove-08.png`, `25-b`, `27-b-done-four-slits.png`

- **Yes, the axis must be picked explicitly.** **Axis of pattern** opens empty and outlined red; no default. The tool description says "Specify the axis, angle, and number of instances." `26-x-tool-search.png`, `26-a`
- **What it accepts:** *not* the **Origin** point and *not* a plane — clicking each left the field empty (`26-x-axis-try-origin.png`, `26-x-axis-try-plane.png`). Beside the field is a button tooltipped **"Select mate connector (ctrl+m)"**; with that active, clicking the stalk cylinder filled the field with **Mate connector** and the pattern solved (`27-a`). **Caveat:** I pressed that button *before* clicking the cylinder, so I have **not** tested whether a cylindrical face goes straight in without it. Someone should, before this reaches a step file.
- Defaults: type must change from **Part pattern** to **Feature pattern** to pattern a cut; **Instance count** already defaults to **4**, **Angle** to **360 deg**, **Equal spacing** ticked — exactly the ×4 wanted.

Note: this test block has a 3.8 mm wall so the slits are decorative; on the Ø8 limb the wall is 0.8 mm and the sheet-2 Ø12 note is the relevant fix.

## Timing (from screenshot timestamps — agent pace, a floor not an estimate)

| Milestone | Clock | Elapsed |
| --------- | ----- | ------- |
| Document created, units mm | 09:12 | 6 min |
| Sketch 1 fully defined (incl. ~18 min on the loose-point bug) | 09:34 | 28 min |
| Revolve done, `Ball stud` named | 09:38 | 32 min |
| Socket sketch + symmetric extrude, named | 09:48 | 42 min |
| **Boolean → Subtract with Offset committed** | 09:53 | 47 min |
| Mouth and cavity measured | 09:58 | 52 min |
| Volumes measured | 10:04 | 58 min |
| `grip` bug found, fixed, re-measured | 10:08 | 62 min |
| Stretch complete | 10:33 | 87 min |

Core build to the Boolean: **47 min**, ~18 of it the sketch bug; a clean run of the path above is ~30 min at agent pace. **A student is not this fast.**

## Not done (fail loud)

- **The steps have not been reproduced from an empty document.** This is a transcript of what worked, not a validated step file — the Quality Gate is not met.
- Untested: whether a cylindrical face is accepted directly as a pattern axis without the mate-connector button.
- The API coordinate cross-check was blocked by HTTP 429 throughout.
