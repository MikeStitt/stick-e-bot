"""The figures for the hinge review, drawn from the numbers that build the hinge.

    uv run --project . python .docs/reviews/hinge/make_figures.py

Every length here is the joint as this review found it, frozen in `J` below. It used to be read
live out of `instructions/robot-guide/make_plans.py`. That stopped being right on 2026-09-04, when
the printed joint was measured and the detent mechanism was replaced: a review reads what it
reviewed, and a design source moves on. The spring answers are still solved rather than typed, by
`tools/hinge_spring.py` against `J`, which reproduces both of this review's headline numbers
exactly. The two frames that are photographs of the
model come from the shaded views taken during the sweep; they are annotated in millimeters of the
model, and the mapping from millimeters to pixels is measured off the frame's own ink rather than
guessed.

Reading the drawings: the pin axis is the origin of every section, the fork's own limb is up the
page and the blade's own limb is down it, which is how the frames sit as well.
"""
import base64
import math
import os
import types
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[2]
IMAGES = HERE / "source" / "images"
# Rendered frames of the joint, read rather than written. They are capture, so
# they live in a session scratchpad and never in this tree; the session that made
# them is gone. Set HINGE_FRAMES to a directory holding them, or the two figures
# that use them will fail with a clear missing-file error.
FRAMES = pathlib.Path(os.environ.get("HINGE_FRAMES", "/nonexistent/hinge-frames"))

from stickbot import make_plans as mp  # noqa: E402

from stickbot import hinge_spring  # noqa: E402

from stickbot.make_plans import circle, mm, rect, text  # noqa: E402

# ------------------------------------------------------------------ the numbers
#
# Names the review uses, all of them derived. The hinge Part Studio holds each part with a stub of
# its own limb on it, EAR long, and the pin on the origin; that is where END_FORK and END_BLADE
# come from. RULE_OUT is what the comment beside BLADE_OUT derives: the blade's own limb has to
# end NOSE from the pin or the fork's ear tips, which sweep NOSE, cannot pass it.

# The joint this review is about, frozen. It is the tooth-and-valley detent as it stood in
# stickbot-draft9p1p2 and stickbot-draft9p1p4, which is what was printed, measured and then
# replaced. Nothing here reads the design source, because the design source no longer holds this
# joint. See the note at the head of the page.

J = types.SimpleNamespace(
    LIMB=24.0, BLADE=10.0, SLIT=4.0, LEAF=3.0, GAP=0.15, SEAT=10.3, EAR=6.85,
    STUB=4.0, STUB_PROUD=1.30, BORE_D=4.4, NOSE=12.0, BLADE_OUT=32, SLOT_DEEP=33,
    TEETH=24, STEP=15, VALLEY_D=1.70, TOOTH_FLAT=0.8, CONE_D=2.00, TOOTH_PROUD=0.60,
    CLIMB=0.45, TAB_FREE=20, EAR_FREE=21, ROD_FORK=17, ROD_BLADE=18,
    ENGAGED=1.15, ARM_DROOP=26, PETG_YIELD=hinge_spring.YIELD_PETG)
J.FLAT = math.sqrt((J.LIMB / 2) ** 2 - (J.SEAT / 2) ** 2)      # 10.8387
J.LIMB_FLAT = 2 * J.FLAT                                        # 21.6774
J.BUMP_R = J.FLAT - 1 - J.CONE_D / 2                            # 8.8387


def reviewed(tab_free=None, ear_free=None, slit=None, proud=None):
    """The reviewed joint as a spring, with its two roots wherever you ask for them."""
    leaf = (J.BLADE - (J.SLIT if slit is None else slit)) / 2
    return hinge_spring.Hinge(
        limb=J.LIMB, blade=J.BLADE, leaf_root=leaf, leaf_tip=leaf, gap=J.GAP,
        tab_free=J.TAB_FREE if tab_free is None else tab_free,
        ear_free=J.EAR_FREE if ear_free is None else ear_free,
        blade_out=J.BLADE_OUT, ring_r=J.BUMP_R, ring_n=J.TEETH, climb=J.CLIMB,
        stub_proud=J.STUB_PROUD if proud is None else proud,
        nose=J.NOSE, flat=J.FLAT)


_H = reviewed()
J.PRESS_F, J.EAR_STRESS, J.LEAF_STRESS = hinge_spring.press(_H)
J.PRESS_F /= 9.81                            # kgf, which is what this review speaks in
J.HOLD_T, J.HOLD_TEETH = hinge_spring.hold(_H)[:2]
J.HOLD_HAND = J.HOLD_T / 150 / 9.81

NOSE, EAR, LIMB = J.NOSE, J.EAR, J.LIMB
HALF = J.BLADE / 2                         # the tongue, half of it
SEAT = J.SEAT / 2                          # the ear's inner face, all of it, and the bore's
                                            # mouth is in it
