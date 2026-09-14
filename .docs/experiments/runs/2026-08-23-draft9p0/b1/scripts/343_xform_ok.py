import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

s = common.load()
def stud(page):
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}")
    pid = [q["partId"] for q in r["body"] if q["name"] == "Ball stud"][0]
    for f in common.faces(page, api, s["did"], s["wid"], s["ps_eid"], pid):
        b = f["box"]
        print(" ", f["surface"]["type"],
              [round(v*1000, 3) for v in b["minCorner"]],
              [round(v*1000, 3) for v in b["maxCorner"]])

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    gui.tick(page)
    page.wait_for_timeout(3500)
    gui.rename_row(page, "Transform 1", "move neck stud")
    page.wait_for_timeout(2000)
    stud(page)
