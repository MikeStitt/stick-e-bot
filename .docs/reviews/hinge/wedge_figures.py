"""Pictures for the one question in changes.md that words did not answer: why, of the

Status: superseded. Despite the file name these are teeth, not the settled wedge ring:
TOOTH_PROUD 1.2, BUMP_R 8.813, GAP 0.6, a third snapshot again distinct from make_figures.py's J.
Read it for the beam argument, which still holds, and not for a dimension.
thirteen teeth inside the slot, only one place along the beam is touching.

A place along the beam is not a tooth. The ring puts two teeth the same distance along
the beam wherever it is not at an end, so the one contact below is two teeth and the two
in the turning case are three.

Every number here is solved, not sketched. The beams are the real leaf and the real ear,
the loads come from the same contact solve as the tables, and the deflections are read
off the same compliance. Only the vertical scale is a lie, and it says so on every sheet.
"""
import math
import pathlib
import sys

R, E, GAP, STEP = 12.0, 2000.0, 0.6, 15
BLADE, SLIT, BUMP_R, NOSE = 10.0, 7.6, 8.813, 12.0
TOOTH_PROUD, STUB_PROUD, S = 1.2, 1.5, 1.4
OUT = pathlib.Path(__file__).parent / "source" / "images"


def seg(a, b, n=6000):
    xs = [a + (b - a) * (i + .5) / n for i in range(n)]
    w = [2 * math.sqrt(max(R * R - x * x, 0.)) for x in xs]
    dx = (b - a) / n
    A = sum(w) * dx
    xb = sum(x * wi for x, wi in zip(xs, w)) * dx / A
    return sum(wi * (x - xb) ** 2 for x, wi in zip(xs, w)) * dx


EIL, EIE = E * seg(SLIT / 2, BLADE / 2), E * seg((BLADE + 2 * GAP) / 2, R)


def comp(p, q, EI):
    lo, hi = min(p, q), max(p, q)
    return lo * lo * (3 * hi - lo) / (6 * EI)


ETAS = sorted({round(BUMP_R * math.cos(math.radians(k * STEP)), 6) for k in range(24)})
A_OF = lambda e: e + 12                     # along the leaf, from the blade's root
B_OF = lambda e: 12 - e + S                 # along the ear, from the fork's rod end
CARRY = (-8.813, 0.0)                       # the two places the solve leaves standing,
                                            # which is three teeth: one and then two


def forces():
    """The two live contact forces, from the 2x2 the active set reduces to."""
    (p, q), g = CARRY, (TOOTH_PROUD - GAP, STUB_PROUD - GAP)
    C = [[comp(A_OF(i), A_OF(j), EIL) + comp(B_OF(i), B_OF(j), EIE) for j in (p, q)]
         for i in (p, q)]
    det = C[0][0] * C[1][1] - C[0][1] * C[1][0]
    return ((g[0] * C[1][1] - g[1] * C[0][1]) / det,
            (g[1] * C[0][0] - g[0] * C[1][0]) / det)


F0, F1 = forces()
leaf = lambda e: F0 * comp(A_OF(e), A_OF(CARRY[0]), EIL) + F1 * comp(A_OF(e), A_OF(CARRY[1]), EIL)
ear = lambda e: F0 * comp(B_OF(e), B_OF(CARRY[0]), EIE) + F1 * comp(B_OF(e), B_OF(CARRY[1]), EIE)

SX, EXAG = 44.0, 190.0                     # mm across the page, and the gap's exaggeration
LM = 210                                   # left margin, in page units
X = lambda eta: LM + (eta - S + 12) * SX    # the fork's frame: its slot mouth is eta - S = -12

CSS = """
 .part{fill:#e8eef2;stroke:#1d262e;stroke-width:1.2;stroke-linejoin:round}
 .ghost{fill:none;stroke:#8fa3b0;stroke-width:1;stroke-dasharray:5 3}
 .tooth{fill:#f6c9dd;stroke:#b8156e;stroke-width:1}
 .live{fill:#b8156e;stroke:#b8156e;stroke-width:1}
 .air{fill:#fdf3d0;stroke:none}
 .dim{stroke:#b8156e;stroke-width:1}
 .rule{stroke:#5b6b78;stroke-width:.8;stroke-dasharray:4 3}
 .axis{stroke:#1d262e;stroke-width:1}
 text{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;fill:#1d262e}
 .h{font-size:19px;font-weight:600}
 .s{font-size:14px}
 .n{font-size:12px;fill:#b8156e}
 .g{font-size:12px;fill:#5b6b78}
"""