BORE_R, STUB_R = J.BORE_D / 2, J.STUB / 2

END_FORK = J.SLOT_DEEP - NOSE + EAR        # 27.8 — the fork's end face, from the pin
END_BLADE = J.BLADE_OUT - NOSE + EAR       # 26.8 — the blade's end face, from the pin
ELBOW = END_FORK + END_BLADE                # 54.6 — the joint end to end

RULE_OUT = 2 * NOSE                         # 24 — what the comment derives for BLADE_OUT
RULE_DEEP = RULE_OUT + 1                    # 25 — and for SLOT_DEEP

ROOT_FORK = J.EAR_FREE                     # 21 — slot root, from the pin
ROOT_BLADE = J.TAB_FREE                    # 20 — tongue root, the same way
ROOT_OLD = NOSE                             # 12 — where the limb's rod used to root both

BURIED_FORK = ROOT_FORK - ROOT_OLD          # 9 — slot the rod used to fill back in
BURIED_BLADE = ROOT_BLADE - ROOT_OLD        # 8 — tongue the rod used to fill back in

ENGAGE = J.ENGAGED                         # 1.15 — how deep the axle sits in its bore
SHEET_ROOT = J.SLOT_DEEP                   # 33 — where the plan sheet used to draw the slot root


def at_roots(tab_free, ear_free, slit=None, proud=None):
    """The joint's press force and detent torque with its two members rooted where you say.

    Everything else is the settled design. Strength is a section property and does not move when a
    root moves; stiffness goes as one over the cube of the free length, which is the whole reason
    this function takes those two numbers and nothing else.
    """
    h = reviewed(tab_free=tab_free, ear_free=ear_free, slit=slit, proud=proud)
    press, ear_mpa, leaf_mpa = hinge_spring.press(h)
    torque = hinge_spring.hold(h)[0]
    return press / 9.81, ear_mpa, leaf_mpa, torque


def solid_press():
    """What a tongue with no slit in it would take to press together, in kgf.

    The tongue is then one beam of the whole Ø LIMB slice between the two faces, and it is stiffer
    than the ear by two orders, so the ear gives the whole climb on its own. Modeled by handing the
    solver a leaf that is the whole tongue and halving nothing.
    """
    h = reviewed(slit=1e-6)
    h.leaf.ei = [1e12] * len(h.leaf.ei)     # rigid, which is what "solid" comes to here
    return hinge_spring.press(h)[0] / 9.81


def crush(proud):
    """What it takes to tear the axle back out of its bore, in kgf.

    The failure is the ear shearing round the bore's mouth, so the area is the bore's own
    circumference times how much axle is engaged.
    """
    return (math.pi * J.BORE_D * (proud - J.GAP) * hinge_spring.SHEAR_PETG) / 9.81


# ------------------------------------------------------------------ drawing
#
# make_plans' own style, plus the few classes a review needs that a plan sheet does not: material
# the rod adds, a callout that says something is wrong, and one that says something is right.

STYLE = mp.STYLE + """
  .rod   { fill:#f3e6d8; stroke:#1d262e; stroke-width:0.9; stroke-linejoin:round; }
  .bad   { fill:#b8156e; font-size:3.6px; font-weight:700; }
  .good  { fill:#0b6e86; font-size:3.6px; font-weight:700; }
  .head  { fill:#12303c; font-size:5.4px; font-weight:700; letter-spacing:0.04em; }
  .sub   { fill:#43525e; font-size:3.8px; }
  .arrow { stroke:#b8156e; stroke-width:0.7; fill:none; }
  .conn  { stroke:#0b6e86; stroke-width:0.8; fill:none; }
  .connd { fill:#0b6e86; font-size:3.6px; font-weight:700; }
"""


def svg(body, x, y, w, h, scale=5.2):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x:g} {y:g} {w:g} {h:g}" '
            f'width="{int(w * scale)}" height="{int(h * scale)}" '
            f'font-family="ui-monospace, Menlo, monospace">'
            f"<style>{STYLE}</style>{''.join(body)}</svg>")


def tick(x, y, up=True):
    """The slash a drawing puts where a dimension line meets its extension line."""
    d = 1.6
    return f'<path class="dim" d="M {x - d:g},{y + d:g} L {x + d:g},{y - d:g}"/>'


def vdim(x, y0, y1, label, side=1, ext=None):
    """A vertical dimension at x, between y0 and y1, with its text beside the line."""
    parts = [f'<path class="dim" d="M {x:g},{y0:g} V {y1:g}"/>', tick(x, y0), tick(x, y1)]
    for y in (y0, y1):
        if ext is not None:
            parts.append(f'<path class="dim" d="M {ext:g},{y:g} H {x:g}"/>')
    parts.append(text(x - 3.4 * side, (y0 + y1) / 2, label, "dimt", "middle", rot=-90))
    return "".join(parts)


