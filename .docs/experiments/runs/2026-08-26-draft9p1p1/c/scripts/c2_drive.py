"""Type one value into robot sizes, wait for the regeneration, then measure over REST.

Usage: c2_drive.py <row-y> <value> <tag>
Rows at this window size: collar 472, fit 506.
"""
import sys, json
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "4b2e0d48efd37d3327a90afb"; WID = "a1af16872d25103815f1c32a"
VS = "f30d47abeacf3059ec4a3342"; ASM = "cd2278317279029435f010de"
SOCKET = "6dcfcf8856d4feea7faa440a"
STUDIOS = [("body", "4e48e81a06c8d40b2a38b871"), ("head", "1562dee65e364ec088dda0ec"),
           ("ball and socket", SOCKET), ("foot", "c01ac56602d81451da6a5db5"),
           ("hinge", "184adaa7b3e7abc7bc4357c7"), ("u limb", "656816292447e8797ff0402d"),
           ("l limb", "88de5da8c7611f141a1a92a9"), ("gripper", "32166c7b3d22572c0e7dd0c3")]
OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/")

row_y, value, tag = int(sys.argv[1]), sys.argv[2], sys.argv[3]

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    if VS not in page.url:
        page.goto(f"https://cad.onshape.com/documents/{DID}/w/{WID}/e/{VS}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(15000)
    page.mouse.click(730, row_y)
    page.wait_for_timeout(900)
    page.keyboard.press("Meta+a")
    page.wait_for_timeout(300)
    page.keyboard.type(value)
    page.wait_for_timeout(400)
    page.keyboard.press("Enter")
    page.wait_for_timeout(25000)

    r = S.api(page, "GET", f"/api/variables/d/{DID}/w/{WID}/e/{VS}/variables")
    tbl = {v["name"]: v["expression"] for v in r["body"][0]["variables"]}
    print("table now:", json.dumps(tbl))

    out = {"tag": tag, "table": tbl, "parts": {}}
    for name, eid in STUDIOS:
        for part in S.api(page, "GET", f"/api/parts/d/{DID}/w/{WID}/e/{eid}")["body"]:
            bb = S.api(page, "GET", f"/api/parts/d/{DID}/w/{WID}/e/{eid}"
                       f"/partid/{part['partId']}/boundingboxes")["body"]
            out["parts"][f"{name}/{part['name']}"] = {
                k: round(v * 1000, 4) for k, v in bb.items() if isinstance(v, (int, float))}
    bd = S.api(page, "GET",
               f"/api/partstudios/d/{DID}/w/{WID}/e/{SOCKET}/bodydetails")["body"]
    out["socket_faces"] = []
    for body in bd.get("bodies", []):
        for f in body.get("faces", []):
            s = f.get("surface", {})
            if s.get("type") in ("sphere", "cylinder"):
                out["socket_faces"].append(
                    [s["type"], round(s.get("radius", 0) * 1000, 4),
                     [round(v * 1000, 4) for v in s.get("origin", [])]])
            elif s.get("type") == "plane" and abs(s["normal"][2]) > 0.99:
                out["socket_faces"].append(
                    ["planeZ", round(s["origin"][2] * 1000, 4),
                     round(f.get("area", 0) * 1e6, 4)])
    ab = S.api(page, "GET",
               f"/api/assemblies/d/{DID}/w/{WID}/e/{ASM}/boundingboxes")["body"]
    out["assembly"] = {k: round(v * 1000, 4) for k, v in ab.items()
                       if isinstance(v, (int, float))}
    asm = S.api(page, "GET", f"/api/assemblies/d/{DID}/w/{WID}/e/{ASM}"
                "?includeMateFeatures=true&includeNonSolids=false")["body"]
    root = asm["rootAssembly"]
    names = {i["id"]: i["name"] for i in root["instances"]}
    out["stations"] = sorted(
        [[names.get(o["path"][-1], o["path"][-1])] +
         [round(o["transform"][k] * 1000, 4) for k in (3, 7, 11)]
         for o in root["occurrences"]], key=lambda r: -r[3])
    open(OUT + f"c2-{tag}.json", "w").write(json.dumps(out, indent=1))

    a = out["assembly"]
    print(f"assembly height {round(a['highZ'] - a['lowZ'], 4)}  "
          f"z {a['lowZ']} … {a['highZ']}")
    for k in sorted(out["parts"]):
        v = out["parts"][k]
        print(f"  {k:30s} z {v['lowZ']:9.4f} … {v['highZ']:9.4f}  "
              f"({round(v['highZ'] - v['lowZ'], 4):8.4f} tall)")
