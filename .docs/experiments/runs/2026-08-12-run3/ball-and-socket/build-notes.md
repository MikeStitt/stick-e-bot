# Ball and socket — run 3 build notes

Built from [`../../../build-briefs/ball-and-socket.md`](../../../build-briefs/ball-and-socket.md)
on 2026-08-12, following it literally. The brief is what was under test.

## Where the work is

| | |
| --- | --- |
| Document name | `ball-socket-run3` |
| Document id | `c440cc33212eb2d5e01d2312` |
| Element (Part Studio 1) id | `728bf1bcb5566d41cc0e1cd0` |
| Version name | `ball-socket-run3-2026-08-12` |
| Version id | `92d8dbc62cfe1cf3bf8800bc` |
| Version link | https://cad.onshape.com/documents/c440cc33212eb2d5e01d2312/v/92d8dbc62cfe1cf3bf8800bc/e/728bf1bcb5566d41cc0e1cd0 |
| Workspace link (**live**, moves) | https://cad.onshape.com/documents/c440cc33212eb2d5e01d2312/w/cc55e05877256cf7b8e2ce84/e/728bf1bcb5566d41cc0e1cd0 |

**I opened both links**, in the browser page this run drove, and screenshotted what came
back. The version link opens with the banner "Versions are view only. Viewing
ball-socket-…", 14 features and 2 parts (`33-b-done-version-link-open.png`); the workspace
link opens the live Part Studio (`33-b-done-workspace-link-open.png`). The version was
published before this file was written.

Workspace units were set to millimetre with 5 decimals (`05-b-done-units-set.png`) before any
geometry was drawn.

## The click path that actually worked

Numbers in brackets are screen coordinates that had to be used because the control does not
resolve as a selector. Screenshot names follow each step.

1. **New document.** Documents page → the **visible** `Create` button (`01-a-select-documents-page.png`)
   → `Document...` clicked by coordinate at (65, 100) (`02-a-select-create-menu.png`) → name
   `ball-socket-run3` → `Create` (`03-b-done-document-created.png`).
2. **Units.** Hamburger left of the document name → `Workspace units…` → Length `Millimeter`,
   decimals `0.12345` → green tick at (543, 93). `04-b-done-workspace-units-dialog.png`,
   `05-b-done-units-set.png`.
3. **Ball stud profile.** `Sketch` at (155, 58) **first**, then click `Front` in the tree into
   the empty Sketch-plane field. `n`, check the view cube. Arc dropdown caret (383, 58) →
   `Center point arc` (located by text, clicked by its bounding box) → centre on the origin,
   swept through +X. Then `LINESEGMENT` (202, 58) for the stalk and base, closing on the
   vertical axis. `06-b-done-sketch-on-front.png`, `07-b-done-arc-drawn.png`,
   `09-b-done-profile-drawn.png`.
4. **Dimensions** with `DIMENSION` (970, 58): arc radius 3, stalk half-width 1.5, base bottom
   at 8, base top at 18, base half-width 5. `10-b-done-dim-*.png`,
   `10-x-profile-dimensioned.png`. The selected region read **Area 71.83242 mm²** against a
   closed-form 71.832417 mm² — proof the profile is at nominal, stronger than curve colour.
5. **Revolve** reached through the `Search tools` box (alt/⌥ c), profile region preselected,
   axis = the profile's vertical line, full revolve, `New`. Renamed `Ball stud`.
   `12-a-select-profile-region.png`, `13-b-done-revolve-accepted.png`.
6. **Limb stub profile.** Sketch on `Top`, **Disable imprinting** left ticked (it is on by
   default), Ø12 circle on the origin. `15-x-disable-imprinting.png`,
   `16-a-select-circle-drawn.png`.
7. **Limb stub.** Extrude, region picked, then click **New** (see below), Depth 10, tick
   `Starting offset`, offset depth 4.15, then **two** flips — the main direction arrow beside
   the `Blind` dropdown at (452, 220) and the starting offset's own arrow on its **Depth** row
   at (450, 372). Bounding box then read z −14.150 … −4.150. Renamed `Limb stub` / part
   `Socket body`. `17-a-select-extrude-region.png`, `18-a-select-offset-flipped.png`,
   `18-b-done-extrude-accepted.png`.
