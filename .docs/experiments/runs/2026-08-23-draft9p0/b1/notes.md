# B1 build notes — stickbot-draft9p0

did 0f4b79a78707651ae20df5b2 · wid d7b87030a78288b62a42de72

| element | eid |
| ------- | --- |
| `body` (Part Studio) | 02e4961f71e6767fb7d7d639 |
| `robot sizes` (Variable Studio) | 97046dd200d2da1151f9008b |
| `Assembly 1` | 546a5e79d793ec8ac2bc902e |

## Tutorial 1 — variables and torso  DONE

- Workspace units: Millimeter / 0.12345. The dialog has no OK button; its green tick
  is at (543, 92) and the ☰ that opens the menu is at (155, 17), "Workspace units…"
  at (252, 236).
- **Two Variable Studios got made** — the first click reported "url unchanged" and
  looked like a miss, but it had worked; the retry made a second. Deleted the second
  through right-click → Delete on its tab. The survivor arrived with
  *Insert into all Part Studios and Assemblies* already ticked, as the how-to says
  the first one in a document does.
- **A Value cell took two double clicks only for the first row.** Rows 2, 3 and 4
  opened on one. The how-to's "two double clicks from cold" is about the table being
  cold, not the row.
- `robot sizes`: torsoH 96 mm, torsoW 72 mm, torsoD 48 mm, limbSeg 48 mm.
- `torso outline` on Front, center point rectangle on the origin, dimensioned
  `#torsoW` and `#torsoH` — both resolved and the sketch went fully defined.
- `torso block`: Extrude, New, Symmetric, `#torsoD`.
- Bounding box read back: X ±36, Y ±24, Z ±48 — **72.000 × 48.000 × 96.000**. Target.

## Tutorial 2 — the head

Built in the `head` Part Studio. Feature order as the plan has it: `head profile`,
`head body`, `upper rounds`, `lower head chamfer`, `eye profile`, `eye`, `second eye`,
`mouth profile`, `mouth`. One part, named `head`.

**Read back off the workspace.** Bounding box `lowX -36 / highX 36`, `lowY -33 /
highY 30`, `lowZ -36 / highZ 36` mm. 29 faces — 14 plane, 9 cylinder, 4 cone, 2 torus.
Volume 263585.819 mm³. Cylinder radii 36 (the arch), 12 (four vertical corner rounds),
10 (the two eye discs) and 5 (the two mouth end caps).

**The head is 72 across, 72 tall and 60 deep**, and the eyes stand 3.0 proud of the
front face at y = -30, so the box reads -33 in y.

### What the numbers came out as

| what | where it came from | value |
| ---- | ------------------ | ----- |
| head profile radius and length | `#torsoH * 3 / 8` | 36 |
| head body | blind symmetric | 60 |
| upper rounds | typed | r12 |
| lower head chamfer | `OFFSET_ANGLE`, 45 deg | 6 |
| eye circle | typed | Ø20 at x ±16, z +16 |
| eye stand-off | derived from the extrude | 3.0 proud |
| mouth slot | typed | 40 × 10, r5 ends, top edge 13 below centre |
| mouth depth | typed | 3.0 |

### Findings

**Chamfering the head's underside *face* fails, every time.** *"Could not chamfer smooth
edges."* Tried with `Distance and angle` and with `Equal distance`, with tangent
propagation on and off. Picking **one straight bottom edge with Tangent propagation ON**
works and carries the whole eight-edge loop. The same message appears if you pick the
r12 fillet's own edge, which is what it is actually complaining about.

**`upper rounds` was built at r12, doubling the plan's typed 6.** The plan types 6 rather
than deriving it, so A2's scale pass would not have touched it. Whether it should have
doubled is undecided — it is recorded here as a number nobody has decided.

**The eyes are the plan's Ø20 circles, not run 3's ellipses.** That settles a conflict
between the brief and run 3 in the plan's favour, and it costs Stage 3 its only home for
the Ellipse tool. Something else has to teach Ellipse or the tool leaves the course.

**The Ø8 pupils were not built.** The plan's step list has no step for them and no depth
is given. Undecided.

**The eye was extruded from the Front plane, 33 mm toward -Y**, not 3 mm off the front
face. Every dimension then references the origin instead of a face that moves. The disc
lands exactly 3.0 proud because 33 - 30 = 3.

**`Feature mirror` needs *Reapply features* here.** Mirroring `eye` about the Right plane
with the box unticked gives *"second eye [Mirror] did not regenerate properly: Could not
create all instances as entered. Try selecting 'Reapply features' option."* — and it says
so in the message, which is unusually helpful. Ticking it gives the second disc at
x = -16. Onshape names the fix; read the error rather than guessing.

**`Mirror` opens on `Part mirror`.** `Feature mirror` is the entry in the type dropdown at
the top of the dialog, and it is the one that wants a feature picked in the tree.

**Escape throws the Slot tool's result away; Enter keeps it.** The Slot tool draws the
slot as soon as you pick the line, but what you see is a preview: press Escape to leave
the tool and the slot goes with it, silently, leaving the line and its dimensions behind
looking like nothing happened. **Press Enter to commit, then click the toolbar button to
disarm.** This cost one full rebuild of the sketch.

**The Slot tool still parks its own DIAMETER label four radii away.** At 2× it opened at
Ø20 with the label up beside the right eye, off the slot entirely. Double-click the label
and type the number you want; do not add a second width dimension, which over-constrains
the sketch.

**A Blind extrude with `Starting offset` measures its depth back toward the sketch
plane.** Sketching the mouth on the Front plane (y = 0) and cutting with `Starting
offset` 27 and `Depth` 3 removed y -27 to -24 — a sealed void inside the head, with the
right volume removed and nothing visible on the face. **Volume alone does not catch
this**; the slot's end-cap cylinders read `y -27 .. -24` and gave it away. `Starting
offset` **30** with `Depth` 3 cuts y -30 to -27, which is the groove that was wanted.
Read the cut face's coordinates, not the volume.

**Sketching on the Front plane and pressing `n` lands you looking at the *back*.** The
view cube read `Back` and the word `Front` was mirrored on the plane. Model-space
projection still puts geometry where you ask, so the sketch is correct either way — but
every frame is a mirror image. Press `n` a second time to flip to the true front.

## Tutorial 3 — the assembly, with two parts in it

`Assembly 1` renamed `stickbot`, dragged to the first tab, holding `torso <1>` and
`head <1>`. No mates — the head has no socket and the torso has no stud yet, so both
instances sit at the origin and the head is inside the torso. That is the honest picture
and the hero frame shows it.

### Findings

**Both open questions in the plan are answered.**

*The insert dialog inserts on a single click of a Part Studio row, and stays open.* Two
clicks put both parts in and the counter at the foot of the panel reads `Inserted: 2`.
Separately is what happens naturally; there is no "together" to choose. Two frames, and
the second one shows the list still open, which is the thing worth showing.

*A mid-drag frame of the tab move is capturable*, but it is nearly identical to the after
frame: Onshape reorders the strip live as you drag, so by the time the pointer is over
the drop position the tab has already moved and only a thin insertion line separates the
two frames. Shoot the drag in flight over an **intermediate** tab if the page wants to
show motion; otherwise before-and-after carries it and the prose says "drag it left".

**Renaming a tab is right-click → Rename**, then select-all and type; Enter commits.
There is no confirmation dialog.

## tutorial 4 — the ball and socket (model built)

Feature tree, in order: ten `#` variables, `stud profile`, `revolve stud`, `collar profile`,
`collar blank`, `cavity from ball`, `slit profile`, `relief slits`, `stud connect to robot`,
`socket connect to robot`. Parts: `Ball stud`, `Socket body`.

### measured, not recalled

| check | brief | measured |
| ----- | ----- | -------- |
| parts | 2 | `Ball stud`, `Socket body` |
| ball Ø | 12.000 | sphere r 6.0 |
| `Ball stud` volume, after the slits | unchanged | 1028.968 mm³ — same as before |
| collar Ø | 18.0 | cylinder r 9.0, z −7.4 … +3.6 |
| cavity sphere | r 6.800 | r 6.8, z −6.8 … +3.6 |
| mouth | Ø11.538, four arcs | four circle edges r 5.7689 at z +3.6 |
| slit depth | 8.0 | four floors at z −4.4, from a top face at +3.6 |
| slit floor | 3.0 | −4.4 down to the collar bottom at −7.4 |
| thinnest wall | 2.20 | collar r 9.0 less cavity r 6.8 |
| socket volume | — | 1666.510 before the slits, 1531.591 after |

### what the sketch circular pattern actually does

- The seed is picked **before** the tool. Four shift-clicks on a 17 px tall rectangle put only
  **two** of the four sides in the seed, and nothing on screen said so: the copies were drawn as
  two parallel lines with no caps, which reads as a slot at a glance.
- The check that catches it is the feature JSON. `constraints[].parameters` with `parameterId`
  `localInstance*,0` lists the seed entities by name — `.top`, `.bottom`, `.left`, `.right` —
  and `,1 ,2 ,3` are the instances. Four names and four instances is the pass.
- The repair is route C from the pattern spike: hover a patterned entity, the five-dot glyph
  appears beside it, right-click the **glyph** (not the entity) → **Edit pattern**, shift-click
  the missing sides, click white space.
- **Zoom before picking.** At 11.7 px/mm the short edges were 17 px tall with the X axis through
  their middle; at 44 px/mm they were 74 px and both picks landed first time.
- There is no tick. `getComputedStyle(canvas).cursor` reads `Confirmation_Cursor` while the
  pattern is pending and `default` once it is taken. **Enter does not take it** — Enter commits
  the count box and leaves the pattern pending. A click on white space takes it. Clicking the
  toolbar button instead throws it away silently, which is how the first attempt was lost.

### the extrude

`Faces of slit profile` came from clicking the sketch's tree row. The dialog opened on **Add**
with **Merge scope** already holding `Socket body`, which is what the brief asks for — but check
it rather than trust it, because merge-with-all cuts four slots into the ball and every other
number still reads right. `Ball stud` volume before and after is the only check that catches it.

The **Direction** checkbox is not a flip: it opens a query field asking for a direction reference
and turns the feature red until something is in it. The flip is the small arrow beside **Blind**,
at (452, 230).

### the two mate connectors

`stud connect to robot` on the stalk's end face at z +10 (`#stud_len`), owner `Ball stud`.
`socket connect to robot` on the collar's bottom disc at z −7.4, owner `Socket body`.
Both are `On entity` with `Attachment: To selection`; picking a circular planar face at its
centre snaps the origin to the centre, picking it off-centre leaves the origin at the pixel.

**Read the view cube, not the arrow count.** Five presses of ArrowDown from isometric landed on a
view whose cube reads `Top` rolled 180°, so +z projected *downward* on screen and the model looked
like it was being seen from below. Eight more presses reached the cube reading `Bottom`, which is
where the collar's bottom face is pickable. `gui.project` is honest throughout; the eye is not.

**`gui.px_per_mm` can return a stale camera.** One call put a point 2200 px off screen; the next
call, unchanged, put it where it belonged. Project a point whose pixel you already know before
trusting a projection you cannot check.

## tutorial 5 — the head gains its socket (model built)

Feature list read back off `head`:

