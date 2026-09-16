# Test report 2 — session 1, both parts

An agent followed `source/index.rst` literally, in the Onshape GUI, from an empty document
(`lesson-test-4`), on the private headless browser. REST was not used at all; every number below was
read off Onshape's own status bar or measured from pixels in a screenshot.

## Where the work is

| Field | Value |
| ----- | ----- |
| Document name | **`lesson-test-4`** |
| Owner | mike@stitt.cc |
| Document id | `c86d7c73e0b468c35d9e86fb` |
| Element | Part Studio 1 — `cc2073efe6e809c2ee198a32` |
| Named version | **none published** |

**Live workspace** — the only link there is, and it moves under you:
<https://cad.onshape.com/documents/c86d7c73e0b468c35d9e86fb/w/fc5d9a3fa7c43d8b8f9d3508/e/cc2073efe6e809c2ee198a32>

**No recovery point exists for this document.** Working Rule 13 wants a published, named version
and there is none, so the finished model is one stray edit from being unreproducible. Publish one
before using this document as evidence for anything. Ids were read from the live browser tab;
**the link has not been opened.**

The earlier run of this lesson lives in `robot-lesson-test-3` — `eac50b6ec48f8a12dec5fdac`,
element `2b8a8d440d3ac3e330b1010e` — also with no published version.

## Verdict

**The model completed. Every dimension that the lesson asks you to check came out exactly right.**
Part one is close to shippable. Part two builds the shape it promises, and its central new idea —
one sketch of four circles yielding a ring and a disc to two different extrudes — **works exactly as
described**. But four steps in Part two cannot be performed as written, and one defect in Part one
is worse than anything in report 1 because it is silent.

The one that would wreck a class:

> **"…type 6, press Tab." then "Press Escape to put the Dimension tool down."**  Escape, pressed
> while the little value box from the previous dimension is still open, **throws the typed number
> away and keeps the as-drawn value.** The dimension still exists, the sketch still goes black, and
> nothing warns you. Reproduced twice. The first time the torso came out **34.8 mm instead of 48** —
> visible. The second time the neck came out **5.9 mm instead of 6** — not visible to anybody.

Four Part-two steps that cannot be done as written: the Slot tool is in the wrong menu *and* is
driven differently; the Midpoint step raises an explicit error; Linear pattern opens on the wrong
mode and needs inputs the lesson never gives; and the lettering's regions cannot be clicked at all.

## What was verified as correct, with the measured numbers

| Check | Lesson says | Measured |
| --- | --- | --- |
| Torso sketch region | `Area: 1728.0 mm²` | **1728.0** |
| Torso front face (isometric) | 1728.0 | **1728.0** |
| Torso side face (isometric) | 1152.0 | **1152.0** |
| Head front face (isometric) | 1296.0 | **1296.0** |
| Head side face (final check) | 1080.0 | **1080.0** |
| Torso side face (final check) | 1152.0 | **1152.0** |
| Neck half-rectangle region | (not stated) | **36.0** = 6 × 6 |
| Eye ring region | (not stated) | **66.0**, and π/4·(10²−4²) = 65.97 |
| Pupil disc region | (not stated) | **12.6**, and π/4·4² = 12.566 |
| Slot mouth region | (not stated) | **119.6**, and 20·5 + π·2.5² = 119.63 |
| Parts count | Parts (1), named Robot | **Parts (1) — Robot** |

Sketch 1 and Sketch 2 were both confirmed **genuinely fully defined**, not just black to the eye: a
per-pixel scan of the geometry region found **zero** pixels of Onshape's underdefined blue (RGB ≈ 9,
9, 207) in either, against 2 700+ such pixels in the same region before the last constraint.

Steps that were doubted and turned out to be right:

- **Step 6 — "right-click Sketch 1 and choose Show".** Correct and in the right place. `Show` sits
  in the context menu with an eye icon, seven rows down, between `Add selection to folder…` and
  `Create Drawing of Sketch 1…`. The rectangles came straight back over the solid.
