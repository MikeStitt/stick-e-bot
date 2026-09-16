import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(400)
    page.mouse.click(451, 93); page.wait_for_timeout(1500)
    for n, v in (("heel_r", "#foot_w / 3"), ("toe_r", "#foot_w / 2"), ("heel_y", "#foot_l / 3")):
        common.add_var(page, gui, n, v)
    s = common.load()
    for name, fid, st in common.features(page, api, s["did"], s["wid"], s["foot_eid"]):
        print(f"{st:8} {name}")
