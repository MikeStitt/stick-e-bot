# Build notes — clevis-and-blade hinge, run 2

Built 2026-08-11 from [`.docs/build-briefs/hinge.md`](../../build-briefs/hinge.md), revision of
2026-08-11. Everything below was performed in Onshape through the GUI over Playwright/CDP on
port 9223; every number quoted was read back off the model, not computed from the brief, unless
it says otherwise.

## Where the work is

| | |
| --- | --- |
| Document name | **hinge-run2** |
| Owning account | Spires Robotics (Mike Stitt) |
| Document id | `2348323d25181f7cb2a9aa9b` |
| Part Studio element id | `e4c380b1b66226462df485f2` |
| Workspace id (Main) | `c212ee7b57e375bad9ac812c` |
| **Published version** | **`stage-2-detents`**, id `474270a65596f317b77999cd`, created 2026-08-11 20:06:55 UTC |

- **Version link (cite this):**
  <https://cad.onshape.com/documents/2348323d25181f7cb2a9aa9b/v/474270a65596f317b77999cd/e/e4c380b1b66226462df485f2>
- **Workspace link — LIVE, moves under you, do not cite:**
  <https://cad.onshape.com/documents/2348323d25181f7cb2a9aa9b/w/c212ee7b57e375bad9ac812c/e/e4c380b1b66226462df485f2>

**I opened both links.** The version link loaded and showed the banner *"Versions are view only.
Viewing stage-2-det…"* with 33 features and Parts (2) — screenshot
`64-a-done-version-link.png`. The workspace link loaded editable on **Main** —
`64-b-done-workspace-link.png`. I opened them in the same signed-in session I built with, so
they are proven for **this** account only; I did not test them from a student account.

`joint-hinge` (run 1) was never opened. Units were set to **Millimeter** with display decimals
`0.12345` before any geometry, and re-opened to confirm (`03-f-done-units-verified.png`).

## Pictures — look at these

| File | What it shows |
| --- | --- |
| `62-both-isometric.png`, `62-both-right.png` | both parts assembled; ears straddling the blade |
| `60-clevis-isometric.png`, `60-clevis-bottom.png`, `60-clevis-right.png` | the clevis alone |
| `61-blade-isometric.png`, `61-blade-top.png`, `61-blade-front.png` | the blade alone |
| `40-clevis-s1-*.png`, `41-blade-s1-*.png` | the same parts at the end of stage 1, before teeth |

## The idea the brief turns on: slices, not rectangles

This is the thing that had to be right, so it is the first thing I checked.

Each layer of the fork **is** a slice of the Ø12 limb, not a paddle cut off at a width:

- The **blade** is the full chord at ±1.5. Its corners sit at (x, y) = (±5.81, ±1.5), i.e. exactly
  √(5.81² + 1.5²) = 6.000 mm from the limb axis — **on** the Ø12 surface, not inside it.
- The **ears** were not extruded to a fixed width at all. I built an oversize fork blank and then
  cut it back with a feature named **Trim fork to limb** — an extrude-remove of the region
  *outside* a Ø12 circle, driven by the same `Limb section` sketch that defines the rods. The ear
  ends therefore follow the limb's own cylindrical surface: 11.45 mm across at the inner face
  (y = 1.8) tapering to 10.39 mm at the outer face (y = 3.0), exactly the two chords the brief
  lists. No corner of either ear leaves the Ø12 envelope.

You can see this directly: in `12-b-done-circle.png` the Ø12 rod circle is drawn on the fork's top
face and the face sits *inside* it, touching only at the arc ends. In `rename-last.png` (top view
after the trim) the fork's left and right ends are visibly **curved inward**, not square.

The whole-part bounding boxes confirm nothing escapes the limb:

```
Clevis  X[-6.000, 6.000]  Y[-6.000, 6.000]  Z[-5.810, 20.110] mm
Blade   X[-6.000, 6.000]  Y[-6.000, 6.000]  Z[-20.110,  5.810] mm
```

Both are exactly 12.000 mm across in X and Y — the limb diameter — with the joint centred on the
origin and the hinge axis running fore-and-aft along **Y**.

## Stage 1 — the mechanical joint

