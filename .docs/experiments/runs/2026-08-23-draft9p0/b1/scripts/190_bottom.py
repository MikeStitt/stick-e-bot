import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(447, 172)               # clear Origin entity
    page.wait_for_timeout(900)
    page.mouse.move(900, 700)
    for _ in range(8):
        page.keyboard.press("ArrowDown")
        page.wait_for_timeout(400)
    gui.still(page)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    for z in (10, 0, -7.4):
        print(f"z={z}", tuple(round(v) for v in gui.project(page, 0, 0, z, cam=cam)))
    page.screenshot(path=D + "bs61.png")
