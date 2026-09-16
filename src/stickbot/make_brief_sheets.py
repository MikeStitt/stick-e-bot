#!/usr/bin/env python3
"""Generate the dimensioned sheets the build briefs reference.

Status: illustrative — derived drawings. It decides no dimension. Every number comes
from make_plans.py, so these sheets cannot describe a robot the design source does not.

Three sheets, each answering a question prose kept failing to answer:

  brief-fork      why the fork is drawn as slices of the limb and not as a rectangle
  brief-detent    what the detent band and one bump actually look like, to scale
  brief-socket    what the socket looks like sitting in a limb rather than on a pad

Every number comes from make_plans.py, so these sheets and the student plan sheets
cannot drift apart.

    uv run python make_brief_sheets.py
"""

from __future__ import annotations

import math
import sys

from stickbot import repo_root

from stickbot.make_plans import (
    BACKLASH,
    BALL,
    BLADE,
    BORE_D,
    CAVITY,
    CLIMB,
    COLLAR_L,
    COLLAR_WALL,
    EAR,
    FLAT,
    GAP,
    GRIP,
    LIMB,
    LIMB_FLAT,
    MOUTH,
    RING_CON,
    RING_IN,
    RING_OUT,
    SLIT_W,
    STALK,
    T_PRINT,
    STUB_PROUD,
    WEDGES,
    WEDGE_BIND,
    WEDGE_C,
    WEDGE_H,
    WEDGE_INSET,
    WEDGE_W,
    circle,
    limb_d,
    rect,
    render,
    svg,
    text,
)

OUT = repo_root() / ".docs" / "experiments" / "build-briefs" / "images"

# ---------------------------------------------------------------- dimensions


def arrow(x, y, d):
    """A filled arrowhead with its tip at (x, y), pointing d."""
    body = {
        "left": "l 4,-1.4 v 2.8 z",
        "right": "l -4,-1.4 v 2.8 z",
        "up": "l -1.4,4 h 2.8 z",
        "down": "l -1.4,-4 h 2.8 z",
    }[d]
    return f'<path d="M {x:g},{y:g} {body}" fill="#b8156e"/>'


def dim_h(xa, xb, y, label, above=True):
    """A horizontal dimension between xa and xb, drawn on the line y."""
    mid = (xa + xb) / 2
    dy = -2.2 if above else 5.2
    return (f'<path class="dim" d="M {xa:g},{y:g} H {xb:g}"/>'
            + arrow(xa, y, "left") + arrow(xb, y, "right")
            + text(mid, y + dy, label, "dimt", "middle"))


def dim_v(ya, yb, x, label, left=True, rot=True):
    """A vertical dimension between ya and yb, drawn on the line x.

    Short dimensions cannot carry a rotated label between their arrows, so rot=False
    sets the label horizontally beside the line instead.
    """
    mid = (ya + yb) / 2
    line = (f'<path class="dim" d="M {x:g},{ya:g} V {yb:g}"/>'
            + arrow(x, ya, "up") + arrow(x, yb, "down"))
    if not rot:
        return line + (text(x + 5, mid + 1.5, label, "dimt") if not left
                       else text(x - 5, mid + 1.5, label, "dimt", "end"))
    return line + text(x + (-2.6 if left else 2.6), mid, label, "dimt", "middle", rot=-90)


def witness(x1, y1, x2, y2):
    return f'<path class="dim" d="M {x1:g},{y1:g} L {x2:g},{y2:g}" stroke-dasharray="2 1.5"/>'


# ---------------------------------------------------------------- sheet: fork


