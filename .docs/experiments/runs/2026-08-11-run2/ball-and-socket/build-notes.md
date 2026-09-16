# Ball-and-socket — run 2 build notes

Built 2026-08-11 by driving the Onshape GUI over CDP. Everything below was performed; where a
number is quoted it was measured, and the measurement route is named.

## Where the work is

| | |
| --- | --- |
| Document name | **ball-socket-run2** |
| Owner | Spires Robotics (signed in as Mike Stitt) |
| Document id | `b58c15803eb989fe3f676150` |
| Element (Part Studio 1) id | `f2b99ffa760d66d00534d1cb` |
| Workspace id | `6b00a528e8d48f5d5c862785` |
| Published version | **v1-ball-and-socket**, id `278e2c9bf3329c2d7f1244f4` |

- **Version link (cite this one):**
  <https://cad.onshape.com/documents/b58c15803eb989fe3f676150/v/278e2c9bf3329c2d7f1244f4/e/f2b99ffa760d66d00534d1cb>
- **Workspace link — LIVE, this moves:**
  <https://cad.onshape.com/documents/b58c15803eb989fe3f676150/w/6b00a528e8d48f5d5c862785/e/f2b99ffa760d66d00534d1cb>

**I opened both links**, in the automation browser, signed in as the document's owner. The version
link loads with the banner *"Versions are view only. Viewing v1-ball-and-…"* and the document
subtitle reads `v1-ball-and-socket` (screenshot `47-b-done-version-link-open.png`); the workspace
link loads the editable Part Studio (`48-b-done-workspace-link-open.png`). I did **not** test either
link from a student account or a signed-out browser, so the *Links resolve* gate is only half met.

The version was published **after** the last geometry change and after all features were renamed.

Workspace units were set to **millimetre**, display decimals `0.12345`, and that was confirmed
independently by `GET /api/documents/d/…/w/…/elements` returning `lengthUnits: millimeter`.

## What it looks like

Render every part on its own — this is the section that would have caught run 1, and it caught a
real defect here too (see *The slits were 2.7 mm, not 5.5 mm*).

| File | What it shows |
| --- | --- |
| `40-render-socket-isometric.png` | Socket alone: pad, collar standing proud, four tabs, cavity |
| `40-render-socket-top.png` | Down the axis: mouth, four slits, concave sphere below |
| `40-render-socket-front.png` | One slit running the full collar height down to the pad face |
| `40-render-socket-bottom.png` | Underside of the pad (plain) |
| `41-render-ballstud-isometric.png` / `-front.png` / `-bottom.png` | Ball stud alone |
| `42-render-both-isometric.png` | Assembled: ball captured, stud exiting upward |
| `43-b-done-section-front.png` | GUI section on the Front plane through the joint |

**What I actually see, in words:**

- The collar **does** stand proud of the pad — clearly, by about its own diameter's worth of
  height. It is not flush and it is not sunk.
- The four slits **do** run the whole length of the collar, top face to pad face. In the front
  render the slit is an unbroken gap from the top edge of the collar down to the pad surface. They
  divide the collar into four separate tabs that are attached only at the pad.
  *This was not true on the first attempt* — see below.
- The mouth looks like something a ball could be pushed into: the top view shows a round opening
  with a concave spherical surface visible through it, and the opening is visibly smaller than the
  sphere behind it. The four slits open into the cavity at the mouth, so the tabs can spread.
- In the section, the ball sits in the cavity with a thin visible gap all round, and the socket
  material clearly continues *above* the ball's equator on both sides. That is the retention.
- The assembled isometric shows only the top of the ball and the stalk above the tabs — the ball is
  swallowed, not sitting in a dish.
- One thing that reads oddly at first in the isometric renders: the large rounded shape in the
  middle-front is the **near tab**, not a plug. In an isometric projection the nearest tab's top
  edge lands lower on the image than the side tabs' tops. Checked against the top view and the
  section; there is no extra solid in there.

## Numbers, and how each was got

Two routes were used: the graphics-area readout (§7 of the how-to) and read-only REST
(`massproperties`, `boundingboxes`, and `POST …/featurescript` evaluating `evSurfaceDefinition`,
`evCurveDefinition`, `evVolume`, `evArea`). Nothing here is inferred.