8. **Collar profile.** Sketch on `Top`, Ø9.4 circle on the origin. `20-a-select-collar-circle.png`.
9. **Socket collar.** Extrude the collar region, remove the auto-added `Face of Limb stub` from
   the entity list with its `×`, switch to **Add**, replace the auto-filled merge scope
   (`Ball stud`) with `Socket body`, Depth 1.35, tick **Second end position** and set it 4.15.
   `21-a-select-collar-region.png`, `21-a-select-merge-scope-socket-body.png`,
   `21-b-done-collar-added.png`. Socket body volume before the Boolean: **1512.661155 mm³**.
10. **Boolean → Subtract.** Search tools → `Boolean`; it opens on **Union**, click `Subtract`
    at (325, 110). Tools = `Ball stud`, Targets = `Socket body`, tick `Offset`, tick
    `Offset all`, `Offset distance` 0.2, leave `Reapply fillet` unticked, tick `Keep tools`.
    `22-a-select-boolean-subtract.png`, `23-a-select-boolean-zoom3.png`,
    `23-b-done-boolean-subtract.png`. Renamed `Socket cavity`.
11. **Slit profile.** Sketch on `Top`. Corner rectangle (254, 58) drawn **in clear space** to
    the right of the part, then dimensioned into position in this order: width 3.5 →
    origin-to-left-edge 2.5 → X-axis-to-top-edge 0.4 → X-axis-to-bottom-edge 0.4. Curves went
    black (fully defined). `25-b-done-rect-drawn.png`, `26-b-done-slot-defined.png`.
12. **Relief slit.** Extrude with the sketch still selected (the dialog opened already holding
    `Faces of Slit profile`), switch to **Remove**, Depth 5.5, tick `Starting offset`, offset
    depth 1.35, **leave `Merge with all` unticked** and set `Merge scope` = `Socket body`.
    No flip was needed — it arrived running the right way. `27-a-select-extrude-scope3.png`,
    `27-b-done-slit-extrude.png`. Renamed `Relief slit`.
13. **Circular pattern ×4.** Search tools → `Circular pattern`; it opens as **Part pattern**.
    Dropdown at (300, 110) → `Feature pattern`. `Features to pattern` = `Relief slit`.
    `Axis of pattern`: the `Top` plane from the tree was refused; the limb's cylindrical face,
    clicked in the graphics area, was accepted as `Face of Limb stub`. Angle 360°, count 4,
    equal spacing. `29-a-select-axis-cylindrical-face.png`, `29-b-done-circular-pattern.png`.
    Renamed `Relief slits x4`.
14. **Version.** Left rail (20, 94) `Create version…`, name `ball-socket-run3-2026-08-12`,
    `Create`. `31-b-done-version-created.png`.

Final tree: `Ball stud profile`, `Ball stud`, `Limb stub profile`, `Limb stub`,
`Collar profile`, `Socket collar`, `Socket cavity`, `Slit profile`, `Relief slit`,
`Relief slits x4`. Parts: `Ball stud`, `Socket body`. `29-b-done-tree-named.png`.

## Acceptance measurements

Everything below was read off the built model — `boundingboxes` and `massproperties` for the
volumes and extents, and a read-only `featurescript` POST calling `evSurfaceDefinition`,
`evCurveDefinition`, `evBox3d` and `evLength` for the faces and edges. Nothing here is
arithmetic on the brief.

