import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

def setnum(page, y, expr):
    page.mouse.click(400, y)
    page.wait_for_timeout(500)
    page.keyboard.press("Meta+A")
    page.keyboard.type(expr)
    page.wait_for_timeout(400)
    page.mouse.click(328, 93)
    page.wait_for_timeout(1500)

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    setnum(page, 261, "#slot_deep")
    setnum(page, 369, "#nose")
    page.screenshot(path=D+"tl70.png")