```
head profile / head body / upper rounds / lower head chamfer /
eye profile / eye / second eye / mouth profile / mouth /
socket mount point / get socket / drop socket to neck / add socket to head / head mate
```

One part, `head`. Studio bounding box `x -36 … 36`, `y -33 … 30`, `z -47 … 36`.
`lowY -33` is the eyes standing 3 mm proud of the front face at -30; forward is -Y.

### measured

| check | brief | measured |
| ----- | ----- | -------- |
| collar disc flush on the head's bottom face | z -36 | plane, area 254.469, z -36.000 |
| socket hangs below the head | -36 … -47 | span -47.0 … -36.0 |
| cavity centre = NECK_Z | -43.4 studio (58 assembly) | sphere centre (0, 0, -43.400), r 6.800 |
| socket volume survives the derive and the move | 1531.591 | 1531.591 |
| `head mate` sits at the ball centre | z -43.4 | triad drawn at the projected -43.4, not at -36 |

The studio-to-assembly offset is 101.4: `HEAD_B` 65.4 lands on the head's own bottom face at
studio -36, so assembly z minus 101.4 is studio z, and `NECK_Z` 58 is studio -43.4.

### deviations from `05-head-socket.md`

- **`socket mount point` is a mate connector, not a sketch point.** The plan left the choice open
  — *"whether that is the sketch point promoted to a connector or a separate feature is a decision
  at the CAD"*. A connector is what the transform consumes, so a sketch plus a promotion is two
  steps to reach the same thing.
- **`turn socket over` does not exist as a feature.** `Transform by mate connectors` has a
  **Flip primary axis** button in its own dialog, and that is the whole rotate. Without it the
  socket lands mouth-up inside the head, spanning -36 … -25; with it, mouth-down at -36 … -47.
  Both states were measured, so the page can still show the three-frame arc — derived, wrong way
  up, right way up — from one feature being edited rather than two features.
- **The typed `dz = -22.15 mm` is gone**, as the plan asked. Nothing in this tutorial is typed.

### GUI lessons

- **`Transform by mate connectors` carries orientation, and `Flip primary axis` at (258, 305) is
  how you reverse it.** Onshape's Transform → **Rotate** refuses a plane as its axis — the `Front`
  plane was rejected twice, from the tree, focused and unfocused — so there was no clean
  horizontal axis to rotate about in this studio anyway.
- **Boolean opened with `Keep tools` already ticked** because the two parts were selected before
  the tool was armed. It produced three parts — `head`, `Socket body` and `Part 3` — all green.
  Unticking it at (246, 229) collapses them to one part still named `head`.
- **The first click after arming a tool only highlights; the second one selects.** The mate
  connector's `Origin entity` stayed empty after a click that visibly turned the cavity sphere
  orange. A `mouse.move`, a pause, then a click filled it.
- **A mate connector picked on a spherical face lands on the sphere's centre**, which is how
  `head mate` gets to -43.4 without a number.
- **`Shift+1` is Front, `Shift+6` is Bottom, `Shift+7` is isometric** — faster and surer than
  counting arrow presses, and the view cube confirms it.

## tutorial 6 — the torso gains shoulders and studs (model built)

Feature list read back off `body`, all `featureStatus` OK:

```
torso outline / torso block /
#ball / #stand / #hip_half / #shoulder_half / #shoulder_drop /
#shoulder_len / #boss_len / #boss_d / #tilt / #yaw /
pivot lines / plane for shoulder / torso shoulder profile / shoulder /
connector on torso shoulder / mirror shoulder /
trim shoulder pattern / trim shoulder cut /
hip connector location / hip connector on torso /
neck connector location / neck connector on torso /
copy ball stud (child: stud connect to robot) /
move neck stud / copy for hip / copy for shoulder /
duplicate shoulder and hip / add neck to body /
neck connector / left shoulder connector / r shoulder connector /
l hip connector / r hip connector
```

**Parts (1) — `torso`.** Volume 343120.267 mm³. Studio bounding box
`x -55.551 … 55.551`, `y -24 … 24`, `z -64 … 64`, which is the five Ø12 balls read off the
extremes: ±(49.5509 + 6) in x, ±(58 + 6) in z.

### measured — the five ball centres

Read as `surface.origin` off each spherical face of `torso` in `bodydetails`, not off a bounding
box: the ball is truncated where the stalk joins, so its box centre is not its centre.

| ball | target from `make_plans.py` | measured |
| ---- | -------------------------- | -------- |
| neck | (0, 0, 58) | (0, 0, 58) r 6 |
| left shoulder | (49.550865, -7.824, 19.235477) | (49.5509, -7.8236, 19.2355) r 6 |
| right shoulder | mirror of the above | (-49.5509, -7.8236, 19.2355) r 6 |
| left hip | (24, 0, -58) | (24, 0, -58) r 6 |
| right hip | (-24, 0, -58) | (-24, 0, -58) r 6 |

Symmetric about the Right plane to every digit the API prints.

### the open question the plan asked

**"Whether the trim survives the reorder" — it does.** With the shoulders built first and mirrored
in their own section, `trim shoulder cut` still reaches both bosses: `highZ` after the cut is
exactly 48.0, which is the torso's own top face. The cut is one symmetric extrude of depth
`2 * #torsoD` from a rectangle on the Front plane, so it does not care how many bosses are in its
way or which feature made them.

### deviations from `06-torso-joints.md`

- **The shoulder construction chain collapses from four features to one.** The plan lists
  `shoulder rotation point`, `shoulder rotation plane`, `shoulder rotate about z` and
  `plane for shoulder`. What got built is `pivot lines` and then `plane for shoulder` alone, with
  `#tilt = 53 deg` and `#yaw = 30 deg` as the two angles a student changes. The plan's argument
  for the long chain — *"the long way puts the shoulder's angle on screen where a student can see
  it and change it"* — is served by the two variables being on screen in the tree. Whether it is
  served as well is a page-writing judgment, not a modeling one, and it is recorded here so the
  page can decide.
- **Ten variables live in `body`, not in `robot sizes`.** `#ball`, `#stand`, `#hip_half`,
  `#shoulder_half`, `#shoulder_drop`, `#shoulder_len`, `#boss_len`, `#boss_d`, `#tilt`, `#yaw`.
  Four of them are expressions on the Variable Studio's numbers — `#ball = #torsoH / 8`,
  `#hip_half = #torsoH / 4`, `#shoulder_half = #torsoW / 2`, `#boss_len = #shoulder_len - #stand`
  — so the studio still drives them and B3 will still move them.
- **`connector on torso shoulder` is placed on the boss's circular *edge*, not its planar face.**
  The edge pick lands at the circle's centre with Z along the boss axis, which is the same frame
  the face pick would have given, and the edge is pickable in one view where the face is edge-on.
- **`mirror shoulder` ended as `Add`, not `New`.** Onshape reverted the operation the moment the
  mirror plane was chosen and filled Merge scope with `torso`. The boss is therefore part of the
  torso from that feature onward, which is where `add neck to body` was going to put it anyway.
- **`duplicate shoulder and hip` did not revert, because it was pushed back to `New`.** Same
  reversion happened; clicking **New** after the plane was chosen cleared Merge scope and stuck.
  The two mirrored studs arrive as their own parts and are unioned a step later, which is what the
  plan's split of stickbot's single mirror asks for.
- **`trim shoulder pattern` is drawn on the Front plane**, a centre-point rectangle
  `#torsoW + 4 * #boss_d` wide by `#boss_d` tall with its bottom edge `#torsoH / 2` from the
  origin, and `trim shoulder cut` takes it symmetric to `2 * #torsoD`. Fully defined, no typed
  length.
- **Left is +X and right is −X.** Nothing in the plan or the briefs fixes the sign, and stickbot's
  two features named `r shoulder connector` cannot settle it. The robot faces −Y, so with +Z up
  its own left hand is at +X: `left shoulder connector` (49.55, …) and `l hip connector` (24, …),
  `r shoulder connector` (−49.55, …) and `r hip connector` (−24, …). This is the robot's
  handedness, not the viewer's — in Front view the robot's left is on the right of the screen.
- **The five connectors are built on the spherical faces, after the Boolean.** That is what fixes
  what stickbot broke: stickbot's five sit after a Boolean that took their references away, and a
  sphere face survives the union. Every one of the five reports OK.

### GUI lessons

- **A mirror's operation reverts to `Add` when the mirror plane is picked**, and Merge scope
  appears pre-filled. Read the labels after the plane pick, not before; clicking `New` afterwards
  removes Merge scope and holds.
- **`gui.row()` returns a position for a row the tree has scrolled out of sight.** It returned
  `(148, 884)` for a row that was not on screen, and a click there lands in the empty space under
  the Parts list. Scroll with the mouse over the tree, screenshot, and confirm the row is visible
  before clicking anything at `x = 219` — that column is the eye icon.
- **Picking five balls is easy in Front view and hard in isometric.** At `Shift+1` every one of
  the five balls falls entirely outside the torso's silhouette — the shoulders clear ±36 in x, the
  hips clear −48 in z, the neck clears +48 — so a click at the projected centre can only hit the
  sphere. `gui.px_per_mm` plus `gui.project` gives all five pixel targets in one call.
- **A shrunken ball reads as no ball at all.** At a zoom-to-fit isometric the Ø12 balls are about
  40 px across and the mate connector glyph drawn on each one covers them; a first reading of the
  hero frame was that the studs had vanished. `bodydetails` said otherwise, and a 5× crop showed
  the ball plainly. Check the API before believing the picture.
- **Mate connector on a spherical face lands at the sphere's centre**, confirmed again here: the
  glyph projects to (923.0, 193.8) and `gui.project` puts (0, 0, 58) at (923.0, 193.78).

## tutorial 7 — the head is mated to the torso (model built)

Assembly `stickbot`, two instances, one mate.

```
torso <1>   fixed
  neck connector / left shoulder connector / r shoulder connector /
  l hip connector / r hip connector
head <1>
  socket mount point / head mate
Mate features (1): head to neck   — Ball
```

Assembly bounding box `x -55.551 … 55.551`, `y -33 … 30`, `z -64 … 137.4`.
**`highZ` is 137.4, which is `HEAD_T` exactly**, so the head landed where `make_plans.py` puts it
without a number being typed anywhere in the chain: the head's socket cavity centre is at its own
studio -43.4, the torso's neck ball centre is at 58, and the ball mate makes those the same point.

### the lesson that cost the most: a mate connector with no owner part never reaches the assembly

**Untick "Owner entity" in a Part Studio and the connector stops existing as far as the assembly is
concerned.** It is still there in the studio, still pickable inside the studio, still drives the
transforms — but `torso <1>` in the assembly tree had no expand chevron at all, while `head <1>`
listed both of its connectors.

The tell is in the feature JSON. Both are `mateConnector` features with the same parameters; the
one that works has

```
ownerPart  [{"geometryIds": ["JHD"], …}]
```

and the one that does not has `ownerPart []`. **`ownerPart` is not filled by ticking the box** —
ticking only reveals the `Select owner entity` field. Something has to be put in it: clicking the
part's row in the **Parts** list while that field has focus does it, and the query comes back
holding the part id.