- **Step 7's `Edge of Sketch 1`.** Once the axis field is focused (see finding 2), one click on the
  neck's own left edge, at mid-height, filled the field with **`Edge of Sketch 1`** first time. No
  fighting with the Right plane at all. Report 1's "impossible instruction" is genuinely fixed.
- **The Ø12 neck.** Half a 6 mm rectangle revolved gave a cylinder measuring 12 mm across on screen.
- **"The sketch has been hidden again, exactly as in Step 6."** True, and only after the *first*
  extrude that consumes it; the second extrude off the same sketch left it shown, so step 11's
  `Hide` is right too.
- **The mouth's Remove went the correct way** with no flip needed, so the "Which way does Remove
  go?" warning did not fire. It is still worth keeping, but it did not describe this run.

## Findings, ordered by how much class time they cost

### 1. Escape discards the last typed dimension — silently (Part one and everywhere after)

**The lesson says** (steps 2.5–2.8, 3.4, 4.2 and by implication every later dimension block): type
the number, press **Tab**, and when the block is finished press **Escape** to put the Dimension tool
down.

**What actually happens.** Tab applies the number to the geometry *as a preview* but leaves the
value box open, with the number selected. The next thing you do decides its fate. Clicking to start
the next dimension commits it. **Escape reverts it.**

- Step 2.7: typed `48`, Tab (rectangle visibly became 36 × 48), Escape → the dimension read
  **34.8**, the as-drawn value. Screenshot `04-x-escape-reverted-48-to-34.8.png`.
- Step 3.4: typed `6`, Tab, Escape → the neck's height dimension read **5.9**. Screenshot
  `06-x-escape-reverted-6-to-5.9.png`.

Both sketches stayed fully defined and black. Nothing errors. A 5.9 mm neck instead of 6 mm is
invisible at any zoom a student will use, survives every check in the lesson, and only surfaces
later when the model does not fit something.

**What it should say.** Commit each dimension with **Enter**, not Tab, and press Escape only after
the value box has closed. Enter was tested seven times in this run and committed correctly every
time, leaving the Dimension tool still armed for the next pick. If Tab is kept for its own reasons,
the step must say "click a clear spot to start the next dimension, or press Enter — do **not** press
Escape while the value box is still open."

This also contradicts the lesson's own troubleshooting entry *"I canceled a dimension with the red
✗ and it stayed anyway — it keeps the measured value."* The same thing happens with Escape, and that
is the more common keystroke.

### 2. Step 7.3 — the Revolve axis field is not focused, so the click destroys the region (Part one)

**The lesson says:** "For **Revolve axis**, click the **neck's own left edge**."

**What happens.** When you invoke Revolve with a region already selected, focus stays on **Faces and
sketch regions to revolve**. Clicking the neck's left edge therefore lands in *that* field and
**empties it** — the region disappears from the dialog, the `Revolve axis` field is still blank, and
the preview vanishes. Screenshot `17-b-done-revolve-axis-picked.png`.

