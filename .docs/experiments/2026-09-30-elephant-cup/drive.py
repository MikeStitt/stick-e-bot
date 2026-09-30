#!/usr/bin/env python3
"""Name the part, then drive `#innerD` to a second value and back.

The acceptance test for design intent: with `#innerD` at 80 mm the fill line and
the brim must drop to hold the same volume, read off the part's faces rather than
the variable table. The value is put back to 70 mm and read off the faces again.

    uv run python .docs/experiments/2026-09-30-elephant-cup/drive.py
"""

from __future__ import annotations

import copy
import json
import math
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

HERE = Path(__file__).parent
IDS = json.loads((HERE / "ids.json").read_text())
DOC = S.Doc(IDS["did"], IDS["wid"], IDS["eid"])
PART = "Cup"
MM = 1000.0
FL_OZ_MM3 = 29573.5295625


def part_id(page):
    return S.api(page, "GET", f"/api/parts/d/{DOC.did}/w/{DOC.wid}/e/{DOC.eid}")["body"]


def name_part(page):
    parts = part_id(page)
    if len(parts) != 1:
        raise RuntimeError(f"expected one part, found {[q['name'] for q in parts]}")
    pid = parts[0]["partId"]
    if parts[0]["name"] == PART:
        print(f"part already named {PART!r}")
        return
    path = f"/api/metadata/d/{DOC.did}/w/{DOC.wid}/e/{DOC.eid}/p/{pid}"
    meta = S.api(page, "GET", path)["body"]
    prop = next(q for q in meta["properties"] if q["name"] == "Name")
    res = S.api(page, "POST", path,
                {"properties": [{"propertyId": prop["propertyId"], "value": PART}]})
    if not res["ok"]:
        raise RuntimeError(f"could not name the part: {json.dumps(res)[:300]}")
    print("part named:", [q["name"] for q in part_id(page)])


def measure(page):
    """Inside radius, ridge center height and lip top, off the part's faces."""
    pid = part_id(page)[0]["partId"]
    bd = S.api(page, "GET", f"/api/parts/d/{DOC.did}/w/{DOC.wid}/e/{DOC.eid}"
                            f"/partid/{pid}/bodydetails")["body"]
    faces = [f["surface"] for b in bd["bodies"] for f in b["faces"]]
    cyl = sorted(round(f["radius"] * MM, 4) for f in faces if f["type"] == "cylinder")
    tori = sorted((round(f["origin"][2] * MM, 4), round(f["minorRadius"] * MM, 4))
                  for f in faces if f["type"] == "torus")
    floor = [round(f["origin"][2] * MM, 4) for f in faces
             if f["type"] == "plane" and f["origin"][2] > 0]
    ridge_z, _ = tori[0]
    lip_z, lip_r = tori[1]
    ri = cyl[0]
    fill = (math.pi * ri ** 2 * (ridge_z - floor[0])) / FL_OZ_MM3
    print(f"  inside r {ri} mm, floor z {floor[0]} mm, ridge center z {ridge_z} mm, "
          f"lip top z {lip_z + lip_r:.4f} mm; cylinder to the ridge center {fill:.4f} fl oz")
    return ri, ridge_z


def variable_feature(page, name):
    for f in S.features(page, DOC):
        m = f["message"]
        if m["featureType"] != "assignVariable":
            continue
        if any(q["message"]["parameterId"] == "name" and q["message"]["value"] == name
               for q in m["parameters"]):
            return f
    raise RuntimeError(f"no variable #{name}")


def set_length(page, name, expression):
    f = copy.deepcopy(variable_feature(page, name))
    for q in f["message"]["parameters"]:
        if q["message"]["parameterId"] in ("lengthValue", "value"):
            q["message"]["expression"] = expression
    S.update_feature(page, DOC, f["message"]["featureId"], f)
    S.pace(page, 1500)
    bad = {k: v for k, v in S.feature_states(page, DOC).items() if v != "OK"}
    print(f"#{name} = {expression}; states not OK: {bad or 'none'}")
    if bad:
        raise RuntimeError("the model did not rebuild clean")


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        S.require_signed_in(page)
        name_part(page)
        print("at 70 mm:")
        measure(page)
        set_length(page, "innerD", "80 mm")
        print("at 80 mm:")
        measure(page)
        set_length(page, "innerD", "70 mm")
        print("back at 70 mm:")
        measure(page)
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
