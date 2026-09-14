"""Type one value into robot sizes, wait for the regeneration, then measure over REST.

Usage: c2_drive.py <row-y> <value> <tag>
The row y values are the ones c2_open.py printed: limbCenter 302, fit 506.
"""
import sys, json
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "a1a859f4bfdfe42d372aff90"; WID = "d3a590c94880f445e3c56902"
VS = "8e21e5ac45ee843a1c536e1b"; ASM = "4515305b332af7d4379b81b3"
STUDIOS = [("body", "6f635a750e13ccbf30d05ba2"), ("head", "915098789c7845370c86c914"),
           ("ball and socket", "365f6106c79b2ef1684bf939"), ("foot", "95448bc5d270c9d8370bf3cf"),
           ("hinge", "f2f0dbd682ff7413d3ce2443"), ("u limb", "3f27ca39a14117e276b7c449"),
           ("l limb", "fa98530f59d5f18889fe7c00"), ("gripper", "7ef73a118e1331213bc1554f")]
SCRATCH = ("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-sponge/"
           "c7e95b50-7b3c-4747-a656-ece9f33b51c4/scratchpad/")

row_y, value, tag = int(sys.argv[1]), sys.argv[2], sys.argv[3]

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    if VS not in page.url:
        page.goto(f"https://cad.onshape.com/documents/{DID}/w/{WID}/e/{VS}",
                  wait_until="domcontentloaded")
        page.wait_for_timeout(12000)
    page.mouse.click(730, row_y)
    page.wait_for_timeout(900)
    page.keyboard.press("Meta+a")
    page.wait_for_timeout(300)
    page.keyboard.type(value)
    page.wait_for_timeout(400)
    page.keyboard.press("Enter")
    page.wait_for_timeout(20000)

    r = S.api(page, "GET", f"/api/variables/d/{DID}/w/{WID}/e/{VS}/variables")
    tbl = {v["name"]: v["expression"] for v in r["body"][0]["variables"]}
    print("table now:", json.dumps(tbl))

    out = {"table": tbl, "parts": {}}
    for name, eid in STUDIOS:
        b = S.api(page, "GET",
                  f"/api/parts/d/{DID}/w/{WID}/e/{eid}")["body"]
        for part in b:
            bb = S.api(page, "GET", f"/api/parts/d/{DID}/w/{WID}/e/{eid}"
                       f"/partid/{part['partId']}/boundingboxes")["body"]
            out["parts"][f"{name}/{part['name']}"] = {
                k: round(v * 1000, 4) for k, v in bb.items() if isinstance(v, (int, float))}
    bd = S.api(page, "GET", f"/api/partstudios/d/{DID}/w/{WID}"
               f"/e/365f6106c79b2ef1684bf939/bodydetails")["body"]
    out["socket_faces"] = []
    for body in bd.get("bodies", []):
        for f in body.get("faces", []):
            s = f.get("surface", {})
            if s.get("type") in ("sphere", "cylinder"):
                out["socket_faces"].append(
                    [body.get("id"), s["type"], round(s.get("radius", 0) * 1000, 4),
                     [round(v * 1000, 4) for v in s.get("origin", [])]])
    ab = S.api(page, "GET", f"/api/assemblies/d/{DID}/w/{WID}/e/{ASM}/boundingboxes")["body"]
    out["assembly"] = {k: round(v * 1000, 4) for k, v in ab.items()
                       if isinstance(v, (int, float))}
    open(SCRATCH + f"c2-{tag}.json", "w").write(json.dumps(out, indent=1))
    a = out["assembly"]
    print(f"assembly height {round(a['highZ'] - a['lowZ'], 4)}  "
          f"z {a['lowZ']} … {a['highZ']}")
    for k in ("u limb/u limb", "l limb/l limb", "ball and socket/Socket body"):
        v = out["parts"].get(k)
        if v:
            print(f"  {k:32s} z {v['lowZ']} … {v['highZ']}  "
                  f"({round(v['highZ'] - v['lowZ'], 4)} tall)")
