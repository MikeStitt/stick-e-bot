"""Draw how far the socket wraps around the ball, for three sizings of the joint.

Writes socket-wrap.html beside itself. Every number and every path point is computed
from the four inputs of a sizing — ball, stalk, fit, grip — so changing a number here
redraws the picture rather than needing the drawing edited to match.

The measure of "how far it wraps" is taken on the BALL, not on the cavity: the mouth
plane sits `grip` above the ball's center, so the socket reaches asin(grip / ball_r)
past the equator and the wrap is 90 deg more than that.
"""
import math
import pathlib

WALL = {6.0: 1.5, 12.0: 3.0}          # socket wall follows the ball


class Sizing:
    def __init__(self, key, title, note, ball, stalk, fit, grip):
        self.key, self.title, self.note = key, title, note
        self.ball, self.stalk, self.fit, self.grip = ball, stalk, fit, grip
        self.r = ball / 2
        self.wall = WALL[ball]
        self.cav = self.r + fit
        self.mouth = 2 * (self.cav ** 2 - grip ** 2) ** 0.5
        # #ball + 2*#wall, per build-briefs/ball-and-socket.md: the fit is deliberately
        # left out, so a printing clearance changes the hollow and nothing else. Computing
        # it as cavity + wall puts the fit in twice over, and is superseded.
        self.collar = ball + 2 * self.wall
        self.material = self.collar / 2 - self.cav
        self.retention = ball - self.mouth
        self.holds = self.retention > 0
        self.past = math.degrees(math.asin(grip / self.r))     # past the equator, on the ball
        self.wrap = 90 + self.past
        self.coverage = (1 + grip / self.r) / 2
        try:
            self.swing = math.degrees(math.acos((stalk / 2) / self.cav)
                                      - math.asin(grip / self.cav))
        except ValueError:
            self.swing = float("nan")


SIZINGS = [
    Sizing("a", "Current CAD", "as built in stickbot-for-bot-review", 6.0, 3.0, 0.2, 1.35),
    Sizing("b", "Twice as big, grip carried over", "what a pure 2x gives", 12.0, 6.0, 0.8, 2.70),
    Sizing("c", "Twice as big, settled", "the fit tightened and grip derived from the mouth",
           12.0, 6.0, 0.08, ((6.0 + 0.08) ** 2 - (0.48 * 12.0) ** 2) ** 0.5),
]
A, B, C = SIZINGS

PX = 13.0          # px per mm, the same for every panel so the sizes compare
W, H = 320, 330


def arc(cx, cy, rad, a0, a1, n=180):
    """Points along a circle, math convention, y up. Flipped to SVG by the caller."""
    return [(cx + rad * math.cos(a0 + (a1 - a0) * i / n),
             cy + rad * math.sin(a0 + (a1 - a0) * i / n)) for i in range(n + 1)]


def path(points, close=True):
    d = "M " + " L ".join(f"{x:.2f},{y:.2f}" for x, y in points)
    return d + (" Z" if close else "")


def panel(s):
    """One cross-section. Math coords in mm, origin at the ball center, y up."""
    def X(v): return W / 2 + v * PX
    def Y(v): return H / 2 + 62 - v * PX          # flip, and sit the joint low

    mouth_r = s.mouth / 2
    floor = -(s.cav + s.wall)
    # the socket: outside box down from the mouth plane, cavity arc back around the bottom
    a_right = math.atan2(s.grip, mouth_r)
    outer = [(s.collar / 2, s.grip), (s.collar / 2, floor),
             (-s.collar / 2, floor), (-s.collar / 2, s.grip), (-mouth_r, s.grip)]
    cavity = arc(0, 0, s.cav, math.pi - a_right, a_right - 2 * math.pi)
    socket = [(X(x), Y(y)) for x, y in outer + cavity]

    # the wrap band, drawn on the ball just outside its surface
    band = arc(0, 0, s.r * 1.16, math.pi - math.radians(s.past),
               math.radians(s.past) - 2 * math.pi)
    band = [(X(x), Y(y)) for x, y in band]

    stalk = [(X(-s.stalk / 2), Y(s.grip - 0.2)), (X(-s.stalk / 2), Y(s.cav + s.wall + 3)),
             (X(s.stalk / 2), Y(s.cav + s.wall + 3)), (X(s.stalk / 2), Y(s.grip - 0.2))]

    good = "var(--good)" if s.holds else "var(--bad)"
    parts = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{s.title}: '
             f'cross-section of the ball and socket, the socket wrapping '
             f'{s.wrap:.0f} degrees around the ball">']
    # equator
    parts.append(f'<line class="rule" x1="{X(-s.collar/2-3):.1f}" y1="{Y(0):.1f}" '
                 f'x2="{X(s.collar/2+3):.1f}" y2="{Y(0):.1f}"/>')
    parts.append(f'<text class="tick" x="{X(s.collar/2+5):.1f}" y="{Y(0)+4:.1f}">equator</text>')
    # the socket, then the ball on top of it, then the stalk
    parts.append(f'<path class="socket" d="{path(socket)}"/>')
    parts.append(f'<circle class="ball" cx="{X(0):.1f}" cy="{Y(0):.1f}" r="{s.r*PX:.2f}"/>')
    parts.append(f'<path class="stalk" d="{path(stalk)}"/>')
    # the wrap band
    parts.append(f'<path class="band" d="{path(band, close=False)}"/>')
    # the mouth plane, and the ball width at the equator, as facing bars
    parts.append(f'<line class="mouth" x1="{X(-mouth_r):.1f}" y1="{Y(s.grip):.1f}" '
                 f'x2="{X(mouth_r):.1f}" y2="{Y(s.grip):.1f}" style="stroke:{good}"/>')
    parts.append(f'<text class="tick" x="{X(0):.1f}" y="{Y(s.grip)-7:.1f}" '
                 f'text-anchor="middle" style="fill:{good}">mouth &#216;{s.mouth:.3f}</text>')
    parts.append(f'<text class="wrapdeg" x="{X(0):.1f}" y="{Y(-s.r*1.16)+20:.1f}" '
                 f'text-anchor="middle">{s.wrap:.1f}&#176;</text>')
    parts.append('</svg>')
    return "\n".join(parts)


