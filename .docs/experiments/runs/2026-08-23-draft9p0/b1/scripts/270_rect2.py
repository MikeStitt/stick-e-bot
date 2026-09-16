import sys, math
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
t = math.radians(53); yw = math.radians(30)
d = (math.cos(t)*math.cos(yw), -math.cos(t)*math.sin(yw), -math.sin(t))
N = (math.sin(yw), math.cos(yw), 0.0)
r = (d[1]*N[2]-d[2]*N[1], d[2]*N[0]-d[0]*N[2], d[0]*N[1]-d[1]*N[0])
R = (36.0, 0.0, 40.0)
def pt(a, b): return tuple(R[i] + a*d[i] + b*r[i] for i in range(3))
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(800)
    page.mouse.click(700, 920); page.wait_for_timeout(800)
    scale, cam = gui.px_per_mm(page)
    A = gui.project(page, *pt(-17, 0), cam=cam)
    B = gui.project(page, *pt(15, 0), cam=cam)
    C = gui.project(page, *pt(15, 9), cam=cam)
    print(scale, A, B, C)
    gui.search_tool(page, "Aligned rectangle")
    page.wait_for_timeout(1200)
    for q in (A, B, C):
        page.mouse.move(round(q[0]), round(q[1])); page.wait_for_timeout(500)
        page.mouse.click(round(q[0]), round(q[1])); page.wait_for_timeout(900)
    page.keyboard.press("Escape"); page.wait_for_timeout(1200)
    page.screenshot(path=D + "tj28.png")
