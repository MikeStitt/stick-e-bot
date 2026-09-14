"""Render the two shapes this draft changed, so the report carries a picture of each."""
import sys, base64
sys.path.insert(0, "/Users/mikestitt/projects/first/2027/sponge")
from playwright.sync_api import sync_playwright
from tools import onshape_session as S

DID = "4b2e0d48efd37d3327a90afb"; WID = "a1af16872d25103815f1c32a"
OUT = ("/Users/mikestitt/projects/first/2027/sponge/.docs/experiments/runs/"
       "2026-08-26-draft9p1p1/c/frames/")
TABS = [("6dcfcf8856d4feea7faa440a", "socket"), ("32166c7b3d22572c0e7dd0c3", "gripper")]
VIEWS = ("isometric", "front", "top")

with sync_playwright() as p:
    browser, ctx, page = S.connect(p)
    for eid, tab in TABS:
        for view in VIEWS:
            r = S.api(page, "GET",
                      f"/api/partstudios/d/{DID}/w/{WID}/e/{eid}/shadedviews"
                      f"?viewMatrix={view}&outputHeight=700&outputWidth=700"
                      f"&pixelSize=0&edges=show")
            if not r["ok"]:
                print(tab, view, r["status"], str(r["body"])[:120])
                continue
            name = f"c3-{tab}-{view}"
            open(OUT + name + ".png", "wb").write(base64.b64decode(r["body"]["images"][0]))
            print("wrote", name, flush=True)