def hdim(y, x0, x1, label, ext=None, below=False):
    parts = [f'<path class="dim" d="M {x0:g},{y:g} H {x1:g}"/>', tick(x0, y), tick(x1, y)]
    if ext is not None:
        for x in (x0, x1):
            parts.append(f'<path class="dim" d="M {x:g},{ext:g} V {y:g}"/>')
    parts.append(text((x0 + x1) / 2, y + (4.6 if below else -1.8), label, "dimt", "middle"))
    return "".join(parts)


def arrow(x0, y0, x1, y1):
    a = math.atan2(y1 - y0, x1 - x0)
    w = 1.5
    return (f'<path class="arrow" d="M {x0:g},{y0:g} L {x1:g},{y1:g}"/>'
            f'<path class="arrow" fill="#b8156e" d="M {x1:g},{y1:g} '
            f'L {x1 - 4 * math.cos(a) + w * math.sin(a):.3f},'
            f'{y1 - 4 * math.sin(a) - w * math.cos(a):.3f} '
            f'L {x1 - 4 * math.cos(a) - w * math.sin(a):.3f},'
            f'{y1 - 4 * math.sin(a) + w * math.cos(a):.3f} Z"/>')


def pin_axis(y0, y1):
    return (f'<path class="ctr" d="M 0,{y0:g} V {y1:g}"/>'
            f'<path class="ctr" d="M {-LIMB:g},0 H {LIMB:g}"/>')


# ------------------------------------------------------------------ the joint in section
#
# One ear, rooted where the caller says. The tip is rounded on NOSE about the pin like every other
# end on the robot, which is what makes the two members interchangeable at the joint.

EY = math.sqrt(NOSE**2 - SEAT**2)           # where the ear's round tip meets its inner face
BY = math.sqrt(NOSE**2 - HALF**2)           # and where the blade's meets its side


def ear(sx, root):
    """One ear. Its inner face is one plane from the root to the round tip.

    That face is both what the tongue seats on and what the bore's mouth is in. It carried a
    raised land before, with the rest of the slot relieved 0.45 further out; the face is drawn
    at SEAT the whole way now because that is where it is.
    """
    return (f'<path class="part" d="M {sx * SEAT:g},{root:g} L {sx * NOSE:g},{root:g} '
            f'L {sx * NOSE:g},0 A {NOSE:g},{NOSE:g} 0 0 {1 if sx > 0 else 0} '
            f'{sx * SEAT:g},{EY:.4f} Z"/>')


def fork(root, end):
    """Both ears rooted at `root`, and the fork's own limb from there to `end` up the page."""
    return (ear(-1, root) + ear(1, root)
            + rect(-NOSE, end, LIMB, root - end)
            + rect(-NOSE, -BORE_R, NOSE - SEAT, 2 * BORE_R, "void")
            + rect(SEAT, -BORE_R, NOSE - SEAT, 2 * BORE_R, "void"))


def blade(root, end):
    """The tongue from its nose down to `root`, and the blade's own limb from there to `end`."""
    return (f'<path class="mate" d="M {-HALF:g},{root:g} L {-HALF:.4f},{-BY:.4f} '
            f'A {NOSE:g},{NOSE:g} 0 0 1 {HALF:.4f},{-BY:.4f} L {HALF:g},{root:g} Z"/>'
            + rect(-J.SLIT / 2, -NOSE, J.SLIT, root + NOSE, "void")
            + rect(-NOSE, root, LIMB, end - root, "mate")
            + rect(-HALF - J.STUB_PROUD, -STUB_R, J.STUB_PROUD, 2 * STUB_R, "mate")
            + rect(HALF, -STUB_R, J.STUB_PROUD, 2 * STUB_R, "mate"))


# ------------------------------------------------------------------ frames of the model
#
# A shaded view answers with the part fitted to the image, so the millimeters-to-pixels mapping is
# not a constant anyone can look up. It is measured here instead: the ink's own bounding box in the
# frame is the projection of the part's bounding box, which is known, and two numbers follow.


def ink_box(path):
    """The pixel box the render's ink occupies, as (x0, y0, x1, y1).

    The frames come back with a transparent background, which reads as black once the alpha is
    dropped, so the frame is laid on white before anything is measured."""
    from PIL import Image
    im = Image.open(path)
    white = Image.new("RGBA", im.size, (255, 255, 255, 255))
    flat = Image.alpha_composite(white, im.convert("RGBA")).convert("L")
    box = flat.point(lambda v: 255 if v < 250 else 0).getbbox()
    if box is None:
        raise SystemExit(f"{path.name} is blank")
    return box


