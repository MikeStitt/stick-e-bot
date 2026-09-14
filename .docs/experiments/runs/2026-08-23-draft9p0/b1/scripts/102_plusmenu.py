import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.screenshot(path=D + "bs0.png")
    txt = page.evaluate("""() => Array.from(document.querySelectorAll('li,a,span,div'))
        .filter(e => !e.children.length && /Create/.test(e.innerText||''))
        .map(e => { const r = e.getBoundingClientRect();
            return [e.innerText.trim(), Math.round(r.x+r.width/2), Math.round(r.y+r.height/2)]; })""")
    print(txt)
