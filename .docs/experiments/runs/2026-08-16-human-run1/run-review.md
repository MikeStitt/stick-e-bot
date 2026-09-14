# Run review — what you did, where it cost you, and what the page owes you

Everything here is read off `capture/2026-08-16-181143/` and out of the built document
`run6-ball-and-socket`. Times are minutes and seconds from the recorder's start.

The headline first: you finished the page, and the part is **exactly right**. Every dimension in
every sketch matches the reference — Ø6, Ø3, 9.4, 1.35, 4.15, 2.5, 6, 0.4, 0.4, 0.2 offset — and
the two solids measure identical to the document the page was written from, to four decimals of
face area. Zero undos. Zero cancelled dialogs. Nothing you built had to come out.

## Where the time went

```
01:30 - 02:17   0:47   document created, units set
02:34 - 06:58   4:24   Stud profile sketch, closed and named
07:20 - 08:29   1:09   back into the sketch, to pin the axis line
08:34 - 09:33   0:59   Revolve
10:14 - 13:57   3:43   Collar circle, then the collar extrude
14:27 - 18:47   4:20   Boolean, in two passes
19:00 - 19:16   0:16   the two parts renamed
19:33 - 24:41   5:08   Slit profile sketch
24:56 - 27:48   2:52   the slits cut
27:48 - 31:31   3:43   after the page's last step, mostly pinning the pattern center
```

Two sketches are 9m32 of the 31m31. Everything the page presents as its hard part — the Boolean
trick, the 0.2 offset, the four-slit pattern — went in faster than drawing a rectangle did.

## What you did differently from the page

**You renamed features from the dialog header, not the tree.** The page always says the same
thing: click the green ✓, then right-click the new row and choose **Rename**. You did that once,
for `stud profile`. At `collar circle` you found the pencil in the dialog's own header and used it
for every feature after — rename first, tick second. It is the better route and the page never
mentions it.

**You deferred both part renames to one batch.** The page renames `Ball stud` right after the
Revolve and `Socket body` right after the collar extrude. You did both at 19:00–19:16, after the
Boolean. This is the deviation that cost you real time, and it is covered below.

**You reached Revolve from the toolbar.** The page routes you through **Search tools** → type
`revolve` → pick it from the list. You clicked the toolbar button at 08:45. You did use the search
for Boolean at 14:27, exactly as written. One click beat three, and nothing was lost.

**Two names are your own.** `Revolve 1` was never renamed at all — the page asks for
`Revolve stud`. The collar extrude you named `face of collar circle` where the page asks for
`Collar blank`. Everything else matched apart from case: you typed lower case throughout, the page
uses `Stud profile`.

**You solved the units defect yourself.** The page asks for a **Display decimals** value of
`0.00001`, which is not in the dropdown. You picked `0.12345` and moved on in eleven seconds.

**Small things.** The document is `run6-ball-and-socket`, not the `ball and socket` the index asks
for. You typed `0.2mm` and `1.35mm` into fields that were already in millimeters. You renamed the
Part Studio tab to `ball and socket joint` at the end, which the page never asks for.

## Where it actually went wrong

### Tools and Targets, swapped

At 15:33 you clicked **Targets** and put **Part 1** — the ball — into it. Six seconds later you
hit the **×**, then filled **Tools** with Part 1 and **Targets** with Part 2, which is right.

You caught it immediately, so it cost seconds. What matters is *why* it happened. The page's step
reads "click **Ball stud** in the parts list" and "click **Socket body**". Your parts list said
**Part 1** and **Part 2**, because the renames were still fifteen minutes away. With the names in
place there is nothing to get backwards; without them, the two rows are indistinguishable and you
have to hold in your head which one is the ball.

### The green ✓ on a red dialog

This is the one real mistake in the run.

**Offset** went on at 15:52. A second checkbox at 16:24 put the feature into *"Select faces to
offset"* and the row went red. At **17:24 you clicked the green ✓ anyway** — the rename box in the
dialog header was carrying the `has-regen-error` class while you typed `cavity from ball` into it,
so the error was on screen the whole time.

Then you reopened the feature at 17:31, clicked **Faces to offset** at 17:59, ticked one more
checkbox at 18:32, and the error cleared. Closed at 18:47.

From the premature ✓ to the fixed close is **1m23**, and the whole Boolean came to 4m20 against
about a minute of actual filling-in. The page's own *How to work* section already tells you the
fix: read the dialog back before you tick it.

The other two red rows in the run were not mistakes. The Revolve one fires the instant the dialog
opens, before you could have picked an axis. The `No merge scope selected` one fires because you
clicked **Remove** — which is what makes merge scope required — in the exact order the page tells
you to. Following the page correctly is what turns that row red.

### Four parts you did not ask for

At 25:48 the Extrude dialog opened on `Slit profile` with **New** as its default, and **Part 3,
Part 4, Part 5 and Part 6** appeared in the tree — one per slot. They sat there for 35 seconds
until you clicked **Remove** at 26:23 and they vanished.

No harm done, and you fixed it by following the next step. But the ✓ was one click away the whole
time, and clicking it would have left four loose slabs and an uncut collar.

