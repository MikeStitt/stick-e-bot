import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    els = gui.number_fields(page)
    print("fields", len(els), [e.input_value() for e in els])
    els[0].click(); page.wait_for_timeout(400)
    page.keyboard.press("Meta+A"); page.wait_for_timeout(250)
    page.keyboard.type("#rim_break"); page.wait_for_timeout(1000)
    page.mouse.click(328, 93); page.wait_for_timeout(1800)
    print("now", [e.input_value() for e in gui.number_fields(page)])
    gui.tick(page); page.wait_for_timeout(3500)
    print(common.features(page, api, s["did"], s["wid"], s["hinge_eid"])[-1])
    print("vol", common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], "JHD"))
