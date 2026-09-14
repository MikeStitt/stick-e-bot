import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.mouse.move(*screen.CENTER)
    page.keyboard.press("Shift+7"); page.wait_for_timeout(1800)
    gui.fit(page); page.wait_for_timeout(1200)
    s, cam = gui.px_per_mm(page)
    print("px/mm", round(s, 3))
    for name, pt in [("front crown", (0, -30, 36)), ("back crown", (0, 30, 36)),
                     ("front arch 45", (25.46, -30, 25.46)), ("bottom front", (0, -30, -36))]:
        print(f"  {name:16s} {pt} -> {tuple(round(v) for v in gui.project(page, *pt, cam=cam))}")
    page.screenshot(path="hd9.png")
