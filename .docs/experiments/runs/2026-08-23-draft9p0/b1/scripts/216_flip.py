import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
s = common.load()
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.click(258, 305); page.wait_for_timeout(2500)
    page.screenshot(path=D + "hs21.png")
    page.mouse.click(423, 93); page.wait_for_timeout(3500)
    fs = common.faces(page, api, s['did'], s['wid'], s['head_eid'], "JqD")
    zs = []
    for f in fs:
        zs += [round(f["box"]["minCorner"][2]*1000, 4), round(f["box"]["maxCorner"][2]*1000, 4)]
        su = f["surface"]
        if su["type"] == "sphere":
            print("cavity centre", [round(v*1000, 4) for v in su["origin"]], "r", round(su["radius"]*1000, 4))
        if su["type"] == "plane" and abs(f["area"]*1e6 - 254.469) < 0.01:
            print("collar disc z", round(su["origin"][2]*1000, 4))
    print("SPAN", min(zs), max(zs))
    print("volume", common.volume(page, api, s['did'], s['wid'], s['head_eid'], "JqD"))
