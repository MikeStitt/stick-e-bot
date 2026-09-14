import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
s = common.load(); did, wid = s["did"], s["wid"]
def dump(eid, want):
    r = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m["name"] not in want: continue
        print("==", m["name"])
        for prm in m["parameters"]:
            pm = prm["message"]
            pid = pm.get("parameterId")
            val = pm.get("value", pm.get("queries", pm.get("expression")))
            if pid in ("ownerPart", "hasOwnerPart", "originQuery", "owner"):
                print("   ", pid, json.dumps(val)[:200] if not isinstance(val, (str,int,float,bool)) else val)
            else:
                print("   ", pid, type(val).__name__)
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    dump(s["head_eid"], {"head mate"})
    dump(s["ps_eid"], {"neck connector"})
