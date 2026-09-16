import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui, onshape_session as api

s = common.load()
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"


def elements(page):
    r = api.api(page, "GET", f"/api/documents/d/{s['did']}/w/{s['wid']}/elements")
    return [(e["name"], e["id"], e["elementType"]) for e in r["body"]]


with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    before = elements(page)
    print("before:", before)
    page.mouse.click(53, 983); page.wait_for_timeout(1800)
    hit = common.menu_item(page, "Create Part Studio")
    print("Create Part Studio at", hit)
    page.mouse.click(*hit); page.wait_for_timeout(5000)
    after = elements(page)
    new = [e for e in after if e not in before]
    print("new:", new)
    common.save(bs_eid=new[0][1] if new else None)