def frame(path, left, right, top, bottom):
    """A frame placed in millimeters: `left`..`right` and `top`..`bottom` are the model extents its
    ink covers, in the figure's own axes, y down the page."""
    from PIL import Image
    x0, y0, x1, y1 = ink_box(path)
    w, h = Image.open(path).size
    sx, sy = (right - left) / (x1 - x0), (bottom - top) / (y1 - y0)
    data = base64.b64encode(path.read_bytes()).decode()
    return (f'<image x="{left - x0 * sx:.4f}" y="{top - y0 * sy:.4f}" '
            f'width="{w * sx:.4f}" height="{h * sy:.4f}" '
            f'href="data:image/png;base64,{data}"/>')


# ------------------------------------------------------------------ figure: the two parts
#
# The fork, the blade, and the pair as the Part Studio holds them, all looked at square across the
# pin and placed on the same millimeter grid, so the three read against each other.


def fig_frames():
    art = []
    for i, (name, tag, lo, hi) in enumerate(
            (("9p1p1-fork-side.png", "the fork", -NOSE, END_FORK),
             ("9p1p1-blade-side.png", "the blade", -END_BLADE, NOSE),
             ("9p1p1-both-side.png", "both", -END_BLADE, END_FORK))):
        art.append(f'<g transform="translate({-34 + 34 * i},0)">'
                   + frame(FRAMES / name, -NOSE, NOSE, -hi, -lo)
                   + text(0, END_BLADE + 8, tag, "sub", "middle") + "</g>")
    return svg(art, -52, -END_FORK - 6, 104, ELBOW + 20, scale=9.0)


# ------------------------------------------------------------------ figure: the empty slot
#
# The same frame again, with the slot's root and the blade's nose marked on it. What lies between
# them is slot that nothing ever reaches.


def fig_slot():
    art = [frame(FRAMES / "9p1p1-both-side.png", -NOSE, NOSE, -END_FORK, END_BLADE)]
    for y, tag in ((-ROOT_FORK, "the slot's root"),
                   (-NOSE, "as far as the blade's nose reaches"),
                   (0, "the pin")):
        art += [f'<path class="stn" d="M {-30:g},{y:g} H 30"/>', text(33, y + 1.3, tag, "call")]
    art += [vdim(24, -ROOT_FORK, -NOSE, f"{mm(BURIED_FORK)} mm", side=-1),
            vdim(-19, -ROOT_FORK, 0, f"{mm(ROOT_FORK)} mm")]
    return svg(art, -34, -END_FORK - 8, 140, ELBOW + 16, scale=7.6)


# ------------------------------------------------------------------ figure: what the rod buries
#
# Left, the joint as the hinge Part Studio holds it. Right, the same joint after the limb's rod is
# unioned onto each half, which is the shape that prints. The rod is the pale material.


def fig_burial():
    """The same joint with the limb's rod run on to the pin, and with it stopped at each root.

    Left is what draft9p1p1 prints and what every figure in the brief was computed against. Right
    is what the settled design asks for: the rod stops where the member's own cut stops, so the
    free lengths the arithmetic uses are the free lengths the plastic has.
    """
    top, bot = -(ROOT_FORK + J.ROD_FORK), ROOT_BLADE + J.ROD_BLADE
    buried = ["".join([
        rect(-NOSE, -(NOSE + J.ROD_FORK), LIMB, J.ROD_FORK, "rod"),
        rect(-NOSE, NOSE, LIMB, J.ROD_BLADE, "rod"),
        fork(-ROOT_OLD, -NOSE), blade(ROOT_OLD, NOSE),
        pin_axis(top - 4, bot + 4),
        f'<path class="hid" d="M {-NOSE:g},{-ROOT_FORK:g} H {NOSE:g} '
        f'M {-NOSE:g},{ROOT_BLADE:g} H {NOSE:g}"/>']),
        vdim(-NOSE - 9, -ROOT_OLD, 0, f"{mm(ROOT_OLD)} mm", ext=-NOSE),
        vdim(-NOSE - 22, -ROOT_FORK, -ROOT_OLD, f"{mm(BURIED_FORK)} mm buried", ext=-NOSE),
        vdim(NOSE + 9, 0, ROOT_OLD, f"{mm(ROOT_OLD)} mm", side=-1, ext=NOSE),
        vdim(NOSE + 22, ROOT_OLD, ROOT_BLADE, f"{mm(BURIED_BLADE)} mm buried", side=-1, ext=NOSE),
        text(0, top - 12, "the rod run on to the pin", "head", "middle"),
        text(0, top - 6.4, "which is what draft9p1p1 prints", "sub", "middle"),
        text(0, bot + 10, f"both members root at {mm(ROOT_OLD)} mm", "bad", "middle"),
        text(0, bot + 15, f"and the joint needs {mm(at_roots(ROOT_OLD, ROOT_OLD)[0])} kgf",
             "bad", "middle")]
    freed = ["".join([
        rect(-NOSE, top, LIMB, J.ROD_FORK, "rod"),
        rect(-NOSE, ROOT_BLADE, LIMB, J.ROD_BLADE, "rod"),
        fork(-ROOT_FORK, -ROOT_FORK), blade(ROOT_BLADE, ROOT_BLADE),
        pin_axis(top - 4, bot + 4)]),
        vdim(-NOSE - 9, -ROOT_FORK, 0, f"{mm(ROOT_FORK)} mm", ext=-NOSE),
        vdim(NOSE + 9, 0, ROOT_BLADE, f"{mm(ROOT_BLADE)} mm", side=-1, ext=NOSE),
        text(0, top - 12, "the rod stopped at each root", "head", "middle"),
        text(0, top - 6.4, "which is what the settled design asks for", "sub", "middle"),
        text(0, bot + 10, f"the ear roots at {mm(ROOT_FORK)} mm and the tongue at "
                          f"{mm(ROOT_BLADE)}", "good", "middle"),
        text(0, bot + 15, f"and the joint needs {mm(at_roots(ROOT_BLADE, ROOT_FORK)[0])} kgf",
             "good", "middle")]
    art = [f'<g transform="translate(-58,0)">{"".join(buried)}</g>',
           f'<g transform="translate(58,0)">{"".join(freed)}</g>']
    return svg(art, -114, top - 20, 228, (bot - top) + 42, scale=4.8)


