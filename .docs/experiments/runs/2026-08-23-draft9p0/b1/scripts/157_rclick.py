import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.pick(page, (820, 517), "left copy upper line")
    page.mouse.click(820, 517, button="right")
    page.wait_for_timeout(1500)
    page.screenshot(path=D + "bs40.png")
    for t in ["Edit pattern", "Confirm seed", "Delete sketch entity"]:
        print(t, common.menu_item(page, t))