def sheet_fork():
    """The fork seen down the limb axis. Every layer is a full slice of the flatted limb."""
    S = 26                                     # 26 px per mm
    r = LIMB / 2
    inner, outer = BLADE / 2 + GAP, BLADE / 2 + GAP + EAR   # 6.0 and 12.0

    def wide(y):
        """The limb section's full width at a cut y off the pin axis, flats included."""
        return 2 * min(FLAT, (r * r - y * y) ** 0.5)

    def P(px, py):                             # model mm -> sheet coordinates
        return (S * px, -S * py)               # y up in the model, down on the sheet

    bands = [
        (-outer, -inner, "part"), (-BLADE / 2, BLADE / 2, "mate"), (inner, outer, "part"),
    ]
    art = [f'<clipPath id="limb"><path d="{limb_d(r, FLAT)}"/></clipPath>',
           f'<path class="ghost" d="{limb_d(r, FLAT)}"/>']
    art += [f'<g clip-path="url(#limb)">'
            + "".join(rect(-r, -b, LIMB, b - a, cls) for a, b, cls in bands)
            + "</g>"]
    art += [f'<path class="ctr" d="M {-r - 1.5:g},0 H {r + 1.5:g} '
            f'M 0,{-r - 1.5:g} V {r + 1.5:g}"/>']
    geo = f'<g transform="scale({S},{-S})" class="det">{"".join(art)}</g>'

    lab = []
    # width dimensions, stacked below the section, nearest cut first
    for i, (y, name) in enumerate([(BLADE / 2, "blade"), (inner, "ear inner face"),
                                   ((inner + outer) / 2, "halfway up the ear")]):
        h = wide(y) / 2
        yy = P(0, -r)[1] + 30 + 26 * i
        lab += [witness(*P(-h, -y), -S * h, yy + 4), witness(*P(h, -y), S * h, yy + 4)]
        lab += [dim_h(-S * h, S * h, yy, f"{wide(y):.2f} mm")]
        lab += [text(0, yy + 12, f"the full slice at &#177;{y:g} mm; {name}",
                     "call", "middle")]

    # the stack, dimensioned up the right-hand side
    x0 = S * r + 40
    stack = [(inner, outer, f"ear {EAR:g} mm"), (BLADE / 2, inner, f"gap {GAP:g} mm"),
             (-BLADE / 2, BLADE / 2, f"blade {BLADE:g} mm")]
    for a, b, name in stack:
        lab += [dim_v(P(0, b)[1], P(0, a)[1], x0, name, left=False, rot=False)]
    lab += [dim_v(P(0, outer)[1], P(0, -outer)[1], x0 + 78,
                  f"fork span {BLADE + 2 * GAP + 2 * EAR:g} mm", left=False)]
    for y in (outer, inner, BLADE / 2, -BLADE / 2, -inner, -outer):
        lab += [witness(S * wide(y) / 2, P(0, y)[1], x0 + 84, P(0, y)[1])]

    lab += [
        text(0, P(0, r)[1] - 52, "THE FORK, SEEN DOWN THE LIMB", "lbl", "middle"),
        text(0, P(0, r)[1] - 41,
             f"Every layer is a full slice of the limb: &#216;{LIMB:g} mm, "
             f"flatted to {LIMB_FLAT:.2f} mm across.", "note", "middle"),
        dim_h(-S * FLAT, S * FLAT, P(0, r)[1] - 24, f"{LIMB_FLAT:.4f} mm across the flats"),
        dim_h(-S * r, S * r, P(0, r)[1] - 12, f"&#216;{LIMB:g} mm"),
        text(0, P(0, -r)[1] + 128,
             f"The two flats are cut at &#177;{FLAT:.4f} mm, which is where the "
             f"&#216;{LIMB:g} mm surface crosses the seat wall at &#177;{inner:g} mm.",
             "note", "middle"),
        text(0, P(0, -r)[1] + 139,
             f"So the ear is a cap of the circle and the blade is the flat middle, "
             f"{wide(BLADE / 2):.2f} mm wide; the slot never bounds it sideways.",
             "note", "middle"),
        text(0, P(0, -r)[1] + 150,
             "Draw a narrower paddle inside the slice and its corners bind before its "
             "faces do. Let every face run out to the section.", "note", "middle"),
    ]
    return svg([geo] + lab, -470, -382, 940, 872, scale=2.2)


# -------------------------------------------------------------- sheet: detent
#
# Everything on this sheet is one wedge and its neighbor, at the radius where a flank
# actually bears. Two things live here that no other drawing shows: what the 45 degree
# draft does to the crest as the radius falls, and what the pair looks like in section
# both seated and riding.

