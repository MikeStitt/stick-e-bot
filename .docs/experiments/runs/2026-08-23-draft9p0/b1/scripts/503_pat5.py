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
    print("fields", len(els))
    gui.set_field(page, els[0], "2 * #rib_w"); page.wait_for_timeout(900)
    els = gui.number_fields(page)
    gui.set_field(page, els[1], "#foot_l / (2 * #rib_w)"); page.wait_for_timeout(1500)
    page.keyboard.press("Shift+6"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1200)
    page.screenshot(path=D+"tk86.png")
