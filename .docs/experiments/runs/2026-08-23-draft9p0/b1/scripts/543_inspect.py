import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    did, wid, eid = s["did"], s["wid"], s["hinge_eid"]
    parts = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}")["body"]
    for pt in parts:
        pid = pt["partId"]
        print(pt["name"], pid, common.volume(page, api, did, wid, eid, pid))
        for f in common.faces(page, api, did, wid, eid, pid):
            su = f.get("surface", {})
            t = su.get("type")
            o = [round(v*1000, 4) for v in (su.get("origin") or [0,0,0])]
            n = [round(v, 3) for v in (su.get("normal") or [])]
            print("   ", t, "r", round(su.get("radius", 0)*1000, 4), "area", round(f.get("area",0)*1e6,3), o, n)
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/boundingboxes?includeHidden=false")
    print(r["body"])
