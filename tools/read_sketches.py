"""Every sketch's geometry, in millimeters, for a whole Part Studio.

`/api/partstudios/.../sketches?includeGeometry=true` answers when `/features` is refused,
and it carries where every line, arc and point actually landed, plus the frame of the
plane each sketch was drawn on. That is not a sketch's constraints; it is what the
constraints produced, which is enough to build the same shape and to prove a rebuilt one
matches.

    uv run --project . python tools/read_sketches.py <did> <wid> <eid> <out.json>

Read only.
"""
import json
import sys

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_session as api

MM = 1000.0


def frame(matrix):
    """A sketch's plane, as an origin in millimeters and three unit axes.

    The route hands back a row-major 4x4 that takes a sketch point to the world. Its
    fourth column is the plane's origin and its first two columns are the plane's own x
    and y; the third is the normal, which is the direction an extrude calls Front.
    """
    rows = [matrix[0:4], matrix[4:8], matrix[8:12]]
    return {"origin": [round(r[3] * MM, 4) for r in rows],
            "x": [round(r[0], 6) for r in rows],
            "y": [round(r[1], 6) for r in rows],
            "normal": [round(r[2], 6) for r in rows]}


def entity(e):
    out = {"id": e.get("id"), "type": e.get("entityType")}
    for key in ("point", "center", "startPoint", "endPoint"):
        if e.get(key) is not None:
            out[key] = [round(v * MM, 4) for v in e[key]]
    if e.get("radius") is not None:
        out["radius"] = round(e["radius"] * MM, 4)
    for key in ("startParam", "endParam", "isConstruction"):
        if e.get(key) is not None:
            out[key] = e[key]
    return out


def main(did, wid, eid, out):
    with sync_playwright() as p:
        browser, ctx, page = gui.connect(p)
        got = api.api(page, "GET", f"/api/partstudios/d/{did}/w/{wid}/e/{eid}"
                                   f"/sketches?includeGeometry=true")
        if got["status"] != 200:
            raise SystemExit(f"the sketch route answered {got['status']}")
        record = {"did": did, "wid": wid, "eid": eid, "sketches": {}}
        for s in got["body"].get("sketches", []):
            record["sketches"][s["sketch"]] = {
                "plane": frame(s["transformMatrix"]),
                "entities": [entity(e) for e in s.get("geomEntities", [])
                             if e.get("entityType") != "point"],
            }
        with open(out, "w") as fh:
            json.dump(record, fh, indent=1, sort_keys=True)
            fh.write("\n")
        for name, sk in record["sketches"].items():
            print(f"{name}: {len(sk['entities'])} entities on a plane at "
                  f"{sk['plane']['origin']}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
