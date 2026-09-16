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
    gui.rename_row(page, "Extrude 1", "click bump")
    page.wait_for_timeout(1500)
    page.mouse.click(140, 880); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    common.scroll_tree(page, -25)
    x, y = common.jrow(page, "Part 1")
    page.mouse.click(x, y, button="right"); page.wait_for_timeout(1500)
    hit = common.menu_item(page, "Hide")
    print("hide at", hit)
    page.mouse.click(*hit); page.wait_for_timeout(2000)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    gui.clear(page)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1500)
    sc, cam = gui.zoom_to(page, 40.0, at_px=(923, 400))
    P = lambda x, z: tuple(round(v) for v in gui.project(page, x, 0, z, cam))
    print("scale", round(sc,3), {"O": P(0,0), "bump": P(0,9.6)})
    json.dump({"cam": cam}, open(D+"cam_dome.json","w"))
    page.mouse.move(1450, 900); page.wait_for_timeout(600)
    page.screenshot(path=D+"tl99.png")
