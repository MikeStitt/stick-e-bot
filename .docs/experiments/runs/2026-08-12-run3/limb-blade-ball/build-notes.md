# Forearm and shin — blade at the top, ball stud at the bottom (run 3, picked up mid-build)

## Where the work is

| | |
| --- | --- |
| Document name | `limb-blade-ball-run3` |
| Document id | `8844e1331199cc35de25a417` |
| Element id (Part Studio 1) | `e70b20b1b40fabbcf35f2956` |
| Workspace id | `b5995fc863d4643895b80f15` |
| Version name | `run3-limb-blade-ball-complete` |
| Version id | `d05d157b5a04360a06b7e8a7` |
| Part | `Forearm and shin`, part id `JHD` |

- **Version link (cite this one):**
  `https://cad.onshape.com/documents/8844e1331199cc35de25a417/v/d05d157b5a04360a06b7e8a7/e/e70b20b1b40fabbcf35f2956`
- **Workspace link — live, will drift:**
  `https://cad.onshape.com/documents/8844e1331199cc35de25a417/w/b5995fc863d4643895b80f15/e/e70b20b1b40fabbcf35f2956`

**I opened both links** in my own browser page after publishing the version. Each loaded to the
Part Studio with the page title `limb-blade-ball-run3 | Part Studio 1`; the version link is in
`23-a-version-link-open.png`. The ids are not pasted together from memory.

The version was published **before** these notes were written, from the state described below:
15 features, 1 part, every feature `OK` read from `GET .../features` `featureStates`, volume
2039.63557 mm³.

No new document was created. This is the document my predecessor started.

Browser page stamp for this run: **`LIMBBB2_RUN3_3b7e91`**. I censused all 20 pages before
stamping, confirmed nothing carried that name, stamped my own new page, and re-censused to
exactly one match. My predecessor's page, still carrying `LIMBBB_RUN3_cfca2a`, was left alone
and never touched.

## What I inherited and what I did

My predecessor was killed mid-sketch. It left 6 features, one part, volume 1942.98845 mm³,
bbox 12.000 × 12.000 × 25.810, everything `OK`, no version. **I verified all of that myself
through read-only REST before touching anything** and it was exactly as described.

| Feature | Whose |
| --- | --- |
| `Blade profile`, `Blade blank` | predecessor |
| `Limb section`, `Trim blade to limb` | predecessor |
| `Limb` | predecessor |
| `Sketch 1` (the ball stud profile, unfinished) | predecessor — I finished and renamed it |
| `Ball stud` | mine |
| `Blade face plane`, `Pocket circle`, `Pocket` | mine |
| `Detent valley circle`, `Detent valley`, `Break the valley rim` | mine |
| `24 detent valleys`, `Mirror the blade features` | mine |

### The inherited sketch: kept, not redone

`Sketch 1` was the start of the ball stud profile and its geometry was right — arc r3 centred
(0, −24), stalk half-width 1.5, closed profile, arc's **upper** endpoint on the **bottom** of the
stalk as `ball-and-socket.md` requires. It was **under-defined by exactly one degree of freedom**:
the stalk's top edge floated, sitting at an arbitrary z = −18.90418 (I read that number out of the
dimension box's pre-fill, which is how I know it was arbitrary rather than chosen).

I kept it and added one dimension — stalk top edge to the X axis = **19** — which took it to 17
constraints against 17 DOF. `12-d-sketch-curves-black.png` is a crop showing every curve black.
Redoing a correct sketch to make it mine would have cost 15 minutes and gained nothing.

One thing I left alone: there is a stray **angle** dimension in that sketch, but it is
`driven: true` — a reference dimension — so it constrains nothing. Removing it risked taking the
overlapping driving "24" with it. Recorded rather than fixed.

## The click path that actually worked

Steps 1–9 are my predecessor's, from its own log, and I did not repeat them. Steps 11 onward are
mine. (There is no step 10: the predecessor's step 10 was the sketch it never finished, which
became my step 11–12.)

