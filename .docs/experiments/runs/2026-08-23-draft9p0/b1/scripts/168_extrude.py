import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.fit(page)
    page.keyboard.press("Shift+7")          # isometric, so the depth direction reads
    page.wait_for_timeout(1500)
    gui.fit(page)
    x, y = gui.row(page, "slit profile")
    page.mouse.click(x, y)
    page.wait_for_timeout(900)
    gui.search_tool(page, "Extrude", settle=2500)
    page.screenshot(path=D + "bs46.png")
    for lab, xy in gui.labels(page):
        print(f"  {lab!r:36s} {xy}")
