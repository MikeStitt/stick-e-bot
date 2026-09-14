# Spike: driving, photographing and checking a sketch circular pattern

Run on 9223 against the scratch document `run7p2-spike-view` on 2026-08-18, with a CDP
screencast running through all six stages. The question was whether the step that guide3
dropped can be taught: it opens no dialog, has no green tick, and its only control is a
two-character tag floating in empty space.

**It can, and none of the three routes to the tag needs a picture to be read back.** The
canvas cursor says whether a pattern is pending, the count box is an ordinary DOM input,
and the committed count is a number in the sketch's own JSON.

## What the tool does, in order

Selection first, then the tool — Onshape's help says so and the run confirms it. A seed
rectangle drawn with **Center point rectangle**, its sides picked, then **Circular
pattern** invoked from the tool search. The pattern arrives already made, with **three**
instances at 120°: a dash-dot circle through them, a pivot square on the origin, an angle
arrow, and a small `3x` tag at the end of a thin leader line off the seed's anchor corner.
Every pixel clicked in this spike was computed from the GPU camera read in
[`../2026-08-18-spike-camera/findings.md`](../2026-08-18-spike-camera/findings.md); no
calibration geometry was drawn.

## The cursor is the state, and it is readable

    getComputedStyle(canvas).cursor

reads `.../cursors/Confirmation_Cursor.png` everywhere on the canvas while a pattern is
pending — that is the "mouse with a green button" the help describes — and `default` once
the pattern is accepted. While pending it is also `default` over the count tag, and over
nothing else nearby.

So the harness gets three things from one page read: whether a pattern is waiting to be
accepted, whether the accept took, and which of several small marks is the tag.

## The count box is a DOM input, and `Control+A` is not select all

Double-clicking the tag opens a real `input:visible`, 100 x 26 px, holding the current
count. `fill()` and `input_value()` both work, which is what `tools/gui_steps.py` already
insists on for every numeric field.

This spike ignored that and typed instead: `Control+A` then `4`. On macOS `Control+A` is
line-start, not select-all, so the field became `43` and the pattern committed at 43
instances with no complaint from anything. The recovery was route B below, which is how
that route came to be tested on a real mistake rather than a staged one.

## Three routes to the count

**A — hunt the tag.** Find the small dark marks near the seed, hover each, and keep the one
that answers: the tag lights a tan pill (482 px of it) and turns the confirmation cursor
off. It works, and it is the most fragile of the three: the tag is about 19 x 12 px, and
the dark cluster it belongs to merges with its own leader line, so the cluster's center is
27 px to the left of the text. Aim at the middle of the highlight, not the middle of the
cluster.

**B — Show constraints on, right-click the pattern glyph.** The glyph is a five-dot icon in
a white box, and with constraints shown it sits in a row of them: 24 px from a horizontal
constraint, 47 px from a perpendicular one, all three boxes touching. That is the burial.
Right-clicking it opens a **DOM context menu** at the click point — *Confirm seed | Edit
pattern | Copy sketch | Show all | Curve/surface analysis… | Select | Select other… | Zoom
to fit | View normal to sketch plane | Delete sketch entity* — and
`get_by_text("Edit pattern", exact=True)` resolves to exactly one node.

**C — Show constraints off, hover any patterned entity.** With the glyphs hidden, a 400 x
320 px box around one instance holds **zero** dark marks. Hovering that instance's long
side adds **exactly one**, and it arrived between two screencast frames 63 ms apart. It
survived a five-step walk from the edge to the icon, and the right-click gives the same DOM
menu.

**Route C is the one to teach and the one to automate.** A single-frame diff finds the icon
with no template, no text search and no knowledge of where it will appear, and the reader
gets a gesture that works on any instance rather than a hunt for a two-character label.

## The check that replaces the missing tick

Closing the sketch and reading the feature back gives the whole pattern as one constraint:

| parameter | reads | what it is |
| --------- | ----- | ---------- |
| `constraintType` | `CIRCULAR_PATTERN` | one per pattern in the sketch |
| `patternc1` | `4` | the instance count |
| `localInstance2,0`, `3,0`, `6,0` | `….top`, `….left`, `….right` | the seed entities |
| `labelDistance`, `labelAngle` | `0.001625 m`, `-0.2008 rad` | where the tag sits |
| `openPattern` | `false` | full circle rather than a swept angle |

That table caught a second mistake nobody could see. The seed list has **three** entries,
not four: one of the four shift-clicks on the rectangle's sides missed, so the pattern
copies three sides. Every feature state reads `OK`, the sketch closes clean, and the only
thing on screen that says otherwise is that each copy is drawn with three sides instead of
four. Counting the seeds and the count is one check that catches both the wrong number and
the wrong selection.

`labelDistance` and `labelAngle` mean an existing pattern's tag is computable from the API
rather than hunted for, which is a better route back into a pattern than route A.

## What this asks of the process

- **`gui_steps` needs a `dblclick`**, and a rule for canvas picks: the orange must increase
  after every one. The missed side above would have failed that check on the spot.
- **A screencast for the agent's own browser.** `rec.py` writes every CDP frame to disk with
  its arrival time and a `mark()` line in the same clock. The 63 ms and the walk are
  measurements off those frames; neither is visible in a screenshot taken afterwards.
- **The human recorder still cannot see this step.** `recorder.py` keeps frames on dialog
  and feature events, and this step raises none. It wants `dblclick` and "a text input
  appeared over the canvas" as triggers.
- **A rule for every step with no dialog:** a figure zoomed enough to read the target, a
  sentence saying how the reader knows it worked, and an API read-back in the build.

## Not established

- **Escape.** The retro says it discards a pending pattern silently. Not retested here.
- **Whether the tag's default position is stable.** `labelAngle` was `-0.2008 rad` in this
  one run.
- **The feature-level circular pattern** is a different tool with a real dialog, and none of
  this applies to it.

## Scripts

`cp1.py` through `cp6.py` in the session scratchpad, with `find.py` for the dark-mark
finder, `rec.py` for the screencast, `cam.py` for the camera read and `meas.py` for the
frame measurements. The six stages wrote about 380 frames and 36 MB of jpeg, which stayed
in the scratchpad.
