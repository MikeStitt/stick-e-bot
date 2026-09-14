# draft9p3 — notes

## Where the work is

| | did | ws |
| --- | --- | --- |
| `stickbot-draft9p3` | `50b2d87357670c07c2fbcb89` | `Main` |
| `stickbot-draft9p3-check` | `555033d6ce000bb44430dd6e` | `Main` |

Both were created empty on Sat 29 Aug and carry Onshape's default `Part Studio 1`, `Assembly 1` and
`BOM : Assembly 1`. Every element id is in [`reference/documents.json`](reference/documents.json),
and each tab is renamed as the tutorial that builds it reaches it.

The reference is `stickbot-draft9p1p1`, `4b2e0d48efd37d3327a90afb`, workspace
`a1af16872d25103815f1c32a`, and it is read only.

## P0 is read at the dependency level for every tab

All eight Part Studios, the assembly and the Variable Studio are in
[`reference/`](reference/README.md): 181 features, 13 mates, 11 variable rows.

**The assembly came back over REST.** `/api/assemblies/.../features` is a different endpoint family
from `/api/partstudios/.../features` and it is not rate limited, so tutorials 3, 7, 13 and 14 have a
full construction record — every mate's name, its type, and the two instances it joins — while the
Part Studio route is still refused.

**What is still owed is the constraint level**, and it is owed on all nine tabs. See
[`reference/README.md`](reference/README.md) § *What is in these files, and what is not*.

## P0's first read: the body tab, and what the dependency graph can and cannot see

`Show dependencies…` was read on all 33 features of `stickbot-draft9p1p1`'s `body` tab and on all 33
of `stickbot-draft9p2`'s. The reference's record is
[`reference/body.json`](reference/body.json). Both trees carry the same 33 features under the same
names in the same order.

**Four features are built on different things.**

| Feature | draft9p2 built on | 9p1p1 built on |
| ------- | ----------------- | -------------- |
| `pivot lines` | `Top`, `Front`, `Right`, `#shoulder_half`, `#shoulder_drop` | `Origin`, `Top`, `Front`, `#shoulder_half`, `#shoulder_drop` |
| `mirror shoulder` | `Right`, `shoulder` | `Right`, `torso block`, `shoulder` |
| `trim shoulder cut` | `trim shoulder pattern` | `torso block`, `trim shoulder pattern` |
| `add neck to body` | `torso block`, `shoulder`, `mirror shoulder`, `copy ball stud`, `copy for hip`, `copy for shoulder`, `duplicate shoulder and hip` | `torso block`, `copy ball stud`, `copy for hip`, `copy for shoulder`, `duplicate shoulder and hip` |

Three of the four are the same mistake: draft9p2's booleans and mirrors take the shoulder solids as
their own tool bodies, where the reference has already merged them into `torso block` and operates on
the block. The fourth is `pivot lines` picking the `Right` plane where the reference picks `Origin`.

**The anchoring tally is identical.** Twenty-one features stand on the model's own geometry in each
document, and the same four stand only on default planes and variables: `torso outline`,
`pivot lines`, `trim shoulder pattern` and `#boss_len`.

## The block for the design source

**9p1p1's shoulder chain is not anchored to the torso either.** `pivot lines` in the reference
depends on `Origin`, `Top`, `Front`, `#shoulder_half = 36 mm` and `#shoulder_drop = 8 mm`. It does
not depend on `torso block`. The side face and the top face the sketch lands on are reached by
arithmetic in the reference exactly as they are in draft9p2.

So *match 9p1p1* and *pick the geometry that already says where it goes* are two different targets in
this part of the model, and only the design source can say which one draft9p3 builds. Until it does,
the plan's rule holds: match the reference and write the departure down.

## What the dependency graph cannot see

The graph names what a feature was built on. It does not carry a sketch's constraints, an extrude's
direction or end condition, or what a dimension measures from. Twenty-nine of draft9p2's body
features are built on the same things as the reference's and the user could still see, by clicking
through the sketches, that they were drawn a different way. **P0 is not finished by this read.** It
finishes when `/api/partstudios/.../features` answers and the constraints and parameters are read
against it.

## Two of tutorial 2's frames are captioned wrong, and the page has to fix it

Both are `shows` records that describe the screen wrongly. The pictures are right, so nothing is
reshot; the page's caption is written from the frame instead of from the record.

- `parts.head.tab-03` names the tabs in the wrong order. The frame reads **body, head, robot
  sizes, Assembly 1**.
- `parts.head.variables-01` says the Name and Value boxes are empty. The Value box reads `0 mm`.

## A sketch has no axis, so the mouth is dimensioned instead

The mouth was to be held in the middle of the face by a symmetric relation about the sketch's
vertical axis. There is no such axis to pick: Onshape draws only the origin point, and a click
where the axis would be lands on the solid behind the sketch. Onshape answers *A symmetry
constraint requires a line and two other geometries of the same type* and adds nothing.

The mouth is held by a third dimension instead: its left end measured `(#mouthW - #mouthH) / 2`
from the origin, which leaves the line with nothing free to slide. 9p1p1's own mouth carries the
same three dimensions and is left free to slide sideways; draft9p3's is fully defined and reads
back at exactly -15 mm to 15 mm. The departure is in the head's `audit.part`.

## The collar circle is dimensioned `#collar * 2`, not `#ball + 2 * #wall`

Both expressions read 18 mm at a 96 mm robot, and they stay equal at every robot size, because
`#collar` is `#ball / 2 + #wall`. Draft9p2 typed the second one. Draft9p3 types the first, so the
socket's outside diameter is the collar row doubled and nothing else restates what `#collar`
already means. A reader who wants to know how thick the socket's wall is reads the row, not the
dimension.

## Where 1.6 mm comes from is not written down

`#slit` is the width of the four cuts that let the socket open around the ball. It is 1.6 mm in
9p1p1, and it was 1.6 mm in draft9p0 before that. It is not a fraction of `#ball`, `#wall` or
`#torsoH`, and it does not move when the robot's size does, which is why it stays typed and stays
in the tab. What it is a fraction of, if anything, is a printer number: it is close to four passes
of a 0.4 mm nozzle. Nothing in the repository says so. Until the design source does, the page says
what the number is for and does not claim where it came from.

## The head hides its own socket from anywhere above the horizon

The socket hangs under the middle of the head's underside, and the head is 72 mm across and 60 mm
deep, so a camera looking down on it, which is where **shift+7** puts one, cannot see the socket at
all. Tutorial 5's hero is **shift+7** and then four presses of the up arrow, which drops the camera
under the horizon; the corner view then carries both eyes, the mouth and the socket at once. Draft
9p2 ran into the same wall and settled for a front view and a view from below. The page has to tell
the reader to press the arrow, because a reader who does not will look at a picture of a plain head
and think a step went wrong.

## The head page tells the reader which side to look at the cut from

Which half a section keeps is decided by where the camera is standing when the plane is picked, so
picking Right makes *Section plane 1 (Left)* one time and *Section plane 1 (Right)* the next. The
rule and what it costs are in [`shots.md`](../../../build/shots.md) § *A cut is view state, and it
stacks*. What tutorial 5's page owes the reader is the sentence that turns that into an
instruction: read the word in brackets, and look from that side.

## The pages are being written after the takes, not between them

[`plan.md`](plan.md) § *Phase W* asks for each tutorial's page immediately after its `audit.part`
passes. This run is taking all fourteen tutorials first and writing the pages afterwards, which is
what the watchdog that is driving it asks for and what draft9p2 did. Nothing about a page depends
on the take that follows it, so the order costs the run only the chance to find a hole in a page
early. The register says which order was used.

## `pivot lines` is drawn on `Front` and dimensioned from `Origin`

[`06-torso-joints.md`](../../../build/plan/06-torso-joints.md) § *What we do not know yet* leaves
open whether the shoulder's construction sketch should stand on the torso's own faces instead. Two
things the repository already says point opposite ways: `stickbot-draft9p1p1` stands it on `Origin`,
`Top` and `Front`, and [`onshape.md`](../../../../.parts/onshape.md) § *Anchor each sketch to the
geometry that gives it meaning* asks for the side face and the top face themselves.

Draft 9p3 follows the reference. The run exists to make the CAD sketch style and 3D modeling steps
the same as 9p1p1's, and a sketch that lands on the same lines by a different route is exactly the
difference this run is chasing. The rule is not withdrawn: a sketch anchored to `Origin` and driven
by `#shoulder_half` and `#shoulder_drop` still moves when the torso does, because those two names
are what size the torso. What it loses is the reader seeing the face the number stands for, and
the page has to make up for that in words.

## The Variable Studio's Value cell was already written down

The first pass at `#limbD` tabbed out of the Name cell, which committed the row at `0 mm` and typed
the expression into the next row's Name box.
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md) § *Variable Studios* says both halves of
that already: *Tab commits the row but does not reach the Value cell*, and *a Value cell takes two
double clicks from cold*. It also says how to undo it, *Right-click a variable row → Delete*. The
pass that reads the how-to first is the cheap one.

## The sketch route answers while `/features` is refused, and it carries the geometry

`/api/partstudios/.../sketches?includeGeometry=true` was never rate limited. It hands back every
sketch's entities in meters, plus a four by four matrix that puts each sketch's own plane in the
world. That is not a sketch's constraints, but it is what the constraints produced, and for the
torso it was enough to settle the four things
[`06-torso-joints.md`](../../../build/plan/06-torso-joints.md) § *What we do not know yet* left
open:

- **`pivot lines` is one line**, on `Front`, running from 36, 48 down to 36, 40: a shoulder half
  width out, from the torso's top corner down by a shoulder drop.
- **`plane for shoulder` contains that line** and turns 30 degrees off `Front` about it. Its frame
  is normal 0.5, 0.866, 0, and the pivot line projects into it at minus 31.1769, which is
  36 times the cosine of the yaw.
- **`torso shoulder profile` is a rectangle 32 by 8**, its long edge running through the pivot
  line's lower end at 53 degrees below the horizontal, 16 mm each way. The long edge is the
  revolve axis; the 8 is the boss's radius, which is why the sketch dimension reads
  `#boss_d / 2`.
- **`trim shoulder pattern` is a rectangle above the torso's top face**, from 48 up to 64 and
  136 wide, which is a boss diameter tall and two boss diameters clear on each side.

The reference's own dependency lists agree: `torso shoulder profile` is built on `#boss_len`,
`#boss_d` and `#tilt`, and on nothing else. What those lists cannot show is a name that lives in
the Variable Studio, because `#torsoH` and `#torsoW` have no feature row in this tab to be listed
as; that is why a rectangle whose top edge is `#torsoH / 2` above the origin looks, in the record,
as though nothing places it.

[`../../../../tools/read_sketches.py`](../../../../tools/read_sketches.py) is that route, written
down so the tabs still to come do not have to rediscover it.

## A plane built on a midpoint snap stops the whole Part Studio

`plane for shoulder` stands on the pivot line and turns `#yaw` away from `Front`. The
first pass picked the line at its middle, at 12 px/mm, and Onshape gave the midpoint
rather than the line: the dialog's second leaf read `Edge point`. The plane took it, the
tick went through, and `errors()` came back empty.

What happened next is worth writing down, because nothing in it says "this feature is
wrong":

- every row in the feature list turned grey and italic, back to `Origin`
- the variable rows stopped showing values and showed their expressions instead:
  `#shoulder_half = #torsoW / 2` where they had read `#shoulder_half = 36 mm`
- the parts list read `Parts (0)` and the canvas was empty
- a reload showed the same, and so did a second reload
- `sketches?includeGeometry=true` answered 200 with an empty list
- `/api/parts` still answered `torso`, from the last microversion that computed

The reading that fits is that the Part Studio stopped computing at the top rather than
failing at the feature that caused it, so no row carries an error marker and the tab
looks paused instead of broken. Deleting the plane brought the torso and the values back.

Two things follow for the rest of this run:

- Pick a line a quarter of the way along, never at its middle. A midpoint snap is as
  strong as an endpoint snap, and the dialog's own words are the check: an entity leaf
  that says `point` when a line was wanted is the bug, and the step raises on it.
- A step that adds a plane or a datum has to prove the tab still computes. `errors()` is
  not enough. The step now waits for the part and an evaluated variable row to be back in
  the tree, and raises if they are not.

The same reading explains the grey italic rows seen earlier and put down to a mid-rebuild
read: grey italic in the feature list means Onshape has no computed result for that row,
whether because it is hidden or because nothing computed at all.

## A constraint badge takes the click the line was meant to get

Onshape draws a small badge on the canvas beside every constraint it holds, and the
aligned rectangle arrives with several. A click on a badge selects nothing, and worse, it
drops whatever was already selected: the log reads `selected 96 -> 0` and the next pick
has lost its partner.

Aiming at a fixed fraction along an edge does not survive this, because where the badges
land depends on what the sketch inferred while it was drawn. The profile step now gives
every edge pick five places to try along its own length and starts the whole run again
when one fails, since a failed click has cleared the run behind it.

Two numbers come out of the same work and are worth keeping:

- A highlighted sketch line is about four pixels wide, so what a pick lights up scales
  with the line's length: a 32 mm edge at 9 px/mm is about eleven hundred pixels, an 8 mm
  edge under three hundred. A guard written as a flat pixel count fires on the long edge
  of a big rectangle. Each pick carries the length it should have instead.
- A face is still an order of magnitude above any of that, which is what the guard is for.

A badge does worse than take a click, though. Sometimes it answers one: the parallel badge
sitting beside the profile rectangle's short edge lit up 456 pixels where the 8 mm edge
itself is worth about 280, which is inside any band wide enough to be useful. The pixel
count cannot tell a badge from a line.

Dimension can. It takes whatever it was handed and opens a box to type into only when what
it holds can carry a dimension, so a badge leaves it with the picks made, the label placed
and nothing on the screen. That is now the proof: `L.dim` raises `NoField` rather than
typing into the canvas, and the caller moves the pick along its line and runs the whole
thing again.

## Say which plane inside the dialog, not before opening it

