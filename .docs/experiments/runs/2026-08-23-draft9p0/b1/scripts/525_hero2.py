import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(400)
    page.mouse.click(1350, 800); page.wait_for_timeout(800)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    gui.fit(page); page.wait_for_timeout(1800)
    gui.frame(page, D + "frames/cad.parts.foot.hero.png")
    gui.frame(page, D + "frames/cad.parts.foot.connector.png")
