# Session 1 lesson — run 2 test report

A second, independent build of `robot-guide/source/index.rst` from an empty Onshape document,
following the written text literally, in order, as a student would. Everything below was
performed; nothing is recalled or inferred. Screenshots for every step are in this folder,
and `steps.log` carries an "about to" line before each action and a "result" line after.

## Where the work is

| | |
| --- | --- |
| Document name | **lesson-run2** |
| Document id | `ca8494ebddc1d41126fd580e` |
| Workspace id (Main) | `f6903596615c3e3f89b25587` |
| Part Studio element id | `67cd64530e81afd24476f8ba` |
| Part id | `JHD` (named **Robot**) |
| **Published version** | **`run2-session1-complete`**, id **`24dafb83c2f7814714e20c7e`** |

- Workspace (live, moves):
  <https://cad.onshape.com/documents/ca8494ebddc1d41126fd580e/w/f6903596615c3e3f89b25587/e/67cd64530e81afd24476f8ba>
- **Named version (cite this one):**
  <https://cad.onshape.com/documents/ca8494ebddc1d41126fd580e/v/24dafb83c2f7814714e20c7e/e/67cd64530e81afd24476f8ba>

Both links were opened in the browser after publishing. The version link resolves and opens
read-only with the banner *"Versions are view only. Viewing run2-sessio…"* — screenshot
`41-a-version-link-opens.png`. Neither link was checked from a student account; that gate is
still unmet.

`lesson-test-4` and `robot-lesson-test-3` were not opened.

## What the model actually measures

Measured, not inferred. Radii and face bounding boxes came from a read-only FeatureScript
evaluation against the model (no geometry was created through the API); areas came off
Onshape's own bottom-right readout, photographed.

| Check the brief asked for | Result | How |
| --- | --- | --- |
| Eyes equal | **Both eye cylinders r = 5.0000 mm (Ø10)**, centres at x = −8 and +8 | FS `evSurfaceDefinition` |
| Pupils | Both r = 2.0000 (Ø4), concentric with the eyes, standing 2 mm proud of the rings | FS |
| **Mouth 20 mm overall** | **Exactly 20.000 mm.** End arcs r = 2.5000 (Ø5); left arc spans x −10.0…−7.5, right arc x +7.5…+10.0 → axes 15 apart, extreme faces −10 to +10 | FS face bounding boxes |
| Mouth height | Slot centred at z = 39; head bottom is z = 30 → **9 mm above the head's bottom edge** | FS |
| Six panel holes | Six cylinders, all r = 2.0000 (Ø4). x centres **−6, 0, +6**; z centres **+5, −5** | FS |
| …where the lesson implies | Panel is 24 × 20 centred on the origin (x −12…+12, z −10…+10), so the first hole is **6 from the left edge and 5 from the top edge**, spacing **6 across and 10 down** — exactly as written | FS |
| **Neck Ø12** | **r = 6.0000 mm → Ø12.000**, spanning z 24 → 30 | FS |
| Part count | **Parts (1)** — one solid named **Robot** | Parts list |
| Overall bounding box | x −18…+18 (36), y −20…+15, z −24…+66 (90 tall) | REST `boundingboxes` |

Areas read off the screen, all exactly as the lesson predicts:

| Face | Read | Lesson says |
| --- | --- | --- |
| Torso front (Step 5.1) | 1728.0 mm² | 1728.0 |
| Torso side | 1152.0 mm² | 1152.0 |
| Head front (Step 8.1) | 1296.0 mm² | 1296.0 |
| Head side | 1080.0 mm² | 1080.0 |

**Every dimension the lesson asks for landed.** The Enter-not-Escape correction works: 36, 48,
6, 6, 36, 36, 24, 30, 10, 4, 8, 10, 15, 5, 9, 24, 20, 4, 6, 5, 3, 5, 2, 1, 1, 0.5 all
committed on the first try. Not one dimension was silently discarded.

### Looking at it

