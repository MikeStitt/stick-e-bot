import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.dimension(page, [(1050, 846)], (1000, 940), "2 * #foot_w")
    gui.dimension(page, [(1166, 831)], (1330, 830), "#rib_w")
    gui.dimension(page, [(700, 523), (1050, 846)], (600, 690), "#foot_l - #heel_y")
    gui.clear(page)
    page.screenshot(path=D+"tk80.png")