**The repair is per feature and it is cheap**: double-click the connector in the tree, tick
**Owner entity**, click the field, click `torso` in the Parts list, accept. Five features, five
minutes, and `torso <1>` then lists all five by name.

**Which connectors want an owner is a real distinction, not a rule to apply everywhere.** The three
that only ever drive a transform inside the studio — `connector on torso shoulder`,
`hip connector on torso`, `neck connector on torso` — are better off without one: they stay out of
the assembly tree, where they would be five more near-identical rows for a student to pick wrongly.
The five that the assembly mates to need one. That is the same split the plan draws when it says
rebuilding the five *"takes work out of the assembly"*.

### a generic field name means an implicit connector, in the assembly too

Before the repair, clicking the neck ball in the graphics area with the Ball mate armed filled the
field with **`Mate connector of torso <1>`**. After it, clicking the tree row filled it with
**`neck connector of torso <1>`**. Same rule as the Part Studio transforms: read the field text.
The implicit one would have landed in the right place — an implicit connector on a spherical face
takes the sphere's centre — and it would have been anonymous and unrepairable from the studio.

### GUI lessons

- **In an assembly, mate connectors are pickable from the tree**, unlike a Part Studio, where only
  the graphics-area glyph works. Expand the instance and click the row.
- **Fix the torso by right-clicking its instance row → `Fix`.** The row's move triad is replaced by
  a hatched ground icon, which is the whole signal the plan asks for a frame of.
- **A click in the tree does not cancel an open mate dialog.** The `Ball 1` feature appears under
  `Mate features` while it is still pending and still red; clicking an instance row selects the row
  and leaves the dialog open. Cancel is the × at (451, 93).
- **`gui.px_per_mm` throws in an assembly** — `window.__cam` is not installed on that page, so
  `onshape_screen.camera` raises `Cannot set properties of undefined`. Pick by eye from a zoomed
  screenshot instead.
- **The instance eye icon is at x ≈ 219**, same column as the Part Studio's, and the row moves
  when an instance above it is expanded — re-read the row before clicking it.

### version published

`t7 head mated` — `acc35f11ec85129825dfdbee`. It is a snapshot of the whole document, so it is the
recovery point for tutorials 1 through 7's models, not tutorial 7's alone.

## Tutorial 8 — the foot (`foot` Part Studio, version `t8 foot` 3d7b30559398005be8c9909f)

**Built, measured, framed.** Seventeen variables, ten features, one part.

### The variable table, as typed

`#foot_l = #torsoH` 96 · `#foot_w = #torsoH / 2` 48 · `#ankle_h = #torsoH / 4` 24 ·
`#plate = 12 mm` · `#top_round = 8 mm` · `#ball = #torsoH / 8` 12 · `#wall = #torsoH / 32` 3 ·
`#collar = 11 mm` · `#grip = 3.6 mm` · `#collar_r = #ball / 2 + #wall` 9 ·
`#collar_down = #collar - #grip` 7.4 · `#pedestal = #plate - #collar_down` 4.6 ·
`#rib_w = 6 mm` · `#rib_d = 2 mm` · `#heel_r = #foot_w / 3` 16 · `#toe_r = #foot_w / 2` 24 ·
`#heel_y = #foot_l / 3` 32.

Four are typed rather than driven — `#plate`, `#top_round`, `#collar`, `#grip`. `#collar` and
`#grip` are typed because the joint itself did not scale; that is the same B3 risk already
recorded against `ball and socket`. `#plate` and `#top_round` are the brief's own **proposed**
numbers and have no driver to hang on.

### The features

`pedestal outline` / `foot pedestal` / `foot outline` / `foot` / `top round` /
`groove profile` / `sole groove` / `sole ribs` / `add socket` / `combine parts` / `mate to robot`.

**`place socket` was not built, and does not need to be.** The plan's eleventh step transforms the
derived socket onto the pedestal by connector. It is a no-op here: `ball and socket` puts the ball
center on its origin, the foot puts the ankle ball center on its origin, so a Derived at **Base
origin** lands the socket exactly where it belongs — measured `highZ` 3.6 = `#grip`, and the
collar's bottom face at −7.4 sits on the pedestal's top face at −7.4. That answers the file's open
question *"whether the reorder breaks anything"*: **the reorder is free, and it deletes a step.**
The pedestal has to exist first only in the sense that the socket has to land on something.

### The outline is two circles and their common tangents

Heel circle Ø32 centered 16 ahead of the origin, toe circle Ø48 centered 40 behind it, two
external tangent lines, inner arcs trimmed. Tangent throughout by construction, and symmetric
about the Right plane without a Symmetric constraint: both centers snap onto the Y axis when
clicked on it, and *coincident-on-circle + tangent* fully determines each side line. The sketch
went black — fully defined — with four dimensions and no symmetry constraint at all.

**Onshape has no sketch slot tool.** The rectangle group is Corner / Center point / Aligned; the
polygon group is Inscribed / Circumscribed. A stadium would have been three clicks if it existed;
it does not, so the two-circle construction is the cheap one as well as the honest one.

### What was measured, against the brief

| Check | Wanted | Got |
| ----- | ------ | --- |
| Parts | 1 | 1, `Foot`, 38837.629 mm³ |
| length × width | 96.000 × 48.000 | y −64…+32, x ±24 |
| ground | z −24.000 | −24.000, ankle ball center on the origin |
| symmetric about its centerline | lands on itself | mirrored about **Right** and merged: volume **unchanged** at 38837.629 |
| tangent throughout | no crease | four entities, tangent-propagated by one fillet pick |
| socket mouth | Ø11.538 | radius **5.7689** at z = 3.6, in four arcs → Ø **11.5378** |
| cavity | 1132.65 mm³ | sphere face **r 6.800** centered on the origin; the derived socket carries `ball and socket`'s measured 1132.649 |
| collar proud of the plate | 15.6, not 11.0 | plate top −12, collar top +3.6 → **15.6**. The gap to the plan's 11.0 is **4.6**, reported, plate not moved |
| flat around the collar | ≈1.29 | side wall plane sits **18.29** from the axis, less r8 fillet less r9 collar = **1.29** |
| relief slits | four | **eight** planar walls at ±0.8 about each axis plane, z −4.4 → four slits |
| sole ribs removed material | yes | 8 groove floors at **−22.000**, 8 rib faces at **−24.000**, **3315.29 mm³** removed (the brief predicted ≈3353 for seven) |
| thinnest wall | 2.20 at the collar, 4 at the plate edge | 9.0 − 6.8 = **2.20**; 12 − 8 = **4.00** |

### Three things that cost a round each

**`gui.row(page, "Top")` does not find the Top plane.** It matched something at (158, **70**) — in
the toolbar, not the tree — and the sketch was created on whatever plane was last used. It came up
as **Right plane** and the two circles drawn into it were invisible from the Top view. Use a DOM
query restricted to `rect.x < 250` instead; the tree row is at x = 158.

**A feature pattern of a Remove extrude fails silently until `Reapply features` is ticked.**
`Linear pattern 1` came back `ERROR` with no message, the volume did not move, and the preview
drew the instances in red. Ticking **Reapply features** fixed it in one click. This is exactly the
failure the brief warns about — *"the pattern regenerated into nothing and the volume did not
move"* — and the only thing that catches it is the volume.

**The instance count field fights its own autocompletion.** `set_field` left `6f` in it and an
autocomplete list open. Click, `Meta+A`, `keyboard.type(...)`, then click a *label* in the dialog
to blur — not Enter, which takes the autocomplete entry. It accepts an expression:
`#foot_l / (2 * #rib_w)` evaluates to **8**, so the rib count survives a change to `#torsoH`.

**The pattern went the wrong way first.** Direction *Front plane* gave −Y; the flip arrow sits at
(455, 276), right of the Instance count field. Both frames are kept —
`cad.parts.foot.ribs.wrong_way.png` and `.right_way.png` — because the plan asks for exactly that
pair.

### Extrude, twice more

Both the plate and the groove needed **Starting offset**, and both needed a flip. The layout is
stable: depth field first, main flip arrow **(453, 230)**, `Starting offset` checkbox **(276,
313)**, and after it opens a second Blind/Depth block whose flip arrow is **(453, 369)**. Switching
the operation to `Add` or `Remove` does not move any of them — it only appends Merge scope.

The groove came out as an **enclosed slot at z −22…−20** the first time: offset down, depth up.
One click on the main flip arrow put it at −24…−22. Reading the planar z levels off `bodydetails`
is what caught it; the picture from below looked plausible either way.

### Owed

- `cad.parts.foot.pedestal_sketch` and `cad.parts.foot.pedestal` were built in the previous
  session without frames. They need a rollback-bar pass or a rebuild to capture.
- The brief's *"build it wrong once on purpose"* frame — the plan shape sketched on **Front** and
  the foreshortened result — was not taken.
- The open question about `FOOT_X` 32 against `LEG_X` 24 cannot be answered from this tab; it is
  an assembly question and belongs to tutorial 14.

## Tutorial 9 — the hinge (`hinge` Part Studio, `d7401eebccc0e7c8681f5bac`) — IN PROGRESS

Stopped after `stub axle outline`. Three of the twenty-six steps in `09-hinge.md` are in.

### Which hinge is being built

`09-hinge.md` says **"Do not resolve this at the CAD."** It has been resolved at the CAD anyway,
in favour of the plan's own step tables, because the alternative was to stop:

- the stub axle is on the **blade** and the hole goes through the **fork**
- the ear is **6.4 mm** — the number the r4 sheets are dimensioned to
- the blade carries **no slit**

**This is a deviation and it is owed back to `make_plans.py`, the plan sheets, the brief and
`09-hinge.md` together.** Nothing built so far depends on the slit question; the ear thickness is
baked into `#ear`, so changing it is a variable edit, not a rebuild.

### The geometry, worked out before any of it was built

Hinge axis is the **Y axis** — fore-and-aft through the origin. The blade limb hangs **below**
(−Z), the fork limb stands **above** (+Z).

| | |
| - | - |
| blade | y ±5, x ±10.9087, z −20…+12; the round end is r12 about the origin and meets the sides exactly at z = +5 |
| fork ears | y 5.6…12, outer surface the Ø24 cylinder about Z, tips at z = −12, slot root at z = +21 |
| stub | Ø4.0 standing 1.6 proud on each blade face — one extrude, symmetric, 13.2 total |
| hole | Ø4.4 through each ear |
| bumps | Ø1.6 at r9.6 on each ear inner face, 1.2 proud |
| valleys | Ø2.0 × 0.9 deep at r9.6 in each blade face, first at (x 0, z +9.6), 24 of them at 15° |
| arm rods | Ø24, length `#rod` = 24 — a chosen number, not a derived one |

### The variable table, as typed

```
#limbD      = #torsoH / 4                      24
#blade      = 10 mm
#gap        = 0.6 mm
#slot       = #blade + 2 * #gap                11.2
#ear        = (#limbD - #slot) / 2             6.4
#nose       = #limbD / 2                       12
#blade_out  = 32 mm
#slot_deep  = #blade_out + 1 mm                33
#blade_half = sqrt(#limbD ^ 2 / 4 - #blade ^ 2 / 4)   10.90871
#stub       = 4 mm
#stub_proud = 1.6 mm
#pocket_d   = 4.4 mm
#teeth_ri   = 8.8 mm
#teeth_r    = 10.4 mm
#bump_r     = (#teeth_ri + #teeth_r) / 2       9.6
#bump_d     = #teeth_r - #teeth_ri             1.6
#valley_d   = 2 mm
#valley_deep = 0.9 mm
#tooth_proud = 1.2 mm
#rod        = #limbD                           24
```