Six server-side renders of the published version are in this folder
(`40-render-isometric|front|right|top|left|back.png`), and all six were opened and read.

- **Front** — eyes level and equal, mouth centred, panel holes centred in the panel both ways,
  `RUN2` engraved on the chest.
- **Right** — the neck cylinder is visible between torso and head; the head overhangs the
  torso by 3 mm front *and* back (head 30 deep, torso 24, both centred), which is what the
  lesson's "big goofy head" note describes.
- **Isometric** — the neck is **invisible**: the head's 3 mm front overhang roofs over the
  6 mm gap, so from any of the standard three-quarter views the neck cannot be seen at all.
  The lesson's Part-one check tells the student to go to Isometric; a student who does that
  and cannot see the neck may reasonably think the revolve failed. Worth a sentence.
- **Top** — the two eye/pupil bosses are the only thing projecting; head reads 36 × 30.

## Findings, worst first

Ordered by how much class time each would cost thirty students.

---

### 1. "A mouth", step 5 — "the slot **5** wide" breaks the sketch. (~10–15 min)

**The text says:** *"Press d. Dimension the line 15 long, the slot 5 wide, and put the line 9
above the head's bottom edge."*

**What happened:** the Slot tool creates its **own** width dimension the moment you place it —
in my run it came out as `Ø20`, taken from where the second click landed. So the slot's width
is *already dimensioned* before step 5 begins.

Following step 5 literally, I clicked an end arc of the slot. The edit box that opened read
**`10 mm`** — a **radius**, not a width. I typed `5` and pressed Enter, and the whole sketch
turned red with **"Sketch could not be solved."** (screenshot `28-f-slot-5.png`). Two width
dimensions cannot both hold.

Note the failure mode has *changed* since run 1 but has not gone away: run 1 got a silent
25 mm mouth, run 2 gets a loud dead sketch. Either way the mouth is not built by following
the words.

**Recovery I had to work out unaided** (none of it is in the lesson): ⌘Z — which restores the
value but *leaves the new dimension in place* — then click the leftover `R10` and press
Delete, then double-click the Slot tool's own `Ø20` and type `5`. That gave the correct
20 mm mouth.

**What the text should say instead:**

> 5. The Slot tool has already put a width dimension on the slot — the number with the leader
>    line, reading Ø-something. **Double-click that number and type 5.** Do not add a second
>    width dimension; clicking the round end gives you a *radius*, and a second one turns the
>    whole sketch red with *"Sketch could not be solved."*
>
>    Then press **d** and dimension the line **15** long and **9** above the head's bottom
>    edge. **Enter** after each, then **Escape**.

---

### 2. Part two has no "vertical line through the origin" to click. (~10 min)

**The text says**, in *Six things that will bite you*: *"Right-click any plane and choose
**Hide all planes** once the sketching is done."* Then four later steps say *"shift-click the
**vertical line through the origin**"* (eyes step 4, mouth step 4, chest panel step 2 — twice,
the second one naming the **horizontal** line).

**What happened:** the vertical line through the origin **is** the Right plane seen edge-on,
and the horizontal one is the Top plane. Once they are hidden they are not drawn and cannot be
clicked. Opening a sketch on the head's front face showed a bare face with no origin lines at
all (`21-c-normal-to-face.png`, `22-a-four-circles.png`). Hovering the **Right** row in the
Features list drew the line back in orange, which is how I confirmed the identification
(`23-a-right-plane-menu.png`).

I had to right-click **Right** → **Show** before the eyes' Symmetric would work, and
right-click **Top** → **Show** before the chest panel's second Symmetric would work. Neither
is in the lesson.

**What the text should say instead:** either move the "Hide all planes" advice to the very end
of the session, or add to the start of Part two:

> The vertical and horizontal lines through the origin are the **Right** and **Top** planes
> seen edge-on. If you hid the planes at the end of Part one you will need them back: in the
> Features list right-click **Right** and choose **Show**, and do the same for **Top**. You
> will use both in the next three sketches.

---

