import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)

    def rename(tab_x, newname):
        page.mouse.click(tab_x, 983, button="right")
        page.wait_for_timeout(1000)
        loc = page.get_by_text("Rename", exact=True)
        b = None
        for i in range(loc.count()):
            bb = loc.nth(i).bounding_box()
            if bb:
                b = bb
        page.mouse.click(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2)
        page.wait_for_timeout(900)
        page.keyboard.press("Meta+A")
        page.keyboard.type(newname)
        page.keyboard.press("Enter")
        page.wait_for_timeout(1500)

    rename(378, "robot sizes")     # Variable Studio 1
    rename(178, "body")            # Part Studio 1

    r = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")
    for e in r["body"]:
        print(e["elementType"], e["id"], repr(e["name"]))
    page.screenshot(path="tabstrip3.png", clip={"x": 0, "y": 940, "width": 900, "height": 60})
