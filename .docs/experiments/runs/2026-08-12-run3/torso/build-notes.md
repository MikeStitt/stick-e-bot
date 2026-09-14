# Build notes — the torso, run 3

Built from [`../../../build-briefs/torso.md`](../../../build-briefs/torso.md), which had never
been gated or built from. Everything below is what happened, not what the brief expected.

## Where the work is

| | |
| --- | --- |
| Document name | `torso-run3` (created by this run; no document of that name existed) |
| Document id | `dfd743765a001160f1f78751` |
| Workspace id | `0935e4f7a86ee713cade9beb` |
| Element id (Part Studio) | `bcddfc5e93ef5562d74c6ef3` |
| Published version | `torso-run3-v1-five-studs-unioned` |
| Version id | `f29c9f2c3b454d8dcb7aa3b5` |
| Version link | https://cad.onshape.com/documents/dfd743765a001160f1f78751/v/f29c9f2c3b454d8dcb7aa3b5/e/bcddfc5e93ef5562d74c6ef3 |
| Workspace link (**live** — it moves) | https://cad.onshape.com/documents/dfd743765a001160f1f78751/w/0935e4f7a86ee713cade9beb/e/bcddfc5e93ef5562d74c6ef3 |

**I did not open either link in a browser.** Both are assembled from the ids above. What I did
instead: I read the *version* through the read-only REST API under the `v/f29c9f2c3b454d8dcb7aa3b5`
scope and compared it, field by field, against the same reads on the workspace. They agree
exactly — parts `1 ['Torso']`, bounding box x[−26, 26] y[−12, 12] z[−32, 32], volume
42115.10511 mm³, periphery 8107.5885 mm². So the version link points at the geometry described
in this report, even though I never rendered the page.

Page stamp used for the whole run: `TORSO_RUN3_OA4SRWBU`. Census before stamping found no page
carrying it; census after stamping found exactly one.

Wall clock from `steps.log`: 00:16:45 → 04:22:54, of which 00:57 → 03:34 was a dead stall (an
API spend limit, then an Onshape edit-session timeout). Hands-on is about 90 minutes.

## What is in the document

Eleven features, one part.

| # | Feature | Type | Key parameters (read from `/features`) |
| - | ------- | ---- | -------------------------------------- |
| 1 | `Torso footprint` | newSketch | 36 × 24 centred rectangle on Top |
| 2 | `Torso block` | extrude | `operationType: NEW`, `symmetric: true`, 48 |
| 3 | `Shoulder stud profile` | newSketch | on Front |
| 4 | `Shoulder stud right` | revolve | `operationType: NEW` |
| 5 | `Shoulder stud left` | mirror | `patternType: PART`, `operationType: NEW` |
| 6 | `Hip stud profile` | newSketch | on Front |
| 7 | `Hip stud right` | revolve | `operationType: NEW` |
| 8 | `Hip stud left` | mirror | `patternType: PART`, `operationType: NEW` |
| 9 | `Neck stud profile` | newSketch | on Front |
| 10 | `Neck stud` | revolve | `operationType: NEW` |
| 11 | `Fuse studs to torso` | booleanBodies | `operationType: UNION` |

Part list: `Torso` (1).

## The click path that actually worked

Coordinates below are screen pixels in a 1456 × 916 viewport and are only useful as a hint —
they were recalibrated from a screenshot after every zoom.

### Document and units

1. Documents page → **Create** → **Document…**, name `torso-run3`, **Create**.
   `00-x-documents-page.png`, `01-a-select-create-menu.png`, `02-b-done-name-typed.png`,
   `03-b-done-document-created.png`
2. Document hamburger (155, 20) → **Workspace units**. Length default unit **Millimeter**,
   display decimals `0.12345`. Green tick.
   `04-b-done-workspace-units-dialog.png`, `05-a-select-units-millimeter.png`, `05-b-done-units-set.png`
   New documents come up in **inches**. Set this first or every dimension you type is wrong.

### The torso block (brief step 1)

