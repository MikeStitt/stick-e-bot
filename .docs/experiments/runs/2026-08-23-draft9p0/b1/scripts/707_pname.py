import sys
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
import onshape_screen as screen

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    common.scroll_tree(page, -25)
    gui.rename_row(page, "Part 1", "blade")
    page.wait_for_timeout(1200)
    gui.rename_row(page, "Part 2", "fork")
    page.wait_for_timeout(1200)
    page.mouse.click(140, 880); page.keyboard.press("Escape"); page.wait_for_timeout(800)
    print("selected", screen.selected(gui.probe(page)))
    for pt in api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}")["body"]:
        print(pt["name"], common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], pt["partId"]))
