import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    common.add_var(page, gui, "hip_half", "#torsoH / 4")
    common.add_var(page, gui, "shoulder_half", "#torsoW / 2")
    common.add_var(page, gui, "shoulder_drop", "8 mm")
    common.add_var(page, gui, "shoulder_len", "26 mm")
    print(gui.tree(page)[-8:])
