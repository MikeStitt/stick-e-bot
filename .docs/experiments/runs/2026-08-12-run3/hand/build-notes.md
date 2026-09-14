# Run 3 — the hand

Built from [`../../../build-briefs/hand.md`](../../../build-briefs/hand.md), which had never been
built from before tonight. Everything below was measured on the model or read off the screen.
Where I could not check something I say so.

## Where the work is

| | |
| --- | --- |
| Document name | `hand-run3` |
| Document id | `1bb0da3ec390097ada708b8c` |
| Element id (Part Studio 1) | `8bcb46f7c9535c9d0daf19df` |
| Workspace id | `496593f76caf867c13606b66` |
| Version (final) | `hand-run3-v2`, id `2f5fcbb9c62198049febf318` |
| Version (recovery, before the relief slits) | `hand-run3-v1`, id `a41a7b94671210b304484ab0` |

- Version link (cite this): <https://cad.onshape.com/documents/1bb0da3ec390097ada708b8c/v/2f5fcbb9c62198049febf318/e/8bcb46f7c9535c9d0daf19df>
- Recovery version: <https://cad.onshape.com/documents/1bb0da3ec390097ada708b8c/v/a41a7b94671210b304484ab0/e/8bcb46f7c9535c9d0daf19df>
- **Live workspace — a moving target, do not cite it:** <https://cad.onshape.com/documents/1bb0da3ec390097ada708b8c/w/496593f76caf867c13606b66/e/8bcb46f7c9535c9d0daf19df>

**I opened both links, I did not only assemble them from ids.** The v2 version link loads read-only
with the banner "Versions are view only. Viewing hand-run3-v2", 10 features and `Parts (1) Hand`
(`64-x-version2-link-open.png`); the workspace link loads live and measures the same solid
(`64-x-workspace-link-open.png`). The v1 link was opened the same way earlier
(`46-x-version-link-open.png`).

Final feature tree, all renamed:
`Clip profile`, `Clip`, `Collar profile`, `Socket collar`, `Wrist ball profile`, `Wrist ball`,
`Wrist socket`, `Slit profile`, `Relief slit`, `Relief slits x4`. One part: `Hand`.

## The click path that actually worked

Coordinates are for a 1600 × 1000 viewport. Toolbar and dialog positions are stable across a
session; they are **not** stable across a page reload, and the graphics-area ones are not stable
across a zoom.

1. **New document.** Documents page → `Create` → the menu item by coordinate at
   (`Create` button x + 30, y + height + 18); typed `hand-run3`.
   `01-a-select-documents-page.png`, `02-a-select-create-menu.png`,
   `02-b-done-new-document-dialog.png`, `03-b-done-document-created.png`
2. **Units.** ☰ document menu (155, 20) → `Workspace units…`. The menu item would not take a
   Playwright `.click()` ("not visible") — clicking its bounding-box centre at (252, 236) worked.
   Length `Millimeter`, display `0.12345`.
   `04-b-done-workspace-units-dialog.png`, `05-b-done-units-set.png`
3. **Clip profile sketch — on the `Right` plane, not `Front`.** `Sketch` button (155, 58) first,
   *then* the plane row in the tree. See "What did not work" #1 for why `Right`.
   `06-b-done-sketch-on-right.png`
4. **View normal to the sketch.** Clicking empty canvas first selects the *Front plane*, and `n`
   then orients to that, not to the sketch. Fix: right-click a plane → `Hide all planes`, `Escape`,
   then `n`. The view cube then read `Right`.
   `06-x-context-menu.png`, `06-x-view-normal-to-right2.png`
5. **Two circles, one centre.** Outer circle centred on the vertical (Z) axis, inner circle drawn at
   a *separate* centre, then both selected and `shift+o` for **Concentric**. Drawing them
   coincident from the start makes the constraint a no-op you cannot see.
   `07-b-done-two-circles-drawn.png`, `08-b-done-concentric.png`
