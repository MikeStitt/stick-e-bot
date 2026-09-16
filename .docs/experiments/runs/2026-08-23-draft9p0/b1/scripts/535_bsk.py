import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common, json
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
JS = """(t) => { const out=[];
  for (const e of document.querySelectorAll('span,div,a')) {
    if (e.children.length) continue;
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.x < 250) out.push([Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]);
  } return out; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(150, 400)
    for _ in range(25):
        page.mouse.wheel(0, -120); page.wait_for_timeout(40)
    page.wait_for_timeout(800)
    hit = page.evaluate(JS, "Front")
    print("Front row", hit)
    page.mouse.click(*hit[0]); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4000)
    print([r for r in gui.labels(page) if r[2] < 200 and r[1] > 250])
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1200)
    s, cam = gui.zoom_to(page, 12.0)
    P = lambda x, z: tuple(round(v) for v in gui.project(page, x, 0, z, cam))
    pts = {"o": P(0,0), "A": P(10.9087,5), "B": P(-10.9087,5), "C": P(-10.9087,-20),
           "Dd": P(10.9087,-20), "top": P(0,12)}
    print("scale", round(s,3), pts)
    json.dump({"cam": cam}, open(D+"cam_hinge.json","w"))
    page.screenshot(path=D+"tl04.png")
