# Phase 4 — the read-back

A person who did not write the page followed
[`index.rst`](../../../../instructions/robot-guide2/source/index.rst) and then
[`ball-and-socket.rst`](../../../../instructions/robot-guide2/source/ball-and-socket.rst) from an
empty document, with the page as the only input. The capture is `capture/2026-08-16-181143/`:
5551 events and 158 frames. The build is `run6-ball-and-socket`
(`d421233fbff9374b85bb6cc9`), created during the run and holding one version.

## The page reproduces

The follower reached `Relief slits`, which is the last thing the page asks for, and the part they
built is **identical to the one the page was written from**. Measured against
`ball-socket-run6p2` with the same script:

```
                    faces  area mm2   surfaces                            radii mm
socket   human         22   414.0488  4 cylinder, 17 plane, 1 sphere      3.2, 4.7 x4
         run6p2        22   414.0488  4 cylinder, 17 plane, 1 sphere      3.2, 4.7 x4
ball     human          3   135.2274  1 sphere, 1 cylinder, 1 plane       3.0, 1.5
         run6p2         3   135.2274  1 sphere, 1 cylinder, 1 plane       3.0, 1.5
```

Every target in the ball-and-socket brief of [`target.json`](../2026-08-14-run6/target.json) is
met. Ball Ø6 reads r 3.0, stalk Ø3 reads r 1.5, cavity Ø6.4 reads r 3.2, collar Ø9.4 reads r 4.7,
and collar length 5.5 reads 5.5 exactly. The four collar arcs are 36.1998 mm² each, which at r 4.7
over a 5.5 height leaves 3.204 mm of circumference removed — 0.801 mm of arc per slit, the arc a
0.8 mm chord cuts at that radius. Four slits, 0.8 wide, as the brief asks.

The feature names differ from the page's in two places, so this is an independent build and not a
copied document. It is the first time *Steps reproduce* has been met by any page of
`robot-guide2`.

## The clock, and what it does not include

**31 minutes 31 seconds**, from the first event to the last.

The guide was read on a second computer. Nothing in the browser sees that, so every second spent
reading the page landed inside the 31:31 and **cannot be subtracted**. The `away`/`back` events
built after phase 2 fired zero times during the run — they catch a window switch, and there was no
window to switch to. The number is honest as a wall-clock total for one page and is an upper bound
on hands-on time by an unknown margin.

`lesson-design.md` balances the sessions on captured clicks. This page has 58 figures and took half
an hour of a capable adult's wall clock. That is the first real number the plan has to work with,
and it is one page of one joint.

## The time is in the two sketches

```
02:53 - 06:43   3m 50s   stud profile
10:14 - 11:53   1m 39s   collar circle
12:15 - 13:57   1m 42s   collar blank extrude
14:29 - 17:25   2m 56s   cavity from ball
19:33 - 24:41   5m 08s   slit profile
25:48 - 27:48   2m 00s   relief slits
29:22 - 31:21   1m 59s   slit profile, reopened
```

The two sketches are 8 m 58 s of the 31 — **28% of the session in two dialogs.** Eleven of the
twelve Escape presses fall inside them. Nothing else in the page comes close, and the difference is
not the number of entities: a sketch asks you to place geometry against references you have to find
in the viewport, and every other step is a field to fill.

The last two minutes are the follower reopening `Slit profile` and adding two dimensions to it. The
geometry did not move — it still matches the reference exactly — so this was constraining a sketch
that was already the right shape. The page closes the sketch and does not come back to it.

## The tree was red for 4 m 10 s, and every window closed

Six error windows opened and all six cleared:

```
08:45 - 08:52      7s   Revolve 1     Select the axis to revolve around
10:14 - 10:41     27s   Sketch 1
14:29 - 15:49     80s   Boolean 1
16:25 - 18:33    128s   Boolean 1     Select faces to offset
19:33 - 19:35      2s   Sketch 1
26:23 - 26:29      6s   Extrude 1     No merge scope selected
```

None of these is a wrong turn. They are the state Onshape shows while a required field is still
empty, and the Revolve one fires at the instant the dialog opens. The `No merge scope selected`
window is the clearest case: the page says **Remove**, then **Merge scope**, then the depths, and
the follower did exactly that. Clicking **Remove** is what makes the merge scope required, so the
row goes red between that click and the next one. Following the page correctly is what produces the
error.

Guide3 should say what the screen does here, because a student who sees red and was not told to
expect it will go looking for a mistake that is not there.

The Boolean is the one with real friction — 3 m 28 s red across two windows, inside a dialog that
was open for 2 m 56 s and reopened afterward.

## Two names did not survive

- `Revolve 1` was never renamed. The page asks for `Revolve stud` at line 185, in the same
  paragraph that also asks for the part to be renamed `Ball stud`. The part rename happened; the
  feature rename did not. One sentence carrying two renames lost one of them.
- The collar extrude was named `face of collar circle`. The page asks for `Collar blank` at line
  248. The follower typed this deliberately, letter by letter with a typo corrected, into the
  dialog header's rename box **before** clicking ✓ — while the page puts its rename sentence after
  the ✓. They named it early, from what they had selected, and by the time the page said what to
  call it the field was already filled.

Every other name matched apart from capitalisation, and both parts got the names the page asked
for. The renames the page attaches to their own step survived; the two that ride along at the end
of another sentence did not.

## What we were hunting, and did not find

Zero undos. Zero cancelled dialogs. Zero uses of the **Alt + c** tool search. Four hovers over a ✗
with no click behind them. Every tool the page named was found where the page said it was, and
nothing that went in had to come out.

Picking is a viewport activity: 133 of the 250 clicks land on the canvas against 19 on feature-tree
rows. The harness identifies the tree rows and cannot identify the canvas picks, so the most common
single action in the session is the one the log describes least well. The frames carry it.

## What the harness learned about itself

- **Dialog titles were not captured** on `dialog-open`, so the durations above are matched to
  dialogs by time rather than by name. Worth fixing before the next page.
- **The step marks did not survive contact.** F8 was pressed twice, both inside the first two and a
  half minutes, and F9 was never used. Everything after 02:23 is stamped `step 2`. A hotkey the
  follower has to remember while learning an unfamiliar tool is a hotkey that gets dropped, so
  aligning the log to the page had to be done from the feature names instead — which worked, and is
  what the next run should rely on.
- **Events buffered in the page before the recorder attaches carry earlier timestamps.**
  `phase2-dryrun.md` predicted this and it happened: eight events from the previous session drained
  into this log, including the three `away` events. Anchoring on `session.json["started"]` and
  discarding what precedes it is the fix, and it is the difference between a 31-minute session and
  a 59-minute one.

## For guide3

1. Fix the **Display decimals** value in `index.rst`, which names a setting Onshape does not offer
   (found in [`phase2-dryrun.md`](phase2-dryrun.md)).
2. Give each rename its own step. Two renames in one sentence loses one.
3. Put the rename where the follower will do it — in the dialog header, before the ✓ — or say
   plainly that it can wait.
4. Say what the screen shows during a half-filled dialog, in the two places the page's own order
   makes a row go red.
5. Budget the sketches. They are a quarter of the page's clock and where all the hesitation is;
   the fields and the picks are not the problem.
