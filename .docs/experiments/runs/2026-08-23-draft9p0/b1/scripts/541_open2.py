import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
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
    for _ in range(12):
        page.mouse.wheel(0, 120); page.wait_for_timeout(40)
    page.wait_for_timeout(900)
    hit = page.evaluate(JS, "blade blank")
    print("row", hit)
    page.mouse.dblclick(*hit[0]); page.wait_for_timeout(3000)
    for r in gui.labels(page):
        if r[2] < 480 and r[1] < 480:
            print(r)
    page.screenshot(path=D+"tl10.png")
