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
    gui.set_field(page, els[0], "#ankle_h - #plate")
    page.wait_for_timeout(800)
    page.mouse.click(453, 230); page.wait_for_timeout(1200)   # flip main direction
    page.mouse.click(276, 313); page.wait_for_timeout(1500)   # Starting offset on
    els = gui.number_fields(page)
    print("fields", len(els))
    gui.set_field(page, els[1], "#plate")
    page.wait_for_timeout(1000)
    page.mouse.click(453, 370); page.wait_for_timeout(1500)   # flip the offset
    page.screenshot(path=D+"tk74.png")