| Check | Wanted | Got | How |
| --- | --- | --- | --- |
| Parts | 2 | 2 — `Ball stud`, `Socket body` | `/parts` |
| Limb stub | Ø12.000 | cylinder r **6.000**, z −14.150 … −4.150 | face definition |
| Collar | Ø9.400 | cylinder r **4.700**, z −4.150 … +1.350 (5.500 long) | face definition |
| Step round the collar foot | 1.3 | **1.300** (6.000 − 4.700) | from the two radii above |
| Mouth | Ø5.803 | four arcs at r **2.9012928**, so **Ø5.8025856** | arc radius × 2 |
| Ball | Ø6.000, unchanged by the subtract | sphere r **3.000** centred on (0, 0, 0) | face definition |
| Cavity spherical face | r 3.200 | **3.200**, centred on (0, 0, 0) | face definition |
| Cavity volume | 109.48 mm³ (27.78 = upside down) | **109.4820 mm³** = 1512.661155 − 1403.179138 | mass properties before and after the Boolean |
| Slit depth | 5.5, z −4.150 … +1.350 | **8** side walls, every one z **−4.1500 … +1.3500** | face bounding boxes |
| Collar bottom edge | four arcs, not one circle | **four** arcs, r 4.700, 6.5818 long each | edge enumeration |
| Mating face | z = +1.35 | plane at z **+1.3500**, and nothing above it | face definition |
| Wall (brief: *proposed* 1.5) | 1.5 | **1.500** = 4.700 − 3.200, built, not adjusted | from the two radii |
| Retention (brief: 0.197) | 0.197 | **0.1974144** = 6.0000000 − 5.8025856 | from ball and mouth |
| Keep tools worked | ball survives | `Ball stud` volume **935.224936 mm³** before the Boolean, after the Boolean, and after the four slits — identical | mass properties, three times |

Supporting volumes: `Socket body` 1512.661155 → 1403.179138 (cavity) → 1394.914649 (one slit,
8.264489 mm³) → **1370.121181** (four slits, 33.057957 mm³). Four times one slit, exactly, so
the slits do not overlap each other.

One measurement was also taken in the GUI rather than through the API: clicking a mouth arc in
Top view put **`Point: X 2.05152 mm  Y 2.05152 mm  Z 1.35000 mm`** in Onshape's readout
(`32-b-done-mouth-arc-readout.png`). That point is on the mouth arc at 45°, so its radius is
√2 × 2.05152 = 2.90129 — the same number the API gives — and its Z confirms the mating face at
1.35 in the interface itself. I did **not** additionally take a GUI dimension readout of the
arc's radius: at the largest zoom the wheel would give in Top view the mouth was about 60 px
across, and picking one specific arc reliably at that size was not worth the time. The arc
radius above is a read of the built edge, not an inference from the brief.

## Render it and look at it

Every part rendered alone with `shadedviews`, four views each: `30-x-render-<part>-<view>.png`.
I opened them.

- **`Socket body`, isometric.** Round limb stub at the bottom; the collar stands proud of it
  with a visible step all the way round; four tabs separated by four slits that run the collar's
  whole length down to the step; the spherical cavity is visible inside with the mouth at the
  top. The collar does stand proud, the slits do run the full length, and the mouth looks like
  something a ball could be pushed into — it is a hole narrower than the sphere behind it.
- **`Socket body`, top.** Two concentric circles (Ø12 and Ø9.4), the mouth broken into four
  arcs by four slits, cavity behind. Round, not square.
- **`Socket body`, front.** The slit is visible running from the top face down to the collar
  foot. This is the view that would have caught a half-depth cut.
- **`Ball stud`, isometric.** Ball at the bottom, stalk rising from it, base at the top.
  The stalk goes up, away from the socket, as the corrected brief requires.

**Against `images/brief-socket.png`: the same shape.** The drawing shows a Ø12 limb with a
narrower round collar standing proud of it, a spherical cavity opening upward through a mouth
narrower than the cavity, and the stud drawn lifted clear above with its stalk pointing away
from the socket. That is what the renders show, in the same proportions. Nothing in the model
is square, and nothing sits above the mating face.

## What did not work

1. **Brief step 1 has the join upside down.** It says "Make the arc's **lower** endpoint
   coincident with the top of the stalk". With the stalk running upward from the ball it is
   the arc's **upper** endpoint that meets the **bottom** of the stalk. Leftover from the
   version that had the stud the wrong way up. I built the correct join.
2. **The Extrude "Direction" checkbox is not a flip.** Ticking it produced a red ERROR
   feature; `/features` showed `hasExtrudeDirection: true, extrudeDirection: null` — it is a
   *custom direction reference* selector waiting for a pick. The flip is the small arrow beside
   the `Blind` dropdown. Cost about three minutes and two attempts.
   `18-x-direction-unticked.png`.
