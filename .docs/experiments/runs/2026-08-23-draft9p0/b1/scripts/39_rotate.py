import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.move(*screen.CENTER)
    for _ in range(4):
        page.keyboard.press("ArrowDown")
        page.wait_for_timeout(400)
    page.wait_for_timeout(1200)
    s, cam = gui.px_per_mm(page)
    print("bottom center ->", tuple(round(v) for v in gui.project(page, 0, 0, -36, cam=cam)))
    print("top center    ->", tuple(round(v) for v in gui.project(page, 0, 0, 36, cam=cam)))
    page.screenshot(path="hd13.png")
