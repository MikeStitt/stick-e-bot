import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.frame(page, D + "frames/cad.parts.hinge.blade.profile_sketch.png")
    gui.tick(page); page.wait_for_timeout(2500)
    gui.rename_row(page, "Sketch 1", "blade profile"); page.wait_for_timeout(1200)
    gui.clear(page)
    x, y = gui.row(page, "blade profile")
    page.mouse.click(x, y); page.wait_for_timeout(900)
    gui.search_tool(page, "Extrude")
    page.wait_for_timeout(1800)
    els = gui.number_fields(page)
    gui.set_field(page, els[0], "#blade"); page.wait_for_timeout(800)
    page.mouse.click(276, 340); page.wait_for_timeout(1500)   # Symmetric
    page.screenshot(path=D+"tl07.png")
    gui.tick(page); page.wait_for_timeout(3000)
    gui.rename_row(page, "Extrude 1", "blade blank"); page.wait_for_timeout(1200)
    s = common.load()
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
