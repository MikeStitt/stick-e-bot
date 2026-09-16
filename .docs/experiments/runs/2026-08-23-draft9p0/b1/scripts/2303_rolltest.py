"""#58 — establish what `Roll to here` means, and that it can be undone.

Rolls `head` back by one feature, proves the model changed, rolls it forward
again and proves the model came back. Restores in a finally.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid, eid = s["did"], s["wid"], s["head_eid"]
MENU = """(t) => { for (const e of document.querySelectorAll('li,a,div,span')) {
    if (e.children.length) continue;
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.height < 40 && r.x > 190)
      return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)];
  } return null; }"""

def rollto(page, name):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    x, y = gui.row(page, name)
    page.mouse.click(x, y, button="right")
    page.wait_for_timeout(1800)
    hit = page.evaluate(MENU, "Roll to here")
    if hit is None:
        page.keyboard.press("Escape")
        return False
    page.mouse.click(*hit)
    page.wait_for_timeout(7000)
    return True

def shape(page):
    b = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/bodydetails")["body"]
    n, rad = 0, set()
    for body in b["bodies"]:
        for f in body["faces"]:
            n += 1
            su = f.get("surface") or {}
            if su.get("type") in ("cylinder", "sphere"):
                rad.add(round(su["radius"] * 1000, 3))
    return n, sorted(rad)

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    if "/e/" + eid not in page.url:
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(15000)
    end = shape(page)
    print("at the end:", end)
    try:
        print("roll to 'add socket to head':", rollto(page, "add socket to head"))
        print("  now:", shape(page))
        page.screenshot(path=D + "rolled.png")
    finally:
        ok = rollto(page, "head mate")
        back = shape(page)
        print("roll to 'head mate':", ok, "->", back)
        print("RESTORED" if back == end else "*** NOT RESTORED ***")
