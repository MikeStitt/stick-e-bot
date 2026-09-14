# Run 7 — rebuild the ball and socket, and write guide3's page from the build

A spike. Build the ball and socket again from an empty document, applying everything found since
2026-08-16, then write `instructions/robot-guide3/source/ball-and-socket.rst` from what was actually
done.

Nothing is copied from `ball-socket-run6p2`. A rebuild that starts by opening the old document is
not a rebuild — and two of the changes below alter the model, so that document could not have
supplied the page anyway.

## Where the work is

Onshape document `run7-ball-and-socket`, version **`run7-ball-and-socket-v1`**
(`a23b8fd563f57b540fb9fff9`), document `57ff951a90b8fb48bd644b0a`. Eight features, two named parts,
every feature `OK`.

## The brief

Numbers come from [`target.json`](../2026-08-14-run6/target.json) and are not restated here. The
model turns them into Onshape variables, which is the part that is new:

| Variable | From | Drives |
| --- | --- | --- |
| `#ball` | `BALL` | the ball's diameter |
| `#stalk` | `STALK` | the stalk's diameter |
| `#fit` | `FIT` | the gap between ball and cavity |
| `#wall` | `COLLAR_WALL` | collar thickness outside the cavity |
| `#collar` | `COLLAR_L` | collar length |
| `#grip` | `GRIP` | how far the collar reaches past the ball's center |
| `#slit` | `SLIT_W` | slit width |
| `#stud_len` | chosen, 5 | the stud's top face above the ball's center |

Everything else is derived in the field rather than typed: the cavity is `#ball + 2 * #fit`, the
collar outside diameter is `#ball + 2 * #fit + 2 * #wall`, and the collar's second depth is
`#collar - #grip`. Guide2 typed 6.4 and 9.4 and 4.15 as literals, which is what
[`.parts/modeling-practice.md`](../../../.parts/modeling-practice.md) exists to prevent.

## Build order

| # | Feature | Plane or face | Notes |
| --- | --- | --- | --- |
| 1 | Variables | — | the table above |
| 2 | `stud profile` sketch | Front plane | arc, three lines, three dimensions |
| 3 | `revolve stud` → `Ball stud` | — | select the sketch, then `Shift+W`; `Shift+7` after |
| 4 | `collar profile` sketch | Top plane | **Center point circle**, driven by `#ball`/`#fit`/`#wall` |
| 5 | `collar blank` extrude → `Socket body` | — | `#grip` and `#collar - #grip` |
| 6 | `cavity from ball` boolean | — | offset `#fit`, **Keep tools** on |
| 7 | `slit profile` sketch | **collar's top face** | two crossing **Center point rectangle**s, two dimensions each |
| 8 | `relief slits` extrude | — | **Remove**, downward, depth `#collar - #wall`, scoped to `Socket body` |

## Every change since 2026-08-16

The evidence lives in [`human-run1/retro.md`](../2026-08-16-human-run1/retro.md) and in
[`capture/run7-stud`](capture/run7-stud); this list is the decisions, so the build can be worked
from one file. Times in brackets are seconds into the stud rebuild.

### The model changes, not only the page

| # | Change | From |
| --- | --- | --- |
| M1 | Every dimension comes from a variable or an expression on one; no literal typed twice | the brief |
| M2 | The stud profile is one closed region — arc, three lines — not a circle and a rectangle crossed by a line | retro; rebuild |
| M3 | The slit sketch sits on the collar's **top face** and cuts **Through all**, so `4.15` and `1.35` and the **Second end position** field all go | retro; 4.0.0 |
| M4 | Features are named as they are created, and the names are the ones typed — lowercase | rebuild [554.6] |
| M5 | The Boolean subtracts the whole `Ball stud`, but only the ball cuts anything | retro |
| M6 | The stud's height above the ball's center is `#stud_len`, chosen at 5 | below |

**M5, so the page does not promise the wrong thing.** The collar's top face sits `#grip` above the
ball's center, and the stud runs upward from there through air — measured on the finished socket,
there is no cylinder the stud's size anywhere in it. The stud swings free because a sphere cut by a
plane `#grip` off its center leaves a mouth wider than the stalk. Say *click the whole part*; do not
say the stud cuts its own clearance.

**M6 was the one open number, and it is now a choice on the record.** The rebuild put the stud's top
face 5 above the ball's center, and `target.json` names nothing it could come from. Mike chose 5 and
it becomes `#stud_len`. The report says *chosen*, not *derived* — if the limb the stud plugs into
later dictates a length, the variable is the one place it has to change.

### How the steps are written