ROWS = [
    ("Ball", "ball", "{:.3f}"), ("Stalk", "stalk", "{:.3f}"),
    ("<code>#fit</code>", "fit", "{:.3f}"), ("<code>#grip</code>", "grip", "{:.3f}"),
    ("<code>#wall</code>", "wall", "{:.3f}"),
    ("Cavity radius", "cav", "{:.3f}"), ("Mouth", "mouth", "{:.3f}"),
    ("Collar outside", "collar", "{:.3f}"),
    ("Material, cavity to outside", "material", "{:.3f}"),
    ("Retention, on diameter", "retention", "{:+.3f}"),
    ("Socket past the equator", "grip", "{:.3f}"),
    ("Wrap around the ball", "wrap", "{:.1f}&#176;"),
    ("Ball surface enclosed", "coverage", None),
    ("Swing from the stalk", "swing", "{:.1f}&#176;"),
]


def table():
    out = ['<div class="tablewrap"><table>', "<thead><tr><th>mm</th>"]
    for s in SIZINGS:
        out.append(f'<th class="{s.key}">{s.title}</th>')
    out.append("</tr></thead><tbody>")
    for label, attr, fmt in ROWS:
        cls = ' class="key"' if attr in ("fit", "grip", "retention") else ""
        out.append(f"<tr{cls}><th>{label}</th>")
        for s in SIZINGS:
            v = getattr(s, attr)
            txt = f"{v*100:.1f}%" if fmt is None else fmt.format(v)
            bad = ' class="bad"' if attr == "retention" and v <= 0 else ""
            out.append(f"<td{bad}>{txt}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "\n".join(out)


CSS = """
:root{
  --ground:#f7f8fa; --panel:#ffffff; --ink:#171b21; --muted:#5d6673; --rule:#d5dae2;
  --ball:#3f6fa8; --ball-fill:#c9dcf0; --socket:#8a6a1f; --socket-fill:#f0dfae;
  --good:#1f7a4d; --bad:#b3341f; --band:#b8862b;
}
@media (prefers-color-scheme:dark){
  :root:not([data-theme="light"]){
    --ground:#12151a; --panel:#1a1f27; --ink:#e6eaf0; --muted:#98a2b1; --rule:#2f3742;
    --ball:#8fbbe8; --ball-fill:#23364c; --socket:#e0bf70; --socket-fill:#3a3324;
    --good:#5fd39a; --bad:#ff8a70; --band:#e0bf70;
  }
}
:root[data-theme="dark"]{
  --ground:#12151a; --panel:#1a1f27; --ink:#e6eaf0; --muted:#98a2b1; --rule:#2f3742;
  --ball:#8fbbe8; --ball-fill:#23364c; --socket:#e0bf70; --socket-fill:#3a3324;
  --good:#5fd39a; --bad:#ff8a70; --band:#e0bf70;
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
.ball{fill:var(--ball-fill);stroke:var(--ball);stroke-width:1.6}
.socket{fill:var(--socket-fill);stroke:var(--socket);stroke-width:1.6;stroke-linejoin:round}
.stalk{fill:var(--ball-fill);stroke:var(--ball);stroke-width:1.6}
.band{fill:none;stroke:var(--band);stroke-width:5;stroke-linecap:round;opacity:.85}
.rule{stroke:var(--rule);stroke-width:1;stroke-dasharray:4 4}
.mouth{stroke-width:2.4;stroke-linecap:round}
text{font:11px/1 ui-monospace,SFMono-Regular,Menlo,monospace;fill:var(--muted)}
.wrapdeg{font-size:15px;font-weight:700;fill:var(--band)}
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
.callout{border-left:3px solid var(--band);padding:.1rem 0 .1rem 1rem;margin:1.4rem 0;
  background:none}
.callout p{margin:.5rem 0}
footer{margin-top:3rem;padding-top:1rem;border-top:1px solid var(--rule);
  color:var(--muted);font-size:.82rem}
"""


def build():
    panels = []
    for s in SIZINGS:
        v = ("holds the ball" if s.holds else "the ball falls out")
        panels.append(
            f'<div class="panel"><h3>{s.title}</h3>'
            f'<p class="note">{s.note}</p>{panel(s)}'
            f'<p class="verdict {"yes" if s.holds else "no"}">'
            f'{"&#10003;" if s.holds else "&#10007;"} {v} &mdash; '
            f'retention {s.retention:+.3f} mm</p></div>')

    html = f"""<title>Socket Wrap</title>
<style>{CSS}</style>
<div class="wrap">
<h1>How far the socket wraps around the ball</h1>
<p class="sub">Cross-sections at true relative scale, so the doubling is the size difference you
see. The gold band is the arc of the ball the socket encloses; the colored line is the mouth the
ball has to squeeze through to get in.</p>

<div class="panels">
{"".join(panels)}
</div>

<div class="callout">
<p><strong>Wrap is not what holds the ball.</strong> The middle panel wraps the ball through exactly
the same angle as the current CAD &mdash; it is a pure doubling, so every proportion is preserved
&mdash; and it still drops the ball. The cavity grew by <code>#fit</code> and the ball did not, so
the mouth opened to &#216;12.482 against a &#216;12 ball. Retention is the mouth against the ball,
and nothing else.</p>
<p><strong>Tightening <code>#fit</code> is what buys it back</strong>, and it does it without
reaching further around the ball. The mouth is the dimension now, drawn at 96% of the ball
&mdash; &#216;{C.mouth:.3f} against &#216;{C.ball:g}, so {C.retention:.3f}&#8239;mm of retention
&mdash; and <code>#grip</code> is whatever puts the cavity sphere through a mouth that size:
{C.grip:.4f} at <code>#fit</code> {C.fit:g}. That is {100 * C.grip / C.r:.0f}% of the ball's radius
against the current CAD's {100 * A.grip / A.r:.0f}%. <strong>The socket wraps less and holds
more.</strong></p>
</div>

<h2>The numbers</h2>
{table()}

<h2>What it buys</h2>
<p>Swing rises from {A.swing:.1f}&#176; to {C.swing:.1f}&#176;. The stalk hits the rim of the mouth
later because the rim reaches less far around the ball, and that is the whole of the trade in the
other direction: every degree of wrap given back is a degree of articulation returned. Wrap goes
from {A.wrap:.1f}&#176; to {C.wrap:.1f}&#176; and coverage from {100 * A.coverage:.1f}% to
{100 * C.coverage:.1f}%, and the joint holds better than the one that was built and assembled.</p>
<p>The route not taken was to leave <code>#fit</code> at 0.8 and raise <code>#grip</code> to 3.60,
which also closes the mouth. It wraps 126.9&#176; and swings 31.9&#176;, and it only holds near the
fit it was dimensioned at &mdash; loosen the fit and the mouth opens past the ball again. Holding
the mouth at 96% survives every value of <code>#fit</code>; the arithmetic is in
<code>.docs/experiments/runs/2026-08-25-draft9p1/a2-fit.md</code>.</p>

<footer>The collar is <code>#ball&#8239;+&#8239;2&#215;#wall</code>, which leaves the fit out
on purpose so a printing clearance changes the hollow and nothing else &mdash; stickbot's built
collar is &#216;9.4 because it predates that rule. Drawn by
<code>.docs/experiments/sketches/socket-wrap.py</code> from the four inputs of each
sizing &mdash; ball, stalk, <code>#fit</code> and <code>#grip</code>. Every other number on this
page is derived. Wrap is measured on the ball: the mouth plane sits <code>#grip</code> above the
center, so the socket reaches asin(<code>#grip</code>&#8239;/&#8239;r) past the equator.</footer>
</div>
"""
    out = pathlib.Path(__file__).parent / "socket-wrap.html"
    out.write_text(html)
    print(f"wrote {out}")
    for s in SIZINGS:
        print(f"  {s.title:38s} mouth {s.mouth:7.3f}  retention {s.retention:+7.3f}  "
              f"wrap {s.wrap:6.1f}  coverage {s.coverage*100:5.1f}%  swing {s.swing:5.1f}")


build()
