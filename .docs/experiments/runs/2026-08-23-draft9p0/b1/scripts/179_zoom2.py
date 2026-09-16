import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.zoom_to(page, 22, at_px=(923, 520))
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    pts = {n: tuple(round(v) for v in gui.project(page, *xyz, cam=cam))
           for n, xyz in {"stalk top": (0,0,10), "collar bottom": (0,0,-7.4),
                          "collar top": (0,0,3.6), "ball": (0,0,0)}.items()}
    print(pts)
    page.screenshot(path=D + "bs54.png")
