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
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1500)
    gui.fit(page); page.wait_for_timeout(2000)
    gui.frame(page, D + "frames/cad.parts.foot.hero.png")
    gui.frame(page, D + "frames/cad.parts.foot.connector.png")
    page.mouse.move(150, 400)
    for _ in range(30):
        page.mouse.wheel(0, 120); page.wait_for_timeout(35)
    page.wait_for_timeout(1200)
    gui.frame(page, D + "frames/cad.parts.foot.tree.png")