Picking a plane in the tree and then pressing Sketch is the natural order, and it is what
tutorials 1 to 5 do. On the sixth tutorial it stopped being reliable. One pass had
`plane for shoulder` reading as the only selected row, pressed Sketch, and got a sketch
on `Face of torso block`: the rectangle then drew flat against the front of the torso and
every dimension after it was measured in the wrong plane.

Nothing in the tree says so. What said so was a measurement: two points that are 32 mm
apart in the shoulder's plane drew 30.517 mm on screen, which is what those two points
measure seen along Front. The step now does two things instead of trusting the click:

- It opens the sketch with nothing selected and picks the plane inside the dialog, then
  reads the dialog back and raises unless the plane's name is in it.
- It keeps the 32 mm measurement as a second check, because the dialog naming the right
  plane and the camera looking along it are two different claims.

The measurement is worth keeping for its own sake. A sketch step that starts by proving
the view is square on to the plane it thinks it is on cannot draw a whole feature into
the wrong place, and the check costs one camera read.

## Three things stand where the pivot line stands, and `Use` will project any of them

`Use (Project/Convert)` projects whatever is clicked onto the sketch plane, and for a face
or a plane the sketch plane runs through, what it projects is the line where the two meet.
The pivot line stands at x = 36 mm, z from 40 to 48, and three other things in the tab run
along that same place:

- The torso's right face, whose plane is x = 36 mm. Its cut is 96 mm long, the height of
  the torso.
- `Front`, because the pivot line is drawn on it. The shoulder plane meets `Front` along
  the pivot line's own place, and the projection runs the width of the plane's square.
- `torso outline`, the sketch `torso block` is made from. Its right hand edge is the line
  x = 36 mm from z = -48 to 48, exactly 96 mm, and it is the same line the pivot line
  sits on the top eighth of.

So a click aimed at an 8 mm line kept projecting a line twelve times longer, and the
sketch was dimensioned to it. Four passes read this as a pixel problem and moved the click
along. A throwaway sketch, given the one click, committed and read back through the
sketches route, settled what was arriving:

    lineSegment  startPoint [-31.177, 48.0]  endPoint [-31.177, -48.0]

The last one is the one that is easy to miss, and it arrives by way of the cure for the
first: suppressing `torso block` puts `torso outline` back on the screen, because a sketch
is hidden while a feature is using it and shown again when nothing is. Taking the face out
of the way is what puts its sketch in the way.

Two things were ruled out on the way, and both are worth writing down:

- The button at (576, 58) is `Use (Project/Convert) (u)`, read off its own tooltip. It was
  not Intersect wearing Use's name.
- Suppressing a feature takes it out of the model, which a read of the model confirms:
  the parts route answers with nothing for `torso block`, and the sketches route stops
  listing `torso outline`. Hiding a part only stops it being drawn.

The step now hides the three planes, suppresses `torso block` and then `torso outline`,
does the `Use` from the `pivot lines` row in the feature list rather than from the canvas,
and measures what arrived: it picks the projection once and raises unless it costs about
what an 8 mm line costs. A wrong projection looks right in the tree and in a screenshot.
Both features are unsuppressed again, outline first, before the step ends.

## An angle between two lines has four answers, and the clicks choose which

The rectangle is drawn beside the pivot line at the lean it wants, and the angle dimension
is meant to hold it there. Typing `90 deg - #tilt` swung it round by more than a hundred
degrees instead: Onshape had offered 143 degrees, and 37 was a different angle of the same
pair of lines.

The two lines do not touch, so Onshape works from where they would cross if they ran on,
which for this pair is a little above the pivot line's top end. Every click on the pivot
line is below that crossing. A click on the rectangle's long edge up beside its top corner
is above it, and that pair of sides is the 143; a click well down toward the bottom corner
is below it, and that pair is the 37.

Where the label is dropped decides the rest. With both clicks on the right side of the
crossing but the label placed up and away from the geometry, the dimension came up reading
322.9667522 degrees, which is 360 less the 37 that was wanted. An angle dimension shows
whichever of the four angles the label lands inside, so the label goes in the wedge
itself, on the line that splits it, about 14 mm down from the crossing.

Three changes came out of it:

- The long edge is clicked three quarters of the way down toward its bottom corner, not a
  quarter of the way down from the top.
- The label is placed inside the wedge rather than clear of the drawing.
- `L.dim` takes an `expect`, reads the value the dimension comes up with before anything
  is typed, and escapes the dimension rather than typing into it when the reading is not
  near what was wanted. A dimension typed into the wrong angle leaves geometry that is
  fully defined, black, and in the wrong place. This is what caught the 322 degrees, and
  it left the sketch fit to try again.

## `Hide` clicked is not `Hide` done, and a right click leaves the row selected

The pass that hid the torso and then projected a 96 mm line had clicked `Hide` and
carried on. Two things came out of that:

- A step that hides a part reads the menu back. The menu offers `Hide` for a part that is
  showing and `Show` for one that is not, so the state is readable before and after, and
  the step tries again rather than building against a part it thinks it put away.
- A right click selects the row it lands on, and a selected tree row changes what the
  toolbar does: pressing Sketch with one selected opened nothing at all, and the run
  carried on clicking into a document with no sketch. Clicking empty canvas does not
  clear a tree selection; clicking the row again does.

## `/features` answers again, and it settles the mate connector

The rate limit that refused `/features` through the whole of P0 has lifted. The body tab's
answer is in `reference/body.features.json`, and it carries what the sketches route cannot:
every feature's parameters by name.

The first thing it settled is `connector on torso shoulder`. 9p1p1's reads:

    originType ON_ENTITY   originQuery ['JMB']   entityInferenceType CENTER
    allowOwnerEntity True   requireOwnerPart False   ownerPart []   attachmentOption NONE

A circle picked on a part fills the connector's owner in for you, and an owner brings an
attachment with it: `ownerPart` gets the boss and `attachmentOption` becomes `TO_OWNER`, so
the connector is fixed to the boss and travels with it rather than standing where the arm's
ball has to find it. Two controls hold that between them, and it takes both clicks:

- `Owner entity` is a checkbox, and it reads back as `requireOwnerPart`.
- `Select owner entity` under it is a query field holding the part, and what empties it is
  the × beside the part's own name, not a click on the field.

Emptying the field on its own leaves `requireOwnerPart` true with nothing to satisfy it,
and the feature arrives red: `connector on torso shoulder [Mate connector] did not
regenerate properly: Cannot determine owner of mate connector.` Unticking the box on its
own leaves the part in the field and the attachment `TO_OWNER`.

The order of the two clicks decides it. Unticking the box takes `Select owner entity` and
the `Attachment` row off the screen without letting go of what they hold, so the boss stays
the owner and the attachment stays `TO_OWNER` out of sight; the dialog then reads as though
the question had gone away. Empty the field first, while it is still on the screen, and
then untick the box. That order reaches 9p1p1's shape and the other three do not.

Reading the feature back is what caught all of this, and a diff against 9p1p1's own
parameters is what named the one that was wrong. Every wrong version sat in the tree
looking right, and two of the three had no error on them at all.

`JMB` is also the id 9p1p1's connector hangs on, so the pick landed on the same entity in
both documents. That is worth noting and not worth relying on: geometry ids are not
promised to match between documents, so the step records a deviation rather than failing
when they differ.

## Unticking `Merge with all` empties the scope field under it

`Mirror` opens with `Merge with all` ticked and the scope field beneath it already holding
the torso. Untick the box and the field is emptied, so the torso has to be named again.
Left empty, `Add` merges the copy with nothing: the tab ends up holding three parts where
it should hold one, the feature is not red, and the shape on the screen looks right,
because a boss standing beside the torso and a boss merged into it are the same picture.

The step reads the field back until it holds `torso`, the same way the mate connector step
reads its parameters back. One click on the part row is not always taken.

With the scope set, `Add` merges the copy and the boss it was made from, both, and the tab
goes from three parts to one. That is what 9p1p1 has: its body tab holds a single part
called `torso`, and `add neck to body` unions six bodies that do not include a boss, so
both bosses are already inside the torso by then.

## A deleted feature stays in the feature list for a moment

The list is read off the page, and the page takes a second or two to catch up with a
delete. Reading it straight away gives a list with the deleted feature still in it, and a
take handed that list sees the step create nothing and fails with `model gained [] and
lost []`. `drop` now waits for the name to go before it returns.

## The reference record must read `expression`, not `value`

A quantity parameter comes back from `/features` carrying both: `value` is the number in
meters or radians, and `expression` is what was typed. Reading `value` alone made the trim
cut's depth look like `0`.

It is `2 * #torsoD`. The cut is symmetric, and a symmetric extrude splits its depth evenly
either side of the sketch, so twice the torso depth reaches a whole torso depth each way.
Typing `#torsoD` reaches half a torso depth each way, which lands exactly on the front and
back faces; that is the kind of coincidence that holds until someone changes a variable.

## `boundingboxes` answers `{}` for this tab, and a face's box is not the face

`/api/partstudios/.../boundingboxes` and `/api/parts/.../partid/JHD/boundingboxes` both
come back `200` with an empty object, so how high the solid reaches has to be read some
other way. `bodydetails` gives every face its own box, and the highest of those is the
reading the trim step uses.

That reading is an upper bound while anything on top is round: a box around a curved face
is bigger than the face. Before the cut it says 57.5927 mm, and that number must not be
quoted as how far the boss stands above the top face, because the boss's highest face is
its cylindrical side and the box around it reaches past the solid. After the cut the top
is flat, and a flat face's box is the face, so 48 mm is exact.

The vertex list is no use for this either. Its highest point is already 48 mm before the
cut, because the top of a boss is a curve with no vertex on it.

## Search tools lets go of the selection before it opens a tool

`arm` clears every selected row on purpose, because a held row changes what the toolbar
does. So a region cannot be picked first and found waiting in the dialog: it goes in after
the dialog is open, and the field is read back until it holds it. An extrude with an empty
region field takes a depth, a direction and a merge scope without complaint and cuts
nothing.

`Symmetric` is a checkbox in the Extrude dialog, not one of the choices in the `Blind`
menu beside it.

## A field names what it took the way Onshape thinks of it

`trim shoulder pattern` picked as a region reads back as `Faces of trim shoulder pattern`.
A read-back that tests for the exact name turns a good pick into a failure, and clicking
the row again to fix it takes the pick back out, so the field ends up empty. The test is
whether the name is in what the field says, not whether it is what the field says.

## The trim survives the reorder

This was the open question in the brief: with the shoulders built before the studs, the
mirror is split in two and `trim shoulder cut` runs while only the shoulders exist. It
reaches both. The tab reads 48.0 mm at the top after the cut, with a boss axis at
(-36, 0, 40) and (36, 0, 40), one part, and the cut's own parameters the same as 9p1p1's:
`REMOVE`, `BLIND`, symmetric, depth `2 * #torsoD`, scope the torso by name.

## A helper that reads the state can still have the two words the wrong way round

`visible` compared the state it read against the word it was about to click, and those are
opposite words. A part that is showing offers `Hide`; the item you click to show a hidden
part is `Show`. Comparing the two meant the helper stopped without clicking in exactly the
cases that needed a click, and clicked in exactly the cases that were already right.

So `visible(torso, shown=False)` left the torso showing, and `visible(torso, shown=True)`
at the end of the same step hid it. Everything after that was captured against an empty
view: the trim's hero frame is a datum plane and nothing else, under a caption describing
a torso with two shoulders on it.

Nothing measured wrong, which is why it ran for two whole steps. The corners came back
right, the top came back at 48 mm, and the parts list said one part. The frames are the
only place it showed, and it took looking at one to see it.

The helper now names the two words apart: `click` is the item that gets the part where it
is wanted, `done` is what the menu offers once it is there.

## A step that draws a sketch again has to take what stands on it

`trim shoulder cut` reads `trim shoulder pattern`. Running the band's step a second time
deletes the band and draws a new one, and the cut goes red the moment the sketch it reads
is replaced: the step then fails on an error that belongs to a feature it never touched.
The band's step drops the cut as well, and the cut's own step builds it back.

## The measurement readout is not on the page

`read_mm` and `read_area` scrape the status bar for `Total length`, `Length`, `Area`,
`Radius` and `Diameter`. They answer `None` for every selection, however long they are
given: a line in a sketch, a face on a solid, one entity or two. The readout a person sees
in the bottom right of the window is not reachable from the leaf text the scrape reads.

`dim_run` never depended on it. It picks, hands the pick to Dimension, and reads the
dimension's own value, which is why the band's three dimensions all passed while the log
said `the status bar reads None mm` under each of them.

What did depend on it was naming a face by its area, which is how a step was to tell the
torso's top face from its bottom face. That check now comes off the camera instead:
`nearer` puts a point through the modelview matrix and compares eye-space z, so the step
proves which face is turned towards it before it picks anything.

## At the middle of the screen the origin is in front of everything

Looking straight at the underside of the torso, the origin at `(0, 0, 0)` draws at the
same pixel as the middle of the face at `(0, 0, -48)`, and its marker takes the click. The
pick succeeds and is worth about a hundred pixels, where the face is worth half a million.

So a face is picked off to one side, and the pick is checked for size rather than for
having happened at all. A hundred pixels is a marker, a few thousand is an edge, and a
face after `f` fills the screen.

## The reference record loses what a derive points at

`copy ball stud` is an `importDerived`, and the record of it reads:

    partStudio = null
    parts = []
    location = []

The two that matter are both empty. `partStudio` is a reference to another tab and `parts`
is the list of what to bring across; neither is a query and neither is an expression, so
`params` falls through to `value` and gets nothing. The record says the derive places its
import at the origin and brings the mate connectors and the properties with it, and it
does not say what it brings or where from.

So the derive's step cannot be checked against the reference the way the others are. What
it can be checked against is the result: the tab gains a part named for the stud, standing
at the origin, with the stud's own mate connector on it.

## The toolbar highlight covers the row Search tools reports