3. **Sketch** (155, 58); the plane field comes up empty, so click **Top** in the feature tree to
   fill it; press `n` to look normal at it.
   `06-a-select-top-plane.png`, `06-b-done-sketch-on-top.png`
4. Rectangle flyout caret (278, 58) → **Center point rectangle**, drawn from the origin outward.
   `07-x-rectangle-flyout.png`, `07-b-done-rect-drawn.png`
5. Dimension the bottom edge **36** (X, width) and the left edge **24** (Y, depth).
   `08-a-select-dim-width-36-box.png`, `11-x-rect-fully-dimensioned.png`
   **I dimensioned it and used Center point rectangle.** The brief asks which; the answer is
   both — the centre-point tool supplies the centring (two `Symmetric`-equivalent constraints to
   the sketch axes) and the two dimensions supply the size. Nothing about the torso is
   `Symmetric`-checkbox driven except the extrude.
6. Green tick to accept `Sketch 1`. `12-b-done-sketch-accepted.png`
7. Select the sketch region on the canvas, open **Extrude**, tick **Symmetric**, depth **48**,
   leave it on **New**, accept.
   `13-a-select-sketch-region.png`, `14-a-select-symmetric-ticked.png`, `14-a-select-depth-48.png`,
   `14-b-done-extrude-accepted.png`
   Bounding box straight afterwards, read from `/boundingboxes`:
   **x[−18, 18] y[−12, 12] z[−24, 24]** = 36.000 × 24.000 × 48.000.

### Fillets (brief step 2)

Skipped, and that is the answer, not an omission. The brief says "fillet the vertical edges **if
the sheets show them rounded**". The parts sheet draws the torso with square corners, so there is
no fillet to apply. The block's volume proves none was applied: 36 × 24 × 48 = 41472 mm³ exactly,
and the model reported 41472.0000.

### One shoulder stud (brief step 3)

8. **Sketch** on **Front**, `n`, then wheel-zoom onto the torso's top-right corner.
   `15-b-done-sketch-on-front.png`, `15-x-zoomed-shoulder-corner.png`
9. Arc flyout (383, 58) → **Center point arc** for the ball; then the **Line** tool chains three
   straight edges — stalk top, root, revolve axis — closing the profile.
   `16-b-done-arc-drawn.png`, `17-b-done-profile-closed.png`
10. **Coincident** (`i`) between the arc centre and the revolve-axis line — this is the brief's
    "found by constraint rather than dimensioned" join. `18-b-done-coincident.png`
11. Dimensions: arc radius **3**; stalk half-width **1.5**; root corner to the Z axis **18**;
    root corner to the X axis **24**; stand-off root-to-ball-centre **5**.
    `27-x-shoulder-profile-dimensioned.png`
12. **Horizontal** on the revolve-axis line and on the stalk-top line.
    `28-x-show-constraints.png`, `28-b-done-horizontal-revolve-axis.png`
    See "What did not work" — I missed the axis one on the first pass and it cost two hours of
    wrong geometry.
13. Accept the sketch, select the region, open **Revolve**. Remove the stray `Face of Extrude 1`
    Onshape adds to the region list by clicking its chip's ×. Click into the empty red **Revolve
    axis** field, then pick the axis line. **Click New** — the dialog had flipped itself to Add.
    Accept.
    `29-a-select-regions-cleaned.png`, `29-a-select-revolve-axis.png`, `29-a-select-revolve-new.png`,
    `29-b-done-revolve-accepted.png`

### Mirror the part (brief step 4)

14. Select **Part 2** in the Parts list, open **Mirror**, click into the empty red **Mirror
    plane** field, pick **Right** in the feature tree, **click New**, accept.
    `30-b-done-mirror-dialog.png`, `31-a-select-mirror-new.png`, `31-b-done-mirror-accepted.png`

    Mirroring the *part* (not the feature) is what the brief asks for and it works. The dialog's
    `patternType` reads `PART` in `/features`, confirmed.

### Hips and neck (brief step 5)

