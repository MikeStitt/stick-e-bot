# 2. The head

Starts from the torso box. Ends with a head — no socket, because the joint does not exist yet.

## The steps

**`state: published`** for every step below.

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.head.tab` | make a Part Studio and name it `head` | the element — no feature |
| `cad.parts.head.width_variable` | `#headW`, before there is an outline to size | `#headW` |
| `cad.parts.head.profile_sketch` | the head's outline | `head profile` |
| `cad.parts.head.depth_variable` | `#headD`, the number the extrude is about to ask for | `#headD` |
| `cad.parts.head.body` | extrude it `#headD`, name the part, hide the planes | `head body` |
| `cad.parts.head.round_variable` | `#round` | `#round` |
| `cad.parts.head.upper_rounds` | round the two arch edges | `upper rounds` |
| `cad.parts.head.chamfer_variable` | `#chamfer` | `#chamfer` |
| `cad.parts.head.lower_chamfer` | chamfer the bottom | `lower head chamfer` |
| `cad.parts.head.eye_variables` | the four the eye is drawn from | `#eyeX`, `#eyeUp`, `#eyeRx`, `#eyeRy` |
| `cad.parts.head.eye_sketch` | one eye | `eye profile` |
| `cad.parts.head.face_variable` | `#face`, how far the eye stands proud | `#face` |
| `cad.parts.head.eye_cut` | extrude it `#face` — **`Add`**, not a cut | `eye` |
| `cad.parts.head.mirror_eye` | mirror the feature for the second | `second eye` |
| `cad.parts.head.mouth_variables` | the three the mouth is drawn from | `#mouthW`, `#mouthH`, `#mouthDn` |
| `cad.parts.head.mouth_sketch` | the mouth | `mouth profile` |
| `cad.parts.head.mouth_cut` | extrude it `#face` — `Remove` | `mouth` |

**`cad.parts.head.variables` is gone, and the seven steps above replace it.** It typed all twelve
numbers into an empty tab before anything was drawn, which is the longest stretch in the robot with
nothing on screen. Frames, logs and pages written under the old identifier stay findable through
this note — [`../steps.md`](../steps.md) § *Renaming and supersession are pointers, not states*.

### The numbers the head owns

`head` was the only Part Studio declaring nothing. Its profile read `#torsoH` out of the Variable
Studio and its face and its depth were typed.

**All twelve are the head's own, and none is a `robot sizes` row**, because one tab reads them. The
*typed at* column is the step each one goes in at, and it is the feature about to read it.

| variable | expression | mm | typed at |
| -------- | ---------- | -- | -------- |
| `#headW` | `#torsoW` | 72 | `width_variable` |
| `#headD` | `#torsoD * 5 / 4` | 60 | `depth_variable` |
| `#round` | `#headW / 6` | 12 | `round_variable` |
| `#chamfer` | `#headW / 12` | 6 | `chamfer_variable` |
| `#eyeX` | `#headW / 6` | 12 | `eye_variables` |
| `#eyeUp` | `#headW / 9` | 8 | `eye_variables` |
| `#eyeRx` | `#headW / 9` | 8 | `eye_variables` |
| `#eyeRy` | `#headW / 18` | 4 | `eye_variables` |
| `#face` | `#headW / 24` | 3 | `face_variable` |
| `#mouthW` | `#headW * 5 / 9` | 40 | `mouth_variables` |
| `#mouthH` | `#headW * 5 / 36` | 10 | `mouth_variables` |
| `#mouthDn` | `#headW * 13 / 72` | 13 | `mouth_variables` |

**Every one of them is read by the feature directly under it in the tree**, which is what the
column is for. It was measured off the construction record rather than decided here: the
expressions in `head.features.json` say which feature first names each variable, and the four eye
numbers come out as one group because `eye profile` reads all four.

**`#face` is typed between the eye's sketch and the eye's extrude**, not with the eye's other four.
It is a depth, the sketch has no depth, and the extrude is the first thing that asks for it. The
mouth's `Remove` reads it again and types nothing.

**The head is as wide as the body, and that is `#torsoW`, not `0.75 × #torsoH`.** Both are 72 here.
Driving `#torsoH` to 120 under the second reading gives a head 90 across on a torso 72 across, and a
head wider than the torso it sits on is not a robot any more. The profile keeps its two dimensions —
radius `#headW / 2` and length `#headW / 2` — and those are what make the front square, so there is
no `#headH`.

**`#face` is one number doing two jobs.** The eye is an `Add` standing `#face` proud of the front
face and the mouth is a `Remove` cutting `#face` into it. They were built at 1.5 in stickbot and at
3 in draft9p0, so they have moved together twice already without anyone writing down that they are
the same number.