### Both sketches closed blue, and you went back for both

This is not a mistake. It is the page's, and you caught it twice.

**`stud profile` closed blue at 06:42.** The frame taken before that ✓ shows the circle and the
rectangle black, and the axis line drawn as a dash-dot centerline with **blue endpoints** — its
length was never pinned. You reopened it at 08:06, dragged twice (352 px and 78 px, left button),
and came out 23 seconds later with a defined line: the status bar in the frame before the second ✓
reads `Length: 3.00000 mm`, origin to the bottom of the ball.

**`slit profile` closed blue at 24:40.** The frame shows the source slot black with its
2.5 / 6 / 0.4 / 0.4 dimensions and **the three patterned copies blue**. You reopened at 29:22,
dragged three times (88 px, 87 px, and a slow 58 px over 3.8 seconds), and closed it at 31:21 with
all four slots black.

The cause is exact and it is in the model. Your sketch carries one constraint the reference does
not:

```
COINCIDENT   localSecond = nxOlsKXoQPJY.center
```

`nxOlsKXoQPJY.center` is the circular pattern's own pivot — the same entity the pattern names as
its `localPivot`. The pattern's center point was never pinned to the origin, so the four copies
could swing around a center that could itself slide, and they stayed blue. One coincident fixed
it. The reference sketch has no such constraint because that pattern picked the origin up for
free when it was placed.

The drags are the diagnosis working: grabbing an entity to see whether it moves is how you find
which one is loose, and both times it found the loose one.

One loose end I could not settle: during the second trip you typed **5** and then **4** into
dimension fields and committed them, and no dimension in the finished sketch corresponds to either.
The instance count came out 4 either way.

## What would have gone faster

1. **Rename the two parts when the page says to.** Thirty seconds spent there removes the
   Tools/Targets swap, and makes the Boolean's step match what is actually on your screen.
2. **Never tick a red dialog.** 1m23, and it was the one thing in the run that had to be redone.
3. **Zoom in harder on the slit rectangle.** It is 3.5 × 0.8 mm and it took 5m08, most of it
   re-clicking small edges in the viewport. The index page already tells you to scroll in until the
   target is the size of a coin; that advice is 250 lines away from where you needed it.
4. **Check the color before the ✓, not after.** Both trips back cost 2m23 and both were necessary.
   Catching either one while the dialog was still open would have cost seconds — the sketch was in
   front of you and blue.

## What the page owes you

**Stop claiming the sketches go black, because neither one does.** This is the biggest defect on
the page and it cost 2m23.

- Line 117, after the axis line: *"Everything is black. The sketch is finished."* The line's
  endpoints are blue. The admonition under it doubles down — *"the line went black the moment you
  drew it"* — and explains a thing that did not happen.
- Line 358, after the fourth slot dimension: *"The slot goes black."* The slot does. The three
  copies the circular pattern makes do not, because the pattern's center point is free.

The page also sets the rule these two claims break: *"A sketch is finished when it is black."* A
student who believes the rule and reads the claim has to decide which one is lying. Say instead
what pins the axis line and what pins the pattern center, and let the color be the check it is
supposed to be.

**Fix the units value.** `index.rst:68` asks for **Display decimals** `0.00001`. Onshape offers
`0`, `0.1`, `0.12`, `0.123`, `0.1234`, `0.12345`. This one fails the *Names are real* gate.

**Give every rename its own step, and put the part renames before the Boolean.** Right now
`Revolve stud` and `Ball stud` share one sentence and only one of them survived; `Collar blank`
and `Socket body` share another and neither landed as written. Then say why the timing matters —
the Boolean step three sections later calls those parts by name.

**Teach the rename in the dialog header.** You found it at the second feature and used it for the
rest of the run. The page describes a route you abandoned.

**Split the Boolean's last step.** One sentence currently carries **Offset all**, the **0.2**
distance and **Keep tools**. The first of the three is the one that failed, and it is the one
buried in the middle of a sentence.

**Say what the screen does at three moments**, because in all three the page is correct and the
screen still looks wrong:

- The Revolve row goes red the instant the dialog opens, and clears when you pick the axis.
- Opening Extrude on `Slit profile` adds four new parts, which disappear when you click **Remove**.
- Clicking **Remove** turns the row red until you set **Merge scope**.

**Say where Revolve actually is.** The page sends you to the tool search; you used the toolbar
button, as most people will.

**Say that the corner rectangle is behind a dropdown arrow.** At 20:22–20:25 you opened and shut a
toolbar dropdown four times looking for it. The page says so for **Circular pattern** and not for
the rectangle.

**Budget the sketches.** They are a third of this page's clock and where all the hesitation is.
The dialogs are not the problem; the drawing is.

## What the page got right

Every tool it named was where it said, and the tool search was needed once. Nothing had to be
undone, no dialog was abandoned, and the numbers it gives produce the correct part to four decimal
places when typed in by someone who had not seen the model before. The 0.2 offset trick, which is
the conceptually hardest thing on the page, went in without a stumble.
