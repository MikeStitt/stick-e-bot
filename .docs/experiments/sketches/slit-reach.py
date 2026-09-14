"""Draw whether the relief slits reach inside the mouth, looking down the socket axis.

Writes slit-reach.html beside itself. Every number and every path point is computed
from the inputs of a sizing, so changing a number here redraws the picture rather
than needing the drawing edited to match.

The test is `mouth radius - #slit_in`, positive meaning the slit breaks through into
the mouth. That is what severs the collar's ring of material into four tabs. If it is
negative the slit stops in the material and leaves a continuous ring, and the tabs
cannot spread however deep the slit is cut.
"""
import math
import pathlib

WALL = {6.0: 1.5, 12.0: 3.0}          # socket wall follows the ball


class Sizing:
    def __init__(self, key, title, note, ball, stalk, fit, grip,
                 slit_w, slit_in, slit_out):
        self.key, self.title, self.note = key, title, note
        self.ball, self.stalk, self.fit, self.grip = ball, stalk, fit, grip
        self.slit_w, self.slit_in, self.slit_out = slit_w, slit_in, slit_out
        self.r = ball / 2
        self.wall = WALL[ball]
        self.cav = self.r + fit
        self.mouth_r = (self.cav ** 2 - grip ** 2) ** 0.5
        self.mouth = 2 * self.mouth_r
        # #ball + 2*#wall, per build-briefs/ball-and-socket.md: the fit is left out on
        # purpose, so a printing clearance changes the hollow and nothing else.
        self.collar = ball + 2 * self.wall
        self.collar_r = self.collar / 2
        self.material = self.collar_r - self.cav
        self.retention = ball - self.mouth
        self.reach = self.mouth_r - self.slit_in       # + means it breaks into the mouth
        self.severed = self.reach > 0
        self.past_rim = self.slit_out - self.collar_r
        # the #grip at which the slit would stop exactly on the mouth
        self.grip_ceiling = (self.cav ** 2 - self.slit_in ** 2) ** 0.5
        self.swing = math.degrees(math.acos((stalk / 2) / self.cav)
                                  - math.asin(grip / self.cav))


SIZINGS = [
    Sizing("a", "Current CAD", "as built in stickbot-for-bot-review",
           6.0, 3.0, 0.2, 1.35, 0.8, 2.5, 6.0),
    Sizing("b", "Twice as big, settled", "#fit 0.08, #grip derived, every slit number doubled",
           12.0, 6.0, 0.08, ((6.0 + 0.08) ** 2 - (0.48 * 12.0) ** 2) ** 0.5, 1.6, 5.0, 12.0),
    Sizing("c", "Past the ceiling", "#grip 4.75 — drawn to show what short looks like",
           12.0, 6.0, 0.08, 4.75, 1.6, 5.0, 12.0),
]

PX = 10.6          # px per mm, the same for every panel so the sizes compare
W, H = 320, 300
CX, CY = 160.0, 148.0
ANGLES = [0, 90, 180, 270]


def circle_pts(rad, n=180):
    """Points around a circle centered on the panel, in SVG coordinates."""
    return [(CX + rad * PX * math.cos(2 * math.pi * i / n),
             CY + rad * PX * math.sin(2 * math.pi * i / n)) for i in range(n)]


def path(points, close=True):
    d = "M " + " L ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    return d + (" Z" if close else "")


def annulus(r_out, r_in):
    """Two subpaths for an even-odd fill: the ring between two radii."""
    return path(circle_pts(r_out)) + " " + path(circle_pts(r_in))


def ray(deg, mm):
    """A point mm out from the center along a ray, in SVG coordinates."""
    a = math.radians(deg)
    return (CX + mm * PX * math.cos(a), CY + mm * PX * math.sin(a))


def slit_rect(deg, r0, r1, width):
    a = math.radians(deg)
    ux, uy = math.cos(a), math.sin(a)
    px, py = -uy, ux
    h = width / 2
    pts = []
    for r, s in ((r0, -1), (r1, -1), (r1, 1), (r0, 1)):
        pts.append((CX + (r * ux + s * h * px) * PX,
                    CY + (r * uy + s * h * py) * PX))
    return path(pts)