3. **A starting offset has a second, separate flip**, and it is on the offset's **Depth** row,
   not its `Blind` row. Clicking the `Blind` row did nothing at all. After the main flip the
   stub sat at z −5.85 … +4.15; after the offset flip, −14.15 … −4.15. Three attempts.
   This is why the how-to's rule — check a bounding box after any extrude with a starting
   offset — earns its place.
4. **Extrude flips itself from `New` to `Add` the moment a sketch region is picked**, and
   auto-fills the merge scope with whatever part is nearby (`Ball stud`, both times). The
   operation button has to be set *after* the region, and the auto-filled scope has to be
   replaced.
5. **`Merge with all` is unticked by default on a Remove extrude**, with `Merge scope` shown
   below it. I clicked the label expecting to untick it and instead ticked it, which made the
   `Merge scope` field disappear. One wasted round trip.
   `27-a-select-extrude-scope2.png`.
6. **Onshape's checkboxes are not `input[type=checkbox]`.** Querying for them inside a dialog
   returns an empty list, so tick state cannot be read programmatically at all — only from a
   cropped screenshot. Worse, clicking about 9 px left of a label (where the box is drawn)
   *focused* `Keep tools` without toggling it, and the focus ring looks enough like a tick at a
   glance to fool you. Clicking the **label text** toggles it reliably. Two attempts, and it
   would have silently consumed the ball if I had not cropped and looked.
   `23-a-select-boolean-zoom2.png` (focused, empty) vs `23-a-select-boolean-zoom3.png` (ticked).
7. **Switching `Part pattern` → `Feature pattern` reshuffles every row upward.** Coordinates
   read from the dialog before the switch land one field off afterwards; my first pick of the
   feature went into `Axis of pattern` instead, where it was silently ignored.
8. **A dimension moves the geometry, so pixel coordinates go stale immediately.** Two of the
   four slot dimensions failed on the first attempt because the entity had moved out from under
   the click. The error text differs usefully: "A dimension cannot be created between these
   items" means it picked something odd; "A constraint must involve something from the sketch"
   means only the default X axis got picked — the origin axes do not count as sketch entities
   on their own, though they are fine as the *second* pick.
9. **`XSRF-TOKEN` is base64 with `==` padding.** Parsing it as `cookie.split('=')[1]` silently
   truncates the padding and every `featurescript` POST returns **401 with an empty body** —
   which reads exactly like a dead session. Keep everything after the first `=`. This cost
   about four minutes chasing a session that was fine.
10. **No Onshape session at the start.** `/api/users/sessioninfo` returned 204 and
    `/api/users/current` 401; the only `/`-path cookie was `on-session-id`, with every auth
    cookie path-scoped to `/btwssm/<docid>`. Two sibling agents were stuck the same way.
    `tools/agent_browser.py` borrows cookies from port 9222, which this run was forbidden to
    touch, so I logged the blocker loudly and started a bounded poller instead of guessing. The
    session was restored externally about 90 seconds later and the build went ahead.
11. Smaller ones, all already in the how-to and all confirmed again: `Sketch` does not resolve
    as `button:has-text('Sketch')`; the sketch opens with an **empty** plane field even when the
    plane was preselected; the arc flyout's items carry no `data-command-id` so they have to be
    found by text; double-clicking a tree item **reopens** it for edit rather than renaming, and
    `text=Rename` also matches a hidden element; `n` gave the *Bottom* view once (view cube read
    "Bottom", mirrored); clicking the view cube's Top face resets the zoom.

Nothing in the design failed. The offset Boolean worked first time and applied uniformly, as
run 2 found.

## What the brief never said

- **The ball stud's base.** The brief dimensions the ball, the stalk and the fit, but not the
  lump the stalk is attached to. I used **Ø10 × 10 long, z 8 … 18**, matching run 2's stud, and
  recorded it here rather than picking silently.
- **Which plane the collar circle is sketched on.** Step 4 says "extrude it from the stub's top
  face up to z = +1.35", which reads as a sketch on that face. `.parts/onshape.md` says sketch
  on planes over faces, so I sketched on `Top` and used **Second end position** — 1.35 up and
  4.15 down from z = 0 — which lands the same solid without depending on a face.
