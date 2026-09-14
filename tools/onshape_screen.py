"""Where things are on Onshape's canvas: by reading the pixels, and by asking the GPU.

Two ways to answer the same question, and a capture needs both. Reading the frame
says where the ink *is* — after a dimension has moved what it did not pin, which is
not where the script drew it. Asking the GPU for the camera says where a model point
*will* land, which is what a pick has to aim at before anything is on screen to read.

Everything here is a question. Nothing in this module clicks; see `onshape_gui.py`.
"""

from __future__ import annotations

import io
from pathlib import Path

import numpy as np
from PIL import Image

# The agent browser runs at this size, and the insets below are measured against it.
# `onshape_gui.viewport` refuses to shoot a window of any other size, so a mask that
# silently covers the wrong pixels is not a failure mode this has to survive.
WINDOW = (1600, 1000)

# The graphics area, and where a freshly opened sketch puts the origin.
CANVAS = dict(x=246, y=76, w=1354, h=894)
CENTER = (923.0, 523.0)

# Never model, whatever color it is: the feature dialog, the view cube, the
# bottom-right icon strip.
CHROME = [(246, 76, 480, 310), (1425, 78, 1575, 265), (1480, 940, 1600, 1000)]

# A pixel has to differ by this much in some channel before it counts as changed.
# Below it is JPEG-ish noise and anti-aliasing on a redraw of the same picture.
NOISE = 12


def rgb(source) -> np.ndarray:
    """A frame as a (h, w, 3) uint8 array, from bytes or from a file."""
    if isinstance(source, (bytes, bytearray)):
        return np.asarray(Image.open(io.BytesIO(source)).convert("RGB"))
    if isinstance(source, np.ndarray):
        return source
    return np.asarray(Image.open(Path(source)).convert("RGB"))


def shot(page) -> np.ndarray:
    """The screen, straight into an array. No file, so nothing to name or clean up."""
    return rgb(page.screenshot())


def canvas_rect(page) -> dict:
    """The graphics area as the DOM reports it, rather than as measured once."""
    return page.evaluate(
        """() => {const r = document.querySelector('canvas').getBoundingClientRect();
            return {x: r.x, y: r.y, w: r.width, h: r.height};}"""
    )


# --- what a color means -------------------------------------------------------


def canvas_mask(im: np.ndarray) -> np.ndarray:
    """True where a pixel is allowed to be model ink."""
    m = np.zeros(im.shape[:2], bool)
    m[78:966, 248:1568] = True
    for x0, y0, x1, y1 in CHROME:
        m[y0:y1, x0:x1] = False
    return m


def is_sketch_blue(im: np.ndarray) -> np.ndarray:
    """Under-defined sketch geometry. Black is what a fully defined sketch turns.

    **Hide the default planes before counting this.** Their edges are drawn in the same
    blue, and they cover the same few hundred pixels whether a sketch is shown, hidden or
    open for edit, so a count taken over them is a reading of the planes. On a torso whose
    rectangle is fully defined the count came back 859 px with the sketch hidden and 693 px
    with it shown; with Top, Front and Right hidden it is 0 either way. `Default geometry`
    has no right-click menu of its own, so the three planes hide one at a time.
    """
    r, g, b = im[..., 0].astype(int), im[..., 1].astype(int), im[..., 2].astype(int)
    return (b - r > 70) & (b > 110) & (g < 160)


def is_selected_orange(im: np.ndarray) -> np.ndarray:
    """What a pick has hold of."""
    r, g, b = im[..., 0].astype(int), im[..., 1].astype(int), im[..., 2].astype(int)
    return (r > 190) & (g > 90) & (g < 200) & (b < 110)


def selected(im: np.ndarray) -> int:
    """How much of the model is selected, in pixels."""
    return int((is_selected_orange(im) & canvas_mask(im)).sum())


def extent(mask: np.ndarray) -> dict | None:
    """Bounding box of a boolean mask."""
    ys, xs = np.nonzero(mask)
    if not len(xs):
        return None
    x0, x1, y0, y1 = int(xs.min()), int(xs.max()), int(ys.min()), int(ys.max())
    return dict(x0=x0, x1=x1, y0=y0, y1=y1, w=x1 - x0, h=y1 - y0,
                cx=(x0 + x1) / 2, cy=(y0 + y1) / 2, px=int(mask.sum()))


def sketch_ink(im: np.ndarray) -> dict | None:
    return extent(is_sketch_blue(im) & canvas_mask(im))


def changed(before: np.ndarray, after: np.ndarray) -> int:
    """How many pixels differ between two frames, ignoring redraw noise."""
    d = np.abs(after.astype(int) - before.astype(int)).max(axis=2)
    return int((d > NOISE).sum())


# --- finding ink that has moved -----------------------------------------------
#
# A dimension moves what it has not yet pinned: in run 8p1 the stalk's top line
# dropped 0.44 mm when the arc radius went to 3, and a pick computed from where the
# line was drawn missed it. These ask the screen where the line is now.


def ink_rows(im: np.ndarray, x_px: float, y_lo: float, y_hi: float) -> list[int]:
    """Every row carrying sketch ink down a column, top to bottom."""
    m = is_sketch_blue(im) & canvas_mask(im)
    col = m[int(y_lo):int(y_hi), int(x_px) - 1:int(x_px) + 2].any(axis=1)
    return [int(y) + int(y_lo) for y in np.nonzero(col)[0]]


def ink_cols(im: np.ndarray, y_px: float, x_lo: float, x_hi: float) -> list[int]:
    """Every column carrying sketch ink along a row, left to right."""
    m = is_sketch_blue(im) & canvas_mask(im)
    row = m[int(y_px) - 1:int(y_px) + 2, int(x_lo):int(x_hi)].any(axis=0)
    return [int(x) + int(x_lo) for x in np.nonzero(row)[0]]


