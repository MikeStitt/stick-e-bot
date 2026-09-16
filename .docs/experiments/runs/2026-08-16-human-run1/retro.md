# Retrospective on `robot-guide2`, from the person who followed it

Mike's account, given after the run. This is the follower's own reading of the page. It stands
beside [`run-review.md`](run-review.md), which is what the recorder measured — where the two
disagree, this file wins and the log gets re-checked against it.

## Layout

**Put the instruction above the image, not below it.** *"Click **Front** in the feature tree, under
**Default geometry**"* has to come before the picture of Front being selected. Every step on the
page currently reads the other way round: the reader meets a screenshot of the finished state and
only then finds out what they were supposed to click.

This is structural, not cosmetic. `.. figure::` puts its caption underneath the image, and every
instruction on the page lives in a figure caption — 58 of them on `ball-and-socket.rst` alone. The
directive has to change, not the wording.

**Screenshots at 4/5 of the page width, centered.** No re-capture — the images stay as they are and
Sphinx shrinks them. `_static/custom.css` currently sets `figure.shot img { width: 100% }`, which
is what makes them full width today; the change is to the figure's own width and margin.

**Put a visible gap or a page break between steps.** Right now a step's text sits closer to the
next step's image than to its own. The grouping has to say which picture belongs to which
instruction. Also mostly CSS, but only once a step is a structural unit — today the stylesheet can
only reach section headings (`.section > h2` already draws a rule between sections), because below
that level a step is just a bare figure.

## Things the page says that are not true

**The view does not swing on its own.** `ball-and-socket.rst:50` reads:

> The dialog opens with **Front** already in its field, and the view swings round to look straight
> at it.

Should be:

> A sketch dialog opens with the sketch plane set to **Front plane**. To swing the view to look
> straight at the plane, press **N**. To toggle showing and hiding the view planes (Top, Front,
> Right), press **P**.

The log corroborates this. The sketch dialog opened at 02:53; **N** was pressed at 02:55 and **P**
at 02:58 — two seconds and five seconds after the moment the page says the view moved by itself.
**N** was pressed again at 04:19, 04:30, 19:46 and 29:35, and **P** at 10:09, 25:11 and four times
between 28:17 and 28:38. Neither key appears anywhere in the guide.

## Keyboard shortcuts

**Give the optional shortcut in parentheses after the click.** `Click **Sketch** (Shift+S)`.

Every shortcut printed has to be read off Onshape's own shortcut list before it goes in — the
*Names are real* gate covers these the same as menu names, and a wrong shortcut is worse than none.
`Shift+S` checks out, with a condition on where it works; see *The feature shortcuts* below.

## What run 6 did to the view and never wrote down

The guide claims the view swings by itself because the build never noticed it was steering. All of
the following was known while `robot-guide2` was being written, and all of it lives in
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md), which students never see:

- **`n` is View normal to** (line 497). This is the keystroke behind the sentence the page
  attributes to Onshape.
- **`n` is not deterministic** (line 341). On one Front plane it gave a true Front twice, the
  **Back** once, and once did not move the camera at all. The note's own instruction is *check the
  view cube after every `n`*.
- **`n` moves the origin on screen** (line 345). Run 6 drew a collar circle 85 px below the origin
  that way, and the note says to re-find the origin after every `n`.
- **Zoom to fit frames the default planes, not the part** (line 499). `f` on a Ø9.4 collar leaves
  it a smudge until Top, Front and Right are hidden — which is what **P** is for, and why P was
  pressed eight times during the run.
- **A view cube *face* is the only confirmation of which view you are in** (line 511), because `n`
  never reports back.

Two of these are load-bearing for a student. `n` is how the sketch step works as pictured, and
hiding the planes is how anything small stays findable. The other three are the reason the page
cannot simply say "press N and carry on" — the key does not always work, it moves the origin when
it does, and only the view cube tells you which of those happened.

## The stud profile is not a revolve profile