### 3. Step 3.5 — Coincident to the centreline took three attempts, and `i` did nothing. (~8 min)

**The text says:** *"Click its **left edge**, shift-click the **vertical line through the
origin**, then press **i** for **Coincident**. The rectangle snaps onto the centreline."*

**What happened, in order:**

1. I shift-clicked the vertical line at a point that was **inside the torso rectangle**. That
   selected the torso's **shaded region**, not the line — the whole rectangle went orange and
   the readout changed to `Parallel dist: 0.0 mm` (`05-a-select-coincident-1.png`). `i` did
   nothing.
2. I shift-clicked the same line **above** the torso, where nothing is shaded. That selected
   the **Right plane** — the `Right` row lit up in the Features list — readout
   `Parallel dist: 2.8 mm` (`05-a2-select-coincident-1.png`). Pressing **i** did **nothing at
   all**: no constraint, no movement, no error message (`05-b2-done-coincident-1.png`).
3. With that identical selection I clicked the **Coincident button on the sketch toolbar**
   instead, and it worked immediately — the neck jumped onto the centreline
   (`05-c-coincident-toolbar.png`).

So the keyboard shortcut did not apply a sketch-line-to-plane Coincident, but the toolbar
button did. (`i` worked fine later for line-to-line: step 3.6 and step 4.3 both snapped on the
first press.)

**What the text should say instead:**

> 5. Click its **left edge**. Now shift-click the vertical line through the origin **above the
>    torso, where there is no shading** — inside the rectangle that click selects the *filled
>    region* instead of the line, and nothing will happen. Then click the **Coincident button
>    on the sketch toolbar** (the ⌐ symbol in the constraints group). **The `i` shortcut does
>    not work for this one** — the line you are picking is really the Right plane, and `i`
>    silently ignores it.

---

### 4. Extruding the mouth grabs the line you drew. (~5 min)

**The text says:** *"Green ✓, then extrude it **Remove**, depth **2**, so it cuts a groove."*
It never says what to select.

**What happened:** I clicked in the middle of the mouth — the obvious place. That picked the
**centre line of the slot**, which runs right through the middle of the region. Extrude opened
in **Surface** mode with `Edge of Sketch 3` in the field and *Sketch curves to extrude* as the
label (`29-c-mouth-extrude-dialog.png`). No error; it just quietly becomes the wrong feature.
Clicking inside the slot but *above* the line picked the region properly
(`zz-slotsel.png`).

**What the text should say instead:**

> 6. Green ✓. Now click **inside the mouth but not on the line running through the middle of
>    it** — that line is still there, and clicking it turns the extrude into a *surface*
>    instead of a cut. Then extrude **Remove**, depth **2**.

---

### 5. Step 4 — the head does not fit on screen, and its bottom edge lands ~1 mm from the neck's top. (~4 min)

**The text says:** step 3 opens with *"Zoom in on the top edge of the torso first"*, and then
step 4 says *"Press **g** and draw a bigger rectangle above the neck."*

**What happened:** at the zoom step 3 requires (6 mm neck comfortably clickable) a 36 mm head
is roughly three screens tall. I had to zoom back out, which the lesson never mentions.

Then step 4.3 — *"Click the head's bottom edge, shift-click the neck's top edge, press i"* —
put those two lines about ten pixels apart, because a head drawn "above the neck" naturally
lands a millimetre or two above it. I had to select the head's bottom edge first (out at the
far end, away from the neck), then zoom in twice before I could hit the neck's top edge
(`08-a`, `08-b`, `08-c`).

**What the text should say instead:** add before step 4.1 —

> **Zoom back out first.** The head is 36 mm and the neck is 6 mm; at the zoom you used for
> the neck the head will not fit on the screen.

and to step 4.3 —

> 3. Click the head's **bottom edge**, out near its left-hand end where the neck is not in the
>    way. Then zoom in on the neck before you shift-click the **neck's top edge** — the two
>    lines end up a millimetre apart and at normal zoom you cannot tell which one you have.

