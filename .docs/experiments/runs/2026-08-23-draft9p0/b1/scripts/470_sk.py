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
    x, y = gui.row(page, "Top")
    page.mouse.click(x, y); page.wait_for_timeout(700)
    page.mouse.click(155, 58); page.wait_for_timeout(4000)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(1200)
    gui.fit(page); page.wait_for_timeout(1200)
    s, cam = gui.zoom_to(page, 7.0)
    print("scale", s)
    for pt in ((0,0), (0,16), (0,-40), (24,-40), (-24,-40), (16,16), (-16,16), (0,32), (0,-64)):
        print(pt, [round(v) for v in gui.project(page, pt[0], pt[1], 0, cam)])
    page.screenshot(path=D+"tk59.png")