# ------------------------------------------------------------------ figure: the ear as a spring
#
# One ear, three times, rooted where each of the three documents puts it. The cantilever is
# make_plans' own; only the free length changes, and stiffness changes as the cube of it.


def fig_ear():
    """One ear, three times, rooted where each of three documents put it.

    Strength does not move when a root moves; stiffness goes as one over the cube of the free
    length. The press force under each drawing is the whole joint's, both sides, out of
    `tools/hinge_spring.py`.
    """
    cases = (("the plan sheet, before this review", SHEET_ROOT, J.BLADE_OUT),
             ("the rod run on to the pin", ROOT_OLD, ROOT_OLD),
             ("the design as it now is", ROOT_FORK, ROOT_BLADE))
    art = []
    for i, (tag, free, tab) in enumerate(cases):
        press, ear_mpa, leaf_mpa, _ = at_roots(tab, free)
        over = max(ear_mpa, leaf_mpa) > J.PETG_YIELD
        cls = "bad" if over else "good"
        g = ["".join([ear(1, -free),
                      rect(SEAT, -BORE_R, NOSE - SEAT, 2 * BORE_R, "void"),
                      f'<path class="ctr" d="M {SEAT - 4:g},0 H 22"/>',
                      f'<path class="gnd" d="M {SEAT - 2:g},{-free:g} H {NOSE + 2:g}"/>']),
             arrow(16, 0, 22, 0), text(19, -2.8, f"{mm(J.CLIMB)} mm", "dimt", "middle"),
             vdim(32, -free, 0, f"{mm(free)} mm", side=-1, ext=15),
             text(9, -SHEET_ROOT - 9, tag, "sub", "middle"),
             text(9, 16, f"{mm(press)} kgf to press", "dimt", "middle"),
             text(9, 23, f"{mm(ear_mpa)} MPa in the ear", cls, "middle"),
             text(9, 29, f"{mm(leaf_mpa)} MPa in the leaf", cls, "middle"),
             text(9, 35, f"{'over' if over else 'under'} PETG's {J.PETG_YIELD:g}", cls,
                  "middle")]
        art.append(f'<g transform="translate({86 * i},0)">{"".join(g)}</g>')
    return svg(art, -46, -SHEET_ROOT - 18, 320, SHEET_ROOT + 60, scale=6.0)


# ------------------------------------------------------------------ figure: the axle in its bore
#
# Across the joint at the pin. The axle stands STUB_PROUD off the blade into a GAP, so what is left
# is what holds the arm on, and it is also what the ear has to give to let the blade in. The slit
# runs through this section, so there are two stubs here and no shaft between them.


