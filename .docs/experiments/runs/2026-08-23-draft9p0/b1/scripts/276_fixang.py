import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.dblclick(1048, 149); page.wait_for_timeout(1500)
    print(page.evaluate("""() => Array.from(document.querySelectorAll('input'))
        .filter(e => e.offsetParent).map(e => { const r = e.getBoundingClientRect();
          return [e.value, Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]; })"""))
    page.screenshot(path=D + "tj34.png", clip={"x": 900, "y": 90, "width": 500, "height": 300})