- **The slit's radial extent.** Step 6 gives width 0.8 and length 5.5 and nothing else. The
  inner end **must** sit inside the mouth radius (2.901) or the mouth never opens and the
  acceptance check "four arcs, not a circle" cannot pass; I used **inner 2.5, outer 6.0**, the
  outer end chosen to clear the collar's Ø9.4 and stop exactly at the limb's Ø12.
- **That the slit's Remove needs a merge scope.** Because the slot has to reach in to radius
  2.5, and the ball is radius 3.0, the slot passes through the ball's space. A Remove extrude
  merged with all parts would cut four slots in the `Ball stud` as well. I set
  `Merge scope = Socket body` before accepting rather than building the failure first, so I am
  reporting the geometry, not an experiment: the slot's inner face at x = 2.5 is inside the
  ball, and the `Ball stud` volume is unchanged at 935.224936 mm³ after the cut.
- **`Reapply fillet`.** The Boolean's Offset section shows `Offset all`, `Faces to offset`,
  `Offset distance`, **`Reapply fillet`** and `Keep tools`. The brief lists all but the fourth.
  Left unticked, as run 2 did.
- **The stretch question, answered:** the circular pattern **does** need the axis picked
  explicitly, and it will not take a default plane. Offering it the `Top` plane from the tree
  did nothing at all — the field stayed empty and **no error was shown**, which is the
  dangerous part. It accepted a **cylindrical face** picked in the graphics area, reported as
  `Face of Limb stub`. That confirms run 2 and adds that the refusal is silent.

## Retrospective

**What went well.** Measuring rather than looking. Every direction decision in this build was
settled by a bounding box or a face definition, and the two that were wrong were wrong in ways
that looked completely fine in the viewport. The three checks the brief singles out — cavity
volume, slit z-extent, collar foot as four arcs — all passed on the first accept, which I think
is because the brief's own warnings had already told me exactly which two things to distrust.
Reading a dimension box's **pre-filled** value before overwriting it also worked well as a free
screen-to-millimetre calibration; it caught the moment geometry moved under a stale coordinate.

**What went poorly.** I lost the most time to things that were invisible rather than hard: a
checkbox that was focused but not ticked, an axis field that refused a plane without saying so,
and a 401 that was my own base64 parsing rather than a dead session. All three share a shape —
the interface gave no signal, so the only defence was to crop a screenshot and look at it.
I also drew the slot rectangle into clear space and dimensioned it home, which was the right
call, but I recomputed pixel positions by eye from screenshots three times when I should have
just zoomed in once at the start.

**What I would change.**

- **The brief:** fix "lower endpoint" to "upper endpoint" in step 1; add `Reapply fillet` to
  the step-5 list; say which plane the collar circle is on; give the slit a radial extent, or
  at least say the inner end must sit inside the mouth radius; and add one line to step 6
  saying the Remove needs `Merge scope = Socket body` because the slot passes through the
  ball's space. Also give the ball stud's base a size, even a throwaway one, so two runs do
  not draw different studs.
- **The how-to:** three additions. That Onshape checkboxes cannot be read from the DOM and must
  be confirmed from a cropped screenshot, and that clicking left of the label focuses without
  toggling — click the label text. That the `XSRF-TOKEN` cookie is base64 with `==` padding and
  `split('=')[1]` truncates it into a silent 401. And that a starting offset has its own flip
  arrow on its **Depth** row, not its `Blind` row — the existing note about flipping direction
  last does not mention there are two of them.
- **The way I was briefed:** the launch was good, and the instruction to make the page stamp
  unique would have saved me a wrong-page navigation — two stale pages already carried
  `BALLSOCK_RUN3` from an earlier incarnation, and `window.name` lookup happily returned one of
  them. A stamp should carry a per-session suffix. Beyond that: being told plainly that nobody
  was awake made the blocked-session decision easy. I logged it loudly, started a bounded
  poller instead of a guess at 9222, and got on with what I could. That is the right shape for
  a rule, and it worked.