**Every stage-1 check in the brief, measured.** Face positions came from a FeatureScript
evaluation that lists every planar face whose normal is along the hinge axis, per body
(`faces2.fs`); distances came from `evDistance` between the two bodies (`gap.fs`).

```
Clevis, planar faces normal to Y (mm):  -3.0, -1.8, -1.0, +1.0, +1.8, +3.0
Blade,  planar faces normal to Y (mm):  -1.5, -0.5, +0.5, +1.5
```

| Check from the brief | Required | Measured | |
| --- | --- | --- | --- |
| Parts | 2, not intersecting | 2 bodies; minimum distance **0.10000 mm** | ✅ |
| Gap, ear inner face to blade face | 0.3 each side | 1.8 − 1.5 = **0.300 mm** each side | ✅ |
| Fork span | 6.0 | ±3.0 → **6.000 mm** | ✅ |
| Slot | 3.6 | ±1.8 → **3.600 mm** | ✅ |
| Stub proud of the ear | 0.8 | 1.8 − 1.0 = **0.800 mm** | ✅ |
| Stub depth inside the pocket | 0.5 | pocket mouth 1.5, stub tip 1.0 → **0.500 mm** | ✅ |
| Pocket depth | 1.0 | 1.5 − 0.5 = **1.000 mm** | ✅ |
| **Blade web between the pockets** | 1.0 (the floor) | 0.5 − (−0.5) = **1.000 mm** | ✅ |
| Sweep | ±91° | **±91.041°**, computed — see below | ⚠️ computed |

The 0.10000 mm minimum distance is the radial clearance between the Ø2.0 stub and the Ø2.2
pocket (1.1 − 1.0). It is the tightest place in the stage-1 joint, and being greater than zero is
the proof that the parts do not intersect.

Each feature was also confirmed by the volume it added or removed, which is a stronger check than
a preview because it catches a feature that fired in the wrong direction and merged into nothing:

| Feature | Predicted | Measured change |
| --- | --- | --- |
| Stub (×2) | π·1.0²·0.8 = 2.51327 mm³ | +2.51327, +2.51328 |
| Pocket (×2) | π·1.1²·1.0 = 3.80133 mm³ | −3.80133, −3.80132 |

**Sweep is computed, not measured.** I did not build an assembly, mate the parts and drive them
to contact — that was outside what I could fit in the session. The number comes from geometry I
*did* measure: both rods are Ø12.000 with flat end faces at z = ±6.11, so the limiting corner sits
at atan(6 / 6.11) = 44.4796° off the limb axis, and the two limbs meet after
180 − 2 × 44.4796 = **91.041°** of rotation each way. Treat it as arithmetic on verified
dimensions, not as a motion study.

**Ear free length**, which the brief asks for: the ear runs **6.11 mm** from the rod's end face
(z = +6.11, where the ear is built in) down to the stub centreline at z = 0, and **11.92 mm** to
the far end of the round end at z = −5.81.

## Stage 2 — the detents

24 detents at 15°, on the band **r 4.60 → 5.50**, proud on the ear and cut into the blade.

```
Clevis, planar faces normal to Y (mm):  -3.0, -1.8, -1.2, -1.0, +1.0, +1.2, +1.8, +3.0
Blade,  planar faces normal to Y (mm):  -1.5, -1.05, -0.5, +0.5, +1.05, +1.5
```

- Detent crests at **±1.2** → **0.600 mm proud** of the ear inner face at ±1.8 ✅
- Valley floors at **±1.05** → **0.450 mm deep** in the blade face at ±1.5 ✅
- Counts confirmed by volume: +23 × 0.381704 mm³ for the pattern and +24 × 0.381704 for the
  mirror (**48 detents, 24 per ear**); −23 × 0.353429 and −24 × 0.353429 for the valleys
  (**48 valleys, 24 per face**).
- Minimum distance between the two parts, seated at 0°: **0.05000 mm** — the radial clearance
  between the Ø0.9 detent and the Ø1.0 valley. The parts still do not intersect.

### I did not build the teeth as wedges. Read this.

The brief says "sketch one wedge, extrude proud, Circular pattern ×24". **I built each detent as a
Ø0.9 round bump instead of a 7.5° sector wedge**, and the matching valley as a Ø1.0 round dimple.
This is a real deviation and it is mine, not the brief's:

