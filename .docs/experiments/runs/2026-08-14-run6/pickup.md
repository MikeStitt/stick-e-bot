# Run 6 — where it stands

Written at a deliberate pause, part-way through [`plan.md`](plan.md). Read that for the phase
list; this file is only what is true right now and what the next session needs to know.

## Position

Phases 0 through 7 and **7a** are **Done**. **Phase 8 is paused and 7b is next** — the rest of
the replan. [`plan.md`](plan.md) grew three phases between 7 and 8 after an audit of how the
parts were actually built: the joints were never reused, and 7a–7c rebuild them on the reuse
route in a new set of `run6p2` documents, gripper first. Read the **run 6p2** section of the plan
for the rule and the why. Phase 8 resumes after 7c. It writes each part page from the run 6 and
run 6.1 record up to the feature where that part switches to 6p2, and from the 6p2 record after
it.

7a proved the route on the gripper: four features where there were ten, measured, with what it
costs and the three things it needs in [`replan-notes.md`](replan-notes.md). Read that before
starting 7b — it will save finding `Derived` the hard way.

Branch `robot-course-plan`. **Nothing has been pushed.** Phase 8's `gripper.rst` and its images
are committed; 7a's shots, notes and measurements are committed with them.

## What phase 8 has done

**The gripper page is written and builds clean.** `make html` in `instructions/robot-guide2` is
quiet. The page is 85 figures over ten sections: the clip profile, the clip, the collar, the ball,
the wrist cavity, a look at it, the slit, the cut, four slits, and a closing feature table with
four things to check the part against.

**Its shape is the pattern for the other five parts.** Open with a finished-part shot and a table
of what every number is measured from, then a section per feature, then the feature table. The
figure block matches `ball-and-socket.rst`:

```rst
.. figure:: images/gr-83-sym-symmetric-ticked-so-the-six-is-the-total.png
   :alt: The extrude dialog with Symmetric ticked, the C solid in the graphics area
   :class: shot

   Tick **Symmetric**. Now the 6 is the *total* thickness…
```

`index.rst` now carries a second toctree, **The parts**, holding `gripper`. The other five pages
and the assembly page go in the same one.

## Writing a part page from the shots

The frames are the record; the build-notes table is what says which of them is the path that
worked. Both are needed — the shots alone include attempts that were thrown away.

1. `frames.py <prefix>` lists every capture with its step text — `gr`, `ts`, `hd`, `sc`, `bb`,
   `ft` for the six parts. A frame marked `x` or `WRONG` is a dead end.
2. Read that part's section of [`build-notes.md`](build-notes.md). Its **tree row** table is the
   feature list the page has to teach, and its `###` sub-sections are the places where the first
   attempt failed and the second worked.
3. Pick the frames on the path that worked, and open the ones whose caption will state a setting.
   Captions state what the dialog actually reads.
4. `pick.py <prefix> "2-13,15-17,44"` copies them into `source/images/` as
   `<prefix>-NN-<slug>.png`.
5. Write the `.rst`, `make html`, then delete the copied frames the page did not use:
   ``for f in images/gr-*.png; do grep -q $(basename $f) gripper.rst || rm $f; done``

Both scripts live in the session scratchpad `r61/` and are short enough to re-write from this
description if the scratchpad is gone.

### Where the torso's record and the torso's page will disagree

The torso is the next page and it is the awkward one. Three of its steps were built twice, and
**the page teaches the second build**:

- **The top-face cut sketch belongs on the torso's top face**, not on the Top plane with a
  starting offset. Frames 463–502 are the first construction; 534–547 are the repair, and 537
  (sketch plane reading `Face of Torso block`) and 545 (`Starting offset` clear, merge scope the
  two shoulder studs) are the two that show the version to teach. Frames 468–477, which draw and
  size the 80 × 40 rectangle, read `Top plane` in the dialog — they show the rectangle honestly
  but not the plane, so either re-shoot them or keep the plane out of those captions.
- **Transform ▸ Rotate will not take a plane as an axis** (frames 318–332 are that attempt).
  `Shoulder pivot lines` exists to give it two lines.
- **The shoulder revolve needs the torso hidden first** (frames 292–302), and **a revolve needs
  its axis line drawn in the sketch** (frames 121–128 are the revolve that had none).

The head, the socket-clevis limb and the blade-ball limb have their own `###` sub-sections in the
build-notes; read them before picking frames, for the same reason.

**What the replan does to the gripper page.** `gripper.rst` teaches the socket from scratch,
which is exactly what 7a replaced. Its clip sections stand; everything from **The collar**
onward is rewritten from the `shots/p7a-gripper-*` frames — the cut, the derive, the union, and
the two renames, which is a much shorter stretch of page than the collar, ball, cavity and four
slits it stands in for. Do not write the other five part pages until 7c is done — they would all
have to be written twice.

## Still to do in phase 8, once 7c lands

Five part pages — torso, head, foot, socket-clevis limb, blade-ball limb — plus the assembly
page, and then the session split: the floor, the ceiling and the published recovery version. The
habit merge in `index.rst` ("Read the dialog back before you tick it") is already settled; phase 8
confirms it against the six parts rather than re-deciding it.

Phase 9 is [`register.md`](register.md) — resolved, not resolved, never attempted, in those
words — and then the watchdog is cancelled.

## Running

**The watchdog `021f596d` is still live.** It is cancelled with CronDelete when phase 9 is Done
and `register.md` is written, and not before.

CAD runs in this top-level agent, through the GUI, on **port 9223 only** — 9222 is the user's own
signed-in browser. `tools/gui_steps.py`'s `connect()` raises on any other port; `onshape_session`'s
`connect()` points at 9222 and is not used for driving. Phase 8 is writing, not CAD, and has not
needed the browser.

## The published versions

Every part is on a named version, and the robot is assembled from those versions. The ids are in
[`build-notes.md`](build-notes.md) — the parts under each phase's *Where the work is*, the mate
versions in the phase 6 assembly table. The assembly is `robot-run6-2026-08-15`
(`cab79923d9e94d9f908d359f`) in `lesson-run6`.

## Scratchpad, which does not survive the session

Under `r61/`. Worth re-writing rather than re-deriving if they are gone:

- `frames.py` and `pick.py` — described above.
- `asm.py` — the phase 6 assembly module: the toolbar coordinates for every mate type, `insert()`
  which reaches a document's newest named version through **Other documents ▸ home ▸ search ▸
  Enter**, `connector()` which finds a mate connector under its instance in the tree, and
  `mate()`. Three things in it were paid for: snapshot the tree **before** opening the mate tool
  because the open dialog inserts its own row, fold both instances up before renaming the new mate
  row, and never right-click a row below y 955 because it lands on the tab bar.
- `vers.py` / `vercheck.py` — publish a named version of all six parts and re-read every connector
  off the published version.
- `e01.py`–`e04.py` — the phase 7 measurements: stations off the assembly's `occurrences`, the
  detent band spacing, mass properties, socket slit counts.

## Known red, not mine

`ninja check` fails on `constitution.md`: 35 lines over 100 columns, committed unwrapped at
`eab19a3`. `check-spell` and `check-level` are clean. The constitution rewrite is parked in
`draft-constitution.md`, `draft-prose-style.md` and `user-constitution.md`, all untracked, waiting
on the user.

`instructions/robot-guide2/build/` is Sphinx output and is untracked. It should not be committed.
