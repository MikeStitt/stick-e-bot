import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

def chip(page, field):
    labs = gui.labels(page)
    ys = [r[2] for r in labs if r[0] == field]
    if not ys: return None
    for r in labs:
        if r[2] == ys[0] + 20 and r[1] == 349: return r[0]
    return None

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    # drop the edge in Origin entity
    page.mouse.click(447, 172); page.wait_for_timeout(1800)
    print("origin now", chip(page, "Origin entity"))
    tgt = [round(v) for v in gui.project(page, 0, 7.0, -100.4)]
    print("target", tgt)
    y0 = [r[2] for r in gui.labels(page) if r[0] == "Origin entity"][0]
    page.mouse.click(356, y0); page.wait_for_timeout(900)
    page.mouse.move(*tgt); page.wait_for_timeout(1200)
    page.mouse.click(*tgt); page.wait_for_timeout(2200)
    print("origin ->", chip(page, "Origin entity"))
    page.screenshot(path=D+"ub33.png")
