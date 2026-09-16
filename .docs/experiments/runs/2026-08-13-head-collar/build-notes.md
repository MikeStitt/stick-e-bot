# Head: the neck socket rebuilt as the standard collar

Run of 2026-08-13/14. The head's neck socket was a cavity bored into a Ø12 boss with no relief
slits. It is now the same Ø9.4 collar standing 5.5 proud with four 0.8 slits that every other
socketed part carries. Done by hand in the Onshape GUI on port 9223; the API was used only to
read geometry and to list versions.

## Where the work is

| | Head | Lesson assembly |
| - | ---- | --------------- |
| document | `head-run5` | `lesson-run5` |
| document id | `92cbe5356b68e79b1fa2de82` | `a999c3039f292ccb278ac94a` |
| element id | `374227cc36f4d555dbc4cfca` (Part Studio 1) | `f09a5c881ece9a882e0f6b39` (Assembly 1) |
| version | `run 5.1` | `run 5.1 assembled` |
| version id | `399f05f6c0b0d7ec577fe4d0` | `e2a99fa2be54ceaaf31c29d5` |

- Head, version `run 5.1` (cite this):
  <https://cad.onshape.com/documents/92cbe5356b68e79b1fa2de82/v/399f05f6c0b0d7ec577fe4d0/e/374227cc36f4d555dbc4cfca>
- Head, live workspace (moves under you):
  <https://cad.onshape.com/documents/92cbe5356b68e79b1fa2de82/w/9fa868aa94c34eae6d48455b/e/374227cc36f4d555dbc4cfca>
- Lesson assembly, version `run 5.1 assembled` (cite this):
  <https://cad.onshape.com/documents/a999c3039f292ccb278ac94a/v/e2a99fa2be54ceaaf31c29d5/e/f09a5c881ece9a882e0f6b39>
- Lesson assembly, live workspace (moves under you):
  <https://cad.onshape.com/documents/a999c3039f292ccb278ac94a/w/1110d41029a137a8e1b6cb79/e/f09a5c881ece9a882e0f6b39>

Both version links were opened in the browser, not just assembled from ids. The head version link
loaded `head-run5 | Part Studio 1` with the banner *Versions are view only*; the lesson version
link loaded `lesson-run5 | Assembly 1` showing `run 5.1 assembled`
(`224-b-done-the-lesson-run-5-1-assembled-version-link.png`). Both live workspaces were driven
directly all evening.

Ids are also written into
[`../2026-08-13-run5/run5-documents.json`](../2026-08-13-run5/run5-documents.json), under each
document's `versions` map.

## The click path that worked

Every frame is in [`shots/`](shots/), numbered in the order things happened, with a matching line
in `shots/steps.log`.

### Turning the boss into a collar

1. Open `Boss circle`, delete the Ø12 circle, draw the collar circle, accept — `09-b-done-the-green-check-to-accept-the-boss-circle-sketch.png`.
2. Open `Neck recess`, switch the **New/Add/Remove** row to **Add**, clear the region field with
   its **x**, click *into* the field, then pick the disc — `16-a-select-the-disc-inside-the-collar-circle.png`.
   A pick made while the field is not focused lands nowhere.
3. Depth 5.5, then flip with the **arrow beside `Blind`** (tooltip *Opposite direction*), not the
   `Direction` checkbox — `29-b-done-the-flip-arrow-beside-blind-to-send-the-collar-o.png`.
4. Accept — `30-b-done-the-green-check-to-accept-the-collar-extrude-fli.png`.

### Fixing what the change broke

5. `Ball profile` lost an external reference: a horizontal 3.35 dimension that had measured to the
   vanished Ø12 boss wall. Select it, **Delete** — `69-b-done-delete-the-broken-3-35-dimension.png`.
6. Re-anchor the ball: **Search tools** (`alt/⌥ c`) → *Dimension*, pick the sketch origin, pick the
   arc's center point, place, type 22.15 — `76-b-done-commit-the-origin-to-ball-center-dimension-at-22.png`.
