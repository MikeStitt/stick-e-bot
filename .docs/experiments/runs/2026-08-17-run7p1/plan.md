# Run 7p1 — shoot guide3's ball and socket figures

Run 7 built the joint and wrote
[`instructions/robot-guide3/source/ball-and-socket.rst`](../../../../instructions/robot-guide3/source/ball-and-socket.rst)
from the model. The page's words are done. Its pictures do not exist. This run makes them.

The page names every image it wants, so the shot list is the page:

```sh
grep -oE 'images/[a-z0-9-]+\.png' instructions/robot-guide3/source/ball-and-socket.rst
```

Nothing here restates that list. If a slug changes, the command still answers.

## Why a new build rather than a re-pick

[Run 7's plan](../2026-08-16-run7/plan.md) settles this under **What the figures show**: F1 and F2
rule out the run 6 pool, because those frames were shot with the default planes on and the shape
small. The run 7 frames are no better — they are the harness debugging itself, wrong framing,
several of states the page does not teach, and a few of the **Through all** cut that was replaced.

Most of the page's steps are mid-sketch — *the arc drawn*, *the three lines closing the loop*, *the
first bar drawn across the collar*. Those states exist only while a sketch is open, so they cannot
be recovered by rolling a finished tree back. The build has to happen again, with the camera aimed.

## Where the work is

A new Onshape document, `run7p1-ball-and-socket`, built on port **9223**. Frames land in
`instructions/robot-guide3/source/images/` under the names the page already uses.

## What has to be true of every frame

Carried from run 7's F-rules, and the reason this run exists:

| | Rule |
| --- | --- |
| F1 | **P** before every sketch shot. Planes on means three grey rectangles behind geometry a few millimeters across |
| F2 | **Shift+7**, **P**, **F** as one habit, so the shape is large and solid-looking in every figure |
| F3 | Caption and picture are the same moment. The page puts its instruction *above* the image, so the check is instruction-against-frame |
| F4 | Alt text and slugs carry the cross-section naming |

F2 is the one that shapes the harness. A canvas click is in pixels; `f` moves the millimeter-to-
pixel mapping under it. Run 7's [spike F](../2026-08-16-run7/plan.md#spike-f--answered-one-calibration-per-sketch-fit-only-to-shoot)
measured the way out:

- the default camera puts the origin at the canvas centre at 3.6066 px/mm on a 1354 x 894 canvas;
- after `f` the mapping is `s = min((W − 42)/w_mm, (H − 42)/h_mm)` px/mm with the model's bounding
  box centre on the canvas centre, predicted twice and measured twice to within a pixel.

So the mapping is computable at every moment of the build, because this run chooses the geometry
and therefore knows the bounding box. That is what lets `f` be pressed between clicks instead of
only before a screenshot.

## Settle first

**S-A — can the harness fill a feature dialog's name box?** The page tells the reader to type the
feature's name into the dialog header *before* the green tick (run 7's S13), and two frames show
exactly that — `bs-11`, `bs-20`, `bs-37`. Run 7's H4 found that a double-click at (277, 93) never
focused an input and every letter ran as a sketch shortcut. If a different route focuses it, the
frames are honest. If nothing does, the page's instruction and its frames have to part company, and
that is a page change, not a capture trick — surface it rather than shooting the tree-menu rename
and captioning it as the header.

**S-B — the two overview figures.** `bs-00-ball-stud` and `bs-00-socket-collar` are not steps. The
first is the finished stud alone. The second is the collar cut open, which needs a section view.
Settle how both are made before the build, because the second may want a Section view in the GUI
rather than a render.

## The build, and where the frames fall

Same fifteen features as run 7 — the model is not being redesigned. Read the recipe off the run 7
model rather than retyping it here; every expression on the page came from that read-back.

| Feature | Frames |
| --- | --- |
| units, eight variables | `bs-01` … `bs-03` |
| `stud profile` sketch | `bs-04` … `bs-11` |
| `revolve stud`, part `Ball stud` | `bs-12` … `bs-15` |
| `collar profile` sketch | `bs-16` … `bs-20` |
| `collar blank`, part `Socket body` | `bs-21` … `bs-25` |
| `cavity from ball` boolean | `bs-26` … `bs-30` |
| `slit profile` sketch | `bs-31` … `bs-37` |
| `relief slits` extrude | `bs-38` … `bs-43` |
| the finished tree, and the version | `bs-44`, `bs-45` |

## Harness rules carried forward

From run 7's H-table, and they are constraints on the script, not on the page:

| | Rule |
| --- | --- |
| H4 | Rename through the tree row's context menu — unless S-A says otherwise |
| H5 | Arm a sketch tool through **Search tools**, not its letter. The letter toggles. The frame is the same either way, because it shows the armed toolbar and not the route to it |
| H6 | Never send a bare `f` while a field has focus |
| H7 | An entity hidden behind a solid does not highlight and does not pick |
| H8 | Place a dimension label clear of the model |

## Floor and ceiling

**Floor.** Every image the page names exists, at 1354 x 894 or larger, and Sphinx builds the page
with no missing-image warning.

**Ceiling.** The frames are checked against the instruction above each one, not merely present —
run 7's F3, and the audit that task #26 asks for on guide2.

**Recovery point.** A published, named version of `run7p1-ball-and-socket`, cited by the page in
place of `run7-ball-and-socket-v1`.

## What this run does not do

It does not edit `robot-guide2`, it does not change the model, and it does not amend the
Constitution or its parts. If a frame cannot be shot as the page describes it, the page changes and
the change is reported — not the caption.
