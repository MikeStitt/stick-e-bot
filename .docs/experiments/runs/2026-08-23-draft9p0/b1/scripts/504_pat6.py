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
    el = els[1]
    el.click(); page.wait_for_timeout(400)
    page.keyboard.press("Meta+A")
    page.keyboard.type("#foot_l / (2 * #rib_w)", delay=45)
    page.wait_for_timeout(900)
    page.mouse.click(274, 254)          # click the Distance label to blur
    page.wait_for_timeout(1500)
    page.mouse.click(455, 276)          # flip the direction
    page.wait_for_timeout(2000)
    gui.fit(page); page.wait_for_timeout(1000)
    page.screenshot(path=D+"tk87.png")