| Check the brief asked for | Target | Measured | How |
| --- | --- | --- | --- |
| Parts | 2 | 2 — `Ball stud`, `Socket body` | Parts list + `GET /parts` |
| Ball diameter, unchanged by the subtract | 6.000 | **6.000000** (sphere r = 3.000000) | FeatureScript `evSurfaceDefinition` |
| Cavity spherical face radius | 3.200 | **3.20000 mm** | GUI readout, face selected (`45-b-done-measure-sphere.png`) |
| Cavity sphere radius (again) | 3.200 | **3.2000000** | FeatureScript |
| Cavity sphere centre | origin | **(0, 0, 0)** to 1e-15 | FeatureScript |
| Mouth diameter | 5.803 | **Ø5.802586** (arc r = 2.9012928) | FeatureScript |
| Mouth, one arc, GUI route the brief describes | — | **Radius: 2.90129 mm** → Ø5.80258 | GUI readout (`46-b-done-measure-mouth-arc.png`) |
| Mouth is four arcs after slitting | 4 | **4** arcs at r = 2.9012928, z = +1.35 | FeatureScript edge query |
| Cavity volume | brief says ≈124.6 | **109.482 mm³** | difference of two `massproperties` calls |
| Retention (ball − mouth) | 0.197 | **0.197414 mm** | 6.000000 − 5.802586 |

Bounding boxes (`GET …/boundingboxes`, mm):

- `Ball stud` — X −5.000 … +5.000, Y −5.000 … +5.000, Z **−3.000 … +18.000**
- `Socket body` — X −10.000 … +10.000, Y −10.000 … +10.000, Z **−10.150 … +1.350**

The socket's top is at exactly **z = +1.35**, the mating face, and all of its material is below it.

Volumes through the build (`massproperties`, mm³):

| Stage | Socket body | Ball stud |
| --- | --- | --- |
| Pad + collar, before the Boolean | 2781.6878 | 935.2249 |
| After Boolean Subtract with 0.2 offset | 2672.2058 | 935.2249 |
| Final, four full-length slits | 2639.1478 | 935.2249 |

The ball stud's volume never changes — **Keep tools** did its job.