| # | Change | From |
| --- | --- | --- |
| S1 | The instruction goes **above** its picture. `.. figure::` puts the caption below, so the directive changes, not the wording | retro |
| S2 | Screenshots at four-fifths page width, centered, with a visible gap between steps | retro |
| S3 | The view does not swing by itself. **N** looks square at the plane; **P** toggles the default planes | retro |
| S4 | Shortcuts in parentheses after the click, each read off Onshape's published list before it ships | retro |
| S5 | **Select first, then press the shortcut** — plane in the tree then `Shift+S`, sketch in the tree then `Shift+W` | rebuild [403.7, 582.2] |
| S6 | In a sketch it is a **cross-section**; `profile` is the closed region and the feature's name; `Ball stud` stays a solid | retro |
| S7 | Tools get their real names — **Center point circle** (`c`), **Corner rectangle** (`g`), **Line** (`l`), **Dimension** (`d`), **Center point arc** — never the dropdown's family name | retro |
| S8 | The collar gets the same number of steps as the ball. It is the second circle, not an easier one | retro |
| S9 | The heading reads *A hollow in the socket made from the ball and stud themselves* | retro |
| S10 | Each slit bar is a **Center point rectangle** started on the origin, which centres it for free, and then two dimensions: its length and `#slit`. Two crossing bars give four slits | build |
| S11 | The sketch circular pattern has no dialog — see below | retro |
| S12 | A radius dimension takes the radius; picking the arc is what announces which it will be | rebuild [516.3] |
| S13 | Rename every feature, so the tree never says `Sketch 1`. The reader does it in the dialog header before the green tick; the harness cannot, and uses the tree row's menu after — see H4 | rebuild [554.6] |
| S14 | **Workspace units…** is set before anything is drawn; opening it mid-sketch closes the sketch | rebuild [195] |
| S15 | An advice callout for a missed snap: click the two points and apply **coincident**, or **vertical** / **horizontal** for a line that came out nearly true | today |
| S16 | **Shift+7** after every 3D operation. The reader has just made a solid and should see a solid | retro |

**S11, written from the manipulator.** Selecting the entities comes first and the tool second; the
pattern then appears on the click that invokes it. It arrives with three instances, and the count is
a small grey `3x` tag floating in empty space at the end of a thin leader line — that tag is the
double-click target, it highlights orange on hover, and a single click on it does nothing visible.
There is no green tick: move to white space, wait for the cursor with the green button, and click.
**Escape** discards the pattern silently and the sketch still closes clean and fully defined.

**S15, as drafted:**

```rst
.. admonition:: If the fill does not appear, add the constraint yourself
   :class: advice

   A closed profile fills in pale grey and turns black. If yours stays blue and empty, one end
   landed a hair off its neighbour. Click the two points that should meet, then click
   **coincident** in the sketch toolbar — the gap closes and the fill arrives. The same trick
   straightens a line that came out nearly upright: select it and click **vertical**, or
   **horizontal** for one that should lie flat.
```

### What the figures show

| # | Change | From |
| --- | --- | --- |
| F1 | **P** before every sketch shot. Planes on means three grey rectangles behind geometry a few millimeters across | retro |
| F2 | **Shift+7**, **P**, **F** as one habit, so the shape is large and solid-looking in every figure | retro |
| F3 | Caption and picture must be the same moment. The pool's `-a-select-` / `-b-done-` slugs make that checkable against the caption's verb | retro |
| F4 | Alt text and image slugs carry the cross-section naming; slugs are renamed on the next capture, not retrofitted | retro |

F1 and F2 are why this page needs new captures rather than a re-pick from the run 6 pool. F3 is the
opposite — most caption mismatches are fixable by choosing a different existing shot.

### The rules that changed

