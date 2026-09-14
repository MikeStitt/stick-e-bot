import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(258, 305); page.wait_for_timeout(2500)     # flip primary axis
    gui.tick(page); page.wait_for_timeout(5000)
    gui.rename_row(page, "Transform 1", "move fork"); page.wait_for_timeout(1500)
    print("bbox", common.bbox(page, api, s["did"], s["wid"], s["ul_eid"]))