**`#round` is `upper rounds`, and it was the last typed number on the head.** The plan typed 6 and
draft9p0 built 12; nobody decided that, the builder doubled it with everything else. `#headW / 6`
reproduces both. It also keeps the eye clear of the fillet by construction: the fillet eats the
front face down to `#headW / 2 - #round` = 24 and the eye reaches `#eyeUp + #eyeRy` = 12, and both
sides of that are fractions of `#headW`.

**The fillet's limit is the depth, not the width.** `#headD` follows `#torsoD` and `#round` follows
`#torsoW`, so the two arch edges need `#torsoD` to stay above `#torsoW / 3` — 48 against 24 here.
Below that the head's top becomes one full round.

**`cad.parts.head.tab` was missing from the plan and is in the build.** The head is the first part
that needs a Part Studio of its own, and the rename has to happen before any frame that shows the
tab strip. Three frames.

**`cad.parts.head.eye_cut` misnames what it does.** The feature is an `Add` extrude that stands the
eye 3.0 mm off the face; nothing is cut. The identifier is kept because the frames on disk carry it
as their stem, and the plan says so here rather than pretending otherwise.

**The eye is an ellipse, and this page has carried its numbers since draft9p0.** The read-back
below records `eye profile` as `HORIZONTAL`, major 8 mm, minor 4 mm, 6 across and 4 up at the
example's size. `make_plans.py` drew a circle at `2/9` and `5/36` instead, and the built head
followed the sheet rather than this page. draft9p1 doubles what is written here — **major 16, minor
8, centered 12 out and 8 up** — which also takes the eye out of `upper rounds`; the arithmetic is
[`../../experiments/runs/2026-08-25-draft9p1/a3-eye-ellipse.md`](../../experiments/runs/2026-08-25-draft9p1/a3-eye-ellipse.md).

**There are no pupils, and there never were.** `make_plans.py` drew a circle inside each eye and
the sheet labeled it *eye and pupil*, but no head in this repository has one and the example
stickbot's head goes `eye profile` → `eye` → `second eye` → `mouth profile` → `mouth`. The circle
could not have been built either: its radius was `#headW / 18`, which is `#eyeRy`, so it touched
the eye ellipse top and bottom and left no eye above it or below it. A pupil that a student could
build wants a radius under `#eyeRy` — `#eyeRy / 2` leaves a 2 mm ring — and adding one back is one
circle in `eye profile` and one extrude.

**The part rename and the plane hiding ride along with `cad.parts.head.body`.** Neither adds a
feature, both are frames the page needs, and neither is worth a step of its own.

## The shots this tutorial needs by name

**Requirements in play.** `req.model.named_features` — this is the first tutorial with a Part
Studio of its own, so the tab rename has to happen before any frame shows the tab strip.
`req.shot.true_state` — the slot's own dimensions were reshot once because a frame showed a state
the build never passed through.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the hero | the head, no socket | `req.page.hero` |
| the fillet's edges, medium and close-up with a ring | picking the wrong edge is silent, and a fillet's edge set is the classic wrong pick | `req.shot.two_frame` |
| the chamfer's face, picked and ringed | which face was picked is what decides whether one pick or eight | |
| the mirror plane, picked | which plane makes the second eye land where the first one is | |
| the slot's own diameter label, parked off-screen | the tool makes a dimension nobody asked for and hides it four radii away | `req.shot.true_state` |
| the tree | at the end | |
| the version dialog | publishing | |

**The two-frame rule reaches edges, not only points.** An edge at medium range is a line among
lines; the ring is what says which one. `upper_rounds` carries the pair: a medium frame with both
rim arcs lit and a ringed close-up of the front one.

**The chamfer takes a face, so it is one ringed frame rather than a pair.** The step picks the
bottom face itself and bevels every edge of it in one go, and a face lit orange is not a line among
lines. The row above says what it shows instead of asking for a close-up of an edge the build never
picks.

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 2 - the head** (`188f791a4811291943e59b84`). Its `head` Part Studio holds the twelve
variables interleaved in the order the steps table gives: `#headW`, `head profile`, `#headD`,
`head body`, `#round`, `upper rounds`, `#chamfer`, `lower head chamfer`, `#eyeX`, `#eyeUp`,
`#eyeRx`, `#eyeRy`, `eye profile`, `#face`, `eye`, `second eye`, `#mouthW`, `#mouthH`, `#mouthDn`,
`mouth profile`, `mouth`. The tab carries tutorial 5's `socket mount point`, `get socket`,
`drop socket to neck`, `add socket to head` and `head mate` after those, because the document
branches draft9p3 with the whole robot in it.

