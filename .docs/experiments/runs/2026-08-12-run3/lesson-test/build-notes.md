# Session 1 lesson — run 3 test report

The whole of `instructions/robot-guide/source/index.rst` was built from the words, in order,
from an empty document, by a reader who had not read ahead. **Both parts completed. Every
measurement the lesson asks for came out exactly right.** The lesson's steps are sound; what it
is missing is the handful of things that happen *between* the steps, and those cost about
eighteen of the seventy-two minutes.

Every line below was performed at the time shown. `steps.log` in this folder carries an "about
to" line before each action and a "result" line after, and every screenshot named here is in
this folder.

## Where the work is

| | |
| --- | --- |
| Document name | **lesson-run3** |
| Document id | `17723bb5b4f85b74849e355b` |
| Element id (Part Studio 1) | `c797d0e3a7e5a614806a22f6` |
| Version name | **lesson-run3-final** |
| Version id | `0d33f8c86fb605e7b8864f0f` |
| Version link | <https://cad.onshape.com/documents/17723bb5b4f85b74849e355b/v/0d33f8c86fb605e7b8864f0f/e/c797d0e3a7e5a614806a22f6> |
| Workspace link — **live, will change** | <https://cad.onshape.com/documents/17723bb5b4f85b74849e355b/w/6da3ae6be1961c300552cd9d/e/c797d0e3a7e5a614806a22f6> |

The version was created at 04:01:09 UTC from the **Create version…** button in the far-left icon
strip. The workspace has had no feature edited since; the two face measurements taken after
publication (below) were taken by clicking faces, which changes nothing.

## What came out

Twenty features, one part named **Robot**, matching the lesson's *What you should have at the
end* list item for item. `63-a-isometric-fit.png` is the finished model; `61-render-*.png` are
four `shadedviews` renders (isometric, front, right, top).

Feature list as built: `Sketch 1`, `Torso`, `Neck`, `Head`, `Sketch 2`, `Extrude 1`, `Extrude 2`,
`Sketch 3`, `Extrude 3`, `Sketch 4`, `Extrude 4`, `Sketch 5`, `Extrude 5`, `Linear pattern 1`,
`Sketch 6`, `Extrude 6` — plus the three default planes.

### Every check the lesson asks for

Clicked in the GUI, with nothing else selected, and read off the status bar:

| Check | Lesson says | Measured | Screenshot |
| --- | --- | --- | --- |
| Torso front face | 1728.0 mm² | **1728.0 mm²** | `21-torso-front-readout.png` |
| Torso side face | 1152.0 mm² | **1152.0 mm²** | `21-torso-side-readout.png` |
| Head front face | 1296.0 mm² | **1296.0 mm²** | `21-head-front-readout.png` |
| Torso side face, at the end | 1152.0 mm² | **1152.0 mm²** | `63-d-torso-side-readout.png` |
| Head side face, at the end | 1080.0 mm² | **1080.0 mm²** | `63-b-head-side-readout.png` |
| Parts | one body | **Parts (1) — Robot** | `63-a-isometric-fit.png` |

Read-only REST, for the dimensions no face area proves:

| Quantity | Value | What it proves |
| --- | --- | --- |
| Bounding box X | −18.0 to +18.0 mm | 36 wide, centred on the origin |
| Bounding box Z | −24.0 to +66.0 mm | torso 48 centred on the origin; head from 30 to 66; a 6 mm neck gap |
| Bounding box Y | −20.0 to +15.0 mm | head 30 deep (−15…+15); pupils reach −20, so **2 mm proud of the 3 mm rings**, exactly as the lesson claims |
| Volume | 8.0787 × 10⁻⁵ m³ = 80 787 mm³ | consistent with 36×48×24 + 36×36×30 + Ø12×6 less the mouth, panel, holes and lettering |
| Centroid | 0, 0, 0 | the symmetric extrudes did what they were asked |

The one acceptance item I can only report partially: **"Every sketch black, endpoints included."**
Sketch 1 and Sketch 5 were photographed fully black before their green ✓
(`22-c-torso-60.png`, `54-g-hole-defined.png`). I did not photograph the other four at the moment
of acceptance, so I am not claiming them.

## The clock

