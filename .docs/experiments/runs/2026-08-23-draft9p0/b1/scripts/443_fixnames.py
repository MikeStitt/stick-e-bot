import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
NAMES = ["#foot_l", "#foot_w", "#ankle_h", "#plate", "#top_round", "#ball", "#wall",
         "#collar", "#grip"]
VALS  = ["96 mm", "48 mm", "24 mm", "12 mm", "8 mm", "12 mm", "3 mm", "11 mm", "3.6 mm"]
lo, hi = int(sys.argv[1]), int(sys.argv[2])
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for i in range(lo, hi):
        row = "#? = " + VALS[i]
        x, y = gui.row(page, row)
        page.mouse.dblclick(x, y); page.wait_for_timeout(1800)
        els = page.query_selector_all("#feature-dialog input")
        els[1].click(); page.wait_for_timeout(300)
        page.keyboard.press("Meta+A")
        page.keyboard.type(NAMES[i])
        page.wait_for_timeout(400)
        page.keyboard.press("Tab"); page.wait_for_timeout(800)
        title = page.query_selector("#feature-dialog").inner_text().split("\n")[0]
        print(NAMES[i], "->", title)
        gui.tick(page); page.wait_for_timeout(1500)