7. `Boss rim chamfer` deleted. It had re-landed on the collar root as a cone face, and no other
   socketed part has a cone face anywhere. Reached through the tree's **Filter by name or type**
   box, because the row was under the `Parts (n)` panel.
8. Rename `Boss circle` → `Collar circle`, `Neck recess` → `Neck collar` — the old names had become
   lies. Right-click → **Clear selection** first, or the context menu is the multi-select one and
   has no **Rename**.
9. Move the `Neck socket` mate connector's Z to −22.15, the new socket center —
   `88-b-done-the-green-check-to-accept-the-neck-socket-mate-c.png`.

### The four slits

10. **Click the view cube's `Bottom` face** for a true orthographic bottom view —
    `92-b-done-the-view-cube-at-1509-194.png`. Then wheel-zoom onto the collar rim.
11. Select the collar rim face, click **Sketch** — `95-b-done-the-sketch-button.png`.
12. **Search tools** → *Center point rectangle*, center on the sketch origin, corner well clear of
    the sketch axis. A corner within about 10 px of an axis snaps onto it and the rectangle comes
    out zero-width.
13. Dimension it 0.8 × 12 by **single-edge length** dimensions, reading the measured value back
    before typing over it — `dim1.py`, frames 148 onward.
14. Accept the sketch — `171-b-done-the-green-check-to-accept-the-slit-sketch.png`.
15. Select the sketch row, **Search tools** → *Extrude*, **Remove** tab, Blind **5.5** —
    `177-b-done-commit-the-slit-cut-depth-at-5-5.png`. Accept: that is two opposed slits, and the
    collar rim is already two arcs — `178-b-done-the-green-check-to-accept-the-first-pair-of-slit.png`.
16. Select the extrude row, **Search tools** → *Circular pattern*. Change the type dropdown from
    **Part pattern** to **Feature pattern** — `184-b-done-feature-pattern-in-the-type-dropdown.png`.
17. `Features to pattern` = the extrude. Then **click the `Axis of pattern` field** before picking
    the `Neck socket` mate connector, or the mate connector joins the features list instead —
    `189-b-done-the-neck-socket-mate-connector-as-the-pattern-ax.png`.
18. Angle **90 deg**, Instance count **2**, and tick **Reapply features** —
    `196-b-done-the-reapply-features-box.png`. Accept: four slits, no errored rows.
19. Rename `Sketch 1` → `Slit profile`, `Extrude 1` → `Neck slit`, `Circular pattern 1` →
    `Four slits`.

### Publishing and re-assembling

20. **Create version…** is the top icon of the left rail, at (20, 95) — hover it to confirm, the
    icons carry no `title` attribute. Name `run 5.1`, **Create** —
    `209-b-done-create-to-publish-the-version-run-5-1.png`.
21. In `lesson-run5`'s Assembly 1, right-click `Head <1>` → **Update linked document…**, which
    opens the **Reference manager** offering *head-run5, run 5 ➞ run 5.1*. **Update all** —
    `218-b-done-update-all-to-take-the-head-to-run-5-1.png`.
22. Create version `run 5.1 assembled` on the lesson document.

## Acceptance measurements

Measured with `parts` → `boundingboxes` → `bodydetails`; the full face dump is
[`bd-head-slits.json`](bd-head-slits.json). `bodydetails` gives every face its surface type,
radius, origin and area, and it answers while `features` is still returning 429.

