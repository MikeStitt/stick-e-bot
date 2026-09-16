import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.dimension(page, [(1191, 523)], (1300, 380), "#limbD")
    page.wait_for_timeout(1800)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    page.screenshot(path=D+"ub06.png")