def panel(s):
    """One top view, looking down the socket axis at the mouth."""
    g = []

    # The ball, seen through the mouth.
    g.append(f'<circle class="ball" cx="{CX}" cy="{CY}" r="{s.mouth_r * PX:.2f}"/>')

    # The collar's ring of material, from the mouth out to the outside diameter.
    g.append(f'<path class="socket" fill-rule="evenodd" '
             f'd="{annulus(s.collar_r, s.mouth_r)}"/>')

    # When the slits stop short, the ring they fail to sever.
    if not s.severed:
        g.append(f'<path class="bridge" fill-rule="evenodd" '
                 f'd="{annulus(s.slit_in, s.mouth_r)}"/>')

    # The four slits. Each removes material only from the mouth outward — inside the
    # mouth there is nothing to remove — so the part of the cut that reaches inside is
    # drawn as an outline over the ball. Past the outside diameter it is dashed, so the
    # reader can see it clears the rim.
    start = max(s.slit_in, s.mouth_r)
    for deg in ANGLES:
        g.append(f'<path class="cut" d="{slit_rect(deg, start, s.collar_r, s.slit_w)}"/>')
        if s.severed:
            g.append(f'<path class="cut inner" '
                     f'd="{slit_rect(deg, s.slit_in, s.mouth_r, s.slit_w)}"/>')
        x0, y0 = ray(deg, s.collar_r)
        x1, y1 = ray(deg, s.slit_out)
        g.append(f'<line class="beyond" x1="{x0:.2f}" y1="{y0:.2f}" '
                 f'x2="{x1:.2f}" y2="{y1:.2f}"/>')

    # The mouth, drawn last so it reads across the slits.
    g.append(f'<circle class="mouth" cx="{CX}" cy="{CY}" r="{s.mouth_r * PX:.2f}"/>')

    # The measurement, on the slit pointing east.
    lo, hi = sorted((s.slit_in, s.mouth_r))
    x0, y0 = ray(0, lo)
    x1, y1 = ray(0, hi)
    cls = "good" if s.severed else "bad"
    g.append(f'<line class="reach {cls}" x1="{x0:.2f}" y1="{y0:.2f}" '
             f'x2="{x1:.2f}" y2="{y1:.2f}"/>')
    label = (f"{s.reach:+.3f} inside" if s.severed else f"{-s.reach:.3f} short")
    g.append(f'<text class="reachlabel {cls}" x="{CX + s.mouth_r * PX + 8:.2f}" '
             f'y="{CY - 5}">{label}</text>')

    # Radii, called out on the slit pointing north.
    g.append(f'<text x="{CX + 5}" y="{CY - s.mouth_r * PX - 6:.2f}" '
             f'class="tick">mouth r {s.mouth_r:.3f}</text>')
    g.append(f'<text x="{CX + 5}" y="{CY - s.collar_r * PX - 6:.2f}" '
             f'class="tick">collar r {s.collar_r:.1f}</text>')
    g.append(f'<text x="{CX + 5}" y="{CY - s.slit_out * PX - 6:.2f}" '
             f'class="tick">#slit_out {s.slit_out:.1f}</text>')
    g.append(f'<text x="{CX - 4}" y="{CY + s.slit_in * PX + 13:.2f}" '
             f'class="tick" text-anchor="end">#slit_in {s.slit_in:.1f}</text>')

    return (f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{s.title}: the socket seen '
            f'down its axis, with four relief slits '
            f'{"cutting through into the mouth" if s.severed else "stopping short of the mouth"}">'
            + "".join(g) + '</svg>')


ROWS = [
    ("Ball &#216;", "ball", "{:.1f}"),
    ("<code>#fit</code>", "fit", "{:.2f}"),
    ("<code>#grip</code>", "grip", "{:.2f}"),
    ("Mouth radius", "mouth_r", "{:.3f}"),
    ("<code>#slit_in</code>", "slit_in", "{:.1f}"),
    ("Reach inside the mouth", "reach", "{:+.3f}"),
    ("<code>#slit_out</code>", "slit_out", "{:.1f}"),
    ("Slit past the rim", "past_rim", "{:.1f}"),
    ("<code>#grip</code> ceiling", "grip_ceiling", "{:.3f}"),
    ("Swing", "swing", "{:.1f}&#176;"),
]
KEY = {"reach"}


