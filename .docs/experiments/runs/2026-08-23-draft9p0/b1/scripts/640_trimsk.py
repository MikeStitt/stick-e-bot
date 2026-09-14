import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    common.scroll_tree(page, 25)
    page.mouse.click(*common.jrow(page, "Front")); page.wait_for_timeout(900)
    page.mouse.click(155, 58); page.wait_for_timeout(4500)
    page.keyboard.press("Shift+1"); page.wait_for_timeout(1400)
    gui.fit(page); page.wait_for_timeout(1000)
    s, cam = gui.zoom_to(page, 12.0)
    P = lambda x, z: tuple(round(v) for v in gui.project(page, x, 0, z, cam))
    pts = {"O": P(0,0), "Rc": P(12,0),
           "TL": P(-14, 5.6), "BR": P(14, -14),
           "cutL": P(-13, -6), "cutR": P(13, -6), "cutB": P(0, -13)}
    print("scale", round(s,3), pts)
    json.dump({"cam": cam}, open(D+"cam_trim.json","w"))
    page.screenshot(path=D+"tl71.png")
