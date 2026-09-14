import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
BALLS = {"neck": (0,0,58), "l_sh": (49.5509,-7.8236,19.2355), "r_sh": (-49.5509,-7.8236,19.2355),
         "l_hip": (24,0,-58), "r_hip": (-24,0,-58)}
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.clear(page)
    page.keyboard.press("Shift+1")
    page.wait_for_timeout(1200)
    gui.fit(page)
    page.wait_for_timeout(1500)
    scale, cam = gui.px_per_mm(page)
    print("scale", scale)
    for k, v in BALLS.items():
        print(k, v, gui.project(page, *v, cam=cam))
    gui.still(page)
    page.screenshot(path=D+"tk06.png")