| # | Step | Screenshots |
| --- | --- | --- |
| 1–9 | *Inherited:* blade profile (Ø11.62 round end, tangent sides, 6.11 to the flat) → `Blade blank` (Extrude symmetric 3.0) → `Limb section` (Ø12 on Top) → `Trim blade to limb` (Extrude **Intersect**) → `Limb` (Extrude **Add**, depth 13.89, **starting offset 6.11**, both directions flipped) | `04-*` … `09-*` |
| 11 | Double-click `Sketch 1` in the tree to edit it; `n` for normal-to, `f` for fit, then wheel-zoom to the stalk | `11-a-sketch1-open.png`, `11-b-sketch1-normal.png`, `11-c-zoomed.png`, `11-d-zoomed2.png` |
| 12 | `d`, pick the stalk's top edge and the X axis, box pre-fills `18.90418 mm`, type `19`, Enter. Accept the sketch, rename to `Ball stud profile` | `12-a-select-stalk-top-edge.png`, `12-b-done-stalk-top-19.png`, `12-d-sketch-curves-black.png`, `12-e-done-sketch-accepted.png`, `12-f-done-renamed.png` |
| 13 | Pre-select the profile region in the graphics area, then `revolve`. Set **Add**; click into **Revolve axis** and pick the sketch's axis line; **Merge scope** already read `Forearm and shin`; accept | `13-a-select-profile-region.png`, `13-b-revolve-dialog.png`, `13-c-select-revolve-axis.png`, `13-d-done-ball-stud.png`, `13-e-done-renamed.png` |
| 14 | `cPlane` → **Offset** 1.5 from **Front**, rename `Blade face plane` | `14-a-select-plane-offset.png`, `14-b-done-blade-face-plane.png` |
| 15 | Sketch on `Blade face plane`, `c` circle on the origin, `d` → 2.2 | `15-a-sketch-on-blade-face.png`, `15-b-select-pocket-circle-drawn.png`, `15-c-done-pocket-circle.png`, `15-d-pocket-circle-crop.png` |
| 16 | Extrude the pocket circle: **Remove**, depth 1.0, assert **Merge scope** names the part, accept | `16-a-select-pocket-remove.png` (no after-shot — see *What did not work*) |
| 17 | Sketch on `Blade face plane`, circle on the vertical axis, `d` → Ø1.0, then `d` centre-to-horizontal-axis → 4.8 | `17-b-select-valley-circle-drawn.png`, `17-c-done-valley-dia.png`, `17-d-select-valley-centre.png`, `17-e-done-valley-at-4p8.png`, `17-f-valley-circle-defined.png` |
| 18 | Extrude the valley circle: **Remove**, depth 0.45, scope asserted, accept | `18-a-select-valley-remove.png` |
| 19 | Zoom hard onto the one valley; `fillet` on the valley's **rim edge** (not its bore face), radius `0.1` | `19-b-hover-rim-edge.png`, `19-c-select-rim-edge.png`, `19-d-select-rim-fillet-0p1.png` |
| 20 | Circular pattern from the pattern split-button's **flyout caret**; switch **Part pattern → Feature pattern**; features = `Detent valley` + `Break the valley rim`; **Axis of pattern** = the Pocket's rim edge; instance count 24; **angle left at 360°** because `Equal spacing` is on; tick **Reapply features**; accept | `20-a-pattern-flyout.png`, `20-b-pattern-dialog.png`, `20-d-feature-pattern.png`, `20-f-select-pattern-axis.png`, `20-g-pattern-filled-crop.png`, `20-h-select-pattern-24.png` |
| 21 | `mirror`; switch **Part mirror → Feature mirror**; the four blade features; **Mirror plane** = Front; **Reapply features**; accept | `21-a-mirror-dialog.png`, `21-b-select-mirror-features.png`, `21-c-select-mirror-plane.png`, `21-d-done-mirror.png` |
| 22 | Left rail, second icon down (`Create version…`), name `run3-limb-blade-ball-complete`, **Create** | `22-b-rail-hover.png`, `22-c-version-dialog.png`, `22-d-done-version-created.png` |
| 23 | Open the version link and the workspace link in my own page | `23-a-version-link-open.png` |

