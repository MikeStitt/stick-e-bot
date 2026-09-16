import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = D + "frames/cad.parts.u_limb."
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(900, 400)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(2500)
    gui.fit(page); page.wait_for_timeout(2000)
    gui.still(page)
    gui.frame(page, F + "hero.png")
    gui.frame(page, F + "tree.png", clip={"x": 40, "y": 80, "width": 300, "height": 720})
    print("hero + tree done")