6. **Dimensions**, `d` each time: outer Ø10, origin→centre 7, bore Ø3.3.
   `09-b-done-dim-outer-10.png`, `10-b-done-dim-centre-7.png`, `11-b-done-dim-bore-3p3.png`
7. **Two mouth lines**, `l`, then centre→upper line 1.3 and line→line 2.6.
   `12-b-done-mouth-lines-drawn2.png`, `13-b-done-dim-mouth-2p6.png`
8. **Trim**, `m` (scissors at (725, 58)). **Six clicks, not two** — see #4 below.
   `14-a-select-trim-armed.png`, `14-b-done-trim-outer-arc.png`, `15-b-done-trim-bore-arc.png`,
   `16-b-done-trim-upper-in.png` … `19-b-done-trim-lower-out2.png`, `19-x-after-all-trims.png`
9. **Extrude the clip.** Region picked at (850, 618) → `Search tools` (1350, 58) → `Extrude`.
   Depth **6**, `Symmetric` (the depth is the TOTAL, so this gives x −3 … +3), operation `New`.
   `21-a-select-clip-region.png`, `22-a-select-extrude-symmetric.png`, `22-b-done-clip-extruded.png`
10. **Rename** sketch → `Clip profile`, extrude → `Clip`, part → `Hand`.
    `23-x-context-menu-extrude2.png`, `23-b-done-renamed4.png`
11. **Collar sketch** on `Top`, one circle on the origin, Ø9.4.
    `24-a-select-sketch-on-top.png`, `25-b-done-collar-circle-9p4.png`
12. **Collar extrude.** Pick the **region interior** at (923, 505), not the circle's curve.
    Depth 1.35; tick `Second end position` and set it 4.15; click `Add` **after** the depths;
    `Merge scope` = `Hand`. Then two direction flips — see #7 and #8.
    `27-a-select-collar-region2.png`, `28-b-done-collar-add-set.png`,
    `30-b-done-collar-flipped.png`, `31-b-done-collar-added.png`
13. **Wrist ball.** There is **no Sphere primitive** (`32-a-select-search-sphere.png`), so:
    sketch on `Front`, part hidden, `Center point arc` from the arc flyout caret (383, 58), closed
    with a line on the vertical axis, radius dimensioned 3, then `Revolve` about that line, `New`.
    `33-b-done-part-hidden.png`, `34-a-select-arc-flyout2.png`, `35-b-done-ball-profile-r3.png`,
    `37-a-select-revolve-axis-and-new.png`, `37-b-done-ball-revolved.png`
14. **Wrist socket.** `Search tools` → `Boolean`. It opens on **Union**; `Subtract` at (348, 121).
    `Tools` = `Wrist ball`, `Targets` = `Hand`, tick `Offset`, tick `Offset all`,
    `Offset distance` **0.2**, `Reapply fillet` and `Keep tools` both left unticked so the ball is
    consumed. Renamed `Wrist socket`.
    `39-a-select-boolean-subtract.png`, `40-b-done-boolean-offset-set.png`, `40-b-done-socket-cut.png`
15. **Slit profile.** Sketch on `Top`. Corner rectangle (254, 58) drawn in clear space, then
    dimensioned in this order: top-edge length 3.5 → origin-to-inner-end 2.5 → X-axis-to-top-edge
    0.4 → right-edge length 0.8. Curves went black.
    `48-b-done-slot-rect-drawn.png` … `52-b-done-slot-fully-defined.png`
16. **Relief slit.** Sketch selected in the tree → `Search tools` → `Extrude`; the dialog opened
    already holding `Faces of Slit profile` and `Merge scope` = `Hand`. Switched to `Remove`,
    Depth 5.5, ticked `Starting offset`, its depth 1.35. No flip needed — it arrived running −Z.
    `54-a-select-slit-startoffset-1p35.png`, `55-b-done-one-slit.png`
