import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.no_banner(page)
    page.mouse.move(900, 500)
    page.keyboard.press("Shift+7")
    page.wait_for_timeout(1500)
    gui.fit(page)
    gui.still(page)
    print(gui.frame(page, F+"cad.parts.hinge.blade.blank.png"))
