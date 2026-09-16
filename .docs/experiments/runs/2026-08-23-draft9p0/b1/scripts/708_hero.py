import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen

CLIP = {"x": 500, "y": 70, "width": 1000, "height": 880}

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.keyboard.press("Escape"); page.wait_for_timeout(500)
    page.mouse.move(1000, 500); page.wait_for_timeout(300)
    page.keyboard.press("p"); page.wait_for_timeout(1000)      # planes off
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1800)
    gui.fit(page); page.wait_for_timeout(1500)
    page.mouse.move(1450, 940); page.wait_for_timeout(700)
    print("selected", screen.selected(gui.probe(page)))
    gui.frame(page, F + "cad.parts.hinge.hero.png", clip=CLIP)
