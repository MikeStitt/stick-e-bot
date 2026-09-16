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
A = pt(-16, 0); B = pt(16, 0); C = pt(16, 8); Dp = pt(-16, 8)
print("A", A, "B", B, "C", C, "D", Dp)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    for nm, q in (("R", R), ("A", A), ("B", B), ("C", C), ("D", Dp), ("top of pivot", (36,0,48))):
        print(nm, gui.project(page, *q, cam=cam))
