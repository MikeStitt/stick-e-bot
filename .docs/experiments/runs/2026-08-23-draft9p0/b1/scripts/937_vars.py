import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
VARS = [("#gripperL", "#torsoH / 4"), ("#clipR", "5 mm"), ("#barD", "3.2 mm"),
        ("#bore", "#barD + 0.1 mm"), ("#mouth", "2.6 mm")]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print("url", page.url[-32:])
    for n, v in VARS:
        common.add_var(page, gui, n, v)
    page.wait_for_timeout(1200)
    print(gui.tree(page))
