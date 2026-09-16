import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(140, 880)          # empty space under the tree
    page.wait_for_timeout(800)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.mouse.move(1450, 900); page.wait_for_timeout(1200)
    print("selected px", screen.selected(gui.probe(page)))
    gui.no_banner(page); gui.still(page)
    gui.frame(page, F+"cad.parts.hinge.blade.valley_round.png",
              clip={"x": 571, "y": 221, "width": 600, "height": 450})