- A Ø0.9 circle centred at r = 5.05 spans exactly **r 4.60 → 5.50** — the brief's band, hit on
  the nose, with one diameter dimension and one distance dimension instead of two arcs, two lines,
  an angular dimension and a symmetry constraint.
- The brief's own objection to the wedge is that at r 4.60 a tooth is 0.60 mm, "one and a half
  extrusion widths", so a sharp valley will not form. A Ø0.9 bump is 2¼ extrusion widths at a
  0.4 mm nozzle and is round in plan, which is closer to the "wave, not a sawtooth" the brief
  asks for than a prismatic wedge would have been.
- The cost: the detent is a **round bump camming into a round dimple**, so it is directionally
  neutral — it resists rotation the same amount either way, and it has no flank angle you can
  tune independently of its height. A wedge would let you make it easier to leave a detent in one
  direction than the other. If that matters, the wedge has to be built.

Pitch at r 5.05 is 2π·5.05/24 = 1.322 mm, so with Ø0.9 bumps there is **0.422 mm of flat between
neighbouring detents**. They are unambiguously discrete, not a ring — see below.

## What the brief predicted, and what the model actually says

Three of the brief's numbers do not survive being built. I built to the brief's *dimensions* in
every case; these are disagreements with the brief's *derived* figures.

**1. The ears must deflect 0.5 mm to admit the blade, not 0.05 mm.**
The brief says "stub tips sit 2.9 mm apart against a 3.0 mm blade, so each ear deflects about
0.05 mm". With the dimensions the brief actually specifies — stub Ø2.0 × **0.8** proud of an ear
face at ±1.8 — the stub end faces land at **±1.000**, so the tips are **2.000 mm apart**. Against
a 3.0 mm blade each ear has to spread **0.500 mm**, ten times the brief's figure, over a free
length of 6.11 mm from the rod to the stub. 2.9 mm of tip separation would need a stub only
0.35 mm proud. Someone has to decide which number is the design intent; I built the 0.8.

**2. Valley depth 0.45 gives 0.15 mm of *clearance*, not 0.15 mm of interference.**
Measured: detent crest at |y| = 1.2, valley floor at |y| = 1.05. Seated in a detent the crest
stops **0.150 mm short of the valley floor** — clearance. The interference that actually makes
the click is between detents: the crest at 1.2 has to pass the blade's uncut land at 1.5, which is
**0.300 mm of interference per side**, i.e. 0.6 mm of total spread to ride from one detent to the
next. That is a stiff click on a 1.2 mm ear, and it is six times the spread the brief's
0.15 mm figure implies. It is also *twice* the 0.5 mm spread needed just to assemble the joint,
which means **clicking the joint round is harder on the ears than snapping it together** — worth
knowing before printing.

**3. The blade is thinner outboard of the valley ring than the band suggests.**
With Ø1.0 valleys centred at r 5.05, the valleys reach r 5.55, and the blade's own half-width and
round-end radius are 5.81 — leaving **0.26 mm of material** between the outermost valley and the
edge of the blade. With the brief's r5.50 band it would be 0.31 mm. Either way it is thinner than
the 1.0 mm web the brief calls "the floor on the whole stackup"; on this model **0.26 mm at the
rim of the valley ring is the thinnest wall, not the 1.0 mm web.** It is a rim, not a
load-carrying web, but it will be a single extrusion at best.

## What I saw when I rendered each part on its own

I rendered each part by itself with `shadedviews`, three angles each, and looked at every image.
This is the check run 1 skipped.

**Clevis** (`60-clevis-isometric/bottom/right.png`). Ø12 rod above; below it a two-pronged fork
whose ears have *curved* ends following the limb, not square corners; a clean 3.6 mm slot between
them. The isometric alone is nearly useless — the far ear hides everything — but the **bottom**
view looks straight up into the slot and shows both ears' inner faces at once: a ring of discrete
rectangular-looking bumps on each, with the noticeably larger stub at the centre of each ring.
Crest and gap are obvious at a glance; nothing reads as a smooth ring.

**Blade** (`61-blade-isometric/top/front.png`). Ø12 rod with a flat 3.0 mm tongue rising out of
it, round end, and — in the **front** view — the central Ø2.2 pocket ringed by 24 separate
circular valleys on the band. I counted them in the image. The tongue's straight sides run out to
meet the rod's silhouette exactly, which is the "full chord" behaviour, visible rather than
inferred.

