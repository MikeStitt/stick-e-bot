"""Put `body` and `head` back to the end of their feature lists.

2306 rolled both back, and its `Roll to end` click missed: it right-clicked the
bar's own centre, which is off in the graphics area, not on the bar's handle.
This dumps what the bar's menu really offers before clicking anything.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
RECT = """() => { const e = document.querySelector('.ns-list-item-rollbackbar');
  if (!e) return null; const r = e.getBoundingClientRect();
  return [Math.round(r.x), Math.round(r.y), Math.round(r.width), Math.round(r.height)]; }"""
DUMP = """() => { const o = [];
  for (const e of document.querySelectorAll('li,a,div,span')) {
    if (e.children.length) continue;
    const t = (e.innerText||'').trim();
    if (!t || t.length > 40) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.height < 40 && r.y > 100 && r.x > 100)
      o.push([t, Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]);
  } return o; }"""

def faces(page, eid):
    b = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/bodydetails")["body"]
    return sum(len(body["faces"]) for body in b["bodies"])

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000)
    page.set_default_timeout(120000)
    for tab, eid, want in (("body", s["ps_eid"], 20), ("head", s["head_eid"], 47)):
        page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(15000)
        print(f"\n=== {tab}: {faces(page, eid)} faces, want {want}")
        r = page.evaluate(RECT)
        print("   bar rect x/y/w/h:", r)
        if not r:
            continue
        page.mouse.click(140, r[1] + r[3] // 2, button="right")
        page.wait_for_timeout(2000)
        items = page.evaluate(DUMP)
        for t, x, y in items:
            print(f"     menu {t!r} at ({x},{y})")
        hit = [i for i in items if i[0] == "Roll to end"]
        if hit:
            page.mouse.click(hit[0][1], hit[0][2])
            page.wait_for_timeout(9000)
        else:
            page.keyboard.press("Escape")
        n = faces(page, eid)
        print(f"   now {n} faces", "RESTORED" if n == want else "*** STILL ROLLED BACK ***")
