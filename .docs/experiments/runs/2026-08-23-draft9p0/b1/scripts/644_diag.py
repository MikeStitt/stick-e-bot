import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.dblclick(641, 619)
    page.wait_for_timeout(1500)
    info = page.evaluate("""() => { const a = document.activeElement;
        const r = a.getBoundingClientRect();
        return [a.tagName, a.className, a.value, Math.round(r.x), Math.round(r.y), Math.round(r.width)]; }""")
    print(info)
    page.screenshot(path=D+"tl75.png")
