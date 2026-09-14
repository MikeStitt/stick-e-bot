# draft9p2 — notes from the run

What the run hit that the plan did not anticipate, and what is waiting on Mike. The plan itself is
[`plan.md`](plan.md); nothing here changes it.

## Blocked on Mike

### `stickbot-draft9p2-check` does not exist

`audit.page` reproduces each page into a scratch document named `stickbot-draft9p2-check`, and the
plan says Phase P gets Mike's agreement to add it to the account before Phase T starts. Phase P did
not get it. The documents this run may create or build in are `stickbot-draft9p0`,
`stickbot-draft9p1`, `stickbot-draft9p1p1` and `stickbot-draft9p2`, and a fifth is not on that list.

Mike has agreed that the builder runs `audit.page` itself and hands the account to a reviewer that
did not watch the build. That settles who runs it, not where it reproduces into.

Until the document exists, `audit.page` cannot run as written. Everything else in Phase T and
Phase W is unblocked, so the run carries on and the pages are written; the `audit.page` pass over
each page is owed once the document is there.

## Found while building

### The Slot tool cost three attempts that were already written down

`head`'s `mouth profile` is a slot, and three attempts went into clicking one out of empty
space before the tool's actual behavior was established. Every fact needed was already in
[`../../../onshape-gui-howto.md`](../../../onshape-gui-howto.md) § 7: the tool wraps a curve the
sketch already holds, and the diameter dimension it writes for itself sits four radii from a cap
center. The online help was read; the repo's own file was not.

`.docs/onshape-gui-howto.md` is the first thing to read before driving a dialog, not the last.

### `n` can look at the back of the plane

**View normal to** (**n**) orients square to the sketch plane, and on the head's Front plane it
landed on the **Back** — mirrored text in the corner, the eyes hidden behind the head, and every
sketch x reversed on screen. The how-to already says the view *has come back 180 degrees rolled*;
what the head adds is that the reverse is not always obvious in a clipped frame. The front view
(**shift+1**) is the one the head's sketches are taken from.

### `f` does not reach the graphics area while the Insert panel is open

The panel keeps the keyboard, so the press goes into its search box and the view does not move.
Three attempts at tutorial 3's two mid-insert frames went at them as pictures of the graphics area
before that was established. The wheel still reaches the canvas, and the frames that stand are
clipped to the feature tree and the panel, where an insert's evidence actually is: the tree's
instance count and the panel's own counter.

### `ring` scaled a clipped frame by the window rather than by the clip

Every ring on a cropped frame landed a fixed fraction of the way in from the crop's left edge, so
the ring on the Insert panel's `body` row sat up in the corner on `Current document`. Fixed in
`tools/onshape_gui.py`. Tutorials 1 and 2 never rang a clipped frame, so nothing already published
carries the fault.

### An assembly's tree row and its tab do not rename at the same moment

The tab strip takes the new name on **Enter** and the tree's top row, which is where the assembly's
own name shows, takes it a beat later. A step that reads the tree straight away sees the old name
and its `creates` check refuses a step that did exactly what the plan said. Wait for the tree.

## Blocked

### Does the guide repeat "the pictures come from this document" on every page?

`torso.rst` and `head.rst` each open with the same three-line advice box naming
`stickbot-draft9p2`. `assembly.rst` leaves it out rather than printing it a third time. Saying one
thing once is the standard, and a reader working the pages in order has read it twice already; a
reader arriving mid-guide has not. Decide it in the register and make all fourteen pages agree.

### Search tools' Enter takes the top row, not the row you typed

Typing `Circular pattern` into Search tools and pressing Enter arms **Linear pattern**, because the
list ranks what it offers and Linear pattern sits above Circular pattern for either name. The tool
then waits for picks that never mean what the script thinks they mean, and the sketch ends up with
no pattern and no error. `t4lib.arm` clicks the row whose text is the tool's own name instead.
`onshape_gui.search_tool` still presses Enter, which is right for a name that ranks first on its
own, such as `Dimension` or `Corner rectangle`, and wrong for any name that another name contains.

### A sketch pattern's count is drawn on the canvas, and only a double click opens it

The circular pattern in a sketch has no feature dialog. It puts `3x` beside the entity you patterned
and that text is painted into the WebGL canvas, so nothing in the page carries it: a search of every
element for `3x`, and a dump of every visible input, both come back empty. A single click lights the
label orange; a **double** click puts a real `input.os-param-number` over it, and that field is the
only way to ask for four copies rather than drag a handle round until four appear.