`Highlight tool in toolbar` is ticked in the search panel. Searching for a tool that lives
in a toolbar menu opens that menu and highlights the tool inside it, and the menu is drawn
over the search panel. The result row underneath is still on the page, still the right
size and still in the right place, so a locator that reads the page finds it and a click
sent to it lands on the menu instead. The tool never arms.

It bites tools in a menu and not tools with their own button: `Extrude` armed every time,
`Mate connector` armed once and then stopped.

`elementFromPoint` says what is drawn on top at a pixel, and dropping every covered row
leaves the highlighted menu item. That does not fix it: the highlighted item will not take
the click either. Search tools has no route to a tool that lives in a menu while the
highlight is on.

What works is the tool's own shortcut. The menu prints it beside the name, `Mate connector
ctrl m`, and `arm` now takes a `key` and presses it, with the dialog as the read back and
Search tools left as the fallback for tools that have no shortcut. It is also the route a
person would take and the one the guide can print.

## The five joint connectors have five different names, spelled three ways

9p1p1's body tab ends with `neck connector`, `left shoulder connector`, `r shoulder
connector`, `l hip connector` and `r hip connector`. The names are distinct, so the
duplicate-name trouble the 2026-08-20 audit found in the original `stickbot` document is
already fixed here; that worry does not carry into draft9p3.

What has not been fixed is the spelling. One side is `left` written out and the other four
are single letters, and the neck has no side at all. draft9p3 reproduces 9p1p1's names as
they are, because the structural check compares names and the run exists to match 9p1p1's
construction.

**For Mike:** whether to keep them or make them `left shoulder connector` / `right
shoulder connector` / `left hip connector` / `right hip connector` is a decision for the
next draft, not this one.

## A route cannot see what a dialog is previewing, but the feature list can

The Derived dialog draws the part it is about to bring across as soon as the tab is
chosen, and the feature list on the page counts it: `Parts (3)` where a moment before it
said `Parts (1)`. `/api/parts` still answers `['torso']`, because it answers from the
committed model.

So a step that has to know what a dialog is doing before it ticks it reads the feature
list, and only checks the route afterwards. The derive needs this: choosing the tab brings
every part in it, and naming the one that is wanted has to be seen to have narrowed it
before the feature goes in.

## The origin will stand in for a mate connector, and the move looks like it worked

`Transform by mate connectors` takes any point as its `From`. The derived stud arrives at
the tab's origin with its ball centered there and its own connector a stud length up the
stalk, so on the screen the origin's marker and the connector's triad sit ten millimeters
apart. A pick aimed between them reaches the origin, Onshape accepts it as a connector of
its own, and the feature goes in green: the stud moves, the field reads back full, and
nothing anywhere says the wrong thing was picked.

What it costs is ten millimeters. The ball lands on the neck connector at z 48 instead of
a stud length beyond it at z 58, so the ball is half sunk in the top face and the head
will clip on inside the torso.

The connector came across under `copy ball stud`, and opening that row in the feature list
shows it by name. That is where this step picks it, and the field is read back against the
name. The measurement afterwards is against 9p1p1's ball at z 58, not against "above the
top face": at 48 the check would have passed on a stud that is buried.

## `socket connect to robot` infers a centroid where 9p1p1 infers a center

Reading both documents' ball and socket tabs side by side, `stud connect to robot` matches
9p1p1 exactly: `ON_ENTITY`, the same query, `CENTER`, no transform. Its neighbor does not.

    draft9p3   socket connect to robot   entityInferenceType = CENTROID
    9p1p1      socket connect to robot   entityInferenceType = CENTER

A centroid is the average of a face's area and a center is the middle of its circle, and
they are the same point only while the face is symmetric. This is a tutorial 4 defect, in
the ball and socket tab, not a tutorial 6 one. It is recorded here to be fixed there.

## A tool opens with what it was last given

`mirror shoulder` chose Add and named the torso as the merge scope. Nine steps later
`duplicate shoulder and hip` opened Mirror and found Add already chosen and the torso
already in the scope field, so the two mirrored studs were merged into the torso instead
of standing beside it. The geometry check passed: all five balls were exactly where 9p1p1
puts them, because a merge does not move anything. What caught it was the reference check,
which reads the committed feature's own parameters:

    operationType reads 'ADD' where 9p1p1's reads 'NEW'

So a step that depends on an operation, a checkbox or a scope says so with a click and
reads back that it took. Reading the dialog's words does not do it: `New`, `Add`, `Remove`
and `Intersect` are all written there whichever one is in force. They are `div.option`
elements in a row, and the one in force is the one carrying `os-active`; that class is the
only thing on the page that answers the question.

Clicking the type dropdown above them to confirm it reads `Part mirror` is worse than not
looking. It is already on Part mirror, and opening the list draws it over the buttons
underneath, so the click meant for `New` lands in the list instead and the operation never
changes.

The same is true of the guide: a student who has just done `mirror shoulder` will find
Mirror on Add too.

## Picking several rows moves the rows

Each name that goes into a query field makes the field taller, and the panel below it moves
down by that much. So a step that reads all five studs' positions once and then clicks all
five puts four of them in and misses the fifth, or lands on a neighbor. `add neck to body`
did exactly this: it read five rows, clicked five times, and the field ended up holding
three studs. The union then went in green with two loose balls left standing beside the
robot.

The fix is to read the rows again before every click and to click by how many the field
already holds, so each click is aimed at where the row is now rather than where it was.
The field's own contents are what says when to stop.

## A union is named after whatever went in first

`add neck to body` picked the five balls and then the torso, and the one part that came out
was called `Ball stud`. Nothing was wrong with the shape: the robot's body was whole, all
five balls in place. It had the wrong name, and the name is what the assembly and the
structural check look for.

The torso goes into the field first and the balls after it. The check is the part list
afterwards, which has to read exactly `['torso']`.

## A connector picked off a face arrives attached to that face

The Mate connector tool fills `Attachment` with `To selection` whenever the origin is picked off
a face, and it writes the same face into `Attach to`. 9p1p1's five joint connectors all read
`attachmentOption: NONE`. The difference does not show anywhere in the model: the connector sits
at the same point either way, and the tab's geometry, the balls' coordinates and the parts list
are all identical. What changes is what happens later. An attached connector travels with its
face, so recutting or replacing that face carries the connector with it or breaks it; an
unattached one is owned by the part, which is what makes 9p1p1's connectors move with the body
and survive a change to the ball underneath.

So the step sets the dropdown back to `None` and reads the field back before it accepts:

```
for _ in range(3):
    if L.held(page, "Attachment", "Attach to") == ["None"]:
        break
    page.mouse.click(*L.dlg_at(page, "To selection"))
    page.wait_for_timeout(1400)
    page.mouse.click(*L.on_top(page, "None", x=(240, 700)))
```

Like the mirror's Add, this was caught by diffing the committed parameters against 9p1p1's own
record and by nothing else. A step that only checks the geometry passes with it wrong.

## A sketch will dimension to model geometry without projecting it, and say nothing

`torso shoulder profile` was built to a step whose frame caption reads "the pivot line now
drawn into this sketch as well, which is what Use does". Use was never run. The built sketch
holds four entities, the rectangle's four edges. 9p1p1's holds five: those four edges and a
projected copy of the pivot line, put there by three `PROJECTED` constraints.

Nothing about the model said so. The rectangle came out the right shape, in the right place,
carrying the same expressions, and the solid it revolved is 9p1p1's solid to three decimal
places. What happened is that Onshape let the rectangle be dimensioned straight to the pivot
line as an outside reference: the angle reaches the pivot line's edge and the midpoint reaches
the line's lower end. 9p1p1's reach the projected copy of each. Both hang off the same two
pieces of geometry, so both survive a change to `#shoulder_drop`; the sketch simply does not
contain the line the caption says it contains.

It shows up one step later. `shoulder`'s revolve profile is a plain query on a face where
9p1p1's is a sketch region query, because with no projected geometry there was no sketch region
to pick.

Across the tab the same habit runs the other way as well. Where 9p1p1 constrains to `IB`, the
sketch's own origin, five of these six sketches constrain to ids in the part studio's space,
picked off the screen. Counted whole: 9p1p1's constraints name the sketch origin seven times
and these name it four, while these name three ids 9p1p1 never touches, five times between
them. Three sketches carry one constraint more than 9p1p1's as a result, which is what it costs
to pin a point against two things picked off the screen where one origin would have done.

`torso outline`, built back in tutorial 1, is identical either side. That is the control: the
read is sound and the drift began in tutorial 6.

The test that catches it is a sketch-by-sketch diff of both `/features` records, comparing
entity counts, constraints by type, dimension expressions, and every id the constraints reach
for outside the sketch. Two things make that diff lie if they are got wrong:

- A dimension's value is the parameter whose `parameterId` is `length`, `angle`, `radius` or
  `diameter`. `labelDistance` and `labelRatio` are expressions too, and they hold where the
  number is drawn on the screen, so reading the last expression in the list makes every sketch
  look different from every other.
- A geometry id is not promised to match between two documents, so the ids are worth comparing
  only for their shape and their count. Here they do match, because both tabs were built the
  same way in the same order, which is what makes the five that differ worth reading.

## The block for tutorial 6's construction

`audit.part` grades five construction differences blocking, on the plan's own rule that a part
whose shape matches and whose construction does not is blocking, because the page is written from
the construction. The shape is not in question: the tab is 9p1p1's solid on every measure taken,
and every one of the 33 features is the same type in the same order under the same name with no
parameter value differing anywhere.

What differs is in the sketches, and it is one habit with two faces:

- `torso shoulder profile` never ran Use, so it holds four entities where the reference holds five,
  and dimensions straight to the pivot line instead of to a projected copy of it. `shoulder` then
  picks a face where the reference picks a sketch region.
- `pivot lines`, `hip connector location`, `neck connector location` and `trim shoulder pattern`
  each reach for something picked off the screen where the reference reaches for the sketch's own
  origin, and three of them carry one constraint more as a result.

Only Mike can settle what happens next, and the choice is not free either way:

- **Rebuild the five sketches to the reference's construction.** `torso shoulder profile` is
  feature 14 of 33, so the edit lands mid-tree, and the step's twelve frames and the revolve's six
  are taken again. The four smaller sketches cost roughly another twenty frames. Tutorial 6's
  version is published, so there is a point to come back to.
- **Carry the deviation and write the page from what was built.** The page then teaches a model
  that reaches the same shape a different way from the reference, which is the thing draft9p2 was
  superseded for.

