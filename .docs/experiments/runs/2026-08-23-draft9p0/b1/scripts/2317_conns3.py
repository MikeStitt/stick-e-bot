"""#59 — the two right-hand connector frames, ringed from Onshape's own numbers.

A close-up of the right shoulder reads exactly like one of the left, which is why
both frames on file are unusable. This shoots the whole torso from the Front, with
the connector selected in the tree, and rings the pixel its own status-bar position
projects to — so the ring cannot mark the wrong ball.

Two traps, both hit on the way here: the WebGL camera hook is lost on every page
load and has to be reinstalled, and Escape does not drop a tree selection, so the
second pick lands on top of the first and the bar reads a distance, not a point.
"""
import sys, os, re
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_screen as screen
from playwright.sync_api import sync_playwright
OUT = D + "retake/"
os.makedirs(OUT, exist_ok=True)
s = common.load(); did, wid = s["did"], s["wid"]
FIND = """(a) => { const [t, x0] = a; let best = null, area = 1e9;
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 46 || r.x + r.width/2 < x0) continue;
    if (r.width*r.height < area) { area = r.width*r.height;
      best = [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }
  } return best; }"""
POINT = """() => { for (const e of document.querySelectorAll('div,span')) {
    const t = (e.innerText||'').trim();
    if (t.startsWith('Point:') && t.length < 90) return t;
  } return null; }"""

def visibility(page, plane, want):
    page.keyboard.press("Escape"); page.wait_for_timeout(500)
    page.mouse.click(*gui.row(page, plane), button="right"); page.wait_for_timeout(1600)
    hit = page.evaluate(FIND, [want, 150])
    if not hit:
        page.keyboard.press("Escape"); return f"{plane}: already there"
    page.mouse.click(*hit); page.wait_for_timeout(2500)
    return f"{plane}: {want}"

def scroll(page, n):
    page.mouse.move(140, 400)
    for _ in range(abs(n)):
        page.mouse.wheel(0, 400 if n > 0 else -400); page.wait_for_timeout(300)
    page.wait_for_timeout(1200)

PLANES = ("Top", "Front", "Right", "plane for shoulder")
JOBS = [("r shoulder connector", "conn_r_shoulder.png"),
        ("r hip connector", "conn_r_hip.png")]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000)
    page.set_default_timeout(120000)
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{s['ps_eid']}",
              wait_until="domcontentloaded")
    page.wait_for_timeout(15000)
    try:
        for pl in PLANES:
            print(" ", visibility(page, pl, "Hide"))
        gui.viewport(page)
        page.mouse.move(900, 500)
        page.keyboard.press("Shift+1"); page.wait_for_timeout(2000)
        gui.fit(page); page.wait_for_timeout(2500)
        print(" hook:", screen.hook(page))
        gui.wake(page); page.wait_for_timeout(2500)
        cam = screen.camera(page)
        assert cam, "no camera"
        scroll(page, 6)
        for name, out in JOBS:
            gui.clear(page)                      # Escape does not drop a tree pick
            page.wait_for_timeout(1200)
            page.mouse.click(*gui.row(page, name)); page.wait_for_timeout(3000)
            page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1500)
            txt = page.evaluate(POINT)
            assert txt and txt.startswith("Point:"), f"{name}: bar reads {txt!r}"
            xyz = [float(v) for v in re.findall(r"-?\d+\.\d+", txt)]
            assert len(xyz) == 3, f"{name}: {txt!r}"
            print(f"  {name}: {txt}")
            gui.ring(page, OUT + out, gui.project(page, *xyz, cam=cam), radius=46)
    finally:
        gui.clear(page)
        page.keyboard.press("Escape")
        scroll(page, -12)
        for pl in PLANES:
            print(" ", visibility(page, pl, "Show"))
