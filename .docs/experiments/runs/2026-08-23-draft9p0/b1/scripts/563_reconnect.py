import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(957, 99)      # "Click here to reconnect."
    page.wait_for_timeout(15000)
    try:
        screen.hook(page)
    except Exception as e:
        print("hook", e)
    page.evaluate("window.name = 'DRAFT9P0_BUILD'")
    page.wait_for_timeout(2000)
    page.screenshot(path=D+"tl25.png")