17. **Circular pattern ×4.** `Search tools` → `Circular pattern`; opens as **Part pattern**,
    changed to **Feature pattern** in the dropdown at (343, 122). `Features to pattern` =
    `Relief slit`; `Axis of pattern` = the collar's cylindrical face clicked in the graphics area
    (accepted as `Face of Socket collar`); Angle 360°, count 4, `Equal spacing` ticked, **and
    `Reapply features` ticked** — see #9. Renamed `Relief slits x4`.
    `57-a-select-pattern-ready.png`, `59-a-select-reapply-features.png`, `59-b-done-four-slits-cut.png`
18. **Symmetry check** (scratch, deleted afterwards). `Search tools` → `Mirror`,
    `Entities to mirror` = `Hand`, `Mirror plane` = `Right` picked in the tree, operation `Add`,
    `Merge scope` = `Hand`. Run twice: once before the slits, once on the final geometry.
    `60-a-select-mirror2-filled.png`, `61-b-done-mirror2-deleted.png`
19. **Versions.** Left rail (20, 94) `Create version…`.
    `63-a-select-version2-named.png`, `63-b-done-version2-created.png`

## Acceptance measurements

Everything here was read off the built model through read-only REST from inside the Onshape page:
`POST …/featurescript` calling `evBox3d`, `evVolume`, `evArea`, `evSurfaceDefinition` and
`evCurveDefinition`, plus `GET …/parts` and `GET …/features`. Nothing in this table is arithmetic
on the brief. `GET …/boundingboxes` returns **404** on this account, which is why everything goes
through FeatureScript.

| Check | Wanted | Got | How |
| --- | --- | --- | --- |
| Parts | 1 | **1** — `Hand` | `GET /parts` |
| Clip bore | Ø3.300 | cylinder r **1.650**; end circles Ø**3.3** at (±3, 0, −7) | surface + curve definitions |
| Clip outer | Ø10.000 | cylinder r **5.000**; arcs Ø**10** at (±3, 0, −7) | surface + curve definitions |
| Mouth, at its narrowest | 2.600 | **2.600** — two parallel planes, normals ∓Z, at z **−5.700** and z **−8.300**. Parallel-sided, so the narrowest *is* 2.600 everywhere | plane definitions |
| Mouth trimmed evenly on both sides | — | the two mouth faces have areas **22.8715380611055** and **22.8715380611055** — equal to 15 figures | face areas |
| Symmetric about YZ | lands on itself | scratch `Mirror` about `Right`, `Add`, merged into `Hand`: Onshape reported **"Boolean resulted in no geometry change"**, volume **530.4489103248033 → 530.4489103248033**, Parts stayed **1**. Repeated before the slits: **563.5068668039881 → 563.5068668039881** | GUI mirror + volume |
| Socket mouth | Ø5.803 | **four arcs**, each Ø**5.8025856**, centred (0, 0, 1.350) | edge curve definitions |
| Cavity volume | 109.48 mm³ (27.78 = upside down) | **109.4820168834203** = 672.9888836874084 − 563.5068668039881 | volume before and after the Boolean |
| Cavity sphere | r 3.200 | **3.2000**, centred exactly on (0, 0, 0) | face definition |
| Hand length | 12.000, wrist centre → lowest point | **12.000** — cavity sphere centre measured at z 0.000, lowest point at z **−12.000** | sphere centre + body box |
| Thinnest wall anywhere | brief expected 3.35 | **1.500**, at the socket collar = 4.700 (collar cylinder) − 3.200 (cavity sphere). The clip wall is **3.350** = 5.000 − 1.650, exactly as the brief predicted, but it is **not** the thinnest | two measured radii |
| Slits run the collar's full length | −4.150 … +1.350 | **8** slit side walls, every one z **−4.1500 … +1.3500** | face bounding boxes |
| Clip thickness | (brief gives none) | **6.000**, x −3.000 … +3.000 | body box |
| Bounding box | — | **9.366 × 9.828 × 13.350** | body box |
| Volume | — | **530.4489103248033 mm³** | `evVolume` |

Supporting volumes: `Hand` **672.9888836874084** (clip + collar) → **563.5068668039881** (after the
socket cavity) → **555.2423780105592** (one slit, 8.264489 mm³) → **530.4489103248033** (four slits,
33.057957 mm³). Four times one slit, exactly — the slits do not overlap each other. The one-slit
figure **8.264489 mm³** is bit-for-bit the number run 3's ball-and-socket build got for the same
slit, which is a useful cross-check that the socket on the hand is the same socket.

