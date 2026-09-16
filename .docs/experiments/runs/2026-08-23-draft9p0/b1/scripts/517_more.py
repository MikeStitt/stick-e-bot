import sys, math, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    s = common.load()
    did, wid, eid = s["did"], s["wid"], s["foot_eid"]
    r = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/JHD/bodydetails")
    body = common._one(r["body"]["bodies"])
    print("keys", list(body.keys()))
    # planar faces whose normal lies in XY (slit walls, side walls)
    n_xy = [f for f in body["faces"] if f.get("surface", {}).get("type") == "plane"
            and abs((f["surface"].get("normal") or [0,0,1])[2]) < 0.01]
    print("planar faces with in-plane normal:", len(n_xy))
    for f in n_xy:
        su = f["surface"]
        o = [round(v*1000, 3) for v in su["origin"]]
        n = [round(v, 3) for v in su["normal"]]
        print("   area", round(f.get("area", 0)*1e6, 3), "origin", o, "normal", n)
    mp = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}/partid/JHD/massproperties")
    b = common._one(mp["body"]["bodies"])
    print("centroid raw", b["centroid"])
