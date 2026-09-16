import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    if page.locator("#feature-dialog").count():
        page.mouse.click(451, 93); page.wait_for_timeout(1800)
    gui.clear(page)
    page.mouse.move(*screen.CENTER)
    for _ in range(2):
        page.keyboard.press("ArrowUp"); page.wait_for_timeout(400)
    page.wait_for_timeout(1200)
    gui.fit(page)
    s, cam = gui.px_per_mm(page)
    print("px/mm", round(s, 3))
    for nm, pt in [("bot front", (0, -30, -36)), ("bot back", (0, 30, -36)),
                   ("bot left", (-36, 0, -36)), ("bot right", (36, 0, -36)),
                   ("corner arc", (32.485, -26.485, -36))]:
        print(f"  {nm:11s} -> {tuple(round(v) for v in gui.project(page, *pt, cam=cam))}")
    page.screenshot(path="hd22.png")