def fig_axle():
    # The ear's inner face is at SEAT / 2 and the bore's mouth is in it. It used to be relieved
    # 0.45 further out everywhere but the land, and a section drawn flat out there gave a gap of
    # 0.6 and an ear of 6.4, neither matching the callout beside it. One face, one number, now.
    tall, face = 8, J.SEAT / 2
    art = ["".join([
        rect(-NOSE, -tall, NOSE - face, 2 * tall), rect(face, -tall, NOSE - face, 2 * tall),
        rect(-NOSE, -BORE_R, NOSE - face, 2 * BORE_R, "void"),
        rect(face, -BORE_R, NOSE - face, 2 * BORE_R, "void"),
        rect(-HALF, -tall, J.BLADE, 2 * tall, "mate"),
        rect(-J.SLIT / 2, -tall, J.SLIT, 2 * tall, "void"),
        rect(-HALF - J.STUB_PROUD, -STUB_R, J.STUB_PROUD, 2 * STUB_R, "mate"),
        rect(HALF, -STUB_R, J.STUB_PROUD, 2 * STUB_R, "mate"),
        f'<path class="ctr" d="M {-NOSE - 3:g},0 H {NOSE + 3:g}"/>'])]
    left = ((-(J.SLIT + J.LEAF) / 2, -tall,
             f"one leaf, {mm(J.LEAF)} mm of a {mm(J.BLADE)} mm tongue"),
            (-HALF - J.STUB_PROUD / 2, -STUB_R, f"the axle, &#216;{mm(J.STUB)} mm"),
            (-(HALF + face) / 2, tall, f"the gap it crosses, {mm(J.GAP)} mm"))
    right = ((HALF + J.STUB_PROUD / 2, -STUB_R,
              f"{mm(ENGAGE)} mm of it is in the bore"),
             ((HALF + J.STUB_PROUD + NOSE) / 2, 0,
              f"{mm(EAR - ENGAGE)} mm of bore is behind it"),
             ((face + NOSE) / 2, tall, f"the ear, {mm(EAR)} mm thick"))
    rows = (-20, -13, 15)
    for i, (px, py, label) in enumerate(left):
        art += [f'<path class="lead" d="M {px:g},{py:g} L -18,{rows[i]:g}"/>',
                text(-19, rows[i] + 1.2, label, "call", "end")]
    for i, (px, py, label) in enumerate(right):
        art += [f'<path class="lead" d="M {px:g},{py:g} L 18,{rows[i]:g}"/>',
                text(19, rows[i] + 1.2, label, "call")]
    art.append(text(0, -30, "the axle in its bore, seen across the pin", "head", "middle"))
    return svg(art, -90, -36, 180, 58, scale=6.4)


# ------------------------------------------------------------------ figure: the two connectors
#
# Where each part carries the mate connector the limb is built onto, drawn on the part itself.


def conn(y, dy):
    return "".join([
        f'<path class="conn" d="M -6,{y:g} H 6"/>',
        f'<circle class="conn" cx="0" cy="{y:g}" r="1.4" fill="#0b6e86"/>',
        f'<path class="conn" d="M 0,{y:g} V {y + dy:g}"/>',
        f'<path class="conn" fill="#0b6e86" d="M 0,{y + dy:g} L -1.5,{y + 0.65 * dy:g} '
        f'L 1.5,{y + 0.65 * dy:g} Z"/>'])


def fig_connectors():
    top, bot = -END_FORK, END_BLADE
    art = ["".join([fork(-ROOT_FORK, top), blade(ROOT_BLADE, bot),
                    pin_axis(top - 4, bot + 4), conn(-NOSE, -8), conn(END_BLADE, 8)]),
           f'<path class="lead" d="M 2,{-NOSE:g} L 16,{-NOSE - 4:g}"/>',
           text(17, -NOSE - 3, "fork to robot connector", "connd"),
           text(17, -NOSE + 2, f"{mm(NOSE)} mm from the pin, inside the solid", "call"),
           text(17, -NOSE + 7, f"{mm(END_FORK - NOSE)} mm short of its own end face", "call"),
           f'<path class="lead" d="M 2,{END_BLADE:g} L 16,{END_BLADE - 4:g}"/>',
           text(17, END_BLADE - 3, "blade to robot connector", "connd"),
           text(17, END_BLADE + 2, f"{mm(END_BLADE)} mm from the pin, on its end face", "call"),
           text(17, END_BLADE + 7, "and pointing out of the part", "call"),
           vdim(-NOSE - 9, -END_FORK, -NOSE, f"{mm(END_FORK - NOSE)} mm", ext=-NOSE),
           text(26, top - 11, "the two robot connectors", "head", "middle"),
           text(26, bot + 16, "one is buried and points inward, the other is flush", "sub",
                "middle"),
           text(26, bot + 21, "and points out, so the fork needs Transform's flip", "sub",
                "middle"),
           text(26, bot + 26, "in its limb where the blade does not", "sub", "middle")]
    return svg(art, -46, top - 18, 156, ELBOW + 50, scale=6.4)


# ------------------------------------------------------------------ figure: draft9p3's connector
#
# Where the same connector landed when the tutorial was driven, against where the reference has it.