W2 = math.radians(WEDGE_W) / 2       # half a wedge, at its base, in radians
R_CI = RING_IN + WEDGE_H             # 6.75 — where the draft's inner arc cuts the crest
R_CO = RING_CON                      # 9.2423 — and its outer arc, which is also the bearing
                                     # radius, so the section below is developed on it
PITCH = 2 * math.pi * R_CO / WEDGES  # 4.8393 mm of arc, one wedge to the next
HALF_B = R_CO * W2                   # 1.5996 — half the wedge's base, in that section
HALF_C = HALF_B - R_CO * math.asin(WEDGE_H / R_CO)   # 0.8487 — and half its crest
FREE = (PITCH / 2 - HALF_B - HALF_C
        + R_CO * math.asin(WEDGE_C / R_CO))   # 0.2215 — one flank's clearance, from one
                                     # member's crest corner across to the other's flank,
                                     # which is where the two come closest at this radius.
                                     # The fit is not set here: it is set at WEDGE_BIND,
                                     # where it comes to 2 T_PRINT exactly


def crest_half(r):
    """Half the crest's angular width at radius r.

    A 45 degree draft is a planar inward offset by WEDGE_H, so the crest boundary is the
    set of points WEDGE_H from a flank: r sin(W/2 - t) = WEDGE_H. The offset is a length
    and the arc it eats is an angle, so the crest narrows going inward.
    """
    return W2 - math.asin(WEDGE_H / r)


def crest_w(r):
    return 2 * r * crest_half(r)


def sheet_detent():
    """One wedge square on, and the pair in developed section."""
    cx = 164                             # the sheet's own center, which is not zero
    head = [
        text(cx, -292, "THE WEDGE", "lbl", "middle"),
        text(-330, -266, "ONE WEDGE SQUARE ON", "call", "middle"),
        text(-330, -256, f"the crest is the base inset {WEDGE_H:g} mm all round",
             "call", "middle"),
        text(300, -266, "THE PAIR IN SECTION", "call", "middle"),
        text(300, -256, f"developed on the r {R_CO:.4f} mm circle, where a flank bears",
             "call", "middle"),
    ]
    notes = [
        f"A 45&#176; draft is a planar inward offset by {WEDGE_H:g} mm, so the crest is the "
        f"base inset {WEDGE_H:g} mm all round; and the offset is a length while the arc it "
        f"eats is an angle.",
        f"So the crest narrows going inward. It would close to a point at r "
        f"{WEDGE_H / math.sin(W2):.4f} mm, which is well inside the ring's own inner "
        f"end at r {RING_IN:g} mm, so on this ring it "
        f"never does.",
        f"{WEDGES} wedges to a face, at {360 / WEDGES:g}&#176; pitch, on the tongue and on "
        f"each ear. The base is {2 * RING_OUT * W2:.4f} mm at the tip and "
        f"{2 * HALF_B:.4f} mm where the section is taken.",
        f"The wedge is {WEDGE_W:.4f}&#176; across, which is wider than half a step. It has "
        f"to be: both members are drafted, and by mid-gap each has leaned "
        f"{GAP / 2:g} mm away from the other.",
        f"That lean is worth {WEDGE_INSET:.4f}&#176; of extra width, and it is set half way "
        f"up the gap at r {WEDGE_BIND:.4f} mm, where the two radial draft ends have taken "
        f"the least off the radius.",
        f"There the clearance comes to {2 * T_PRINT:.2f} mm, which is 2 T_PRINT; a flank "
        f"turns {BACKLASH:.4f}&#176; before it touches, and that is the backlash.",
        f"Riding, the two crests are flat on flat, {2 * HALF_C:.4f} mm of contact, and the "
        f"pair has opened {CLIMB:g} mm. Nothing bottoms; the axle stays "
        f"{STUB_PROUD - 2 * WEDGE_H:.2f} mm into its &#216;{BORE_D:g} mm bore while it does.",
    ]
    head += [text(cx, 190 + 14 * i, n, "note", "middle") for i, n in enumerate(notes)]
    return svg(head + [_wedge_face(-330, -40), _wedge_section(300)],
               -500, -310, 1340, 630, scale=1.7)