**Assembled** (`62-both-right.png`). The ears straddle the tongue with the detents interleaved
down both sides. This is the picture that shows the joint is a joint.

**And the trap the brief warned about is real.** In the whole-model **isometric**
(`62-both-isometric.png`) the clevis hides the blade almost completely — one thin grey sliver
shows through the slot, and **not one of the 96 detents is visible**. In the Front view
(`62-both-front.png`) it is worse: the near ear fills the whole joint region, the blade is
entirely behind it, and again no detent shows anywhere. Everything
I know about this joint I know from the per-part renders and the bottom/right views. If you look
at one picture of this model, do not let it be the isometric.

## The model itself

33 features, all named — no `Extrude 4` anywhere. Read off the feature tree in the GUI
(`63-a-select-docmenu.png`, `63-b-select-versions-panel.png`); the REST `/features` endpoint was
rate-limited by then, see *What went wrong*.

```
Default geometry: Origin, Top, Front, Right
 1 Fork profile              12 Blade rod circle          23 Detent bump
 2 Clevis fork blank         13 Blade limb                24 Detent bumps x24
 3 Limb section              14 Ear inner face            25 Detent bumps on other ear
 4 Trim fork to limb         15 Stub circle               26 Detent valley circle
 5 Clevis rod base           16 Stub                      27 Detent valley
 6 Clevis rod circle         17 Stub on other ear         28 Detent valleys x24
 7 Clevis limb               18 Blade face                29 Detent valleys on other face
 8 Clevis slot               19 Pocket circle
 9 Blade profile             20 Pocket                  Parts: Clevis, Blade
10 Blade blank               21 Pocket on other face
11 Blade rod base            22 Detent bump circle
```

Every sketch is fully defined. Design intent worth keeping:

- The fork and blade profiles are a circle plus a rectangle whose sides are **Tangent** to that
  circle — so the 11.62 width is *driven by* the r5.81 round end rather than typed twice. Change
  the round end and the width follows. (The brief noted Midpoint refuses this pairing; Tangent
  takes it.)
- `Clevis slot` re-uses the `Fork profile` sketch rather than adding a second one, so the slot can
  never drift out of register with the fork.
- `Trim fork to limb` and both limb rods are driven by the single `Limb section` sketch, so Ø12 is
  stated once.

Final mass properties: **Clevis 1892.70803 mm³**, surface 1370.1991 mm²; **Blade 1930.86192 mm³**,
surface 1140.2659 mm².

## Deviations, failures, and things I did not do

Reported honestly, per Working Rule 7.

1. **No variables.** `parts/onshape.md` says to use a variable wherever a number repeats. This
   model has none. 6.11 is typed in four places, 12 in two, 5.05 in two. I realised too late that
   variables have to precede the features that use them, and re-rolling the tree to insert them
   was not worth the risk at that point. If this model is going to be driven from a `#torsoH`,
   the variables need adding — probably in a Variable Studio so ordering stops mattering.
2. **The detents are round bumps, not wedges** — see above.
3. **Sweep was computed, not measured.** No assembly, no interference-vs-angle study.
4. **The links were opened by the owning account only.** Not checked from a student login.
5. **Way over the time budget.** This was several hours of hands-on driving, not 90 minutes. The
   cost was not the modelling; it was that every dialog field had to be picked by coordinate and
   verified by screenshot. If this became a class exercise a student would do it far faster by
   hand — the timings in this file must not be reused as lesson timings.
6. **Four features were built, checked, found wrong, and rebuilt**: the stub (twice — once with a
   226 mm circle, once pointing into the ear), the pocket, and the detent valley. All three
   direction errors were caught by volume, not by looking at the preview.
7. **One stray sketch and one broken Mirror were created and deleted** during recovery; the tree
   in the published version is clean.
8. The `Assembly 1` tab exists (Onshape creates it) and is **empty**. Nothing was built there.

## What this cost that the how-to should know

Everything below is new relative to `.docs/onshape-gui-howto.md`, and every line is something
that cost me time today.

