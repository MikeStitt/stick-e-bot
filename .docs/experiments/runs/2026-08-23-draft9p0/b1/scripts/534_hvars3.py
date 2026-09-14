import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
V = [("bump_r", "(#teeth_ri + #teeth_r) / 2"), ("bump_d", "#teeth_r - #teeth_ri"),
     ("valley_d", "2 mm"), ("valley_deep", "0.9 mm"), ("tooth_proud", "1.2 mm"),
     ("rod", "#limbD")]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for n, v in V:
        common.add_var(page, gui, n, v)
    print("done")
