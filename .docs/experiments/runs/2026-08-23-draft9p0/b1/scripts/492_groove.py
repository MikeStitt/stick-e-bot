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
    for _ in range(20):
        page.mouse.wheel(0, -120); page.wait_for_timeout(50)
    page.wait_for_timeout(900)
    hits = page.evaluate(JS, "Top")
    print("Top rows:", hits)
    page.mouse.click(*hits[0]); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4000)
    print([r for r in gui.labels(page) if r[2] < 200 and r[1] > 250])
    page.keyboard.press("Shift+5"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1200)
    s, cam = gui.zoom_to(page, 5.0)
    P = lambda x, y: tuple(round(v) for v in gui.project(page, x, y, 0, cam))
    print("scale", round(s, 3), "o", P(0, 0), "c", P(0, -61), "corner", P(48, -58))
    page.screenshot(path=D+"tk78.png")