`ball-and-socket.rst:116`:

> Draw the line on the vertical axis, from above the stalk down to below the ball, and press
> **Escape**. Everything is black. The sketch is finished.

Misleading four ways.

**The line's job is not the axis.** A revolve axis was already there — the sketch plane's own
vertical axis, visible through the origin in every shot of this step. The line is needed so the
circle is cut into pieces you can select half of. The page has it doing a job that did not need
doing and stays silent about the job it is actually for.

**The line has to meet the ball.** Its ends have to be coincident with the circle, or the region
does not close and the length is never pinned. This is the same defect as the sketch closing blue:
when the sketch was reopened at 08:06 the line came out **3.00 mm, origin to the bottom of the
ball** — snapped to the circle. Making it coincident and making it black are one act.

**A whole ball against half a stalk is inconsistent.** The sketch holds a full Ø6 circle and a
rectangle 1.5 wide, which is half of the stalk's Ø3. Read off the model, all six entities are
real geometry, none of it construction: one circle, four rectangle segments, one line.

**One closed region is the right shape.** Trim the leftovers so the sketch is the profile that
gets revolved and nothing else. The cost of not doing it is visible two steps later at line 151,
where the page has to say:

> Click the three regions that sit to the **right** of the axis line — the ball's half outside the
> stalk, the stalk's half inside the ball, and the stalk's half above the ball. Hold **shift** for
> the second and third.

Three regions and a shift-click exist only because the circle and the rectangle overlap and the
line cuts across both. One trimmed profile is one click, and the step stops needing a sentence
that names three sub-areas a student has to pick out by eye.

## In the sketch it is a cross-section, not a ball

There is no ball on screen until the revolve runs. Up to that point the page calls a circle "the
ball" and a rectangle "the stalk", and asks the reader to see a sphere in a circle before anything
has made one. Suffix them: **ball cross-section**, **stalk cross-section**, **stud cross-section**.

**Or "profile".** Both words say the same thing and either would fix the page. Profile is real CAD
vocabulary, it is one word instead of two, and it is already on the page as the sketch's own name —
`Stud profile`, at line 142.

That last point cuts both ways. If the sketch is `Stud profile` and the circle inside it is also
"the ball profile", a whole and one of its parts share a word, and the reader has to work out which
scale is meant each time. Cross-section keeps the sketch's name distinct from the shapes in it.

It also gets sharper once the profile is trimmed to one region (above): after that the sketch holds
exactly one profile, and calling the circle a profile before the trim describes something that is
not one yet. Cross-section is true at both stages.

Recommendation: cross-section in the prose for the shapes, profile reserved for the whole closed
region that gets revolved and for the feature name. Whichever way it goes, one word per concept.

Where `ball-and-socket.rst` names the 2D thing after the 3D one:

```
 31   half the ball, half the stalk, and the line they spin around
 78   The circle goes black — that is Ø6, the ball.
 84   Now the stalk. Pick the corner rectangle tool.
 97   Dimension the rectangle's right edge to 5 — the stalk's height.
103   That is half the stalk's Ø3
116   from above the stalk down to below the ball
151   the ball's half outside the stalk, the stalk's half inside the ball
```

Line 151 is the one that gains most: *the stalk's half inside the ball* is three nouns deep in an
object that does not exist yet. It also disappears entirely if the profile is trimmed to one region
(above).

The distinction is already doing work elsewhere on the page and should stay: after the revolve the
part **is** a ball on a stalk, and `Ball stud` at line 186 is a solid, correctly named. The suffix
belongs on the sketch side of the revolve only.

Alt text and image slugs carry it too — `bs-13-zoomed-so-the-ball-circle-fills-the-working-area`.
Alt text is a text edit. Slugs are a rename, and worth doing on the next capture rather than now.

## Tool names are families, not names

`ball-and-socket.rst:57` says *"Pick the **circle** tool from the sketch toolbar."* Should be:

> Pick the **Center point circle** (c) tool from the sketch toolbar.

There is no tool called "circle". There is a dropdown holding several, and the page names the
dropdown while the author clicked one of its entries. **This is a common problem across the
instructions**, not a single slip.

The guide's own typography already marks which names were checked and which were invented. Every
tool written in **Title Case** is a label that appears in Onshape. Every tool written in
**lower case** is a description the author wrote from memory:

| Written | Where | Status |
| --- | --- | --- |
| `**circle**` | 57, 203 | a dropdown, not a tool — **Center point circle** (c) |
| `**dimension**` | 77, 344 | a dropdown; which entry is unrecorded |
| `**corner rectangle**` | 84, 330 | plausible as a name, never verified, wrong case |
| `**line**` | 110 | plausible as a name, never verified, wrong case |
| `**arrow** beside the pattern tool` | 364 | the pattern tool itself is never named |

Against: **Front**, **Sketch**, **Search tools**, **Revolve**, **Top**, **Extrude**, **New**,
**Boolean**, **Subtract**, **Tools**, **Targets**, **Circular pattern**, **Remove**, **Rename**,
**Workspace units…** — all Title Case, all real.

The replacements have to be read off the sketch toolbar in Onshape, not written from memory.
Guessing here would put five more invented names in the guide.

**The collar is the barer of the two.** Line 57 at least says *"from the sketch toolbar"*; line 203
is only *"Pick the **circle** tool."* The picture cannot rescue it either — `bs-58` shows the
toolbar entry lit with its dropdown arrow beside it and the dropdown shut, so which entry was
chosen is not visible in the shot any more than it is in the words.

The step after it compresses five actions into one caption and one picture:

> Circle on the **origin**, dimension it **9.4**, press **Enter**. Black. Close the sketch with the
> **green ✓** and rename it ``Collar circle``.

Place the circle, dimension it, commit the dimension, close the sketch, rename it. The ball's
version of the same work is spread over five figures at lines 59–78. Nothing about the collar is
easier; it is the second circle, so the page hurried. A reader who has drawn exactly one circle in
their life is the reader of this step.

## Say where the hollow is, and what you actually clicked

`ball-and-socket.rst:251` is the section heading *"The hollow, made from the ball itself"*. Should
be:

> A hollow in the socket made from the ball and stud themselves.

It names the two things the old heading leaves the reader to infer: the hollow is **in the socket**,
and the thing you subtract is the whole `Ball stud` part — ball and stud — because that is what
line 279 has you click in the parts list.

**One thing to get right when this is rewritten: the stud does not cut anything.** Measured on the
finished socket, the faces are one sphere at r 3.2 and four cylinders at r 4.7 — the cavity and the
outside of the collar. There is no r 1.7 cylinder, which is what a stud subtracted with a 0.2 gap
would have left. The collar's top face sits 1.35 above the ball's center and the stud runs upward
from there, so it is above the collar the whole way and passes through empty air.

The stud's clearance comes free from the ball's cut. A sphere of r 3.2 broken by a plane 1.35 off
its center leaves a mouth of Ø5.80, and the stud is Ø3, so it swings inside an opening that was cut
for the ball.

So both halves of the sentence are true and they are true for different reasons: you click the
whole part, and only its ball does the work. Guide3 should say the first and not accidentally
promise the second.

## Sketch the slits on the collar's top face, not the Top plane

`ball-and-socket.rst:323` starts the slit sketch on the **Top** plane. That choice is what forces
the two numbers three steps later at line 428:

> Set **Depth** to **4.15**, tick **Second end position**, and set that one to **1.35**. Between
> them the two depths cover the collar's whole height.

4.15 and 1.35 are the `Collar blank` extrude's own two depths, retyped. The sentence explaining
them is an admission — the only reason those are the values is that some earlier feature used them.
Change the collar's length and the slits stop short or cut into air, and nothing in the model says
they were supposed to follow.