| Block | From | To | Elapsed |
| --- | --- | --- | --- |
| Signed-out browser — diagnose, wait, recover | 22:41:42 | 22:50:06 | 8 min 24 s |
| Create the document, set units | 22:51:10 | 22:52:04 | 54 s |
| **Part one** — Steps 1–9 | 22:52:26 | 23:10:59 | 18 min 33 s |
| Part one — check by measuring | 23:11:26 | 23:12:14 | 48 s |
| Part one — change one number | 23:12:50 | 23:14:36 | 1 min 46 s |
| **Part two** — sketch on the head face | 23:15:03 | 23:15:43 | 40 s |
| Part two — eyes and pupils | 23:16:16 | 23:28:44 | **12 min 28 s** |
| Part two — the mouth | 23:29:12 | 23:43:01 | **13 min 49 s** |
| Part two — chest panel and pattern | 23:43:48 | 23:54:03 | 10 min 15 s |
| Part two — lettering | 23:54:31 | 23:56:21 | 1 min 50 s |
| Measure, render | 23:56:57 | 23:57:37 | 40 s |
| Publish the version | 23:58:07 | 00:01:14 | 3 min 7 s |
| Final two face checks | 00:02:47 | 00:03:35 | 48 s |
| **Hands-on, document created to last check** | **22:51:10** | **00:03:35** | **72 min 25 s** |
| **Wall clock including the sign-out** | **22:41:42** | **00:03:35** | **81 min 53 s** |

The shape, which is what matters:

- **Part two costs about twice Part one.** Part one 22 min 10 s, Part two 41 min 18 s — a ratio
  of 1.86. Run 2 measured 1.69. Two runs, two different agents, same shape: **the face is the
  expensive half, and it is the half the lesson spends fewer words on.**
- **Two sections own a third of the whole session.** Eyes 12 min 28 s and mouth 13 min 49 s are
  26 minutes of a 72-minute build, and every one of the three deviations below lives in them.
- **The lettering, the most intimidating-looking section, took 1 min 50 s.** It is written well
  enough that it cost nothing.
- Run 2 took 82 minutes; this run took 72 min 25 s of hands-on. The nine-minute difference is not
  evidence the text improved — a different agent with different aiming luck accounts for it. What
  *is* comparable is the ratio above, and it held.

The budget is 90 minutes of hands-on per session. This run fits, with 18 minutes to spare, but
only because nothing went badly wrong in Part one. A student who loses a sketch to a double
Escape has no spare.

## Where the lesson did not work as written

Six places. Three cost real time and needed a deviation; three are text defects.

### 1. Clicking inside a pupil disc does not select the pupil disc — and Onshape does not say so

*Eyes and pupils, step 10: "Click inside the two **pupil discs**. **shift + e**, depth **5**,
**Add**, green ✓."*

This took three attempts, 23:25:18 to 23:28:06, and it is the single worst gap in the lesson.

- **Attempt 1**, at the zoom where the whole head fits: the two clicks selected the two sketch
  **center points**, not the discs. The status bar read *Min dist: 16.0 mm*. Extrude opened with
  an empty selection and no depth field at all (`33-a`, `33-b`). Nothing said anything was wrong.
- **Attempt 2**, after zooming in 8 notches: the same clicks landed on the pupil **circle edges**.
  Onshape silently switched the Extrude from Solid to **Surface**, and from Add to **New**, and
  previewed "Surfaces (2)" — a valid feature that would have added two zero-thickness surfaces to
  the part list (`34-b`, `34-c`). **There is no error. Taking the green ✓ here produces a wrong
  model that still says Parts (1) plus two surfaces.**
- **Attempt 3**, after 8 more notches, with each pupil about 70 px across: the clicks finally
  gave *Face of Sketch 2* twice, on Solid / Add, and depth 5 worked (`35-a`, `35-b`, `35-c`).

**What the lesson should gain**, as an admonition beside step 10:

> **A pupil is a small target and Onshape will take the wrong thing quietly.** Zoom until each
> pupil is about the size of a fingertip on screen before you click into it. If the extrude
> dialog has no **Depth** field, you picked the center points. If it says **Surface** instead of
> **Solid**, you picked the circle's edge. Cancel with the red ✗ — do not correct it in the
> dialog — zoom in further, and click again.

The *Zoom in before you aim* item in *Six things that will bite you* is about aiming; it does not
prepare a reader for a tool that changes what it is building based on what got picked.

### 2. The mouth's Symmetric needs the vertical line where no solid is behind it

