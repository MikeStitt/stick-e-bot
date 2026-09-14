"""B2 — read every Part Studio back over REST and dump it raw.

Nothing is judged here. This writes b3_raw_120.json and the checking happens offline,
so a rate limit or a dropped session costs one fetch and not the analysis.
"""
import sys, json, time
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright

st = json.load(open(D + "state.json"))
DID, WID = st["did"], st["wid"]

STUDIOS = [
    ("body",            st["ps_eid"]),
    ("head",            st["head_eid"]),
    ("ball and socket", st["bs_eid"]),
    ("foot",            st["foot_eid"]),
    ("hinge",           st["hinge_eid"]),
    ("u limb",          st["ul_eid"]),
    ("l limb",          st["ll_eid"]),
    ("gripper",         st["gr_eid"]),
]

out = {}
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    for name, eid in STUDIOS:
        base = f"/api/parts/d/{DID}/w/{WID}/e/{eid}"
        rec = {"eid": eid}
        r = osx.api(page, "GET", base)
        rec["parts"] = r.get("body")
        r = osx.api(page, "GET",
                    f"/api/partstudios/d/{DID}/w/{WID}/e/{eid}/bodydetails")
        rec["bodydetails"] = r.get("body")
        rec["partboxes"] = {}
        for prt in (rec["parts"] or []):
            pid = prt["partId"]
            rr = osx.api(page, "GET", base + f"/partid/{pid}/boundingboxes")
            rec["partboxes"][pid] = rr.get("body")
        r = osx.api(page, "GET",
                    f"/api/partstudios/d/{DID}/w/{WID}/e/{eid}/boundingboxes")
        rec["studio_bbox"] = r.get("body")
        out[name] = rec
        got = len(rec["parts"] or [])
        print(f"  {name:16s} {got} part(s)", flush=True)
        time.sleep(2)

json.dump(out, open(D + "b3_raw_120.json", "w"), indent=1)
print("wrote b3_raw_120.json")