15. Same shape again on a new Front sketch, dimensioned to the hip station: root corner to Z axis
    **12**, root corner to X axis **24** (the bottom face), stand-off **5**, radius **3**, stalk
    half-width **1.5**, plus **Vertical** on the revolve axis and **Horizontal** on the root line.
    `32-b-done-sketch3-on-front.png`, `33-b-done-hip-profile.png`, `39-x-hip-dims.png`,
    `41-b-done-vertical.png`, `42-b-done-horizontal.png`, `43-b-done-coincident.png`
16. Revolve **New**, then Mirror the part about **Right**, **New**.
    `60-a-select-revolve2-ready.png`, `61-a-select-revolve2-new.png`, `62-b-done-revolve2.png`,
    `65-a-select-mirror2-ready.png`, `66-a-select-mirror2-new.png`, `67-b-done-mirror2.png`
17. Neck: one more Front sketch on the axis, growing up from z = +24. No mirror — it is on the
    plane of symmetry.
    `69-x-neck-view.png`, `70-b-done-neck-profile.png`, `82-x-neck-dims.png`, `87-b-done-standoff.png`,
    `88-b-done-sketch4-final.png`, `89-a-select-revolve3-region.png`, `91-a-select-revolve3-new.png`,
    `92-b-done-revolve3.png`

### Union and naming (brief steps 6–7)

18. Select all six parts in the Parts list, **Boolean** → **Union**, accept.
    `93-a-select-six-parts.png`, `94-a-select-boolean-dialog.png`, `95-b-done-union.png`
19. Rename all eleven features by right-click → **Rename**. Rename the part the same way — but
    **only after clearing every selection**, see below.
    `102-b-done-part-renamed.png`
20. Left rail → versions panel → **Create version…** → name → **Create**.
    `104-a-select-versions-panel.png`, `105-a-select-create-version.png`, `107-b-done-version-created.png`

## Acceptance measurements

Everything in this section was measured, not inferred. Three tools were used, all read-only:

- **REST** `/parts`, `/boundingboxes`, `/partstudios/.../massproperties` — box extents, volume,
  total surface area.
- **FeatureScript** via `POST /featurescript`, querying
  `qOwnedByBody(qBodyType(qEverything(EntityType.BODY), BodyType.SOLID), EntityType.FACE)` and
  calling `evSurfaceDefinition`, `evArea` and `evBox3d` on each face. This gives exact analytic
  radii and centres, not a bounding-box estimate.
- **`shadedviews`** renders, looked at before writing any of this down.

| Check | Expected | Got | How |
| ----- | -------- | --- | --- |
| Parts at the end | 1 | **1**, named `Torso` | `/parts` on both workspace and version |
| Block before studs | 36.000 × 24.000 × 48.000 | **x[−18, 18] y[−12, 12] z[−24, 24]** | `/boundingboxes` right after Extrude 1 |
| Ball 1 (right shoulder) | Ø6.000 | **Ø6.00000** at **(23.00000, 0, 24.00000)** | `evSurfaceDefinition` on the sphere face |
| Ball 2 (left shoulder) | Ø6.000 | **Ø6.00000** at **(−23.00000, 0, 24.00000)** | same |
| Ball 3 (right hip) | Ø6.000 | **Ø6.00000** at **(12.00000, 0, −29.00000)** | same |
| Ball 4 (left hip) | Ø6.000 | **Ø6.00000** at **(−12.00000, 0, −29.00000)** | same |
| Ball 5 (neck) | Ø6.000 | **Ø6.00000** at **(0, 0, 29.00000)** | same |
| Symmetric about YZ | lands on itself | **yes**, two independent ways | below |
| Thinnest section | — | **Ø3.000**, the five stalks | face inventory |

All five balls were measured separately. The five spherical faces each report an area of
**105.5213 mm²**, identically. That is not the 113.0973 mm² of a whole Ø6 sphere; the difference,
7.5761 mm², is exactly the curved area of a cap 0.40192 mm deep — the mouth where the stalk
enters. Same on all five, so all five studs are the same solid.

**Ball centre coordinates as actual numbers**, since the brief asked for measurements rather than
confirmations: shoulders (±23, 0, 24); hips (±12, 0, −29); neck (0, 0, 29). Read the shoulder row
carefully — x = 23, not 18. The stand-off pushes the centre 5 mm off the side face it grows from.
The *station* is x = ±18; the *ball* is at ±23.