*A mouth, step 4: "shift-click the **vertical line through the origin**, and press **shift + q**."*

Three attempts, 23:34:37 to 23:37:15.

- At zoom-to-fit, the two mouth endpoints could not be picked at all — the clicks selected
  nothing and only the Right plane ended up in the selection (`40-a`, `40-b`).
- Zoomed in 12 notches, the endpoints picked correctly (*Min dist: 12.2 mm*), but the third
  click, on the vertical line below the mouth, selected the **torso's front face** instead: the
  line runs across solid geometry, and the solid wins (`41-b`, `41-c`).
- **Deviation:** zoomed back out 8 notches until a stretch of the vertical line hung below the
  body against empty background, and clicked it there — (878,317), (966,317), (923,850).
  Symmetric landed (`41-d`, `42-a`, `42-b`).

*Six things that will bite you* warns that the planes steal clicks meant for background. **This
is the mirror of that, and it is not written down: once there is a solid, the solid steals clicks
meant for the plane lines.** Every step in Part two that says "shift-click the vertical line
through the origin" has this problem, because by then the body exists.

> **Pick the vertical line where nothing is behind it.** Once the body is solid, the part of the
> line that crosses it belongs to the face, not the plane. Zoom out until the line runs past the
> robot into empty space, and click it there.

### 3. The Slot leaves the sketch unpickable, and the fix is a checkbox the lesson never names

Two separate problems, both in *A mouth*, together costing about four minutes.

**The Slot's own width dimension is placed off-screen.** Step 5 says to double-click "the width
dimension the tool created". After drawing the slot, its leader ran off the top of the window and
the dimension was not on screen at any point (`38-d`). **Deviation:** pressed **f** to zoom to
fit, which brought "Ø20" into view at (955,97) where it could be double-clicked; the prefill read
`20 mm` and 5 went in cleanly (`43-a`, `43-b`).

**The Slot's constraint glyphs completely cover the line.** Step 6 then asks for a dimension on
the line, but the slot drops a pile of glyphs directly along it, and pressing **d** and clicking
the line hit a glyph every time (`44-a`, and the failed dimension logged at 23:39:41).
**Deviation:** unticked **Show constraints** in the Sketch panel — the checkbox at the top left,
under the sketch plane field. The line became pickable immediately, the dimension took `15`
(prefill `3.10293 mm`), and the 9-above-the-bottom-edge dimension followed (`44-b`, `45-e`,
`46-b`).

The lesson's advice for covered geometry is *"Zoom in until the glyphs are small compared with
the geometry."* **That does not work for the Slot**, because the slot glyphs sit on the line
itself and stay the same size in pixels however far you zoom. The Show constraints checkbox is
the actual fix, it is one click, and it stays unticked for later sketches once you set it (Sketch
5 opened with it still off, `54-g`). The lesson never mentions it.

### 4. Step 4 needs you to zoom out, and only says to zoom in

Step 3 has you zoom in on the neck — a 6 mm feature — as the *bite you* list advises. Step 4
then says "Press **g** and draw a bigger rectangle above the neck". **At the zoom step 3 needs, a
36 mm head is about 414 px tall and runs off the top of the window before you finish the drag.**
**Deviation** at 23:00:22: zoomed out 10 notches, then drew the head.

One clause fixes it: *"Zoom back out first — the head is six times the neck."*

### 5. Editing the 48 empties the Parts list, and nothing warns you

*Change one number* is the lesson's payoff, and it works exactly as written: two double-clicks
(the first opens the dimension, the second gives an edit box prefilled `48 mm`), typing 60 and
pressing Enter moves the neck and head up with the torso, and ⌘Z puts it back.

What the lesson does not say is what the screen looks like while you are doing it. Opening
Sketch 1 rolls the feature list back to before the solids: **Parts goes to (0), the robot
disappears, and Torso, Neck and Head go grey in the list** (`22-c-torso-60.png`). A student who
has just been told to be careful with Escape will read that as having destroyed the model. One
sentence — *"The robot vanishes while the sketch is open; it comes back when you close it"* —
would cover it.

### 6. Three text defects

- **"Six things that will bite you" lists seven things.** Shortcuts, Escape, armed tools, zoom,
  constraint glyphs, deselecting, and keeping the planes shown. The seventh was added to answer
  run 2's finding; the heading was not updated.
