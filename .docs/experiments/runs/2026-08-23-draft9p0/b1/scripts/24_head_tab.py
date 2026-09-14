import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape")
    page.mouse.click(53, 983)
    page.wait_for_timeout(1500)
    b = page.get_by_text("Create Part Studio", exact=True).first.bounding_box()
    page.mouse.click(b["x"] + b["width"] / 2, b["y"] + b["height"] / 2)
    page.wait_for_timeout(4000)
    print("url:", page.url)
    r = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")
    for e in r["body"]:
        print(" ", e["elementType"], e["id"], repr(e["name"]))
    page.screenshot(path="tabstrip4.png", clip={"x": 0, "y": 940, "width": 1000, "height": 60})
