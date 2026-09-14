import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.name_feature(page, "upper rounds")
    gui.tick(page)
    print("tree:", gui.tree(page))
    # tilt the camera under the part with a middle-button drag
    page.mouse.move(*screen.CENTER)
    page.mouse.down(button="middle")
    page.mouse.move(screen.CENTER[0], screen.CENTER[1] - 260, steps=14)
    page.mouse.up(button="middle")
    page.wait_for_timeout(1500)
    gui.fit(page)
    s, cam = gui.px_per_mm(page)
    print("px/mm", round(s, 3),
          "bottom center ->", tuple(round(v) for v in gui.project(page, 0, 0, -36, cam=cam)))
    page.screenshot(path="hd12.png")
