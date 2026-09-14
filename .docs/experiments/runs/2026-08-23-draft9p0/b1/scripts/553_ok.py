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
    gui.tick(page)
    page.wait_for_timeout(3500)
    print(common.bbox(page, api, s["did"], s["wid"], s["hinge_eid"]))
    r = api.api(page, "GET", f"/api/parts/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}")
    pid = r["body"][0]["partId"]
    print("pid", pid, "vol", common.volume(page, api, s["did"], s["wid"], s["hinge_eid"], pid))
    for f in common.faces(page, api, s["did"], s["wid"], s["hinge_eid"], pid):
        su = f["surface"]
        print(su["type"], [round(x*1000,4) for x in su.get("origin",[])],
              [round(x,4) for x in su.get("normal", su.get("axis",[]))],
              round(su.get("radius",0)*1000,4), round(f["area"]*1e6,3))
