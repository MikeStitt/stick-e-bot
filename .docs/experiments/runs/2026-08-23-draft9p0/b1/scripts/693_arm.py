import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Mirror 1", "two forks")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    common.scroll_tree(page, 25)
    page.mouse.click(*common.jrow(page, "Top")); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4500)
    page.keyboard.press("Shift+5"); page.wait_for_timeout(1500)
    gui.fit(page); page.wait_for_timeout(1000)
    sc, cam = gui.zoom_to(page, 12.0)
    P = lambda x, y: tuple(round(v) for v in gui.project(page, x, y, 0, cam))
    print("scale", round(sc,3), {"O": P(0,0), "R": P(12,0)})
    json.dump({"cam": cam}, open(D+"cam_farm.json","w"))
