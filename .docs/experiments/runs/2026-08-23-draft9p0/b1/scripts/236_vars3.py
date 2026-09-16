import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.add_var(page, gui, "boss_len", "#shoulder_len - #stand")
    common.add_var(page, gui, "boss_d", "16 mm")
    common.add_var(page, gui, "tilt", "53 deg", kind="Angle")
    common.add_var(page, gui, "yaw", "30 deg", kind="Angle")
    print(gui.tree(page)[-11:])