Renders of the part alone, four angles, through `GET .../parts/.../partid/JHD/shadedviews`:
`render-final-{isometric,front,right,top}.png`. **I looked at all four** before writing this.

- *Isometric and front:* blade with a ring of 24 valleys around the central pocket, Ø12 stock
  below it, and the ball hanging on a short neck. Matches the numbers.
- *Right:* the blade is a 3 mm slab seen edge-on, the ball centred on the axis.
- *Top:* the 3 mm blade band crosses the Ø12 circle and **its two ends touch the circle exactly**
  — this is the picture of "the corners land on the Ø12 surface".

I also measured the front render's silhouette in pixels as a cross-check on the geometry:
limb band 402 px, blade band 388 px, part 1098 px tall, i.e. 12.00 / 11.58 / 32.78 mm at
33.5 px/mm against 12.000 / 11.619 / 32.810 modelled. The 0.04 mm shortfall on the blade is the
1 px dark edge line at each side, not the part.

## Every acceptance measurement

Method: read-only FeatureScript through `POST .../featurescript` (`evSurfaceDefinition`,
`evBox3d`, `evDistance` over `qOwnedByBody(body, EntityType.FACE)`), plus
`GET .../massproperties`. Nothing here is inferred from a dialog or a preview.

| Check | Expected | Measured | How |
| --- | --- | --- | --- |
| 12.000 across X | 12.000 | **12.000** (body box x −6.00000 … +6.00000) | `evBox3d` on the body |
| 12.000 across Y | 12.000 | **12.000** (body box y −6.00000 … +6.00000) | same |
| Nothing stands proud | no face outside Ø12 | blade sides are planes at x = ±5.81, blade faces reach x = ±5.80948, ball Ø6 — **all inside** | face census |
| 24.000 between joint centres | 24.000 | **24.000**: hinge axis is the r5.81 cylinder through z = 0; sphere centre (0, 0, **−24**) | `evSurfaceDefinition` |
| Blade 3.000 | 3.000 | **3.000**: the two blade faces are planes at y = **−1.50000** and **+1.50000** | face census |
| Ball Ø6.000, centre on the axis | 6.000 | **6.000**: one sphere face, r 3.000000, centre (0, 0, −24) | `evSurfaceDefinition` |
| Blade corners on the Ø12 surface | corners **on** Ø12 | **yes** — see below | face census + box |
| Pocket Ø2.2 × 1.0, web 1.0 | 2.200 / 1.000 / 1.000 | pocket floors are planes at y = **∓0.5** spanning x −1.1…1.1, z −1.1…1.1 → **Ø2.200, 1.000 deep, web 1.000** | face census |
| Detent valleys Ø1.0 × 0.45, 24 at 15° | 24 per face | **24 floors at y = −1.05 and 24 at y = +1.05** (48 bores of r 0.5) → Ø1.000, 0.450 deep, 24 per face. The two rim centres I read out — (0, −1.4, 4.800) and (−1.2423, −1.4, 4.6364) — are both at r 4.8000 and **15.0000° apart** | face census |
| Rim break r0.10 on the edge | present on every valley | 48 torus faces, major 0.6, minor 0.1 | face census |
| Rim outboard of the valley ring | 0.51 proposed | **0.410**: the rim torus reaches r 5.400, the blade edge is r 5.810 | `evBox3d` on a rim torus |
| **Land between neighbouring valleys** | (unresolved problem) | **0.05305 mm** | `evDistance` from the 0° rim torus to every other torus |
| **Thinnest wall in the part, and where** | — | **0.053 mm**, on the blade faces, between neighbouring valley rims at r 4.8. Next thinnest: the 0.410 rim between the valley ring and the blade edge, then the 1.000 web between the two pocket floors | as above |
| Feature health | all OK | 15 features, all `OK`; 1 solid body; 161 faces | `featureStates`, `qAllSolidBodies` |

