# Where draft9p4 stands — 2026-09-13

Written part way through tutorial 9, after an audit found a wrong shape in the foot and a gap in
how the run proves its own work. The run folder is
[`experiments/runs/2026-09-08-draft9p4/`](experiments/runs/2026-09-08-draft9p4/). This file records
what is built, what is wrong, where the pieces are, and what could come next. It changes no plan.

## The two documents

| Role | Name | Document id | Workspace id |
| ---- | ---- | ----------- | ------------ |
| Holds the CAD and every frame | `stickbot-draft9p4-check` | `86f40935a709a0748cdbb199` | `075a86f5b8f922210c0a7317` |
| Named in the plan as the build | `stickbot-draft9p4` | `fe052e606c96bb7cc5aaf59f` | `0ff70e8921be572d630dd9cc` |

The plan at [`plan.md:215`](experiments/runs/2026-09-08-draft9p4/plan.md) says the build document
branches the version named in `from`, and the check document starts empty. The run did the
opposite. Every frame in the guide, and every step in all nine logs, came from
`stickbot-draft9p4-check`. The logs themselves call it "the reader's document." No note, task,
commit message or plan amendment records when or why the roles swapped.

## What is built

**Tutorials 1 through 8 are built, paged and published.** Both documents carry versions
`tutorial 1 - ...` through `tutorial 8 - the foot`. The guide has 587 committed frames across nine
folders, and the pages `torso`, `head`, `assembly`, `ball-and-socket`, `head-socket`,
`torso-joints`, `mate-head` and `foot` are written from them.

**Tutorial 9, the hinge, is part way.** The blade is complete: section variables, profile, blank,
axle, the 24 wedges, the pattern, the mirror, the arm and the relief slit. The fork is complete
through `two forks`. What remains in `stickbot-draft9p4-check`:

- `cad.parts.hinge.fork.arm_variables`, which is `#ear_free` in `robot sizes` and `#rod_fork` in
  the tab
- `cad.parts.hinge.fork.arm_sketch` and `cad.parts.hinge.fork.arm`
- `cad.parts.hinge.fork.combine`, the union of the fork's pieces
- `cad.parts.hinge.rename`, so the two parts read `blade` and `fork`
- the two connectors, `fork to robot` and `blade to robot`

The take has logged 39 step verdicts and 208 frames so far. Both are uncommitted.

**Tutorials 10 through 14 have not started.** Neither has Phase R, the register.

## What went wrong

### The foot has no tread

Both feet in both documents have an unbroken sole. The eight grooves are sealed tunnels that run
across the width between z −22 mm and z −20 mm, with a 2 mm skin under them. draft9p3's foot, which
is right, has eight open notches and a sole broken into nine land strips. The pattern is correct in
both; the y positions match to the millimeter.

The cause is one dialog. `sole groove` has two Opposite direction arrows. Only the Starting offset
arrow was turned, so the cut begins 22 mm below the sketch and runs 2 mm back up into the foot
instead of down to the ground. The page already tells the reader to turn both; the frame
`groove-06.png` shows only one turned.

Nothing caught it for two reasons that are worth keeping separate:

- **`shift+5` gives the Top view in Onshape, not the bottom one.** `hero-02.png`, `groove-09.png`
  and `ribs-01.png` are all captioned as the sole and all show a view cube reading Top. The page
  never shows the sole once.
- **Every measurement agreed while the shape was wrong.** The face count collides at 60 by
  coincidence. Notches give a roof, two walls and nine land strips; tunnels give a roof, a floor,
  two walls and one sole. Both come to 33 for the tread. The bounding box, the volume, the radii
  and the groove roof heights all match as well.

This is why the constitution now carries the four visual-verification rules and the reworded
*Model inspected* gate, added 2026-09-13 at Mike's instruction.

### The reproduce gate has no evidence behind it

`.docs/build/plan/08-foot.md:159` says: "**The page reproduces.** Driven back into
`stickbot-draft9p4` from the written text, 20 of the 22 stages stood on their first attempt." Four
other tutorial sheets carry similar claims.

What can be proved:

- All nine tutorial logs, 2,404 lines in total, name `stickbot-draft9p4-check` and nothing else.
  `grep -rl '"stickbot-draft9p4"' --include='*.jsonl'` returns nothing.
- The build document's id appears in the run folder only in `notes.md`, six read-only spike scripts
  and `reference/documents.json`. Never in a log.
- Tutorials 1, 2 and 3 logged real reproduction language, such as "audit.page follows torso.rst
  from an empty document." From tutorial 4 onward the logs record only the take: "tutorial N is
  built and captured in the reader's document."
- `stickbot-draft9p4`'s foot exists and has all 31 tree rows, and it carries the same wrong tread,
  down to the same face positions.

What cannot be proved either way is whether a reproduction ran at all. If one did, it left no
record, and it produced the take's own error rather than what the written sentence "Turn both
arrows" would produce. Repeating a defect exactly is what re-running the same clicks looks like.

The *Steps reproduce* gate is the one this whole draft exists to close;
[`plan.md:20`](experiments/runs/2026-09-08-draft9p4/plan.md) says it has never closed on any page in
any draft. On the evidence it is not closed on tutorials 4 through 8 either.

### The hinge page is draft9p3's, and its frames no longer resolve

`instructions/stickbot-draft9p4/source/hinge.rst` has not been touched since commit `34373114`,
when the guide was inherited. It uses the words bump, dome or valley 126 times and the word wedge
zero times, so it describes draft9p3's round detents, not the 15 degree wedge ring that draft9p1p6
proved and that `09-hinge.md` now specifies.