**The end-of-tutorial-2 numbers are measured in `stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)), at its own version
**tutorial 2 - the head**, because that document holds nothing past this page. Its `head` tab is
the twenty-one rows above and no more, with one part named `head` and no error row: bounding box
`lowX -36 / highX 36`, `lowY -33 / highY 30`, `lowZ -36 / highZ 36` mm, which is 72 × 63 × 72 mm;
29 faces — 14 plane, 7 cylinder, 4 cone, 2 extruded, 2 torus. All three sketches are fully defined.

**The numbers behind those faces.** `head body` is a symmetric extrude `#headD` deep; `upper rounds`
is a `#round` fillet on the two rim arcs, which tangent propagation carries down both straight
sides; `lower head chamfer` is `#chamfer` at 45 deg on the bottom face; `eye` is an `Add` extrude
`#headD / 2 + #face` deep and `mouth` a `Remove` extrude `#face` deep started `#headD / 2` off the
plane; `second eye` is a feature mirror about `Right`. `head profile` carries `COINCIDENT ×5`,
`HORIZONTAL ×3`, `VERTICAL ×2`, `RADIUS ×1` and `LENGTH ×1` — **both** sides carry `VERTICAL`.
`mouth profile` carries the line's `LENGTH`, two `DISTANCE` constraints from the origin to the
line's left end, and the `DIAMETER` the Slot tool wrote itself, edited to `#mouthH`.

**Nothing on this page is typed as a length.** `#headW` is `#torsoW` and `#headD` is
`#torsoD * 5 / 4`, and the other ten are written from `#headW`, so changing `#torsoW` in
`robot sizes` moves the eyes, the mouth and the rounds with the box.

**The head's underside is `#headW × #headD` and the torso's top face is `#torsoW × #torsoD`,** so
the head hangs 6 mm over the torso's front face and 6 mm over its back. That overhang is what
[`../../experiments/build-briefs/head.md`](../../experiments/build-briefs/head.md) works the neck's
tilt from, and tying the depth to `#torsoD` keeps it a fixed proportion at every size.

**There is no shell.** The brief describes one and no head in this repository has ever had one, so
none was built.

**Slot makes its own pick.** Its tooltip reads *create a slot around continuous sketch entities*: it
wraps a line already drawn. A line left selected when the tool arms sends it straight past the pick
and into setting the width, so the click meant for the line sets a width of nothing and the tool
drops. It also writes its own `DIAMETER` constraint as it builds and parks the label four radii
above a round end; editing that label is what sets the width, and adding a second width dimension
over-constrains the sketch.

**Measuring the mouth's drop to the line cannot be solved.** Picking the line and the origin asks
for the shortest distance from a point to a segment; Onshape takes the constraint and then refuses
to solve the sketch. Both position dimensions run from the origin to the line's **left end**.

## Captured

**`instructions/stickbot-draft9p4/source/head.rst`**, written from the 72 frames in
`instructions/stickbot-draft9p4/source/images/head/`. Sphinx builds the page with no warning; every
frame on disk is used and every frame the page names is on disk.

**None of draft9p3's head frames carried.** Every one of them shows the feature list with the twelve
numbers in a block at the top of the tab, which is the ordering this draft replaced, so the whole
page was recaptured by following it into `stickbot-draft9p4-check` step by step. That is also why
the frames come from the check document rather than the build one: the build document's `head` tab
already carries tutorial 5's socket.

**Two toolbar frames were deleted rather than shipped.** `tb-variable.png` and
`tb-plane-variable.png` showed a Variable button on the Part Studio toolbar. There is none at this
window width — hovering x 1020 to 1320 at y 58 gives `Move face`, `Replace face`, `Plane`, `Frame`,
`Sheet metal model` and `Add custom features` — and `Default geometry`'s right-click menu has no
`Variable` either. The page reaches the tool through **Search tools**, or **alt/⌥+c**.

**Three frames were retaken because the page had the clicks wrong**, and the run is what found it:
`profile_sketch-06` and `-07` now show **both** sides picked and both carrying a vertical marker,
and `upper_rounds` was rebuilt from two rim-arc picks after the first run's single pick landed on
the arch's top face. The face pick gives the same 12-face head, which is what made it silent.

## What we do not know yet

**Whether the face gets built here or later.** Eyes and mouth are cosmetic and could move to the
end of the whole build as a decorating tutorial. They are here because they are in stickbot's tree
here, and moving them is a paragraph move, not a rebuild.

**Whether the head is shelled.**
[`../../experiments/build-briefs/head.md`](../../experiments/build-briefs/head.md) specifies a
1.2 mm shell in its table and no step that builds one, and no head in this repository has ever had
one. The brief's row says so now; what a hollow head would be for is still open.
