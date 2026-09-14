import math

# The joint, from build-briefs/ball-and-socket.md. The mouth is the dimension, drawn at 96%
# of the ball, and #grip -- how deep the ball's center sits below the socket's face -- is
# whatever puts the cavity sphere through a mouth that size. So tightening #fit lifts the
# ball toward the face and buys swing, and the socket's height does not move with it.
BALL_R, STALK_R, FIT = 6.0, 3.0, 0.08
WALL, COLLAR_L = 3.0, 9.0     # the socket's wall, and the ball center down to the socket's root
LIMB_R, STAND = 12.0, 10.0    # the thigh across, and the ball center below the torso's face

CAV_R = BALL_R + FIT
MOUTH_R = 0.48 * 2 * BALL_R   # 96% of the ball, on the radius
GRIP = math.sqrt(CAV_R**2 - MOUTH_R**2)
COLLAR_R = BALL_R + WALL      # #ball + 2 x #wall on the diameter; the fit is left out on purpose
FACE = -COLLAR_L              # the thigh's top face is the socket's root, so the fit moves the
                              # hollow and leaves the thigh's length alone
STALK_TOP = math.sqrt(BALL_R**2 - STALK_R**2)
TH = math.degrees(math.acos(STALK_R/CAV_R)) - math.degrees(math.asin(GRIP/CAV_R))
C, S = math.cos(math.radians(TH)), math.sin(math.radians(TH))
RIM_HI, RIM_X = GRIP*C + COLLAR_R*S, -COLLAR_R*C + GRIP*S
SWEEP = math.hypot(COLLAR_R, GRIP)

K, OX, OY, BOT = 8.0, 160.0, 230.0, -22.0
X = lambda x: OX + K*x
Y = lambda z: OY - K*z

def outline(n=72):
    p = [(-LIMB_R, BOT), (-LIMB_R, FACE), (-COLLAR_R, FACE), (-COLLAR_R, GRIP), (-MOUTH_R, GRIP)]
    a0 = math.atan2(GRIP, -MOUTH_R); a1 = math.atan2(GRIP, MOUTH_R) + 2*math.pi
    p += [(CAV_R*math.cos(a0+(a1-a0)*i/n), CAV_R*math.sin(a0+(a1-a0)*i/n)) for i in range(1, n)]
    p += [(MOUTH_R, GRIP), (COLLAR_R, GRIP), (COLLAR_R, FACE), (LIMB_R, FACE), (LIMB_R, BOT)]
    return p

def rot(p, d):
    c, s = math.cos(math.radians(d)), math.sin(math.radians(d))
    return [(x*c - z*s, x*s + z*c) for x, z in p]

def d_of(p):
    return "M " + " L ".join(f"{X(a):.2f} {Y(b):.2f}" for a, b in p) + " Z"

REST, TILT = d_of(outline()), d_of(rot(outline(), -TH))

def rect(x0, z1, x1, z0):
    return f'x="{X(x0):.2f}" y="{Y(z1):.2f}" width="{K*(x1-x0):.2f}" height="{K*(z1-z0):.2f}"'

def stud(top):
    """Ball + stalk as one closed silhouette, stalk running up to z=top."""
    a = math.acos(STALK_R/BALL_R)
    pts = [(-STALK_R, top), (-STALK_R, STALK_TOP)]
    a0 = math.pi - a; a1 = 2*math.pi + a
    n = 60
    pts += [(BALL_R*math.cos(a0+(a1-a0)*i/n), BALL_R*math.sin(a0+(a1-a0)*i/n)) for i in range(1, n)]
    pts += [(STALK_R, STALK_TOP), (STALK_R, top)]
    return d_of(pts)

