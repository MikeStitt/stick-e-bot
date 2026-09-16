import sys
sys.path.insert(0, "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1")
import common
from playwright.sync_api import sync_playwright
import onshape_gui as gui
import onshape_session as api
V = [
 ("limbD", "#torsoH / 4"), ("blade", "10 mm"), ("gap", "0.6 mm"),
 ("slot", "#blade + 2 * #gap"), ("ear", "(#limbD - #slot) / 2"), ("nose", "#limbD / 2"),
 ("blade_out", "32 mm"), ("slot_deep", "#blade_out + 1 mm"),
 ("blade_half", "sqrt(#limbD ^ 2 / 4 - #blade ^ 2 / 4)"),
 ("stub", "4 mm"), ("stub_proud", "1.6 mm"), ("pocket_d", "4.4 mm"),
 ("teeth_ri", "8.8 mm"), ("teeth_r", "10.4 mm"),
 ("bump_r", "(#teeth_ri + #teeth_r) / 2"), ("bump_d", "#teeth_r - #teeth_ri"),
 ("valley_d", "2 mm"), ("valley_deep", "0.9 mm"), ("tooth_proud", "1.2 mm"),
 ("rod", "#limbD"),
]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    for n, v in V:
        common.add_var(page, gui, n, v)
    s = common.load()
    r = api.api(page, "GET", f"/api/partstudios/d/{s['did']}/w/{s['wid']}/e/{s['hinge_eid']}/features")
    st = {row["key"]: row["value"]["message"]["featureStatus"] for row in r["body"]["featureStates"]}
    for f in r["body"]["features"]:
        m = f["message"]
        d = {}
        for prm in m["parameters"]:
            pm = prm["message"]
            d[pm["parameterId"]] = pm.get("expression", pm.get("value"))
        print(f"{st.get(m['featureId']):6} {d.get('name')} = {d.get('value')}")