### Symmetry about YZ, checked twice

1. **The brief's own check.** A scratch **Mirror**, part = `Torso`, plane = **Right**, kept as
   **Add** with merge scope `Torso`, so a good mirror unions back onto the original and changes
   nothing. Result: part count stayed **1**, volume stayed **42115.10511 mm³** — identical to five
   decimals. It landed on itself. `109-a-select-scratch-mirror.png`, `110-b-done-scratch-mirror.png`
2. **A face multiset check.** All 18 solid faces, each reduced to (area, x-extents, y-extents,
   z-extents), then mirrored x → −x and compared as a multiset. **Identical.**

The mass-properties centroid is *not* usable for this. It reads (0, 0, 0) for every part in the
document because no material is assigned, so mass is zero and the centroid is degenerate. It
would have "passed" on any shape at all.

### Thinnest wall

**There is no wall.** The torso as specified is a solid block, not a shell, so the brief's
"thinnest wall anywhere" has no referent. The nearest honest answer is the thinnest *section*:

- **Ø3.000 mm** — the five stalk necks, each 2.40192 mm of exposed cylinder between the face it
  grows from and the ball it carries. This is the thinnest material in the part and it is where
  it will break.
- Nearest approach between separate features: the two hip balls are **18.000 mm** apart surface to
  surface; a hip ball's surface (x = 15) clears the torso side face (x = 18) by **3.000 mm**; the
  neck ball clears each side face by **15.000 mm**. Nothing is close to touching.

### Face inventory — the whole part in eighteen faces

| Face | Area mm² | Where | What it is |
| ---- | -------- | ----- | ---------- |
| front, back | 1728.0000 each | y = ±12 | 36 × 48 exactly — proof of no fillet |
| sides | 1148.4657 each | x = ±18 | 1152 − 3.5343, i.e. **half** a Ø3 disc removed |
| top | 856.9314 | z = +24 | 864 − 7.0686, one whole neck root |
| bottom | 849.8628 | z = −24 | 864 − 2 × 7.0686, two whole hip roots |
| **two half-discs** | **3.5343 each** | **x = ±18, z[24, 25.5]** | **see below** |
| 5 spheres | 105.5213 each | the balls | Ø6.00000 |
| 5 cylinders | 22.6376 each | the stalks | Ø3.00000, 2.40192 long |

Volume closes in closed form. A stud is (Ø6 sphere) − (0.40192 cap) + (Ø3 × 2.40192 cylinder) =
128.62102 mm³; 41472 + 5 × 128.62102 = **42115.10511 mm³**, which is the measured volume to every
digit reported. Nothing is missing and nothing is double-counted.

## The shoulder stud straddles the top edge

This is the finding of the run, and it falls straight out of the two rows above that do not look
like the others.

The shoulder station is z = +24, which is also the plane of the torso's **top face**. The stud
roots on the **side** face at x = 18. So the stalk's Ø3 root circle is centred exactly on the top
edge where those two faces meet. Its lower half lands on the side face — that is why each side
face is 1152 − 3.5343, half a disc. Its upper half has nothing to land on and hangs off the
corner in mid-air, closed by a bare flat semicircle: the two 3.5343 mm² planar faces at x = ±18,
z[24, 25.5].

Half of each shoulder stud is attached to nothing.

I looked at this in five renders before writing it down: `103-x-render-front.png`,
`103-x-render-right.png`, `103-x-render-top.png`, `103-x-render-isometric.png`,
`103-x-render-trimetric.png`, plus a GUI close-up at `116-x-shoulder-straddle.png`. In the
trimetric view the two shoulder balls sit visibly *above* the top face while the neck ball sits
*on* it — the shoulders are perched on the corner, the neck is planted. The top view shows both
shoulder studs sticking out sideways past the block outline with the stalk crossing the silhouette
edge. The numbers implied this; the pictures confirm it is as bad as it sounds.

