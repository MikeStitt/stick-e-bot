import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
LL, RL = (817, 572), (1029, 572)
CA, CB = (880, 363), (859, 848)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for line, circ, what in ((LL, CA, "L-heel"), (LL, CB, "L-toe"), (RL, CA, "R-heel"), (RL, CB, "R-toe")):
        gui.clear(page)
        gui.pick(page, line, what + " line")
        gui.pick(page, circ, what + " circle", add=True)
        gui.search_tool(page, "Tangent")
        page.wait_for_timeout(1200)
    gui.clear(page)
    page.screenshot(path=D+"tk70.png")