### Escape ends a sketch pattern by throwing it away, and `clear` presses Escape

A circular pattern in a sketch stays live after you set its count: the `4x` label is still on the
canvas and the copies are still blue. Escape at that point does not accept the pattern, it cancels
it, and the sketch goes back to the one entity you started from with no error and no banner.
`onshape_gui.clear` presses Escape before it clicks, so every use of it between the count and the
green tick committed a sketch with one slit in it. `t4lib.deselect` clicks and does nothing else.
The pattern is accepted by the sketch's own green tick, and the picks that follow it are ordinary
picks.

### A Remove with an empty merge scope removes nothing and says nothing

The Extrude that cuts the relief slits arrived with **Merge with all** already off and its **Merge
scope** empty. It committed green, the feature listed, the tree grew a row, and the socket had
exactly the four faces it had before. Nothing in the dialog, the tree or the banner said the cut
had taken material from no part at all. The check that catches it is the one the model can answer:
read the face count before and after and refuse a cut that changed nothing.

The direction needs the same treatment rather than a click. Onshape already points a cut from a
face into the material, so the flip control turns a correct default around; the first pass flipped
it on principle and cut air.

### A mate connector takes no pre-selection, and its own arrows get in the way of the next one

Extrude and Revolve both accept a face picked before the tool is armed. Mate connector does not:
armed with a face already selected, it opens with an empty **Origin entity** and commits a
connector on the part origin, green and wrong. The tool goes first and the face second.

Its arrows are then drawn in front of everything on that axis. The socket's connector is placed by
picking the flat underside of the collar, and the stud's connector, made a moment earlier, stands
on the same axis 19 mm away; from below its arrows cover the middle of the disc, so a click there
selects nothing at all. Picking 1.5 mm out clears them.

That pick reads as the **centroid** of the face rather than the **center** of the circle. On a full
disc the two are one point, and the connector lands where the reference's does; the reference
records `CENTER` and this records `CENTROID`.

### There is no `Show` on a part that is already showing

The two halves of the joint live inside one another, so a hero of either one needs the other
hidden. A part's right-click menu offers **Hide**, **Hide other parts**, **Hide all parts** and
**Isolate…** when the part is showing, and **Show** only when it is hidden. Asking for `Show` on a
visible part finds nothing, so the pass that puts one part on screen asks for `Show` first and
shrugs if it is absent, then asks for `Hide other parts`.

### Section view is not a tool, and its menu cannot be read like the others

Search tools does not offer it and the graphics area's own menu does not carry it. It hangs off the
button beside the view cube, at (1555, 232), whose rows are plain leaf elements rather than list
items; `menu_on` looks at `li, a, button, [role=menuitem], .tool` and comes back with an empty list.
`t4lib.view_menu` reads the rows the way the canvas menus are read, by what the click adds to the
page.

Once a section is on, that menu offers **Edit section view…** and **Turn off section view** in
place of **Section view…**, so a run that wants its own cut turns off whatever is there first.

The cut is a picture, not a part: nothing lands in the tree and nothing changes in the model.
Looking at the cut from the side the section removed shows a whole part, which reads as a failure
and is not one.

### A Variable Studio's rows carry no text of their own

The table is made of `input` elements, so a Variable Studio tab looks empty to anything that reads
leaf text the way a feature tree is read. The row is found by the input whose *value* is the
variable's name, and the cell to type into is the input on the same line further right.

Onshape also normalizes what is typed there: typing `0.8` and reading the table back gives
`0.8 mm`, so a check that compares what it typed against what it reads has to type the unit too.

### A step that ends on another tab reads as having lost the whole tree

`Take.step` compares the feature tree at the open against the tree at the close, and the
exaggerated section ends on the Variable Studio tab where the fit goes back. The tree there is
empty, so the check reported every feature in the studio as lost. The frames were taken and the
verdict stands; the step now returns to the Part Studio before it closes.

### Where the toolbar buttons are, read off their tooltips

Hovering across each strip at eight-pixel steps and printing the tooltip when it changes gives the
x of every button at y 58. The two strips hold different tools at the same pixels.