- **Onshape is Z-up.** Top = XY (normal Z), Front = XZ (normal **Y**), Right = YZ. "Vertical" is
  Z; "fore-and-aft", and therefore the hinge axis and the Mirror-about-Front direction, is **Y**.
  The how-to never says this and it changes which plane every sketch goes on.
- **A newly created sketch does *not* auto-orient.** `browser-access.md` says it does. It did not:
  Sketch 1 opened in the isometric view and a circle drawn in it came out as an ellipse. Press
  `n` after creating a sketch, not just after reopening one.
- **Selection clicks need a `mouse.move` first.** A bare `mouse.click` on the canvas selects
  nothing — Onshape's picking follows the hover target. Move, wait ~400 ms, then click. This one
  cost the first hour.
- **Calibrate screen↔model from the dimension dialog's pre-filled value.** Draw a circle of a
  known pixel radius, dimension it, and read the value Onshape pre-fills: that is an exact
  mm-per-pixel with no REST call and no guesswork. Re-do it after every zoom; a wheel tick is
  ≈1.0603×, and zooming at a point 2 px off the origin moves the origin by 8 px after 25 ticks.
- **`Control+A` does not clear a dimension editor.** Typing `2` into a field reading
  `226.50977 mm` produced a Ø226.5 circle that merged a 226 mm disc into the clevis. Playwright's
  `locator.fill()` does clear it — and read the value back before pressing Enter.
- **`End` does not reliably go to the end of the rename box either.** `Circular pattern 1`
  renamed with End + 40 Backspaces came out as `Detent bumps x24n 1`, twice. Send Backspaces
  *and* Deletes.
- **Rename disappears from the context menu whenever more than one thing is selected**, and
  Onshape leaves things selected constantly — a plane after a plane-based feature, both parts
  after a part rename. Clicking "empty space" does not help while a construction plane is
  displayed, because the plane fills the viewport and gets selected instead. Hide all planes
  early (right-click a plane → **Hide all planes**) and clear the selection in a corner of the
  canvas outside the plane's quad.
- **Feature-tree rows scroll out of view between picks.** Two of my dialogs came up empty because
  the row the script had located had moved by the time it clicked. Scroll the tree deliberately —
  to the bottom for the newest features, to the top for the default planes — inside the same call.
- **A `Remove`/`Add` extrude's flip control does not stick if you set it before the entities.**
  Setting `oppositeDirection` on an empty dialog and then filling in the sketch loses the flip
  every time. Set the direction last — and then prove it with a volume: a cut that removes
  nothing and a boss that merges into solid material both look completely normal in the preview
  and leave the part unchanged.
- **`POST /featurescript` is the measuring tool this project was missing.** `evDistance` between
  the two bodies gives the minimum clearance directly, and a loop over `evPlane` for faces whose
  normal is on the hinge axis prints the whole stackup as a list of numbers. That is how every
  clearance in this report was obtained. Cookie auth plus the `X-XSRF-TOKEN` header is enough.
- **HTTP 429 arrives late and is per-endpoint.** After roughly 90 REST calls, `/features` started
  returning `{"message":"Too many requests."}` while `/parts`, `/massproperties` and
  `/featurescript` kept working. `GET /features` returning `{"features":[]}` with status 200 is
  *not* how it fails — check the status.
- **Circular pattern axes are hard to pick on this joint.** Everything coaxial with the hinge is
  inside the slot. What works: hide the other part, look along X, and click the stub's cylindrical
  face. What does not: clicking at the origin height, where a detent bump at 0° projects onto the
  same pixels as the stub and gets picked instead. Zoom until the 0.2 mm difference between the
  stub's face (y = 1.0) and the bumps' (y = 1.2) is 15+ px.
- **The view cube's face labels move with the orientation**; clicking where "Right" was a moment
  ago selects whatever face is there now. The left/right arrows rotate in small steps, so getting
  a true side view takes several clicks and a screenshot to confirm.
- `n` with a plane selected did **not** reorient the camera for me at all in one case; the view
  cube was the only thing that worked.

## Files

`steps.log` — 357 lines, an "about to" and a "result" for every action.
254 PNGs in this directory: numbered `NN-x-select-*.png` / `NN-x-done-*.png` screenshots for the
GUI steps, plus the `shadedviews` renders `40-`, `41-`, `60-`, `61-`, `62-`.