**On the bounding box, since it was asked about.** It is 9.366 × 9.828 × 13.350 and no dimension of
it is 12, which is correct and not a defect:

- **13.350 in z** is the hand length 12.000 *plus* the 1.350 the socket's mating face stands above
  the wrist centre. `hand.md` measures hand length "wrist center to the bottom of the hand", and the
  wrist centre is the ball centre at z 0, not the top of the part. 12.000 + 1.350 = 13.350.
- **9.366 in x** is the collar: Ø9.400 with the two ±x relief slits nibbling the outermost sliver
  off, leaving ±√(4.7² − 0.4²) = ±4.6829. Before the slits it measured exactly 9.400.
- **9.828 in y** is the clip: Ø10.000 with 0.172 taken off the front by the mouth
  (5.000 − √(5² − 1.3²) = 0.172), so 5.000 + 4.828 = 9.828.

And yes, **it is smaller than a hand** — smaller than the Ø12 wrist it hangs from, in every
direction. That is open question 1, answered below.

## Render it and look at it

The part was rendered **alone** with `shadedviews` from five angles and I opened all five:
`62-x-hand-isometric.png`, `-front.png`, `-right.png`, `-top.png`, `-bottom.png`.

- **Isometric.** A four-tabbed socket collar with the spherical cavity inside and the mouth broken
  into four arcs, sitting on a C-clip whose opening faces forward. The slits run from the mating
  face right down to the collar foot. It matches what the numbers implied.
- **Right.** A textbook C — Ø10 outer, Ø3.3 bore, a parallel-sided 2.6 slot opening to +Y, with the
  collar standing above it. This is the view that shows the mouth is trimmed evenly on both sides.
- **Front.** Mirror-symmetric about the vertical centreline, which is the whole point of the part.
  The slit is visible running the collar's full length and stopping on clip material.
- **Top.** The mouth is genuinely four arcs, not one circle — the slits' inner ends cut *into* the
  cavity, as `ball-and-socket.md` insists they must. The clip's rectangular body shows behind the
  collar, sticking out ±5.0 in y where the collar only reaches ±4.7.
- **Bottom.** The clip's flat underside and the bore.

Nothing in the renders contradicts the measurements.

## The three open questions

**1. A Ø10 clip on a Ø12 wrist — does it read as a hand or as a mistake?**
Looking at all five renders: **it does not read as a hand.** It reads as a mechanical coupling with
a clip on the end, which is what it is. The problem is not that Ø10 is close to Ø12; it is that Ø10
is *less* than Ø12, so the silhouette **narrows** at the wrist and stays narrow. Arms do not get
thinner at the hand. The socket collar makes it worse: Ø9.4 is narrower still, so the widest thing
on the whole assembly is the limb, and the hand is a taper off the end of it. The plan's claim that
it "reads as deliberate" is not supported by looking at it.

Two honest options, neither of which I took, because the brief says to build the number and report:
take the clip out to Ø12 so the silhouette is continuous with the limb (still legal under the
README's Ø12 rule — the joint is not growing the limb), or accept it and stop calling it a hand in
student-facing text. I would take Ø12. Note that Ø12 also fixes the overhang in the next answer.

**2. Does the Ø9.4 socket collar foul the Ø10 clip?**
**No — and the relationship is the opposite of fouling.** The clip's Ø10 circle is centred at
z −7, so by the time it reaches the collar's foot at z −4.150 it has already narrowed to y ±4.108,
which is inside the collar's r 4.700. The two merged into one solid with no error and no
self-intersection. What actually happens is that the **collar overhangs the clip**: 17.107 mm² of
the collar's foot faces downward into free air (measured as the total area of the downward-facing
planar faces at z −4.150), overhanging by up to **1.700 mm** in x (4.700 − 3.000). That is an
unsupported overhang to print, and the clean 1.300 mm annular step that `ball-and-socket.md`
specifies round the collar foot **does not exist here** — the step is irregular, wide at ±x and
nearly nothing at ±y.

