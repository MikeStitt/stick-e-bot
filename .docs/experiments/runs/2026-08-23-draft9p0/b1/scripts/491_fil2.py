import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = gui.number_fields(page)
    print("fields", len(els))
    gui.set_field(page, els[0], "#top_round")
    page.wait_for_timeout(1200)
    gui.frame(page, D + "frames/cad.parts.foot.top_round.pick.png")
    gui.tick(page); page.wait_for_timeout(3000)
    gui.rename_row(page, "Fillet 1", "top round"); page.wait_for_timeout(1200)
    gui.clear(page)
    gui.frame(page, D + "frames/cad.parts.foot.top_round.png")
    s = common.load()
    print(common.bbox(page, api, s["did"], s["wid"], s["foot_eid"]))
    print([r for r in gui.tree(page)][-4:])
