# Unmet — draft9p0, build b1

## The Onshape session ended mid-build, on 2026-08-24 — since recovered

**Resolved.** The user signed in again, the agent browser picked the session back up, and tutorial
12 was finished and published as `t12 gripper` (5324ccf7cef995c69366e6a6). What follows is the
account of the stall, kept because the recipe at the end is the one to follow next time.

`agent_browser.py` answers **"the borrowed cookies carry no session — sign in to Onshape in your
own browser, then run this again"**. It borrows its cookies from the signed-in browser, so the
sign-in has to happen there; restarting the agent browser cannot recover it, and it was restarted
once to confirm that.

**Where it stopped.** Half-way through `clip profile`, the first sketch of tutorial 12. Onshape put
up "Your Onshape session has timed out. Your document is saved.", cancelled the open sketch, and
swallowed the two circles that were being drawn into it. Nothing was lost that had been accepted:
the eight gripper variables and `copy socket` are all in the document, and `t11 l limb`
(b5617bfbc551a3949f4cf02a) is the last version.

**What it blocks.** Everything that needs the CAD:

- B1, from `clip profile` onward — tutorials 12, 13 and 14. All three were finished afterwards
- B2, reading the model back. Ran afterwards; [`b2-readback.md`](b2-readback.md)
- B3, driving `#torsoH` 96 → 120 → 96. Ran afterwards; [`b3-driving.md`](b3-driving.md)
- the frames for the guide's first five pages, which are still owed

**What it does not block.** A7, and all of D1–D3 for the tutorials that are built. Work continued
there.

**To resume.** Sign in to Onshape in the ordinary browser, then
`pkill -f agent_browser.py && uv run python tools/agent_browser.py`, reopen
`https://cad.onshape.com/documents/0f4b79a78707651ae20df5b2/w/d7b87030a78288b62a42de72/e/614e820e82591f54aad4a4eb`,
and carry on from the last accepted feature. That is what was done.

## The guide's first five pages started with no pictures

Tutorials 1 to 5 were built before any capture harness was running in this build, so `torso.rst`,
`head.rst`, `assembly.rst`, `ball-and-socket.rst` and `head-socket.rst` were written with no
figures at all. They were written anyway, from [`notes.md`](notes.md), because the words and the
numbers are the part that is expensive to recover.

**All five have since been shot**, four of them from a state the model had moved past:

- `ball-and-socket.rst` and `head-socket.rst` **have their heroes.** Nothing has touched the
  `ball and socket` tab since tutorial 4 or the `head` tab since tutorial 5, so what is in each tab
  today is exactly what its page ends on. Neither has step frames.
- `torso.rst` and `head.rst` **have their heroes too**, shot from a rolled-back tree. `torso.rst`
  wants the plain 72 × 48 × 96 block and the torso grew shoulders and studs in tutorial 6;
  `head.rst` wants the head before it had a socket and tutorial 5 gave it one. Both tabs were rolled
  back, shot, and rolled forward again, and both were read back through `bodydetails` afterwards to
  prove the bar went home — `body` to 20 faces and `head` to 47, matching
  [`b2-raw.json`](b2-raw.json). Both frames are cropped to the graphics area, because the feature
  tree behind them is the finished tree and not the tree a reader has at that point.
- `assembly.rst` **has its hero**, from a throwaway assembly. The `stickbot` assembly holds
  fourteen instances and an assembly has no rollback bar, so this one was built fresh with `body`
  and `head` both rolled back to where page 3 leaves them, giving `torso <1>`, `head <1>` and
  **Mate features (0)** — the page's own check list. The tab was deleted afterwards and the
  document's element list is back to what it was. Deleting a tab takes no confirming dialog.
- **None of the five has step frames**, only a hero apiece. That is what remains of this defect,
  and closing it is a re-run of the five pages rather than a repair — [the
  register](../register.md) says why under *What is still open*.

**How to drive the rollback bar**, which nothing in `tools/onshape_gui.py` or
[`onshape-gui-howto.md`](../../../../onshape-gui-howto.md) does yet:

- Right-click a feature row found with `gui.row` — not `common.jrow`, which wants `r.x < 250` and
  a row with no children — and pick **Roll to here**. The bar lands *after* the feature clicked,
  and the item is missing altogether when the bar is already there.
- **Roll to end** is on the bar's own context menu. The bar is `div.ns-list-item-rollbackbar`,
  about 190 × 7 px at the left edge of the tree.
- `common.menu2` finds neither item. A hand-written finder does, but the usual `r.x > 190` guard on
  a context-menu hit is too tight for **Roll to end**, which sits at about `x` 186. That miss is
  what left both tabs rolled back through a whole script, and it is silent — the menu simply
  stays open, so press Escape at the top of the next script.
- Face count is the test, and geometry is not always one: `head` has 47 faces both rolled to
  `head mate` and rolled to the end, because the trailing feature is a mate connector. The bar
  element is always in the DOM, so its presence is not a test either — only its position is.

The guide's index says which pages are in this state rather than leaving a reader to find out.

## The build published no version until t7

Pages 1 to 6 each end by publishing a version, and this build published none of them: the
document's version list runs `Start`, then `t7 head mated` through `t14 legs`. Nothing was lost —
the workspace carried everything forward — but a version is the one state a later run can open
read-only, so the states pages 1 to 6 describe had to be reached by rolling the tree back instead.
A build that publishes as it goes can shoot any earlier page whenever it likes, and can prove what
it shot. This one could not.

## Five captured frames could not be used

Listed with their reasons in [the register](../register.md), where the retakes are recorded
alongside them. All five have since been retaken and all five are now on a page. Three of the five
were the same mistake — a close-up framed without checking what was in the frame.

Two of them could not be fixed by reframing alone, because the state the step describes is not the
state the tab ends in. Both were shot with the tree rolled back, using the recipe under **How to
drive the rollback bar** above.

## Every figure was read against its caption, and three frames stay wrong

The audit is written up in [the register](../register.md). Twenty-one of the twenty-nine
mismatches were prose. Of the eight that needed the camera, five are retaken and three could not
be, for a reason worth keeping.

Retaken:

- **`torso-joints/connectors.medium.png`** — was byte-identical to `studs.combine.png`. Now the
  Front view its caption promises, with all five connectors selected and a triad on each ball.
- **`foot/connector.png`** — was byte-identical to `foot/hero.png`. Now the whole foot with the
  ring on `mate to robot` at the socket's ball center.
- **`u-limb/elbow_end.closeup.png`** — was framed so tight the fork was off screen and the ringed
  triad sat on bare rod. Panning the connector to the canvas center *before* zooming puts the slot,
  both ears and the ring in one frame.
- **`l-limb/tree.png`** — was cropped below the `Features (14)` header, so the caption's count was
  not in the picture. It is now.
- **`arms/hero.png`** — could not be retaken, see below, so the caption was rewritten to describe
  the pose the frame is actually in, and `pose.across.png` now names it rather than repeating it.

**Not retaken, because the state is not in the model any more:**

- **`arms/hero.png`** wants the robot with arms and no legs, arms down. `t13 arms` is the only
  legless state this build published and its saved pose is the same folded-across one, because a
  version stores the pose along with everything else.
- **`legs/hero.front.png`** and **`legs/knee.straight.png`** carry a stray **"Go to documents"**
  tooltip from a pointer left on the Onshape logo. Both are otherwise right, and both show a pose
  the workspace has since been dragged out of — `t14 legs` holds a stride, not the square stand.
- **`legs/pair.floating.closeup.png`** is a mid-build state — a limb pair floating before the hip
  mate — that was never published either.

**The lesson is that a pose is state, and this build treated it as scenery.** Geometry can be
recovered from a rolled-back tree; a pose cannot be recovered from anything, because dragging a
joint overwrites it and the version that could have held it is already published. A page that
shoots a pose has to shoot every frame it needs of that pose before it drags the next one, or
publish a version per pose.

**A version view cannot stand in for a workspace frame.** Opening `t13` or `t14` read-only puts a
*"Versions are view only"* banner across the top of the canvas, and there is no × on it.
