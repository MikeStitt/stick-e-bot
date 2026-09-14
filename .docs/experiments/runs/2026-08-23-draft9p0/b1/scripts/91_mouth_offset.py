import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    el = gui.number_fields(page)[1]
    el.click(); page.wait_for_timeout(300)
    el.fill("27 mm"); el.press("Tab"); page.wait_for_timeout(2500)
    print("fields:", [f.input_value() for f in gui.number_fields(page)])
    page.mouse.move(*screen.CENTER)
    for _ in range(2):
        page.keyboard.press("ArrowLeft"); page.wait_for_timeout(500)
    page.wait_for_timeout(1500)
    page.screenshot(path=D + "mo16.png")