def _wedge_face(ox, oy):
    """One wedge, radius across the page, at a scale that makes the crest readable."""
    S = 62
    mid = (RING_IN + RING_OUT) / 2

    def pt(r, a):
        return f"{r * math.cos(a) - mid:.4f},{r * math.sin(a):.4f}"

    def P(r, a=0.0):
        return (ox + S * (r * math.cos(a) - mid), oy - S * r * math.sin(a))

    base = (f'<path class="part" d="M {pt(RING_IN, -W2)} '
            f'A {RING_IN:g},{RING_IN:g} 0 0 1 {pt(RING_IN, W2)} '
            f'L {pt(RING_OUT, W2)} '
            f'A {RING_OUT:g},{RING_OUT:g} 0 0 0 {pt(RING_OUT, -W2)} Z"/>')
    n = 48
    rs = [R_CI + (R_CO - R_CI) * i / n for i in range(n + 1)]
    ring = [pt(r, -crest_half(r)) for r in rs] + [pt(r, crest_half(r)) for r in reversed(rs)]
    crest = f'<path class="mate" d="M {" L ".join(ring)} Z"/>'
    geo = (f'<g transform="translate({ox:g},{oy:g}) scale({S},{-S})" class="det">'
           f'{base}{crest}</g>')

    y_top, y_bot = P(RING_OUT, W2)[1], P(RING_OUT, -W2)[1]
    x_out = P(RING_OUT)[0]
    lab = [
        dim_h(P(RING_IN)[0], P(RING_OUT)[0], y_top - 46,
              f"the wedge is {RING_OUT - RING_IN:.4f} mm long"),
        dim_h(P(R_CI)[0], P(R_CO)[0], y_top - 30,
              f"the crest is {R_CO - R_CI:.4f} mm long"),
        dim_v(P(R_CO, -crest_half(R_CO))[1], P(R_CO, crest_half(R_CO))[1], x_out + 26,
              f"crest {crest_w(R_CO):.4f} mm", left=False, rot=False),
        dim_v(P(R_CI, -crest_half(R_CI))[1], P(R_CI, crest_half(R_CI))[1], P(R_CI)[0] - 24,
              f"{crest_w(R_CI):.4f} mm", rot=False),
    ]
    for r in (RING_IN, R_CI, R_CO, RING_OUT):
        lab += [witness(P(r)[0], y_top - 6, P(r)[0], y_top - 50)]
    lab += [
        witness(*P(R_CO, crest_half(R_CO)), x_out + 32, P(R_CO, crest_half(R_CO))[1]),
    ]
    lab += [text(ox - 150, y_bot + 44, "the crest, radius by radius", "call")]
    lab += [text(ox - 150, y_bot + 60 + 13 * i,
                 f"r {r:7.4f} mm &#8212; {crest_w(r):.4f} mm wide", "call")
            for i, r in enumerate((R_CO, 9.0, 8.0, 7.0, R_CI))]
    return geo + "".join(lab)


