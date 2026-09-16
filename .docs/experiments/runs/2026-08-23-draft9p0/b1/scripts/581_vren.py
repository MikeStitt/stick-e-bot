import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
F = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/frames/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Extrude 1", "click lock valley")
    page.wait_for_timeout(2000)
    print(common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-1])
    gui.clear(page); gui.no_banner(page)
    page.mouse.move(900, 500)
    page.keyboard.press("Shift+2"); page.wait_for_timeout(1200)   # Back: the -Y face toward us
    gui.fit(page); gui.still(page)
    gui.frame(page, F+"cad.parts.hinge.blade.valley.png")
