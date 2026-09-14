import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

def status(page):
    return page.evaluate("""() => {
      const out = [];
      for (const e of document.querySelectorAll('div,span')) {
        if (e.children.length) continue;
        const t = (e.innerText || '').trim();
        if (/^(Length|Parallel dist|Radius|Diameter)/.test(t)) out.push(t);
      }
      return out; }""")

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for y in (517, 519, 520, 526, 527, 529):
        page.mouse.move(1063, y); page.wait_for_timeout(700)
        print("right x=1063 y=", y, status(page))
    for y in (517, 519, 520, 526, 527, 529):
        page.mouse.move(982, y); page.wait_for_timeout(700)
        print(" left x= 982 y=", y, status(page))
