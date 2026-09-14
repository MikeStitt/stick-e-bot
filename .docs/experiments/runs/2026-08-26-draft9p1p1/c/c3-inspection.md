# C3 — the model looked at, and the version cut

C1 and C2 are numbers. This is the gate that says somebody opened the robot and turned it round
before calling the draft done, and it is also where the version 9p2 starts from was made.

## The assembly, turned through six views

[`scripts/c3_open.py`](scripts/c3_open.py) opened the `stickbot` assembly on port 9223 and
[`scripts/c3_turn.py`](scripts/c3_turn.py) drove the view cube, pressing `f` to fit before each
frame. Screenshots are taken over CDP, because `page.screenshot` times out on Onshape.

| frame | what it shows |
| --- | --- |
| [`frames/c3-01-iso.png`](frames/c3-01-iso.png) | the robot as it opens, standing, arms down |
| [`frames/c3-02-front.png`](frames/c3-02-front.png) | both feet meeting at the middle, no gap and no overlap |
| [`frames/c3-03-right.png`](frames/c3-03-right.png) | the arms hanging clear of the hips |
| [`frames/c3-04-back.png`](frames/c3-04-back.png) | the heels and the back of the torso |
| [`frames/c3-05-left.png`](frames/c3-05-left.png) | the other side, and the same standoff |
| [`frames/c3-06-left-front.png`](frames/c3-06-left-front.png) | the left-front corner |

The robot stands, the arms hang, the feet meet, and nothing is inside out.

**The last frame is not the top view it was asked for.** The click that was meant to land on the
cube's Top face landed on a Left/Front corner, so the file was renamed for what it shows rather than
for what was intended. See [`../../../../.parts/onshape.md`](../../../../.parts/onshape.md)
§ *Discipline*: a frame is named after the nav cube, not after the click.

## The two shapes this draft changed

[`scripts/c3_parts.py`](scripts/c3_parts.py) asked `shadedviews` for each Part Studio at 700 × 700
with edges shown. These are renders from the server, so they carry no window furniture.

| | isometric | front | top |
| --- | --- | --- | --- |
| `ball and socket` | [iso](frames/c3-socket-isometric.png) | [front](frames/c3-socket-front.png) | [top](frames/c3-socket-top.png) |
| `gripper` | [iso](frames/c3-gripper-isometric.png) | [front](frames/c3-gripper-front.png) | [top](frames/c3-gripper-top.png) |

- The socket's front view shows the four slits running from the mouth clean out through the side of
  the collar, with no ring of material closing them off at the bottom. That is A1 as a picture, and
  [`c1-readback.md`](c1-readback.md) is A1 as a number.
- The gripper's top view shows the Ø18 collar sitting inside an 18 × 18 square and touching it at
  the middle of all four sides, with the four corners left proud. That is why the platform reads as
  four faces rather than one.

## The version

[`scripts/c3_ver.py`](scripts/c3_ver.py) opened **Create version…** from the document menu and
reported the dialog's fields; [`scripts/c3_cut.py`](scripts/c3_cut.py) typed the name and
description and clicked **Create**.

| | |
| --- | --- |
| name | `Recovery point` |
| id | `0f4e9b6b36b5c1a6f45197e1` |
| cut | 2026-08-28T04:30:08Z |
| the dialog, filled | [`frames/c3-version-typed.png`](frames/c3-version-typed.png) |
| the version, open | [`frames/c3-07-version-open.png`](frames/c3-07-version-open.png) |

Its description says what a reader arriving at it needs: `#collar` is re-based on the ball's center,
the relief slit is a slot for its whole depth, the gripper's clip top is flat and square, `#fit` was
driven and the robot stood 317.0000 at every value, and this is what draft9p2 starts from.

**The version's own link was opened and measured, not just clicked.** The page came up titled
"stickbot-draft9p1p1 | stickbot", and the assembly's bounding box read at `/v/0f4e9b6b…` gave the
same 317.0000 the workspace gives. A version that opens is not the same as a version that holds the
geometry, and this checks the second.

The document's versions now read:

| version | id | what it is |
| --- | --- | --- |
| `Start` | `8a5484206371ce199e41968f` | the copy of 9p1's `Recovery point`, before any edit |
| `Recovery point` | `0f4e9b6b36b5c1a6f45197e1` | after Phase B, measured by Phase C |

## The gates

| gate | met by |
| --- | --- |
| Model inspected | six views of the assembly and six renders of the two changed parts, above |
| Recovery point | `Recovery point`, `0f4e9b6b36b5c1a6f45197e1` |
| Links resolve | the version opened at its own URL and its assembly measured at 317.0000 |