It is a print problem (an unsupported overhanging half-cylinder, on a Ø3 feature, at the joint
that carries the arm) and a strength problem. **I did not fix it** — it is a consequence of the
station table, not of anything in the build, and the brief tells me to report rather than resolve.

## The three open questions — reported, not resolved

### 1. The stand-off, built at 5

Built at 5 as instructed, unchanged. Measured consequences at the shoulder:

| | mm |
| --- | --- |
| ball centre from the face it grows from | **5.000** |
| ball surface clear of that face | **2.000** |
| exposed stalk cylinder | **2.40192** |
| total stud protrusion (face to ball far side) | **8.000** |
| ball centre x | **23.000** |

The shoulder is described above: at a stand-off of 5 the stud is a Ø3 stalk sitting on a corner,
half-supported, carrying a Ø6 ball 8 mm out. Increasing the stand-off does not help — it makes the
unsupported stalk longer. Decreasing it to 3 would bury the ball in the face. **The stand-off is
not the variable that fixes this; the shoulder root location is.** I have not adopted the 154 mm
stack and I have not proposed a number. It stays open.

### 2. Boss diameter and protrusion at the shoulder and hip

**No boss was built anywhere, including the neck.** The brief's build order never asks for one —
steps 1–7 go sketch, extrude, fillet, one stud, mirror, repeat, union — and the numbers table
lists Ø12 only as a proposal for the neck. So the studs grow directly out of flat faces.

That leaves the question exactly where the brief left it: diameter open, protrusion open, and
whether a hip boss moves the knee and ankle stations untested. What this run *can* add is that at
the shoulder a boss is not cosmetic — it is the obvious candidate for giving that half-floating
stalk something to root into, and its diameter and protrusion would have to be chosen with the
straddle in mind rather than to match the neck's drawn Ø12. Somebody should decide that
deliberately.

### 3. Does the shoulder stud line up with the arm?

**No. The gap is 4.000 mm.**

The arm centreline is `#armX` = 27. The shoulder ball centre, measured on the model, is
x = **23.00000** — the side face at 18 plus the stand-off of 5. 27 − 23 = **4.000 mm**.

I have not picked a value to close it. Three ways it could close, all of them somebody else's
decision: move the arm in to 23, raise the stand-off to 9 (which lengthens the unsupported stalk —
see above), or put a boss on the side face that carries the root outward. The gap is reported as
found.

## What did not work

### The brief

- **"Thinnest wall anywhere in the part"** has no answer for a solid block. There is no wall.
  Either the brief means "thinnest section", or the torso was at some point meant to be shelled
  and nothing says so.
- **The fillet step is conditional on a sheet** that shows square corners, so step 2 is a no-op.
  That is fine, but it reads like a step and it is not one.
- **Nothing in the build order produces a boss**, while the numbers table lists a boss diameter.
  A reader following steps 1–7 will finish with no boss and no signal that one was expected.
- The **stand-off is measured from the face, which the brief does not quite say.** "How far a ball
  center stands off the face it grows from" is clear enough, but at the shoulder there are two
  candidate faces meeting at the joint centre, and choosing the side face is what produces the
  straddle. Saying which face, explicitly, would have made the problem visible before modelling.

### The build, in order of cost

- **The revolve axis was never made Horizontal in Sketch 2**, and the sketch was under-defined in
  a way that looked defined. The axis sat tilted by 1.1124°, so the revolve produced studs whose
  bounding boxes were 8.058 long and 6.194 across instead of 8.000 and 6.000. Both numbers are
  fully explained by the tilt: the ball centre ends up 0.09695 mm off the tilted axis, so the swept
  radius is 3.09695 and the box is 6.1939 across; the root disc tilts so its low corner reaches
  x = 17.94191, making the box 8.0582 long. Diagnosed by reading
  `/sketches?includeGeometry=true` and doing the arithmetic, not by eye.
  **One Horizontal constraint between the axis line's two endpoints fixed it** and the sketch went
  fully defined on its own. `47-x-sketch2-edit-zoom.png`, `49-b-done-horizontal.png`,
  `51-x-sketch2-fixed.png`, `53-b-done-sketch2-accepted.png`
  A second Horizontal (root corner to ball centre) made the sketch unsolvable and had to be undone
  — over-constraining is one click away from under-constraining. `52-x-sketch2-after-undo.png`
