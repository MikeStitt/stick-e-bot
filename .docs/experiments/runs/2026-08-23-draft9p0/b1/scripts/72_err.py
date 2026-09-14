import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "second eye")
    page.mouse.move(x, y); page.wait_for_timeout(2500)
    txt = page.evaluate("""() => Array.from(document.querySelectorAll('div,span'))
        .filter(e => !e.children.length && (e.innerText||'').length > 20)
        .map(e => e.innerText.trim()).slice(-12)""")
    print("\n--\n".join(txt))
    gui.frame(page, D + "mi7.png")
