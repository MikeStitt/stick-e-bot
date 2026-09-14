import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
F = D + "frames/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page); page.wait_for_timeout(3000)
    gui.rename_row(page, "Ball 1", "head to neck")
    page.wait_for_timeout(2000)
    gui.clear(page)
    gui.fit(page); page.wait_for_timeout(2500)
    page.mouse.move(900, 500); page.wait_for_timeout(2500)
    page.screenshot(path=F+"cad.assembly.mate_head.png")
    for r in gui.tree(page): print(r)
