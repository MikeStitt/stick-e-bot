"""#59 — retake the two right-hand connector frames.

Both were close-ups, and a close-up of the right shoulder reads exactly like one
of the left. The fix is not a better close-up: it is a frame wide enough to carry
the whole torso, with the connector selected in the tree so Onshape's own
highlight says which one it is. Front view, where handedness is readable.
"""
import sys, os
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
OUT = D + "retake/"
os.makedirs(OUT, exist_ok=True)
s = common.load(); did, wid = s["did"], s["wid"]
FIND = """(a) => { const [t, x0, x1, y0, y1] = a; let best = null, area = 1e9;
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 46) continue;
    const cx = r.x + r.width/2, cy = r.y + r.height/2;
    if (cx < x0 || cx > x1 || cy < y0 || cy > y1) continue;
    if (r.width*r.height < area) { area = r.width*r.height; best = [Math.round(cx), Math.round(cy)]; }
  } return best; }"""

def find(page, t, x0=0, x1=2000, y0=0, y1=1200):
    return page.evaluate(FIND, [t, x0, x1, y0, y1])

def visibility(page, plane, want):
    page.keyboard.press("Escape"); page.wait_for_timeout(500)
    page.mouse.click(*gui.row(page, plane), button="right"); page.wait_for_timeout(1600)
    hit = find(page, want, x0=150)
    if not hit:
        page.keyboard.press("Escape"); return f"{plane}: already {want.lower()}n"
    page.mouse.click(*hit); page.wait_for_timeout(2500)
    return f"{plane}: {want}"

def to_bottom(page):
    """The connector rows are the last of thirty-nine, so they start below the fold
    and `gui.row` cannot see them."""
    page.mouse.move(140, 400)
    for _ in range(6):
        page.mouse.wheel(0, 400); page.wait_for_timeout(400)
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
        to_bottom(page)
        for name, out in JOBS:
            page.keyboard.press("Escape"); page.wait_for_timeout(600)
            page.mouse.click(*gui.row(page, name)); page.wait_for_timeout(3000)
            page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1500)
            gui.frame(page, OUT + out)
    finally:
        page.keyboard.press("Escape")
        page.mouse.move(140, 400)
        for _ in range(10):
            page.mouse.wheel(0, -400); page.wait_for_timeout(300)
        page.wait_for_timeout(1200)
        for pl in PLANES:
            print(" ", visibility(page, pl, "Show"))