**The blade's corners land exactly on the Ø12 surface, and the model proves it two ways.** The
blade's two side faces are planes at x = ±5.81 but they span y = **−1.49797 … +1.49797**, not
±1.5 — the last 0.002 mm of each side is cylinder, so the corner is *on* the round stock. And the
Ø12 cylindrical face's box runs z −20.000 … **+0.078**, i.e. that face continues up past the top
of the round stock into the blade's corner region: after the `Limb` Add, the trimmed corner
patches and the limb's own cylinder are **one face**.

Volume ledger — every feature checked against a closed-form prediction before it was renamed:

| Feature | Δ volume | Predicted |
| --- | --- | --- |
| `Trim blade to limb` (inherited) | −0.000013 | the four corner slivers |
| `Limb` (inherited) | → 1942.98845 | 372.06646 + 1570.85841 = 1942.92487 (the difference is the blade/limb overlap) |
| `Ball stud` | **+121.55244** | 121.5510 |
| `Pocket` | **−3.80133** | 3.80133 |
| `Detent valley` | **−0.35343** | 0.35343 |
| `Break the valley rim` | **−0.00704** | run 3's hinge measured 0.00706 for the same break |
| `24 detent valleys` | **−8.29086** | 23 × 0.360469 = 8.29079 — proof of 24 real, non-overlapping instances |
| `Mirror the blade features` | **−12.45266** | 12.45266 |
| **Final** | **2039.63557 mm³** | |

### The land is 0.053 mm here too

The launch warned that run 3's hinge measured a 0.053 mm land between neighbouring valleys and
told me to build to the brief's numbers anyway. I did. **My own measurement is 0.05305 mm** —
`evDistance` from the 0° valley's rim torus to every other torus face on the body, which returns
the closest approach, and the closest neighbour is the 15° valley.

The arithmetic behind it: at r 4.80 the 15° pitch gives an arc of 1.2566 between centres; each
valley's Ø1.0 bore plus its r0.10 break eats 0.60 of radius, so 1.2566 − 1.2 = 0.0566 nominal
chord-to-chord, and 0.053 measured across the true circular geometry. **No 0.4 mm nozzle will
form a 0.053 mm land.** It is not a build error and it is not new: it is the same number the
hinge got, so it is a property of "24 teeth at 15° on a Ø9.6 pitch circle", not of the stock the
blade is cut from. Building it onto Ø12 round stock did not change it.

## What did not work

1. **The Fillet swallowed a face I never meant to pick.** At the zoom needed to see one valley,
   the blade fills the whole canvas, so my usual "click empty space to clear the selection" click
   at (600, 850) landed *on the blade* and the dialog read
   `Entities to fillet | Face of Blade blank | × | Edge of Detent valley | ×`. I cancelled,
   clicked genuinely empty canvas at (1530, 900) outside the Ø12 silhouette, and re-picked only
   the edge. **Read the entity list back after every pick** — the preview looked fine both times.
2. **Applying the Ø1.0 dimension moved the valley circle.** Dimensioning the diameter pulled the
   under-defined centre from ~4.8 mm down to 1.52 mm above the axis, so my next pick — aimed at
   where the centre *had been* — hit nothing and Onshape said *"A dimension cannot be created
   between these items."* Fix: re-read the centre's pixel position from the screenshot, re-pick,
   and confirm from the dimension box's pre-fill (`1.52163 mm`) that the pick landed on the
   circle before typing 4.8. **The pre-fill is the receipt that the pick was right.**
3. **Renaming typed into the tree's filter box.** My rename helper took "the first visible input
   at x < 400", which is the *Filter by name or type* box, not the rename editor. The first
   rename silently did nothing and I only found out when the Revolve dialog said
   `Face of Sketch 1`. Fix: choose the input **nearest the row you right-clicked**; then clear the
   filter box, which was left holding `Ball stud profile` and hiding most of the tree.
4. **`Features to pattern` and `Features to mirror` never read back.** Both fields kept reporting
   `<none>` after every successful tree click, unlike every other field in Onshape, which reads
   back cleanly. I had to accept both features blind and prove them afterwards from the volume
   delta. That is the one place in this build where "assert the field" was not available.
