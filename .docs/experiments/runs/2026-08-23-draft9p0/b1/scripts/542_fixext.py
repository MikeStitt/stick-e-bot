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
    page.mouse.click(356, 182); page.wait_for_timeout(800)
    gui.pick(page, (922, 620), "blade region")
    page.wait_for_timeout(1200)
    labs = {l: (x, y) for l, x, y in gui.labels(page)}
    print(labs.get("Symmetric"), labs.get("Depth"))
    els = gui.number_fields(page)
    gui.set_field(page, els[0], "#blade"); page.wait_for_timeout(900)
    sy = labs.get("Symmetric")
    page.mouse.click(276, sy[1]); page.wait_for_timeout(1500)
    page.screenshot(path=D+"tl11.png")
    gui.tick(page); page.wait_for_timeout(3000)
    s = common.load()
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
