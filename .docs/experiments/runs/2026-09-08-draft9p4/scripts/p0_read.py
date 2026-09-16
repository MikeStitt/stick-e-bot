"""draft9p1p6's five tabs, read at the version Phase F published, into `reference/`.

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/p0_read.py

The version is read rather than the workspace because the two are not the same: on
2026-09-09 the workspace stood at microversion `1009393f43c6384ece39b921` and the version
at `dd821b5b9c8498eb568aee67`. Every call is a GET against a `/v/` path, paced, so the
feature route is not driven into a block.

Read only. The page is opened to give the fetches a same-origin host and nothing on it is
touched.
"""
import json
import sys
import time


from playwright.sync_api import sync_playwright

from stickbot import repo_root
from stickbot import onshape_gui as gui
from stickbot import onshape_session as api
import read_shape
import read_sketches

DID = "500752af84dc92deea53f9e4"
WID = "f30bf96cfeece59f61e0e7b2"
VID = "80c22eb7b8b0342ac03f8a6d"
OUT = str(repo_root()) + "/.docs/experiments/runs/2026-09-08-draft9p4/reference"
PACE = 3.0

TABS = [
    ("robot-sizes", "5e9a0328a109ff92f5f6e9aa", "variables"),
    ("ball-and-socket", "88ea6b759912b789d6de4647", "part"),
    ("hinge", "62fca6aa5a67b51adcb2318c", "part"),
    ("u-limb", "f3f8362fd5e9f31ee2fa5eb2", "part"),
    ("l-limb", "261b7ee66567bab16d145c83", "part"),
]


def get(page, path):
    time.sleep(PACE)
    r = api.api(page, "GET", path)
    if r["status"] != 200:
        raise SystemExit(f"{path} answered {r['status']}")
    return r["body"]


def write(name, body):
    path = f"{OUT}/{name}"
    with open(path, "w") as fh:
        json.dump(body, fh, indent=1, sort_keys=True)
        fh.write("\n")
    return path


def main():
    with sync_playwright() as pw:
        browser, ctx, page = gui.connect(pw)
        gui.open_doc(page, api.Doc(DID, WID, TABS[1][1]))
        page.wait_for_timeout(4000)

        for tab, eid, kind in TABS:
            base = f"d/{DID}/v/{VID}/e/{eid}"

            feats = get(page, f"/api/partstudios/{base}/features")
            write(f"{tab}.features.json", feats)
            print(f"{tab}: {len(feats['features'])} features")

            if kind == "variables":
                rows = get(page, f"/api/variables/{base}/variables")
                write("variables.json", rows)
                n = sum(len(t.get("variables", [])) for t in rows) if isinstance(rows, list) else 0
                print(f"{tab}: {n} variable rows")
                continue

            faces = read_shape.faces(get(page, f"/api/partstudios/{base}/bodydetails"))
            write(f"{tab}.faces.json", faces)
            print(f"{tab}: {len(faces)} faces")

            got = get(page, f"/api/partstudios/{base}/sketches?includeGeometry=true")
            record = {"did": DID, "vid": VID, "eid": eid, "sketches": {}}
            for s in got.get("sketches", []):
                record["sketches"][s["sketch"]] = {
                    "plane": read_sketches.frame(s["transformMatrix"]),
                    "entities": [read_sketches.entity(e) for e in s.get("geomEntities", [])
                                 if e.get("entityType") != "point"],
                }
            write(f"{tab}.geometry.json", record)
            print(f"{tab}: {len(record['sketches'])} sketches")


if __name__ == "__main__":
    main()