**What it should say.** "Click once in the **Revolve axis** field so it turns blue, then click the
neck's own left edge." With the field focused, the pick worked on the first attempt and read `Edge
of Sketch 1`.

Also worth adding: as soon as the axis is picked, **Onshape sets the operation to Add by itself**
(and fills a `Merge scope` of `Part 1`). Step 7.5, "Set the operation to Add", is already done. The
same happened at step 8 — the head's extrude opened on **Add**, not New. Both steps read as if the
student must change something, and a student who goes looking for the setting will be confused.

### 3. The Slot tool — wrong menu, and wrong interaction (Part two, mouth)

**The lesson says:** "Choose **Slot** from the sketch toolbar — it shares a dropdown with the
rectangle tools. Click a start point, an end point, then move out to set the width."

Both halves are wrong.

- **It is not in the rectangle dropdown.** That dropdown holds exactly three items: `Corner
  rectangle` (g), `Center point rectangle` (r), `Aligned rectangle`. Screenshot
  `40-x-rectangle-dropdown.png`.
- **It is in the Offset dropdown**, alongside `Offset` (o). Found only by typing "slot" into
  **Search tools…**, which then highlighted the right toolbar button. Its own tooltip reads
  **"Create a slot around continuous sketch entities."**
- **Click-start, click-end, move-out draws nothing.** With Slot armed, two clicks on the face and a
  move produced no geometry at all. Screenshot `41-b-done-slot-drawn.png`.
- **What does work:** draw a **line** first, select it, then invoke Slot. The tool then previews a
  slot offset around that line, with the width following the pointer, and one more click places it.
  Screenshot `42-a-select-slot-on-line.png`.

**What it should say.** "Press **l** and draw a horizontal line roughly where the mouth goes.
Escape. Click the line to select it. Then open the **Offset** dropdown (the one with `Offset (o)` in
it) and choose **Slot**. Move the pointer away from the line to set the width and click."

One more thing the step needs: the slot arrives with its own **Ø** dimension already placed, which
is the slot's *width*, not its length. It came in at Ø20 — a mouth wider than the head — and had to
be double-clicked down to 5.

Finally, the line you drew stays in the sketch, running down the middle of the slot. It did **not**
split the region — the slot still measured 119.6 mm² as one piece — but a student will see a line
across their mouth and reasonably worry. Say so, or tell them to toggle it to construction geometry.

### 4. The Midpoint step is impossible as written (Part two, mouth)

**The lesson says:** "Click the slot's **center line**, shift-click the **vertical line through the
origin**, press **shift + m** for **Midpoint**."

**What happens.** A yellow banner across the top of the graphics area:

> **Midpoint constraint requires a point and a line or arc.**

Two lines are not a valid Midpoint selection. Screenshot `43-b-done-midpoint.png`.

**What worked instead** (labeled deviation): select the slot centreline's **two endpoints**,
shift-click the vertical line, and press **shift + q** for Symmetric. The mouth centered itself, and
the sketch went fully defined once the three dimensions were on. That is also the same constraint
the student has already used twice, which is a teaching argument for it.

### 5. Linear pattern needs three things the lesson never mentions (Part two, chest panel)

**The lesson says:** "With that feature selected, use **Linear pattern** to repeat it — 3 across, 2
down."

**What happens.**

1. The dialog opens on **Part pattern**, and the feature you selected first is **dropped**. You must
   change the type dropdown to **Feature pattern** and then re-pick `Extrude 5` from the Features
   list. Screenshot `53-x-linear-pattern-dialog.png`.
2. `Direction` is a **required** field, outlined in red. It needs an **edge** — there is no default.
   The panel's bottom edge served for "across" and its left edge for "down".
3. "3 across, 2 down" is only half the input. Each direction also needs a **Distance**, and Distance
   is the gap between adjacent instances, not the total span. Nothing in the lesson gives a number,
   and the default 25 mm puts the holes outside the panel.

I used 6 mm across and 10 mm down, which fits six Ø4 holes tidily in the 24 × 20 panel. Screenshot
`53-a-select-pattern-3x2.png`.

**What it should say.** Name the type as **Feature pattern**, name the two edges to click, and give
the two spacings — and note that the second direction may need its arrow flipped to go downwards.

### 6. The lettering's regions cannot be clicked (Part two, lettering)

**The lesson says:** "Green ✓, extrude **Remove**, depth **0.5**."

Onshape's Text produces letter **outlines**. At the zoom where the whole torso is on screen, each
stroke is two or three pixels wide, so every click lands on an edge, not a region — three attempts
selected lines and a point instead. Zooming in sixteen notches did not help enough. Screenshots
`56-a-select-letters.png`, `56-a-select-letter-B.png`.

**What works:** invoke Extrude with nothing selected, then click **Sketch 6** in the Features list.
The field fills with `Faces of Sketch 6` and all three letters come in at once. Screenshot
`57-x-text-extrude-sketch-selected.png`. The 0.5 mm Remove then cut cleanly and regenerated in about
a second — no sign of the slowness the lesson warns about, though "BOT" is only three letters.

### 7. Selecting a sketch line and a *plane* and pressing `i` does nothing (Part one, step 3.5)

**The lesson says:** "Click its **left edge**, shift-click the **vertical line through the origin**,
then press **i** for **Coincident**. The rectangle snaps onto the centerline."

**What happened.** Both entities highlighted orange, the `Right` row lit up in the Features list,
and the status bar read `Parallel dist: 2.7 mm` — a good, visible selection. Pressing `i` **armed
the Coincident tool** (its toolbar button became active; hovering it read `Coincident (i)`) and
dropped the selection. The rectangle did not move. Screenshot
`07-b-done-neck-coincident-centreline.png`.

Picking the *same two things again* with the tool now armed applied the constraint immediately.

I cannot state the cause with confidence, so here is exactly what was observed across four attempts:

| Attempt | Selection | Result |
| --- | --- | --- |
| 3.5 | sketch line + **Right plane**, then `i` | armed the tool, no constraint |
| 3.5 retry | same two, picked with tool armed | applied |
| 3.6 | sketch line + sketch line, then `i` | applied |
| 4.3 | sketch line + sketch line, then `i` | applied |
| 4.4 | two sketch lines + **Right plane**, then `shift + q` | applied |

So it is not simply "planes break pre-selection" — Symmetric took a plane happily. But
select-then-`i` failed the one time a plane was in the selection and never failed otherwise.
Whatever the cause, the step needs a symptom line: **"if the rectangle does not move, the shortcut
armed the tool instead — click the two things again and it will apply."**

### 8. The chest-panel hole is left underdefined, contradicting the lesson's own checklist

**The lesson says:** "draw one small circle, dimension it **4**, and place it near the top-left of
the panel."

"Near the top-left" is not a constraint. After Ø4 the circle is still blue and can be dragged
anywhere. Screenshot `50-x-hole-dia4.png`. The lesson's own closing checklist demands "**Every
sketch black, endpoints included**", so the step as written cannot satisfy the step that checks it —
and the Linear pattern that follows depends on where the hole actually is.

I added 6 mm from the panel's left edge and 5 mm from its top edge, which the pattern spacings in
finding 5 are built around.

The **Text** sketch has the same problem and it is not fixable the same way: the text box arrives
with no constraints and stayed blue to the end. Either the checklist has to carve out the text
sketch, or the step has to say how to pin the box down.

### 9. "Change one number" cannot be done at the point the lesson puts it

**The lesson says:** "Double-click the **48** on the torso and type **60**."

By then, step 9.1 has hidden Sketch 1, so **there is no 48 anywhere on screen.** Two extra actions
are needed, neither of them in the text:

1. Right-click **Sketch 1** → **Show dimensions** (a separate menu item from `Show`), which draws
   the dimensions onto the 3D model.
2. Double-click the 48 — this **opens the sketch for editing** and rolls the solid back (Parts goes
   to 0), it does not open the value box. **Double-click it a second time** to get the value box.

After that it works, and works beautifully: 48 → 60 and the neck and head ride up together, which is
exactly the point the section is making. Screenshot `25-b-done-torso-60.png`. ⌘Z put it back. But
you are inside the sketch editor the whole time, so you never see the solid change — you have to
accept the sketch to see the result the paragraph promises.

Either move this section above step 9.1, or add the two actions.

### 10. "Click an empty patch of background" selects the Front plane

The lesson's deselect rule — *"To deselect, click an empty patch of background"* — does not work in
a Part Studio, because the default planes are drawn and they fill the view. Looking straight at the
Front plane, **every** click outside the model lands on it: the plane turned orange and the `Front`
row lit up in the Features list. Screenshot `23-x-view-menu.png`.

From an isometric view there is usually a corner outside all three planes. Reliably, clicking the
**empty area below the Features list** deselects and cannot hit anything.

### 11. Zoom is needed in four places and is mentioned in one

The lesson tells you to zoom for the neck. It also needs to, for:

- the **head** — you must zoom back **out** or the 36 mm rectangle does not fit on screen;
- the **eyes** — Ø10 and Ø4 on a 36 mm face are about 35 px and 14 px at the zoom you land on after
  pressing `n`; twenty-two scroll notches in made them workable;
- the **letters** — and even then it was not enough (finding 6).

Onshape's wheel zoom is small per notch: eight notches gave 1.57×, so roughly 1.06× a notch. Telling
a student "zoom in" without saying "a lot" understates it by an order of magnitude.

### 12. Smaller things

- **"Click inside the two rings"** and **"Click inside the two pupil discs"** need a **shift-click**
  for the second one. The lesson says "click" for both and never mentions shift here, though it
  explains shift-click carefully back in Part one.
- The ring click itself is completely reliable — one click between the two circles selected the
  annulus, not the disc, and read 66.0 mm². It wants a note that you must click **between** the two
  circles, not near the center.
- **Step 9.2** says "Right-click each feature… and call them **Torso**, **Neck** and **Head**", but
  there are four features by then; Sketch 1 has no name in the list.
- The extrude **Depth field arrives pre-filled with `25 mm`** every time, and the only reliable way
  to replace it is to triple-click the field. "Select what is there" (step 5.3) is doing a lot of
  work.
- The **Workspace units** dialog has **eleven** "Display decimals" dropdowns visible without
  scrolling — the lesson's "about a dozen" is fair.
- After the Coincident tool has been *used*, it stays armed, so the very next ordinary click is
  eaten. The lesson's "Escape first" rule is written only about the Dimension tool; it needs to
  cover any armed constraint tool too.
- The pupils genuinely end up **2 mm proud** of the eyes, as the lesson says: rings 3 mm, pupils 5
  mm, both measured from the same sketch plane.

## Part two, considered on its own

Part two is the half that had never been built, so here is a verdict on it separately.

**The design is sound and the model comes out looking right.** The finished robot has two ringed
eyes with pupils standing proud, a slot mouth cut 2 mm into the head, a recessed chest panel with
six holes and "BOT" cut into the chest below it. Both closing measurements are exact.

**The eyes-and-pupils idea — the new thing — works, and works better than it reads.** Every one of
its steps did what the text said:

- `c` drew four circles; `shift + o` snapped each small circle onto its big one, twice, first time;
- `e` made the two big and the two small equal;
- `shift + q` on the two center points plus the vertical line jumped them to matching distances;
- four dimensions — Ø10, Ø4, 8 and 10 — took the sketch fully defined, exactly as the paragraph
  claims ("Four circles and four dimensions, and everything else is held by Concentric, Equal and
  Symmetric");
- **clicking inside the ring selected the ring**, measuring 66.0 mm², and clicking the pupil
  selected the disc at 12.6 mm². The claim "a circle drawn inside another circle splits that area
  into two regions — a ring and a disc — and a feature can take either one" is exactly true.

The whole eye section took 15 minutes with no dead ends. If the rest of Part two were as accurate,
it would be ready.

**The three sections after it are not.** The mouth cost two dead ends (Slot's location, Slot's
interaction) and one hard stop (Midpoint). The chest panel leaves a sketch underdefined and hands
the Linear pattern three unstated inputs. The lettering cannot be selected the way the step implies.
None of these is a design problem — the shapes are all achievable and all of them were achieved —
they are all "the click-by-click has gaps", which is precisely what the warning at the top of the
lesson predicts. The warning is honest and should stay until these are fixed.

One design note rather than a text note: **the mouth ends up close to the eyes.** 9 mm above the
bottom of a 36 mm head with eyes 10 mm below the top leaves the two features about 11 mm apart, and
the face reads as a bit crowded. It is not wrong, and it matches the plan, but it is worth a look
before it is locked in.

## What I had to work out for myself

Things the lesson never states, in the order I hit them:

1. Commit a dimension with **Enter**, not Tab-then-Escape (finding 1).
2. Zoom in, and by how much, at the neck, the head, the eyes and the letters.
3. Click into the **Revolve axis** field before picking the axis.
4. Onshape has already set the operation to **Add** on the revolve and the head extrude.
5. Where the **Slot** tool lives, and that it needs a line drawn and selected first.
6. **Symmetric** on the two endpoints in place of the impossible Midpoint.
7. **Shift**-click to add the second ring, the second pupil, the second letter region.
8. Locating dimensions for the panel hole (I chose 6 from the left edge, 5 from the top).
9. Everything about the Linear pattern: Feature pattern, two direction edges, 6 mm and 10 mm.
10. That the lettering must be extruded by selecting the whole **sketch** from the Features list.
11. That "empty background" means the empty area under the Features list, not the graphics area.
12. **Show dimensions** (not `Show`) to get at a dimension after the sketch has been hidden, and
    that it then takes two double-clicks to reach the value.

## Did the two plan sheets help?

**Sheet 2 was used three times** — to confirm the head is 36 × 36 × 30 and not 36 cubed, that the
mouth is a slot rather than a rectangle, and that the eye is a circle inside a circle rather than
two separate features. **Sheet 1 was used once**, for the overall proportion of head to torso, and
its "origin — center of the torso" callout remains the single most useful thing on either sheet.

What is wrong with them, from this run:

1. **Neither sheet carries a single Part-two dimension.** Ø10, Ø4, the 8 and 10 that place the eyes,
   the 20 × 5 mouth and its 9 — none of them appear. A student who wants to check their face against
   the plan cannot.
2. **The chest panel, the six holes and the lettering are on neither sheet.** Sheet 2's torso is
   blank except for its four joint studs. Three of Part two's four sections have no drawing at all.
3. **Sheet 2's head draws the eyes much larger, relative to the head, than Ø10 on 36 mm.** Drawn,
   they read as roughly a third of the head's width; built, they are just over a quarter. A student
   who models to the picture rather than the number gets a different face.
4. **Sheet 2 carries an unresolved design question in red** — "the hip station sits on the torso's
   own bottom face, so the hip stud has nowhere to stand… Decide before the legs are modeled." That
   is a note to the authors, printed on a sheet the lesson hands to students.

Nothing on either sheet was numerically wrong where it overlapped with what I built.

## Timing

**Wall clock: 92 minutes**, 09:20:17 to 10:52:28, logged action by action in
`.docs/build-log/lesson-test/steps.log`.

**This is not student pace and must not be read as one.** It is an agent driving a headless browser
one Playwright call at a time, taking a screenshot after most actions and reading it before deciding
the next click. Some things it does far faster than a student (typing, no hesitation, no reading);
some far slower (every mouse move is a scripted coordinate, every zoom is a loop, and finding a
toolbar button means a screenshot).

What the numbers *do* say reliably is where the cost sits:

| Block | Elapsed |
| --- | --- |
| Setup, units, and all of Part one to the three area checks | 33 min |
| "Change one number" | 2 min |
| **Part two total** | **57 min** |
| — eyes and pupils | 15 min |
| — the mouth | 13 min |
| — chest panel, hole, and pattern | 18 min |
| — lettering | 10 min |

**Part two took nearly twice Part one**, and the split inside it is the story: the one section that
was written accurately (the eyes) was the fastest thing in Part two despite being the most
constraint-heavy, while the three sections with gaps each cost roughly the same as the entire eye
section. Of the mouth's 13 minutes, about 6 went on hunting for Slot and recovering from Midpoint.
Of the panel's 18, **7 were the Linear pattern alone** — a single step.

Consistent with report 1, the time went where the text was incomplete, not where the modeling was
hard.