Part Studio: Sketch 155, Extrude 204, Revolve 236, Sweep 276, Loft 308, Thicken 340, Fillet 396,
Chamfer 452, Draft 484, Rib 532, Shell 572, Hole 604, External thread 636, Linear pattern 676,
Mirror 724, Boolean 764, Split 796, Transform 836, Delete part 884, Modify fillet 924, Delete face
956, Move face 988, Replace face 1028, Plane 1060, Frame 1116, Sheet metal 1172, Custom features
1228.

Sketch: Line 188, Corner rectangle 244, Center point circle 292, 3 point arc 348, Inscribed polygon
396, Spline 452, Point 500, Text 532, Use 572, Construction 620, Sketch fillet 660, Trim 708,
Offset 764, Mirror 812, Linear pattern 852, Insert DXF 900, Dimension 956, Coincident 996.

Three of the tools this tutorial uses are rows in a menu rather than buttons on a strip. **Circular
pattern** is in the sketch pattern button's dropdown, at the caret at 884. **Mate connector** is
well down the dropdown that starts at Plane, at the caret at 1092, and carries the shortcut
`ctrl m`. **Section view** is in the view menu. Search tools finds all three, and its *Highlight
tool in toolbar* box is what showed where Mate connector lives.

### A reviewer that did not watch the build found four things the builder's own audit missed

Mike allowed one reviewer for `audit.page`: told what the builder did, and asked to decide whether
it cheated. It said partly, and four of its findings hold up against the artifact.

The page said the slit extrude's dialog opens on **Add**. It opens on **New**, which is what the
collar extrude in the same page left it on, and **New** with four regions is what makes the four
new solids the frame shows. The claim was invented in the writing; the log's `shows` for that
frame never said it, and the block audit then certified it.

The page asserted five names it never told the reader to type: `revolve stud`, `collar blank`,
`cavity from ball`, `relief slits`, and the rename of `Part 2` to `socket body`. A reader
following the page could not have produced the tree the page shows them. The attack that catches
this is the one `plan.md:111` already asks for and the first round skipped: read the block as a
student who has not seen the model, and check every noun against the figure above it or an earlier
sentence.

The audit reported the guide's Sphinx warnings falling from 118 to 104 without counting them. A
clean build prints 117. The rewritten page removed exactly one warning, because the page it
replaced referenced exactly one image that did not exist.

Nine findings were recorded `blocking`. `takes.md:226-229` makes `blocking` mean the geometry
cannot go on being built over it. All nine were alt text or frame publication. They are carried.

**What this costs the process.** The builder cannot be the only auditor of its own page. Two of
the four are things no mechanical check would catch: the invented dialog state reads perfectly
well, and the missing renames are invisible to anyone who watched the build happen.

### `req.model.derive` was tagged on nine blocks that derive nothing

`drafts.md:253` defines it as a joint built once and derived wherever it is used. `ball-and-socket`
*is* the joint. The tag belongs on the pages that consume the joint, and what these blocks embody
is `req.model.design_intent`, with `req.page.view_keys` where a view key is pressed.

### `req.page.shortcut_form` has never been applied anywhere in draft9p2

`drafts.md:270` asks for **Extrude** (or press **shift+e**), dropping the words once the reader has
seen the pattern. No page carries it. The shortcut appears only inside toolbar close-up alt text.
It is recorded as unmet on the eight tutorial 4 blocks that name a tool, and it wants a decision in
the register: apply it across the guide, or withdraw the requirement.

### A log line written at capture time can say more than its frame holds

Three of tutorial 5's `shows` lines describe a socket that is not in the picture. `place-07` says
the socket is "now hanging below the head's underside with its mouth pointing down", `place-09`
says it is "standing below the head, its slit rim pointing down", and `connector-05` says "the
finished head, its socket underneath". All three frames are corner views from above, and the socket
hangs under the head where that camera cannot see it. `version-03`'s line names tutorial 4 at the
top of the versions panel; the frame shows tutorial 5 there.

The builder knew where the socket was, so the line describes the model rather than the frame. It is
the same failure the reviewer found in tutorial 4's alt text, one step earlier in the pipeline: the
page inherits it if the page is written from the log. Opening all 41 frames before writing is what
caught it, and it is the only thing that would have.

### The parts list and the tree are one panel, so one of the two steps is a duplicate

`cad.tree` and `cad.part_list` both shoot the feature panel, and on the head tab the parts list is
inside it. The two frames came out byte-identical, so `req.shot.one_use` leaves `cad.part_list`
with nothing to publish and tutorial 5's page carries eight step tags rather than nine. Either the
part list step clips to the parts rows, or the two steps merge.

