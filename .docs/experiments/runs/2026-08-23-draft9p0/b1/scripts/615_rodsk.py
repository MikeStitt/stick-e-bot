import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    common.scroll_tree(page, 25)
    hit = common.jrow(page, "Top")
    print("Top row", hit)
    page.mouse.click(*hit); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4500)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(1400)
    gui.fit(page); page.wait_for_timeout(1000)
    s, cam = gui.zoom_to(page, 15.0)
    P = lambda x, y: tuple(round(v) for v in gui.project(page, x, y, 0, cam))
    print("scale", round(s,3), "O", P(0,0), "R", P(12,0), "Q", P(8.485,8.485))
    page.screenshot(path=D+"tl56.png")