def first_ink(im: np.ndarray, x_px: float, y_lo: float, y_hi: float) -> int:
    """The topmost row of sketch ink down a column."""
    ys = ink_rows(im, x_px, y_lo, y_hi)
    if not ys:
        raise RuntimeError(f"no sketch ink down x={x_px} between {y_lo} and {y_hi}")
    return ys[0]


def runs(im: np.ndarray, y: int, predicate=is_sketch_blue) -> list[tuple[int, int]]:
    """Runs of matching pixels along one row, as (start, end) pairs."""
    row = predicate(im)[y] & canvas_mask(im)[y]
    out: list[list[int]] = []
    for i in np.nonzero(row)[0]:
        if out and i == out[-1][1] + 1:
            out[-1][1] = int(i)
        else:
            out.append([int(i), int(i)])
    return [tuple(r) for r in out]


def hits(im: np.ndarray, x_px: float, y_px: float, tol: int = 2):
    """Does a predicted pixel land on sketch ink along its own row?"""
    for a, b in runs(im, int(round(y_px))):
        if a - tol <= x_px <= b + tol:
            return (a, b)
    return None


# --- the camera, read off the GPU ---------------------------------------------
#
# Onshape draws the Part Studio with WebGL and hands the shader a model-view and a
# projection matrix. Wrapping the draw calls catches both, which turns a model point
# in millimeters into the pixel it will be drawn at — the only way to aim a pick at
# geometry that is not on screen yet to be measured.

HOOK = r"""
() => {
  if (window.__cam) return 'already';
  window.__cam = {seen: []};
  const grab = (gl) => {
    const p = gl.getParameter(gl.CURRENT_PROGRAM);
    if (!p) return;
    if (!p.__u) {
      p.__u = {};
      const n = gl.getProgramParameter(p, gl.ACTIVE_UNIFORMS);
      for (let i = 0; i < n; i++) {
        const u = gl.getActiveUniform(p, i);
        if (u.type === gl.FLOAT_MAT4) p.__u[u.name] = gl.getUniformLocation(p, u.name);
      }
    }
    if (!p.__u.uMVMatrix || !p.__u.uPMatrix) return;
    const mv = gl.getUniform(p, p.__u.uMVMatrix), pr = gl.getUniform(p, p.__u.uPMatrix);
    if (!mv || !pr) return;
    const vp = Array.from(gl.getParameter(gl.VIEWPORT));
    window.__cam.seen.push([Array.from(mv), Array.from(pr), vp]);
    if (window.__cam.seen.length > 400) window.__cam.seen.shift();
  };
  const wrap = (proto) => { if (!proto) return;
    for (const n of ['drawElements', 'drawArrays']) {
      const orig = proto[n]; if (!orig) continue;
      proto[n] = function(...a) { try { grab(this); } catch(e) {} return orig.apply(this, a); };
    } };
  wrap(window.WebGLRenderingContext && WebGLRenderingContext.prototype);
  wrap(window.WebGL2RenderingContext && WebGL2RenderingContext.prototype);
  return 'hooked';
}
"""


def hook(page) -> str:
    """Install the draw-call hook. Idempotent, and lost on every page load."""
    return page.evaluate(HOOK)


def _model_camera(seen):
    """The model's own camera among the frame's draws: full viewport, largest scale.

    Onshape draws the view cube and the origin triad with their own tiny viewports.
    Taking the last camera seen picks one of those about as often as not.
    """
    tally = {}
    for mv, pr, vp in seen:
        k = repr((mv, pr, vp))
        n = tally.get(k, (0, mv, pr, vp))[0]
        tally[k] = (n + 1, mv, pr, vp)
    full = [t for t in tally.values() if t[3][2] >= 1300 and t[3][3] >= 850]
    if not full:
        return None
    n, mv, pr, vp = max(full, key=lambda t: abs(t[2][0]))
    return dict(n=n, of=len(seen), mv=mv, p=pr, vp=vp)


def camera(page, nudge=True):
    """The model camera, or None if the canvas has not drawn since the last look."""
    page.evaluate("() => window.__cam.seen = []")
    if nudge:
        page.mouse.move(CENTER[0] + 3, CENTER[1] + 3)          # provoke a redraw
    page.wait_for_timeout(900)
    return _model_camera(page.evaluate("() => window.__cam.seen"))


def project(cam: dict, x_m: float, y_m: float, z_m: float) -> tuple[float, float]:
    """A model point in meters to a pixel, through P * MV. Column-major, orthographic."""
    mv, p = cam["mv"], cam["p"]
    e = [mv[0]*x_m + mv[4]*y_m + mv[8]*z_m + mv[12],
         mv[1]*x_m + mv[5]*y_m + mv[9]*z_m + mv[13],
         mv[2]*x_m + mv[6]*y_m + mv[10]*z_m + mv[14],
         mv[3]*x_m + mv[7]*y_m + mv[11]*z_m + mv[15]]
    c = [p[0]*e[0] + p[4]*e[1] + p[8]*e[2] + p[12]*e[3],
         p[1]*e[0] + p[5]*e[1] + p[9]*e[2] + p[13]*e[3]]
    w = p[3]*e[0] + p[7]*e[1] + p[11]*e[2] + p[15]*e[3]
    ndc = (c[0] / w, c[1] / w)
    vp, b = cam["vp"], CANVAS
    return (b["x"] + vp[0] + (ndc[0] + 1) / 2 * vp[2],
            b["y"] + (b["h"] - vp[1] - vp[3]) + (1 - ndc[1]) / 2 * vp[3])


def scale(cam: dict) -> float:
    """Pixels per millimeter."""
    return cam["p"][0] * cam["vp"][2] / 2 / 1000