### The reference builds a shoulder in eight features, and the plan asks for eleven

[`06-torso-joints.md`](../../../build/plan/06-torso-joints.md) lists `shoulder rotation point`,
`shoulder rotation plane` and `shoulder rotate about z` between the pivot sketch and the plane the
profile is drawn on. The reference `body` in `stickbot-draft9p1p1` has none of the three. Its chain
is `pivot lines`, then `plane for shoulder`, then `torso shoulder profile`, then `shoulder`.

The two angles are still on screen where the plan wants them. `#yaw` is the angle field of `plane
for shoulder`, which is a plane at an angle to a line, and `#tilt` is a dimension in the profile
sketch. So the shorter chain keeps the argument the plan's own prose makes for the longer one, and
draft9p2 builds what the reference holds. The plan's step table and
[`lesson-plan.md`](../../../build/lesson-plan.md) § *Geometry a student can see, not numbers they
cannot* both want amending to eight steps.

### `/features` is rate limited for the rest of the day, and the tree answers instead

Reading the feature list twice in a few minutes spent the endpoint's quota: Onshape refuses
`/api/partstudios/.../features` until about midday tomorrow, and the countdown runs against the
clock rather than against silence. `gui.tree(page)` reads the same names off the screen, and
`bodydetails`, `parts`, `boundingboxes` and `variables` each kept answering. A feature's *name* in
that list is a template anyway: an `assignVariable` feature is stored as `###name = #value` and
only the tree renders it as `#hip_half = 24 mm`, so the screen is the better reader here.

### A tab that reads *not computed* is a browser that has come adrift, not a broken model

Accepting `plane for shoulder` left every user feature in `body` greyed and italic, the parts list
reading Parts (0), and the graphics area empty. The variable rows stopped showing their values and
showed their expressions instead, which is what Onshape does when a variable has not computed.

The model was never harmed. `bodydetails` answered for the same element with the solid it always
had: one body, `JHD`, six faces. `head` and `ball and socket` went on computing in the same window.

None of the obvious cures worked. `page.reload()` came back to the same greyed list. So did the
Regenerate Part Studio button, and so did entering and leaving paused regeneration by all three of
its buttons. What did work was building a new client: a second page opened on the same URL showed
`Parts (1)` and the torso at once, and navigating the working page away to `/documents` and back
cleared it there too.

`t6lib.unwedge` navigates away and back, and it cured the tab once. It stopped curing it: after
`plane for shoulder` was accepted, two trips to `/documents` and back left the list greyed both
times. A page created inside the run computed the whole tree at once, with `plane for shoulder` in
it and `Parts (1) torso` under it, while the old page beside it stayed greyed. So the client wears
out; the model does not break, and the cure is a new client rather than a new address.

Every step from here on opens the body tab on a page of its own through `t6lib.fresh_body`, and
closes that page when it is done. Closing it is allowed because the run made it.

### The plane stood on a point, and the point was the line's own midpoint

`plane for shoulder` went in three times carrying `ns-list-item-error`, and a sketch asked to stand
on it answered *Missing plane for shoulder*. The cause was the pick. Clicking the pivot line at
(36, 0, 44) is clicking its midpoint, and Onshape snaps a click there to the midpoint rather than to
the line, so the dialog took *Edge point* as the plane's first entity. A plane through a point and a
plane is not a plane, so the feature errored, and everything downstream of it had nothing to stand
on.

Clicking at z = 42.5 instead takes *Edge of pivot lines*, which is the line. Two other things had to
be true first: the `pivot lines` sketch has to be shown, because construction geometry in a hidden
sketch is not there to click, and the camera has to be looking straight at Front, because that is
where the line is and an isometric click on the same point lands on the torso's corner instead.

### A tool's prompt is a bubble the frame guard had not been taught

With the line picked, Plane says *Select an additional point, plane, or axis to specify where the
angle is measured from*. That arrives in `.osx-message-bubble.alert-info`, and `gui.no_banner` knew
only the older `.speech-bubble`, so it read the prompt as a notification with no × and refused every
frame for as long as the script would wait. It now skips a message bubble while a feature dialog is
open, and only then: *Sketch 1 has been canceled* comes in the same bubble with no dialog on screen,
and that one still has to be waited out.

### Blocked: the agent browser has no Onshape session, and only Mike can give it one

