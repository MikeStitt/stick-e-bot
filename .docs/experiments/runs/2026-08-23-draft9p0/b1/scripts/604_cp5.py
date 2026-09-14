import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = gui.number_fields(page)
    print("fields", [e.input_value() for e in els])
    for el, txt in ((els[0], "360 deg"), (els[1], "24")):
        el.click(); page.wait_for_timeout(400)
        page.keyboard.press("Meta+A"); page.wait_for_timeout(250)
        page.keyboard.type(txt); page.wait_for_timeout(900)
        page.mouse.click(328, 93); page.wait_for_timeout(1500)
    print("now", [e.input_value() for e in gui.number_fields(page)])
    page.screenshot(path=D+"tl49.png")