| Check | Expected | Measured | How |
| ----- | -------- | -------- | --- |
| one part at the end | Parts (1) | one body, `-all-`, volume 5968.068 mm³ | massproperties |
| whole part height | 41.500, −23.500 to +18.000 | `lowZ −23.5`, `highZ +18.0` | part bounding box |
| collar diameter | Ø9.400 | `CYLINDER r=4.700` at `[0, 0, −23.5]` | bodydetails |
| rim is four arcs, not a circle | 4 | the r4.700 cylinder is reported as **four separate faces** | bodydetails |
| collar proud, and slits its whole length | 5.500 | 4 × 36.2 = 144.8 mm² of collar OD | area arithmetic, below |
| cavity | r3.200 at z −22.15 | `SPHERE r=3.200` at `[0, 0, −22.15]`, in four faces | bodydetails |
| mouth | Ø5.803 | √(3.2² − 1.35²) = 2.9015, and the rim sits at −22.15 − 1.35 = −23.5 | arithmetic on the two measured numbers |
| top of head on the figure | +69.15 | `highZ 0.06915 m` | assembly bounding box |

**The collar-length check is the area arithmetic**, and it is worth writing out because it settles
two of the acceptance checks at once. An unslit collar's outside wall would be
2π × 4.7 × 5.5 = 162.42 mm². Four slits 0.8 wide, cut for the collar's whole length, take
4 × 0.8 × 5.5 = 17.6 mm² off it, leaving 144.82. The four faces measure 4 × 36.2 = 144.8. So the
collar OD is 5.5 tall and the slits run all of it — a shallower cut would leave more wall than
that, and there is none.

The cavity sphere and the shell dome are each reported in four faces too, which is the *four arcs*
check applied one surface further in: the slits reach past the mouth radius, so the mouth can open.

### The rest of the brief's checks, taken on a second pass

**Shell thickness.** A shell offsets each face inward by its thickness, so every shelled surface
leaves a concentric pair in `bodydetails` and the gap between them *is* the wall. Four pairs, all
1.200:

| Where | Outer | Inner | Wall |
| ----- | ----- | ----- | ---- |
| head's top arc | `CYLINDER r=18.000` at `[0, −15, 0]` | `CYLINDER r=16.800`, same origin | 1.200 |
| socket dome | `SPHERE r=4.400` at `[0, 0, −22.15]` | `SPHERE r=3.200`, same origin | 1.200 |
| outline rounds | `CYLINDER r=3.000` at `[±15, ±12, …]` | `CYLINDER r=1.800`, same origin | 1.200 |
| beside the mouth | `CYLINDER r=3.200` at `[±8, −13.5, −6]` | `CYLINDER r=2.000`, same origin | 1.200 |

That last pair is the brief's *one of them next to a cut*: r2.000 is a rounded end of the mouth
slot and r3.200 is the head's inner surface around it. The mouth is 20 × 4, so its ends are r2.0
arcs centered at x ±8, z −6 — the eyes are ellipses and leave no cylinder to pair at all.

**Which way up the socket is.** The cavity `SPHERE r=3.200` sits at z −22.15 and the part's `lowZ`
— the rim plane — is −23.5, so **the cavity center is 1.350 above the rim**. Built the wrong way
up it would be 1.350 below. This replaces the brief's cavity-volume check, which the slits have
made unmeasurable: 109.48 and 27.776 are still the two pieces the rim plane cuts a r3.2 sphere
into, but the void is no longer enclosed, so nothing can weigh it. The brief now carries the
sign check instead.

**Tangency.** First taken as a look at `shots/head-slits-front.png` and `head-slits-isometric.png`
— the silhouette runs from the vertical side into the top arc with no crease — and recorded here as
a look rather than a proof, because a render only shows that no crease is *visible*. It is a proof
now. Two faces meeting tangentially share a normal along their common edge, so `tools/measure_tangency.py` takes
every pair that shares an `edgeId`, finds the vertices they have in common, and compares the facet
normals on either side. Of 166 adjacent pairs, 42 come out tangent and **every junction in the
outline is one of them**: the top arc into both side planes, the arc into both edge rounds, the edge
rounds into all four corner rounds and into the front and back faces, and the corner rounds into the
sides. All read 0.57° or 0.69°, inside the 1.15° the tessellation's own facet normals can be off by.

The numbers behind it are exact, and each is distance-equals-radius:

