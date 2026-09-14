"""Phase C — read every Part Studio and the assembly back over REST and dump it raw.

Nothing is judged here. The checking happens offline against c1-raw.json, so a rate limit
or a dropped session costs one fetch and not the analysis. This is 9p1's c1_read.py with
draft9p1p1's ids; the feature endpoint is left alone because it was spent when this ran.
"""
import sys, json, time
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "4b2e0d48efd37d3327a90afb"
WID = "a1af16872d25103815f1c32a"
STUDIOS = [
    ("body",            "4e48e81a06c8d40b2a38b871"),
    ("head",            "1562dee65e364ec088dda0ec"),
    ("ball and socket", "6dcfcf8856d4feea7faa440a"),
    ("foot",            "c01ac56602d81451da6a5db5"),
    ("hinge",           "184adaa7b3e7abc7bc4357c7"),
    ("u limb",          "656816292447e8797ff0402d"),
    ("l limb",          "88de5da8c7611f141a1a92a9"),
    ("gripper",         "32166c7b3d22572c0e7dd0c3"),
]
ASM = "cd2278317279029435f010de"
VS = "f30d47abeacf3059ec4a3342"
OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/c1-raw.json")

out = {"did": DID, "wid": WID, "studios": {}}
with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    out["variables"] = S.api(
        page, "GET", f"/api/variables/d/{DID}/w/{WID}/e/{VS}/variables").get("body")
    for name, eid in STUDIOS:
        base = f"/api/parts/d/{DID}/w/{WID}/e/{eid}"
        rec = {"eid": eid}
        rec["parts"] = S.api(page, "GET", base).get("body")
        rec["bodydetails"] = S.api(
            page, "GET", f"/api/partstudios/d/{DID}/w/{WID}/e/{eid}/bodydetails").get("body")
        rec["partboxes"] = {}
        for prt in (rec["parts"] or []):
            pid = prt["partId"]
            rec["partboxes"][pid] = S.api(
                page, "GET", base + f"/partid/{pid}/boundingboxes").get("body")
        rec["studio_bbox"] = S.api(
            page, "GET", f"/api/partstudios/d/{DID}/w/{WID}/e/{eid}/boundingboxes").get("body")
        out["studios"][name] = rec
        print(f"  {name:16s} {len(rec['parts'] or [])} part(s)", flush=True)
        time.sleep(2)
    q = "?includeMateFeatures=true&includeMateConnectors=true&includeNonSolids=false"
    out["assembly"] = S.api(page, "GET", f"/api/assemblies/d/{DID}/w/{WID}/e/{ASM}{q}").get("body")
    out["assembly_bbox"] = S.api(
        page, "GET", f"/api/assemblies/d/{DID}/w/{WID}/e/{ASM}/boundingboxes").get("body")
    print("  assembly", len(out["assembly"]["rootAssembly"]["instances"]), "instances", flush=True)

json.dump(out, open(OUT, "w"), indent=1)
print("wrote", OUT)
