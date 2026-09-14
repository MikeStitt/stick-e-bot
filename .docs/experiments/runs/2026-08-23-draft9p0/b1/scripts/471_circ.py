import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common, json
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s, cam = gui.zoom_to(page, 5.5)
    P = lambda x, y: tuple(round(v) for v in gui.project(page, x, y, 0, cam))
    pts = {k: P(*v) for k, v in {
        "o": (0, 0), "cA": (0, 16), "rA": (16, 16), "cB": (0, -40), "rB": (24, -40),
        "heel": (0, 32), "toe": (0, -64)}.items()}
    print("scale", round(s, 3), pts)
    json.dump({"scale": s, "cam": cam}, open(D + "cam_foot.json", "w"))
    gui.search_tool(page, "Circle")
    for c, r in (("cA", "rA"), ("cB", "rB")):
        page.mouse.move(*pts[c]); page.wait_for_timeout(500)
        page.mouse.click(*pts[c]); page.wait_for_timeout(600)
        page.mouse.move(*pts[r]); page.wait_for_timeout(500)
        page.mouse.click(*pts[r]); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.screenshot(path=D+"tk60.png")
