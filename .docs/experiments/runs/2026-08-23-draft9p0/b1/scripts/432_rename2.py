import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid = s["did"], s["wid"]
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.keyboard.press("Escape"); page.wait_for_timeout(600)
    page.mouse.click(380, 984, button="right")
    page.wait_for_timeout(1500)
    hit = common.menu_item(page, "Rename")
    print("Rename", hit)
    if hit:
        page.mouse.click(*hit); page.wait_for_timeout(1200)
        page.keyboard.press("Meta+A"); page.keyboard.type("foot"); page.keyboard.press("Enter")
        page.wait_for_timeout(3000)
    r = api.api(page, "GET", f"/api/documents/d/{did}/w/{wid}/elements")
    for e in r["body"]:
        print(e["elementType"], e["name"], e["id"])
