import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui
from playwright.sync_api import sync_playwright
DUMP = """() => { const o = [];
  for (const e of document.querySelectorAll('li,a,div,span,button')) {
    if (e.children.length) continue;
    const t = (e.innerText||'').trim();
    if (!t || t.length > 44) continue;
    const r = e.getBoundingClientRect();
    if (r.width && r.height && r.height < 46 && r.y > 300)
      o.push([t, Math.round(r.x + r.width/2), Math.round(r.y + r.height/2)]);
  } return o; }"""
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up(); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.mouse.click(57, 984); page.wait_for_timeout(3500)
    for t, x, y in page.evaluate(DUMP):
        print(f"  {t!r} at ({x},{y})")
    page.screenshot(path=D + "plusmenu.png")
    page.keyboard.press("Escape")
