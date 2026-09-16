import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["foot_eid"]
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "foot pedestal")
    page.mouse.dblclick(x, y); page.wait_for_timeout(2500)
    page.mouse.click(453, 370); page.wait_for_timeout(1500)
    page.screenshot(path=D+"tk55.png")
    from PIL import Image
    Image.open(D+"tk55.png").crop((240,80,470,450)).resize((690,1110)).save(D+"tk55c.png")
    gui.tick(page); page.wait_for_timeout(3000)
    print(common.bbox(page, api, did, wid, eid))
