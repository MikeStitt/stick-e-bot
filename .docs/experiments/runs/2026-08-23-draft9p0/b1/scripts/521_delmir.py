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
    gui.clear(page)
    common.delete_row(page, gui, "Mirror 1")
    page.wait_for_timeout(1500)
    s = common.load()
    print([r for r in gui.tree(page)][-4:])
    print(common.volume(page, api, s["did"], s["wid"], s["foot_eid"], "JHD"))
    page.keyboard.press("Shift+5"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1200)
    sc, cam = gui.zoom_to(page, 22.0)
    P = lambda x, y, z: tuple(round(v) for v in gui.project(page, x, y, z, cam))
    print("scale", round(sc, 3), "centre", P(0, 0, -6.8), "off", P(2.0, 0, -6.5))
    page.screenshot(path=D+"tk96.png")
