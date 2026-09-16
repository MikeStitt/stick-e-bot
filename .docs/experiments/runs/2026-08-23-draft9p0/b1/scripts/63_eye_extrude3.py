import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Add")
    page.mouse.click(x, y); page.wait_for_timeout(1200)
    el = gui.number_fields(page)[0]
    el.click(); page.wait_for_timeout(300)
    el.fill("33 mm"); page.wait_for_timeout(400)
    el.press("Tab"); page.wait_for_timeout(2000)
    print("depth:", el.input_value(), "dialog:", page.locator("#feature-dialog").count())
    page.screenshot(path="ey7.png")