def fig_9p3():
    top, bot = -NOSE - 4, END_BLADE + 6
    step_x = (HALF + NOSE) / 2
    art = ["".join([blade(ROOT_BLADE, END_BLADE), pin_axis(top, bot), conn(END_BLADE, 8)]),
           f'<path class="lead" d="M 2,{END_BLADE:g} L 16,{END_BLADE - 3:g}"/>',
           text(17, END_BLADE - 2, "the reference", "connd"),
           text(17, END_BLADE + 3, f"0, 0, {mm(-END_BLADE)}, pointing out", "call"),
           f'<circle cx="{-step_x:g}" cy="{ROOT_BLADE:g}" r="1.4" '
           f'fill="#b8156e" stroke="#b8156e"/>',
           f'<path class="lead" d="M {-step_x:g},{ROOT_BLADE:g} L -20,'
           f'{ROOT_BLADE - 3:g}"/>',
           text(-21, ROOT_BLADE - 2, "draft9p3", "bad", "end"),
           text(-21, ROOT_BLADE + 3, "0, -7.884, -20", "call", "end"),
           text(-21, ROOT_BLADE + 8, "the tongue root step's centroid", "call", "end"),
           text(0, top - 6, "the blade's robot connector", "head", "middle")]
    return svg(art, -90, top - 12, 190, (bot - top) + 20, scale=6.4)


# ------------------------------------------------------------------ plumbing


def render(svg_path):
    from playwright.sync_api import sync_playwright
    out = svg_path.with_suffix(".png")
    html = "<style>html,body{margin:0;background:#fff}</style>" + svg_path.read_text()
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
        page = b.contexts[0].new_page()
        page.set_viewport_size({"width": 2400, "height": 1800})
        page.set_content(html)
        page.wait_for_timeout(700)
        page.locator("svg").screenshot(path=str(out))
        page.close()
        b.close()
    print(f"  {out.name}  {out.stat().st_size:,} bytes")


FIGURES = (("frames", fig_frames), ("slot", fig_slot), ("burial", fig_burial),
           ("ear", fig_ear), ("axle", fig_axle), ("connectors", fig_connectors),
           ("blade-connector", fig_9p3))