Each run of a step opens its own page, and killed runs left theirs behind. With several Part Studio
clients alive at once the browser slowed until `page.goto` and one right-click menu together took
eleven minutes, so the agent browser was restarted to clear them. That was the wrong cure. The
borrow only works while the signed-in browser is signed in, and it is not: port 9222 is sitting on
`cad.onshape.com/signin`. The restart therefore traded a slow session for no session, and
`agent_browser.py` now exits with *the borrowed cookies carry no session*.

**What clears it.** Mike signs in to Onshape in his own browser, and then `agent_browser.py` is
started again. Nothing else does: the session cookie is held in memory by the signed-in browser and
cannot be recovered from a profile on disk.

**What is left standing.** `body` in `stickbot-draft9p2` holds the torso, the eight tab variables
and `pivot lines`, all computing. `plane for shoulder` was deleted before the block, so the tab ends
on a clean feature rather than a broken one. The CAD picks up at
`cad.parts.body.shoulders.plane`.

**The log still carries a verdict for that step, and it does not stand.** Attempts 1 to 4 of
`cad.parts.body.shoulders.plane` are in `log/torso-joints.jsonl` with the last of them marked as
the performance, because the check the harness ran asked only whether a feature by that name had
appeared. It had, with an error on it. `gui_steps` now reads the row's class as well and refuses a
step whose feature went in broken, so the next attempt either stands or says why not, and
`read_log` keeps only that one.

### Two page questions answered while the CAD was blocked

**`req.page.shortcut_form` is applied, not withdrawn.** The requirement had never been applied on
any draft9p2 page, and the pages disagreed with each other: `torso` put the key before the tool
(*press* **shift+e** *for* **Extrude**), `head` put it after in parentheses, and five pages spelled
the view keys **Shift+7** where the requirement asks for lower case. Every `**Shift+`` in the guide
is now `**shift+`, and `torso`'s three reversed forms read **Center point rectangle** (or press
**r**), **Dimension** (or press **d**) and **Extrude** (or press **shift+e**) — the full form on
the page that teaches each key, which is what lets `head` drop to (**d**) and (**shift+e**) later.

**Every page carries the note about the document's name.** `torso`, `head`, `ball-and-socket` and
`head-socket` opened with *The pictures come from the document this guide was built in*; `assembly`
did not. Four pages to one is the convention `req.carry.conventions` points at, so `assembly` now
carries the same admonition in the same place, above the first section.

### The shoulder chain is built, and four of its frames cannot be published as shot

`body` in `stickbot-draft9p2` now ends on `mirror shoulder` with three parts: `torso`,
`shoulder boss` and one still called `Part 3`. `shoulder` reads back as one cylindrical face of
radius 8.000 mm on the axis `#tilt` and `#yaw` aim, which is `#boss_d / 2` and the direction
draft9p0 measured. The tree carries no errors.

`log/torso-joints.jsonl` had held no audit records at all. Seven `audit.step` records now go with
it, and they turned up four blocking findings and eight carried ones. The blocking four are all
frames, and all four need the browser rather than a rewrite:

- `parts.body.variables-01` to `-04` are cropped to the table's first nine rows, and every one of
  them is about the empty row below the crop.
- `parts.body.numbers-01` carries a tooltip reading `#tilt = 53 deg [Variable]`, left by an earlier
  pass, in a frame whose job is to show the tab before any variable exists.
- All five frames of `parts.body.shoulders.plane` were shot on a tree still holding six attempts'
  wreckage: a red `Sketch 1`, two rows both named `Plane 1`, an error badge on the header.
- `parts.body.shoulders.plane-05` is supposed to show the new plane and draws only Front and Right.

Two more retakes are worth doing in the same pass: `parts.body.shoulders.connector-06` has the
torso's whole side face lit orange from a tree row under the pointer, and
`parts.body.shoulders.revolve-06` has one highlighted edge for the same reason.

**The habit that causes it.** Every one of these is the pointer or the tree left where the last
action put it. A frame is taken of the whole window, so the panel is in the picture; moving the
pointer to the middle of the canvas and clearing the selection before the shot costs nothing.

### The studs, and two ways the read-back lied

The five studs are one derive and four transforms, and the transforms are where the run spent its
time. Three facts came out of it.

**The flip button is not a habit, it is a reading of the preview.** `move neck stud` needs it,
`copy for hip` does not, and `copy for shoulder` needs it again. The three connectors were built
the same way; which way each one points is a fact about the face or the edge it stands on, and no
rule short of looking at the preview gets all three right. The bounding box is what caught the two
wrong ones: a stud placed inside the torso moves no face of the model, so the box comes back
unchanged, which is a louder signal than a picture.

