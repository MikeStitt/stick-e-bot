import sys, json
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api

s = common.load()
def strip(o):
    if isinstance(o, dict):
        m = o.get("message", o)
        out = {}
        for k, v in m.items():
            if k in ("nodeId", "importMicroversion", "hasUserCode", "documentId", "elementId",
                     "versionId", "isOutOfDate", "elementMicroversionId"):
                continue
            sv = strip(v)
            if sv not in (None, [], "", {}):
                out[k] = sv
        return out
    if isinstance(o, list):
        return [strip(x) for x in o]
    return o

with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['ps_eid']}/features")
    for f in r["body"]["features"]:
        m = f["message"]
        if m["name"] in ("move neck stud", "neck connector on torso"):
            print("=====", m["name"])
            print(json.dumps(strip(f), indent=1)[:3000])
