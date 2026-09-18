# draft9p4 — register

**Written 2026-09-18, after the plan was deactivated.** draft9p4 set out to retake every tutorial
the settled ball joint and the fifteen degree hinge reach, write each page immediately after its
take, and close the *Steps reproduce* gate by reproducing each page into a second document. It
reached tutorial 9 part way, wrote eight pages, and closed *Steps reproduce* on three of them.

Everything below is read off the logs, the documents and the tree. Where a claim could not be
checked, it says so.

## The two documents, and the roles that swapped

| Role in the plan | Name | Document id | Workspace id |
| ---------------- | ---- | ----------- | ------------ |
| the build, branching `from` | `stickbot-draft9p4` | `fe052e606c96bb7cc5aaf59f` | `0ff70e8921be572d630dd9cc` |
| the check, starting empty | `stickbot-draft9p4-check` | `86f40935a709a0748cdbb199` | `075a86f5b8f922210c0a7317` |

**The run did the opposite, and nothing records the change.** All nine logs carry 371 lines naming
a document, and every one of them names `stickbot-draft9p4-check`. The logs call it *the reader's
document*. No note, task, commit message or plan amendment says when the roles swapped or why.

## What was built

| Tutorial | State | Steps | Frames | Verdicts |
| -------- | ----- | ----: | -----: | -------: |
| 1 torso | built, paged, reproduced | 10 | 53 | 15 |
| 2 head | built, paged, reproduced | 20 | 138 | 29 |
| 3 assembly | built, paged, reproduced | 7 | 56 | 10 |
| 4 ball and socket | built, paged | 21 | 147 | 25 |
| 5 head socket | built, paged | 10 | 123 | 14 |
| 6 torso joints | built, paged | 32 | 289 | 39 |
| 7 mate head | built, paged | 4 | 26 | 5 |
| 8 foot | built, paged | 24 | 235 | 30 |
| 9 hinge | part way, no page | 32 | 397 | 39 |
| 10 to 14 | not started | — | — | — |

160 step identifiers, 1,464 frame records and 206 verdicts across nine `.jsonl` logs. The run wrote
no per-step `state` field; the verdict lines are what stands in for it, and this table is derived
from the logs rather than recalled.

**Versions.** Both documents carry the same eight names, `tutorial 1 …` through
`tutorial 8 - the foot`, with the check document stamped first every time. Tutorial 9 published
none.

**Tutorial 9 stopped after `two forks`.** The blade is complete. What
`stickbot-draft9p4-check` lacks is `fork arm outline`, `fork arm`, `combine fork parts` and the two
mate connectors, so its fork is two loose bodies of 125 faces where draft9p1p6's is one of 252. The
build document's `hinge` is a different joint again: 48 features, bumps and valleys, never retaken.

## What each audit found, and what was done

### Phase P

- **A Variable feature cannot be renamed.** The dialog has no rename pencil, the tree row has no
  *Rename*, and `F2` does nothing, proven by driving the box in `stickbot-draft9p3-check` and
  framing every step. So the naming rule stopped being a preference: a page says nothing about
  naming a variable, because a student cannot type over the title.
- **Three settled rows moved and `pedestal outline` reads two of them as typed constants.**
  `#collar_r` and `#collar_down` are typed 9 mm where the settled rows make them 7.8 mm and 10 mm.
  `read_shape.py` cannot find this, because the foot measures as exactly what draft9p3 built. The
  step lost `captured` before any measurement.
- **The guide inherits 199 of draft9p3's 796 frames**, and 15 of the ones it drops were never on a
  page.
- **The free plan claim holds, and the page was short one condition.** Tested 2026-09-09 against
  `before-you-start.rst`.
- **`head mate` sat 0.8 mm off center because the pick was made along the socket's own axis.** Four
  spike runs; the first three held Shift wrong, because Shift is a lock rather than a modifier. The
  cure is a camera angle: turn the view off the axis before picking, and the pick lands on the
  sphere's center with nothing else in `secondaryOriginQuery`. Tutorial 5's step changed and lost
  its hide.

### Phase T and Phase W, tutorial by tutorial

Each finding below changed the page rather than the model, except where it says otherwise.

- **Tutorial 1** — the page was wrong about which way `n` turns first.
- **Tutorial 2** — four of the page's sentences were wrong about the clicks.
- **Tutorial 3** — the carried page was two frames short.
- **Tutorial 4** — the carried page was five frames short and its socket out of date.
- **Tutorial 5** — four of the page's sentences were wrong about the dialogs.
- **Tutorial 6** — a shown sketch cost the build two picks.
- **Tutorial 7** — the mate's first pick is the part that moves.
- **Tutorial 8** — the sole pattern fails four ways with nothing turning red.

### The foot, which is the finding this run is remembered for

Both feet in both documents have an unbroken sole. The eight grooves are sealed tunnels running
across the width between z −22 mm and z −20 mm under a 2 mm skin, where draft9p3's foot has eight
open notches and a sole broken into nine land strips.