def table():
    head = "".join(f"<th>{s.title}</th>" for s in SIZINGS)
    body = []
    for label, attr, fmt in ROWS:
        cells = []
        for s in SIZINGS:
            v = getattr(s, attr)
            bad = ' class="bad"' if attr == "reach" and v <= 0 else ""
            cells.append(f"<td{bad}>{fmt.format(v)}</td>")
        cls = ' class="key"' if attr in KEY else ""
        body.append(f"<tr{cls}><th>{label}</th>{''.join(cells)}</tr>")
    return ('<div class="tablewrap"><table><thead><tr><th></th>' + head +
            "</tr></thead><tbody>" + "".join(body) + "</tbody></table></div>")


CSS = """
:root{
  --ground:#f7f8fa; --panel:#ffffff; --ink:#171b21; --muted:#5d6673; --rule:#d5dae2;
  --ball:#3f6fa8; --ball-fill:#c9dcf0; --socket:#8a6a1f; --socket-fill:#f0dfae;
  --good:#1f7a4d; --bad:#b3341f; --bridge:#f2c3b6;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#12151a; --panel:#1a1f27; --ink:#e6eaf0; --muted:#98a2b1; --rule:#2f3742;
    --ball:#8fbbe8; --ball-fill:#23364c; --socket:#e0bf70; --socket-fill:#3a3324;
    --good:#5fd39a; --bad:#ff8a70; --bridge:#5c2a1e;
  }
}
:root[data-theme="dark"]{
  --ground:#12151a; --panel:#1a1f27; --ink:#e6eaf0; --muted:#98a2b1; --rule:#2f3742;
  --ball:#8fbbe8; --ball-fill:#23364c; --socket:#e0bf70; --socket-fill:#3a3324;
  --good:#5fd39a; --bad:#ff8a70; --bridge:#5c2a1e;
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
  font:16px/1.6 ui-sans-serif,system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;
  padding:2.4rem 1.2rem 4rem}
.wrap{max-width:1080px;margin:0 auto}
h1{font-size:1.7rem;line-height:1.2;margin:0 0 .3rem;letter-spacing:-.01em;text-wrap:balance}
.sub{color:var(--muted);margin:0 0 2.2rem;max-width:62ch}
h2{font-size:1.05rem;margin:2.6rem 0 .8rem;letter-spacing:.04em;text-transform:uppercase;
  color:var(--muted);font-weight:650}
p{max-width:68ch}
.panels{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(280px,1fr))}
.panel{background:var(--panel);border:1px solid var(--rule);border-radius:10px;padding:1rem .6rem .4rem}
.panel h3{margin:0 .6rem;font-size:.95rem}
.panel .note{margin:.15rem .6rem 0;color:var(--muted);font-size:.82rem}
.panel svg{display:block;width:100%;height:auto}
.verdict{margin:0 .6rem .8rem;font-size:.85rem;font-weight:650}
.verdict.no{color:var(--bad)} .verdict.yes{color:var(--good)}
.ball{fill:var(--ball-fill);stroke:none}
.socket{fill:var(--socket-fill);stroke:var(--socket);stroke-width:1.4}
.bridge{fill:var(--bridge);stroke:var(--bad);stroke-width:1.4}
.cut{fill:var(--panel);stroke:var(--socket);stroke-width:1.2}
.cut.inner{fill:none;stroke-dasharray:3 2;opacity:.85}
.beyond{stroke:var(--socket);stroke-width:1.2;stroke-dasharray:3 3;opacity:.7}
.mouth{fill:none;stroke:var(--ball);stroke-width:2.4}
.reach{stroke-width:5;stroke-linecap:round}
.reach.good{stroke:var(--good)} .reach.bad{stroke:var(--bad)}
.reachlabel{font-size:13px;font-weight:700}
.reachlabel.good{fill:var(--good)} .reachlabel.bad{fill:var(--bad)}
text{font:11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;fill:var(--muted)}
.tablewrap{overflow-x:auto}
table{border-collapse:collapse;width:100%;font-variant-numeric:tabular-nums;
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.87rem;min-width:520px}
th,td{padding:.42rem .7rem;border-bottom:1px solid var(--rule);text-align:right}
thead th{text-align:right;font-size:.78rem;line-height:1.3;color:var(--muted);
  border-bottom:2px solid var(--rule);vertical-align:bottom;
  font-family:ui-sans-serif,system-ui,sans-serif}
tbody th{text-align:left;font-weight:400;color:var(--muted);white-space:nowrap;
  font-family:ui-sans-serif,system-ui,sans-serif}
tr.key td,tr.key th{font-weight:700;color:var(--ink)}
td.bad{color:var(--bad);font-weight:700}
code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:.92em}
.callout{border-left:3px solid var(--good);padding:.1rem 0 .1rem 1rem;margin:1.4rem 0}
.callout p{margin:.5rem 0}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--rule);
  color:var(--muted);font-size:.82rem}
"""