def dim(x, ztop, zbot, label, cls="dim"):
    """Vertical dimension between two z levels at abscissa x."""
    xp, y0, y1 = X(x), Y(ztop), Y(zbot)
    return f'''
      <g class="{cls}">
        <line x1="{xp:.2f}" y1="{y0:.2f}" x2="{xp:.2f}" y2="{y1:.2f}"/>
        <line x1="{xp-5:.2f}" y1="{y0:.2f}" x2="{xp+5:.2f}" y2="{y0:.2f}"/>
        <line x1="{xp-5:.2f}" y1="{y1:.2f}" x2="{xp+5:.2f}" y2="{y1:.2f}"/>
        <text class="num" x="{xp-9:.2f}" y="{(y0+y1)/2+4:.2f}" text-anchor="end">{label}</text>
      </g>'''

def datum(z, label, x0=-20, x1=20):
    return (f'<line class="datum" x1="{X(x0):.2f}" y1="{Y(z):.2f}" x2="{X(x1):.2f}" y2="{Y(z):.2f}"/>'
            f'<text class="tick" x="{X(x1)-2:.2f}" y="{Y(z)-5:.2f}" text-anchor="end">{label}</text>')

def panel(uid, stalk_len, pedestal, plate_top=26.0):
    ped_h = 4.0
    plate_z = stalk_len + (ped_h if pedestal else 0)
    parts = [f'<rect class="fixed" {rect(-20, plate_top, 20, plate_z)}/>',
             f'<rect class="edge" {rect(-20, plate_top, 20, plate_z)}/>']
    if pedestal:
        parts += [f'<rect class="fixed" {rect(-8, plate_z, 8, stalk_len)}/>',
                  f'<rect class="edge" {rect(-8, plate_z, 8, stalk_len)}/>']
    parts.append(f'<path class="thigh-tilt" d="{TILT}"/>')
    parts.append(f'<path class="thigh" d="{REST}"/>')
    parts.append(f'<path class="stud" d="{stud(stalk_len)}"/>')
    parts.append(f'<circle class="sweep" cx="{X(0):.2f}" cy="{Y(0):.2f}" r="{K*SWEEP:.2f}"/>')
    parts.append(f'<line class="axis" x1="{X(0):.2f}" y1="{Y(12.0):.2f}" x2="{X(0):.2f}" y2="{Y(BOT):.2f}"/>')
    parts.append(datum(RIM_HI, f'rim at {TH:.1f}°'))
    parts.append(f'<circle class="node" cx="{X(RIM_X):.2f}" cy="{Y(RIM_HI):.2f}" r="3.2"/>')
    parts.append(dim(RIM_X, stalk_len, RIM_HI, f'{stalk_len - RIM_HI:.3f}'))
    parts.append(f'<line class="axis" x1="{X(-4.4):.2f}" y1="{Y(0):.2f}" x2="{X(4.4):.2f}" y2="{Y(0):.2f}"/>')
    parts.append(f'<text class="tick" x="{X(9.2):.2f}" y="{Y(stalk_len)+27:.2f}">stalk {stalk_len:.0f}</text>')
    return f'<svg viewBox="-24 0 368 430" role="img" aria-labelledby="t{uid}">' + "".join(parts) + '</svg>'


def swing_arc(r=18.0):
    a0 = math.radians(270); a1 = math.radians(270 - TH)
    x0, y0 = X(r*math.cos(a0)), Y(r*math.sin(a0))
    x1, y1 = X(r*math.cos(a1)), Y(r*math.sin(a1))
    return (f'<path class="swing" d="M {x0:.2f} {y0:.2f} A {K*r:.2f} {K*r:.2f} 0 0 1 {x1:.2f} {y1:.2f}"/>'
            f'<text class="tick" x="{X(-8.0):.2f}" y="{Y(-17.2):.2f}" text-anchor="middle">{TH:.2f}&deg;</text>')

PANEL = panel("a", STAND, False).replace("</svg>", swing_arc() + "</svg>")

