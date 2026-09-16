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
    page.mouse.click(356, 203); page.wait_for_timeout(900)
    page.mouse.move(150, 400)
    for _ in range(30):
        page.mouse.wheel(0, -120); page.wait_for_timeout(40)
    page.wait_for_timeout(900)
    hit = page.evaluate(JS, "Front")
    print("Front", hit)
    page.mouse.click(*hit[0]); page.wait_for_timeout(1800)
    for r in gui.labels(page):
        if r[2] < 320 and r[1] < 480:
            print(r)
    page.screenshot(path=D+"tk85.png")