| Junction | Arc | Line it meets |
| -------- | --- | ------------- |
| top arc into the sides | `CYLINDER r=18.000`, axis at x 0 | planes at x ±18.000 |
| corner rounds into the sides | `CYLINDER r=3.000` at x ±15 | planes at x ±18.000 |
| corner rounds into front and back | same, at y ±12 | planes at y ±15.000 |
| edge rounds into the top arc | `TORUS` major 15.000 minor 3.000 | 15 + 3 = the arc's 18.000 |
| edge rounds into front and back | same, at y ±12 | 12 + 3 = the faces' 15.000 |

The other 124 pairs are creased, and every crease that touches an outline face is at the head's flat
underside at z −18 or at the shell's open rim. Both are meant to be sharp. The rest are the socket,
the slits at 90.00°, the eye bosses meeting the front face at 90.00°, and the mouth.

**Thinnest wall.** `POST .../featurescript` is returning 429 — the same account-wide bucket as
`/features`, which has refused all evening — so `evDistance` was not available and the search was
done a different way. A shell offsets each face inward, so **every shelled wall leaves a pair of
faces sharing an origin and an axis, and the radius gap between them is the wall exactly**.
`tools/measure_walls.py` takes every such pair out of the face dump. There are nine, and **all nine are 1.2000**:
both rounded ends of the mouth, all four outline rounds, the collar OD against the shelled bore,
the head's top arc, and the socket dome. Nothing thinner. The old 0.400 mm ring is gone with the
boss.

One more wall is exact without being concentric: at z −22.15 the cavity sphere's radius in plane
is 3.200 and the collar OD is 4.700, so **the collar wall at the cavity equator is 1.500** — the
standard's `COLLAR_WALL`.

**The flat walls take the same treatment, with one extra step.** Concentric faces are curved; the
head's flat walls are pairs of parallel planes, and there spacing alone proves nothing — two planes
0.3 apart are a wall if the plastic is between them and a gap if it is not. The dump says which.
Every face carries `orientation` and its surface carries `isOrientedWithFace`; multiply the two into
the surface normal and you get the face's **outward** normal, which by definition points away from
material. A pair is a wall only when the two outward normals oppose *and* point out of the space
between them. `tools/measure_planes.py` applies that test to all 34 planar faces. **The thinnest flat wall is
1.2000** — the front wall, the mouth's floor, the eye cups' front walls — and it is the same 1.2 the
shell gave everything else.

The three closest plane pairs are voids, and both are worth naming because a spacing-only search
reports them as walls:

- **0.800** between two planes 12.079 mm² each with opposed outward normals at x ±0.4 — that is a
  slit, seen edge-on. It is the cut, not a wall.
- **0.300**, three times: under each eye and behind the mouth. The eyes stand 1.5 proud of the front
  face and the mouth is recessed 1.5 into it, but the shell is 1.2, so each feature's own wall stops
  0.3 short of the head's skin. An eye cup's inner floor sits at y −15.3 while the head's outer face
  is at −15.0; the mouth's floor plane is at −13.5 while the shell's interior is at −13.8. Material
  lies on the far side of both planes in each case, so the 0.3 is air, bridged laterally by the
  feature's own side wall. Nothing is 0.3 thick. Nothing prints as a 0.3 gap either — that is
  narrower than the 0.4 nozzle, so the slicer closes it.

**The rest of the part, without featurescript at all.** Both searches above are exact but narrow,
and neither can look at a flat cut face approaching a curved one, or at the head's `SWEEP` and
`TORUS` faces, or at its two `OTHER` faces, which `bodydetails` describes with no geometry
whatsoever — type `OTHER`, and nothing else. `POST .../featurescript` was asked a sixth time and
answered 429 again. It was not needed: **`GET .../tessellatedfaces` answers 200**, and it returns
real triangles for every face including the ones with no description. At a 0.0002 m chord tolerance
the head comes back as 185,582 facets over all 67 faces.

