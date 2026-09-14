"""Put the four hidden planes back on in `body`.

2312's finally ran with the feature tree scrolled to the bottom, where gui.row
cannot see a plane row, so it timed out before showing any of them.
"""
import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
FIND = """(a) => { const [t, x0] = a; let best = null, area = 1e9;
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if ((e.innerText||'').trim() !== t) continue;
    const r = e.getBoundingClientRect();
    if (!r.width || !r.height || r.height > 46 || r.x + r.width/2 < x0) continue;
    if (r.width*r.height < area) { area = r.width*r.height;
      best = [Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]; }
  } return best; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.mouse.move(140, 400)
    for _ in range(12):
        page.mouse.wheel(0, -400); page.wait_for_timeout(250)
    page.wait_for_timeout(1500)
    for pl in ("Top", "Front", "Right", "plane for shoulder"):
        page.keyboard.press("Escape"); page.wait_for_timeout(500)
        page.mouse.click(*gui.row(page, pl), button="right"); page.wait_for_timeout(1600)
        hit = page.evaluate(FIND, ["Show", 150])
        if hit:
            page.mouse.click(*hit); page.wait_for_timeout(2500)
            print(f"  {pl}: shown")
        else:
            page.keyboard.press("Escape")
            print(f"  {pl}: already shown")
    page.screenshot(path=D + "planes_back.png")