This is the same disagreement [The block for the design source](#the-block-for-the-design-source)
records, arrived at from the other end. That section says *match the reference and write the
departure down* holds until the design source rules. The departure is now written down and it is
larger than one sketch, so it is worth ruling on before tutorials 7 to 14 are built the same way.

**It is also larger than one tutorial.** The same diff run against the tabs tutorials 2, 4 and 5
built puts tutorial 4 in worse shape than tutorial 6: four of the reference's five tab variables
were never made, and three of the expressions standing in for them scale where the reference's are
constants, so that joint is 9p1p1's joint at 96 mm and nobody's at any other size. Tutorial 6
changes how a shape is arrived at; tutorial 4 changes what the shape becomes when the robot is
resized. Both are in the same decision.

## Tutorial 4 built a ball and socket that is 9p1p1's only at 96 mm

The sketch diff was written for tutorial 6 and then run against the tabs tutorials 2, 4 and 5
built, because `/features` now answers for all of them. The head is clean: 26 features either
side, same order, all twelve of its variables identical, and one sketch reaching for the origin
twice where the reference reaches for the origin and an edge.

The ball and socket is not clean. 9p1p1's tab defines five variables of its own and draft9p3's
defines one:

| 9p1p1 | draft9p3 |
| --- | --- |
| `#stalk = #ball / 2` | not made |
| `#slit = 1.6 mm` | `#slit = 1.6 mm` |
| `#stud_len = 10 mm` | not made |
| `#slit_in = 5 mm` | not made |
| `#slit_out = 12 mm` | not made |

The four that were never made are spelled out in the sketches instead:

| sketch | 9p1p1 | draft9p3 | at 96 mm | at 120 mm |
| --- | --- | --- | --- | --- |
| `stud profile` | `#stalk / 2` | `#ball / 4` | 3 mm either way | 3.75 mm either way |
| `stud profile` | `#stud_len` | `#stand` | 10 mm either way | 10 mm against 12.5 mm |
| `slit profile` | `#slit_in` | `#ball * 5 / 12` | 5 mm either way | 5 mm against 6.25 mm |
| `slit profile` | `#slit_out` | `#ball` | 12 mm either way | 12 mm against 15 mm |
| `collar profile` | `#ball + 2 * #wall` | `#collar * 2` | 18 mm either way | 22.5 mm either way |

Two of the five are the same expression written another way and hold at every size. Three are
not. `#stud_len`, `#slit_in` and `#slit_out` are constants in the reference and the expressions
standing in for them all scale with the ball, so **the two joints are the same solid at 96 mm and
different solids at every other size**. Driving `#torsoH` to 120 mm makes draft9p3's stud 12.5 mm
long where 9p1p1's stays 10 mm.

Nothing caught this. Tutorial 4's `audit.part` ran a drive test to 120 mm and passed it, because
what it checked was that draft9p3's own joint moved coherently, which it does: every substituted
expression is ball-derived, so the whole tab scales together. It never held the driven numbers
against 9p1p1's driven numbers. Every other check it ran was at 96 mm, where the two agree
exactly.

Outside the sketches the tab is sound: every feature is the same type in the same order under the
same name, and the only parameter that differs is `socket connect to robot`'s
`entityInferenceType`, which is already recorded.

Which way this should be fixed is not obvious. `10 mm`, `5 mm` and `12 mm` are typed numbers in
the reference, and a typed number in a model that is meant to be driven is the thing
[`.parts/onshape.md`](../../../../.parts/onshape.md) argues against. draft9p3's expressions may be
the better model. What is certain is that the departure was made without being noticed and without
being written down, which is what the plan's *report a departure instead of making one* exists to
prevent.

## The reference settles tutorial 7's pick order

[`07-assembly-head.md`](../../../build/plan/07-assembly-head.md) lists *whether the first pick has
to be the part that moves* under what we do not know yet. 9p1p1's `head to neck` answers it: the
mate's two queries are in order `head mate`, which is the connector on the head, then `neck
connector`, which is the one on the body. The part that moves is picked first, which is Onshape's
own convention.

That is worth confirming at the screen rather than only in the record, because the brief also asks
what a wrong pick looks like and wants a frame of it. The record says which order to build; it does
not say what the reader sees if they go the other way.

Both connectors exist under those names in draft9p3 already: the head tab's 26 features match
9p1p1's name for name, and tutorial 6 built `neck connector` on the body.

## The head is the right shape and `drop socket to neck` is told a different number

Running the parameter diff over the head tab, the way tutorial 6's `audit.part` runs it, turns up
three construction differences that tutorials 2 and 5 never looked for. The head's solid is not in
doubt: all 47 faces match 9p1p1's face for face on surface, place, direction and area, and so do
the volume, the area and the centroid.

- **`drop socket to neck` turns the socket 30 degrees where the reference turns it 180.** Every
  other parameter of the feature is identical, including the 25 mm distance. The socket still lands
  in exactly the same place, because the feature's `baseConnector` and `destinationConnector` are
  different entities in the two documents, and the angle is measured from whichever connector was
  picked. Thirty degrees from this build's base is 180 degrees from the reference's.

  Nothing is wrong with the model. What is wrong is what the page would say. A reader told to type
  30 degrees gets the socket in the right place only if they also picked the connectors this build
  picked, and the page has no way to make them. This is blocking for that reason and not for the
  geometry.

- **`second eye` reads `fullFeaturePattern` false where the reference reads true.** Both make the
  same eye in the same place.

- **`head mate` carries a secondary origin pick the reference does not have.** Where that lands
  is measured in [The rim of the socket comes along with the
  ball](#the-rim-of-the-socket-comes-along-with-the-ball); it is blocking.

The head's `head mate` and `socket mount point` both read `attachmentOption: TO_SELECTION`, and so
do the reference's. The connectors that arrive attached are the body tab's five, recorded under
[A connector picked off a face arrives attached to that
face](#a-connector-picked-off-a-face-arrives-attached-to-that-face); the head's are attached in
both documents and are not a departure.


## The rim of the socket comes along with the ball

Tutorial 7 mated the head to the neck, and the head came to rest 0.8 mm off the plane of symmetry.
The reference puts it on the plane. Everything else about the mate agrees: same type, same limits,
same offsets, same two connectors, and the head at the same height of 103 mm.

The 0.8 mm is not in the solids and not in the mate.

- Both neck balls are a sphere of radius 6 mm centered at (0, 0, 58), read off `bodydetails`.
- Both socket cavities are a sphere of radius 6.08 mm centered 45 mm below the head's own origin.
- `neck connector` holds the same face, the same `CENTER` inference and the same zero offsets in
  both documents. So does `head mate`, except for one thing.

`head mate` holds a second entity in `secondaryOriginQuery` that the reference leaves empty. With
two entities the connector does not sit on the sphere's middle; it sits 0.8 mm away from it, and
the socket the head hangs by is 0.8 mm off the ball it is meant to turn on. Tutorial 5's own frame
shows it: the Bottom view of the socket has two connector triads in it, `socket mount point` on the
axis and `head mate` a little below it, about 25 px apart where a millimetre is 30 px.

**This is blocking.** It is the robot's first joint and it does not sit where it should.

The second entity is not a second click. `head mate` was deleted and built again eleven times, and
one click on the ball produces it every time. Nine pixels across the opening were tried, three zoom
levels, selecting the face before arming the tool, and clearing the owner entity in the dialog. The
pixels away from the middle give `MID_POINT` and a different edge; the middle gives `CENTER` and
this edge; selecting first gives nothing at all, because the dialog opens empty and throws the
selection away. `KrVB` is a `K` id, which is an edge, and the only edge near the pointer is the rim
of the socket's opening.

The gesture is not the problem, and neither is the tool. Five connectors in the body tab sit on the
middle of a ball with one entity and nothing else: `neck connector` and the four shoulder and hip
connectors. Every one of those balls is convex and is picked from outside, where the pointer sits on
open surface. The socket's ball is concave and is picked from inside, down its own axis, where the
rim rings the pointer whatever the zoom. That is the whole difference.

A second entity is also not wrong by itself. `stud connect to robot` carries one in both documents,
and `socket connect to robot` carries one in the reference and not in mine, which is the other way
round and is recorded as its own line. What matters is where the connector lands, and here it lands
0.8 mm out.

**This is for Mike.** Two ways out, and both change the design rather than the clicking:

- Take the deviation. The head turns on its ball either way and the robot prints; the joint is
  0.8 mm off the plane of symmetry and the guide would say so.
- Give the head's connector a different origin, the way `socket mount point` already has one. A
  connector built on the socket's own mount point, or on a sketch point, has no rim near it.

Tutorial 7 is built and its frames are taken, with the deviation measured in the take. `audit.part`
diffs a tab against the reference rather than only against itself, which is what found this.


## audit.part now compares parameters, and the three built tabs are clean but for six lines

`diff_construction.py` answers what each feature was built on.  It cannot see what a feature was
told, so a sketch that reaches the right shape from the wrong dimension passes it.
[`diff_features.py`](../../../../tools/diff_features.py) reads two `/features` files and compares
every parameter of every feature, with
[`read_features.py`](../../../../tools/read_features.py) fetching the tab to compare.

Geometry ids are per document, so a query is compared by how many entities it holds. `Jr6` against
`Js6` is the same pick on the same face; one entity against two is a real difference, and that is
what caught `head mate`.

A tab's variables all carry `###name = #value` as their tree name. Keyed on that name, twelve
variables collapse to one and eleven are never compared, which reads as a pass. The tool keys a
variable by its own name instead, so the head tab compares twenty-six features and not fifteen.

What it says about the three Part Studio tabs built so far:

| Tab | Agree | What differs |
| --- | ----- | ------------ |
| body | 28 of 33 | the five connectors' `attachTo`, already recorded |
| head | 24 of 26 | `head mate`'s second entity, and `second eye` |
| ball and socket | 9 of 10 | `socket connect to robot`, already recorded; four variables missing |

**`second eye` is new.** It is a mirror, and its `fullFeaturePattern` is off in draft9p3 and on in
the reference. The reference mirrors the feature; draft9p3 mirrors the faces it made. Both put an
eye on the other side of the head, which is why no shape measurement caught it.

**A second entity is normal on this geometry, and the reference has one where I do not.**
`stud connect to robot` carries one in both documents. `socket connect to robot` carries one in the
reference and none in mine, and mine infers `CENTROID` where the reference infers `CENTER`. So the
head's `head mate`, with `CENTER` and no second entity, is the exception in its own document rather
than the rule.

`CENTROID` is not a third way out of [the socket's
rim](#the-rim-of-the-socket-comes-along-with-the-ball). On a whole sphere it names the middle, but
the socket's ball is cut by its opening, and the centroid of what is left is on the axis part way
toward the far side. It would trade 0.8 mm across the plane of symmetry for an error in height,
which is worse: the height is what tutorial 7 measures. The two ways out written there are the two
there are.

## /features is spent until Sunday lunchtime

Reading `/features` on the foot tab ran the endpoint's budget out on 29 August. It answers again
at about 12:39 on Sunday 30 August, and nothing done before then shortens it.

That takes `built`, `like_reference` and the sketch comparison in `t8j.py` off the table for the
rest of tutorial 8. What is left still proves the work:

- `bodydetails` answers, and it carries every face's surface, radius, axis and area. A slot in the
  sole shows up as a floor plane `#rib_d` above the bottom face, so where a cut landed is readable
  without the feature record.
- The GUI is not limited at all. The feature tree's names, a dialog's fields and a dialog's
  checkboxes can all be read off the page.
- Which way a fresh Extrude dialog points is read by building a throwaway as a **new part** and
  seeing where the slab lands in z. A new part never fails on a wrong direction, so the throwaway
  always answers, where a Remove that misses the foot would not.

Two sketches have been held against 9p1p1 entity by entity and constraint by constraint before the
limit came down: `foot outline` and `groove profile`. Both agree exactly. The comparison is over a
line's two ends rather than the point it records on itself, because two sketches can hold the same
line and record different points along it.

## A throwaway only reads the dialog it is built the same way as

The two flip arrows in the Extrude dialog carry no state a script can read, so which of them is
already lit is read by building a throwaway and looking at where the material landed. That works,
and it is how the pedestal and the foot went in.

It does not work across a change of operation. The sole's slot was read off a throwaway built as a
**New** extrude and then those same two pixel positions were clicked in a **Remove** dialog. A
Remove dialog is not laid out like a New one, one of the two clicks landed somewhere harmless, and
the slot came out hanging inside the foot: its walls ran from z = -20 to z = -22 and the sole below
it was still whole. The pattern then repeated that eight times.

**The check that passed said less than it looked like it said.** It asked whether a floor plane sat
at z = -22, and one did — the bottom of a slot in the wrong place is at the same height as the top
of a slot in the right one. What caught it was holding the finished part against 9p1p1 face by
face: 9p1p1's sole is nine strips with eight slots between them, and this one was a single face of
3569.8 mm².

Two things follow, and both are now done here:

- A throwaway is built the same way the step builds it, Remove and all, and the click list is
  tried against the shape rather than reasoned about.
- A shape check names something that only the right answer has. A wall that runs down to the sole
  at z = -24 is that; a floor at z = -22 is not.

## 9p1p1 calls the part `Foot`, and the brief has no step that renames it

draft9p3's foot tab ends with a part called `Part 1`. The brief's step table goes straight from
`cad.parts.foot.combine` to `cad.parts.foot.connector`, so nothing in it renames the part, and the
assembly tutorials insert parts by name.

Renaming a part is not a feature and never appears in the feature tree, which is why it can go
missing from a table built by reading one. The step is `cad.parts.foot.rename`, and the brief now
carries the row.

The same brief asked for "the transform's two connectors, medium and close-up with a ring". There
is no transform: the pedestal is drawn around the origin so that Base origin lands the socket on
it, and nothing moves afterwards. That row is now the sole before and after the pattern, which is
the failure the tutorial actually has.

## The foot's shape half of `audit.part`: the pedestal is 0.98 mm off the origin

Held against 9p1p1 face by face, off `bodydetails`, draft9p3's foot has 63 faces and 9p1p1's has
60, and 59 of them are the same face in both. Both tabs call the part `Foot`. The reads are
[`log/foot.faces.json`](log/foot.faces.json) and
[`reference/foot.faces.json`](reference/foot.faces.json).

The five that are left over are all at one place, where the pedestal's wall meets the derived
socket's collar. Both are cylinders of radius 9:

| | 9p1p1 | draft9p3 |
| --- | ----- | -------- |
| faces of radius 9 | one, area 757.0 mm² | two, areas 587.3 and 169.6 mm² |
| where their axes run | both through x = 0, y = 0 | the socket's through y = 0, the pedestal's through y = 0.98 |
| flats at z = -9 | none | two, area 17.6 mm² each |

**The pedestal is drawn 0.98 mm along +y from the origin.** The socket derives onto the origin, so
it sits off center on its seat, which is what shows on the screen. The two flats at z = -9 are the
crescents left standing on either side, and their size says the same thing a second way: two
circles of radius 9 pushed 0.98 mm apart leave 2 * 9 * 0.98 = 17.6 mm² standing on each side.

9p1p1's `pedestal outline` holds two constraints, a COINCIDENT tying the circle's center to the
origin and a DIAMETER of `2 * #collar_r`. draft9p3's circle was placed by clicking the pixel the
origin projects to, and that pixel was about 12 px out at 12 px per mm. Nothing pulled the center
back afterwards, because the coincident constraint is the thing that would have.

The first reading of this residue, written here and now withdrawn, was that the foot is the same
shape and that 9p1p1's union merged two coincident cylinders which this build left as two. The
areas do add up, which is what made the wrong reading comfortable. Two cylinders 0.98 mm apart are
not coincident, and the number was sitting in the record.

## A face count is not a verdict

The audit that missed this printed a residue and left the judgment to prose. Three things were
wrong with it, and all three are now answered in `tools/`:

- It compared faces as an unordered set, so a part built 1 mm out of place agrees on 59 faces of 60
  and reads as almost right. [`diff_shape.py`](../../../../tools/diff_shape.py) follows every
  unmatched face up: it finds the nearest face of the same kind and size in the reference and says
  how far it had to look. A face a fraction of a millimeter from its counterpart is a sketch placed
  by clicking rather than by constraint, and the tool now says so in that many words.
- It compared a cylinder by the origin the read happened to carry. A cylinder's origin is any point
  on its axis, so one cylinder read twice can come back with different origins and opposite axes.
  The comparison is the axis line: the direction with its sign settled, and the foot of the
  perpendicular from the world origin.
- It compared floats as they were read. The head's four cones differ in the thirteenth decimal of
  their half angle and are the same cone; that alone reported three differences that were not there.

[`read_shape.py`](../../../../tools/read_shape.py) is the read, in millimeters, and it keeps
working while `/features` is rate limited because `bodydetails` is a different endpoint family.

## Three tabs of four are the same shape as 9p1p1's, face for face

| Tab | Faces, mine and the reference's | Verdict |
| --- | ------------------------------- | ------- |
| body | 20 and 20 | the same shape, face for face |
| head | 47 and 47 | the same shape, face for face |
| ball and socket | 22 and 22 | the same shape, face for face |
| foot | 63 and 60 | the pedestal is 0.98 mm off the origin |

Each read is in `reference/<tab>.faces.json` for 9p1p1 and `log/<tab>.faces.json` for draft9p3.
This says nothing about how any of them was built. That is the construction half, and it waits.

## The sketch geometry route answers, and it finds a second thing

`/api/partstudios/.../sketches?includeGeometry=true` answers while `/features` is refused, and it
carries where every line, arc and circle in a tab actually landed. That is the half of a sketch
audit this run needed all along and did not run:
[`diff_geometry.py`](../../../../tools/diff_geometry.py) pairs each entity with the reference
entity nearest it and prints how far apart they are, so a point placed by clicking is a distance
with a name on it.

| Tab | Sketches | Verdict |
| --- | -------- | ------- |
| body | 6 and 6 | `torso shoulder profile` is missing a line the reference has |
| head | 3 and 3 | every sketch landed where the reference's did |
| ball and socket | 3 and 3 | every sketch landed where the reference's did |
| foot | 3 and 3 | `pedestal outline` is 0.98 mm out |

**9p1p1's `torso shoulder profile` holds five lines and draft9p3's holds four.** The line that is
missing runs from (-31.1769, 48) to (-31.1769, 40) in the sketch's own frame. Read out of
`reference/body.features.json`, it is construction, and it is a projected edge: the sketch carries
three PROJECTED constraints naming it, a MIDPOINT tying the rectangle to it, and an ANGLE of
`90 deg - #tilt` measured from it. So 9p1p1 pulled an edge that was already there into the sketch
and stood the shoulder on it, and draft9p3 put the same rectangle in the same place by other
means.

The two solids are the same, face for face. The difference is in why the shape is that shape,
which is the thing `audit.part` exists to catch and the thing `req.model.visible_geometry` asks
for. It belongs with tutorial 6's recorded deviation over its five sketches rather than beside it.

The construction half of the audit cannot run: `tools/diff_features.py`, `tools/diff_sketches.py`
and `tools/diff_construction.py` all read `/features`, which does not answer until Sunday. The
union's own parameters were never read back either, so whether `combine parts` went in the way
9p1p1's did is exactly what is still owed. That is task #122.

## The pedestal is back on the origin, and the foot now matches face for face

`pedestal outline` was opened, the circle's center and the origin were picked, and Coincident was
applied. The sketch route says the circle now sits at (0, 0) with radius 9, and both halves of the
audit that can run agree with 9p1p1:

- 60 faces and 60 faces, and every one of them is the same face in both.
- all three sketches land where the reference's do.

**The picks were made where the camera says those two points are drawn, and that is the thing that
was wrong the first time.** At 39.91 px per mm the circle's center projected to (922, 524) and the
origin to (922, 563), 39 px apart, which is the 0.98 mm. So the projection is right when it is read
after the zoom has settled. `zoom_to` says in its own docstring that a freshly opened sketch puts
the origin at the middle of the canvas, and here the middle of the canvas held the circle's center
instead. A step that computes a pixel from the camera has to check that the pick landed on the
thing it aimed at, and the sketch route is how that is checked now.

**Five frames of `cad.parts.foot.pedestal_sketch` are of the sketch as it was.** They show the
circle placed 0.98 mm off and the sketch under-defined, and one of their captions calls it fully
defined. The model is right and the pictures are not, so the step has to be driven again before its
page is written.

**The Onshape version named `tutorial 8 - the foot` was published before this fix** and holds the
foot with the pedestal off center. The workspace is what tutorial 9 builds on, so the fix is
carried forward and will be inside the next version published.

## The first sketch on Front drew every point at the middle of the window

`blade profile` is the run's first sketch on a plane that is not Top. Three attempts drew all four
entities on top of each other in the middle of the canvas, because the step handed the sketch's y
to `gui.project` as the world's y, and Front's normal *is* the world's y, so every point was aimed
along the line of sight.

[`onshape-gui-howto.md`](../../../onshape-gui-howto.md) § *4. Selecting things* already says a
sketch point `(x, y)` on Front is the world point `(x, 0, y)`. The foot's three sketches are on
Top, where a sketch's two axes are the world's x and y and the swap is the identity, so eight
tutorials went by without the rule ever being exercised.

## Normal to gives the far side first

Pressing `n` on Front puts the camera behind the plane, looking back through it. Every pick and
every dimension still lands, because the projection is told where the camera is. The picture is
what suffers: the part is a mirror of itself, the view cube reads *Back*, and the sketch's name in
the corner of the window reads backwards.

A second `n` turns the camera to the other side. Which side the first press lands on is worth
measuring rather than remembering: project 1 mm along x and -1 mm along x, and if the first comes
back to the left of the second the camera is behind the plane.

## The bottom of the window is the tab bar

A pick worked out from the camera can land below the graphics area. The tab strip is at y = 983 and
the status strip at y = 966, so a click at y = 995 goes to a tab and leaves the part the step is
building. A step that aims at a point some distance below the origin has to check the pixel is on
the canvas before it clicks, and aim somewhere else when it is not.

## Tutorial 9's first sketch cost eight attempts, and each one was a different thing

`blade profile` is four entities and it took eight passes. None of them was the same mistake twice,
and all five findings are now in [`onshape-gui-howto.md`](../../../onshape-gui-howto.md):

- The sketch's y was handed to the projection as the world's y, so every point drew at the middle
  of the window.
- `n` faced the camera at the back of the plane, which mirrors the picture without moving anything.
- A pick worked out below the tail landed on the tab bar, because the tail was near the bottom of
  the window.
- The next one landed on the tail's own horizontal marker, which is drawn just under it and is
  pickable, and Mirror accepted the tail as a mirror line without complaint.
- The tool named *Mirror* draws a copy. The constraint that holds two entities either side of a
  line is *Symmetric*, and `MIRROR` is what the feature data calls Symmetric.

**Only the last of the five was visible in a picture.** The other four all produced a blade that
looked right: the two that mirrored the view or moved a pick left the shape unchanged, and the two
that took the wrong line left it 0.03 mm and 0.002 mm off center, which is nothing to look at. The
step passed its own eye and failed the sketch route every time, which is the argument for the check
that this run added.

## Eight tutorials of takes stand and not one page is written

Phase W says a page is written *"immediately after its `audit.part` passes."* Eight have passed and
the guide has had one commit, the inherit. Every `.rst` under
[`instructions/stickbot-draft9p3/source/`](../../../../instructions/stickbot-draft9p3/source/) is
still draft9p2's text pointing at draft9p2's frame names, so the 520 unreadable images the plan
uses as the measure of work left have not moved.

**The takes were run back to back because the tick that drives this run reads Phase T and Phase W as
two blocks in sequence.** The plan does not say that. It interleaves them, and it interleaves them
for a reason the batching threw away: `audit.block` and `audit.page` findings are meant to reach the
next tutorial's take. Four findings are already sitting unhonored for exactly that reason, two
captions from tutorial 2 and two shots from tutorial 5, and every one of them is a retake that has
to be driven again rather than a sentence that could have been written differently.

**The recovery is to write the eight owed pages before taking a ninth tutorial**, and then to hold
the interleave for tutorials 9 to 14. Tutorial 9's take stops where it is, six features into the
hinge tab, with the studio consistent and nothing half-applied.

## Tutorial 1's capture saved one picture under three names, and captioned two of them wrongly

Writing the torso page found six duplicate frames in a capture that `audit.step` and `audit.part`
had both passed. `tools/page_sweeps.py`'s `blockcheck` names them in a second; nothing before it
looked.

- `hero-01`, `tree-01` and `version-03` are one file. It shows the finished torso from a corner
  with the planes hidden and the feature tree beside it, so the hero caption and the tree caption
  are both true of it. **`version-03`'s caption is false**: it claims the Versions and history
  panel listing `tutorial 1 - variables and torso` above `Start`, and there is no panel in the
  picture. The version step therefore has no frame of its own result.
- `document.units-03` and `-04` are one file, and it shows **Millimeter** with `0.12345` already
  set. **`-03`'s caption is false**: it claims the dialog as it arrives, on Inch with `0.123`.
  There is no frame of the dialog before it was changed.
- `document.units-01` and `-05` are one file. Both captions are true, because a unit change is not
  visible, so the frame after the dialog closes is the same pixels as the frame before it opened.
- `parts.body.block-05` and `-06` are one file, and both captions are true of it.
- `variables.sizes-01` and `variables.studio-02` are one file, and both captions are true of it.

**The page was written around what the frames actually show.** Twenty-six of the thirty-two are
used, every figure resolves, and no caption on the page says anything the picture does not. The
tree section points back at the picture at the top rather than publishing it again, and the two
steps whose evidence is missing say what to look for in words.

**Two of the six can be retaken and two cannot.** The versions panel and the tree are there to be
photographed at any time. The Workspace units dialog on arrival cannot be, because the workspace is
in millimeters now and there is no going back to catch it; the same is true of the empty document
before the units were set. Those two wait for a document built from empty again.

**What the take should do differently:** hash a frame as it is written and refuse a second name for
the same bytes. A step that shoots the same pixels twice has not shot what its caption says, and
the take knows both the bytes and the caption at the moment it writes them.

## The last frames of a tab are the same picture three times, on every tab that has them

Tutorial 1 was not a one-off. On the head tab, `hero-02`, `tree-01` and `version-02` are one file,
and it shows the head straight on in the `head` tab. **`version-02`'s caption is false** in exactly
the way tutorial 1's was: it claims the Versions and history panel listing `tutorial 2 - the head`
at the top, and there is no panel in the picture. `parts.head.body-06` and
`parts.head.upper_rounds-01` are also one file, and both of their captions are true of it.

Counted across the eight tabs that have been captured, by hashing every frame:

- `torso` 32 frames, 5 repeated images
- `assembly`, `foot`, `head`, `mate-head` 2 each
- `ball-and-socket`, `hinge` 1 each
- `head-socket` and `torso-joints` none

**The pattern is the tail of a tab.** `cad.hero`, `cad.tree` and `cad.version` all end with a frame
of the model, because the take shoots the window and the version panel is never opened before the
shot is taken. So every page loses its picture of the versions list, and gets the same hero three
times instead.

**Both written pages spend the picture once** and say the rest in words. The tree section points
back at the hero, which carries the feature list down its left side and is a true picture of it,
and the version section describes the list instead of showing it.

## Two of tutorial 2's steps carried a deviation that is a wrong check, not a wrong model

- `lower head chamfer` recorded *"take failed: 12 faces became 20"*. Twenty is right: the chamfer
  bevels the bottom face's eight edges and the rounded corners with them. The next step reads 22
  faces before the eye and the tab finishes at 29, which is what 9p1p1 has.
- `second eye` recorded *"the mirror added 301.669 of 301.593"*, a difference of 0.076 mm³ on a
  300 mm³ eye. The eye is an extrude that starts inside the head and stops 3 mm past its face, and
  the mirrored copy meets the far side of a head whose top is rounded, so the two solids are not
  quite congruent. This is the same `second eye` line `audit.part` reports, where the reference has
  `fullFeaturePattern` true and draft9p3 has it false. **It stays open**; the page does not depend
  on it.

## Tutorial 4 saved the variable table twice and captioned one of them for a state it never held

`parts.ball_and_socket.variables-02.png` and `section.wide-04.png` are the same bytes. The picture
is the `robot sizes` table with all ten rows in it, `fit` at 0.08 mm and `grip` at 1.94648 mm, and
the `grip` cell focused.

- `section.wide-04`'s caption — *the fit row back at 0.08 mm* — is true of that picture.
- `variables-02`'s caption — *the grip row, its Value box holding the square root that solves for
  the snap* — is false. The Value column shows what the expression evaluates to, not the
  expression, so no frame in this tab shows the square root being typed. The take believed it was
  shooting a field mid-entry and it was shooting a committed table.

`parts.ball_and_socket.variables-03.png` is the same table again with nothing focused, so tutorial
4 has three names for two pictures of one state.

**The page spends it once.** `variables-03` carries the ten rows in the variables step,
`section.wide-04` carries the restored `fit` at the end, and `variables-02` goes unused. The square
root is written out in the page's own table and explained in an advice block, which is the better
place for it: a screenshot of an evaluated number could never have taught it.

**One more caption is loose.** `parts.ball_and_socket.tab-03`'s `shows` reads *the tab strip ending
in the new tab, ball and socket*, and the new tab is fourth of five; `robot sizes` is behind it.
The page's alt says where it really sits, so `altdiff` reports the difference. This is the same
class as the two above: the take writes the caption from what it meant to do, and the frame records
what the screen did.

## Tutorial 5's page is written around the two things that are Mike's to decide

`head-socket.rst` is written from this run's 42 frames, and it uses all 42. Two of its steps had to
be written carefully rather than freely, and both are waiting on a decision recorded above.

**`head mate` does not claim to land on the sphere's center.** The inherited page said *A connector
picked on a spherical face lands on the sphere's center, so this one is at the middle of the hollow
without a number being typed*. In this build it does not: the rim edge comes along in
`secondaryOriginQuery` and the connector sits 0.8 mm off, which is [The rim of the socket comes
along with the ball](#the-rim-of-the-socket-comes-along-with-the-ball). The page now says where to
click and what the dialog reads back, and says the arrows stand *at the ball the neck stud sits in*
without asserting the exact point. **If Mike takes the deviation the page needs a sentence saying
the joint is 0.8 mm off the plane of symmetry; if he moves the connector's origin the step is
rewritten.** Either way it is a page change, not a model rebuild.

**`drop socket to neck` names no angle.** The feature holds 30 degrees where the reference holds
180, and the angle is measured from whichever connector was picked, so a typed number would only be
right for a reader who picked what this build picked. The page names both connectors and says to
click the flip button, which is what the take did and what the frames show. Nothing in the reader's
path depends on the stored angle.

**`page_sweeps.py` learned the arrow keys.** `cad.hero` recorded `ArrowUp`, and `keycheck` looks
for a key in the form the page has to write it in. `**arrowup**` is not a form a page for
middle-schoolers can use, so `KEY_FORMS` now accepts `**up arrow**` for it and the same for the
other three.

## Tutorial 6's page is written from what was built, and one frame's caption had to be replaced

`torso-joints.rst` is written from this run's 152 frames and uses all 152. It is the guide's
longest page and it carried the guide's worst warning count, 36; it now builds with none.

**`parts.body.shoulders.profile_sketch-04`'s caption is false.** The log's `shows` reads *the pivot
line now drawn into this sketch as well, which is what Use does*, and [A sketch will dimension to
model geometry without projecting it, and say
nothing](#a-sketch-will-dimension-to-model-geometry-without-projecting-it-and-say-nothing) proves
Use was never run. The picture is real; it shows the new sketch with the pivot line visible in it,
which is what model geometry looks like from inside a sketch. The page's alt says that, and the
sentence above it says the sketch can dimension to the line without owning it. `altdiff` reports the
difference, and it should.

**The page teaches the construction that was built, not the reference's.** That is the choice [The
block for tutorial 6's construction](#the-block-for-tutorial-6s-construction) puts to Mike, and it
stays open. If he rules *rebuild to the reference*, this page's `torso shoulder profile` step gains
a Use step and its twelve frames are retaken, `shoulder`'s revolve picks a sketch region instead of
a face, and four smaller sketches change what they constrain to. Nothing else on the page moves: the
numbers, the plane, the mirror, the trim, the studs and the five connectors are all the reference's
already.

**Two names on the page are Onshape's, not English.** `left shoulder connector` sits beside
`r shoulder connector`, `l hip connector` and `r hip connector`. The page uses the built names,
because a reader hunting the assembly's connector list has to find what is really there. Whether a
later draft normalizes them is still for Mike.

**No frame in this tab is a duplicate of another.** 152 files, 152 distinct pictures.

## Tutorial 7's take has no hero step, and its tail frames repeat

`mate-head.rst` is written from this run's 19 frames and publishes 17 of them.

**Two pairs are the same bytes.** `assembly.fix_body-03` and `assembly.mate_head-01` are one
picture of the tree, and both of their captions are true of it: the pin is on `torso <1>` and both
instances are open with their connectors showing. The page spends it once, in the fix step, and then
tells the reader to read the same picture again for the rows the mate picks from.
`assembly.drag_head-01` and `assembly.drag_head-05` are the head at rest before and after the drag.
They are the same picture because it is the same state, which is the step's whole point; the page
publishes one and says in words that the head comes back to it.

**The take recorded no `cad.hero` step for this tutorial.** Every other tutorial's page opens with
one. This page opens on prose and its first picture is the assembly tree, which reads flat next to
its neighbors. The take should shoot a hero for an assembly page the way it does for a part page.

**The page does not say the head rests off center.** The take measured it at `[0.0, 0.8, 103.0]`,
and the 0.8 mm is [The rim of the socket comes along with the
ball](#the-rim-of-the-socket-comes-along-with-the-ball), made on page 5 and only visible here. The
page states the height, which is measured and is the number the chain explains, and claims nothing
about the middle. If Mike takes the deviation the page gains a sentence naming the 0.8 mm; if he
moves `head mate`'s origin the page is already right.

**`ninja draft9p3` no longer warns on any page tutorials 1 to 7 wrote.** What is left is
`legs`, `hinge`, `foot`, `arms`, `lower-limb`, `upper-limb`, `gripper` and `plan`, all inherited and
all still to be written or reviewed.

## Tutorial 8's pedestal frames were retaken, and two of the five were carried forward

The pedestal circle was drawn 0.98 mm off the origin and fixed with one Coincident constraint. The
frames of `cad.parts.foot.pedestal_sketch` were not retaken at the time, and three of the five then
said things the fixed sketch does not show: `-03` called the circle centered on the origin, `-04`
was the moment the width was typed over an off-center circle, and `-05` called the sketch black and
fully defined over a blue one.

Attempt 7 retook those three. The circle was not touched, because every feature after it in the tab
queries it and the tab matches the reference face for face; only the diameter dimension was deleted
and typed again. `tools/read_sketches.py` before and after says every sketch in the tab is
identical, down to the circle's entity id.

`-01` and `-02` are the plane pick and the empty sketch, which the fix did not touch. They are
attempt 6's, copied into attempt 7 so the verdict promotes a whole step, and the step's own record
says which frames came from where.

The three retaken frames are cropped to the graphics area. The feature list beside it now holds all
28 rows of a finished foot, and a reader on this step has 15; a picture of the wrong tree would
have traded one untrue frame for another.

Two things the take could not do on its own:

- A pick on a sketch dimension reads dead for several seconds after a zoom. The same pixel answered
  nothing nine ways running, and answered first time once a slow DOM walk had gone between the zoom
  and the click. `gui.still` and a four second wait is what makes it repeatable.
- `Take.verdict` copies one attempt's directory and nothing else, so a step whose frames come from
  two attempts has to have them put in one directory by hand before the verdict runs.

## `mate to robot` never resolved, and one pick is what builds it

Tutorial 8's connector went in with every box empty and has read *"[Mate connector] did not regenerate
properly: Cannot resolve entities"* since the day it was made. Its own accepted frame shows the row
red and no arrows on the model, so the frame was untrue as well as the feature.

The cause is a pick that does nothing. The take clicked `Foot` in the parts list with **Origin
entity** armed. A parts-list click does not reach that field: the dialog's text is byte-identical
before and after it, and the take had no assertion that would notice.

What builds the connector is the tree's `Origin` row. That one pick fills **Origin entity** with
`Vertex of Origin`, and Onshape then fills **Owner entity** with `Foot` and puts **Attachment** on
`To owner` by itself. Setting **Attachment** to `To selection` opens an **Attach to** field, and
`Foot` clicked in the parts list fills that. The result matches 9p1p1's connector: an owner part, an
attach-to part, and `TO_SELECTION`.

Two facts about query fields came out of it, and both belong in the harness:

- A parts-list click fills **Owner entity** and **Attach to**, and does nothing to **Origin
  entity**. The guide already says the first half in `mate-head.rst`; the second half is new.
- `gui.pick` calls a part picked into a query field empty. The probe counts lit pixels and a part
  picked that way lights none, so `pick` raises where the click worked. The clicks in `t8conn.py`
  are raw, and the dialog's own text is what is asserted.

The step was driven again from the front after the old feature was deleted, so all six frames are of
the connector that stands now. `cad.hero` and `cad.tree` were retaken with it, because `hero-01`,
`hero-02` and `tree-01` all had `mate to robot` in red.

`Step.__exit__` skips its feature-error check whenever `deviate()` was called, which is how a broken
feature passed in the first place. That is a harness fix still owed.

## The `tutorial 8 - the foot` version holds a foot that no longer exists, and cannot be deleted

The version was cut before the connector was repaired, so what it holds is a foot whose `mate to
robot` is red. The Versions panel's own menu on that row offers `Open`, `Compare`, `Copy link`,
`Properties…`, `Restore to Main…`, `Branch to create workspace…`, `Publish FeatureScript…` and
`View in repair`. There is no `Delete`, so the stale milestone stays.

Nothing builds from it. The assembly pages insert from the workspace, and a version is a milestone
the reader cuts at the end of a page rather than an input any later page reads. A reader following
`foot.rst` from the front cuts their own version at the end and it holds the foot the page built.

The three `cad.version` frames are still true: they are frames of the act of cutting the version,
and the act did not change. What is stale is the content behind the name in this one account.

## Two frames of the foot take are the same bytes as the frame before them

`parts.foot.pedestal-01` and `-02` are identical, and so are `parts.foot.ribs-05` and `-06`. The
Extrude dialog opens on **Solid** and **New** already, so a frame captioned "set to New" shows
nothing the frame before it did not; **Reapply features** arrives ticked on Linear pattern, so the
same holds there. `foot.rst` publishes the first of each pair and says the fact in the sentence
instead. `blockcheck` reports the two as unused, which is the correct reading.

The harness fix is to hash a frame as it is written and refuse a second name for the same bytes.

## One pick fills a Mate connector, and a second pick empties it again

Tutorial 9's `axis for circular patterns` stands on the stub axle's round end. Clicking that face
with `Origin entity` armed fills four things at once: `Origin entity` reads `Face of stub axle`,
`Owner entity` reads the part the face belongs to, `Attachment` moves off `None` onto `To
selection`, and `Attach to` reads the same face. Nothing else has to be set.

Clicking the face a second time, to put it into `Attach to` by hand, takes it back out: the pick
count went `688 -> 0` and `Attach to` came back empty. That is the same defect tutorial 8's `mate
to robot` went in with, in the opposite direction; there the extra click emptied `Owner entity`.

A canvas click needs a hover in front of it. `page.mouse.click` on its own picks whatever the
pointer was last over, which on a fresh page is nothing, and the dialog does not change. `gui.pick`
moves first, which is why it works where a raw click does not.

## The hinge's two connectors cannot be checked against 9p1p1 until Sunday

`/features` on the hinge tab is spent until about 12:39 on Sun 30 Aug, so `entityInferenceType` on
`axis for circular patterns` is unread. What the connector does is checked instead: the 24 teeth it
patterns land at one height, on one circle, 15 degrees apart, which a wrong axis does not give.
`CENTER` and `CENTROID` are the same point on a circle, so the geometry cannot tell them apart
either. The construction half of `audit.part` is where this gets settled.

## The reference's own parameters were on disk the whole time

`reference/hinge.features.json` holds all 49 of 9p1p1's hinge features with every parameter
spelled out, captured in Phase P0 before the rate limit. The fork was being built by reading
geometry and guessing which region a feature took; the file says outright. It settled three
things the geometry could not:

- `fork blank` extrudes **one** region and `two forks` mirrors the body it makes, so the blank is a
  single ear `#ear` thick and not a bar across the slot. Two runs went in as a bar before the file
  was opened.
- `trim fork to arm`, `pocket axle on fork` and `ear valley` all carry an explicit `booleanScope` of
  the fork body, with `defaultScope` off. A cut left on merge-with-all takes the blade with it.
- `fork arm` starts at `#slot_deep - #nose` with no flip on either the depth or the offset.

The rate limit is on reading **draft9p3's** features, not the reference's. `audit.part`'s
construction half still waits for it.

## A sketch dimension moves the whole shape, not the one side it names

`fork blade top cut outline` is a box round a circle, and the box's four sides are dimensioned one
after another. Holding the left side 2 mm off the circle slid **all four** sides 4 mm to the right:
the right side went from the +18 mm it was drawn at to +22 mm, which at 10.98 px/mm is 44 px away
from where the pick was aimed. Any pick that assumes where a line was drawn is wrong from the
second dimension onward. The cure is to look for the line over rings out past the distance the
last dimension could have moved it.

## Inside the box, a click takes the region

The same step spent ten runs picking the same 4273 px at every offset it tried. That is not the
box's side; it is the **region** between the box and the circle, and the status strip reads
`Area: 554.71979 mm²` when it is lit. The prices are far enough apart to tell them by count alone:
a side about 1500 px, the Ø24 circle about 3700, the horizontal axis about 3890, the region about
4270, the origin between 4 and 19. `pick_near`'s `most=` cap is what does the work; at 2500 the
search walks past the region and lands on the side.

## The horizontal axis answers no pick where it is clear of everything

Out at 26 mm along it, where nothing else is drawn, the axis lit nothing at all at any of the
sixteen offsets tried. The fourth side is measured to the **origin** instead, which is the same
perpendicular distance and the same intent: 5.6 mm above the middle. The origin is the smallest
thing in the sketch, so its pick is capped at 400, below what the axis or the region costs.

## Never pick a sketch line where an axis crosses it

The long-running "24 mm" failure on this sketch was not the model behind the sketch and not the
circle. The side picks sat at y = 0, exactly where the horizontal axis crosses them, and the axis
runs the full width of the screen under the same pixel. What came back was the circle measured
against the axis. Every pick in the step now sits well off both axes.

## The agent browser's session dies when Onshape signs the other browser out

Symptom: `gui.tree(page)` returns `[]` and `page.url` is `https://cad.onshape.com/signin`.
`tools/agent_browser.py --status` says "up; not signed in", and a restart says the borrowed cookies
carry no session. The cure is `uv run --project . python -u tools/browser.py --signin`, which types
the email from git config and lets Chrome fill the password, then a restart of `agent_browser.py`.

## An end condition is not a `select`, so `dlg_select` can never find it

The Extrude dialog carries no `select` element at all: a probe that listed every one of them
printed nothing, armed and again with Remove chosen. `dlg_select` looks for a `select` whose
options carry the wanted word, so it raised "no dropdown in the dialog offers 'Through all'" while
the control sat there reading `Blind`. The list only exists once the control is clicked and it is
drawn outside the dialog. `t6lib.dlg_drop(page, showing, want)` clicks the control by the word it
is reading now, picks the entry out of the list, and reads the dialog back.

## Turning Merge with all off fills the scope with the wrong part

An Extrude set to Remove arrives with `Merge scope` already holding `Part 1`, the blade, because
the blade is what the cut runs through. Clicking the ear adds it to a box that still names the
blade, and the cut takes the blade with it. The blade goes out by the x on its own row, which is
`dlg_drop_entry`, before the ear goes in. The step now reads the scope back and refuses to commit
if the blade is still in it. `trim fork to arm`, `pocket axle on fork` and `ear valley` all carry
this.

## `read_shape` hands over millimeters, so a radius must not be scaled again

Two step checks multiplied `surface["radius"]` by a thousand and then compared it against 12 and
against 2.2. Nothing ever matched, and `trim fork to arm` was reported as having cut nothing when
the fork had come out exactly right. The boundingboxes route is the one that answers in meters;
`read_shape.faces` has already converted. A check that reads a radius compares it as it comes.

## A part check must name the part it is checking

`round_ends` looked across the whole tab for a `#nose` cylinder about the joint's axis. The blade's
own nose is one, so the check would have passed whether the ear was cut or not. `read_shape.faces`
carries each face's `body`, and `/api/parts` gives the body id a name, so the search is held to the
one part the step is about.

## The fork's bounding box does not change when its end is rounded off

The trim takes the corners off the ear at negative z, and the ear still reaches z = -12 at x = 0,
still reaches x = 10.613 at z = 0, and still spans y 5.6 to 12. Every number in the box is where it
was. The circle's edge is where the cut shows: the fork body goes from two faces to four, and one
of the new ones is a `#nose` cylinder about the joint's own axis.

## A vertical hold swings a point round the origin rather than sliding it sideways

`ear valley outline` draws its circle at (4, 7) and then holds the center straight above the
origin. A hold that only names an x has one obvious answer, which is to move the center to (0, 7),
and that is not the answer the solver picks. It swings the center round the origin instead,
keeping the 8.06 mm it was drawn at, and the center arrives at (0, 8.06). The step aimed its next
pick at (0, 7), found nothing there, and took the ear's face behind the sketch every time.

The height of the swung center is the distance the circle was drawn at, so the next pick is aimed
at `hypot(*DRAWN_AT)` up rather than at the height it was drawn. The same reasoning applies to any
hold that leaves a point one number short: work out where the solver puts it, and do not assume it
takes the shortest road.

## A cut that meets nothing is not an error, and the dialog is the only thing that says so

`ear valley` took four attempts because a Remove scoped to one part, aimed where that part is
not, is accepted without complaint. The feature lands in the tree, the tree shows no error mark,
`gui_steps.errors` finds nothing, and the ear comes out whole. Three settings of the two arrows
put the cut somewhere the ear is not, and all three were taken.

The dialog does say so, in a line above the model: **Selected tools and targets do not intersect.**
Reading that line while the dialog is still open is the check, and `ear valley` now refuses to
commit when the line is showing. Any scoped Remove wants the same guard.

Which arrow does what is worth writing down as well, because it is not what the names suggest.
The arrow beside the end condition turns the whole cut over, offset and all; the arrow beside the
starting offset turns only the offset. For a sketch on Front cutting an ear that lies between
y = 5.6 and y = 12, the settings that work are the end condition's arrow left alone and the
offset's arrow clicked once. The other three all miss.

## The fork's ear is a segment of the limb, not a slab

The ear is the piece left when a Ø24 rod along z is cut by the plane y = 5.6: its outer face is a
cylinder of radius 12 about the z axis, its inner face is that plane, and it runs from z = -12 to
z = 21. Four faces before anything is cut into it. That is why the valley's floor is a flat disc
normal to y at y = 6.5, and why a check for one is a check that the cut happened at all.

## A long feature list draws neither end when you want the middle

`list_top` scrolls the feature list to its head and `list_end` scrolls it to its foot, and
between them they reached every row until the hinge tab passed fifty rows. Onshape draws
only the rows near the scroll position, and `axis for circular patterns` sits in the
middle: from the head it is below the panel, from the foot it is above it, and in neither
place is it in the page at all. `gui.row` waited thirty seconds for a row that was never
going to be drawn and the step died with the pattern dialog open.

`list_find` is the third helper. It walks the scroll from head to foot in eighths and stops
at the first place the wanted row is drawn. Every pattern from here on picks its axis with
it, because every tab gets longer as it is built and the axis stays where it was made.

## Two of the twenty-four valleys run off the ear's edge, in 9p1p1 as well

The check on `24 ear valleys` counted flat discs `#valley_d` across on the ring and found
twenty-two. The two it missed are at 90 and 270 degrees, where the ring is widest across
the ear. The ear is a slice of the `#limbD` limb rather than a full disc, so it runs out of
material at x = 10.613; a valley centred 9.6 out has its rim at 10.6, which is over that
edge by thirteen thousandths of a millimetre. Those two valleys come out as part discs of
2.505 square millimetres rather than the full pi.

The reference model has exactly the same two part valleys at exactly the same two angles
and exactly that area, which is what `hinge.faces.json` says. So this is not a defect to
correct; it is what the numbers give, and the check now reads it rather than filtering it
out. It is worth a line in the hinge page: a student who looks closely will see two of the
twenty-four valleys open onto the ear's edge.

## Move is the tick that offsets a mate connector, and a box keeps the words you typed

Nothing before the hinge had moved a mate connector off the face it was built on, and the
dialog does not show anywhere to type an offset until `Move` is ticked. That tick is what
the feature's own record calls `transform`. Ticking it opens four boxes: three that read
`0 mm`, which are how far to slide the connector along its own X, Y and Z reading down the
dialog, and one that reads `0 deg` for turning it about its Z.

The Z box then keeps showing `#nose - (#slot_deep - #nose + #rod)` rather than the -15.4 mm
that comes to. That is what every number box in this repository does, and a check written
against the number rather than the words fails on a step that is right. Read the box to
confirm the expression reached it; prove the number from the geometry.

## The fork's connector does not sit on the end of its rod

The blade's connector stands on the flat end of the blade's arm and stays there. The fork's
is built on the flat end of the fork's arm at z = 27.4 and then slid 15.4 mm back down the
rod, so it ends up at z = 12, which is `#nose`, the far tip of the blade's nose. It is
15.4 mm short of where its own rod ends, and the rod is only 6.4 mm long, so the connector
sits inside the fork's body rather than on it.

This is what 9p1p1 does and the expression is copied from it, so draft9p3 matches the
reference. Tutorial 10 then explains it. The limb's rod is
`#limbCenter - #collar - #limbD / 2`, which is 48 - 9 - 12 = 27 mm, and the fork is landed
on the rod's far end by that connector. The fork's ears are 24 mm deep, so their axis comes
out at 9 + 27 + 12 = 48 mm from the socket's ball center, which is `#limbCenter` exactly.
The 15.4 mm the connector sits back from the arm's end is the length of arm that ends up
buried inside the rod. Nothing here is loose, and this is no longer a question for Mike.

## A spent route must not take a step down with it

`/features` on the hinge tab is rate limited for half a day. The fork's connector built
cleanly, took its six frames and then died on the optional read-back that asks the route
what the feature went in with, so the step lost its verdict and had to be built again.
`built` now answers a refusal the same way it answers a missing feature, with None, which
is what every caller already handles. A read that a step can do without must not be able
to fail the step.

## A dimple that runs off the ear's edge, and the arithmetic that says which two

The ear is a slice off a round bar, not a disc, so it is not the same width all the way through.
Its inside face is at `#slot / 2` from the middle and is `2 * sqrt(#nose ^ 2 - (#slot / 2) ^ 2)`
across, which is 21.23 mm. The dimple floors are `#valley_deep` further in, at 6.5 mm from the
middle, where the same sum gives 20.17 mm.

The ring of dimples is `2 * #bump_r` across and each dimple is `#valley_d` wide, so the ring reaches
21.2 mm across. That is 1.03 mm past the 20.17 mm the ear has at that depth, and the two dimples
sitting at the ring's widest points lose a slice each. A circle of radius 1 cut at 0.487 from its
center keeps `pi - (arccos(0.487) - 0.487 * sqrt(1 - 0.487 ^ 2))` = 2.505 mm², which is exactly what
`bodydetails` reports for both of them, and exactly what `reference/hinge.faces.json` reports for
9p1p1's.

So it is not a mistake in either model, and `t9w.py` asserts the two by angle rather than filtering
them out.

## The two parts are still Part 1 and Part 2

Nothing in the hinge tab renames its parts, in draft9p3 or in 9p1p1. `upper-limb.rst` tells the
reader to derive "the **fork** body only" and `lower-limb.rst` does the same for the blade, and
neither name in the parts list says which is which.

**For Mike.** Either the tab gains two renames, or the two limb pages tell the reader how to tell
Part 1 from Part 2. A rename adds no feature and moves no geometry, so it is the cheaper of the two,
but it is a step 9p1p1 does not have.

## Extrude arrives on New, so a frame of the click has nothing in it

`cad.parts.hinge.blade.blank` took a frame of the dialog and then a frame of the dialog "set to
New". Extrude arrives on **New**, so the two frames are one picture to the byte. Retaking cannot fix
it; there is no second thing to photograph. The page carries one figure and says the dialog arrives
on New.

`gui_steps.Step.shot` now hashes a frame as it writes it and refuses a second name for the same
bytes, so the next one is caught where it happens rather than by `page_sweeps.py` a day later.

It caught the next one the same day, and the catch turned into a finding. See below.

## Extrude flips itself to Add when the region it is given lies on a part

`cad.parts.u_limb.body` framed the dialog, pressed **New**, framed it again, and got the same bytes
twice. Extrude does arrive on New. So the click was dropped as a no-op, the depth was typed, the
feature was accepted, and the rod came out **welded to the socket**: one body from -36 to 1.946
where there should have been two.

What happens is that the dialog arrives on New with nothing picked, and switches itself to **Add**
the moment it is given a region that sits on a face of an existing part. Nothing on the screen says
so except which of the four words is lit, and the merge scope it quietly fills in is the part the
face belongs to.

Tutorial 6 met this on Mirror and Revolve and tutorial 9 met it on Extrude, and `t6lib.choose`
was written for it: it presses the option and reads back that the option took. This step pressed
New before there was anything picked, where `choose` would have been no help either, because at
that moment New was already right.

So the order is what matters. Pick the region first, then set the operation, then read it back
with `choose`. A page that tells a student to press New before picking is telling them to press a
button their next click will undo.

## A ring can be drawn outside the picture it is meant to mark

`cad.parts.u_limb.fork_connector`'s close-up zoomed to 26 px/mm about the canvas center. The
connector it was about sits on the far end of the rod, which at that zoom is at y=1298 in a window
1000 tall. `gui.ring` drew the circle at 1298, off the bottom, and saved a frame whose `shows` says
a connector is circled on it. Nothing complained.

Two changes. `gui.zoom_to` takes `at_px`, so a close-up zooms about the thing it is a close-up of
and that thing stays where it was. And `gui.ring` now refuses to save a frame whose ring falls
outside the image, which is the check that would have caught it either way.

The three hundred rings this run has drawn before it were all inside their frames, so nothing
already published has to be reshot for this.

## Two of the upper limb's three bodies are called `Part 2`

The rod comes out of its extrude as `Part 2`, because the socket already holds the first place in
the parts list. The fork is then derived from the hinge, where it is also called `Part 2`, and it
arrives under that name. The tab reads **Parts (3)**: `Socket body`, `Part 2`, `Part 2`.

Onshape is content with it and so is the union that follows, which is why 9p1p1 has it too and
nothing has ever noticed. What it breaks is anything that reads bodies back by name: the first
`boxes` here was a dictionary, one of the two `Part 2` rows overwrote the other, and the step that
had just derived the fork was told the tab had gained nothing. `boxes` is a list now, and the fork
is told apart by the box it fills.

It also decides how the page has to be written. A student is told to click the fork in the graphics
area, where there is no doubt which body is which, rather than to click a row in a list that says
the same three words twice. Renaming the hinge's two parts would fix this at the source and is
[the open question](#the-two-parts-are-still-part-1-and-part-2) for Mike.

## The hinge was doubled as one block, and four lengths should not have gone with it

Mike asked for a sweep of the hinge from a dozen directions, in both `stickbot-draft9p1p1` and
`stickbot-draft9p3`. The two tabs are the same part: face for face, 153 on the fork and 111 on the
blade, the same bounding boxes and the same radius histograms. Every finding below is a design
finding, not a copying one, and it lands on 9p1p1 as hard as on 9p3.

These findings are written up with drawings, for whoever decides what to change, in
[`.docs/reviews/hinge/`](../../reviews/hinge/source/index.rst) — `ninja hinge`. What is below is
the working record, corrected on 2026-08-30 where reading the limbs back overturned it.

`instructions/robot-guide/make_plans.py` is the source of the numbers, and its own history shows
what happened. The 2x pass doubled every length in the hinge block together:

| name | 1x | 2x | derived from anything? |
| ---- | -- | -- | ---------------------- |
| `LIMB` | 12 | 24 | `TORSO_H / 4` |
| `BLADE` | 5.0 | 10.0 | typed |
| `GAP` | 0.3 | 0.6 | typed |
| `STUB` | 2.0 | 4.0 | typed |
| `STUB_PROUD` | 0.8 | 1.6 | typed |
| `BLADE_OUT` | 16 | 32 | typed |
| `TOOTH_PROUD` | 0.6 | 1.2 | typed |
| `VALLEY_DEEP` | 0.45 | 0.90 | typed |

Doubling is right for the ones that set the shape. It is wrong for two kinds of length: a
clearance a printer has to hold, and a length another number already decides.

### `BLADE_OUT` is typed where the comment beside it gives the rule

The comment in `make_plans.py` says the blade's own limb "has to end `NOSE` clear of" the fork's
ear tips, which sweep `NOSE` from the pin. That makes the blade's limb stop `NOSE` from the pin
and `BLADE_OUT` come out at `2 * NOSE`, which is 24. It is typed 32, so the blade's limb stops 20
from the pin where 12 would do. `SLOT_DEEP` is `BLADE_OUT + 1`, so the slot that swallows the
blade is 33 where 25 would do, and in the hinge tab 9 mm of it is empty above the highest point
the blade's nose reaches.

`SLOT_DEEP = BLADE_OUT + 1` is wrong on its own account as well. The slot has to clear the blade's
**nose**, which reaches `NOSE` past the pin, not the blade's whole stand-out. The rule is
`2 * NOSE + 1`, measured from the fork's tip, which lands on the same 25.

**Neither excess reaches a printed part, and the first reading of this said it did.** Each limb
unions a rod onto its half of the joint, and the rod stops `NOSE` short of the pin. Read off
9p1p1's own limbs: the u limb's slot walls run z -60 to -36 with the elbow at -48, so the slot is
24 deep and its root is 12 from the pin; the l limb's tongue faces run z -12 to +12 with the elbow
at 0, so the tongue is 24 long and its root is 12 from the pin. The rod fills in the last 9 mm of
the slot and the first 8 mm of the tongue. The joint prints the same whatever `BLADE_OUT` is
typed.

So the earlier claim that the elbow is 53.8 long inside a `#limbCenter` of 48 is about the hinge
tab's two limb stubs, not about anything anyone prints, and the forearm's plain rod is not 15.6.
The rods are 27 for the upper and 26 for the lower, both of them 48 less what the far end takes
(`COLLAR_L` and `STAND`) less `NOSE`.

### The spring is figured from a free length the printed ear does not have

`EAR_FREE` is `SLOT_DEEP - NOSE`, 21, and every figure for the snap comes off it: `PRESS_F` at
**36.3 kgf** (80 lbf) and `EAR_STRESS` at **51.3 MPa** against PETG's 50. The brief and the
assembly brief both carry those two, so they are not stale; they are computed from the tab.

The printed ear is rooted where the rod ends, **12** from the pin, not 21. Stiffness goes as one
over the cube of the free length, so the same formula at 12 gives **194.78 kgf** and **157.11
MPa**. The brief asked for exactly this check: under *What would make this design fail* it says
the ear cantilevers 21 from its slot root to the pin, then "Measure both and report them, because
everything above goes as 1/L^3".

`detail_hinge` draws it longer still. It puts the slot's root at `SLOT_DEEP` from the pin, where
`SLOT_DEEP` is measured from the fork's tip, so the sheet a student is handed shows a 33 mm free
ear: 9.37 kgf and 20.77 MPa, the only one of the three that is under yield.

These are the brief's own idealized cantilever figures, and the brief's standing caveat applies to
them: half-size joints printed from `stickbot-for-bot-review` press and release without a slit, and
a snap fit that yields a little on the way in is ordinary. What is not ordinary is three documents
with three different free lengths in them.

`STUB_PROUD` is the length that never had to scale, and the brief already says so in
*What doubling did to the snap*. It sets three things at once, because the stub crosses the gap
and what is left over is all of them:

- how far the ear has to spread to let the blade in, 1.0 mm
- how deep the stub sits in its bore once it is in, also 1.0 mm, inside a bore 6.4 deep
- the press force, straight through the ear's stiffness

So the axle holds an arm by a 1 mm lip with 5.4 mm of open hole behind it, and takes 80 lbf to
assemble. Four elbows and knees.

### The only lever left is `STUB_PROUD`, and it is not enough

Shortening `SLOT_DEEP` is no lever at all, because the rod already roots the ear at 12 and cutting
the slot back to 25 changes nothing anyone prints. What is left is what the ear has to give, which
is `STUB_PROUD - GAP`, and the force goes straight through it:

| `STUB_PROUD` | spread | free 21 | free 12 (printed) |
| ------------ | ------ | ------- | ----------------- |
| 1.6 (built) | 1.00 | 36.3 kgf, 51.3 MPa | 194.8 kgf, 157.1 MPa |
| 1.1 | 0.50 | 18.2 kgf, 25.7 MPa | 97.4 kgf, 78.6 MPa |
| 0.9 | 0.30 | 10.9 kgf, 15.4 MPa | 58.4 kgf, 47.1 MPa |

No row of the printed column is a joint a middle-schooler can press together, and the gentlest one
buys that by leaving 0.3 mm holding the arm on. The snap needs a change of kind, not a change of
number, and the choice of which is Mike's:

- put the relief slit back in the blade, which is what the numbers in the brief were written for
- open the bore to the ear's tip, so the blade drops in along the slot and never spreads anything
- let the ear be thinner than the full `(LIMB - SLOT) / 2` slice near its tip

**Blocked on Mike.** Nothing in the hinge has been changed yet.

### The two robot connectors are placed by two different rules

Read back with `evMateConnector`, in the hinge's own axes with the pin on the origin:

- `blade to robot connector` at z **-26.4**, on the blade's own end face, z axis pointing out of
  the part
- `fork to robot connector` at z **+12**, which is `NOSE`, 15.4 short of the fork's end face at
  +27.4 and inside its solid, z axis pointing into the part

What follows is `move fork` having to press Transform's flip because the fork's connector faces
the wrong way, where the blade's does not, and two tutorials teaching two recipes for one idea.
The rods themselves are figured by the same rule either way — 27 for the upper and 26 for the
lower, both of them 48 less what the far end takes less `NOSE` — because the rod's length is set
by the limb's stations and not by where the joint part carries its connector.

Putting the fork's connector on its end face, where the blade's already is, makes the two halves
the same part turned around and takes the flip out of tutorial 10.

## Between entities halves what you clicked, not what you meant

`elbow end` has to sit on the pin axis half way between the fork's two ears. The reference builds
it by setting the mate connector's type to **Between entities** and picking the two Ø4.4 holes,
and lands at (0, 0, -48). Built the same way, draft9p3 landed at **(0, -3.220, -48)**: on the
axis, at the right station along the limb, and 3.2 mm off the middle along the pin.

Reading one pick at a time settles what a click on a hole's wall means. Put a connector on the
near ear's wall on its own, accept it, and it reads (0, -12.0408, -48) with z (0, 1, 0). Do the
same on the far ear and it reads (0, +12.0408, -48) with z (0, -1, 0). So a click gives an end of
the hole rather than the hole, and the end it gives is the one nearest the eye. Neither number is
`#limbD / 2`: the hole leaves the ear at 12.0408, so the ear's outside is not a flat face at 12.

That also settles the 3.220. The average of -12.0408 and +5.6 is -3.2204, and 5.6 is where the
hole meets the slot between the ears. One click was read from outside the fork and the other from
the gap between them, so one gave the outer end and the other the inner one.

Two things do not fix it. Click depth is not what decides the end: clicks 51%, 23% and 79% of the
way into the bore all gave (0, -3.220418363578604, -48) to sixteen digits. And the rim will not
stand in for the wall; a connector put on the rim edge sits at a point on the circle rather than at
its center, with its z along the tangent, at (0.0009, -12, -45.8), z (-1, 0, 0).

Making both clicks mean the same end does not fix it either, because the second click is not read
the way the first one is. Look straight at each ear from outside the fork, turn 35 degrees off the
pin so the wall shows, and click. The first hole keeps its outer end; the second comes back with
the end that faces the first. Near then far gives (0, -3.220418363578604, -48); far then near
gives (0, +3.220418363578604, -48); taking the first hole out and putting it back afterwards
leaves the number exactly where it was. The order mirrors the answer and neither order lands on
the pin.

The reference's own feature says why the GUI cannot reach it. It carries one
`entityInferenceType`, TOP_AXIS_POINT, for the whole feature, and that one applies to
`originQuery`. The second entity, `originAdditionalQuery`, has no inference of its own for the
dialog to set, so the pair of ends the GUI infers is not the pair the reference used.

A default plane will not stand in for the holes either. The feature's origin query filter is
`(EDGE or VERTEX or (FACE and isConstruction:false))`, and a default plane is construction
geometry, so every click on the Top plane comes back `selected 0 -> 0`: from the corner, face on,
and through the tree row alike. That is the filter refusing the plane, not the clicks missing it.
The same filter allows a VERTEX, and a sketch point is one.

This is a defect the frames cannot show. The connector draws as a triad on the axis either way,
and 3.2 mm along a 12 mm pin looks like nothing. What catches it is reading the model back:
`evMateConnector` over every mate connector body in the tab, which needs no `/features` and so
answers on a day when `/features` is rate limited.

## The hinge's blade connector is 6.4 mm short and 7.9 mm off its axis

Reading draft9p3's hinge back the same way gives three mate connectors:

| what it should be | reference | draft9p3 |
| --- | --- | --- |
| `axis for circular patterns` | (0, -6.6, 0), z (0, -1, 0) | (0, -6.6, 0), z (0, -1, 0) |
| `fork to robot connector` | (0, 0, 12), z (0, 0, 1) | (0, 0, 12), z (0, 0, 1) |
| `blade to robot connector` | (0, 0, -26.4), z (0, 0, -1) | **(0, -7.884, -20), z (0, 0, 1)** |

The third one is on neither the axis nor the end face, and its z points back into the part rather
than out of it. The blade's end face is at z = -26.4; -20 is 6.4 short of it, and -7.884 is off
the axis by about two thirds of the blade's half width. It reads like a pick that landed on a
tooth or a valley wall rather than on the end face.

The upper limb does not use it, so tutorial 10 stands. The lower limb does: it is the connector
`move blade` lands on `mate for ball stud`, so tutorial 11 will build a lower limb with its blade
7.9 mm off center and 6.4 mm short unless this is fixed first. The names are assigned here by
elimination against the reference's three, because `/features` is rate limited until about midday
on Sun 30 Aug; confirm the names before the fix.

## `audit.part`'s construction half ran on all six built tabs, and three of them differ

Both halves of `audit.part` were owed on every tab: the sketch half because `/features` was refused
for the whole build, the dependency half because it was never run against the reference records
waiting for it. Both ran on Fri 4 Sep and the result is in [`audit-part.md`](audit-part.md).

Every tab reproduces 9p1p1's feature list in 9p1p1's order. `head` and `foot` are otherwise clean.
Three findings stand, and each already has a task:

- **`torso shoulder profile` has no projected line where the reference has one.** Every other
  constraint matches exactly, and both sketches are built on the same five things, so the dependency
  graph reads them as identical; only the sketch half sees it. Task #125.
- **`u limb`'s tenth feature is a sketch called `elbow station` where the reference has a mate
  connector called `elbow end`.** It is the only floating feature in either tab. Task #139.
- **`ball and socket` is short the four tab variables, and the two sketches that read them in the
  reference carry the arithmetic instead.** Task #119.

**A read failure looks exactly like a missing feature.** Three features returned an empty
dependency panel on the first pass, and the record `read_construction.py` writes still lists them
in `order` while leaving them out of `features`, so `diff_construction.py` reported two features the
body tab does not have and one the ball and socket tab does not have. All three are in both tabs.
Compare `order` against `features` before reading a difference off that record.

**The reference constrains a symmetric sketch to a second default plane and draft9p3 does not**, on
six sketches across five tabs. Both spellings leave every sketch fully defined, and it is the same
trade already written down for the mouth.

## `page_sweeps.py` is clean on all nine written pages

[`plan.md`](plan.md) § *Phase W* asks for the sweeps before each page's `audit.page`. They ran on
Fri 4 Sep over `torso`, `head`, `assembly`, `ball-and-socket`, `head-socket`, `torso-joints`,
`mate-head`, `foot` and `hinge`: 765 figures, 143 `.. step:` blocks and 58 recorded keystrokes.

- **No figure is missing and none is published twice**, on any page.
- **No `.. step:` tag and no `req` tag is unknown**, on any page.
- **No picture stands without a sentence above it**, on any page. This is what draft9p2 failed
  twenty-two times over on one page.
- **Every keystroke the log recorded is on the page**, on any page.

Eighteen frames on disk are never used, spread over six pages: `torso` 6, `head` 3, `assembly` 3,
`mate-head` 2, `foot` 2, `ball-and-socket` 1. `head-socket`, `torso-joints` and `hinge` use every
frame they have. An unused frame is what a take shooting more than it needs looks like, so none of
these is read as a defect.

The gate that these sweeps precede, `audit.page`, is the reproduction into
`stickbot-draft9p3-check`, and that is task #129.

## `audit.page` drove tutorial 1 as far as the version, and one of its sentences does not work

The work is in `stickbot-draft9p3-check`, document `555033d6ce000bb44430dd6e`, workspace
`7786456e4391bf899e70d825`, Part Studio `74433d23ba8c3b718fe83b85`. It started empty. No version is
published, so there is nothing to cite yet.

One substitution was made on purpose. [`torso.rst`](../../../../instructions/stickbot-draft9p3/source/torso.rst)
opens with *Make a new Onshape document and name it* ``stickbot``, and the audit used the check
document that already existed, because that is the document the run is scoped to build in.

**Clicking the name at the top of the sketch dialog does not open the name box.** The page says to
click it and change `Sketch 1` to `torso outline`. The rename input is in the page but stays
invisible; a click on the title leaves the keyboard on the dialog body, and the letters typed next
reach the sketch as tool shortcuts. Onshape answered with *A constraint must involve something from
the sketch*, and the sketch was still called `Sketch 1`. The box is summoned by a small pencil that
appears to the right of the title on hover, which is what `name_feature` in
[`../../../../tools/onshape_gui.py`](../../../../tools/onshape_gui.py) does. Every page that names
a feature carries some version of this sentence, so the fix is not local to `torso.rst`.

Everything else on the page reproduced from its own words:

- **The units step.** The dialog opened on Inch with Display decimals `0.123`, exactly as written,
  and both fields are real `<select>` elements.
- **The Variable Studio.** The tab strip's **+** offers **Create Variable Studio**; the new tab
  carries **Name**, **Variable type**, **Value** and **Description**; and **Insert into all Part
  Studios and Assemblies** arrives ticked, as the page says it does.
- **The five rows.** Name, **Tab**, value, **Enter** commits a row and opens the next. All five came
  out type **Length**, and `wall` reads `3 mm` off `#torsoH / 32`.
- **The rectangle.** The arrow beside the rectangle button offers exactly three kinds, with **Center
  point rectangle** the middle one.
- **The two dimensions.** Typing `#torsoW` and `#torsoH` into the dimension box turned the rectangle
  black at 72 by 96, each dimension carrying `fx`.
- **The extrude.** The pick filled **Faces and sketch regions to extrude** with `Face of torso
  outline`, and **Symmetric** with `#torsoD` gave one part.
- **The tree check.** `Default geometry`, `torso outline`, `torso block`, and under
  **Parts (1)** one part named `torso`. No `Sketch 1` and no `Extrude 1`.

**The dimension box arrived reading `45.41539 mm`**, which is the units step proving itself five
steps later; the page's own claim is that you find out the unit took the first time you type a size.

Two smaller readings, neither a defect. The page hedges that the **Value** cell may need a second
double-click; one was enough on all five rows. And the page's *Dimension* button sits at the right
of the sketch toolbar as `sketch-dimension-button`, four buttons past `sketch-construction-button`;
the toolbar carries no tooltip text a script can read, so the icon's own name is what identifies it.

Owed on this page when the work resumes:

- Publish `tutorial 1 - variables and torso` and open **Versions and history** to see it above
  `Start`.
- Read the bounding box back against the page's check table: 72 mm by 48 mm by 96 mm, at x ±36 mm,
  y ±24 mm, z ±48 mm.
- Look at the box while `torsoW` is 50. The variable was driven to 50 and put back to 72, and the
  table followed both ways, but the box itself was never framed at 50, so the page's *still
  centered, still fully defined* is not yet checked.

Eight of tutorial 1's ten `.. step:` blocks are driven. Across the nine written pages the gate has
143 blocks in front of it.
