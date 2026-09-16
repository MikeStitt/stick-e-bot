"""#58 — heroes for torso.rst and head.rst, from a rolled-back tree.

`Roll to here` on a feature's context menu puts the bar *after* that feature.
`Roll to end` is on the bar's own context menu, and the bar is always in the DOM
as `.ns-list-item-rollbackbar` — its position, not its presence, is the state.
Every roll is undone in a finally and the undo is verified against REST.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
OUT = "/Users/mikestitt/projects/first/2027/sponge/instructions/stickbot-draft9p0/source/images/"
s = common.load(); did, wid = s["did"], s["wid"]
MENU = """(t) => { for (const e of document.querySelectorAll('li,a,div,span')) {
    if (e.children.length) continue;
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.height < 40 && r.x > 190)
      return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)];
  } return null; }"""
BARY = """() => { const e = document.querySelector('.ns-list-item-rollbackbar');
  if (!e) return null; const r = e.getBoundingClientRect();
  return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }"""

def faces(page, eid):
    b = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/bodydetails")["body"]
    return sum(len(body["faces"]) for body in b["bodies"])

def rollto(page, name):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    x, y = gui.row(page, name)
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(1800)
    hit = page.evaluate(MENU, "Roll to here")
    assert hit, f"no 'Roll to here' on {name!r}"
    page.mouse.click(*hit)
    page.wait_for_timeout(8000)

def rolltoend(page):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    bar = page.evaluate(BARY)
    assert bar, "no rollback bar in the DOM"
    page.mouse.click(bar[0], bar[1], button="right")
    page.wait_for_timeout(1800)
    hit = page.evaluate(MENU, "Roll to end")
    if hit is None:
        page.keyboard.press("Escape")
        return "already at the end"
    page.mouse.click(*hit)
    page.wait_for_timeout(8000)
    return "rolled to end"

JOBS = [("body", s["ps_eid"], "torso block", "torso", "hero.png"),
        ("head", s["head_eid"], "mouth", "head", "hero.png")]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000)
    page.set_default_timeout(120000)
    for tab, eid, upto, folder, shot in JOBS:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(15000)
        end = faces(page, eid)
        print(f"{tab}: {end} faces at the end")
        try:
            rollto(page, upto)
            print(f"  rolled to {upto!r}: {faces(page, eid)} faces")
            gui.viewport(page)
            page.mouse.move(900, 500)
            page.keyboard.press("Shift+7")
            page.wait_for_timeout(2000)
            gui.fit(page)
            page.wait_for_timeout(2500)
            gui.clear(page)
            page.mouse.move(*gui.EMPTY)
            page.wait_for_timeout(1500)
            gui.frame(page, OUT + folder + "/" + shot)
        finally:
            print("  ", rolltoend(page))
            back = faces(page, eid)
            print(f"   {back} faces", "RESTORED" if back == end else "*** NOT RESTORED ***")