Both "before" figures match closed-form arithmetic to within the tolerance band the API itself
reports: pad + collar should be 20·20·6 + π·4.7²·5.5 = 2400 + 381.7035 = **2781.7035** (measured
2781.6878, and the API's own bracket for that call was 2781.49 … 2781.89). The ball stud should be
sphere 113.0973 + stalk cylinder 56.5487 − the lens where they overlap 19.8191 + base 785.3982 =
**935.2249** (measured 935.2249).

### The cavity volume: the brief's 124.6 mm³ is wrong

Measured cavity = 2781.6878 − 2672.2058 = **109.4820 mm³**.

Closed form: a Ø6.4 sphere is (4/3)π·3.2³ = 137.2583. The cap above the mouth plane has height
h = 3.2 − 1.35 = 1.85, so V_cap = πh²(3r − h)/3 = π·3.4225·7.75/3 = **27.7787**. Sphere less cap =
**109.4796**. Measured 109.4820 — agreement to 0.0024 mm³.

A second, independent confirmation from a different quantity: the cavity's spherical face **area**
measures **91.48318 mm²**. Full sphere area 4π·3.2² = 128.6796, cap area 2πrh = 2π·3.2·1.85 =
37.1955, difference **91.4841**. Both the volume and the area say the cavity is the sphere *less*
the cap.

So the socket is the right way up, unambiguously. But two figures in the brief's warning box need
correcting before anyone reuses them:

- the correct cavity volume is **109.48 mm³**, not 124.6;
- the upside-down failure would measure the cap, which is **27.78 mm³**, not ~13.

The rest of that warning is sound, and its central point held: the mouth measurement alone cannot
tell the two apart, and the volume can.

## Does Boolean → Subtract with Offset work on a sphere?

**Yes, and it is uniform.** This was the question the whole design rested on, and the answer is
clean:

- After the subtract the cavity is a **single spherical face**, not a patchwork.
- Its radius is **3.200000** everywhere on that face (both the GUI readout and
  `evSurfaceDefinition` agree), i.e. ball radius 3.000 plus the 0.2 offset exactly.
- Its centre is the origin to 1e-15 mm, i.e. exactly concentric with the ball.
- The mouth circle it produces, 2·√(3.2² − 1.35²) = 5.802586, is what came out.

The clearance is one number in one field, and the cavity cannot drift from the ball. The forum
reports of non-uniform offsets did not reproduce here, on a whole sphere, at 0.2 mm.

The dialog matched the brief's description — **Offset**, then **Offset all**, **Faces to offset**,
**Offset distance**, plus **Keep tools** — with one addition the brief did not list: a **Reapply
fillet** checkbox, which sits between *Offset distance* and *Keep tools*. I left it unticked.
Screenshot: `26-a-select-offset-ticked.png`, `26-a-select-offset-02.png`.

## The slits were 2.7 mm, not 5.5 mm — and every headline check still passed

This is the most important finding in the run.

The slit is a Remove extrude from a Top-plane sketch (z = 0), and it has to reach from z = +1.35
down to z = −4.15. I used **Direction 1 = Blind 1.35** and ticked **Second end position = Blind
4.15**. Both values committed correctly — I read them back out of `GET …/features` as
`depth: "1.35 mm"` and `secondDirectionDepth: "4.15 mm"`.

The result was still wrong, because the same feature carries **`oppositeDirection: true`**, set by
Onshape and never touched by me. Direction 1 therefore pointed **down**, and the second direction
pointed **up** — into empty air above the collar. The cut ran z = −1.35 … +1.35: 2.7 mm long
instead of 5.5.

**Nothing complained.** No error, no warning, no orange feature. And critically:

- the mouth was still cut into **4 arcs** of the right radius;
- the collar top face was still cut into 4 pieces;
- the mouth diameter still measured 5.802586;
- the cavity volume was still right;
- the part count was still 2.

Every acceptance check in the brief passed while the slits were less than half the required length
and the tabs were held rigid by an unbroken ring of collar below them. That is run 1's "decorative
slits", arrived at by a different route.

What caught it was measuring the **z extent of the cut faces**, not the cut's existence:

```
evBox3d on the slit side-walls  ->  zmin = -1.35   zmax = +1.35     (wrong)
```

and the tell-tale that the collar's **bottom** edge at r = 4.7 was still one full circle rather
than four arcs.

**Fix:** swap the two depths — Direction 1 (which points down) = 4.15, Second end position (up) =
1.35. After the edit:

```
slit side-wall count = 8   (2 per slit x 4)
each wall  zmin = -4.150   zmax = +1.350        -> full 5.500 mm
collar bottom edge at r 4.7 = 4 arcs, 0 full circles
```

**The check to write into the lesson:** after any two-direction or offset extrude, do not ask *did
it cut* — ask *where does the cut start and stop*. The bounding box of the cut face is the answer.

## Circular pattern: what it accepts as an axis

The brief asked. Tested, in the GUI, in this order:

1. The dialog opens as **Part pattern**. It must be switched to **Feature pattern** with the
   dropdown at the top before *Features to pattern* will take a feature.
   (`34-a-select-pattern-type-menu.png`)
2. **A default plane is rejected.** With *Axis of pattern* focused I clicked **Front** in the
   feature tree. Nothing was added — the field stayed empty and no error appeared.
   (`34-a-select-axis-try-plane.png`)
3. **A cylindrical face is accepted.** Clicking the collar's outer Ø9.4 face filled the field with
   `Face of Revolve 2` and the preview immediately showed four slits.
   (`34-a-select-axis-cyl-face.png`)

Angle 360°, Instance count 4, **Equal spacing** on — all defaults, nothing to change.
**Reapply features** was not needed; it built first time.

So: yes, the axis must be picked explicitly, and the thing to teach students to pick is a round
face on the part itself, not a plane. A sketch line and a straight edge were not tested.

## The feature tree as built

All ten authored features are named. (The tree header reads "Features (14)" because it also counts
the four default-geometry entries — Origin, Top, Front, Right.) Sketches are hidden, so they show
greyed in the tree. Every feature regenerates `OK`.

| # | Feature | What it does |
| --- | --- | --- |
| 1 | `Ball stud profile` (Sketch, Front plane) | Ø6 circle on the origin, a short axis line, stalk rectangle, base rectangle |
| 2 | `Ball stud` (Revolve, New) | 4 sketch regions, full revolve about the sketch's axis line |
| 3 | `Pad profile` (Sketch, Front plane) | 20 × 6 rectangle, symmetric about the Y axis, top face 4.15 below the X axis |
| 4 | `Socket pad` (Extrude, New, Symmetric 20) | the 20 × 20 × 6 pad |
| 5 | `Collar profile` (Sketch, Front plane, imprinting disabled) | 4.7 × 5.5 rectangle, left edge on the axis, top edge 1.35 above the X axis |
| 6 | `Socket collar` (Revolve, Add → Socket body) | the Ø9.4 × 5.5 collar |
| 7 | `Cavity = ball + fit` (Boolean Subtract) | Tools `Ball stud`, Target `Socket body`, Offset all 0.2, Keep tools |
| 8 | `Relief slit profile` (Sketch, Top plane, imprinting disabled) | 0.8-wide slot, r 2.5 → 6, symmetric about the X axis |
| 9 | `Relief slit` (Extrude, Remove) | Blind 4.15 down + second end 1.35 up, scope `Socket body` |
| 10 | `Relief slits x4` (Circular pattern, Feature pattern) | ×4, 360°, axis = collar's cylindrical face |

Every sketch is fully defined: all curves render black and the two solids' bounding boxes and
volumes come out exactly nominal, which is the practical proof. I did **not** find a
"fully defined" text readout in this Onshape build — I looked for one in the sketch panel and in
the page text and it is not there, so I am reporting the colour and the measurements, not a status
label.

Design intent, briefly: `grip` (1.35) and the collar length (5.5) are the two dimensions on the
collar profile; the pad's face position is derived from them. The clearance `fit` lives in exactly
one place, the Boolean's *Offset distance*. Nothing is placed by typed coordinates.

## Where I deviated from the brief, and why

1. **The stalk goes UP, not down.** Suggested build order step 1 describes "a base about 10 wide
   and 10 tall, a stalk of half-width 1.5 **rising from it**, and an arc of radius 3 centered on
   the origin" — base at the bottom, ball on top. That puts the stalk and base *inside* the socket,
   which the Geometry section forbids ("all the socket's material is below z = +1.35; the ball
   enters from above"). I built ball at the origin, Ø3 stalk from z = 0 to z = 8, Ø10 × 10 base
   from z = 8 to z = 18. **This is the same class of contradiction the brief itself warns about
   for the socket, one paragraph earlier, in the same document.** Worth fixing in the brief.
2. **The pad rectangle is 20 × 6, not 20 × 20.** Step 3 says "sketch a 20 × 20 rectangle … extrude
   symmetric 20 deep", which would give a 20 × 20 × 20 block, not the 20 × 20 × 6 pad the prose
   asks for. I sketched 20 wide × 6 tall on the Front plane and extruded symmetric 20. The result
   measures 20 × 20 × 6 with its top at z = −4.15.
3. **No arc in the ball profile.** The brief's step 1 wants an arc closed by lines, and warns
   (rightly) about arc endpoints. I used a full **Ø6 circle centred on the origin** plus a short
   vertical line from the origin down to the circle, which splits the circle into two halves; the
   revolve then takes the four regions on the +X side. The circle's centre snaps to the origin,
   which is a far more reliable click than an arc endpoint, and one diameter dimension defines the
   whole ball. If this becomes a lesson, teach the circle.
4. **Collar and slit sketches use "Disable imprinting".** Without it, the Front-plane collar sketch
   is cut by the imprinted outline of the ball and the single rectangle becomes several regions,
   which makes the revolve pick fiddly and ties the feature to an earlier solid. The checkbox is in
   the sketch dialog and it removed the problem completely.
5. **Ceiling work was not skipped**: the relief slits are in the main build, not left as stretch,
   because the brief's own acceptance check ("once the slits are cut this is four arcs") assumes
   them.

## Driving the GUI: what run 2 paid for that the how-to does not yet say

The how-to file is 208 lines / 12 KB — worth saying, since the task described it as 1.2 million
tokens; that is the cost of *producing* it, not its size. Reading it took two minutes and saved
much more. These are additions.

1. **A typed dimension value is silently discarded, intermittently.** It happened twice out of
   eleven dimensions. The edit box was open and focused, the value was typed into the real
   `<input>` (verified by reading `input_value()` back as `"6 mm"`), Enter was pressed — and the
   dimension committed at the *dragged* size (Ø61.28175, and 4.98956 where 5 was wanted). It is
   not the Escape-instead-of-Enter trap already documented; Enter was used. **Read the dimension
   label back off a screenshot after every dimension.** The repair is to double-click the label and
   retype, which worked every time.
2. **A dimension's label-placement click has a dead zone near the bottom of the canvas.** Placing a
   label at y = 955 in a 1000 px-tall window silently aborted the whole dimension — no input box
   appeared, no error, the tool just disarmed. The same dimension succeeded immediately with the
   label at y = 790. If a dimension "does nothing", move the label click inward before suspecting
   the entity pick.
3. **`n` is not deterministic on the same plane.** On the Front plane it gave a true **Front** view
   the first and third time and the **Back** view (view cube reading "Back", +X running left) the
   second time, in the same session, with no intervening rotation. Check the view cube after every
   `n`, every time. Everything here is symmetric about the axis so the mirrored pass was harmless,
   but it would silently mirror anything that is not.
4. **Keyboard shortcuts go to whatever you last clicked.** After clicking the *Disable imprinting*
   checkbox in the sketch dialog, pressing `g` did nothing at all — no rectangle tool, no error.
   Focus was still on the checkbox. Use the toolbar buttons by `command-id`
   (`RECTANGLE_TWO_CORNERS`, `LINESEGMENT`, `CIRCLE_CENTER_RADIUS`) rather than the shortcut when a
   dialog control was the last thing clicked.
5. **Calibrating screen-to-model without a probe sketch.** Draw the first circle roughly, dimension
   it to a known diameter, then measure it in pixels on the screenshot. The circle's centre gives
   the origin's screen position and its pixel diameter gives the scale, in one step, with no
   throwaway geometry. Wheel-zoom is about ×1.072 per notch (×2 per ten notches, measured).
6. **The sketch-inside-a-solid trap, confirmed and costed.** The slit sketch sits on the Top plane
   at z = 0, buried inside both parts. Clicking its region in the Extrude dialog picked *Face of
   Revolve 1* — a face of the ball stud — and Onshape then auto-populated the merge scope with
   `Ball stud`, i.e. it was one green tick away from cutting the wrong part. Hiding both parts made
   the region the only thing under the cursor. **Hide first, then pick.**
7. **Merge scope defaults are the opposite of what the how-to records, and still need setting.**
   On this build, Revolve→Add opened with **Merge with all unchecked** and *Merge scope* empty and
   red-outlined; Extrude→Remove the same. So the failure mode is a blocked feature rather than a
   silent weld — but the conclusion is unchanged: set the scope by hand every time.
8. **Extrude defaulted to New, not Add.** With one solid already in the studio, the Extrude dialog
   opened on **New**. The how-to says it defaults to Add once any solid exists. Do not rely on
   either; look at which of New / Add / Remove / Intersect is underlined.
9. **Multi-select for a constraint is shift+click**, and it worked first time for **Symmetric**
   (`shift+q`) with two edges plus an origin axis.
10. **A feature's committed values are readable, and worth reading.** `GET …/features` gives each
    quantity as `expression` (`"1.35 mm"`) with `value: 0` alongside — read `expression`, not
    `value`. That is how the direction bug was pinned down: the depths were right and
    `oppositeDirection: true` was the culprit.
11. **Left rail, top to bottom:** *Versions and history* (y ≈ 58), **Create version…** (y ≈ 95),
    *Comments*, *Document notes*, *Performance errors detected*, *AI Advisor*, *Action items*. The
    names come from hovering each and reading the tooltip. Create version… is its own button; you
    do not need to open the version graph.
12. **The view menu's "Section view…" accepts a default plane from the feature tree**, unlike the
    circular pattern's axis field. Turning it off is *view menu → Turn off section view*.

## Failures and unknowns, stated plainly

- **The slit length bug above was a real failure of my first attempt**, found only after the
  circular pattern was already built on top of it. It cost one feature edit to repair and the
  pattern regenerated without complaint.
- **I did not time anything.** No hands-on timing was clocked, so this run says nothing about
  whether the sequence fits a class block.
- **I did not follow these steps from an empty document.** These are notes on what happened, not a
  verified step file; the *Steps reproduce* gate is not met and should not be claimed.
- **I did not check the links from a student-level account** — only as the owner.
- **I did not find a "fully defined" status readout** in this Onshape build and did not verify
  sketch DOF any other way than by curve colour plus the exactness of the resulting solids.
- **The fallback design was not built**, correctly, because the offset worked.
- **Not tested as pattern axes:** a sketch line, a straight edge, a mate connector.
- **Not measured:** how far the tabs actually deflect, i.e. whether 0.8 mm slits in this material
  make the mouth openable in practice. That is a print-and-try question, not a CAD one.
- The base of the ball stud is Ø10 × 10 tall. The brief said "about 10 wide and 10 tall" about a
  profile drawn to one side of the axis, which could equally have meant Ø20. I chose Ø10 because it
  is close to the collar's Ø9.4 and looks like a stud, and it is a test fixture either way.

## Deliverables in this folder

- `steps.log` — 141 lines, an "about to" line before each action and a "result" line after.
- 118 screenshots, `NN-a-select-*.png` before each action and `NN-b-done-*.png` after.
- Seven server-side renders (`40-`, `41-`, `42-`), each part alone from three or more angles.
- This file.
