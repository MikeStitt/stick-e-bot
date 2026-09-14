"""A Part Studio's faces as Onshape measures them, written to a file.

    uv run --project . python tools/read_shape.py <did> <wid> <eid> <out.json>

This is the read [`diff_shape.py`](diff_shape.py) diffs, and it is the one that still answers while
`/features` is rate limited, because `bodydetails` is a different endpoint family. Every length is
written in millimeters and every area in square millimeters, so that a difference can be read
without arithmetic. Read only: the route is a GET and nothing on the page is touched.
"""
import json
import sys

from playwright.sync_api import sync_playwright

import onshape_gui as gui
import onshape_session as api

LENGTH = ("origin", "radius", "majorRadius", "minorRadius")


def mm(surface):
    """The same surface in millimeters. A direction is a direction and is left alone."""
    out = {}
    for k, v in surface.items():
        if k in LENGTH:
            out[k] = [c * 1000 for c in v] if isinstance(v, list) else v * 1000
        else:
            out[k] = v
    return out


def faces(detail):
    out = []
    for body in detail.get("bodies", []):
        for f in body.get("faces", []):
            box = f.get("box") or {}
            out.append({
                "body": body.get("id"),
                "id": f.get("id"),
                "surface": mm(f.get("surface", {})),
                "area": f.get("area", 0) * 1e6,
                "box": {side: [c * 1000 for c in box[side]] for side in box
                        if side in ("minCorner", "maxCorner")},
            })
    return out


def main(did, wid, eid, out):
    doc = api.Doc(did, wid, eid)
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, doc)
        page.wait_for_timeout(4000)
        r = api.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")
    if r["status"] != 200:
        raise SystemExit(f"the bodydetails route answered {r['status']}")
    rows = faces(r["body"])
    json.dump(rows, open(out, "w"), indent=1)
    print(f"{len(rows)} faces on {len(r['body'].get('bodies', []))} bodies -> {out}")


if __name__ == "__main__":
    main(*sys.argv[1:5])
