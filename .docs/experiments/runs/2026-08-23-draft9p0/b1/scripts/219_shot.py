import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    rows = page.evaluate("""() => Array.from(document.querySelectorAll('.os-list-item'))
        .map(e => { const r = e.getBoundingClientRect();
          return [e.innerText.trim().split('\\n')[0], Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]; })""")
    for r in rows: print(r)
    page.screenshot(path=D + "hs22.png")
