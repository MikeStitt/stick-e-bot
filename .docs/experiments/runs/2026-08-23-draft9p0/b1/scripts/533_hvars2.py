import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
V = [("blade_half", "sqrt(#limbD ^ 2 / 4 - #blade ^ 2 / 4)"),
     ("stub", "4 mm"), ("stub_proud", "1.6 mm"), ("pocket_d", "4.4 mm"),
     ("teeth_ri", "8.8 mm"), ("teeth_r", "10.4 mm")]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for n, v in V:
        common.add_var(page, gui, n, v)
    print("done")