That is the whole closed boundary of the part, which makes two things computable with no CAD
kernel. `tools/measure_gaps.py` puts the vertices through a spatial grid and reports the closest approach between
every pair of faces that do not already share an edge — 239 pairs come within 1.25 mm. `tools/measure_solid.py`
then decides each one the only way that settles it: take the midpoint of the closest approach and
fire rays up and down, and an odd number of crossings means the point is inside the plastic. Wall
or void, decided by the mesh.

**The thinnest wall anywhere in the head is 1.2000 mm.** Every approach closer than that is one of
three things, and none of them is plastic:

- **0.800** — a slit. Marching a line from `[4.683, 0, −18]` into the part finds no solid at all.
- **0.300** — the eye and mouth steps above, air on the far side of both planes.
- **0.000** — faces that touch at a point rather than along an edge, at the head's corners where the
  outline round, the side and the top arc all converge. A boundary point makes the ray test
  meaningless, so these were marched instead: from `[−18, 12, 0]` inward the solid runs **1.200**.

One approach is worth naming because it is neither a wall nor a slit. The eye bosses come within
**0.4038** of the head's front edge round, at `[−12.868, −15, 7.308]` — both faces run out at the
same y −15 edge, so that number is the **width of the flat land left between them on the front
surface**, not a thickness. Marching inward from that point gives **1.200** of solid, the ordinary
shell. It is a 0.4 mm wide strip of face, one nozzle across.

`bodydetails`, `tessellatedfaces`, `massproperties`, `boundingboxes` and `shadedviews` all answer
200 throughout; only the two POST endpoints are throttled. The tessellation itself is 101 MB and is
not committed — re-fetch it from
`/api/v10/partstudios/d/{did}/v/{vid}/e/{eid}/tessellatedfaces?angleTolerance=0.02&chordTolerance=0.0002`.

Renders of the part alone: `shots/head-slits-front.png`, `head-slits-bottom.png`,
`head-slits-isometric.png`. The bottom view is the one to look at — four equal collar arcs with
four gaps between them, and the spherical cavity behind. The re-assembled figure:
`shots/lesson-head51-front.png`.

## What did not work

**The Extrude dialog's `Direction` checkbox is not a flip.** It opens an empty custom-direction
reference field. Ticking it with nothing selected fails the feature with *Select Extrude
direction.*, and unticking it left the collar extruding up into the head, which failed as *Boolean
resulted in no geometry change*. The flip is the small arrow beside the `Blind` dropdown, tooltip
*Opposite direction*. Two failed regenerations went to this.

**The feature error text is only in the row's tooltip.** `gui_steps.Steps.errors()` tells you
*which* row is in error; the message needs a hover at the row's left edge and a DOM scrape. The
scrape has to match on **`regenerat`** — the message is *"did not regenerate properly"*, and a
pattern of `error|fail|cannot|could not|unable` matches nothing.

**Two crossed rectangles in one sketch did not solve.** Drawing the second 0.8 × 12 rectangle
across the first picked up constraints against it, and dimensioning its width to 0.8 gave *Sketch
could not be solved*. Deleting the second rectangle and patterning the extrude instead worked
first time. The brief offers crossed slots as the fallback for when the pattern fights you; here
it was the other way round.

**A feature circular pattern needs `Reapply features`.** Without it the pattern failed with *Could
not create all instances as entered*, which is exactly the message that tells you to tick it.

**A pattern's `Axis of pattern` only takes a pick when it has the focus.** Its red border means
*required and empty*, not *focused*; the blue-filled box is the focused one. Picking the mate
connector while `Features to pattern` still had focus added the mate connector to the list of
features to pattern.

**The Dimension tool with two parallel-line picks can give a single-line length dimension.** It
reported 12 mm for what should have been a 4.4 mm gap; setting that to 0.8 drove the wrong entity
and broke the sketch. Two undos, then a single-edge length dimension, which measured 4.43761 and
took 0.8 cleanly. Always read the value back before typing over it.