**Twenty variables do not fit in one 90 s script** — about 4.5 s each. They went in as 8 / 6 / 6.

### What is built, and measured

`blade profile` — Front-plane sketch, fully defined. A **Center point arc** centered on the origin
from (10.9087, 5) counter-clockwise to (−10.9087, 5), then three lines closing the shape down to
z = −20, a **Symmetric** constraint on the two vertical lines about the vertical axis, and three
dimensions: R12 (`#nose`), 21.81742 (`2 * #blade_half`), 20 (`#blade_out - #nose`).

`blade blank` — Extrude, New, Blind, **Symmetric**, depth 10 mm. Read back off `bodydetails`:

```
bbox   x ±10.909   y ±5.0   z −20.0…+12.0
volume 6551.991 mm3
cylinder r 12 about [0,1,0] through the origin, area 273.845
planes at x ±10.9087 (250.0 each), z −20 (218.174), y ±5 (655.199 each)
```

`stub axle outline` — Front-plane sketch, one circle on the origin, **Ø4** dimensioned as `#stub`.
Fully defined.

### The mistake that cost the most: a checkbox one row off

`blade blank` was built with **Draft 3°** and no Symmetric, because the checkbox positions were
read from `gui.labels` *immediately after* the region pick and were stale by one row. The click
meant for `Symmetric` at y 340 landed on `Draft` at y 368. The part came back with a **cone** for
its round end and y −10…0 instead of ±5, and neither is visible in a shaded isometric.

**Read the labels, screenshot the dialog, and only then click the checkbox.** The crop is what
shows the tick state; `gui.labels` gives positions and says nothing about whether a box is on.

Repairing it took four rounds, all of them spent on *re-opening the feature*, not on the fix:

- `gui.row(page, "blade blank")` returns a **toolbar** hit as readily as a tree row.
- `common.jrow` restricts to `rect.x < 250`, which fixes that — **but it still returns a position
  for a row scrolled out of the feature list's own scroll box.** `blade blank` read as (148, 767),
  which is empty white space below `Parts (1)`; clicking and right-clicking there do nothing at
  all, silently.
- The feature list has an **inner scroll container**, separate from the panel. `common.scroll_tree`
  drives it: **positive n scrolls up, negative n scrolls down.** After `scroll_tree(page, -14)` the
  row was at (148, 616) and a plain `dblclick` opened the dialog first try.

So `common.edit_row`'s right-click hunt for "Edit feature" was never the problem — the row simply
was not there. **Double-click works anywhere in the tree once the row is actually visible.**

### Checkbox pixel positions, from a crop rather than a guess

In the Extrude dialog with a region picked and no starting offset:

```
Symmetric checkbox  (257, 341)
Draft checkbox      (257, 368)
```

Ticking Symmetric hides `Second end position`; unticking Draft removes its angle field. Depth
stays where it is.

### Frames on disk

```
cad.parts.hinge.blade.profile_sketch.png
cad.parts.hinge.blade.blank.png
cad.parts.hinge.blade.axle_sketch.png
```

### The blade is complete — all twelve steps, measured

```
blade profile / blade blank / stub axle outline / stub axle /
click lock valley sketch / click lock valley / #rim_break = 0.1 mm /
round valley rim / axis for circular patterns / 24 valleys / mirror blade /
blade rod outline / blade arm
```

| | |
| - | - |
| bbox | x ±12.0, y ±12.0, z −44.0…+12.0 |
| volume | 17313.169 mm3 |
| blade alone, before the arm | 6455.824 |
| valley floors | 24 at y −4.10 and 24 at y +4.10 |
| valley angles | exactly 15° apart, −180 through +165 |
| rod | π · 12² · 24 = 10857.34, and 6455.824 + 10857.34 = 17313.16 |

**`#rim_break = 0.1 mm` is a twenty-first variable that the plan's step table does not have.** The
brief sizes the rim break at r0.10 in prose only — `make_plans.py` has no constant for it — so the
model carries it as a variable rather than as a typed number, and `make_plans.py` is owed a
`BREAK` to match.

### The valley cut is a Front-plane sketch with a starting offset, not a sketch on the face

The valley has to be constrained to the hinge axis, and the origin is the only thing that says
where that is. A sketch on the blade's own face has no origin on it. So `click lock valley sketch`
sits on the **Front** plane — one circle, `Ø#valley_d`, its centre `#bump_r` above the horizontal
axis and snapped onto the vertical one — and `click lock valley` is a Remove extrude with
`startOffsetDistance = #blade / 2` and `depth = #valley_deep`. The floor reads back at y −4.100,
which is the whole check.

### Two directions and two flips, on the arm

`blade arm` needs **both** flips: the starting offset runs +Z and the depth runs +Z by default, so
the first attempt built the rod from z +20 to +44 and Onshape said *"Boolean resulted in no
geometry change"* and quietly made **Part 2**. The banner is the tell, and so is `Parts (2)`. Main
flip arrow **(453, 230)**, offset flip arrow **(453, 369)**.

### GUI lessons this half paid for

- **`p` toggles the default planes.** Every frame before that had a pale blue plane across it and
  one had the selected Front plane tinting half the part olive. Press `p` with the pointer on the
  canvas before any frame.
- **A number field shows its expression when it is committed and its literal when it is not** —
  which is exactly backwards from what it looks like. Do not trust `input_value()`; read
  `parameters[].message.expression` off `/features` instead. `depth = '#valley_deep'` and
  `startOffsetDistance = '#blade / 2'` are what the JSON says, and both fields displayed literals
  at some point while being right.
- **`el.fill()` then Enter loses the expression sometimes.** Click, `Meta+A`, `keyboard.type(...)`,
  then click the **dialog title** at (328, 93) to blur. The title is the only safe blur target — a
  label click toggles its checkbox, and a field label click selects that field's text.
- **`gui.rename_row` leaves the row selected**, which puts a hover highlight on the geometry it
  owns. Click empty tree space at (140, 880) and press Escape before framing;
  `screen.selected(gui.probe(page))` should read 0.
- **A circular pattern with Angle 360 and Equal spacing divides by N, not N−1.** 24 instances came
  out at exactly 15°.
- **Feature pattern and feature mirror both need Reapply features** when what they carry is a
  Remove. The mirror's checkbox moves down the dialog once the mirror plane is picked — read the
  labels again after the pick.

### Where to pick up

**The fork, fourteen steps**, starting at `fork outline`. Nothing of it is built. The numbers are
in the geometry table above: ears y 5.6…12 with the Ø24 cylinder as their outer surface, tips at
z −12, slot root at z +21, a Ø4.4 hole through each ear, Ø1.6 bumps at r9.6 standing 1.2 proud,
domed with an r0.8 fillet on the crown **face**.

Then `blade to robot connector` and `fork to robot connector`, then a version.

### Owed

- The valley and bump close-ups are taken for the valley, not the bump. The **detent frame** — a
  bump sitting in a valley — is the one the plan says to fight for and it needs both halves.
- The count field frame: `24 valleys` was accepted before the dialog was framed. Re-open the
  feature to take it.
- A section through the axle and the pocket.
- The two heroes, the clicked-together hero, the part list, the tree, the version dialog.
- The deviation above, back into `make_plans.py`, the sheets, `hinge.md` and `09-hinge.md`.

### The fork, built 2026-08-23 — all fourteen steps

The fork is done and the studio is closed: **49 features, all OK, Parts (2)**, named `blade` and
`fork`, version **`t9 hinge`** (`dcb3dcc42e49e130ce163031`).

| Step | Feature | What it is | Checked by |
| ---- | ------- | ---------- | ---------- |
| 1 | `fork outline` | Top plane: Ø`#limbD` circle, chord at `#slot / 2` | fully constrained, both dimensions `fx` |
| 2 | `fork blank` | extrude New, start offset `#nose` down, depth `#slot_deep` up | bbox z −12…+21; volume **3195.923**, and the circular segment `r²·acos(d/r) − d·√(r²−d²)` at r 12, d 5.6, times 33, is **3195.92279** |
| 3 | `fork blade top cut outline` | Front plane: Ø`2 * #nose` circle, rectangle top at `#slot / 2`, sides and bottom at `#nose + 2 mm` | five `fx` dimensions, sketch black |
| 4 | `trim fork to arm` | extrude Remove, Through all, Symmetric, **merge scope `fork` only** | volume **3085.390**; the integral of `12 − √(144 − x²)` over the segment is **110.53113**, and 3195.923 − 110.531 = 3085.392 |
| 5 | `pocket axle sketch` | Front plane: Ø`#pocket_d` on the origin | coincident constraint added by hand; see the trap below |
| 6 | `pocket axle on fork` | Remove, Through all, Symmetric, scope `fork` | volume **2988.853**, against 96.54 predicted for a Ø4.4 bore through a 6.4-thick ear whose far face is the Ø24 cylinder |
| 7 | `click bump outline` | Front plane: Ø`#bump_d` at `#bump_r` up the vertical axis | Vertical constraint to the origin, then one distance dimension |
| 8 | `click bump` | Add, start offset `#slot / 2`, depth `#tooth_proud`, scope `fork` | volume **2991.266**, i.e. +2.4127 = π·0.8²·1.2 |
| 9 | `dome click bump` | fillet `#bump_d / 2` on the crown **face** | volume **2990.730**, i.e. −0.53616, which is exactly a Ø1.6 × 1.2 cylinder becoming a 0.4 stalk plus an r0.8 hemisphere |
| 10 | `24 bumps` | feature pattern of `click bump` + `dome click bump` about `axis for circular patterns`, 360°, 24, equal spacing | volume **3033.891**, i.e. +23 × 1.876578 — exact to the last digit |
| 11 | `two forks` | **part** mirror of `fork` about the Front plane | the second ear, **3033.890** |
| 12 | `fork arm outline` | Top plane: Ø`#limbD` on the origin | black first try — the circle snapped |
| 13 | `fork arm` | New, start offset `#slot_deep - #nose`, depth `#rod` | **10857.344** = π·12²·24, bbox z to +45 |
| 14 | `combine fork parts` | Boolean union of the two ears and the arm | **16924.803**, against 16925.126 by arithmetic; `massproperties` reports a ±14.6 band on this body, so the 0.32 is the API's tolerance, not geometry |

Then `fork to robot connector` on the arm's top disc at (0, 0, 45) and `blade to robot
connector` on the blade arm's bottom disc at (0, 0, −44). Both were placed by selecting the
**planar end face**, which lands the connector on the face's centre with Z along the normal.

### Traps this half of the tutorial found

- **`#nose + 2` is not a valid expression.** A bare number cannot be added to a length; it has to
  be **`#nose + 2 mm`**. The dimension silently keeps its as-drawn value and shows it without the
  `fx` marker — that missing `fx` is the only warning you get.
- **A circle drawn on the origin is not always constrained to it.** Sometimes it snaps and comes
  out black, sometimes it comes out blue with the centre merely sitting there. The fix that
  works every time: drag the circle away, then pick its centre and the origin and apply
  **Coincident**. You cannot pick two points that are exactly on top of each other.