There is one more measured consequence, and it is the interesting one. In `ball-and-socket.md` the
collar stands on a Ø12 limb stub, and the slits bottom out on it. Here they bottom out on the clip,
and because the clip is not round the four slits do not bottom out equally: the two ±x slits have a
floor area of **0.400 mm²** each and the two ±y slits **1.2866 mm²** each, **3.373 mm²** in total.
The four tabs are still four tabs of the same 5.500 free length, so the socket should flex the same
as the proven one, but the base they are rooted in is not rotationally symmetric.

**3. Does the clip need a chamfer on its leading edges?**
**Yes.** Measured: the mouth is a parallel-sided 2.600 slot between two flat planes at z −5.700 and
z −8.300, and the jaw tips are square corners where those planes meet the Ø10 cylinder at
y 4.828. The bar is Ø3.200, so **0.600 mm of interference has to be taken up with no lead-in at
all** — the bar cannot cam the jaws open, it can only lever them. The same argument that carried for
the hinge stub carries here, more strongly, because a C-clip is pushed on by a middle-schooler's
thumb. I did **not** add one: the brief has no number for it and says to model and report, not tune.
A lead-in flare on the two jaw tips is the change I would make first.

## What did not work

1. **Brief step 1 is geometrically self-contradictory, and this is the finding of the run.**
   It says "Sketch on the Front plane — the clip's opening faces forward, along +Y, so the shape
   lies in the XZ plane and the clip is extruded fore-and-aft." A profile lying in XZ **cannot** have
   an opening along +Y; +Y is the extrude direction, normal to that sketch. Extruded fore-and-aft,
   the clip would open sideways along ±X and the part would be handed — which destroys the one idea
   the brief exists to test. The profile has to be sketched on the **`Right` (YZ) plane** and
   extruded **symmetrically along X**, so the bar runs left-right and the mouth opens along +Y.
   I built it that way. The symmetry check then passes; built as written it could not have.
2. **The brief's own tables forget the relief slits.** Step 5 says "Wrist socket … per
   `ball-and-socket.md`", and that document requires four 0.8 mm slits through the collar for its
   whole length, and is emphatic that a socket without them cannot open. `hand.md`'s numbers table
   has no slit row and its acceptance checks say nothing about them. A builder working from the
   table alone ships a socket that cannot accept a ball — 0.197 mm of retention on a solid collar —
   and every headline check in the brief still passes. I built them, from `ball-and-socket.md`'s
   numbers, and flagged it here. **`hand.md` needs a slit row and a slit acceptance check.**
3. **"Thinnest wall anywhere" expects the wrong answer.** The brief says "Expect the clip wall at
   3.35, unless the socket cuts into it." The socket does not cut into it — but the socket's own
   wall is 1.500, less than half of it, so the answer to "thinnest wall anywhere in the part" was
   never going to be 3.35. The expectation should read 1.5 at the collar.
4. **Sketch trim removes only the piece you clicked**, bounded by its two nearest crossings, and
   cleans up nothing else. Two circles crossed by two lines took **six** clicks, not two: outer arc
   between the lines, bore arc between the lines, then each of the four line stubs (two inside the
   bore, two outside the outer circle). One of the six clicks silently did nothing and the tool had
   to be re-armed with `m`. Budget six clicks and a re-arm for this step in the lesson.
   `19-x-after-all-trims.png`
5. **`#barD` = 3.2 does not scale — and neither does anything derived from it.** Recorded here
   because the brief asks for it: the bore 3.3, the mouth 2.6 and the clip wall 3.35 are all
   downstream of a LEGO dimension, so none of them may be written as a fraction of `#torsoH`.