- **Revolve and Mirror silently flip New → Add.** Every one of the three Revolves and both Mirrors
  came up on **Add** with the merge scope pre-filled to Part 1, despite New being the last thing I
  chose. Caught all five times by reading the dialog's own text back before accepting; missed once
  (Mirror 1) and had to delete and redo the feature. Screenshots
  `29-a-select-revolve-new.png`, `31-a-select-mirror-new.png`, `61-a-select-revolve2-new.png`,
  `66-a-select-mirror2-new.png`, `91-a-select-revolve3-new.png` are each the moment New was
  restored. **This is the single most dangerous behaviour in this whole build**, because the
  brief's entire lesson is New-versus-Add and the dialog quietly votes the other way.
- **Revolve auto-adds a stray face to its region list.** Both the shoulder and neck revolves
  arrived with `Face of Extrude 1` already in "Faces and sketch regions to revolve", picked up
  from a canvas selection I could not see. Removed by clicking the chip's ×.
  `29-a-select-regions-cleaned.png`
- **Delete acts on a stale canvas selection you cannot see in the tree.** Twice: deleting
  `Mirror 1` took `Extrude 1` with it (`30-x-mirror1-deleted.png`, `30-x-after-undo-delete.png`),
  and at the very end deleting the scratch mirror took `Torso block` with it — features went 11 →
  10 and parts 1 → 5. One `Control+z` each time. The cause, confirmed from a screenshot: the
  torso's front face (1728 mm²) had been silently selected the entire time. Clicking bare canvas
  *outside the default-plane rectangles* is what clears it — clicking inside a plane selects the
  plane. `113-x-after-undo3.png`, `115-x-selection-cleared.png`
- **Renaming the part took five attempts.** Double-click, slow double-click, double-click on the
  text node, all failed. The how-to already says it: **Rename disappears from the context menu
  whenever more than one thing is selected**, and something was always selected. Clear everything
  first and Rename appears. `96-x-rename-failed-695.png` … `101-x-partrename-failed.png`,
  `102-b-done-part-renamed.png`
- **Dimensioning between two entities that both lie on a sketch axis does not work.** The neck
  stand-off is root corner → ball centre, and both are on the Z axis; the Dimension tool produced
  no input box at all. Two attempts at a fallback pair pre-filled 1.5 mm, and setting *that* to 5
  deformed the sketch (two `Control+z`). The fix: pick the **stalk** corner instead, which is
  1.5 mm off-axis, and place the label to the right so Onshape resolves it as a *vertical*
  distance. After that I gated the script on the pre-filled value and made it escape rather than
  commit if the wrong pair had been picked. `73-x-dim-failed.png`, `83-x-undo1.png`,
  `86-x-neck-closeup.png`, `87-b-done-standoff.png`
- **Canvas picks silently do not register** in a dialog's selection field with a plain click, even
  when the geometry highlights orange. `mouse.click()` on a region left both Revolve fields empty.
  What works: click the dialog's selection field first, then `mouse.move` → wait →
  `mouse.down()` → wait 150 ms → `mouse.up()` → wait ~1.8 s.
