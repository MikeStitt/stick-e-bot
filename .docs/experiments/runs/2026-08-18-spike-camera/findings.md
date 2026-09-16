# Spike: reading the camera, instead of holding it still

Run on 9223 against a scratch document, `run7p2-spike-view`, on 2026-08-18. The question was
whether the harness can build at a comfortable zoom and shoot at a large one without re-deriving
the millimetre-to-pixel mapping every time the camera moves.

**It can, and the mapping never has to be derived from geometry again.** Onshape hands its own
view matrices to the GPU on every frame, and they can be read back. A pixel computed from them
lands where it was aimed, at a camera nobody planned.

## What was measured

**The camera is readable.** Onshape's renderer is WebGL on the page's main thread. Wrapping
`WebGLRenderingContext.prototype.drawElements` and reading the current program's `uMVMatrix` and
`uPMatrix` uniforms — plus `gl.getParameter(gl.VIEWPORT)` — gives the model-view and projection
matrices for that draw. `uPMatrix` is **orthographic**: a diagonal scale with no perspective
divide, which is why a sketch view is a plain uniform scale.

Several cameras draw into the same canvas. The view cube draws with an 11 x 11 viewport, and
screen-space overlays draw a full-viewport projection at about 0.001 px/mm. The model's matrix is
the full-viewport one with the largest scale.

**Pixels per millimetre falls out of the projection alone**, with no geometry to measure against:

    scale = uPMatrix[0] * viewport_width / 2      (and uPMatrix[5] * viewport_height / 2, equal)

**A pixel computed from those matrices is right.** With a Ø20 circle and a Ø4 marker circle at
+6 mm on the Front plane, after `f` and then three wheel notches in, anchored well off-centre at
(1100, 400), the camera read 50.6262 px/mm with the sketch origin at (889.4, 546.4). Measured off
that frame along y = 546:

| feature | predicted | measured |
| ------- | --------- | -------- |
| big circle, left edge | 383.1 | 382-383 |
| big circle, right edge | 1395.7 | 1394-1396 |
| marker circle, left edge | 1091.8 | 1091-1092 |
| marker circle, right edge | 1294.3 | 1293-1295 |
| marker circle, centre point | 1193.1 | 1190-1195 |

Every one lands inside the ink, at a camera reached by scrolling rather than by any rule.

**And it selects what it is aimed at.** Clicking the computed pixel selected the intended circle
at the fit camera and at the zoomed one, at the top, the left and the right of the Ø20 circle and
on the marker circle — ten clicks, each one hovered first and checked against the orange it left.

**The click that first looked like a miss was a deselect.** A click on an entity that is already
selected turns it off, and a selection survives a wheel zoom. The spike's first pass selected the
circle at the fit camera, zoomed, and clicked the same circle again: the frame came back with no
orange anywhere, which is also what a miss looks like. Clicking empty canvas before each measured
click makes the two tell apart, and then nothing failed.

## Zoom to fit is exact arithmetic, not a rescale to be recovered from

`f` scales the bounding box by **1.05** and fits that into the canvas, then centres it:

    scale = min(canvas_w / (1.05 * bbox_w), canvas_h / (1.05 * bbox_h))
    origin_px = (923 - bbox_centre_x * scale, 523 + bbox_centre_y * scale)

Confirmed against the projection matrix in both branches, on a 1354 x 894 canvas: a Ø20 circle
reads 42.5714 px/mm, and 894 / (1.05 * 20) = 42.5714. A 100 x 10 rectangle reads 12.8952, and
1354 / (1.05 * 100) = 12.8952. The 5% is the whole of it — there is no fixed pixel margin.

This corrects the number the harness has been using. `852 / size` treats the margin as a constant
42 px, which is right to a pixel when the height binds and wrong by 26 px when the width does.
The two builds that used it were both height-bound, which is why nothing went wrong.

**`f` returns to the same camera exactly.** Fit, scroll three notches in, fit again: 42.5714 px/mm
with the origin at (923.0, 523.0) both times, and the same computed pixel selected the same circle
both times. It is a home to come back to, not an approximation.

## One wheel event is a semitone

Three wheel events took the scale from 42.5714 to 50.6262, a ratio of 1.18921 — and a single
event of the same `deltaY` gave 1.05946. So each event multiplies the scale by **2^(1/12)**,
1.059463, and twelve notches double it. The magnitude of `deltaY` did not change the step: −260
in one event moved the same distance as −260 would in any other.

That makes zoom an exact instrument. To go from the fit scale to a chosen one, the number of
events is `round(12 * log2(target / current))`.

## What forces recalibration, and it is not `f`

Two things move the mapping without anybody asking:

- **Sketches stay shown after they are created.** Four sketches built in one studio all render at
  once, so `f` frames their union and every new sketch changes the scale of the old ones. In this
  spike a Ø20 circle came back at 12.95 px/mm rather than 42.57, because a 100 mm rectangle from
  two sketches earlier was still on screen.
- **`n` came back on the Back side.** The view cube read `Back` and the sketch's own name rendered
  mirrored, so sketch +x pointed left. A marker entity off to +x makes the frame say which way it
  went; the view cube's face label says the same thing.

## What is not established

- **Nothing here was tried in a 3D view.** The projection is general and the model-view carries the
  rotation, so picking a face by computed pixel should work the same way; it has not been done.
- **The hook is unsupported.** It reads uniforms Onshape names today. A build that renames
  `uMVMatrix` breaks it silently, so anything relying on it should assert a known point projects
  where it should before trusting the rest.

## Scripts

`vs1.py` through `vs7.py` and the harness `v.py`, in the session scratchpad, with the camera
hook and the projection in `cam.py` and the frame measurements in `meas.py`. `v.py` reads frames
with pillow and numpy: `blue_ink` for the active sketch's extent, `runs` for one row, `hits` for the
assertion, `orange_pixels` for what is selected.

An earlier pass hand-rolled a PNG decoder in `zlib` and `struct`, because `import numpy` failed and
that was taken to mean the environment had no image libraries. **Pillow was already a declared
dependency.** The hand-rolled reader gave the same answers and took about 30 seconds a frame
against 0.11 seconds for the whole set. Numpy was added on 2026-08-18.