- **Do not trust a screen coordinate across scripts.** Re-entering a sketch and pressing
  `Shift+1` does not restore the previous zoom. Call `gui.zoom_to` and `gui.project` again in the
  same script that clicks, or you will draw at the wrong place — the bump circle went in at
  z 21 instead of z 9.6 this way and looked, at a glance, like it had been deleted.
- **Flipping an extrude's direction moves its starting offset with it.** They are not
  independent: the main arrow flips the whole frame and the offset arrow then flips the offset
  inside it. Getting `click bump` from "no geometry change" to a merged bump took main-flip,
  offset-flip, main-flip.
- **`Face of Origin` is a real pick.** In a Top view the world origin projects onto whatever
  face is under it, and a mate connector click at the centre of a disc grabs `Vertex of Origin`
  instead of the face. Click 3–4 mm off centre and let the face's own centroid place it.
- **An extrude's operation tab resets to New when you edit a number and blur on the title.**
  Read the tab back before you accept; `click bump` had to be put back on Add.

### What is owed on tutorial 9

- The fork's per-step frames were not taken. The blade's were. What exists for the fork is the
  end state: `cad.parts.hinge.hero.png`, `cad.parts.hinge.fork.bumps.png`,
  `cad.parts.hinge.tree.png`, `cad.parts.hinge.version.png`.
- The detent shot — a bump sitting in a valley — needs a section view and was not taken.
- `two forks` is a **part** mirror, not the feature mirror the blade uses. A feature mirror here
  would have to carry two Removes with explicit merge scopes and reapply them onto a body that
  does not exist yet; the part mirror is one pick and is provable by volume. This is a deviation
  from stickbot and it is deliberate.

## Tutorial 10 — the upper limb (`u limb` Part Studio, version `t10 u limb` 7d293115a90ebec16359ccf7)

**Built and measured.** One local variable, nine features, one part, `u limb`, 40171.463 mm³,
spanning z −112.4 … +3.6 and x, y ±12.

### The frame: the top joint's centre is the origin

[`limbs.md`](../../../build-briefs/limbs.md) says to build a limb *"with the top joint's center on
the origin and the limb running downward"*. The first attempt here ignored that and stood the limb
up from z 0 to 48 with the socket on top. Everything measured correctly and the last step was
still impossible: `shoulder end` has to sit at the socket's ball centre, and in that frame the
ball centre is a point in mid-air with no entity on it — see
*the connector that had nothing to land on* below.
The studio was stripped back to `add socket` and rebuilt in the brief's frame. In the brief's
frame the ball centre is **the origin**, and `shoulder end` is one pick: `Vertex of Origin`.

### The features, and why there are nine and not eleven

| # | Feature | What it is | Checked |
| - | ------- | ---------- | ------- |
| 1 | `#limbD = #torsoH / 4` | 24 mm, the local variable | |
| 2 | `add socket` | Derived `ball and socket` → Socket body, **Base origin** | **1531.591**, identical to its source; bbox z −7.4 … +3.6 |
| 3 | `limb section` | one circle on the **collar's bottom disc**, Ø `#limbD` | black, one dimension, centre on the sketch origin |
| 4 | `limb` | extrude New, Blind `#limbSeg`, away from the socket | **21714.688** = π·12²·48; z −55.4 … −7.4 |
| 5 | `mate for fork` | mate connector on the limb's bottom face, owner unticked | |
| 6 | `add fork` | Derived `hinge` → fork only | **16924.803**, identical to its source |
| 7 | `move fork` | transform by mate connectors, **flip primary axis** | bbox lowZ −112.4 |
| 8 | `combine parts` | Boolean union of the three | **40171.463** against 40171.082 by arithmetic |
| 9 | `shoulder end` | mate connector on `Vertex of Origin`, owner `u limb` | at the ball centre by construction |
| 10 | `elbow end` | mate connector, **Between entities**, the two Ø4.4 pocket faces | preview triad landed on the hinge axis, 3 px |

`10-u-limb.md`'s table has eleven steps; this has nine. **`mate for socket` and `move socket` are
not built, and do not need to be.** `ball and socket` puts the ball centre on its own origin, so a
Derived at **Base origin** already lands the socket where the brief wants it — the same discovery
tutorial 8 made about the foot, for the same reason. Deriving the socket **first** and sketching
the limb on the collar's own bottom face is what buys it: the limb hangs off a real face, so a
change to `#torsoH` moves the face and the limb follows.

### The connector that had nothing to land on

`shoulder end` must be at the socket's ball centre, because that is where the torso's shoulder ball
connector is and a ball mate makes the two origins coincident. In the limb-up frame that point is
inside solid material, and three attempts to pick it all missed:

| what was picked | what Onshape stored | where it landed |
| --------------- | ------------------- | --------------- |
| the cavity sphere, 3 mm off the axis, in Top view | `MID_POINT` | on the sphere **surface**, 6.8 from the centre |
| the axis pixel in Top view, connectors hidden | `CENTER` of the mouth circle | the collar's mouth plane, z 59 — **3.6 high** |
| the same, with a `Move` offset of `-#grip` | nothing | `#grip` is not in scope; the field went red |

**A concave sphere does not offer its centre.** Every sphere connector elsewhere in this document
— `head mate`, `neck connector`, the shoulder and hip connectors, `stud connect to robot` — stores
`CENTER`, and every one of them was picked on a **convex** ball. Looking down into a cup, the
inference that wins at the axis pixel is the mouth circle's centre, and off the axis it is the
picked surface point. Neither is the sphere centre.

**And `#grip` is not a robot-wide variable.** `robot sizes` holds four numbers — `#torsoH`,
`#torsoW`, `#torsoD`, `#limbSeg`. `#grip` and `#collar` live in the `ball and socket` and `foot`
Part Studios, so an expression that reaches for them from `u limb` cannot resolve. Any offset
written here would have had to be a typed 3.6 or 7.4, which is the magic number the brief exists
to prevent.

Rebuilding in the brief's frame removes the problem instead of working around it.

### `elbow end` is the one pick that has to be two

The hinge axis has no entity on it either — it is the axis of two blind pockets, one in each ear,
with the blade's slot between them. **Between entities** with the two Ø4.4 pocket cylinder faces
puts the connector at the average of their two centroids, which is y 0 on the axis. That is what
`stickbot-for-bot-review`'s own `Mate connector 2` stores, and it is the construction copied here.

**Both picks must be the same kind of entity.** An edge paired with a face averages a circle centre
against a cylinder centroid and lands 8 mm off. The two pocket faces are visible one at a time:
one from the standard isometric, the other after rotating 180°.

### Traps this tutorial found

- **Concentric circles in an axial view cannot be told apart.** Looking straight down the hinge
  axis, the pocket's four circles — two ears, two ends each — project onto one ellipse, and every
  click lands on the same one. Clicking the same edge twice does not add a second entity. Turn the
  model until the two ears separate on screen, then click each.
- **Middle-drag does not rotate the Onshape canvas.** The camera did not move. The **view cube's
  side arrows** do rotate, 90° a click; two clicks from the isometric gives the view from behind.
- **`gui.px_per_mm` returns a tuple**, `(scale, camera)`. `round()` on it raises
  `TypeError: type tuple doesn't define __round__`. Unpack it.
- **A Derive picks the whole Part Studio if you click the studio row.** The parts appear indented
  under it; click the one part you want and the studio-wide selection drops away. Parts (4) went
  back to Parts (3).
- **An extrude on a face defaults to Add, not New**, with the face's own body already in the merge
  scope. Click **New** before setting the depth, then read the tab back — it resets to New when a
  number is edited and blurred on the title, which here was the tab we wanted anyway.


### the limb segment does not close, and it never has

**`ARM_SEG` and `LEG_SEG` in `make_plans.py` are joint-centre to joint-centre.** Line 761 reads
`KNEE_Z, ANKLE_Z = HIP_Z - LEG_SEG, HIP_Z - 2 * LEG_SEG`, and lines 776–777 step the elbow and
wrist along by `ARM_SEG`. The limb sheet's caption says the same rod is `Ø24 × 48 mm`, so the
sheet treats the stock length and the centre distance as one number. They are not one number,
because each joint stands off the stock's end face:

| joint | stands off its own end face by |
| --- | --- |
| socket | 7.4 — `socket connect to robot` sits on the collar's bottom disc, the ball centre 7.4 above it |
| fork | 45 — `fork to robot connector` sits on the arm's top disc, the hinge axis 45 below it |
| blade | 44 — `blade to robot connector` sits on the arm's end disc, the hinge axis 44 above it |
| ball stud | 10 — `stud connect to robot` sits on the stalk's end face, the ball centre 10 beyond it |

A 48 segment would need the upper limb's stock to be `48 − 7.4 − 45 = −4.4` long, and the lower
limb's to be `48 − 44 − 10 = −6`. **There is no limb short enough, on either part.** The minimum
segment these joints admit is 52.4 above the elbow and 54 below it, with no rod at all between
them.

**This is older than the doubling, and the doubling made it far worse than twice as bad.** All
four limbs were measured read-only over REST on 2026-08-24. `stickbot-for-bot-review`'s `u limb`
runs z −25.92 … 9.5, its cavity sphere centered at z 8.15 and its axle pocket at z −20.11, so its
centres are **28.26** apart where the 1× sheet said 24. Its `l limb` runs z −25.91 … 12.0, its ball
at z 9.0 and its stub axle at z −20.11, so that segment is **29.11**, again against 24. The printed
robot has always been longer than its own plan sheet — by 4.26 and 5.11.

draft9p0 overshoots the same sheet by **52.4 and 54**. The overshoot grew about twelvefold, not
twofold, and the parts grew with it: 116 against 35.42 is **3.28×**, and 120 against 37.91 is
**3.17×**, while the limb's diameter is 24 against 12, **exactly 2.000×**. What doubled is the
stock. The stand-offs sit outside `#limbSeg` instead of inside it, and they are set by the socket
and the hinge, so nothing about `#limbSeg` controls them.

The reference's own stock length is not in this record. `/features` timed out twice against that
document, so nothing here splits its 28.26 into stock and stand-offs; the segment, the overall
length and the radii are what was measured.

**draft9p0 built what [`10-u-limb.md`](../../../../build/plan/10-u-limb.md) says to build**: the
extrude's depth is `#limbSeg`, which is 48. With the socket's ball centre on the origin that puts
the hinge axis at z −100.4, so the segment is **100.4** and the part is **116** long overall.
[`11-l-limb.md`](../../../../build/plan/11-l-limb.md) got the same treatment: with the hinge axis on
the origin the ball stud's centre lands at z −102, so that segment is **102** and the part is
**120** long. Both are buildable, both are measurable, and both are wrong against `make_plans.py`
by the same kind of amount.

**The fix is one variable, and it is the user's call which way it goes.** Either
`#limbSeg` stops meaning the stock and starts meaning the centre distance — which needs the
hinge's `#rod` (24) and the blade's reach cut down before 48 fits — or `ARM_SEG`/`LEG_SEG` in
`make_plans.py` become the centre distance the joints actually produce. Nothing else in the model
has to move: the depth field holds `#limbSeg`, so the whole robot's limb length is one edit in the
Variable Studio.