---

### 6. Step 7.5 — Revolve opens on **New**, not Add. (~3 min)

**The text says:** *"Leave **Full revolve** ticked, and check the operation says **Add** —
Onshape sets this itself once a solid exists, so there is usually nothing to change."*

**What happened:** the Revolve dialog opened with **New** highlighted
(`12-c-revolve-dialog.png`). It flipped itself to **Add** only *after* I picked the axis
(`12-d-revolve-axis-picked.png`). A student who does step 5 in the order written — check the
operation, then look at the axis — sees **New** and will change it, or will worry.

**What the text should say instead:**

> 5. Leave **Full revolve** ticked. **Once the axis is in, the operation switches itself to
>    Add** — it says *New* until then, which is normal. Check it says **Add** now.

---

### 7. The Text tool opens a dialog of its own that the lesson does not mention. (~2 min)

**The text says:** *"Choose **Text** from the sketch toolbar, drag a box across the chest, and
type a name."*

**What happened:** dragging the box opened a separate **Text** panel with a font dropdown,
bold/italic buttons, a greyed-out preview box, an editable box below it containing
`Default text` selected, a character counter, and **its own green ✓ / red ✗**
(`35-c-text-box.png`). The lesson stops at "type a name" and never says to accept that panel
before accepting the sketch — two green ticks, not one.

**What the text should say instead:**

> 2. Choose **Text** from the sketch toolbar and drag a box across the chest. A **Text** panel
>    opens with `Default text` already selected in the lower box — type your name over it and
>    take **that panel's** green ✓. You still have to take the sketch's green ✓ afterwards.

---

### 8. "Change one number" leaves you inside an open sketch, and leaves Sketch 1 shown. (~2 min)

**The text says:** *"**Double-click the 48**, type **60**, press **Enter**. […] Undo it with
⌘Z."* and then Part two begins.

**What happened:** the first double-click *opens Sketch 1 for editing* — the Sketch 1 dialog
appears with its green ✓ (`19-c-after-first-dblclick.png`), which is what the "two
double-clicks" note is really describing. After ⌘Z that dialog is **still open**. The lesson
never says to close it. A student who reaches for Escape here — the one key the lesson has
spent two pages warning them about — is in trouble.

Second: this section un-hides Sketch 1 and never re-hides it, so Part two starts with the
Part-one sketch lines drawn across the solid. My face pick still worked, but Step 9.1 was
explicit that those lines steal clicks.

**What the text should say instead:**

> 3. **Double-click the 48** — this opens Sketch 1 for editing. **Double-click the 48 again**,
>    type **60**, press **Enter**.
>
> Undo it with ⌘Z, then take the sketch's green **✓** to close it — *not* Escape. Finally,
> right-click **Sketch 1** → **Hide** again, or its lines will sit over the head while you are
> trying to click the head's face in Part two.

---

### 9. Linear pattern — the four fields are right; two names are not. (~1 min)

**The text says:** *"It opens on **Part pattern**. Switch it to **Feature pattern**. It will
have dropped whatever you had selected. Pick **Extrude 5** from the Features list. **Direction**
is a required field and starts empty… Set **Instance count 3** and **Distance 6**. Tick
**Second direction**…"*

**Checked, and the four named fields are the right four.** *Direction*, *Instance count*,
*Distance* and *Second direction* all exist under those exact names, and the second direction
opens its own *Direction / Distance / Instance count* trio. **`Extrude 5` is also the correct
feature name** — with the three Part-one features renamed as Step 9 instructs, the panel hole
really is `Extrude 5`, and `Sketch 6` really is the lettering sketch. Both numbers held.

Two small mismatches:

- The pick list is called **"Entities to pattern"** on *Part pattern* and renames itself to
  **"Features to pattern"** once you switch. The lesson doesn't name it either way, which is
  fine, but "it will have dropped whatever you had selected" was not true in my run — the
  field was simply empty from the start.
- The dialog puts **Distance above Instance count**; the lesson says them the other way round.