Sketch on the **top face of the collar blank** instead, and extrude **Remove** downward with
**Through all**. The cut runs to the far side because there is nothing left to cut, not because a
number happened to reach. Both depths go, and so does the **Second end position** step — one fewer
field, one fewer figure, and no number in the feature that has to agree with another number
somewhere else.

**Through all** and **Second end position** are the published names, read off Onshape's
[Extrude](https://cad.onshape.com/help/Content/extrude.htm) help.

The in-plane numbers already do this correctly and are worth pointing at as the example: the slot
runs 2.5 to 6 along the axis, where the cavity is r 3.2 and the collar r 4.7. Both ends deliberately
overshoot into space rather than matching an edge. The sketch already has the habit; the depths did
not.

The cost is that a sketch on a face depends on that face rather than on origin geometry. That is the
trade, and it is the right way round here: the slit's job is defined by the collar, so it should be
attached to the collar.

This changes the model, not only the page — as does trimming the stud profile to one region, above.
Guide3 cannot be written from `ball-socket-run6p2` as it stands.

## Dimension the slit from the origin, point to point

With the planes hidden there is no x or y axis line on screen to click, and every dimension in the
slit sketch currently reaches for one:

```
337   Draw a small rectangle out along the x axis to the right of the collar's center
344   Click the slot's inner end, then the y axis, then a clear spot for the label, and type 2.5
349   Same again for the outer end: 6
357   Dimension the top edge to the x axis as 0.4, and the bottom edge as 0.4 too
```

The replacement is three clicks, in this order: **the origin**, then **the corner point**, then
**an empty spot in the direction you want the dimension to run**. The third click is what decides
whether you get the horizontal distance or the vertical one, and it is the part that has to be
written down, because nothing on screen announces it.

Two corners give all four numbers. From the origin to the inner-bottom corner is **2.5** across and
**0.4** down; from the origin to the outer-top corner is **6** across and **0.4** up. Same two
picks, twice each, with the direction of the third click doing the rest.

It is a better pick even with the planes on. A point is a point; an axis is a hairline running the
width of the window that shares its pixels with whatever is behind it. And the dimension then says
what it means — *this corner is 2.5 from the center of the collar* — rather than measuring to a
reference the reader has stopped being able to see.

One thing to confirm at capture: with the sketch on the collar's top face (above), the origin sits
1.35 below the sketch plane rather than in it. Check what the dimension lands on before shooting the
step.

## The caption and the picture are of different moments

`ball-and-socket.rst:70`:

> Press **Escape** to put the circle tool down. The circle is blue, which means it is still free to
> change size.

`bs-09-the-circle.png` shows the circle **orange**, and the status bar reads
`Diameter: 59.61830 mm`. That is the dimension tool live with the circle picked, waiting for the
label to be placed — two steps later than the sentence.

**The right shot exists.** `p3-run61-bs-08-b-done-put-the-circle-tool-down.png` in the run 6 pool
shows the circle blue, no tool lit, no diameter readout. It is named for this exact step, and the
gap at `bs-08` in the guide's own numbering is where it was dropped.

So this is a **selection** defect, not a capture one. The pool holds 6767 shots and the guide ships
801, which means most of these are fixable by re-picking rather than re-shooting.

The shot names already carry the check. The pool tags every frame `-a-select-` (the state to act
on), `-b-done-` (the state after) or `-x-` (context), and spells out the action. A caption that
says *"press Escape to put the circle tool down"* wants `-b-done-put-the-circle-tool-down`, and got
a frame from a different step. Comparing the caption's verb against the shot's slug catches this
class mechanically.

## There is no circular pattern dialog

`ball-and-socket.rst:371` says *"The dialog opens asking for entities to copy."* No dialog opens.
A circular pattern **inside a sketch** is a canvas manipulator, not a feature dialog.

The log settles it. Every dialog the run opened is timestamped, and between the sketch opening at
**19:34** and its ✓ at **24:41** nothing opened or closed. **Circular pattern** was chosen from the
toolbar at **23:22**, in the middle of that span. The recorder takes a frame on every dialog-open,
so the entire pattern operation produced **no frames at all** — because there was no dialog to
trigger one.

`bs-141`, captioned *"The circular pattern dialog, empty"*, shows the **Sketch 1** dialog, which had
been open since 19:34 and has `Top plane` in its field, so it is neither the circular pattern's nor
empty. The slot is drawn with its 2.5, 6, 0.4 and 0.4 already on it and nothing has been copied yet.
The only thing in the shot belonging to the pattern is the lit toolbar icon.

**The webm is the only record of this step.** The screencast buffer writes on dialog events, so it
saw nothing here; the whole-session video Playwright wrote saw all of it. That is the fallback
[`plan.md`](plan.md) argued for on one parameter's cost, earning itself back on the first page. Read
at 800×600 with a bundled `ffmpeg`, aligned to the log by the file's birth time and confirmed
against the sketch closing at 24:41.

What the run actually did, read off the video frame by frame:

```
23:22   Circular pattern picked from the toolbar. Nothing appears. Nothing was selected.
23:22   ...and nothing keeps appearing, for 32 seconds
23:54   the slot goes orange, all four sides
23:56-24:00   the pattern draws itself: dash-dot circle, two more copies, a 3x tag
24:05   a single click on the tag — no visible change
24:14   a double-click on the tag opens a text box holding 3
24:41   the sketch's own green ✓ — the pattern never had one
```

Fifty-two seconds from picking the tool to getting the number box open, and half of it was spent in
front of a screen where the tool had been chosen and nothing had happened.

### What you double-click is a label that says `3x`

*"The instance count needs a double-click"* is not enough to act on, and the target is the reason.
Onshape's published procedure is four steps
([Circular sketch pattern](https://cad.onshape.com/help/Content/Sketch/sketch_circular_pattern.htm),
[Sketch pattern](https://cad.onshape.com/help/Content/sketch-tools-sketch-pattern.htm)):

> Select the sketch entity or entities to pattern and then click **[the circular sketch pattern
> icon]**. … Double-click to enter the number of instances in the pattern. … Move the mouse to white
> space and notice the icon is a mouse with a green button. Click to accept and set the sketch
> pattern.

**Selection comes first, then the tool.** The guide has it backwards — line 364 picks the tool and
line 375 then says to click the four sides. That order is not fatal: the video shows the tool stays
armed, and the pattern draws itself a few seconds after the selection finally lands. What it costs
is the 32 seconds in between, with the tool chosen and the screen refusing to change. Selecting
first makes the pattern appear on the click that invokes it, which is the version a reader can tell
is working.

**The pattern arrives with three instances**, and the count shows as a small grey tag reading `3x`.
That tag is the double-click target — not the copies, not the pivot square, not the angle arrow, not
the slot. It is not drawn on the geometry at all: it floats in empty space at the end of a thin
leader line with an arrowhead, aimed back at the pattern's anchor on the slot. At 5× magnification
of the video it is unmistakable; at working zoom it is a smudge the width of two characters, and it
is easy not to know it is there.

It highlights orange on hover, which is the only confirmation you are on it. A **single** click does
nothing visible — the run spent nine seconds between its single click and its double-click. Run 6's
shots catch the ends of the same sequence: `bs-146` has the slot orange with `3x` beside it, and in
`bs-148` that spot has become a white text box holding `4`.

`bs-146` is also captioned as the moment of picking the four sides, and the picture is already past
it — the pattern exists in the shot.

**To finish there is no ✓.** Move to white space, watch for the cursor with the green button, and
click. **Escape discards it silently** — [`onshape-gui-howto.md`](../../../onshape-gui-howto.md)
records that the sketch still closes clean and still reads fully defined afterward, and the tell is
the next extrude previewing one instance where you asked for four.

Guide3 has to write this step from the manipulator. Which entities got picked and how is the one
thing the log cannot answer — canvas picks are the harness's blind spot, and here there are no
frames either.

**For the harness:** a step that opens no dialog is invisible to the frame logic. The most
error-prone minute of the run is the one with nothing to look at.

## Hide the default planes before shooting a sketch

Across all of the instructions. A sketch shot with **Top**, **Front** and **Right** switched on
shows three large grey rectangles behind geometry that is often a few millimeters across, and the
thing the reader is being asked to click is the smallest object in the frame.

(The default trio is Top, Front and Right — there is no Back plane. The feature tree in
`frames/1-0125-before-dialog-ok.jpg` lists them under **Default geometry**.)

**P** is the toggle, which is the same key the page already needs for
[the view](#things-the-page-says-that-are-not-true) and does not mention. Hiding them also fixes
zoom to fit: [`onshape-gui-howto.md:499`](../../../onshape-gui-howto.md) records that `f` frames
the planes rather than the part, so on a Ø9.4 collar it leaves the part a smudge until the planes
are off.

This is the one item in this retrospective that needs new captures, because it changes what is in
the image rather than how it is displayed. `robot-guide2` carries 801 figures over ten pages, and
every sketch shot among them was taken with the planes on.

## Zooming is done the slow way, because the fast ways are not in the guide

Getting the thing you are working on to fill the screen took a long time. The log agrees: **75
wheel events and no zoom-to-fit at all.** All six `f` keystrokes in the run land inside a rename
box — "stud pro**f**ile", "**f**ace of collar circle", "cavity **f**rom ball", "slit pro**f**ile",
"relie**f** slits". The wheel bursts run up to 9 notches at a time, in the two sketches most of
all: 20 notches in `slit profile`, 18 in the Boolean, 15 in the collar, 14 in `stud profile`.

Two faster routes, both already recorded in
[`onshape-gui-howto.md`](../../../onshape-gui-howto.md) and neither in the guide:

- **Right-click → *Zoom to selection*.** Select the edge, face, region or part, then right-click.
  One step, and it frames what you are aiming at. Line 320 records that this survives an open
  feature dialog, where the right-click menu is cut down to only *Hide other parts* and *Zoom to
  selection*.
- **`f` (Zoom to fit), after hiding the planes.** On its own it frames the default planes, which
  dwarf the robot — line 499 has `f` leaving a Ø9.4 collar "a smudge in the middle of the window".
  **P** then **F** frames the part. This is the third job **P** is doing, after the sketch view and
  the screenshots.

The wheel is slow by measurement, not impression: line 206 puts a notch at **×1.06–1.07**, so
reaching a 0.8 mm slot from the default framing is on the order of fifty notches.

`index.rst:99` already tells the reader to *"scroll-wheel in until the thing you are aiming at is
the size of a coin on screen"*. That is the slow way, written down as the method.

### The shortcuts, from Onshape's own list

Read off [Keyboard Shortcuts and
Hotkeys](https://cad.onshape.com/help/Content/Home/keyboard_shortcuts_and_hotkeys.htm) and
[Zoom to Fit, Window, and
Selection](https://cad.onshape.com/help/Content/View/zoom_to_fit_window_and_selection.htm), not
from memory. `Shift+/` opens the same list inside Onshape.

| Key | Command | Times used in the run |
| --- | --- | --- |
| `w` | Zoom to window — drag a box, that region fills the view | 0 |
| `f` | Zoom to fit; also a double-click of the scroll wheel | 0 |
| `z` / `Shift+z` | Zoom out / zoom in, about the center of the view | 0 |
| `n` | Normal to; a second press flips to inverse-normal | 5 |
| `p` | Hides or shows planes | 7 |
| `d` | Dimension | 13 |
| `l` | Line | 1 |
| `c` | **Center point circle** | 1 |
| `g` | **Corner rectangle** | 1 |

**`w` is the answer to "how do I make this fill the screen".** None of the four zoom keys was used
in the whole run; the wheel did all of it.

This also settles three of the five unverified tool names above — **Center point circle** (`c`),
**Corner rectangle** (`g`) and **Line** (`l`) — and gives **Dimension** (`d`) a key, though which
entry of the dimension dropdown the page means is still open. `g` would have saved the four clicks
spent opening and shutting a toolbar dropdown at 20:22–20:25 hunting for the rectangle.

## The feature shortcuts, and `shift+s` after all

Onshape publishes a second family, and the split between the two is clean: **bare letters are view
and sketch tools, `shift`+letter opens a feature.**

| Key | Feature |
| --- | --- |
| `shift+s` | Sketch — prompts *Select a sketch plane* |
| `shift+e` | Extrude |
| `shift+w` | Revolve |
| `shift+f` | Fillet |
| `shift+h` | Show or hide sketches |

Put these in parentheses where the page names the tool: **Extrude (shift+e)**, **Revolve
(shift+w)**. `shift+w` also removes the trip through **Search tools** the page asks for at line 159
and that the follower skipped for the toolbar button anyway.

**Correction.** Earlier in this retrospective I said Onshape's list contains no `shift+s` and that
the `(Shift+S)` in the layout item was wrong. It is published, and it opens Sketch. What
[`onshape-gui-howto.md:348`](../../../onshape-gui-howto.md) recorded — `shift+s` giving the Point
tool — is a different context: that was with a sketch already open, where the sketch toolbar owns
the keys. The howto's own last bullet in that section says why: **keyboard shortcuts go to whatever
you last clicked.** Both are true, and the guide should give the shortcut in the one place it
applies — closing a sketch before starting the next one.

The families collide on purpose and it is worth saying once: `f` fits the view, `shift+f` opens
Fillet; `w` zooms to a window, `shift+w` revolves.

## Come back to isometric after every 3D operation

`shift+7` gives the isometric view — the top-front-right corner. It is on Onshape's published list
with the six orthographic views beside it, and none of the seven appears anywhere in the guide. The
run used `n` seven times and `shift+`digit **zero** times.

| Key | View |
| --- | --- |
| `shift+1` / `shift+2` | front / back |
| `shift+3` / `shift+4` | left / right |
| `shift+5` / `shift+6` | top / bottom |
| `shift+7` | isometric |

After a revolve or an extrude, press **shift+7** and shoot that. The reader has just made a solid
and should see a solid.

The page does the opposite, because a sketch leaves the camera normal to its plane and nothing
brings it back. `bs-53`, the shot of the finished ball stud, is taken with the view cube reading
**Front**: the ball is a flat blue lollipop, a circle with a tab on top, and the one interesting
thing about it — that it is round in the other direction too — is invisible. The revolve is the
step where a student most needs to see that something 3D happened.

The last figure on the page, `bs-194`, is the other half of the problem. Its view *is* isometric,
so the camera was right, but the three default planes are on and the collar is a smudge maybe ten
pixels across in the middle of them. The caption reads *"the slits running the collar's whole
length"* and nothing of the kind is visible.

The three keys work together and should be taught as one habit: **shift+7**, **p**, **f**.
Isometric, planes off, fit. Both defects above are one of the three missing.

## Todo — a completeness review before a page is called done

Review a page's prose against everything actually done to build the part, and account for each
action: it either appears as a written step, or it is left out on purpose and the reason is
recorded.

*Steps reproduce* catches a page that cannot be followed. It does not catch a page that can be
followed to the wrong screen, which is what the `n` sentence produced — the reader does every step
and ends up looking at the plane edge-on.

Where this rule lives is open. A Quality Gate in `constitution.md` and a rule in
`.parts/onshape.md` are both candidates; constitution edits are on hold, so it goes nowhere near
either without asking.