5. **The stored feature parameters lie about numbers.** `GET .../features` reported the pattern
   as `{"angle": 0.0, "instanceCount": 0.0}` and the `Limb` extrude as `depth: 0` — expression
   -valued fields come back as 0. Do not verify a dimension from stored parameters; verify it
   from geometry.
6. **`GET .../features` started returning 429** ("Too many requests") immediately after the Mirror
   accepted, while `massproperties`, `featurescript` and `parts` all kept working. Rate limiting
   is per-endpoint. I renamed the last feature through the GUI and stopped polling that endpoint;
   it recovered a few minutes later.
7. **`input[placeholder^='Search tools']` does not resolve as an input.** The documented way in to
   Circular pattern did not work; the flyout caret at (x + w + 9, y + 16) on the pattern
   split-button does.
8. **Mirror's `patternType` is not a `<select>`** even though Circular pattern's is. Click the row
   and then click `Feature mirror` by text — and take the **last** match, because the closed row
   itself matches the same text.
9. **`n` (normal to) gave me the *Back* view once and *Front* another time on the same plane.**
   Harmless here — everything I sketched sits on the vertical axis — but on a handed feature it
   would have flipped the part. Read the view cube after pressing `n`.
10. **Two steps have no after-screenshot.** `Pocket` and `Detent valley` were driven by a script
    that shoots before accepting; their evidence is the volume delta and the final renders. Said
    plainly rather than dressed up.
11. **FeatureScript friction, for the next agent:** `roundToPrecision` refuses a
    `ValueWithUnits`; a `Torus` has no `majorRadius` (its keys are `coordSystem, minorRadius,
    radius, surfaceType`) and `minorRadius` is already a plain number in metres, so dividing it by
    `millimeter` yields a unit blob instead of a number; and error notices sit at
    `notices[i].message.level`, so a naive check swallows them and you get an empty result with no
    error. Also `qEverything(EntityType.FACE)` includes the default construction planes and sketch
    regions — use `qOwnedByBody` or your plane count is wrong.

## What the brief never said, that I had to decide

| Question | What I chose | Why |
| --- | --- | --- |
| How far the ball stud's stalk runs **into** the limb | stalk top at **z = −19**, i.e. 1.0 mm of overlap inside the limb (bottom face z = −20) | `ball-and-socket.md` builds the stud on a scaffolding base and never says; 1.0 is enough to weld the revolve to the limb without eating into the socket's swing |
| Whether to build the **pocket** at all | built it | The launch's "what is left" list named only the ball stud and the valleys, but `hinge.md` was assigned to me and a blade with no pocket cannot snap onto the clevis stubs. The 1.0 web is also a headline number, and the pocket's rim edge is the pattern axis run 3 proved works |
| Version name | `run3-limb-blade-ball-complete` | matches run 3's `run3-hinge-stage2` convention |
| Where the round stock starts (**inherited**) | z = −6.11 | see below |

**The two briefs disagree about the limb, and the inherited build followed the right one.**
`limbs.md`'s suggested order says "extrude 24 downward"; `hinge.md` says the limb rod stops
**6.11 mm from the hinge axis**. My predecessor built the limb as depth 13.89 with a 6.11
starting offset, so the Ø12 round stock runs z = −6.11 … −20 and the blade occupies everything
above it. That follows `hinge.md`, and `limbs.md` labels its own build order "our best guess, not
a tested path", so the conflict resolves cleanly — but it means **"12.000 across X and Y over the
limb's whole length" cannot mean "the section is a Ø12 circle for 24 mm."** It can only mean
*nothing stands outside Ø12 anywhere*, which is what I measured. Someone should reword that check
in `limbs.md`; as written, a reader would expect round stock where the blade is.

## Four limbs, two parts — report, not action

**I found no reason the forearm and the shin cannot be the same part, and one extra reason they
can.**