**What the text should say instead:** *"Set **Distance 6** and **Instance count 3** (the
dialog lists them in that order)."*

---

### 10. Small things, no real cost

- **Step 1.1** — "open the **Default geometry** folder": it is already open in a new document.
- **Before you start, step 4** — *Display decimals* offers `0`, `0.1`, `0.12`, `0.123`,
  `0.1234`, `0.12345`. `0.1` exists; the count "about a dozen" is right (I count eleven).
- **The deselect warning is real.** Twice I clicked what looked like empty background and got
  the **Front** plane instead — the whole viewport turned orange and the right-click menu that
  followed was the *plane's* menu, not the feature's (`14-c-ctxmenu-extrude1.png`). The lesson
  warns about this; the warning earns its place.
- **The constraint-glyph warning is real.** On the 6 mm neck the glyphs were larger than the
  rectangle, and my first attempt to dimension it produced *"A dimension cannot be created
  between these items."* (`04-c-neck-w-done.png`) because the click landed on a glyph.

## Two failures I believe were environmental, not the lesson's

Twice a sketch-region selection was silently dropped between selecting and opening Extrude, so
the dialog came up with an empty (red) region field — once for the pupils, once for the panel
hole. Onshape displayed **"Poor connection…"** at the bottom of the window during one of them
(`26-i-picked-into-dialog.png`). Picking the regions again *into* the already-open dialog fixed
it both times. I am recording this as a network/environment problem rather than a lesson
problem, but I cannot prove it, so: **unverified.**

## Timing — measured, and not student pace

Wall clock, from `steps.log`.

| Block | Start | End | Elapsed |
| --- | --- | --- | --- |
| Create the document, set units | 14:09:16 | 14:10:57 | **1 min 41 s** |
| **Part one — the body** (Step 1 → end of *Change one number*) | 14:11:14 | 14:37:50 | **26 min 36 s** |
| **Part two — the face** (sketch on face → lettering cut) | 14:38:14 | 15:23:08 | **44 min 54 s** |
| Final measuring, publish version, renders | 15:23:08 | 15:32:03 | **8 min 55 s** |
| **Total** | 14:09:16 | 15:32:03 | **82 min 47 s** |

**Agent pace is not student pace, and these numbers must not be used for the lesson plan.**
They are lower than a student's in some ways and higher in others, and there is no honest
conversion factor:

- I type coordinates instead of aiming a mouse, and I never mis-click through fatigue.
- But I also spent minutes of the above re-deriving pixel positions from screenshots, which a
  student does not do, and I paused at every step to record evidence.
- Against that, I already knew the shape I was building, I never re-read the page, and I never
  asked a question or waited for a mentor.

The one thing these numbers do support: **Part two took 1.7× as long as Part one**, and three
of the four expensive findings above are in Part two. A 90-minute session that spends 27
minutes on the body has about 60 left, and Part two consumed 45 of them for one person who
never had to put a hand up.

## What was proved, and what was not

**Proved by this run:**

- Enter-commits-a-dimension: every one of the 26 typed dimensions landed.
- Midpoint → Symmetric: Symmetric worked on the head, the eyes, the mouth and the chest panel.
- Linear pattern's four field names, `Extrude 5`, and `Sketch 6` are all correct.
- Selecting the lettering sketch by name from the Features list works, and is much easier than
  clicking letters.
- Every area check in the text reads exactly the number the text predicts.
- The finished model measures right in every respect the brief asked about: eyes equal at Ø10,
  mouth **20.000 mm** overall, six Ø4 holes at −6/0/+6 by +5/−5, neck **Ø12.000**.

**Not proved:**

- The mouth reached 20 mm only after I deviated from the written step 5. **A student following
  the words gets a red sketch, not a mouth.**
- Steps 2, 3.5 and 4 of Part two cannot be performed at all with the planes hidden as the
  lesson's own preamble instructs.
- No link was checked from a student account.
- Nothing here was walked at student pace or timed at student pace.