**The feature list draws only the rows near the scroll position.** A step that ends with the list
scrolled to the bottom reads back as having deleted `Default geometry`; scroll to the top instead
and the same step reads back as having created nothing. Three step records in this run carry one
of those two lies. The cure is to collapse `Default geometry`, which takes four rows out of the
list and lets both ends render at once, and to scroll to the top before asking whether it is
already collapsed — a row that is not drawn reads exactly like a row that is not there.

**A row that is open holds its children's text.** `get_by_text("Default geometry", exact=True)`
finds nothing while the four planes are showing under it, because the row's text is all five names
at once. Rows with children have to be found in the list rather than by their label.

### The same lie reached a guard, and the guard answered False

`gui.planes(page, shown=False)` reads the three plane rows and presses `p` only when they
disagree with what was asked for. It read them with `Default geometry` closed, found none of the
three, and answered *not hidden* — so `shown=False` had nothing to press and returned quietly. The
Boolean's finished-part frame came out with two planes across it and the torso fitted to them
rather than to itself.

`planes_hidden` now refuses to answer when the three rows are not all in the list, and says which
of them it could not find. It is the same fact as the two above, arriving in a shared tool instead
of a run script: a row that cannot be read looks exactly like a plane that is not hidden, and a
guard that guesses is worse than one that stops.

### The cure is to read the list at both ends

Collapsing `Default geometry` bought four rows and held until the tutorial's thirty-third feature,
where the third connector was recorded as creating nothing: Onshape keeps about thirty rows in the
page and evicts the rest, so the new row at the foot of the list was gone by the time the step
read it back.

`gui.tree_all` reads the list at the top and again at the bottom and stitches the two, the second
reading contributing only rows the first did not have. Feature names are unique inside a Part
Studio, so the join is exact. The parts list underneath is not — five studs are all called `ball
stud` — so anything counting parts still uses `gui.tree` and scrolls to them itself. Every step's
before and after now go through the stitched read.

The stitch has one trap of its own, which cost a run. The parts pane is pinned to the foot of the
panel and is drawn whatever the scroll, so both readings end with it; joined as they came, `Parts
(1)` landed in the middle of the list and `_features`, which cuts there, threw away exactly the
rows the stitch had been written to recover. The pane comes off both readings before they are
joined and goes back on afterwards.

### One number drives the whole body tab, and the proof is cheap

`audit.part` for the body tab wanted evidence that no length in it was typed into a dialog. The
way to get that is not to read every dimension; it is to move the number they are all supposed to
come from and see what follows.

`#torsoH` went from 96 mm to 144 mm in `robot sizes`, with nobody opening the body tab. `#hip_half`
went 24 to 18 mm, `#shoulder_drop` 8 to 12, `#shoulder_len` 26 to 39, `#boss_len` and `#boss_d` 16
to 24, and the part 343120.267 to 535952.324 mm³. Three things stayed put: `#shoulder_half`,
because it is half of `#torsoW` and `#torsoW` was not driven, and `#tilt` and `#yaw`, which are the
shoulder's aim and are typed on purpose. Put back at 96 mm, all twenty faces, the volume, the box
and all eight variables returned exactly.

That is stronger than reading the dimensions, because it catches a number that is right today and
unlinked. It is also worth knowing that `#ball` and `#wall` are themselves `#torsoH / 8` and
`#torsoH / 32`, so driving `#torsoH` drives the joints as well as the frame.

### /features can be spent for the day while everything else still answers

The comparison against 9p1p1 asked for `/api/partstudios/.../features` and was told the endpoint
was rate limited for another 9.7 hours. Nothing shortens that; the countdown runs against the
clock rather than resetting when you stop asking.

`bodydetails`, `boundingboxes`, `massproperties`, `variables` and `documents` all kept answering,
and the GUI is not rate limited at all. So the feature-for-feature comparison was done off the
feature tree read through the DOM in both documents, and the solid was compared face for face over
`bodydetails`. Both came back identical, which is the answer `/features` would have given.

The cost is recorded as a carried finding rather than hidden: the comparison is of names and order
rather than of each feature's parameters. A parameter that differed while the solid, the volume,
the box and all twenty faces agreed would have to be one that changes nothing.

### A feature dialog is not a form; it is the model

