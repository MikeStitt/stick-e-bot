import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "#? = 96 mm")
    page.mouse.dblclick(x, y); page.wait_for_timeout(2000)
    info = page.evaluate("""() => {
      const d = document.querySelector('#feature-dialog');
      return [...d.querySelectorAll('input,textarea')].map(e => {
        const r = e.getBoundingClientRect();
        return {tag:e.tagName, type:e.type, cls:e.className.slice(0,60), name:e.getAttribute('name'),
                ph:e.placeholder, val:e.value, x:Math.round(r.x), y:Math.round(r.y), w:Math.round(r.width)};
      });
    }""")
    for i, e in enumerate(info):
        print(i, e)