def build():
    panels = []
    for s in SIZINGS:
        v = ("four separate tabs" if s.severed else "one ring, the tabs cannot spread")
        panels.append(
            f'<div class="panel"><h3>{s.title}</h3>'
            f'<p class="note">{s.note}</p>{panel(s)}'
            f'<p class="verdict {"yes" if s.severed else "no"}">'
            f'{"&#10003;" if s.severed else "&#10007;"} {v}</p></div>')

    b, c = SIZINGS[1], SIZINGS[2]
    html = f"""<title>Slit Reach</title>
<style>{CSS}</style>
<div class="wrap">
<h1>Do the relief slits reach inside the mouth?</h1>
<p class="sub">The socket seen down its own axis, at true relative scale. Gold is the collar's
material; the blue circle is the mouth, with the ball visible through it. A slit does its job
only if it crosses that circle &mdash; that is what cuts the ring into four tabs that can spread.</p>

<div class="panels">
{"".join(panels)}
</div>

<div class="callout">
<p><strong>Doubling the slit numbers keeps the slit working, with room to spare.</strong> The built
robot reaches {SIZINGS[0].reach:.3f}&#8239;mm inside its mouth. At 2&#215; the same proportions
reach {b.reach:.3f}&#8239;mm inside &mdash; nearly twice as far in absolute terms, and
{b.reach / (2 * SIZINGS[0].reach) * 100:.0f}% of the {2 * SIZINGS[0].reach:.3f} a pure doubling
would have given. What separates the two is the mouth: the built joint's is
{100 * SIZINGS[0].mouth / SIZINGS[0].ball:.1f}% of its ball, and the settled one is held at exactly
96% at any <code>#fit</code>, so the doubled mouth is proportionally the narrower of the two.</p>
<p><strong>The ceiling is <code>#grip</code> {b.grip_ceiling:.3f}.</strong> Every millimeter of
<code>#grip</code> pulls the mouth inward, and at {b.grip_ceiling:.3f} the mouth arrives at
<code>#slit_in</code> and the slit stops breaking through. The settled {b.grip:.4f} sits a full
{b.grip_ceiling - b.grip:.2f}&#8239;mm below that. The third panel is drawn past it, at
{c.grip:.2f}, so the failure has a picture beside the working one.</p>
</div>

<h2>The numbers</h2>
{table()}

<h2>Why a short slit is worse than it looks</h2>
<p>A slit that stops short still cuts most of the way through, so the part looks slit from every
angle except this one. What survives is a thin continuous band of material between the mouth and
the slit's inner end &mdash; the pink ring in the third panel. That band ties all four tabs
together at their weakest radius, so pressing the ball in loads it in hoop tension instead of
bending four tabs outward. It is stiff, and then it splits. The failure mode is a cracked socket
rather than a stiff one, which is why this is checked by arithmetic before the part is printed.</p>

<footer>Drawn by <code>.docs/experiments/sketches/slit-reach.py</code> from each sizing's ball,
stalk, <code>#fit</code>, <code>#grip</code> and three slit numbers. Every other number on this
page is derived: the mouth radius is
&#8730;(<code>#cavity_r</code>&#178;&#8239;&#8722;&#8239;<code>#grip</code>&#178;), the collar is
<code>#ball&#8239;+&#8239;2&#215;#wall</code> with the fit deliberately left out, and the reach is
the mouth radius less <code>#slit_in</code>. Stickbot's built collar is &#216;9.4 because it
predates that collar rule; the ring drawn here is the rule's &#216;9.0.</footer>
</div>
"""
    out = pathlib.Path(__file__).parent / "slit-reach.html"
    out.write_text(html)
    print(f"wrote {out}")
    for s in SIZINGS:
        print(f"  {s.title:26s} mouth r {s.mouth_r:6.3f}  #slit_in {s.slit_in:4.1f}  "
              f"reach {s.reach:+7.3f}  ceiling {s.grip_ceiling:6.3f}  "
              f"{'severed' if s.severed else 'RING'}")


build()
