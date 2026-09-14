import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(328, 93)                 # blur into the dialog title
    page.wait_for_timeout(1200)
    els = gui.number_fields(page)
    print("before", [e.input_value() for e in els])
    els[0].click(); page.wait_for_timeout(500)
    page.keyboard.press("Meta+A"); page.wait_for_timeout(300)
    page.keyboard.type("#valley_deep"); page.wait_for_timeout(1200)
    page.mouse.click(328, 93)                 # blur
    page.wait_for_timeout(2000)
    print("after", [e.input_value() for e in gui.number_fields(page)])
    page.screenshot(path=D+"tl37.png")