- **The slot admonition points at the wrong step.** *"The **15** in step 5 is the distance
  between the two end centers"* — the 15 is set in step **6**. Step 5 is the width.
- **"Which way does Remove go?" did not trigger.** The mouth's Remove extrude cut *into* the head
  with no flip needed (`47-e`, `48-a`), as did the panel, the hole and the lettering — four
  Removes, no direction flip anywhere. The admonition is written conditionally
  (*"If the mouth does not appear"*), so it is not wrong; but it is placed and worded as though
  the flip is expected, and a reader will go looking for an arrow that does not need touching.
  Its counterpart in *If something else happened* covers the case already.

## What the lesson gets right — claims I tested and that held

Worth recording, because run 2's corrections are what these are:

- **One sketch, three features.** Extruding the torso from Sketch 1, revolving the neck from the
  same sketch, and extruding the head from it again all worked, including the sketch being hidden
  after each consuming feature and needing right-click → **Show** each time (Step 6, and again
  before Step 8).
- **Revolve: click into the axis field first.** Doing so, then clicking the neck's own left edge,
  gave *Edge of Sketch 1* on the first try (`16-a`, `16-b`). The warning about catching the Right
  plane instead is real and the instruction defuses it.
- **The depth field always opens on `25 mm`.** Nine extrudes, nine prefills of `25 mm`. "Select
  what is there and type over it" is the right instruction.
- **Concentric, Equal and Symmetric carry values across.** Dimensioning one big circle to 10 and
  one small to 4 resized both eyes and both pupils; four circles and four dimensions left the
  sketch defined, with the eyes 8 mm either side of centre (`29-d`, `30-b`).
- **The Linear pattern claims are all three correct.** It opened on **Part pattern**; it had
  dropped the selection; **Direction** was required and empty (`56-a`). Switching to Feature
  pattern, picking Extrude 5, a horizontal panel edge, distance 6 / count 3, then a vertical edge,
  distance 10 / count 2, produced exactly six holes (`58-*`).
- **Text opens its own dialog with its own green ✓**, and selecting **Sketch 6** by name in the
  Features list is the only workable way to extrude the letters — confirmed, and it took under
  two minutes.
- **Slot really is under the Offset dropdown**, not the rectangle dropdown (`38-a`).
- **The units instruction is right**, including that the ☰ menu is the one to the left of the
  document name and that Display decimals has one entry per unit kind.

## Environment findings, which are not about the lesson

Three, all of them things the next agent will hit.

**The browser was signed out of Onshape for eight minutes at the start.** From 22:41:42 every
`goto` landed on `/signin`, in every tab, for four agents at once. Auth returned by itself at
22:50:06. No password was ever typed; the sign-in form was abandoned and the page parked at
`about:blank`.

`fetch('/api/users/sessioninfo')` distinguishes "signed out" from "slow" in one call, but the
rule has to be written as a positive test, not as "not 200":

| Response | Meaning | What an agent does |
| --- | --- | --- |
| **200** with a body carrying `roles` | signed in | carry on |
| **204** with an empty body | signed out | stop and write up; no agent can fix this |
| anything else | **unknown — a different fault** | log the status; 429 is rate limiting, 5xx is Onshape down, a thrown error is the CDP connection |

What I observed: 204 with an empty body five times between 22:42:53 and 22:45:37, flipping to
200 with a `BTUserOAuth2SummaryInfo` body (`roles: ["USER"]`) at 22:50:06 when the user signed
in by hand. **I did not observe a rate limit or a 5xx from this endpoint**, so the 204 mapping is
one day's observation and not a documented contract. A rule phrased "not 200 means signed out"
would fire on a 429 and send the next agent to wake a human over a problem that clears itself.

**The page stamp the launch prompt handed me was already in use.** Another page in the same
browser was stamped `LESSON_RUN3` and was sitting on a document that was not mine. `mypage()` as
specified returns the *first* match, and that page was index 0 — following the instruction
literally would have driven every click of this run into another agent's document. **Deviation:**
re-stamped mine `LESSON_RUN3_MSTITT_A`.

**How I noticed was luck, and the luck is the point.** I did not check for a collision; I was
chasing the sign-out, and to diagnose that I printed a read-only census of every page in the
context with `window.name` and `document.title`. `LESSON_RUN3` appeared twice in that list. Had
the login been healthy I would never have printed the census, `mypage()` would have returned index
0, and this run would have been built in somebody else's document. **The collision was caught by
an unrelated failure.**