**Clicking empty canvas does not clear a selection** — it selected the head's face instead. Use
Escape, twice.

**Tree rows below `Head shell` are unclickable** even though their DOM rects say otherwise: the
`Parts (n)` panel is over them and the click lands on the Parts header. The tree's **Filter by name
or type** box reaches them.

**`POST .../versions` returned 401, and I drew the wrong conclusion from it.** I wrote here that
versions have to be created through the GUI. They do not. The 401 was my own bug: this run's
throwaway `hc.py` pulled the XSRF token out of the cookie with `cookie.split('=')[1]`, and the
token is base64 ending in `==`, so the split handed back a truncated token — which Onshape refuses
exactly as it refuses no token at all. `X-XSRF-TOKEN` set from a regex match gets straight past
auth. Run 3's ball-and-socket notes had already found this; `tools/onshape_session.py` and
`onshape-api.md` both do it correctly, and I wrote a fresh helper instead of using either.
The GUI route is still the one this run used, and the frames above are still the click path.

**`GET partstudios/.../features` is still 429.** Re-tested this run. Every diagnosis went through
the GUI and `bodydetails`.

## What the brief never said

- **How to make the four slits as features.** The brief gives the geometry — 0.8 wide, the collar's
  whole 5.5, inner end inside the mouth radius — but not that one 0.8 × 12 rectangle drawn straight
  through the axis gives two of them at once, so the pattern only needs two instances over 90°.
- **That the collar has no chamfer.** The head had a `Boss rim chamfer` on the old boss. Nothing
  says whether the standard collar keeps one; the evidence that it does not is that no other
  socketed part has a cone face anywhere in its `bodydetails`.
- **That the head's mate connector has to move.** The socket center moved from −16.65 to −22.15,
  and the mate connector does not follow the geometry.
- **That the lesson assembly pins the head to a version.** It does, so the change is invisible
  there until the reference is updated. Nothing in the brief says who updates it.
- **That deleting the Ø12 boss orphans a dimension in a later sketch.** `Ball profile` measured to
  the boss wall, so it broke as soon as the wall went.

## Retrospective

**What went well.** Measuring rather than looking. The collar-length check came out of face-area
arithmetic on `bodydetails`, not out of a dimension I placed in the GUI and could have misread —
and the same dump proved the four arcs, which is the check run 1 failed. Driving every click
through `gui_steps.Steps` also paid for itself: this write-up is assembled from `steps.log` and
numbered frames rather than from memory, and the two dimension mistakes are in the record with
their measured values, so I could see immediately that 12 mm was the wrong magnitude.

**What went poorly.** I set a dimension without checking the number I was overwriting, and broke
the sketch. `dim1.py` grew a `-` mode that measures without setting only after that. I also spent
two failed extrudes on the `Direction` checkbox because I assumed what it did from its name
instead of hovering it. And I chased the crossed-rectangle sketch further than it deserved; the
pattern route was one feature and no fighting. Worst of the three: I wrote a fresh two-line XSRF
helper rather than importing `tools/onshape_session.py`, reproduced a bug run 3 had already found
and written down, and then recorded my own bug in the how-to as a fact about Onshape. A wrong
finding published is worse than a missing one, because the next run believes it.

**What I would change.** In the brief: say that a slit rectangle drawn through the axis makes two
slits, so the pattern is two instances over 90°, and that the pattern needs `Reapply features`.
Both are one line each and would have saved an hour. In the how-to: the `Direction` checkbox and
the *Opposite direction* arrow deserve their own entry, as does the `regenerat` tooltip scrape,
the view-cube **face** click for a true orthographic view, and the `Parts (n)` panel occluding the
tree. In the way I was briefed: nothing. The instruction was one sentence and the standard it
pointed at is fully written down in `ball-and-socket.md`, which is what let this be a measurement
problem rather than a design one.
