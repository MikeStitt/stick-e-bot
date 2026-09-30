#!/usr/bin/env python3
"""Measure the cup: variables as resolved, the sketch as solved, the part's faces.

Read only. Capacity is computed from the measured faces, not from the variables:
the inside cylinder's radius, the floor's height, the ridge's torus, the lip's top.

    uv run python .docs/experiments/2026-09-30-elephant-cup/verify.py [out.json]
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

HERE = Path(__file__).parent
IDS = json.loads((HERE / "ids.json").read_text())
DOC = S.Doc(IDS["did"], IDS["wid"], IDS["eid"])
MM = 1000.0
FL_OZ_MM3 = 29573.5295625


def main() -> int:
    out = {}
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        S.require_signed_in(page)

        res = S.api(page, "GET", f"/api/variables/d/{DOC.did}/w/{DOC.wid}/e/{DOC.eid}/variables")
        out["variables"] = res["body"]
        print("variables:", json.dumps(res["body"])[:1500])

        res = S.api(page, "GET", f"/api/partstudios/{DOC.path}/sketches?includeGeometry=true")
        out["sketches"] = res["body"]
        for sk in res["body"].get("sketches", []):
            print("sketch", sk.get("sketch"))
            for e in sk.get("geomEntities", []):
                print("  ", e.get("id"), e.get("entityType"),
                      {k: [round(v * MM, 4) for v in e[k]] for k in
                       ("startPoint", "endPoint", "center") if k in e},
                      round(e["radius"] * MM, 4) if "radius" in e else "")

        parts = S.api(page, "GET", f"/api/parts/d/{DOC.did}/w/{DOC.wid}/e/{DOC.eid}")["body"]
        out["parts"] = parts
        print("parts:", [(q["name"], q["partId"]) for q in parts])
        pid = parts[0]["partId"]
        bd = S.api(page, "GET", f"/api/parts/d/{DOC.did}/w/{DOC.wid}/e/{DOC.eid}"
                                f"/partid/{pid}/bodydetails")["body"]
        out["bodydetails"] = bd
        faces = []
        for body in bd.get("bodies", []):
            for f in body.get("faces", []):
                s = f.get("surface", {})
                faces.append({"type": s.get("type"),
                              "radius": round(s["radius"] * MM, 4) if "radius" in s else None,
                              "minorRadius": round(s["minorRadius"] * MM, 4)
                              if "minorRadius" in s else None,
                              "origin": [round(v * MM, 4) for v in s.get("origin", [])],
                              "axis": [round(v, 4) for v in s.get("axis", [])]
                              if "axis" in s else s.get("normal"),
                              "area": round(f.get("area", 0) * MM * MM, 3),
                              "box": f.get("box")})
        for f in faces:
            print("  face", {k: v for k, v in f.items() if k != "box"})

        mp = S.api(page, "GET", f"/api/partstudios/{DOC.path}/massproperties")["body"]
        out["massproperties"] = mp
        vol = next(iter(mp["bodies"].values()))["volume"][0] * MM ** 3
        print(f"part volume: {vol:.3f} mm^3")
        (Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "verify.json").write_text(
            json.dumps(out, indent=1) + "\n")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