def _wedge_section(ox):
    """The pair developed at r RING_CON, drawn twice: seated, and riding crest on crest.

    Horizontal is arc length along that circle; vertical is the hinge axis. At this radius
    the flanks come out 45 degrees to within a thousandth of a millimeter, so they are
    drawn straight.
    """
    S, half, body = 40, 1.5 * PITCH, 0.6

    def tongue(cu):
        return (f'<path class="mate" d="M {cu - HALF_B:.4f},0 L {cu - HALF_C:.4f},{WEDGE_H:g} '
                f'L {cu + HALF_C:.4f},{WEDGE_H:g} L {cu + HALF_B:.4f},0 Z"/>')

    def ear(cu, sep):
        return (f'<path class="part" d="M {cu - HALF_B:.4f},{sep:g} '
                f'L {cu - HALF_C:.4f},{sep - WEDGE_H:g} '
                f'L {cu + HALF_C:.4f},{sep - WEDGE_H:g} L {cu + HALF_B:.4f},{sep:g} Z"/>')

    def draw(dy, sep, ear_us):
        art = [rect(-half, -body, 2 * half, body, "mate")]
        art += [tongue(cu) for cu in (-PITCH, 0, PITCH)]
        art += [rect(-half, sep, 2 * half, body, "part")]
        art += [ear(cu, sep) for cu in ear_us]
        return (f'<g transform="translate({ox:g},{dy:g}) scale({S},{-S})" class="det">'
                f'{"".join(art)}</g>')

    y_a, y_b = -126, 100
    geo = (draw(y_a, GAP, [-0.5 * PITCH, 0.5 * PITCH])
           + draw(y_b, 2 * WEDGE_H, [-PITCH, 0, PITCH]))

    def A(pu, pv):
        return (ox + S * pu, y_a - S * pv)

    def B(pu, pv):
        return (ox + S * pu, y_b - S * pv)

    x_l, x_r = ox - S * half, ox + S * half
    lab = [
        text(ox, A(0, 0)[1] - 118, "SEATED AT A DETENT", "call", "middle"),
        dim_h(A(-PITCH, 0)[0], A(0, 0)[0], A(0, 0)[1] - 100, f"pitch {PITCH:.4f} mm"),
        witness(*A(HALF_C + FREE / 2, WEDGE_H), *A(HALF_C + FREE / 2, GAP + 0.9)),
        text(A(HALF_C + FREE / 2, GAP + 0.95)[0], A(0, GAP + 0.95)[1],
             f"{FREE:.4f} mm free between the crest corner and the facing flank", "call"),
        dim_v(A(0, GAP)[1], A(0, 0)[1], x_r + 26, f"gap {GAP:g} mm", left=False, rot=False),
        dim_v(A(0, GAP)[1], A(0, WEDGE_H)[1], x_r + 122,
              f"clearance {WEDGE_C:g} mm", left=False, rot=False),
        dim_v(A(0, WEDGE_H)[1], A(0, 0)[1], x_l - 26, f"proud {WEDGE_H:g} mm"),
        text(ox, B(0, 0)[1] - 118, "RIDING, CREST ON CREST", "call", "middle"),
        dim_v(B(0, 2 * WEDGE_H)[1], B(0, 0)[1], x_r + 26,
              f"{2 * WEDGE_H:g} mm", left=False, rot=False),
        dim_v(B(0, 2 * WEDGE_H)[1], B(0, GAP)[1], x_r + 122,
              f"climb {CLIMB:g} mm", left=False, rot=False),
    ]
    for v, x1, x2 in ((GAP, x_r, x_r + 128), (0, x_r, x_r + 32), (WEDGE_H, x_r, x_r + 128),
                      (WEDGE_H, x_l, x_l - 32), (0, x_l, x_l - 32)):
        lab += [witness(x1, A(0, v)[1], x2, A(0, v)[1])]
    for v, x1, x2 in ((2 * WEDGE_H, x_r, x_r + 128), (0, x_r, x_r + 32),
                      (GAP, x_r + 96, x_r + 128)):
        lab += [witness(x1, B(0, v)[1], x2, B(0, v)[1])]
    return geo + "".join(lab)


# -------------------------------------------------------------- sheet: socket


