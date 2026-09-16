# 5. The head gains its socket

Starts from a finished joint. Ends with a head that can be mated to the torso.

**Short, and probably read as the tail of the tutorial before it.** It is its own file because the
tab changes.

## The steps

| Identifier | The move | `creates` |
| ---------- | -------- | --------- |
| `cad.parts.head.socket.mount_sketch` | a point where the socket sits under the head | `socket mount point` |
| `cad.parts.head.socket.derive` | bring the socket in from the joint studio | `get socket` |
| `cad.parts.head.socket.place` | move it onto the mount point, by connector, mouth down | `drop socket to neck` |
| `cad.parts.head.socket.combine` | union it into the head | `add socket to head` |
| `cad.parts.head.connector` | the head's mate connector | `head mate` |

**Two of these are repairs, not transcriptions.**

- **`drop socket to neck` carries a typed `dz = -22.15 mm` in stickbot.** It is the one place in
  the robot where a part is placed by a number nobody can read back, and a change to the torso or
  the joint would land the socket in the wrong place with no error. **draft9p0 is that change**:
  the correct offset is now **−43.4 mm**, and a typed −22.15 would have put the socket halfway up
  the head with every feature green. It is rebuilt as a connector-to-connector transform, like
  every other consumer.
- **`Boolean 1` is not a name.** It becomes `add socket to head`.
- **`head mate` is built from a turned view, not from the bottom view.** Every fixture the socket
  puts on its own axis lines up when the camera is on that axis: the cross slit's four traces and
  the derived socket's own `socket connect to robot`, which sits at (0, 0, -36) mm in front of the
  cavity. A pick there catches one of them, which is where draft9p3's 0.8 mm came from. Press
  **shift+7**, then the up arrow to drop under the head and the left arrow to swing the heading,
  and click the hollow from the side. The connector then holds the sphere alone and lands on
  (0, 0, -45) mm. The step loses its *hide `socket mount point`* instruction, which the turn makes
  unnecessary. Hold shift from the face across to the point as well, which is the habit the guide
  now teaches; it is not what cures this one, and it is what keeps the snap from wandering on
  every other connector. Proved on 2026-09-11; the six runs are in
  [the draft9p4 notes](../../experiments/runs/2026-09-08-draft9p4/notes.md) § *The socket's own
  axis is what puts `head mate` 0.8 mm off center*.

## The shots this tutorial needs by name

**Requirements in play.** `req.model.derive` — the joint is brought in from the studio that
owns it, never resketched here.

| Shot | Why a rule cannot produce it | Req |
| ---- | --------------------------- | --- |
| the derive dialog, with the other tab's part in the list | reaching into another tab is the new idea here | |
| the socket where the derive puts it — at the origin, inside the head | the frame that makes *why transform* land | |
| the same view after the rotate | half-right, and visibly so | |
| the same view after the place | right | |
| the two connectors the transform picks, medium and close-up with a ring | this is the alternative to the typed number, and it has to be legible | `req.shot.two_frame` |
| the union, before and after | a socket that was a separate body is now part of the head | |
| the tree, the version dialog | | |

**The three-frame arc — derived, rotated, placed — is the argument.** One frame of the finished
head shows nothing about why any of it happened.

## Built

**Document `stickbot-draft9p4`**
([`fe052e60`](https://cad.onshape.com/documents/fe052e606c96bb7cc5aaf59f)), version
**tutorial 5 - the head gains its socket** (`e0b8ff6eb4d8cc535fcfa525`). The five rows draft9p3
left in the `head` tab were taken back and built again by following the written page, step for
step.

**The tab ends with twenty-six features and one part.** The five this page adds are, in order,
`socket mount point`, `get socket`, `drop socket to neck`, `add socket to head` and `head mate`.
`head` has **47 faces** and measures x ±36 mm, y −33 mm to +30 mm, z **−48.2205 mm** to +36 mm. The
socket's hollow is a sphere of radius **6.08 mm** centered on **(0, 0, −46) mm**.

**`socket mount point` infers `CENTROID` on the head's flat underside**, which puts it on
**(0, 0, −36) mm** without a number being typed. That is the mount point the transform then drives,
and it answers the plan's open question above: the mount point is a mate connector on the face's
own middle, not a sketch point.

**`head mate` infers `CENTER` on the hollow.** It holds one entity and no secondary, and its origin
is **(0, 0, −46) mm** — the middle of the ball the socket will swallow. The tab ends with three
connectors: `socket mount point` and the derived `socket connect to robot`, both at (0, 0, −36) mm,
and `head mate` at (0, 0, −46) mm.

**`stickbot-draft9p4-check`**
([`86f40935`](https://cad.onshape.com/documents/86f40935a709a0748cdbb199)) carries its own version
**tutorial 5 - the head gains its socket** (`90e56de300ecea0cb2feaa1d`), taken where the page's
frames were shot. Read back side by side, the two documents agree on the feature list, the part
count, the face count, the bounding box, the cavity and all three connector origins.

## Captured

**`instructions/stickbot-draft9p4/source/head-socket.rst`**, written from the 42 frames in
`instructions/stickbot-draft9p4/source/images/head-socket/`, captured across 10 steps in
`stickbot-draft9p4-check`. `ninja check` comes back clean with no paragraph above grade 8, and
`src/stickbot/page_sweeps.py`'s sweeps come back clean: every frame on disk is used, every frame the
page names is on disk, no picture stands above its sentence, and every view key a step pressed is
named in the block that shows it.

**Four page-level corrections came out of the build rather than out of the plan.**

- **Boolean's box is labeled `Tools`, not `Parts`**, and `Keep tools` arrives **ticked** on the
  reader's path, because the reader's last Boolean is tutorial 4's `cavity from ball` and Boolean
  remembers what it was last left at. The page tells the reader to untick it, and says what the
  parts list reads when they have not: three rows, `head`, `Socket body` and `Part 3`.
- **The Derived panel lists only the *other* Part Studios**, and the caret at the left of
  `ball and socket` is not the same click as the name. The caret opens the studio and lists its two
  parts; the name would take the whole studio and bring the ball across as well.
- **`Shift+7` alone hides the socket behind the head.** The place step needs four presses of the up
  arrow after it to put the camera under the head.
- **The `Right` section plane cuts down one of the four relief slits**, so the close-up shows a
  white slot through the middle of the hollow. The caption says so rather than leaving it as an
  unexplained mark.

**Three deviations from this plan are recorded rather than carried.**

- The plan names the first step `cad.parts.head.socket.mount_sketch`; the log and the page use
  `cad.parts.head.socket.mount_point`, and it is a mate connector rather than a sketch.
- The plan's note carries draft9p3's `(0, 0, -45) mm` for `head mate` and, from earlier still,
  `-46.946 mm` for the head's lowest point. This draft measures **(0, 0, -46) mm** and
  **-48.2205 mm**. Those older numbers belong to draft9p3's own older socket.
- **Boolean's `Keep tools` had been left unticked in the build document** by the check run that
  preceded it, so the step's third frame had no click to photograph there. It is recorded as a
  deviation in the take log; the frame the page carries is the one shot in the check document,
  where the tick was there to undo.

## What we do not know yet

**Which two connectors the transform should pick.** The socket carries `socket connect to robot`;
the head needs one at the mount point. Whether that is the sketch point promoted to a connector or
a separate feature is a decision at the CAD.

**Whether the socket should be derived before the head's own geometry.** `foot` does it that way
and every other consumer does not. The question is settled once, for the whole robot, in
[`08-foot.md`](08-foot.md).