- The brief's own inputs make them identical: `#armSeg` = `#legSeg` = 24, the limb is Ø12 for
  both, the elbow and knee are the same hinge, and the wrist and ankle are the same ball stud.
  Nothing in this part references an arm or a leg. The name `Forearm and shin` on the single part
  is not a convenience — nothing in the 15 features distinguishes them.
- **The part has no handedness.** It is symmetric about the Front plane by construction (the
  Mirror), and it is also symmetric about the Right plane: the valley ring is 24 at 15° starting
  at 0°, so reflecting x → −x maps every valley onto another valley. One printed part can serve
  the left or right side, at the elbow or the knee, without a mirrored variant. That is 4 prints
  of 1 part, not 2 prints of 2.
- The only way they could diverge is a **load** argument, not a geometry one: a shin carries the
  robot's weight and a forearm does not, so if the ball stud or the 0.053 mm land turns out to be
  the weak point, someone may want a thicker leg. Nothing in this model forces that, and it
  cannot be settled with a measurement.

One thing worth flagging for the assembly, from arithmetic on brief numbers (**not** something I
measured): with the ball centre at z = −24 and the socket's cavity centre sitting `grip` = 1.35
below its mouth face, the mating socket's mouth lands at z = −22.65, which is 2.65 mm clear of
this limb's bottom face at z = −20. The neck between them is Ø3 over that whole span, so the
swing is limited by the stalk against the Ø5.803 mouth rim and not by the two limbs colliding.

## Retrospective

**What went well.** Taking over a dead agent's document cost me about eight minutes: verify the
inherited state through read-only REST first, read its log end to end, and *judge* the unfinished
sketch rather than rebuilding it. The judgement was worth making explicitly — the sketch was
correct but under-defined by one DOF, and the one number it was missing (z = −18.90418) was
visibly arbitrary, which is exactly the evidence needed to decide "keep, add one dimension"
instead of "redo".

The habit that carried the whole run is the one run 3's hinge invented: **predict the volume
delta in closed form before accepting a feature, then compare.** Eight features, eight matches to
five decimal places. It is the only check that catches an empty merge scope, a cut in the wrong
direction, and a pattern that made 24 overlapping copies of one valley, and it costs one line of
arithmetic. The launch's warnings — empty merge scope silently no-ops, `Equal spacing` makes the
angle a total sweep, the break goes on the edge not the bore — were all real and all saved time.

**What went poorly.** I typed a rename into the tree's filter box and did not notice until two
steps later, when a dialog labelled its input `Face of Sketch 1`. My selector was "first visible
input at x < 400", which is lazy: the tree filter is always there and always matches. I also lost
a Fillet to a deselect-click that landed on the part, because at that zoom there was no empty
canvas where I was clicking. Both are the same mistake — assuming a coordinate or a selector
means what it meant last time, instead of reading back what the UI now says.

**What I would change.**

- *In the brief:* `limbs.md`'s acceptance check "12.000 across X and Y over the limb's whole
  length" reads as "the limb is round stock for 24 mm", which contradicts `hinge.md`'s "each limb
  rod stops 6.11 from the axis". Reword it to *nothing outside Ø12 anywhere along the part*. And
  `limbs.md`'s build order ("extrude 24 downward") should say it is superseded by the joint
  briefs at each end.
- *In the brief, second:* the ball stud's **stalk length into the limb** is unspecified. Every
  limb with a ball stud will need that number; someone should pick it rather than each agent
  choosing 1.0 in the dark.
- *In the how-to:* add the rename trap (the tree filter box is an input and it comes first), the
  Mirror-vs-Circular-pattern `patternType` inconsistency, and that `Features to pattern` /
  `Features to mirror` do not read back at all, so a volume check is the only proof.
- *In how I was briefed:* the launch was unusually good — it told me what my predecessor had
  done, what to verify rather than trust, which warnings were fresh from tonight's hinge build,
  and that the land problem was known and not mine to fix. The one thing I would add for a
  pickup brief: say whether the dead agent's *decisions* are binding. I inherited a limb built to
  `hinge.md`'s set-back rather than `limbs.md`'s 24 mm extrude, and I had to work out for myself
  that this was correct rather than a mistake to undo.
