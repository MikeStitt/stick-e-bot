import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(380, 261); page.wait_for_timeout(2200)
    gui.frame(page, F + "cad.parts.l_limb.limbseg.png",
              clip={"x": 246, "y": 80, "width": 454, "height": 340})
