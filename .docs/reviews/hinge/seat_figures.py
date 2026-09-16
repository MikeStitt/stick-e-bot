"""What the sharp rim does to the hold as it wears.

It drew the land as well, until the slot's relief was dropped and the ear's inner face became
one plane; that half of the file went with it, and so did ``source/images/seat.svg``.

Every length is computed from the same numbers as the text. Only the magnification is
chosen by hand, and each sheet says what it is.
"""
import math
import pathlib
import sys

R, RT2 = 12.0, math.sqrt(2)
BUMP_R, BASE, VALLEY_D = 9.109, 1.6, 1.2
TOOTH, GAP = 0.6, 0.2
FLAT = BASE - 2 * TOOTH                      # 0.4 on top of the cone
HW = lambda z: math.sqrt(R * R - z * z)      # half width of a face this far off the mid-plane
OUT = pathlib.Path(__file__).parent / "source" / "images"

CSS = """
 .fork{fill:#dbe6ee;stroke:#1d262e;stroke-width:1.1;stroke-linejoin:round}
 .blade{fill:#f9e3ed;stroke:#1d262e;stroke-width:1.1;stroke-linejoin:round}
 .land{fill:#a9c8de;stroke:#1d262e;stroke-width:1.1;stroke-linejoin:round}
 .cham{fill:#c5d9e8;stroke:#1d262e;stroke-width:.9;stroke-linejoin:round}
 .hole{fill:#ffffff;stroke:#1d262e;stroke-width:.9}
 .worn{fill:#b8156e;stroke:none;opacity:.45}
 .ghost{fill:none;stroke:#8fa3b0;stroke-width:1;stroke-dasharray:5 3}
 .dim{stroke:#b8156e;stroke-width:1;fill:none}
 .lead{stroke:#5b6b78;stroke-width:.8;fill:none}
 .hit{fill:#b8156e;stroke:#fff;stroke-width:1}
 text{font-family:'Helvetica Neue',Helvetica,Arial,sans-serif;fill:#1d262e}
 .h{font-size:19px;font-weight:600} .s{font-size:14px}
 .n{font-size:12px;fill:#b8156e} .g{font-size:12px;fill:#5b6b78}
"""


def svg(body, w, h, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" '
            f'height="{h}"><title>{title}</title><style>{CSS}</style>'
            f'<rect width="{w}" height="{h}" fill="#ffffff"/>{body}</svg>')


