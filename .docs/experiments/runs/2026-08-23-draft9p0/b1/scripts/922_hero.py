import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(900, 500); page.wait_for_timeout(300)
    page.keyboard.press("p"); page.wait_for_timeout(1200)          # planes off
    page.keyboard.press("Shift+7"); page.wait_for_timeout(2200)    # isometric
    gui.fit(page); page.wait_for_timeout(1800)
    print("selected", screen.selected(gui.probe(page)))
    gui.frame(page, F + "cad.parts.l_limb.hero.png")
    gui.frame(page, F + "cad.parts.l_limb.tree.png",
              clip={"x": 40, "y": 140, "width": 210, "height": 580})
    print("ok")
