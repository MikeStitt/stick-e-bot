import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.at(page, "Offset all")
    page.mouse.click(x, y); page.wait_for_timeout(1800)
    el = gui.number_fields(page)[0]
    el.click(); el.fill("#fit"); el.press("Tab"); page.wait_for_timeout(2000)
    kx, ky = gui.at(page, "Keep tools")
    page.mouse.click(kx, ky); page.wait_for_timeout(2000)
    print("labels:", [l[0] for l in gui.labels(page)])
    print("fields:", [f.input_value() for f in gui.number_fields(page)])
    page.screenshot(path=D + "bs21.png")
