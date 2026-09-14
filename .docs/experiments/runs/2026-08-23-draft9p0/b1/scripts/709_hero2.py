import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

CLIP = {"x": 620, "y": 120, "width": 700, "height": 760}

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(1000, 500); page.wait_for_timeout(300)
    page.keyboard.press("p"); page.wait_for_timeout(1200)      # planes off
    gui.zoom_to(page, 7.5, at_px=(970, 500))
    page.mouse.move(1450, 940); page.wait_for_timeout(700)
    gui.frame(page, F + "cad.parts.hinge.hero.png", clip=CLIP)
