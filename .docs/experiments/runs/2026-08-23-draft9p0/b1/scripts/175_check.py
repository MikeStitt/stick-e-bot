import sys, math, collections
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["bs_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    parts = api.api(page, "GET", f"/api/parts/d/{did}/w/{wid}/e/{eid}")["body"]
    for pt in parts:
        pid, nm = pt["partId"], pt["name"]
        vol = common.volume(page, api, did, wid, eid, pid)
        fs = common.faces(page, api, did, wid, eid, pid)
        kinds = collections.Counter(f["surface"]["type"] for f in fs)
        print(f"\n{nm}  id={pid}  volume={vol}  faces={len(fs)}  {dict(kinds)}")
        for f in fs:
            su = f["surface"]; t = su["type"]
            box = f.get("box", {})
            z = (round(box.get("lowZ", 0)*1000, 3), round(box.get("highZ", 0)*1000, 3))
            if t == "cylinder":
                print(f"   cyl r={round(su['radius']*1000,4):>8}  z={z}  area={round(f['area']*1e6,3)}")
            elif t == "sphere":
                print(f"   sph r={round(su['radius']*1000,4):>8}  z={z}  area={round(f['area']*1e6,3)}")
            elif t == "plane":
                n = su.get("normal", [0,0,0])
                print(f"   pln n=({n[0]:+.2f},{n[1]:+.2f},{n[2]:+.2f})  z={z}  area={round(f['area']*1e6,3)}")
            else:
                print(f"   {t} z={z} area={round(f['area']*1e6,3)}")