So, of the two available fixes, **the loud lookup is the one that protects and unique stamps only
shorten the odds.** A unique stamp is a convention, and a convention is honoured by the agent that
reads it — the *other* agent's stamp is not under my control. Copy a prompt, hardcode a default,
or leave a stale page from a previous run carrying the old name, and the collision returns with
nothing to detect it. The assertion is what converts an undetectable wrong-document write into a
crash on the first line. Two details of it matter:

- **Check before stamping, not after.** The failure is "somebody already has my name". Stamping a
  duplicate makes it worse: now two pages carry the mark and neither can be told from the other.
- **Fail on any count that is not exactly one**, zero included. As written, `mypage()` returns the
  first match and never notices a second, and has no defined behaviour for none.

Do both if it is cheap. If only one, do the assertion.

**A shared scratchpad helper was overwritten by another agent mid-run.** Moved all helpers into a
private `r3lesson/` module directory. Agents sharing a scratchpad need private subdirectories.

## Which defects stop a student, and which only cost time

Ranked for whoever rewrites the lesson. The principle behind the order is worth stating because
it inverts the obvious one: **a defect that stops the student is safer than one that does not.**
A student who is stuck asks for help. A student who is wrong and unblocked does not.

1. **The pupil extrude (finding 1).** Top, and not close. It is the only defect where **the
   lesson's own acceptance check passes on a wrong model.** A Surface/New extrude leaves
   *Parts (1)* intact and changes no face area, so a student who follows *What you should have at
   the end* to the letter verifies successfully and is still wrong. Every other defect here either
   blocks the student or slows them down; this one ends with a broken model and a confident child.
2. **The vertical line, once the body is solid (finding 2).** A hard stop, and it recurs — three
   steps in Part two say "shift-click the vertical line through the origin" and all three are
   affected. There is no path forward from the text: the student clicks the right place and gets
   the wrong thing, with nothing on screen explaining why.
3. **The Slot's glyphs and its off-screen width dimension (finding 3).** Also a hard stop, and
   worse than a plain omission because **the lesson's stated remedy does not work** — a student
   who follows "zoom in until the glyphs are small" zooms in forever and the glyphs never shrink.
   Following the advice is indistinguishable from ignoring it.
4. **Parts (0) during *Change one number* (finding 5).** Not a stop, but the failure is behavioural:
   the model vanishing looks like catastrophe, and a frightened student undoes work that was fine
   or starts the session over. One sentence prevents it.
5. **Zoom out for the head (finding 4).** Time only, and partly self-correcting — a student whose
   rectangle runs off the screen will scroll out on their own.
6. **The three text defects (finding 6).** Seconds each. The six-versus-seven count and the
   step-5-versus-step-6 reference cost a moment of doubt; the Remove admonition costs a hunt for
   an arrow that never needs touching.

## What to cut if the session has to fit 90 minutes at student pace

I am the only reader who has walked this start to finish, so this is the recommendation and not
a survey. My 72 minutes is a floor: a student is slower everywhere and much slower on the
small-target work, because the aiming problems that cost me retries cost them confidence too.

**Cut the pupil extrude, keep the pupil circles.** The four circles, Concentric, Equal, Symmetric
and the four dimensions are where the teaching is, and they are cheap. The second extrude adds
nothing new — it is another Add extrude of a sketch region, which the student did three lines
earlier on the rings — and it is simultaneously the most expensive and most dangerous step in the
session. Extrude the rings only. This deletes the top-ranked defect outright.

**Demote the Slot.** It cost 13 min 49 s and produced three of the six findings. Symmetric on two
endpoints teaches a constraint the student already used on the head, and the Slot teaches a tool
they will not meet again this session. A mouth drawn as a plain rectangle with two dimensions and
extruded Remove 2 costs about three minutes and still teaches **Remove**, which is the thing Part
two actually has to teach. If the Slot stays, it needs finding 3's two fixes first.

**Protect, in this order.** *One sketch, three features* — it is the idea the whole course rests
on. ***Change one number*** — 1 min 46 s for the payoff of every constraint in Part one, the
cheapest teaching per minute in the session by a wide margin, and the moment a model stops being
a drawing. The chest panel's **Symmetric twice** — positioning by constraint instead of dimension,
with no small-target problem to fight. The **Linear pattern** — one circle, six holes, three
minutes, and the second "stop drawing the same shape twice" idea after Mirror. The **lettering**,
at 1 min 50 s, is the best reward-per-minute in Part two and reads as the payoff of the whole
session; it should never be the thing that gets dropped for time.

