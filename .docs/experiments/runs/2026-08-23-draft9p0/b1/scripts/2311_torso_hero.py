"""#26 — retake torso-joints/hero.png, whose caption promises five studs.

The frame on file shows one: the three planes are on, and four of the studs are
behind the box or clipped by a plane. Shoot a Front view, where all five stand out
in silhouette, and an isometric, and choose from the two. Plane visibility is
restored before the script ends.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
OUT = D + "retake/"
import os
os.makedirs(OUT, exist_ok=True)
s = common.load(); did, wid = s["did"], s["wid"]
FIND = """(a) => { const [t, x0, x1, y0, y1] = a; let best = null, area = 1e9;
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 46) continue;
    const cx = r.x + r.width/2, cy = r.y + r.height/2;
    if (cx < x0 || cx > x1 || cy < y0 || cy > y1) continue;
    if (r.width * r.height < area) { area = r.width*r.height; best = [Math.round(cx), Math.round(cy)]; }
  } return best; }"""

def find(page, text, x0=0, x1=2000, y0=0, y1=1200):
    return page.evaluate(FIND, [text, x0, x1, y0, y1])

def visibility(page, plane, want):
    """`want` is 'Hide' or 'Show'; returns what it actually clicked."""
    page.keyboard.press("Escape"); page.wait_for_timeout(500)
    page.mouse.click(*gui.row(page, plane), button="right")
    page.wait_for_timeout(1600)
    hit = find(page, want, x0=150)
    if not hit:
        page.keyboard.press("Escape")
        return f"{plane}: no {want!r} — already there"
    page.mouse.click(*hit); page.wait_for_timeout(2500)
    return f"{plane}: {want}"

def shot(page, key, name):
    gui.viewport(page)
    page.mouse.move(900, 500)
    page.keyboard.press(key); page.wait_for_timeout(2000)
    gui.fit(page); page.wait_for_timeout(2500)
    gui.clear(page); page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1500)
    gui.frame(page, OUT + name)

# `plane for shoulder` is a construction plane this page makes, and its label
# reads as a smudge at the torso's top corner in a Front view.
PLANES = ("Top", "Front", "Right", "plane for shoulder")
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
        shot(page, "Shift+1", "torso_front2.png")
        
    finally:
        for pl in PLANES:
            print(" ", visibility(page, pl, "Show"))
