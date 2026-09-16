import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
F = D + "frames/cad.parts.u_limb."
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page); gui.still(page)
    # medium: whole limb, ring both ends
    a = [round(v) for v in gui.project(page, 0, 0, 0)]
    b = [round(v) for v in gui.project(page, 0, 0, -100.4)]
    c = [round(v) for v in gui.project(page, 0, 0, -55.4)]
    print("shoulder", a, "elbow", b, "forkjoin", c)
    gui.ring(page, F + "ends.medium.png", a, radius=46)
    gui.ring(page, F + "elbow_end.medium.png", b, radius=46)
    gui.ring(page, F + "move_fork.medium.png", c, radius=46)