def sheet_socket():
    """The socket in section, in a limb — not on a pad."""
    S = 22
    r = LIMB / 2
    coll_r = CAVITY + COLLAR_WALL              # 4.7
    z_mouth, z_face = GRIP, GRIP - COLLAR_L    # +1.35 and -4.15
    z_bot = z_face - 10
    m = MOUTH / 2
    explode, stalk_l = 8, 5

    art = [
        # limb below the collar, cut on the section plane
        rect(-r, z_bot, LIMB, z_face - z_bot, "part"),
        # collar, standing proud, with the cavity taken out of it. The arc runs the long
        # way round from mouth to mouth, so the cavity is a void inside the collar.
        f'<path class="part" d="M {-coll_r:g},{z_face:g} V {z_mouth:g} H {-m:g} '
        f'A {CAVITY:g},{CAVITY:g} 0 1 1 {m:g},{z_mouth:g} '
        f'H {coll_r:g} V {z_face:g} Z"/>',
        # one slit, seen through the near wall
        f'<path class="hid" d="M {-SLIT_W / 2:g},{z_mouth:g} V {z_face:g} '
        f'M {SLIT_W / 2:g},{z_mouth:g} V {z_face:g}"/>',
        f'<path class="ctr" d="M 0,{z_bot - 1.5:g} V {explode + stalk_l + 1.5:g}"/>',
        # the ball stud, exploded above the mouth it has to enter
        rect(-STALK / 2, explode, STALK, stalk_l, "mate"),
        circle(0, explode, BALL / 2, "mate"),
    ]
    geo = f'<g transform="scale({S},{-S})" class="det">{"".join(art)}</g>'

    def P(px, py):
        return (S * px, -S * py)

    top = P(0, explode + stalk_l)[1]
    x_r = S * r + 26
    lab = [
        text(0, top - 44, "THE SOCKET, IN SECTION, IN A LIMB", "lbl", "middle"),
        text(0, top - 32,
             "The socket is the ball, grown by the fit. The stud is drawn lifted clear of "
             "the mouth it has to enter.", "note", "middle"),
        dim_h(P(-BALL / 2, 0)[0], P(BALL / 2, 0)[0], P(0, explode)[1],
              f"ball &#216;{BALL:g} mm"),
        dim_h(P(-m, 0)[0], P(m, 0)[0], P(0, z_mouth)[1] - 16, f"mouth &#216;{MOUTH:.3f} mm"),
        witness(*P(-m, z_mouth), P(-m, 0)[0], P(0, z_mouth)[1] - 16),
        witness(*P(m, z_mouth), P(m, 0)[0], P(0, z_mouth)[1] - 16),
        dim_h(P(-CAVITY, 0)[0], P(CAVITY, 0)[0], P(0, -1.1)[1],
              f"cavity &#216;{2 * CAVITY:g} mm = ball + 2 &#215; fit"),
        dim_h(P(-coll_r, 0)[0], P(-CAVITY, 0)[0], P(0, 0.4)[1], f"wall {COLLAR_WALL:g} mm"),
        dim_h(P(-coll_r, 0)[0], P(coll_r, 0)[0], P(0, z_face)[1] + 22,
              f"collar &#216;{2 * coll_r:g} mm"),
        witness(*P(-coll_r, z_face), P(-coll_r, 0)[0], P(0, z_face)[1] + 22),
        witness(*P(coll_r, z_face), P(coll_r, 0)[0], P(0, z_face)[1] + 22),
        dim_h(P(-r, 0)[0], P(r, 0)[0], P(0, z_bot)[1] + 24, f"limb &#216;{LIMB:g} mm"),
        dim_v(P(0, z_mouth)[1], P(0, z_face)[1], x_r,
              f"collar {COLLAR_L:g} mm proud", left=False),
        dim_v(P(0, z_mouth)[1], P(0, 0)[1], x_r + 108, f"grip {GRIP:g} mm",
              left=False, rot=False),
        witness(P(coll_r, 0)[0], P(0, z_mouth)[1], x_r + 114, P(0, z_mouth)[1]),
        witness(P(coll_r, 0)[0], P(0, z_face)[1], x_r + 6, P(0, z_face)[1]),
        witness(P(CAVITY, 0)[0], P(0, 0)[1], x_r + 114, P(0, 0)[1]),
        text(0, P(0, z_bot)[1] + 48,
             f"Retention is {BALL - MOUTH:.3f} mm &#8212; the ball less the mouth. That is all "
             f"that holds it in.", "note", "middle"),
        text(0, P(0, z_bot)[1] + 60,
             f"Four slits {SLIT_W:g} mm wide run the collar&#8217;s whole {COLLAR_L:g} mm so "
             f"the mouth can open. One is drawn hidden.", "note", "middle"),
        text(0, P(0, z_bot)[1] + 72,
             "On the head this same socket sits in a flat face. On a limb it sits in the "
             "cylinder, as here &#8212; never on a square pad.", "note", "middle"),
    ]
    return svg([geo] + lab, -330, -348, 660, 790, scale=2.0)


# ---------------------------------------------------------------- plumbing


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, maker in (("brief-fork", sheet_fork),
                        ("brief-detent", sheet_detent),
                        ("brief-socket", sheet_socket)):
        path = OUT / f"{name}.svg"
        path.write_text(maker())
        print(f"wrote {path.relative_to(OUT.parents[4])}")
        if "--no-render" not in sys.argv:
            render(path)


if __name__ == "__main__":
    main()