No hinge frames are committed under draft9p4 at all. The page names 200 frames; 100 of those names
happen to match files this run's new take has written, and the other 100 resolve to nothing. So the
page as it stands would show half its figures missing and the other half showing a joint the text
does not describe. It needs a fresh write in Phase W, not a patch.

## Where the artifacts are

**Committed and on the branch `robot-run3`:**

- `instructions/stickbot-draft9p4/source/` — 18 `.rst` pages and 587 frames for tutorials 1 to 8
- `.docs/experiments/runs/2026-09-08-draft9p4/log/` — eight `.jsonl` logs, 1,824 lines
- `.docs/experiments/runs/2026-09-08-draft9p4/reference/` — the shape read off draft9p1p6, as
  `*.faces.json`, `*.features.json` and `*.geometry.json`, plus `documents.json` and
  `variables.json`. These are read off the model and are not hand-edited.
- `.docs/experiments/runs/2026-09-08-draft9p4/scripts/` — 14 scripts. `p0_read.py` and the `p_*`
  set are the planning reads; `s1` through `s6` are the view and picking spikes.
- `.docs/build/plan/` — 15 tutorial sheets, the design source for each page

**Written but not committed:**

- `.docs/experiments/runs/2026-09-08-draft9p4/log/hinge.jsonl`, 580 lines, 39 step verdicts
- `instructions/stickbot-draft9p4/source/images/hinge/`, 208 frames from the tutorial 9 take
- edits to `constitution.md`, `.parts/onshape.md`, `09-hinge.md`, `notes.md` and
  `src/stickbot/onshape_gui.py`

**Not for committing, and listed here so they are not swept in:** the two `Image 8-*.jpeg` files,
the run7 and draft9p2 `capture/` trees, `process-map.md`, `retakes-changes.md`, `nord.sh.py` and
`nordvpn.conf`.

**Session scratch**, which is temporary and will age out with the session directory: renders of the
three feet and three hinges as `9p3.foot.bottom.png`, `9p4build.foot.bottom.png`,
`9p4check.foot.bottom.png` and the matching `.right` and hinge pairs. These are the pictures the
foot finding rests on. If they matter beyond this session they have to be copied into the run
folder.

## Lessons

**A picture of the working face is not optional, and it is not a nice-to-have.** The foot passed
every number we checked. It failed the first time anyone rendered the underside. The fix already in
the constitution is to name the features a part should have, pick a view that shows each one, and
render the part it was built from in the same views for a side-by-side look.

**Read the view cube before trusting a frame.** A wrong key press produced 15 frames captioned as
the sole that are all top views. The key is written into the page four times. Neither the writing
nor the review caught it, because both trusted the caption.

**A claim written at the end of a stage is written from memory.** `## Built` and `## Captured` are
composed after the work, often after a compaction, from whatever the summary carried. The take is
in the summary because it just happened. The check is not, because it never got logged. Anything
that is not logged as it happens is a claim, not a record.

**One document doing two jobs hides the second one.** Because the CAD, the frames and the
reproduction all happened in `stickbot-draft9p4-check`, there was no moment where the absence of a
second pass was visible. Two documents with two names only help if two different passes write to
them.

**Naming drift is a warning sign.** The document called `-check` became the one holding the build,
and the logs started calling it "the reader's document." That rename happened with no record, and
it is the same event as the missing gate.

## Paths forward

These are options, not a plan. They are roughly in the order they would have to happen.

**Correct the record first.** Amend the five tutorial sheets that claim a reproduction so they say
what is actually evidenced. Write the document-role swap into `plan.md`, either by making the
observed arrangement the specified one or by restoring the specified one. Neither is more honest
than the other; what is dishonest is the current gap between them.

**Fix the foot, then retake.** Task #215 turns the Depth arrow in both documents and republishes
`tutorial 8 - the foot`. Task #216 finds the real bottom-view key, corrects `shift+5` at
`foot.rst` lines 23, 781, 795 and 1157, rewrites the alt text on three frames, and retakes the 15
frames `groove-06` through `ribs-11`, plus `hero-02`, plus whichever of the 28 frames from
`socket.derive-01` onward show the foot's lower edge. A frame of a state the model no longer has is
a page defect, so the retake is part of the fix and not a follow-up.

**Prove the gate on one page before trusting it on fourteen.** The foot is the page to try, because
we now know what the right answer looks like. Drive `foot.rst` into a document that does not have
the answer, follow only what is written, log every step with the document id in it, and see what
the page actually produces. That result tells us whether the other seven pages need the same
treatment or whether the foot was singular.

**Finish tutorial 9 the way it was started.** The seven remaining features in
`stickbot-draft9p4-check` are small. The larger job after them is Phase W: `hinge.rst` written
fresh from the 208 new frames, replacing draft9p3's bump page, then a version in both documents and
the `## Built` and `## Captured` sections of `09-hinge.md`.

**Decide what stops a stage from closing.** Today a tutorial closes when its prose is written. A
check that a log exists naming the reproduction document is one grep, and it would have failed on
tutorials 4, 5, 6 and 8 on the day each was written. Where that check lives, and whether it is
advisory or blocking, is an open question.

**Consider whether tutorials 10 through 14 wait.** They are five tabs and five pages, and each one
built now inherits whatever the process still gets wrong. Closing the gate question first costs
less than five more pages that have to be re-proved.

## Open tasks that belong to this

- **#203** tutorial 9, the hinge, in progress
- **#204** to **#208** tutorials 10 through 14, in strict order
- **#209** Phase R, the register
- **#214** the head and body carry diff, to re-run once the settled rows are back
- **#215** the `sole groove` direction fix
- **#216** the bottom-view key and the retakes that follow
- Carried from earlier drafts and still open: **#27**, **#29**, **#60**, **#129**, **#139**,
  **#177**
