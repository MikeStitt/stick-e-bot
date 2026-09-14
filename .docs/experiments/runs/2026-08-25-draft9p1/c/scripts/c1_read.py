"""Phase C — read every Part Studio and the assembly back over REST and dump it raw.

Nothing is judged here. The checking happens offline against c1-raw.json, so a rate limit
or a dropped session costs one fetch and not the analysis.
"""
import sys, json, time
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "a1a859f4bfdfe42d372aff90"
WID = "d3a590c94880f445e3c56902"
STUDIOS = [
    ("body",            "6f635a750e13ccbf30d05ba2"),
    ("head",            "915098789c7845370c86c914"),
    ("ball and socket", "365f6106c79b2ef1684bf939"),
    ("foot",            "95448bc5d270c9d8370bf3cf"),
    ("hinge",           "f2f0dbd682ff7413d3ce2443"),
    ("u limb",          "3f27ca39a14117e276b7c449"),
    ("l limb",          "fa98530f59d5f18889fe7c00"),
    ("gripper",         "7ef73a118e1331213bc1554f"),
]
ASM = "4515305b332af7d4379b81b3"
OUT = "/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/2026-08-25-draft9p1/c/c1-raw.json"

out = {"did": DID, "wid": WID, "studios": {}}
with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
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