Tutorial 6's `plane for shoulder` frames had to be retaken: attempt 7 stood on a tree that six
failed attempts had littered with a red `Sketch 1`, two rows both named `Plane 1`, and an error
badge on the Features header. Opening the finished feature for edit looked like the cure. It rolls
the model back to the moment before the feature ran and shows it against the clean tree the tab has
now, which is a better picture than the original.

The first attempt at that cleared the Entities box, clicked where the pivot line is, and picked the
torso's side face instead, because the line lies in that face and a click aimed at it lands on
whatever is behind it. The script asserted, raised, and closed its page.

The torso came back 72 mm across with no shoulders on it.

Onshape applies a feature edit as you make it. There is no draft that is thrown away when the
dialog goes: the × cancels and reverts, and anything else — a crash, a closed page, a navigation —
keeps the last state the dialog applied. A script that opens a feature for edit has to press
Escape on every failure path, and one that does not is a script that can quietly rebuild the model
into something else.

Two more things came out of it. A sketch Onshape has already consumed is hidden, and a hidden
sketch cannot be clicked, so the line has to be shown before it can be picked. And even shown, an
8 mm line fitted to the screen is a few dashes on a face a thousand pixels across; the click has
to be made zoomed in.

The repair reads the bounding box back and refuses to finish unless the torso is 111.1018 mm across
again.

### A page sweep finds what reading a page never does

Six mechanical sweeps ran over `torso-joints.rst` before its `audit.page`, and between them they
found more than every close reading of the draft had. The sweeps and what each turned up:

- `blockcheck`: one pair of figures with the same bytes, `studs.hip-06` and `-07`. Nothing on
  screen changed between them, because the hip connector already pointed down and the flip button
  was never clicked. The take shot the second frame out of habit, from the neck's sequence.
- `instruction_first`: twenty-two pictures whose nearest thing above them was another picture, a
  caption or a heading. Some were the accepted frame after a name frame; some were one sentence
  covering three frames.
- `keycheck`: eleven of the take's twenty-three recorded presses were on no page. This is exactly
  `req.page.view_keys`, and the page had been read closely twice without anyone noticing.
- `altdiff`: all 157 alts against the `shows` the take wrote at the CAD. Forty-one differ. Four
  frames were reopened at full size, and two of the take's own records turned out to be wrong
  where the page was right.
- the name census: every literal and bold word with the line it first appears on, which is the
  student attack made mechanical.
- `ninja check` and a clean `ninja draft9p2`.

The lesson is that a page is not readable at this length. Two of the sweeps compare the page
against the log, two compare the page against itself, and none of them needs a model. They live in
[`tools/page_sweeps.py`](../../../../tools/page_sweeps.py) now, and running them back over the five
pages written before them found nine more pictures with no instruction above them, an untagged hero
on the assembly page, and the two presses that framed it on no page at all.

### The log can be wrong where the page is right

`mirror-06`'s `shows` says two mirrored bosses lean "the same way on both sides". `studs.mirror-03`'s
says the operation was "pushed back to **New**"; the dialog opened on **New** and stayed there.
Both were written at the CAD with the frame on screen, and both are wrong.

The page happens to say the right thing in both places, because it was written with the pictures
open. Anything written from the log alone would repeat the error, and so would any check that
compares a page against the log and trusts the log. That is why `altdiff` prints the pair rather
than passing or failing: the differences are where a person has to look, and the log is not the
answer key.

### A feature-panel crop is not the frame the take framed

`parts.body.numbers-01` carried a stale tooltip hanging in its graphics area, and the state it
holds cannot be reached again: the body tab had six features then and has thirty-seven now. The
version that keeps that state announces itself in its title bar, in a banner and in a tab strip
missing two tabs, so a frame taken there would put the student somewhere they are not.

Cropping to the feature panel keeps the half of the frame the sentence is about and drops the
tooltip with the rest. It is honest — no pixel is invented, and the promoted attempt directory
holds exactly what the page shows — but the frame reads as a tree frame rather than the `arrived`
frame it was shot as. The cure is upstream: frame the panel from the start when the panel is the
point.

### The audit.page gate is still owed

`stickbot-draft9p2-check` has never been created, so no page in this run has been reproduced from
its own words into a second document. Tutorials 1, 2, 3, 4, 5 and 6 all carry the reduced form of
`audit.page` with that block recorded as a carried finding. Creating the check document needs
Mike's agreement, which Phase P did not get.