**Reorder Part two easiest-first.** It currently runs eyes → mouth → panel → text, which is
hardest-first, and there is no dependency forcing that — the panel and lettering are on the torso,
the eyes and mouth on the head. Panel → text → eyes → mouth means a student who runs out of the
clock stops holding a robot with a decorated chest and its name on it, rather than one with no
face.

## Retrospective

**What went well.** Following the text literally, without reading ahead, is what found the pupil
problem — a reader who already knew the model would have zoomed in by reflex and never seen it.
Screenshotting the state after every coordinate click, rather than trusting that a click landed,
caught the silent Surface switch before it was committed; that one habit is the difference between
this report and a report that says "built it, all fine" about a model with two stray surfaces in
it. Logging "about to" before and "result" after every action made this write-up a matter of
reading the log rather than remembering.

**What nearly got past me, and the hole it exposes.** At 23:51:55, setting up the Linear pattern,
I clicked what I believed was **Instance count** and typed `3`. The field's prefill read `25 mm` —
a millimetre value where a count should be — because the dialog's rows had shifted when the
Direction chip was added. The `3` went into **Distance**, which I only established a minute later
when I aimed at Distance and found it prefilled `3 mm`. Had I trusted my own log line instead of
re-reading the screenshot, the pattern would have been distance 3, count 3: three Ø4 holes at 3 mm
centres, overlapping into one blob.

**Nothing I reported would have caught that.** Part count, bounding box, centroid and all five
face areas are identical whether the six holes are spread across the panel or piled on top of each
other — every acceptance number I have is blind to anything inside the silhouette. The mouth, the
panel, the six holes and the lettering are invisible to all of them. The only artefact that shows
those features is `61-render-isometric.png`, and **I generated the renders as a nicety after I had
already decided the build was good, not as a check.** That ordering is the fault. A render is the
only acceptance test this build has for feature placement, and it should be taken and read
*before* the model is called finished, not attached to the report afterwards.

**What went poorly.** I spent 3 min 20 s hunting the Slot tool in the toolbar (23:29:48–23:33:08)
because Onshape's toolbar buttons carry no `title` or `aria-label` and I had to hover each x
position and diff `document.body.innerText`. That is an agent-tooling cost, not a lesson cost, and
I should have gone to the tooltip-diff sweep immediately instead of guessing four carets first.
The same applies to several dimension retries where my click simply missed an edge by a few
pixels; I have logged those as retries rather than findings, but they inflate the clock and a
human reader should discount them. I also let two of my own aiming errors — typing a feature name
into the tree's filter box, and typing a pattern count into the distance field after the dialog's
rows shifted — cost about two minutes between them.

**What I would change.**

1. **The pupil admonition (finding 1) is the one change that matters most.** It is a silent wrong
   answer, in the section that already costs 12 minutes, and no other step in the lesson has that
   property.
2. **Give the "vertical line through the origin" instruction a home.** It appears three times in
   Part two and it means something different once the body is solid. One admonition, referred back
   to by name, the way *Six things that will bite you* items already are.
3. **Name the Show constraints checkbox once.** It is the fix for a whole class of "my click
   landed on a glyph" problems, it is already in the panel the student is looking at, and the
   lesson's current advice for that class of problem does not work for the Slot.
4. **Re-check the clock claim after those changes, not before.** Part two is twice Part one in
   both runs. If the three changes above land and Part two does not come down, the cause is
   somewhere else and the next run should be told to look for it.
5. **Take the render before calling the build finished, and read it.** It is the only acceptance
   test in this run's battery that can see a feature's *placement*; every number I reported is
   blind inside the silhouette. Ordering it after the decision, as I did, makes it a souvenir.
6. **Make the page lookup fail loudly on any match count but one, and check before stamping.**
   Unique stamps help; the assertion is what actually protects, because the colliding stamp is
   always the other agent's, and I only found mine by accident while chasing a different failure.
7. **Test the signed-out path before launching a build agent.** One `sessioninfo` call from the
   launching session costs a second and would have saved eight minutes here, times four agents.
   Write the check as *200 means signed in*, never as *not 200 means signed out*.