def svg(body, w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
            f'height="{h}"><title>{title}</title><style>{CSS}</style>'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>')


def txt(x, y, s, cls="s", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{s}</text>'


def hatch(x, y, h, side):
    """A rooted end: the wall, with its ticks leaning away from the beam."""
    d = [f'M {x:.1f},{y:.1f} V {y + h:.1f}']
    for k in range(7):
        yy = y + h * k / 6.0
        d.append(f'M {x:.1f},{yy:.1f} l {-9 * side:.1f},9')
    return f'<path class="axis" d="{" ".join(d)}"/>'


def bump(cx, cy, live=False, r=3.2):
    return (f'<path class="{"live" if live else "tooth"}" d="M {cx - r:.1f},{cy:.1f} '
            f'a {r:.1f},{r:.1f} 0 0 1 {2 * r:.1f},0 Z"/>')


# ---------------------------------------------------------------- A: one beam at a time

def bar(fn, base, thick, sign=1):
    """A beam of constant thickness following its own deflected line."""
    es = [-12 + 24 * k / 96 for k in range(97)]
    top = [f"{X(e):.1f},{base + sign * fn(e) * EXAG:.1f}" for e in es]
    bot = [f"{X(e):.1f},{base + sign * fn(e) * EXAG + thick:.1f}" for e in reversed(es)]
    return f'<polygon class="part" points="{" ".join(top + bot)}"/>'


def face(fn, base, sign=1):
    es = [-12 + 24 * k / 96 for k in range(97)]
    return " ".join(f"{X(e):.1f},{base + sign * fn(e) * EXAG:.1f}" for e in es)


def fig_beams():
    w, h = 1400, 740
    g = [txt(w / 2, 46, "Each half bends about its own root, and the roots are at opposite ends",
             "h", "middle"),
         txt(w / 2, 72, f"Left to right is true scale. Up and down is drawn "
                        f"{EXAG / SX:.0f} times bigger, or none of it would show.", "g", "middle")]
    for panel, (lab, left, fn) in enumerate((
            ("The leaf. Rooted at the mouth end, so it hardly moves there and swings "
             "hugely at the far end.", True, leaf),
            ("The ear. Rooted at the far end, so it does the opposite, and by much less.",
             False, ear))):
        oy = 170 + panel * 330
        g.append(txt(LM, oy - 46, lab, "s"))
        g.append(f'<path class="ghost" d="M {X(-12):.1f},{oy:.1f} H {X(12):.1f}"/>')
        g.append(bar(fn, oy, 14))
        rx = X(-12) if left else X(12)
        g.append(hatch(rx, oy - 24, 62, 1 if left else -1))
        g.append(txt(rx + (-18 if left else 18), oy - 30, "rooted here", "g",
                     "end" if left else "start"))
        for e, tag in ((-8.813, "at the mouth"), (0.0, "in the middle"),
                       (8.813, "at the far end")):
            d = fn(e)
            g.append(f'<path class="dim" d="M {X(e):.1f},{oy:.1f} V {oy + d * EXAG:.1f}"/>')
            g.append(f'<circle cx="{X(e):.1f}" cy="{oy + d * EXAG:.1f}" r="4" class="live"/>')
            g.append(txt(X(e) + 12, oy + d * EXAG + (5 if d > 0.1 else 22), f"{d:.3f} mm", "n"))
            g.append(txt(X(e), oy - 12, tag, "g", "middle"))
    g.append(txt(LM, h - 44,
                 "The leaf moves ten times as far at one end as at the other. That tilt is "
                 "the whole story of the next picture.", "s"))
    return svg("".join(g), w, h, "each half bends about its own root")


# ---------------------------------------------------------------- B: the wedge

def fig_wedge():
    w, h, datum = 1400, 1120, 300
    gap = lambda e: leaf(e) + ear(e)
    need = lambda e: STUB_PROUD - GAP if e == 0.0 else TOOTH_PROUD - GAP
    g = [txt(w / 2, 46, "Put them face to face and the joint opens as a wedge", "h", "middle"),
         txt(w / 2, 72, "Each tooth is drawn its own height. A tooth is touching only if it "
                        "reaches the ear.", "g", "middle")]
    g.append(f'<polygon class="air" points="{face(ear, datum, -1)} '
             f'{" ".join(reversed(face(leaf, datum).split()))}"/>')
    g.append(bar(ear, datum - 44, 44, -1))
    g.append(hatch(X(12), datum - 88, 44, -1))
    g.append(txt(X(12) + 16, datum - 96, "the ear, rooted here", "g"))
    g.append(bar(leaf, datum, 44))
    g.append(hatch(X(-12), datum, 44, 1))
    g.append(txt(X(-12) - 16, datum - 8, "the leaf, rooted here", "g", "end"))
    for e in ETAS:
        base = datum + leaf(e) * EXAG
        top = base - need(e) * EXAG
        live = e in CARRY
        hw = 9 if e == 0.0 else 7
        g.append(f'<path class="{"live" if live else "tooth"}" d="M {X(e) - hw:.1f},{base:.1f} '
                 f'V {top + hw:.1f} a {hw},{hw} 0 0 1 {2 * hw},0 V {base:.1f} Z"/>')
        if not live:
            g.append(f'<path class="rule" d="M {X(e):.1f},{top:.1f} '
                     f'V {datum - ear(e) * EXAG:.1f}"/>')
    for e, note, dy in ((-8.813, "touching. this one tooth is the whole load", 0),
                        (0.0, "the axle, taller, so it just reaches too", 34),
                        (8.813, "needs 0.600, is handed 1.304, so 0.704 of air", 68)):
        yy = 150 + dy
        g.append(f'<path class="{"dim" if e in CARRY else "rule"}" d="M {X(e):.1f},{yy + 6:.1f} '
                 f'V {datum - ear(e) * EXAG - 46:.1f}"/>')
        g.append(txt(X(e), yy, note, "n" if e in CARRY else "g", "middle"))
    # the same gap, laid flat
    fy, fs = 900, 150
    g.append(txt(LM, fy - 230, "The same gap, with the lean taken out", "s"))
    g.append(f'<path class="axis" d="M {X(-12):.1f},{fy:.1f} H {X(12):.1f}"/>')
    g.append(f'<polygon class="air" points="'
             + " ".join(f"{X(e):.1f},{fy - gap(e) * fs:.1f}" for e in ETAS)
             + f' {X(8.813):.1f},{fy - 0.6 * fs:.1f} {X(-8.813):.1f},{fy - 0.6 * fs:.1f}"/>')
    for v, lab in ((0.6, "what a tooth needs, 0.600"), (0.9, "what the axle needs, 0.900")):
        g.append(f'<path class="dim" stroke-dasharray="7 5" d="M {X(-12):.1f},'
                 f'{fy - v * fs:.1f} H {X(12):.1f}"/>')
        g.append(txt(X(12) + 14, fy - v * fs + 5, lab, "n"))
    g.append('<polyline fill="none" stroke="#1d262e" stroke-width="2.5" points="'
             + " ".join(f"{X(e):.1f},{fy - gap(e) * fs:.1f}" for e in ETAS) + '"/>')
    for e in ETAS:
        g.append(f'<circle cx="{X(e):.1f}" cy="{fy - gap(e) * fs:.1f}" '
                 f'r="{6 if e in CARRY else 4}" class="{"live" if e in CARRY else "tooth"}"/>')
    g.append(txt(X(-8.813), fy + 26, "mouth end", "g", "middle"))
    g.append(txt(X(8.813), fy + 26, "far end", "g", "middle"))
    g.append(txt(LM, h - 44,
                 "The shaded band is air. One tooth sits on the line it needs; every other "
                 "tooth floats above it.", "s"))
    return svg("".join(g), w, h, "the joint opens as a wedge")


# ---------------------------------------------------------------- D: the handover

def solve_at(s):
    """Which station carries, and how much, at separation s. Same active set walk."""
    merged = {e: TOOTH_PROUD - GAP for e in ETAS if e - s > -NOSE + 1e-9}
    if s < NOSE:
        merged[0.0] = max(merged.get(0.0, 0), STUB_PROUD - GAP)
    ks = sorted(merged)
    Aa = [e + 12 for e in ks]
    Bb = [12 - e + s for e in ks]
    C = [[comp(Aa[i], Aa[j], EIL) + comp(Bb[i], Bb[j], EIE) for j in range(len(ks))]
         for i in range(len(ks))]
    act = list(range(len(ks)))
    for _ in range(80):
        m = len(act)
        M = [[C[i][j] for j in act] + [merged[ks[i]]] for i in act]
        for c in range(m):
            p = max(range(c, m), key=lambda r: abs(M[r][c]))
            M[c], M[p] = M[p], M[c]
            for r in range(m):
                if r != c and M[r][c]:
                    f = M[r][c] / M[c][c]
                    for cc in range(c, m + 1):
                        M[r][cc] -= f * M[c][cc]
        F = [0.0] * len(ks)
        for k, i in enumerate(act):
            F[i] = M[k][m] / M[k][k]
        neg = [i for i in act if F[i] < -1e-12]
        if neg:
            act = [i for i in act if i != neg[0]]
            continue
        d = [sum(C[i][j] * F[j] for j in range(len(ks))) for i in range(len(ks))]
        bad = [i for i in range(len(ks)) if i not in act and d[i] < merged[ks[i]] - 1e-9]
        if not bad:
            break
        act = sorted(act + [bad[0]])
    return ks, F


def fig_stroke():
    w, h = 1400, 800
    sx, lm, gapy = 26.0, 380.0, 34
    Xs = lambda z: lm + (z + 12) * sx            # in the fork's frame, its mouth at zeta -12
    g = [txt(w / 2, 46, "Through the stroke the load hands off, always to the newest tooth in",
             "h", "middle"),
         txt(w / 2, 72, "The blade slides right into the fork&#8217;s slot. s is how far it "
                        "still has to go. The bars are held apart to show the teeth; a tooth "
                        "labeled with a force is one that is touching.",
             "g", "middle")]
    for row, s in enumerate((12.0, 8.0, 4.0, 1.4)):
        oy = 160 + row * 150
        ks, F = solve_at(s)
        tot = 2 * sum(F) / 9.81
        g.append(f'<rect class="part" x="{Xs(-12):.1f}" y="{oy:.1f}" '
                 f'width="{24 * sx:.1f}" height="30"/>')
        g.append(txt(Xs(-12) - 14, oy + 20, "the fork", "g", "end"))
        g.append(f'<path class="axis" d="M {Xs(-12):.1f},{oy - 12:.1f} '
                 f'V {oy + 30 + gapy + 42:.1f}"/>')
        if row == 0:
            g.append(txt(Xs(-12) + 8, oy - 18, "the slot&#8217;s mouth", "g"))
        by = oy + 30 + gapy
        g.append(f'<rect class="part" x="{Xs(-12 - s + S):.1f}" y="{by:.1f}" '
                 f'width="{24 * sx:.1f}" height="30"/>')
        if row == 0:
            g.append(txt(Xs(-12 - s + S) - 14, by + 20, "the blade", "g", "end"))
        for e in ETAS:
            f = F[ks.index(e)] if e in ks else 0.0
            cx = Xs(e - s)
            g.append(f'<path class="{"live" if f > 1e-9 else "tooth"}" d="M {cx - 5:.1f},{by:.1f} '
                     f'V {by - 12:.1f} a 5,5 0 0 1 10,0 V {by:.1f} Z"/>')
            if f > 1e-9:
                g.append(f'<path class="dim" d="M {cx:.1f},{by - 17:.1f} V {oy + 34:.1f}"/>')
                g.append(txt(cx, by - 22, f"{f:.1f} N", "n", "middle"))
        g.append(txt(w - 30, oy + 22, f"s = {s:g} mm", "s", "end"))
        g.append(txt(w - 30, oy + 44, f"{sum(1 for e in ETAS if e - s > -NOSE + 1e-9)}"
                                      f" teeth inside the slot", "g", "end"))
        g.append(txt(w - 30, oy + 64, f"{tot:.2f} kgf to push", "n", "end"))
    g.append(txt(lm - 300, h - 44,
                 "The tooth that carries is never the one that went in first. It is the one "
                 "nearest the mouth, which is the one that just entered.", "s"))
    return svg("".join(g), w, h, "the load hands off to the newest tooth in")


def render(path):
    """Rasterize one SVG, so the published page can carry a PNG next to its source."""
    from playwright.sync_api import sync_playwright
    png = path.with_suffix(".png")
    with sync_playwright() as pw:
        b = pw.chromium.connect_over_cdp("http://127.0.0.1:9223")
        page = b.contexts[0].new_page()
        page.set_viewport_size({"width": 1500, "height": 1900})
        page.set_content("<style>html,body{margin:0;background:#fff}</style>" + path.read_text())
        page.wait_for_timeout(500)
        page.locator("svg").screenshot(path=str(png))
        page.close()
    print(f"  {png.name}  {png.stat().st_size:,} bytes")


FIGS = (("beams", fig_beams), ("wedge", fig_wedge), ("stroke", fig_stroke))

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    print(f"contacts: {F0:.1f} N at the last tooth in, {F1:.1f} N at the axle")
    parts = []
    for name, fn in FIGS:
        s = fn()
        (OUT / f"{name}.svg").write_text(s)
        print(f"  {name}.svg  {len(s):,} bytes")
        if "--no-render" not in sys.argv:
            render(OUT / f"{name}.svg")
        parts.append(f'<figure><img src="source/images/{name}.svg" alt="{name}"></figure>')
    (pathlib.Path(__file__).parent / "changes-pictures.html").write_text(
        "<!doctype html><meta charset='utf-8'><title>Why one tooth carries</title>"
        "<style>body{margin:40px auto;max-width:1400px;font-family:Helvetica,Arial,sans-serif}"
        "figure{margin:0 0 48px}img{width:100%;border:1px solid #d7e0e6}</style>"
        "<h1>Why only one tooth is touching</h1>" + "".join(parts))
    print("  changes-pictures.html")
