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
    before = {e[1] for e in elements(page)}
    page.mouse.click(139, 814); page.wait_for_timeout(6000)
    after = elements(page)
    new = [e for e in after if e[1] not in before]
    print("new:", new)
    print("url:", page.url)
    if new:
        common.save(bs_eid=new[0][1])
        # rename the tab
        page.mouse.click(*gui.viewport(page) and (0, 0)) if False else None