6. **The bore: I used 3.300, not 3.400.** The brief offers 3.4 on the grounds that `#fit` is 0.2.
   Three reasons for 3.3: the brief's own acceptance check names Ø3.300; the derived clip wall 3.35
   is `(10 − 3.3) / 2` and moves if the bore does; and `#fit` = 0.2 is used everywhere else in this
   robot as a **radial** offset (it is the socket Boolean's `Offset distance`, applied to a radius),
   so applying it the same way here would give 3.2 + 2×0.2 = **3.6**, not 3.4. The 3.4 arithmetic
   uses `#fit` as a diametral allowance in the one place the model uses it radially. 3.3 gives
   0.050 radial clearance on the bar, which is a running fit at a 0.4 mm nozzle. **Not adjusted
   after measuring** — it measured 3.300 first time.
7. **Ticking `Second end position` silently flips the operation from `Add` back to `New`.** Set the
   depths first, then click `Add`, then fill `Merge scope`. Cost two attempts.
   `28-a-select-second-end-position.png`
8. **A second end position has its own, separate `Opposite direction` arrow.** After flipping only
   the primary one, both ends ran the same way (z +1.35 … +4.15), the collar no longer touched the
   clip, and `Add` produced a red feature that Onshape had nonetheless *accepted* — the tree showed
   an error but the feature was in the model. Flipping the second end's own arrow at (452, 421)
   fixed it. This is the same trap the ball-and-socket run hit, in a different dialog row. Three
   attempts. **Check a bounding box after every extrude with an offset or a second end.**
9. **The circular pattern failed silently-in-numbers and loudly-on-screen.** Accepting it with
   `Reapply features` unticked produced a red `Circular pattern 1` and **the part volume did not
   change at all** — 555.242378 before and after, i.e. three of the four slits were never cut.
   Onshape's message was exact: *"Could not create all instances as entered. Try selecting
   'Reapply features' option."* Ticking it fixed it and the volume dropped to 530.448910.
   Had I trusted the preview or a render taken from the wrong side, this is precisely how run 1's
   "decorative" slits happen. `58-x-pattern-error.png`, `59-a-select-reapply-features.png`
10. **Clicking a circle's *curve* opens Extrude in Surface mode**, holding "Edge of Sketch 1", and
    leaves a `Surfaces (1)` entry behind. Pick the region *interior*. `27-x-solid-tab-empty.png`
11. **There is no Sphere primitive.** `Search tools` → "Sphere" gives "No items match your search".
    The sketch-and-revolve path from `ball-and-socket.md` is the only route. `32-b-done-sphere-dialog.png`
12. **`Rename` vanished from the tree's context menu** while two rows were still selected, and
    left-clicking a row did not clear the earlier selection. The menu's own `Clear selection`, then
    a fresh left-click and right-click, brought it back. Three attempts.
13. **The arc flyout will not take a raw coordinate click.** (421, 162) selected the Z axis instead.
    Open the caret at (383, 58), assert `Center point arc` is visible, and click it through a
    locator — all in one Playwright call, because the flyout does not survive the call boundary.
14. **`n` on the `Top` plane produced the *Bottom* view**, mirrored. Harmless here: the only thing
    drawn on that plane in that sketch was a circle on the origin.
15. **The Onshape edit session timed out** during the 2½ hours the run was stopped, with the banner
    "Your Onshape session has timed out. Your document is saved." Read-only REST kept working
    throughout — the cookie was fine, it was the editing socket that had dropped. `Click here to
    reconnect.` restored editing and `window.name` survived it. `41-x-resume-state.png`

## What the brief never said

- **The clip's thickness.** There is no number for the extrude depth anywhere. I used **6**, because
  it is `#ballD` and `#torsoH / 8`, i.e. an existing plan variable that scales with the robot, and
  because extruding it `Symmetric` makes the left-right symmetry structural rather than something
  that has to be checked. **The brief needs a row for this.**
- **Where the clip's centre goes.** The brief says "z = −7 or wherever the clip lands once the socket
  is placed — report what drove it." What drove it: hand length 12 puts the lowest point at z −12,
  and a Ø10 clip whose bottom is at −12 has its centre at **−7** and its top at **−2**. Given the
  brief's own numbers there is no freedom here at all; −7 is forced, not chosen. Worth saying in
  the lesson, because it is a nice example of a dimension that looks free and is not.
- **That the clip and the collar necessarily overlap.** The collar's foot is at z −4.150
  (1.350 − 5.500) and the clip's top is at z −2.000. They overlap by **2.150 mm** whatever anyone
  wants, which is what makes step 6's "blend the clip into the socket body so it is one solid" free
  — no blending feature was needed, the collar's `Add` did it. The brief presents that step as work.
- **Relief slits** — see #2 above.
- **What "hand length 12.000" is measured from.** The acceptance check says "from wrist center to
  the lowest point", which is unambiguous once you notice it; the numbers table's "wrist center to
  the bottom of the hand" is the same thing. I measured the cavity sphere's centre (0, 0, 0) and the
  body's lowest point (−12.000). The bounding box is 13.350 and it would be easy to report that
  number by mistake.
- **What to do about `#clipR`.** The brief says the plan discusses it but has no variables row for
  it, and marks Ø10 `proposed` for that reason. Nothing tells the builder whether to *add* the
  variable. I did not: this document is a standalone test build, not the shared Part Studio.

## Retrospective

**What went well.** The measurement discipline paid for itself three times. The circular pattern
looked plausible in preview and was silently wrong; the only thing that caught it was taking a
volume before and after and getting the same number twice. The collar's direction flip looked fine
in the preview and was upside down; the bounding box caught it. And the socket's cavity came out at
109.4820 rather than 27.78, which is the check `ball-and-socket.md` put there precisely because
run 1 got that one wrong. Deferring to the ball-and-socket run's proven click path was also right —
the slit's four dimensions, in the order that document gives them, defined the rectangle first try,
and the one-slit volume came out bit-for-bit identical to that run's, which is a stronger check on
"same socket" than any dimension I could have taken.

**What went poorly.** I spent the first twenty minutes of the sketch step building to the brief's
`Front` plane instruction before working out that it could not be right, and I nearly built a handed
part. I should have read step 1 against the acceptance check before opening the browser: the check
says "mirror about the YZ plane", the step says "sketch on XZ", and those two cannot both be
satisfied by a clip that opens along +Y. Two minutes of reading would have saved twenty of
modelling. I also made a judgement call mid-run to skip the relief slits because `hand.md`'s tables
omit them, and then reversed it later — the reversal was right, but the first decision was me
letting a table override a document the same brief points at, which is exactly the failure mode the
briefs README warns about.

**What I would change.**

- **In `hand.md`:** fix step 1 to say `Right` plane, extruded symmetrically along X. Add a numbers
  row for the clip's thickness. Add a slit row and a slit acceptance check, or say explicitly that
  the hand's socket omits them and why. Change the "thinnest wall" expectation from 3.35 to 1.5.
  Drop the 3.4 bore suggestion or fix its arithmetic — as written it misuses `#fit`. Say that the
  clip centre at −7 is forced by hand length and clip diameter, not chosen.
- **In `onshape-gui-howto.md`:** add the circular-pattern trap. "Could not create all instances as
  entered — tick `Reapply features`" belongs in the failure-mode table next to the extrude-direction
  entry, because it is the same shape of bug: the feature is accepted, the tree shows an error, and
  *every dimensional check still passes*. Also worth a line: a feature-pattern axis will not take a
  plane from the tree, but takes a cylindrical face clicked in the graphics area.
- **In the way I was briefed:** the launch was good — the stamp-uniqueness rule, "decide and record",
  and "the brief is the thing under test, not you" were all load-bearing, and the last one is why
  this report says step 1 is wrong instead of quietly building around it. The one thing I would add
  is a sentence about what to do when a brief's prose points at another document whose requirements
  its own tables then omit. I had to decide that alone and I decided it twice.

**Clock.** First entry in `steps.log` 00:16:10, last 04:03:54, with the run stopped between 00:57
and 03:33 by an API spend limit. Hands-on was therefore about **72 minutes** across the two
stretches, inside the Constitution's 90-minute floor. I clocked this from the log's own timestamps.