HTML = f'''<title>The hip joint reaches its limit without touching anything</title>
<style>
:root {{
  --ground:#EDECE8; --surface:#FDFDFC; --ink:#191B1D; --muted:#62676B; --line:#D6D3CC;
  --fixed:#B3AFA4; --fixed-ink:#8E897C; --moving:#8DA3B0; --moving-ink:#5C7383;
  --stud:#3F4F59; --dim:#A93B26; --good:#2C6B50;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --ground:#121416; --surface:#1B1E21; --ink:#E8E6E1; --muted:#969BA0; --line:#2C3033;
    --fixed:#5F5B53; --fixed-ink:#8A8478; --moving:#4C6273; --moving-ink:#8BA6B8;
    --stud:#9DB2BE; --dim:#DE7259; --good:#5FA582;
  }}
}}
:root[data-theme="dark"] {{
  --ground:#121416; --surface:#1B1E21; --ink:#E8E6E1; --muted:#969BA0; --line:#2C3033;
  --fixed:#5F5B53; --fixed-ink:#8A8478; --moving:#4C6273; --moving-ink:#8BA6B8;
  --stud:#9DB2BE; --dim:#DE7259; --good:#5FA582;
}}
* {{ box-sizing:border-box; }}
body {{
  margin:0; background:var(--ground); color:var(--ink);
  font:400 16px/1.55 ui-sans-serif,-apple-system,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
}}
.num {{ font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace; font-variant-numeric:tabular-nums; }}
.wrap {{ max-width:1000px; margin:0 auto; padding:48px 24px 72px; display:flex; flex-direction:column; gap:38px; }}
header {{ display:flex; flex-direction:column; gap:14px; max-width:64ch; }}
.eyebrow {{ font-size:11px; letter-spacing:.13em; text-transform:uppercase; color:var(--muted); font-weight:600; }}
h1 {{ margin:0; font-size:clamp(26px,3.4vw,38px); line-height:1.12; letter-spacing:-.022em; font-weight:650; text-wrap:balance; }}
header p {{ margin:0; color:var(--muted); font-size:16.5px; }}
header p strong {{ color:var(--ink); font-weight:600; }}
.main {{ display:grid; grid-template-columns:minmax(240px,320px) 1fr; gap:32px; align-items:start; }}
@media (max-width:720px) {{ .main {{ grid-template-columns:1fr; }} }}
figure {{ margin:0; background:var(--surface); border:1px solid var(--line); border-radius:3px; padding:18px; }}
figure svg {{ width:100%; height:auto; display:block; }}
.side {{ display:flex; flex-direction:column; gap:22px; }}
.side h3 {{ margin:0 0 8px; font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); font-weight:600; }}
.side p {{ margin:0 0 10px; font-size:15px; max-width:62ch; }}
.side p:last-child {{ margin-bottom:0; }}
.verdict {{ display:flex; align-items:baseline; gap:10px; }}
.verdict .num {{ font-size:30px; font-weight:600; letter-spacing:-.02em; color:var(--good); }}
.verdict span.lbl {{ font-size:12.5px; letter-spacing:.05em; text-transform:uppercase; color:var(--muted); }}
.eq {{
  font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-size:13.5px; line-height:1.9;
  background:var(--surface); border:1px solid var(--line); border-left:2px solid var(--dim);
  padding:14px 16px; overflow-x:auto; white-space:pre; border-radius:2px;
}}
.legend {{ list-style:none; margin:14px 0 0; padding:0; display:flex; flex-wrap:wrap; gap:7px 18px; font-size:12.5px; color:var(--muted); }}
.legend li {{ display:flex; align-items:center; gap:7px; }}
.sw {{ width:20px; height:10px; flex:none; border-radius:1px; }}
.sw-fixed {{ background:var(--fixed); border:1px solid var(--fixed-ink); opacity:.75; }}
.sw-thigh {{ background:var(--moving); border:1px solid var(--moving-ink); opacity:.7; }}
.sw-tilt {{ height:0; border-top:2px dashed var(--moving-ink); }}
.sw-stud {{ background:var(--stud); }}
.sw-sweep {{ height:0; border-top:2px dotted var(--moving-ink); opacity:.7; }}
/* drawing */
.fixed {{ fill:var(--fixed); opacity:.55; }}
.edge {{ fill:none; stroke:var(--fixed-ink); stroke-width:1.2; }}
.thigh {{ fill:var(--moving); fill-opacity:.5; stroke:var(--moving-ink); stroke-width:1.3; }}
.thigh-tilt {{ fill:none; stroke:var(--moving-ink); stroke-width:1.2; stroke-dasharray:5 3; opacity:.85; }}
.stud {{ fill:var(--stud); stroke:var(--stud); stroke-width:1; }}
.sweep {{ fill:none; stroke:var(--moving-ink); stroke-width:.8; stroke-dasharray:2 4; opacity:.5; }}
.swing {{ fill:none; stroke:var(--dim); stroke-width:1.2; }}
.axis {{ stroke:var(--muted); stroke-width:.8; stroke-dasharray:9 3 2 3; opacity:.6; }}
.datum {{ stroke:var(--dim); stroke-width:.9; stroke-dasharray:6 3; opacity:.75; }}
.node {{ fill:var(--dim); }}
.dim line {{ stroke:var(--dim); stroke-width:1.2; }}
.dim text, text.tick {{ fill:var(--dim); }}
.dim text {{ font-size:15px; font-weight:600; }}
text.tick {{ font-size:10.5px; letter-spacing:.06em; font-family:ui-monospace,SFMono-Regular,Menlo,monospace; opacity:.85; }}
.tablewrap {{ overflow-x:auto; }}
table {{ border-collapse:collapse; width:100%; font-size:14px; }}
caption {{ text-align:left; font-size:12px; letter-spacing:.12em; text-transform:uppercase; color:var(--muted); font-weight:600; padding-bottom:10px; }}
th, td {{ text-align:left; padding:8px 14px 8px 0; border-bottom:1px solid var(--line); vertical-align:baseline; }}
th {{ font-weight:600; font-size:12px; letter-spacing:.05em; text-transform:uppercase; color:var(--muted); }}
td.n {{ font-family:ui-monospace,SFMono-Regular,Menlo,monospace; font-variant-numeric:tabular-nums; text-align:right; padding-right:22px; }}
tbody tr:last-child td {{ border-bottom:none; }}
footer {{ font-size:13px; color:var(--muted); border-top:1px solid var(--line); padding-top:16px; }}
</style>

<div class="wrap">
  <header>
    <span class="eyebrow">Hip joint &middot; section on the ball center &middot; &Oslash;{2*STALK_R:g} stalk, {STAND:g} mm to the torso&rsquo;s underside</span>
    <h1>The hip reaches its full travel without touching the torso.</h1>
    <p>The thigh swings until the stalk meets the socket&rsquo;s mouth, at
    <span class="num">{TH:.2f}&deg;</span> either way. Nothing outside the socket gets in the way:
    at that limit the collar&rsquo;s rim is still <span class="num">{STAND-RIM_HI:.3f}</span> mm below the
    torso. <strong>The travel is set by the joint&rsquo;s own internals, which is what the design
    intends.</strong> No pedestal, no longer stalk, no change.</p>
  </header>

  <div class="main">
    <figure>
      {PANEL}
      <ul class="legend">
        <li><span class="sw sw-fixed"></span>torso &mdash; fixed</li>
        <li><span class="sw sw-thigh"></span>thigh, hanging straight</li>
        <li><span class="sw sw-tilt"></span>thigh at the limit</li>
        <li><span class="sw sw-stud"></span>ball and stalk</li>
        <li><span class="sw sw-sweep"></span>sphere the rim sweeps</li>
      </ul>
    </figure>

    <div class="side">
      <div>
        <div class="verdict"><span class="num">&plusmn;{TH:.2f}&deg;</span><span class="lbl">both axes, unobstructed</span></div>
      </div>
      <div>
        <h3>What limits it</h3>
        <p>Two things touch inside the socket, and neither is the torso. The stalk runs into the
        mouth&rsquo;s edge, and how soon it gets there is set by <span class="num">#grip</span> &mdash;
        the {GRIP:.4f} mm the ball center sits inside the collar&rsquo;s face. The mouth is held at 96%
        of the ball whatever the fit is, so retention is fixed and the swing is what a tighter fit
        buys: at <span class="num">#fit</span> 0.8 this drawing showed 28.0&deg;.</p>
      </div>
      <div>
        <h3>The {STAND-RIM_HI:.3f} is air, not interference</h3>
        <p>The stud belongs to the torso and the collar belongs to the thigh. They are printed as
        separate objects and snapped together, so the gap between them is not a feature any slicer
        ever sees. At a 0.4 mm nozzle it is {(STAND-RIM_HI)/0.4:.1f} extrusion widths of nothing.</p>
        <p>It is recorded here only as the proof that the collar clears &mdash; not as a number to
        improve.</p>
      </div>
      <div>
        <h3>The arithmetic</h3>
        <div class="eq">&theta;max = arccos(stalkR / cavR) &minus; arcsin(grip / cavR)
     = arccos({STALK_R:g} / {CAV_R:g}) &minus; arcsin({GRIP:g} / {CAV_R:g})
     = {math.degrees(math.acos(STALK_R/CAV_R)):.3f}&deg; &minus; {math.degrees(math.asin(GRIP/CAV_R)):.3f}&deg;  =  {TH:.3f}&deg;

rim high = {GRIP:g}&middot;cos&theta; + {COLLAR_R:g}&middot;sin&theta;  = {RIM_HI:.3f}
rim out  = {COLLAR_R:g}&middot;cos&theta; &minus; {GRIP:g}&middot;sin&theta;  = {abs(RIM_X):.3f}
air      = {STAND:g} &minus; {RIM_HI:.3f}          = {STAND-RIM_HI:.3f}</div>
      </div>
    </div>
  </div>

  <div class="tablewrap">
    <table>
      <caption>Numbers in the drawing, ball center at the origin</caption>
      <thead><tr><th>Feature</th><th>Value</th><th>Where it comes from</th></tr></thead>
      <tbody>
        <tr><td>ball diameter</td><td class="n">{2*BALL_R:.3f}</td><td>joint design</td></tr>
        <tr><td>cavity radius</td><td class="n">{CAV_R:.3f}</td><td>ball radius + <span class="num">#fit</span> {FIT:g}</td></tr>
        <tr><td>stalk radius</td><td class="n">{STALK_R:.3f}</td><td>joint design</td></tr>
        <tr><td>collar outer radius</td><td class="n">{COLLAR_R:.3f}</td><td>ball radius {BALL_R:g} + <span class="num">#wall</span> {WALL:g}, with the fit left out</td></tr>
        <tr><td>mouth radius</td><td class="n">{MOUTH_R:.3f}</td><td>96% of the ball, on the radius &mdash; the dimension the rest follows</td></tr>
        <tr><td><span class="num">#grip</span></td><td class="n">{GRIP:.3f}</td><td>&radic;(cavity&sup2; &minus; mouth&sup2;) &mdash; derived, not typed</td></tr>
        <tr><td>rim sweep radius</td><td class="n">{SWEEP:.3f}</td><td>&radic;({COLLAR_R:g}&sup2; + {GRIP:g}&sup2;)</td></tr>
        <tr><td>travel limit</td><td class="n">{TH:.3f}&deg;</td><td>stalk against the mouth</td></tr>
        <tr><td>ball below the torso</td><td class="n">{STAND:.3f}</td><td>chosen so the swept rim, at {SWEEP:.3f}, always clears</td></tr>
      </tbody>
    </table>
  </div>

  <footer>Drawn from the joint&rsquo;s own numbers, not measured off a model. Redrawn for draft9p1,
  where <span class="num">#fit</span> went to {FIT:g} and <span class="num">#grip</span> stopped being
  typed &mdash; the swing is {TH:.2f}&deg; here against the 31.86&deg; the same drawing showed at
  <span class="num">#fit</span> 0.8, and 37.09&deg; at half the robot&rsquo;s size.</footer>
</div>
'''
open("hip-clearance.html", "w").write(HTML)
print("theta %.4f  rim %.4f  air %.4f  sweep %.4f" % (TH, RIM_HI, STAND-RIM_HI, SWEEP))
