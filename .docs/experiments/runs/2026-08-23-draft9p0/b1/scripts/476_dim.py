import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common, math
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    k = 5.358
    a = (923, 437); b = (923, 737)
    ea = (round(a[0] + 16*k*0.7071), round(a[1] - 16*k*0.7071))
    eb = (round(b[0] + 24*k*0.7071), round(b[1] - 24*k*0.7071))
    print("edges", ea, eb)
    gui.dimension(page, [ea], (1330, 380), "2 * #heel_r")
    gui.dimension(page, [eb], (1330, 800), "#foot_w")
    page.screenshot(path=D+"tk67.png")
