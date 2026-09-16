# Run 2 — 2026-08-11

The second agent build of the robot's parts, and the first run to work from written briefs
rather than from a conversation. **Frozen.** The three Onshape documents below are published at
named versions; cite those, not the workspaces.

Run 1's results are in [`../2026-08-11-run1/`](../2026-08-11-run1/). Read it first if you want
to know why run 2's briefs say what they say.

## What was built, and where it is

| Directory | Onshape document | Published version |
| --------- | ---------------- | ----------------- |
| `ball-and-socket/` | `ball-socket-run2` `b58c15803eb989fe3f676150` | `v1-ball-and-socket` — `278e2c9bf3329c2d7f1244f4` |
| `hinge/` | `hinge-run2` `2348323d25181f7cb2a9aa9b` | `stage-2-detents` — `474270a65596f317b77999cd` |
| `lesson-test/` | `lesson-run2` `ca8494ebddc1d41126fd580e` | `run2-session1-complete` — `24dafb83c2f7814714e20c7e` |

Version link form: `https://cad.onshape.com/documents/<did>/v/<vid>/e/<eid>`. Element ids are in
each directory's `build-notes.md`, under *Where the work is*.

Each directory holds `build-notes.md`, a `steps.log` written one line before and one line after
every action, and the screenshots: 119 for the ball and socket, 255 for the hinge, 204 for the
lesson.

## What run 2 established

- **Boolean → Subtract with Offset applies uniformly over a sphere.** The socket mouth measured
  Ø5.802586 against Ø5.803 predicted. The whole joint design rests on this, and it holds.
- **The slice fork fits.** Both hinge parts measure 12.000 across X and Y, so every layer of the
  fork runs out to the limb's own surface and no corner stands proud.
- **The lesson builds and measures right** — eyes r5.0000, mouth 20.000 overall, neck Ø12.000.
- **Rendering each part alone catches what numbers miss.** The ball-and-socket agent rendered
  the socket on its own and found the relief slits were 2.7 mm deep where the brief said 5.5.
  Every acceptance number had passed.

## What run 2 cost, and what it changed

Six errors in the briefs were found by building them. Most were stale numbers carried from a
superseded revision — a driver changed and the numbers derived from it did not. All six were
corrected **after** this run, so **no build in this directory was made from the current text.**
Run 3 is the first test of it.

Acceptance checks were strengthened in the same pass. A slit came out half depth and every
check still passed, so the briefs now ask for the z-extent of cut faces and the thinnest wall
anywhere in the part, not just the headline dimensions.

The GUI knowledge from these three builds was folded into
[`../../onshape-gui-howto.md`](../../onshape-gui-howto.md), which is what stops the next agent
paying 350–525k tokens to rediscover it.
