"""#58 — the hero for assembly.rst: two parts at the origin, overlapping, no mates.

The live `stickbot` assembly holds fourteen instances and an assembly has no
rollback bar, so this builds a throwaway assembly instead, with `body` and `head`
rolled back to where page 3 leaves them. The tab is deleted and both part studios
are rolled forward again before the script ends.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
OUT = "/Users/mikestitt/projects/first/2027/sponge/instructions/stickbot-draft9p0/source/images/"
s = common.load(); did, wid = s["did"], s["wid"]

FIND = """(a) => { const [t, x0, x1, y0, y1] = a; let best = null, area = 1e9;
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 46) continue;
    const cx = r.x + r.width/2, cy = r.y + r.height/2;
    if (cx < x0 || cx > x1 || cy < y0 || cy > y1) continue;
    if (r.width * r.height < area) { area = r.width * r.height;
      best = [Math.round(cx), Math.round(cy)]; }
  } return best; }"""
BAR = """() => { const e = document.querySelector('.ns-list-item-rollbackbar');
  if (!e) return null; const r = e.getBoundingClientRect();
  return [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }"""

def find(page, text, x0=0, x1=2000, y0=0, y1=1200):
    return page.evaluate(FIND, [text, x0, x1, y0, y1])

def faces(page, eid):
    b = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/bodydetails")["body"]
    return sum(len(body["faces"]) for body in b["bodies"])

def tabs(page):
    els = osx.api(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")["body"]
    return [(e["name"], e["elementType"], e["id"]) for e in els]

def goto(page, eid):
    page.goto(f"https://cad.onshape.com/documents/{did}/w/{wid}/e/{eid}",
              wait_until="domcontentloaded")
    page.wait_for_timeout(15000)

def rollto(page, name):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.mouse.click(*gui.row(page, name), button="right")
    page.wait_for_timeout(2000)
    hit = find(page, "Roll to here", x0=150)
    assert hit, f"no 'Roll to here' on {name!r}"
    page.mouse.click(*hit); page.wait_for_timeout(9000)

def rolltoend(page):
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    bar = page.evaluate(BAR)
    if not bar:
        return "no bar"
    page.mouse.click(bar[0], bar[1], button="right"); page.wait_for_timeout(2000)
    hit = find(page, "Roll to end", x0=150)
    if not hit:
        page.keyboard.press("Escape")
        return "no 'Roll to end' — already at the end"
    page.mouse.click(*hit); page.wait_for_timeout(9000)
    return "rolled to end"

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.set_default_navigation_timeout(180000)
    page.set_default_timeout(120000)
    before = tabs(page)
    print("tabs before:", [t[0] for t in before])
    made = None
    try:
        for tab, eid, upto, want in (("body", s["ps_eid"], "torso block", 6),
                                     ("head", s["head_eid"], "mouth", 29)):
            goto(page, eid)
            rollto(page, upto)
            n = faces(page, eid)
            print(f"{tab} rolled to {upto!r}: {n} faces", "OK" if n == want else "*** WRONG ***")

        print("creating the throwaway assembly")
        page.mouse.click(57, 984); page.wait_for_timeout(2500)
        hit = find(page, "Create Assembly", y0=600, y1=970)
        assert hit, "no 'Create Assembly' on the + menu"
        page.mouse.click(*hit); page.wait_for_timeout(12000)
        after = tabs(page)
        made = [t for t in after if t not in before]
        print("made:", made)
        page.screenshot(path=D + "asm_new.png")

        row = find(page, "body", x0=250, x1=620, y0=100, y1=900)
        if not row:
            page.mouse.click(189, 58); page.wait_for_timeout(4000)
            row = find(page, "body", x0=250, x1=620, y0=100, y1=900)
        assert row, "no 'body' row in the insert panel"
        page.mouse.click(*row); page.wait_for_timeout(4000)
        row = find(page, "head", x0=250, x1=620, y0=100, y1=900)
        assert row, "no 'head' row in the insert panel"
        page.mouse.click(*row); page.wait_for_timeout(4000)
        page.screenshot(path=D + "asm_ins.png")
        page.mouse.click(504, 93); page.wait_for_timeout(4000)
        print("tree:", gui.tree(page))

        gui.viewport(page)
        page.mouse.move(900, 500)
        page.keyboard.press("Shift+7"); page.wait_for_timeout(2000)
        gui.fit(page); page.wait_for_timeout(2500)
        gui.clear(page); page.mouse.move(*gui.EMPTY); page.wait_for_timeout(1500)
        gui.frame(page, OUT + "assembly/hero.png")
    finally:
        print("--- putting it all back")
        if made:
            name = made[0][0]
            tab = find(page, name, y0=960)
            print("  tab", name, "at", tab)
            if tab:
                page.mouse.click(*tab, button="right"); page.wait_for_timeout(2000)
                dele = find(page, "Delete", x0=tab[0] - 40, y0=400, y1=980)
                print("  Delete at", dele)
                if dele:
                    page.mouse.click(*dele); page.wait_for_timeout(3000)
                    ok = find(page, "Delete", y0=300, y1=700) or find(page, "OK", y0=300, y1=700)
                    print("  confirm at", ok)
                    if ok:
                        page.mouse.click(*ok); page.wait_for_timeout(6000)
        for tab, eid, want in (("body", s["ps_eid"], 20), ("head", s["head_eid"], 47)):
            goto(page, eid)
            print(" ", tab, rolltoend(page))
            n = faces(page, eid)
            print(f"  {tab}: {n} faces", "RESTORED" if n == want else "*** NOT RESTORED ***")
        print("tabs after:", [t[0] for t in tabs(page)])
