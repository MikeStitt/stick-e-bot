import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    x, y = gui.row(page, "plane for shoulder")
    page.mouse.dblclick(x, y); page.wait_for_timeout(2500)
    rows = {r[0]: (r[1], r[2]) for r in gui.labels(page)}
    print(rows)
    page.mouse.click(447, 168); page.wait_for_timeout(1500)   # drop the vertex (2nd entry)
    for r in gui.labels(page): print(r)
    scale, cam = gui.px_per_mm(page)
    pt = gui.project(page, 36, 0, 42, cam=cam)
    print("pick", pt)
    page.mouse.move(round(pt[0]), round(pt[1])); page.wait_for_timeout(900)
    page.mouse.click(round(pt[0]), round(pt[1])); page.wait_for_timeout(2000)
    for r in gui.labels(page): print(r)
    page.screenshot(path=D + "tj21.png")