**Constitution 4.0.0** removed *sketch on planes over faces* and replaced it with **anchor each
sketch to the geometry that gives it meaning**, and added **not every variable is a scaling knob**.
Both are in [`.parts/onshape.md`](../../../.parts/onshape.md); the reasoning is in the
[changelog](../../../.parts/constitution-maintenance.md#changelog). M3 follows the new rule rather
than excepting the old one.

**Still unplaced:** a completeness review — account for every action taken while building, as a
written step or as a deliberate omission with its reason. *Steps reproduce* catches a page that
cannot be followed, not one that can be followed to the wrong screen. Run once for this page,
under [The page](#the-page); it still has no home in the rules, and constitution edits are on hold,
so it goes nowhere near `constitution.md` or a part without asking.

### The harness

| # | Change | From |
| --- | --- | --- |
| H1 | A step that opens no dialog produces no frames, so the whole-session webm is the only record of manipulator work | retro |
| H2 | Finalize the webm by **closing the page target over CDP**, then stopping the process — see below | today |
| H3 | `Shift+7` arrives in the event log as `&`. Key scans have to look for the shifted character | today |
| H4 | Rename through the tree row's context menu, never the dialog header. A name typed with the graphics area focused runs as shortcuts — `stud profile` toggled the planes and armed an equal constraint | build |
| H5 | Arm a sketch tool through **Search tools**, not its letter. The letter toggles, so it turns the tool off as often as on and the picks land as plain selection clicks | build |
| H6 | Never send a bare `f` while a field has focus. It lands in the field, and the depth that looked set reads back as `f` | build |
| H7 | An entity hidden behind the solid does not highlight and does not pick. The slit bars had to be picked past the ball's silhouette | build |
| H8 | Place a dimension label clear of the model. A label click that lands on an edge makes a two-entity dimension instead of opening the field | build |

**H2, the working shutdown.** `human_browser.py` closes its context on `KeyboardInterrupt`, but a
job started in the background has SIGINT ignored, so the signal never lands and SIGTERM kills the
process with the webm unfinished. The route that works needs no signal at all: `curl
http://127.0.0.1:9224/json/close/<targetId>` closes the page, Chrome finalizes the video, and the
process can then be stopped however. The head video carries a real `DURATION` in its header and
decodes to the end; the stud video, killed with SIGTERM, reads `Duration: N/A` and stops short. The
recorder needs none of this — it installs a SIGTERM handler that raises `KeyboardInterrupt`, so it
writes its summary either way.

## Settled before the build starts

**Where the slit sketch lives — the collar's top face.** The Top plane looks dependency-free and is
not: the slit sketch works there only because the Top plane is the plane the collar was extruded
from, and nothing records that it has to be. Rotate the collar onto another plane and the slits are
silently in the wrong place while regenerating clean — the same defect as the typed `4.15`, moved up
to where it cannot be seen. The face states the relationship, and it turns the cut depth into a real
choice: **Through all**, or a named depth for a slit that deliberately stops short.

**One closed region is cheap, and Trim is never needed.** The stud rebuild drew arc-plus-three-lines
in under a minute with no leftover geometry and no constraint applied by hand — the line tool's
snaps wrote the coincidents, and the pale grey **fill** is the tell that the loop closed. The collar
and slit profiles use the same recipe.

## Answered by the build

**Through all reaches the far side, and that is the problem.** Built as published, the cut left
five bodies: the stud and four loose petals. The slits run the full wall thickness, so cutting the
whole collar height separates it into quarters. The depth is now `#collar - #wall`, measured down
from the collar's top face, which leaves exactly one wall thickness of floor. `#grip + #ball/2`
was tried first and is wrong for a different reason: it is bounded by the ball, so at `#ball = 10`
it runs past the collar's bottom and severs it again. Bound the slit by the thing it is cut into.

**The origin lands in the sketch plane, not below it.** The slit sketch's own origin sits on the
collar's top face directly above the part origin, and the two crossing bars, centred there, read
back at exactly ±4.7 by ±0.4. Nothing had to be dimensioned down to the part origin.

**The model survives a driving-dimension change.** `#ball` driven 6 → 9 → 6: every feature stayed
`OK`, the socket stayed one body, the cavity followed at `#ball/2 + #fit` and the collar at
`#ball/2 + #fit + #wall`, and the return to 6 reproduced the original radii exactly.

## The page

[`instructions/robot-guide3/source/ball-and-socket.rst`](../../../../instructions/robot-guide3/source/ball-and-socket.rst),
written from the model above and read back off it — every expression on the page is the expression
the feature holds. The tree it needed did not exist, so `conf.py`, `_static/custom.css`, `Makefile`
and a stub `index.rst` came with it; the CSS gained an `img.shot` rule because S1 moves the
instruction out of the caption and into the paragraph above, which makes the steps plain images
rather than figures. Sphinx builds it clean apart from the missing pictures.

**The pictures are the one thing outstanding.** Every step image and both overview figures are
named, slugged and alt-texted in the page; none has been captured, and
`instructions/robot-guide3/source/images/` is empty. F1 and F2 rule out re-picking from the run 6
pool, and the run 7 build shots are the harness debugging itself — wrong framing, planes on, and
several of states the page does not teach.

**One menu path was opened rather than assumed.** The page tells the reader to publish a version,
and no version in this run was made through the GUI — they went in over the API. So the rail was
hovered: the top icon is **Versions and history** and the one under it is **Create version…**,
which opens *Create version from Main* with **Name**, **Description** and a **Create** button.

### Completeness review

Every action the build performed, as a written step or as an omission with its reason.

| Build action | On the page |
| --- | --- |
| Workspace units, decimals to 0.00001 | step, with S14's reason |
| Eight variables | one worked step plus the table |
| Front plane, `n`, `p`, arc, three lines, three dimensions | steps |
| The **vertical** applied by hand to the last line | the S15 callout, not a step — the reader's line may snap true |
| Revolve: region, axis, full revolve, `New` | steps |
| `Shift+7` after each of the four solid operations | steps; `p` and `f` join it at the first one |
| Rename each feature and both parts | steps, in the dialog header before the tick (S13) |
| Top plane, **Center point circle**, diameter from the expression | steps |
| Extrude both directions, `#grip` and `#collar - #grip` | steps |
| Boolean subtract, offset all `#fit`, keep tools | steps |
| Collar's top face, two **Center point rectangle**s, two dimensions each | steps |
| Extrude remove, flipped down, `#collar - #wall`, scoped | steps |
| Named version at the end | step |
| Driving `#ball` 6 → 9 → 6 | omitted. The ceiling callout drives `#fit` instead — joint sizes do not scale, and the plan says so under **Floor and ceiling** |
| Picking the slit bars past the ball's silhouette (H7) | kept, as part of the dimension step. A line under a solid is awkward to hit with a mouse too |
| The harness's other workarounds — Search tools for every sketch tool, rename through the tree's context menu, dimension labels placed clear of the model | omitted. H4, H5, H6 and H8 are constraints on driving Onshape from a script, not on a person with a mouse |
| Building **Through all** first, and the four loose petals it left | omitted. The depth that works is the one taught; what it replaced is recorded above under **Answered by the build** |

## Spike F — answered: one calibration per sketch, fit only to shoot

Run on 9223 against a scratch document, `run7-spike-f`. What was measured:

- **A canvas click lands exactly where it is aimed.** A line drawn at two chosen pixels read back
  through the API and predicted its own second endpoint to the pixel. There is no drift to budget
  for; the only question was ever the mapping.
- **The mapping is a uniform scale about the origin's position on screen** — two unknowns, no
  rotation, when the view is normal to the sketch plane. Both fall out of any one line whose
  model coordinates the API reports.
- **The default camera puts the origin at the exact centre of the canvas**, at 3.6066 px/mm on a
  1354 x 894 canvas. Measured, not assumed — the origin came out at (922.5, 523.5) against a
  centre of (923.0, 523.0).
- **`f` changes both numbers.** The same sketch went to 7.8711 px/mm with the origin moved to
  (976.9, 564.3), framing the geometry at 93.5% of the canvas width and 95.2% of its height.
- **Reloading the document does not restore a known camera.** It comes back isometric with the
  default planes shown, which is why `n` and `p` are the first two keys of every sketch.

**So: neither (a) nor (b), but the thing underneath both.** Calibrate once per sketch. The first
entity goes down at arbitrary pixels — its position does not matter, because dimensions pin it
afterwards, which is what a person does too. Read it back, solve for scale and origin, and every
remaining click in that sketch is computed in millimetres. Press `f` after the last click, to
shoot. The next sketch calibrates on its own first entity, so the camera may move freely between
features and never during one.

This is a constraint on the automation, not on the page. Students can press `f` whenever they like.

### The two shapes considered before the measurement

F2 tells students to press `f` often, so the shape is large in every figure. That changes how I
build, because a canvas click is in pixels and `f` moves the mapping from millimeters to pixels
under it. Two shapes the work could take:

**(a) Re-derive the mapping after each fit.** Screenshot, find the origin marker and one entity
whose model coordinates are known, compute pixels-per-millimeter and the origin's pixel position,
then click in model coordinates. If this holds, the camera may move whenever a picture wants it to.

**(b) Keep the construction camera still, and reframe only to shoot.** Build with a fixed view;
press `f` immediately before the screenshot. Simpler, and it fails only for a figure that has to
show *where to click* — that shot is framed by the previous fit, not the current one.

Both were half right, which the measurement above shows: (a)'s re-derivation is real and cheap, and
(b)'s instinct to keep the camera still is right *within* a sketch and unnecessary between them.

**One thing the API gave up for free.** Onshape does not store a sketch line as two endpoints. It
keeps a point on the line, a unit direction, and the parameter value of each end, so the endpoints
are `pnt + t * dir`. Anything reading sketch geometry back has to do that arithmetic.

## Floor and ceiling

**Floor.** Two named parts in one Part Studio, a ball that turns inside its socket, and four slits
that let the collar swallow it.

**Ceiling.** Change `#fit` from 0.2 to 0.3 and watch the cavity, and only the cavity, open up.

Not `#ball`. **Joint dimensions are set by the snap fit and do not scale with the robot** — a ball
twice as big still needs the same gap and the same slit, because those numbers come from how the
plastic bends, not from how big the robot is. The variables here exist to record *why* a number is
what it is, not to offer a scaling knob. The change-one-number demonstration that
[`modeling-practice.md`](../../../.parts/modeling-practice.md) asks to be put somewhere on purpose
belongs on a major shape, not on a joint.

**Recovery point.** A published, named version at the end, cited by the page.

## What this run does not do

It does not edit `robot-guide2`, and it does not amend the Constitution or its parts.
