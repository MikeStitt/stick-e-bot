"""B3 — the expressions behind the variables, straight off the feature list."""
import sys, json, time
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid = s["did"], s["wid"]
STUDIOS = [("body", s["ps_eid"]), ("head", s["head_eid"]), ("ball and socket", s["bs_eid"]),
           ("foot", s["foot_eid"]), ("hinge", s["hinge_eid"]), ("u limb", s["ul_eid"]),
           ("l limb", s["ll_eid"]), ("gripper", s["gr_eid"])]
out = {}
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    for name, eid in STUDIOS:
        try:
            r = osx.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}/features")
        except Exception as e:
            print(f"{name}: {type(e).__name__} {e}")
            continue
        out[name] = r["body"]
        json.dump(out, open(D + "b3_features_raw.json", "w"))
        rows = []
        for f in r["body"]["features"]:
            m = f["message"]
            d = {}
            for prm in m["parameters"]:
                pm = prm["message"]
                pid = pm.get("parameterId")
                if pid in ("name", "value", "variableType"):
                    d[pid] = pm.get("expression") or pm.get("value")
            if m.get("featureType") == "variable" or "name" in d:
                rows.append((m["name"], d))
        print(f"--- {name}")
        for n, d in rows:
            print(f"   {n:28} {d}")
        time.sleep(4)
json.dump(out, open(D + "b3_exprs.json", "w"), indent=1)