def numbers():
    """The tables the page reads, written where they are computed rather than typed into prose.

    One file each, so the page can put a table where it argues for it."""
    rows = [("``LIMB``", 12, LIMB, "``TORSO_H / 4``"), ("``BLADE``", 5.0, J.BLADE, "typed"),
            ("``GAP``", 0.3, 0.6, "was typed; is now the seat, 0.20"),
            ("``STUB``", 2.0, J.STUB, "typed"),
            ("``STUB_PROUD``", 0.8, 1.6, "was typed; is now 1.00"),
            ("``BLADE_OUT``", 16, J.BLADE_OUT, "typed, and kept"),
            ("``TOOTH_PROUD``", 0.6, 1.2, "is now the cone's own height, 0.60"),
            ("``VALLEY_DEEP``", 0.45, 0.9, "gone; the valley goes through the ear")]
    doubling = [".. list-table:: What the doubling took with it",
                "   :header-rows: 1", "   :widths: 24 10 10 34", "",
                "   * - name", "     - before", "     - after", "     - where it ended up"]
    for name, a, b, src in rows:
        doubling += [f"   * - {name}", f"     - {mm(a)}", f"     - {mm(b)}", f"     - {src}"]

    rooted = [".. list-table:: The same joint, with its two members rooted three ways",
              "   :header-rows: 1", "   :widths: 34 12 12 14 14 14", "",
              "   * - where the two members root", "     - ear", "     - tongue",
              "     - press force", "     - ear", "     - leaf"]
    for tag, free, tab in (
            ("the plan sheet, before this review", SHEET_ROOT, J.BLADE_OUT),
            ("the rod run on to the pin", ROOT_OLD, ROOT_OLD),
            ("the design as it now is", ROOT_FORK, ROOT_BLADE)):
        press, ear_mpa, leaf_mpa, _ = at_roots(tab, free)
        rooted += [f"   * - {tag}", f"     - {mm(free)} mm", f"     - {mm(tab)} mm",
                   f"     - {mm(press)} kgf", f"     - {mm(ear_mpa)} MPa",
                   f"     - {mm(leaf_mpa)} MPa"]

    floor = at_roots(ROOT_BLADE, ROOT_FORK, proud=J.GAP + J.CLIMB)[0]
    axle = [".. list-table:: How much axle to leave standing off the tongue",
            "   :header-rows: 1", "   :widths: 16 16 16 16 22", "",
            "   * - ``STUB_PROUD``", "     - in the bore", "     - press force",
            "     - tears out at", "     - over the teeth's own"]
    for proud in (1.2, J.STUB_PROUD, 0.9, 0.8):
        press = at_roots(ROOT_BLADE, ROOT_FORK, proud=proud)[0]
        axle += [f"   * - {mm(proud)} mm", f"     - {mm(proud - J.GAP)} mm",
                 f"     - {mm(press)} kgf", f"     - {mm(crush(proud))} kgf",
                 f"     - {mm(press - floor)} kgf"]

    slit = [".. list-table:: What the slit up the tongue buys and what it costs",
            "   :header-rows: 1", "   :widths: 12 14 16 18 20", "",
            "   * - slit", "     - each leaf", "     - press force", "     - turning torque",
            "     - the tongue sideways, at a hand 150 mm out"]
    for w in (1.0, 2.0, 3.0, J.SLIT, 5.0, 6.0):
        leaf = (J.BLADE - w) / 2
        press, _, _, torque = at_roots(ROOT_BLADE, ROOT_FORK, slit=max(w, 1e-6))
        sideways = hinge_spring.sections(
            reviewed(slit=max(w, 1e-6)))["blade"][1] / 150 / 9.81
        slit += [f"   * - {mm(w)} mm", f"     - {mm(leaf)} mm", f"     - {mm(press)} kgf",
                 f"     - {mm(torque)} N&#183;mm", f"     - {mm(sideways)} kgf"]

    settled = [".. list-table:: The joint as it now stands",
               "   :widths: 30 18 52", ""]
    for what, value, why in (
            ("the limb", f"&#216;{mm(J.LIMB)} mm",
             f"cut flat top and bottom to {mm(J.LIMB_FLAT)} mm, so it prints on a face"),
            ("the slot", f"{mm(J.SEAT)} mm",
             f"cut through the limb, its whole depth, so the fit is ``GAP`` {mm(J.GAP)} mm a "
             "side everywhere the tongue touches"),
            ("the ear", f"{mm(EAR)} mm", "``(LIMB - SEAT) / 2``, and it roots at "
             f"{mm(ROOT_FORK)} mm"),
            ("the tongue", f"{mm(J.BLADE)} mm",
             f"split by a {mm(J.SLIT)} mm slit into two {mm(J.LEAF)} mm leaves, rooted at "
             f"{mm(ROOT_BLADE)} mm"),
            ("the teeth", f"{J.TEETH}, {J.STEP}&#176; apart",
             f"&#216;{mm(J.VALLEY_D)} mm valleys through the ear on r {J.BUMP_R:.3f}"),
            ("a tooth", f"{mm(J.TOOTH_PROUD)} mm proud",
             f"a 45&#176; cone, &#216;{mm(J.CONE_D)} mm at its base and {mm(J.TOOTH_FLAT)} mm "
             f"flat on top"),
            ("the climb", f"{mm(J.CLIMB)} mm", "how far the pair opens to let a tooth out"),
            ("the axle", f"&#216;{mm(J.STUB)} mm", f"{mm(J.STUB_PROUD)} mm proud into a "
             f"&#216;{mm(J.BORE_D)} mm bore, so {mm(J.ENGAGED)} mm is engaged"),
            ("pressing it together", f"{mm(J.PRESS_F)} kgf",
             f"{mm(J.EAR_STRESS)} MPa in the ear, {mm(J.LEAF_STRESS)} in the leaf, against "
             f"PETG's {J.PETG_YIELD:g}"),
            ("turning it", f"{mm(J.HOLD_T)} N&#183;mm",
             f"{mm(J.HOLD_HAND)} kgf at a hand 150 mm out, and {mm(J.HOLD_T / J.ARM_DROOP)} "
             f"times what holding the arm up takes"),
            ("teeth carrying", f"{J.HOLD_TEETH}",
             "the rest ride clear, because both members are beams")):
        settled += [f"   * - {what}", f"     - {value}", f"     - {why}"]

    return {"doubling": doubling, "rooted": rooted, "axle": axle, "slit": slit,
            "settled": settled}


def main():
    IMAGES.mkdir(parents=True, exist_ok=True)
    tables = HERE / "source" / "tables"
    tables.mkdir(exist_ok=True)
    for name, lines in numbers().items():
        (tables / f"{name}.rst").write_text("\n".join(lines) + "\n")
        print(f"wrote tables/{name}.rst")
    for name, maker in FIGURES:
        path = IMAGES / f"{name}.svg"
        try:
            drawn = maker()
        except FileNotFoundError as missing:
            # The two figures built on photographs need the shaded views taken during the sweep,
            # which live outside the repo and are long gone. The drawings they made are committed,
            # so leave them alone and say which one was skipped rather than failing the build.
            print(f"skipped {path.name}: {pathlib.Path(missing.filename).name} is not here")
            continue
        path.write_text(drawn)
        print(f"wrote {path.name}")
        if "--no-render" not in sys.argv:
            render(path)


if __name__ == "__main__":
    main()