**One dialog caused it.** `sole groove` has two Opposite direction arrows and only the Starting
offset one was turned, so the cut begins 22 mm below the sketch and runs 2 mm back up into the
foot. The page already told the reader to turn both; the frame `groove-06.png` shows one turned.

**Two things let it through, and they are separate failures.**

- **`shift+5` is the Top view, not the bottom.** `hero-02.png`, `groove-09.png` and `ribs-01.png`
  are captioned as the sole and all show a view cube reading Top. The page never shows the sole.
- **Every measurement agreed while the shape was wrong.** The face count collides at 60 by
  coincidence: notches give a roof, two walls and nine land strips; tunnels give a roof, a floor,
  two walls and one sole. Both come to 33 for the tread. Bounding box, volume, radii and groove
  roof heights matched as well.

**What was done.** The four visual-verification rules and the reworded *Model inspected* gate went
into the constitution on 2026-09-13. The model fix and the retakes did not happen here; they are
`task.foot.sole_groove` and `task.foot.bottom_view`.

## The gates

The plan claimed every Quality Gate except *Floor & ceiling*.

| Gate | Verdict |
| ---- | ------- |
| Steps reproduce | **not closed**, except tutorials 1, 2 and 3 |
| Names are real | closed for the eight pages written here; **fails on `hinge.rst`** |
| Links resolve | closed |
| Model inspected | **not closed** |
| Floor & ceiling | not claimed |
| Recovery point | closed through tutorial 8 |
| Prose style, Spelling, Capture is out, Imports installed | `ninja check` green, 2026-09-18 |
| Reading level | tracked, not adjudicated |

**Steps reproduce.** Tutorials 1, 2 and 3 logged reproduction language — *audit.page follows
torso.rst from an empty document*. From tutorial 4 onward the logs record only the take: *tutorial
N is built and captured in the reader's document*. Because the build and the reproduction happened
in the same document, there was no moment where the absence of a second pass was visible. The
build document's foot carries the same wrong tread down to the same face positions, which is what
re-running the same clicks looks like. Carried as `task.reproduce.draft9p4`.

**Names are real.** `instructions/stickbot-draft9p4/source/hinge.rst` has not been touched since
the guide was inherited. It says bump, dome or valley 95 times and wedge zero times, so it
describes draft9p3's round detents rather than the joint draft9p1p6 proved. It names 213 figures.

**Links resolve.** The guide carries one Onshape link, `www.onshape.com` on
`before-you-start.rst`. It was opened and the free plan claim beside it tested on 2026-09-09.

**Model inspected.** The foot is the counterexample and it is in this draft. The gate was reworded
because of it.

**Recovery point.** Eight named versions exist in both documents. Tutorial 9 published none, so
there is no recovery point for the hinge.

## What this draft leaves behind

**In `stick-e-bot`:** 18 `.rst` pages, the nine logs, the five construction records under
`reference/`, 14 scripts, `notes.md`, and 22 toolbar close-ups.

**Not in `stick-e-bot`: the frames.** The move on 2026-09-14 carried the pages and not their
pictures. `instructions/stickbot-draft9p4/source/images/` here holds `toolbar/` and nothing else,
so every figure in the eight written pages resolves to a file this repository does not have. They
are in the archive repository beside it — 795 on disk, 587 of them tracked, the other 208 being
tutorial 9's take, which was never committed anywhere.

**In Onshape:** two documents, neither of them a finished robot. `stickbot-draft9p4` has no
`l limb` and no `gripper`, and its hinge is the old detent. `stickbot-draft9p4-check` has the wedge
hinge, unfinished.

## What draft9p5 takes from it

- **`stickbot-draft9p4-check`'s `hinge` build order.** All fifteen of its variables are on the
  template and interleaved with the geometry, where draft9p1p6 opens with a block of eighteen.
  Nothing is in the check document that is not in draft9p1p6; it is a subset built to newer rules.
- **The rulings this draft settled** — the variable naming rule, variables arriving at the step
  that reads them, the connector names, and the four visual-verification rules.
- **One measured defect**, the head's eye reproducing 1.5 % oversize, which is now draft9p5's
  plan § *The head, where the eye reproduces 1.5 % oversize*.

## Open work

- `task.reproduce.draft9p4`, `task.hinge.ear_rename` and `task.briefs.section_retakes` —
  [`../../../tasks.md`](../../../tasks.md) #221, #225 and #226.
- `task.foot.sole_groove`, `task.foot.bottom_view`, `task.capture.zoom_fit`,
  `task.capture.tutorials_1_to_5`, `task.hinge.wedge_loss`, `task.print.whole_robot` —
  [`../../../2026-09-14-move-to-stick-e-bot.md`](../../../2026-09-14-move-to-stick-e-bot.md)
  § *The open work, by name*.
- The six unbuilt tabs draft9p4 owed are draft9p5's, which builds them from empty rather than
  carrying them.
