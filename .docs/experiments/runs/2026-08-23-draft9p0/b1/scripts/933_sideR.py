import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

TABS = {"u limb": (3.6, -112.4), "l limb": (12.0, -108.0)}

def tab(page, name):
    hits = page.evaluate("""(nm) => { const out=[];
      for (const e of document.querySelectorAll('span,div,a')) {
        if (e.children.length) continue;
        const r=e.getBoundingClientRect();
        if (r.y>965 && (e.innerText||'').trim()===nm)
          out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
      } return out; }""", name)
    page.mouse.click(*hits[0]); page.wait_for_timeout(6000)

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for name, (hi, lo) in TABS.items():
        tab(page, name)
        gui.clear(page)
        page.mouse.move(900, 500); page.wait_for_timeout(300)
        page.keyboard.press("Shift+4"); page.wait_for_timeout(2200)
        gui.fit(page); page.wait_for_timeout(1600)
        sc, cam = gui.px_per_mm(page)
        mid = gui.project(page, 0.0, 0.0, (hi + lo) / 2, cam)
        sc, cam = gui.zoom_to(page, 6.0, at_px=(int(mid[0]), int(mid[1]))); page.wait_for_timeout(1500)
        t = gui.project(page, 0.0, 0.0, hi, cam)
        b = gui.project(page, 0.0, 0.0, lo, cam)
        print(name, round(sc, 3), t, b)
        page.mouse.move(1450, 300); page.wait_for_timeout(500)
        gui.frame(page, D + f"sideR_{name.replace(' ', '_')}.png")
        print("  top/bot px", t[1], b[1], "x", t[0])