### What is owed on tutorial 10

- The two derives were not framed **as arrived**; the features were accepted before the shot was
  taken. What exists is the finished part, the two ends and the join, each medium and close-up
  with a ring, plus the depth field and the tree.
- The first build — limb up from the origin, socket on top — is gone. It measured correctly at
  every step; it was replaced because of where it left `shoulder end`, not because anything about
  it was wrong to build.

## Tutorial 11 — the lower limb (`l limb` Part Studio, version `t11 l limb` b5617bfbc551a3949f4cf02a)

`454ab6f22f9df4f86778b537`. Ten features, one part, **40056.825 mm³**, bounding box
x ±12, y ±12, **z +12 … −108**.

### The same frame as the upper limb, and it costs one step less

[`11-l-limb.md`](../../../../build/plan/11-l-limb.md) says *"the same eleven moves as `10-u-limb.md`,
with the mating halves swapped"*, and the upper limb had already dropped two of those eleven. The
lower limb drops the same two for the same reason:
[`limbs.md`](../../../build-briefs/limbs.md) asks for the **top joint's centre on the
origin with the limb running downward**, and the `hinge` studio already puts the hinge axis on its
own origin, so a Derived at **Base origin** lands the blade in exactly the right place. There is
nothing to sketch a connector onto and nothing to move.

| # | Feature | What it is | Measured |
| - | ------- | ---------- | -------- |
| 1 | `#limbD = #torsoH / 4` | 24 mm | |
| 2 | `add blade` | Derived `hinge` → the `blade` body only, **Base origin** | 17313.169, identical to the source; z −44 … +12 |
| 3 | `limb section` | circle on the blade arm's end disc (area 452.389 = π·12²), Ø `#limbD`, centre on the sketch origin | black with one dimension |
| 4 | `limb` | Extrude **New**, Blind `#limbSeg`, away from the blade | 21714.688 = π·12²·48; z −44 … −92 |
| 5 | `mate for ball stud` | mate connector on the limb's far end face, **Owner entity unticked** | |
| 6 | `add ball stud` | Derived `ball and socket` → `Ball stud` only | 1028.968, identical to the source |
| 7 | `move ball stud` | Transform by mate connectors + **Flip primary axis** | bbox lowZ −108 |
| 8 | `combine parts` | Boolean Union of the three | **40056.825**, and 17313.169 + 21714.688 + 1028.968 = 40056.825 exactly |
| 9 | `elbow end` | mate connector, **Between entities**, the two Ø4 stub axle end faces | glyph on the hinge axis, Z fore-and-aft |
| 10 | `wrist end` | mate connector on the ball's spherical face | glyph within 3 px of the projected ball centre |

The union is exact to the last digit because nothing overlaps: the blade arm ends at z −44 where
the limb begins, and the ball stud's stalk end face sits on the limb's end face at z −92. Both
joints butt, neither interferes.

### Why the flip is needed, worked out before it was clicked

`mate for ball stud` sits on the limb's far end face, so its Z runs **out of** the limb, −Z.
`stud connect to robot` sits on the stalk's end face at the source's z +10 with its Z running +Z,
which puts the ball at −10 along its own Z. Map one frame onto the other and the ball lands at
z −92 + 10 = −82 — inside the limb. **Flip primary axis** turns the target's Z to +Z and the ball
goes to z −102, which is what the bounding box then read.

### `elbow end` is easy here and it was hard on the upper limb

The upper limb's elbow had to be found on two Ø4.4 pocket faces buried inside the fork's slot, in
a rear isometric, because the four pocket circles are concentric in an axial view and cannot be
told apart. The lower limb's elbow is the **outside** of the same joint: the Ø4 stub axle stands
1.6 proud on each blade face, and each end disc is the nearest surface along the view ray at the
hinge axis. So:

- **Front view** — the disc at y −6.6 is the front-most face at the axis. One click, off centre
  by (1.2, 0.8), reads `Face of add blade`.
- **Back view** — the same click reads the disc at y +6.6.

Two planar circular faces of equal area at y ±6.6 average to the origin, which is the hinge axis
by construction. Both picks are the same kind of entity, which is the trap the upper limb fell
into: an edge paired with a face averages an edge centre against a face centroid and lands 8 mm
off.

`wrist end` is one pick on the ball. A **convex** sphere offers its centre — this is the fourth
time that has held, and it is the exact opposite of the concave socket, which does not.

### The side-by-side is a composed figure, and it says so

`cad.parts.limbs.side_by_side.png` is not one CAD view. It is two Right-view screenshots, the
upper limb's resampled to the lower's scale, placed so both `elbow end` connectors sit on the same
row. Onshape cannot produce this picture from one Part Studio — the two limbs live in different
studios and only meet in the assembly, which is tutorial 13's work. What the figure shows is the
fork's slot, its detent bumps and its axle pockets facing the blade's stub axle and detent ring,
with the socket at one far end and the ball stud at the other.

### The traps this tutorial paid for

- **A view shortcut typed into a number field.** `Shift+1` and `f` pressed while the Extrude
  dialog's Depth field still had focus turned `#limbSeg` into `#limbSeg1f`, twice. The field does
  not reject it and the view does not change — the only tell is reading the value back. Blur
  first, or read `input_value()` before accepting.
- **`Meta+A` in a freshly clicked number field does not always select.** The first attempt left
  the old value in front of the typed one. `Meta+A` then `Backspace`, then check the field is
  empty, then type.
- **A Derive picks the whole studio unless you click the indented part row.** Clicking `hinge`
  brought in `blade` and `fork`; clicking `blade` under it narrowed to one.
- **`gui.ring` draws in the wrong place when it is given a `clip`.** It scales by
  `image width / window width`, which is the device pixel ratio only when the image is the whole
  window; with a 560-px crop the factor comes out 0.35 and the ring lands about a third of the way
  to the target. Reported, not fixed — the close-ups here are full-window frames.

### The two questions `11-l-limb.md` left open

- **"Whether this is a page or a section."** The moves are the upper limb's moves and the build
  took a fraction of the clicks, but three things here have no counterpart on the upper limb: the
  flip is argued from a different pair of connectors, `elbow end` is a two-view pick rather than a
  buried one, and the side-by-side is this tutorial's whole point. That is a **short page**, not a
  section — enough to stand on its own and short enough to lean on the page before it.
- **"Whether `#limbSeg` should differ between the two limbs."** It does not. One variable drives
  both extrudes, both read **48 mm**, and nothing in the build wanted them apart. Stickbot's 35.42
  and 37.91 stay what the plan called them: drift.

### The segment defect shows on this limb too

Same finding, same fix, its own numbers — see *the limb segment does not close, and it never has*
above. This limb's two joints stand off 44 and 10, so the segment came out **102** where
`make_plans.py` says 48.

### What is owed on tutorial 11

- Nothing was framed **as arrived**: every step was accepted before its shot. What exists is the
  finished part, both ends medium and close-up with a ring, the transform's two connectors, the
  depth field, the tree, the version dialog and the side-by-side.
- The mate connector glyphs are on in every frame. They are what these frames are about, but a
  page that wants a clean part hero will need one taken with them hidden.
- **`featureStatus` was never read.** Onshape's `/features` endpoint was rate limiting
  account-wide for the whole of this build and `onshape_session.RateLimited` fired after 110 s of
  backoff every time. What stands in for it: the tree frame shows no error badge on any of the ten
  rows, and every feature was checked by measurement — `/parts`, `/massproperties` and
  `/bodydetails` all answered normally throughout.

## Tutorial 12 — the gripper (`gripper` Part Studio)

The build ran in two sittings. The first stopped part-way through the opening sketch when the
Onshape session timed out; the second finished the part, rebuilt the sketch once for the reason
below, and published `t12 gripper` (`5324ccf7cef995c69366e6a6`).

### what is in the document

| # | Feature | Detail | Measured |
|---|---------|--------|----------|
| 1 | `#gripperL = #torsoH / 4` | 24 mm | |
| 2 | `#clipR = 5 mm` | LEGO-fixed, does not scale | |
| 3 | `#barD = 3.2 mm` | the LEGO bar | |
| 4 | `#bore = #barD + 0.1 mm` | 3.3 — `#fit` is deliberately *not* applied here | |
| 5 | `#mouth = 2.6 mm` | | |
| 6 | `#ball = #torsoH / 8` | 12 | |
| 7 | `#wall = #torsoH / 32` | 3 | |
| 8 | `#collarR = #ball / 2 + #wall` | 9 | |
| 9 | `copy socket` | Derived `ball and socket` → `Socket body`, **Base origin** | 1531.591; bbox x, y ±9, z −7.4 … +3.6 |

The rest of the tree is `clip profile`, `clip body`, `plane to cut top of clip`,
`remove top of clip`, `combine parts` and `mate to robot` — 19 rows with the default geometry, no
error badges, and **Parts (1)** named `Gripper`.

`Sketch 1`, the empty row the timed-out session left behind, is gone: the tree's 19 rows are the
four default-geometry rows, the eight variables and the seven features named above.

### the derive moved to the front, and that answers one of the plan's open questions