- **The Onshape edit session timed out** during the 2.5-hour stall ("Your Onshape session has
  timed out. Your document is saved."), while REST `sessioninfo` still returned 200 with roles —
  so the API check does **not** detect this state. Recovered by clicking "Click here to
  reconnect", waiting 15 s, re-stamping `window.name` (a reload clears it) and re-asserting
  exactly one match. `44-x-resume-state.png`, `45-x-after-reconnect.png`
- **The view zoomed itself out** during the failed neck dimension. Cause not established. Handled
  by recalibrating screen-to-mm from a fresh screenshot before every subsequent pick.
- `/features` returned **429 Too many requests** twice under polling. Backed off 12–45 s inside
  Python and retried.

## What the brief never said

- **Set the units first.** A new Onshape document is in inches.
- **Which face the shoulder stud roots on**, when the joint centre lies on the edge between two.
  This is not a detail; it is the whole straddle.
- **Whether the neck gets a boss.** The numbers table implies the neck's Ø12 is settled; the build
  order never builds it.
- **How to check symmetry when the part has no material.** The obvious check — compare centroids —
  silently passes on anything, because an unassigned material makes every centroid (0, 0, 0).
- **That the scratch mirror must be Add with the original in its merge scope.** As a New mirror it
  creates a second part and the part count check reads 2, which looks like a failure and is not.
- **How to get the stud profile's revolve axis to actually be an axis.** Drawing a line and
  choosing it as the revolve axis is not enough — nothing makes it horizontal, and a 1° tilt
  produces a part that looks right, passes a glance, and is wrong by 0.19 mm.
- **What "Parts (1)" is really testing.** The brief says a stray part means a Boolean that touched
  nothing. True, but the count is also the only thing standing between you and five studs that
  each silently merged into the torso as they were made, which destroys the lesson without
  changing the final geometry. Reading `operationType` out of `/features` is the check that
  actually distinguishes those.

## Retrospective

### What went well

The brief's central idea is correct and it survived contact. **New, mirror the part, one Union at
the end** produced exactly one part with all five studs, both mirrors landed, and the final
Boolean consumed six parts into one. The `Parts (1)` check did its job. Neither of the two failure
modes the brief warned about occurred — no instance failed quietly, and nothing auto-merged with
its seed — but I only know that because the count was taken.

Reading geometry through FeatureScript rather than bounding boxes is what made this report worth
anything. `evSurfaceDefinition` on a sphere gives the analytic radius and centre; a bounding box
gives you a number that is right for the wrong reason, which is precisely how the tilted-axis bug
survived its first inspection. The face inventory then explained the entire part in closed form —
volume matching to five decimals means nothing is unaccounted for.

And the failure that matters was found by *looking*. The straddle is visible in the renders, and
the two 3.5343 mm² faces are the same fact in the face table. Numbers and pictures agreeing is the
only reason I am confident enough to state it flatly.

### What went poorly

I accepted Sketch 2 while it was under-defined and did not notice for two hours of elapsed time.
The sketch was blue-ish rather than black and I talked myself past it. The cost was two studs
built wrong and a full re-open-and-fix cycle. **An under-defined sketch is a defect, not a style
choice**, and the check is free: if it is not fully defined, do not accept it.

I let a canvas selection persist across features and it bit twice, both times destructively. Both
recoveries were one `Control+z`, which made it feel cheap; it was not — the second one deleted the
torso block one action after publishing a version, and if I had not been reading the feature count
back after every destructive action I would have written this report against a broken model.

I also trusted `New` after clicking it, five times, and was wrong five times. Reading the dialog
back is not paranoia here, it is the only reliable state.

### What I would change

**About the brief.** Add the station-versus-root distinction to the geometry section — say which
face each stud roots on, and say what happens when the station lies on an edge. That one sentence
would have surfaced the straddle at reading time instead of at render time. Replace "thinnest wall"
with "thinnest section" or say the part is meant to be shelled. Either drop the boss from the
numbers table or add a build step for it, because a proposal with no step is a number that will
get quietly adopted by whoever reads the table and not the steps.

**About the how-to.** It should carry a standing warning that **Revolve and Mirror flip New to Add
between dialogs** — the how-to documents this for Extrude, and I hit it five times on the other
two tools. It should also say that a stale canvas selection makes Delete destructive in ways the
feature tree does not show, and that clicking "empty" canvas inside a default plane's rectangle
selects the plane rather than clearing.

**About the way I was briefed.** The instruction to report rather than resolve the three open
questions was exactly right and I would keep it. Being told which numbers were `proposed` and
never checked changed how I worked: I built to 5, measured, and reported the shoulder instead of
tuning it until it looked good. The one thing I would add is an explicit instruction to verify the
model is intact immediately before writing the report — I did it out of habit after the accidental
delete, and it is the only reason this report describes the part that is actually in the document.
