import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid, eid = s["did"], s["wid"], s["ps_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    print(common.bbox(page, api, did, wid, eid))
    for n, f, st in common.features(page, api, did, wid, eid):
        if st != "OK":
            print("BAD", n, st)
    sph = [f for f in common.faces(page, api, did, wid, eid, "JHD")
           if f.get("surface", {}).get("type") == "sphere"]
    for f in sph:
        print([round(v*1000, 4) for v in f["surface"]["origin"]], round(f["surface"]["radius"]*1000, 3))
    print("volume", common.volume(page, api, did, wid, eid, "JHD"))
