import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui

def between_chip(page):
    labs = gui.labels(page)
    ys = [r[2] for r in labs if r[0] == "Between entity"]
    if not ys: return None
    y = ys[0]
    for r in labs:
        if r[2] == y + 20 and r[1] == 349:
            return r[0]
    return None

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    cur = between_chip(page)
    if cur:
        page.mouse.click(447, [r[2] for r in gui.labels(page) if r[0]=="Between entity"][0] + 20)
        page.wait_for_timeout(1500)
    for dx, dy in [(58,0), (-58,0), (41,41), (-41,-41), (0,58), (54,0), (60,0)]:
        y0 = [r[2] for r in gui.labels(page) if r[0]=="Between entity"][0]
        page.mouse.click(356, y0); page.wait_for_timeout(800)
        px = (922 + dx, 864 + dy)
        page.mouse.move(*px); page.wait_for_timeout(900)
        page.mouse.click(*px); page.wait_for_timeout(2000)
        got = between_chip(page)
        print(px, "->", got)
        if got and "Edge" in got:
            break
        if got:
            y0 = [r[2] for r in gui.labels(page) if r[0]=="Between entity"][0]
            page.mouse.click(447, y0 + 20); page.wait_for_timeout(1500)