[`12-gripper.md`](../../../../build/plan/12-gripper.md) lists `copy socket` third and asks "whether
the derive moves earlier". **It should be first, and the measurement is the argument.** Derived at
Base origin the socket lands with its collar's bottom disc at z −7.4 and its ball centre at z 0 —
the wrist centre is on the origin without a single placing feature, which is exactly the frame
[`gripper.md`](../../../build-briefs/gripper.md) asks for ("build with the wrist center on the origin
and the gripper running downward"). Deriving first also means the plane that cuts the top of the
clip has a real face to sit on before the clip exists, so the cut is a dependency rather than an
offset number. `gripper mate point` is expected to be the same no-op the foot's `place socket`
was.

### the width has to be built from the collar, and Onshape will not let it be geometric

The lesson of this page is the body width: `stickbot` has **9.4** typed into the extrude, and the
same expression at draft9p0 gives **Ø18.0**, so the typed number went stale twice. The fix the
plan asks for is that the width "has to be built from the collar, not typed and checked".

**It can be built from the collar's numbers but not from the collar's geometry.** The width runs
along the extrude axis (X), and an extrude depth field cannot reference another body's diameter —
there is no "up to face" that works symmetrically about a plane. So the honest construction is
`#collarR = #ball / 2 + #wall`, the same expression the `ball and socket` studio uses, and an
extrude of `2 * #collarR`. Drive `#torsoH` and the clip's width follows the collar. That is the
whole point of the variable, and it is worth saying on the page that it is a *shared expression*,
not a shared face.

### two disagreements between the sources, found by reading before building

**The bore's axis.** [`make_plans.py`](../../../../../instructions/robot-guide/make_plans.py) draws
the gripper with its bore running fore-and-aft — line 964 says so in as many words: "the gripper's
bore runs fore-and-aft, so its hole stays a full circle".
[`gripper.md`](../../../build-briefs/gripper.md) lists the opposite as an acceptance check: "the
clip's bore axis is parallel to X, read off the model", and names the failure mode a Front-plane
build produces — it passes every other check
while gripping a bar that points away from the robot. **The build follows `gripper.md`**: sketch on
`Right` (YZ), extrude symmetric along X, bore axis along X.

**The stem's width in the sketch plane.** `make_plans.py`'s `clip()` draws the stem with
`rect(cx - 3, cy, 6, c - cy)` — a literal 6, which never doubled with everything else on
2026-08-23 and is now half the size its neighbours are. The build uses `2 * #clipR` (10) instead:
the stem is as wide as the clip head it grows out of, its sides meet the head at the head's widest
point, and there is no literal left in the sketch.

Both belong to B2.

### the overhang is real and is task #28

The socket's collar is Ø18 and the clip head is Ø10. Whatever the stem's width, the collar
overhangs it: at `2 * #clipR` the top face is 10 (Y) × 18 (X) and its corners at (±9, ±5) stand
10.3 from the axis where the collar's edge is at 9. **The outline is not flush and cannot be made
flush by choosing a width** — the top of the clip is flush with the *edge* of the socket in Z,
which is what the plane on the collar's bottom face gives, and that is all the acceptance check
asks for. Making the body follow the socket's outside profile is task #28 and is a different
feature (a loft or a revolve), not a number.

### the mouth was built backward, because the brief says the wrong sign

The clip came off the sketch with its mouth opening **+Y** — built exactly as
[`gripper.md`](../../../build-briefs/gripper.md)'s build order says: "the mouth opens forward (+Y) and
the gripper runs down (−Z)". Measuring the finished part is what caught it. The two lips ran
y +1.0161 … +5.0 and y +1.0161 … +4.828, which is toward the back of the robot, because
[`build-briefs/README.md`](../../../build-briefs/README.md) settles the frame in one line: "**The
robot faces −Y.**" A hand that grips behind itself is not a hand.

`gripper.md`'s "(+Y)" is the stale half of the pair. It is a source disagreement, so it is written
here and the brief is left alone; fixing it belongs to whoever next edits the briefs. The build
follows the README.

`clip profile` was rebuilt rather than mirrored, so the sketch reads the way the page will teach
it: a rectangle from (−5, 0) to (5, −17.7) with its top edge on the horizontal axis, two concentric
circles at (0, −19), a lip line at z −20.3, then seven trims. Six dimensions hold it —
`2 * #clipR`, `#bore`, `#gripperL - #clipR`, one `#clipR`, `#mouth / 2` and `#mouth` — and it comes
up fully constrained.

**One `#clipR` is enough, and the second one will not solve.** The vertical axis to the rectangle's
left line is the only distance worth typing: the outer circle is tangent to both sides, so the
right line follows from it. Dimensioning the right line as well makes the sketch over-defined, and
Onshape reports it as "Sketch could not be solved" rather than as a redundancy. Undo removes one
step, not the pair — click the offending dimension's label and press Delete.

The rebuilt part is the exact mirror of the first one about the XZ plane and its volume is
unchanged at **4006.738 mm³**, which is the evidence that nothing else moved.

### a re-solved extrude gets a new body id, and two downstream features lose their grip

`remove top of clip` and `combine parts` both failed after the sketch rebuild — "Missing Part of
clip body" and "Missing Part of remove top of clip". Nothing about them was wrong; the extrude
handed back a body with a new id and the picks pointed at the old one. The repair is to open each
feature, click the × on the missing reference and re-pick the body in the graphics area. The split's
three checkboxes have to be read again afterwards: **Keep tools** on, **Trim to face boundaries**
off, **Keep both sides** off.

This is worth a line on the page. A student who edits a sketch will hit it, and the red rows look
far worse than they are.

### `gripper mate point` was not built, and that is the third time

The plan's step table lists `socket.connector` → `gripper mate point`. It is a no-op here for the
same reason it was dropped from tutorials 10 and 11: `copy socket` derives at Base origin, which
already puts the wrist centre on the studio origin, so there is nothing for a connector-to-connector
transform to move. Three tutorials in a row is a pattern rather than an accident — the derive is
the placement.

It costs the page one figure. "The transform's connectors, close-up with a ring" has no subject,
so it is not in `images/gripper/`.

### the 0.172 ledge, and where it sits

The stem's flat side is tangent to the Ø10 clip circle at the equator, but the stem stops
`#mouth / 2` above the circle's centre, so its bottom corner lands 5 − 4.828 = **0.172** outside the
arc. It is inherent in the profile, not a mistake, and it is too small to print away.

Rebuilding the mouth onto −Y moved it from the front of the gripper to the **back**, which is the
better of the two places for it.

### the collar-to-clip step measured, and it changes sign around the joint

[`gripper.md`](../../../build-briefs/gripper.md) asks for the step's shape rather than a single number,
and expects it to be irregular and worse than the foot's. It is irregular, and it is stranger than
that: **the step reverses**.

- Fore and aft, the Ø18 collar overhangs the 10-deep stem — two crescents of 42.106 mm² each at
  z −7.4, running 4.0 deep at the center line and tapering to nothing at x ±7.4833.
- At the ends, the 18-long stem overhangs the collar — four tongues of 2.436 mm² each, reaching
  5 mm of overhang out at x ±9.

So from the Right view the joint has a visible lip and from the Front view it is flush, which is
why both frames are in the guide. That is the evidence for task #28: the fix is a feature that
follows the collar's outside profile, and no choice of stem width reaches it.

### what could not be captured

- **The hero holding a LEGO bar.** There is no bar in the document and modeling one is not one of
  tutorial 12's steps. `hero.png` is the gripper alone.
- **The transform's connectors.** No subject, per `gripper mate point` above.

## Tutorial 13 — one arm, then the other by copy (`stickbot` Assembly)

Built in one sitting on 2026-08-24 and published as `t13 arms` (0be0c433c7c1f3f8847ea7e5). The
assembly went from two instances and one mate to eight instances and seven mates. Five of those
mates are Ball and two are Revolute.

### what is in the assembly now

Read back from `/api/assemblies/.../?includeMateFeatures=true`, which answers while the feature
endpoints are rate limited:

- Instances (8) — `torso <1>`, `head <1>`, `u limb <1>`, `l limb <1>`, `Gripper <1>`,
  `Gripper <2>`, `l limb <2>`, `u limb <2>`
- Mate features (7) — `head to neck` BALL, `left shoulder` BALL, `left elbow` REVOLUTE,
  `left wrist` BALL, `right elbow` REVOLUTE, `right wrist` BALL, `right shoulder` BALL

The two limbs and the gripper on the right side were never inserted. They arrived by copy and
paste, and two of the three mates arrived with them.

### the copy carries mates, and the proof is a count taken twice

This is the whole lesson of the tutorial, and `13-assembly-arms.md` says so: *"The mate list before
and after is the whole proof."* So it was counted before and counted again after, in the same
panel, one paste apart:

| | before the paste | after the paste |
| --- | --- | --- |
| Instances | 5 | 8 |
| Mate features | 4 | 6 |

Three instances in, two mates in, from one paste. `left elbow` and `left wrist` were duplicated;
`left shoulder` was not. The rule that explains it is that a mate comes along when **both** of its
sides are in the selection. The elbow joins the lower limb to the upper limb and the wrist joins
the gripper to the lower limb — both ends of each are in the three parts that were copied. The
shoulder joins the upper limb to the **torso**, and the torso was not copied, so that mate had
nowhere to land and was dropped.

That makes the seventh mate the only one a student builds by hand on the second arm.

### the pasted mates are named `left elbow (1)`, and they should not stay that way

Onshape names a duplicated mate after its original with a number in brackets. So the right arm
arrived carrying `left elbow (1)` and `left wrist (1)`, which is wrong on the face of it — they are
on the right. Both were renamed to `right elbow` and `right wrist`.

`copy.tree.after.png` was taken before the rename and shows the bracketed names, because that is
what a student sees. `tree.png` was retaken after and shows the seven finished names.

**The rename happened after `t13 arms` was published**, so that version carries `left elbow (1)`
and `left wrist (1)`. The workspace is correct and tutorial 14's version will carry the correct
names. Nothing downstream reads a mate by name.

### the four questions `13-assembly-arms.md` left open, answered by doing it

- **Does the selection have to be in the graphics area or in the list?** The instance list works,
  with `Meta+click` to add to the selection. The graphics-area route was not tried, so the page
  teaches the list and does not claim the other one fails.
- **Where do the pasted instances land?** Offset up and to the right of the originals, clear of the
  robot and clear of each other. Not on top of the originals and not at the origin. They are easy
  to see and easy to grab.
- **What are they called?** The same names with `<2>`, and they appear in the list in the reverse
  of the order they were selected — `Gripper <2>`, `l limb <2>`, `u limb <2>`.
- **Is the shoulder mate carried?** No. See the count above.

### mirrored or parallel stops mattering at a Ball mate

The plan asks whether the copy arrives mirrored or parallel. It arrives **parallel** — a copy is a
copy, not a mirror, so the right arm starts out pointing the same way as the left one.

It does not matter, and the reason is worth writing down. A Ball mate constrains three
translations and leaves all three rotations free. Mating the copy's `shoulder end` to the torso's
`r shoulder connector` puts the two origins on top of each other and says nothing about which way
the arm faces. So the handedness of the connector frames never comes up, and the arm just hangs.

Where it would come up is a Fastened or a Revolute mate, and there is one of those on this arm —
the elbow. It came in already made, from a copy of a working joint, so its axis is right by
construction. A student who built the second elbow by hand could get it backwards.

### the wrong connector is one row away, on every part

Every part in this tutorial carries a mate connector left over from how it was built, sitting in
the list beside the one the student wants:

- `u limb` — `socket connect to robot` next to `shoulder end`
- `l limb` — `axis for circular patterns` and `blade to robot connector` next to `elbow end` and
  `wrist end`
- `Gripper` — `socket connect to robot` next to `mate to robot`

Picking one of those gives a mate that solves and puts the part in the wrong place, which is worse
than a mate that fails. The page names the connector to pick at every step for this reason.

### inserted from the workspace, not from a version

`assembly.md` is plain about this: *"You insert from versions, not from workspaces."* That is not
what was done. The Insert dialog's **Current document** tab lists the Part Studios in this document
and offers no version picker — clicking "Main" opens nothing. The parts went in from the workspace.

It matches how `torso` and `head` got into this assembly back at tutorial 3, so the assembly is at
least consistent with itself. The cost is that the assembly follows the workspace: change a Part
Studio and the robot changes under you. That is convenient during a build and wrong for a
published guide. Recorded here rather than fixed, because fixing it means re-inserting eight
instances and rebuilding seven mates.

### no Width mates on the elbows

`assembly.md` asks for a Width mate per hinge and says *"A Width mate is not optional decoration on
a hinge"* — it is what keeps the blade centered in the fork with 0.6 mm of clearance each side. The
step table in `13-assembly-arms.md` does not list one, and run 4 did not build them either.

They were not built here. Without them the Revolute at each elbow leaves the blade free to slide
along its own axis, so the arm can be pushed a little sideways in the fork. Two of the three
sources want it and the one that drives the tutorial does not; this is the third source
disagreement in this build and the second one on a hinge.

### the arms move, and they move differently at each joint

Dragging is how the page shows a Ball and a Revolute are not the same thing. Three poses were
caught: the arm raised, the arm straight down, and the arm folded across the torso. The shoulder
swings in any direction and the elbow only folds, which reads immediately once you have dragged
both.

The pose across the torso is also evidence for the interference question in `assembly.md` — the
arm reaches the front of the torso and the gripper passes over it. Measuring the angle at which
they touch is B2's job.

### the bounding box is pose-dependent, and only one number is not

Read back from `/api/assemblies/.../boundingboxes`, in metres:

```
lowX -0.06155086455914865  lowY -0.19179698806631318  lowZ -0.20716452326122958
highX 0.06195245258757624  highY 0.03  highZ 0.13740000000000002
```

`highZ` = 137.40 mm is the top of the head, and it matches the register. Everything else is where
the arms happened to be left. There are no legs yet, so `lowZ` is a hanging gripper and not a foot.
A standing-height check has to wait for tutorial 14.

### the model is saved with the left arm posed

The drag that was meant to put the arm back at rest did not take, and it was left. It is cosmetic —
a mate-solved position, not geometry — and any student's assembly will be posed differently
anyway. It is visible in `hero.png`.

### two traps that cost time

- **A killed script can leave the mouse button down.** A Bash timeout between `page.mouse.down()`
  and `page.mouse.up()` leaves the button held, and every later `mouse.move` drags whatever is
  under the cursor. Two attempts to zoom in on the elbow produced new arm poses instead. The cure
  is a script whose first call is `page.mouse.up()`; the prevention is `try/finally` around every
  drag, which still does not survive a SIGTERM.
- **Mate connector glyphs cannot be hidden in an assembly.** They are on in every frame in this
  tutorial. In a Part Studio they can be turned off; here they cannot, so the close-ups have to be
  framed to keep the glyph that matters legible among the ones that do not.

### what could not be captured

- **The graphics-area selection route.** Not tried, so there is no frame of three parts selected in
  the graphics area. `copy.selected.png` shows the instance-list selection, which is the route the
  page teaches.
- **A rest pose.** See above.

## Tutorial 14 — one leg, then the other by copy (`stickbot` Assembly)

Built on 2026-08-24 and published as `t14 legs` (737db64e2567c96e2d3de63f). The assembly went from
eight instances and seven mates to fourteen and thirteen. The robot is complete, and it stands.

### what is in the assembly now

- Instances (14) — `torso <1>`, `head <1>`, `u limb <1>`, `l limb <1>`, `Gripper <1>`,
  `Gripper <2>`, `l limb <2>`, `u limb <2>`, `l limb <3>`, `u limb <3>`, `Foot <1>`, `Foot <2>`,
  `l limb <4>`, `u limb <4>`
- Mate features (13) — `head to neck` BALL, `left shoulder` BALL, `left elbow` REVOLUTE,
  `left wrist` BALL, `right elbow` REVOLUTE, `right wrist` BALL, `right shoulder` BALL,
  `left knee` REVOLUTE, `left ankle` BALL, `left hip` BALL, `right knee` REVOLUTE,
  `right ankle` BALL, `right hip` BALL

Nine Ball and four Revolute, which is exactly what
[`assembly.md`](../../../build-briefs/assembly.md) says a finished robot has. That brief was
written before anything was built; this is the first time the count has been read off a model.

### the copy carries mates, counted twice more

Tutorial 13 proved the rule once. Tutorial 14 uses it twice, and the counts were taken across each
paste:

| | before | after | what came along |
| --- | --- | --- | --- |
| copy an arm's two limbs | 8 instances, 7 mates | 10 instances, 8 mates | the elbow |
| copy the whole first leg | 11 instances, 10 mates | 14 instances, 12 mates | the knee and the ankle |

The first copy takes `u limb <1>` and `l limb <1>` — an arm's two limbs, with the gripper left
behind — and gets back a jointed pair. The mate that came with it was `left elbow (1)`, because
both of its ends were in the selection. The shoulder was not carried, for the same reason it was
not carried in tutorial 13: its other end is the torso.

**A limb pair copied off an arm is a leg.** Nothing about the two limbs is arm-specific. The
elbow mate that came along becomes the knee, and renaming it is the whole conversion:
`left elbow (1)` → `left knee`.

The second copy takes all three of `u limb <3>`, `l limb <3>` and `Foot <1>` and gets the knee and
the ankle with them, arriving as `left knee (1)` and `left ankle (1)`. The hip was dropped. Both
were renamed, to `right knee` and `right ankle`.

### the copy arrives parallel, not mirrored, and does not need turning

`14-assembly-legs.md` asks whether a leg copied from an arm needs turning. It does not, and the
reason is the same one that made handedness a non-question at the shoulder in tutorial 13: **a Ball
mate constrains three translations and leaves all three rotations free.** The hip mate pins one
point of the upper limb to one point of the torso and says nothing about which way the limb points.
Whatever orientation the pasted pair happens to arrive in, the first drag puts it where it belongs.

There is no Mirror in this tutorial and there does not need to be one.

### where the paste lands is a view, not a fact

`arms.rst` said the copy lands "up and to the right of the original, clear of the robot". That was
true of the frame it was written from, and it is not a property of the paste. The leg paste landed
overlapping the robot in one view and half off the screen in another, on the same document, minutes
apart. The offset is applied in screen space, so what a student sees depends on where they had the
camera. `arms.rst` was corrected to say the copy lands offset from the original and may overlap the
robot or sit off the edge of the screen.

### a free-floating jointed pair cannot be posed at its joint

`14-assembly-legs.md` asks for a frame of *"the same pair dragged at the knee, before it is mated
to anything"* and calls the floating-but-jointed pair *"the frame this whole tutorial is built
around"*. The first half was captured — `pair.floating.png` and `pair.floating.closeup.png` show
the pair off on its own with a working knee in it. The second half could not be.

Three attempts, from the Front view, the Left view, and in two perpendicular drag directions, all
translated the whole pair instead of bending it. The reason is that the pair is completely
unconstrained: nothing is grounded, so the solver can satisfy a drag by moving both limbs together,
and translation is the cheaper answer than rotating one about the knee. The knee is real; there is
just no reason for the solver to use it.

The proof was taken instead one step later, after the hip mate grounds the upper limb to the torso:
`knee.straight.png` and `knee.bent.png` are the same leg before and after a drag at the ankle, and
the only thing that changed is the knee angle. `pair.bent.png` and `pair.bent.closeup.png` are the
floating pair as it arrived, which is already bent, so a page can show that the joint is there
without claiming a student can drive it.

**Write it as: mate the hip first, then bend the knee.** That is also the more useful order, because
a leg mated at the hip is a leg that hangs where it should.

### the robot stands, and it is 421.8 mm tall — and the bounding box does not say so

The assembly bounding box, with the legs down, reads:

```
highX  68.45   highY  36.99   highZ  137.40
lowX  -61.55   lowY -64.86    lowZ  -294.57
```

which is 431.97 top to bottom. **That is not the robot's height, and it took B2 to catch it.**
`lowZ` is not a sole sitting flat — both feet are tilted, 12.74° and 9.60° measured off their
occurrence transforms, and a tilted 96 × 48 sole drops a corner further below its ball centre than
`FOOT_H` ever does. The 34.4 mm that looked like a deep foot was that corner.

The height that means something is added from the parts, each read off its own studio:

| station | z | from |
| --- | --- | --- |
| head top | +137.4 | `head`; `HEAD_T` agrees exactly |
| hip ball | −58.0 | `body` |
| knee pin | −158.4 | the `u limb` pin axis at −100.4 |
| ankle ball | −260.4 | the `l limb` ball stud at −102 |
| sole | −284.4 | the `foot` box, −24.0 … 3.6 |

**421.8 mm**, which is what [the register](../register.md) predicted by arithmetic before any of it
was measured. [`assembly.md`](../../../build-briefs/assembly.md)'s 315.4 is a 1× number that
survived the 2× pass, and all 106.4 mm of the gap is the two limb segments — 100.4 and 102 where
`LEG_SEG` is 48. **`FOOT_H` is exactly right at 24.**

I wrote the 431.97 into the register and into `legs.rst` before checking it, one paragraph after
writing down that a posed assembly cannot be measured for symmetry. The rule is the same rule.

### a posed assembly cannot be checked for symmetry, or for height

`assembly.md` asks for feet 8 mm outboard with their inner edges at x = ±8. The feet as built sit
at

```
Foot <1>  x =  26.05   y = 0.88   z = -259.73
Foot <2>  x = -31.42   y = 0.04   z = -260.18
```

which is neither symmetric nor 8. That is not a defect. Every joint down each leg is a free Ball or
a free Revolute, so the feet go where the last drag left them; the two z values agreeing to 0.45 mm
is the honest reading of "both legs are the same length". A symmetry check would need the mates
driven to a named pose, which nothing in this build does. **The acceptance check as written cannot
be run against a posed assembly and should say what pose it means.**

The feet do point −Y, which is the way the robot faces. That much was confirmed from the Right
view.

### no Width mates at the knees either

The same deviation recorded for tutorial 13's elbows applies to tutorial 14's knees.
`assembly.md` says *"A Width mate is not optional decoration on a hinge"* and asks for one per
hinge with 0.6 mm clearance each side. `14-assembly-legs.md`'s step table does not have a Width
step, and neither knee got one. The revolute alone leaves the lower limb free to slide sideways
inside the fork. Run 4 skipped this too, so it is now three tutorials deep and belongs in a fix
rather than in a page.

### inserted from the workspace again

The foot was inserted the same way the limbs and grippers were: from the Insert dialog's **Current
document** tab, which lists Part Studios from the workspace and offers no version picker.
`assembly.md` says *"You insert from versions, not from workspaces."* Doing it that way needs the
**Other documents** route, which is a different dialog and a different set of clicks. The deviation
is recorded, not fixed, for the same reason it was in tutorial 13: changing it now would invalidate
every insert frame in three pages.

### what could not be captured

- **A drag at the knee before any mate.** See above — it is not a capture failure, it is a thing
  that does not happen.
- **Nothing, in the end.** `copy2.tree.after.png` is clipped before `left knee (1)` and
  `left ankle (1)`, and it cannot be retaken because the mates have since been renamed — but the
  full-window `copy2.paste.graphics.png` was taken at the same moment and does carry both bracketed
  names under `Instances (14)` and `Mate features (12)`. The page uses that one and leaves
  `copy2.tree.after.png` unused. `copy1.tree.after.png` covers the first paste the same way.

## After the build — B2 and B3

The model was read back and checked against `make_plans.py`, and then driven from its variable
table. Neither is a build step and neither belongs in this log; they have their own files.

- [`b2-readback.md`](b2-readback.md) — every part measured against the sheets. It withdrew the
  431.97 mm height and the foot defect that followed from it, both of which this log had recorded
  from a posed assembly's bounding box.
- [`b3-driving.md`](b3-driving.md) — `#torsoH` 96 → 120 → 96 and `#torsoW` 72 → 90 → 72. Both round
  trips came back identical, and four numbers turned out to be typed where a variable belongs.

**The one thing worth carrying forward into a build.** Three of B3's four findings are the same
mistake: a sketch reached for `#ball` or `#torsoH` because at 96 it had the right value, not because
it was the right number. Every one of them measures correctly at the size the robot was drawn. The
habit that catches this is to drive the variable before publishing the version, not after the guide
is written.
