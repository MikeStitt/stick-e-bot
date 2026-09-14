"""B3 — what the assembly holds now the variable has been driven and put back."""
import sys, json
D = "/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/b1/"
sys.path.insert(0, D)
import common, onshape_gui as gui, onshape_session as osx
from playwright.sync_api import sync_playwright
s = common.load(); did, wid, asm = s["did"], s["wid"], s["asm_eid"]
with sync_playwright() as p:
    browser, ctx, _ = gui.connect(p)
    page = common.mypage(ctx)
    page.mouse.up()
    r = osx.api(page, "GET",
        f"/api/assemblies/d/{did}/w/{wid}/e/{asm}?includeMateFeatures=true"
        "&includeMateConnectors=true")
    b = r["body"]["rootAssembly"]
    print("instances:", len(b["instances"]))
    for i in b["instances"]:
        print("   ", i["type"], i["name"])
    feats = b.get("features", [])
    print("features:", len(feats))
    for f in feats:
        m = f["featureData"]
        print("   ", f["featureType"], m.get("mateType", ""), m.get("name", ""))
