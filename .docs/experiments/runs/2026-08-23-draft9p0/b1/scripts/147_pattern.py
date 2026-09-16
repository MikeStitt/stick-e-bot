import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    gui.pick(page, (1050, 514), "top edge")
    for spot, what in [((1050, 531), "bottom"), ((1063, 518), "right"), ((982, 518), "left")]:
        gui.pick(page, spot, what, add=True)
    gui.search_tool(page, "Circular pattern", settle=2500)
    page.screenshot(path=D + "bs31.png")
    for lab, xy in gui.labels(page).items():
        print(f"  {lab!r:44s} {xy}")