def txt(x, y, s, cls="s", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" class="{cls}" text-anchor="{anchor}">{s}</text>'


def poly(cls, pts):
    return f'<polygon class="{cls}" points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + '"/>'


def vdim(x, ya, yb, label, side=1, out=34, cls="n"):
    """A height between two page y values, dimensioned at x + side*out."""
    tip = x + side * out
    a, b = min(ya, yb), max(ya, yb)
    head = lambda y, d: (f'<path class="dim" d="M {tip:.1f},{y:.1f} l -3.5,{d * 6} '
                         f'm 7,0 l -3.5,{-d * 6}"/>')
    if b - a > 34:
        line = f'<path class="dim" d="M {tip:.1f},{a:.1f} V {b:.1f}"/>' + head(a, 1) + head(b, -1)
    else:
        line = (f'<path class="dim" d="M {tip:.1f},{a - 20:.1f} V {b + 20:.1f}"/>'
                + head(a, -1) + head(b, 1))
    return "".join((
        f'<path class="lead" d="M {x:.1f},{a:.1f} H {tip + side * 7:.1f}"/>',
        f'<path class="lead" d="M {x:.1f},{b:.1f} H {tip + side * 7:.1f}"/>',
        line, txt(tip + side * 9, (a + b) / 2 + 4, label, cls,
                  "start" if side > 0 else "end")))


# ------------------------------------------------------- 1: where the seat and the fit live

LO, HI, XB, XT, SC = 7.4, 11.2, 4.85, 6.10, 260.0


STUB, BORE_D, STUB_PROUD = 4.0, 4.4, 1.0


# --------------------------------------------------------------- 2: the rim, and its wear

def fig_rim():
    w, h, sc = 1400, 780, 150.0
    g = [txt(w / 2, 44, "The cone lands on a corner, and the corner does not stay sharp",
             "h", "middle"),
         txt(w / 2, 70, f"The same cone and valley, drawn {sc:.0f} times full size, sectioned "
                        f"the way it slides. The whole load runs through the rim&#8217;s edge.",
             "g", "middle")]
    for i, (lab, x, rho) in enumerate((("seated, new", 0.0, 0.0),
                                       ("at the top of its climb", 0.4, 0.0),
                                       ("seated again, after the rim has worn 0.10",
                                        0.0, 0.10))):
        ox, oy = 224 + i * 464, 360
        lift = GAP + x + RT2 * rho
        X = lambda t: ox + t * sc
        Y = lambda v: oy - v * sc
        g.append(poly("blade", [(X(-1.45), Y(0)), (X(x - BASE / 2), Y(0)),
                                (X(x - FLAT / 2), Y(TOOTH)), (X(x + FLAT / 2), Y(TOOTH)),
                                (X(x + BASE / 2), Y(0)), (X(1.45), Y(0)),
                                (X(1.45), Y(-0.42)), (X(-1.45), Y(-0.42))]))
        for s in (-1, 1):
            e, sw = s * VALLEY_D / 2, 1 if s > 0 else 0
            arc = (f'A {rho * sc:.1f},{rho * sc:.1f} 0 0 {sw} '
                   f'{X(e + s * rho):.1f},{Y(lift):.1f}') if rho else ''
            g.append(f'<path class="fork" d="M {X(e):.1f},{Y(1.12):.1f} '
                     f'V {Y(lift + rho):.1f} {arc} H {X(s * 1.45):.1f} '
                     f'V {Y(1.12):.1f} Z"/>')
            if rho:
                g.append(f'<path class="worn" d="M {X(e):.1f},{Y(lift + rho):.1f} '
                         f'V {Y(lift):.1f} H {X(e + s * rho):.1f} '
                         f'A {rho * sc:.1f},{rho * sc:.1f} 0 0 {1 - sw} '
                         f'{X(e):.1f},{Y(lift + rho):.1f} Z"/>')
            if s > 0 or x == 0:
                cx = s * (VALLEY_D / 2 + rho) - s * rho / RT2
                g.append(f'<circle class="hit" cx="{X(cx):.1f}" '
                         f'cy="{Y(lift - rho + rho / RT2):.1f}" r="4.5"/>')
        g.append(f'<path class="ghost" d="M {X(-1.45):.1f},{Y(TOOTH):.1f} '
                 f'H {X(1.45):.1f}"/>')
        g.append(vdim(X(-1.40), Y(0), Y(lift), f"{lift:.3f}", 1, 18))
        g.append(txt(ox, oy + 108, lab, "s", "middle"))
        g.append(txt(ox, oy + 130, "the faces stand this far apart", "g", "middle"))
        g.append(txt(ox, oy + 152,
                     "riding the land" if x else f"{TOOTH - lift:.3f} of climb left",
                     "n", "middle"))
    g.append(txt(70, h - 208, "A round on the rim, whether it is designed in or worn in, holds "
                              "the cone up off its seat by 1.414 times the radius, so the joint "
                              "loses that much", "s"))
    g.append(txt(70, h - 186, "of its climb before it ever starts to turn. Hold goes with "
                              "climb:", "s"))
    for i, rho in enumerate((0.0, 0.05, 0.10, 0.15)):
        climb = TOOTH - GAP - RT2 * rho
        g.append(txt(110 + i * 310, h - 146, f"rim round {rho:.2f} &#8594; climb "
                                             f"{climb:.3f}", "s"))
        g.append(txt(110 + i * 310, h - 124, f"holds {100 * climb / (TOOTH - GAP):.0f}% of new",
                     "n"))
    g.append(txt(70, h - 76, "This is why the 0.1 round that used to sit on the valley&#8217;s "
                             "rim was worth taking off, and why the joint will feel looser "
                             "after a few dozen presses", "s"))
    g.append(txt(70, h - 54, "than it does on the first one. Size the tooth for the worn "
                             "number, not the new one.", "s"))
    return svg("".join(g), w, h, "the rim and its wear")


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


HERE = pathlib.Path(__file__).parent
OUT.mkdir(parents=True, exist_ok=True)
parts = []
for name, fn in (("rim", fig_rim),):
    s = fn()
    (OUT / f"{name}.svg").write_text(s)
    print(f"  {name}.svg  {len(s):,} bytes")
    if "--no-render" not in sys.argv:
        render(OUT / f"{name}.svg")
    parts.append(f'<figure><img src="source/images/{name}.svg" alt="{name}"></figure>')
(HERE / "seat-pictures.html").write_text(
    "<!doctype html><meta charset='utf-8'><title>The seat and the rim</title>"
    "<style>body{margin:40px auto;max-width:1400px;font-family:Helvetica,Arial,sans-serif}"
    "figure{margin:0 0 48px}img{width:100%;border:1px solid #d7e0e6}</style>"
    "<h1>The seat and the rim</h1>" + "".join(parts))
print("  seat-pictures.html")
