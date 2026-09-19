#!/usr/bin/env python3
"""Phase A — why the eye in `stickbot-draft9p4-check` is 1.5 % oversize.

Each eye's end face is 102.0857 mm² in the check document against 100.531 mm² in
the build document, and 100.531 mm² is pi * `#eyeRx` 8 mm * `#eyeRy` 4 mm exactly.
The area alone does not say what moved: both radii larger by 1.0077 fits it, and
so does both radii offset outward by 0.0411 mm. The sketch says which.

This reads and writes nothing in the check document. The REST grant names
`stickbot-draft9p5`, and every call here is a GET.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/a_eye_read.py
"""

from __future__ import annotations

import json
import math
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

CHECK_DID = "86f40935a709a0748cdbb199"
CHECK_WID = "075a86f5b8f922210c0a7317"
OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
MM = 1000.0

# What each candidate predicts, from the plan's § The head, where the eye
# reproduces 1.5 % oversize.
SCALED = (8.0616, 4.0308)     # both radii larger by a factor of 1.0077
OFFSET = (8.0411, 4.0411)     # both radii larger by 0.0411 mm
DESIGNED = (8.0, 4.0)


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))

        els = S.api(page, "GET",
                    f"/api/documents/d/{CHECK_DID}/w/{CHECK_WID}/elements")["body"]
        print("tabs in stickbot-draft9p4-check:")
        for e in els:
            print(f"  {e['elementType']:<16} {e['name']:<18} {e['id']}")
        head = next((e for e in els if e["name"] == "head"), None)
        if head is None:
            raise RuntimeError("no tab named 'head' in stickbot-draft9p4-check")
        doc = S.Doc(CHECK_DID, CHECK_WID, head["id"])

        sk = S.api(page, "GET",
                   f"/api/partstudios/{doc.path}/sketches?includeGeometry=true")["body"]
        names = [s.get("sketch") for s in sk.get("sketches", [])]
        print("\nsketches:", names)
        eye = next((s for s in sk["sketches"] if s.get("sketch") == "eye profile"), None)
        if eye is None:
            raise RuntimeError(f"no sketch named 'eye profile'; the tab has {names}")

        print("\nentities in `eye profile`:")
        found = []
        for e in eye.get("geomEntities", []) or []:
            if e.get("entityType") == "point":
                continue
            row = {"id": e.get("id"), "type": e.get("entityType")}
            for k, v in e.items():
                if k in ("id", "entityType"):
                    continue
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    row[k] = round(v * MM, 5) if abs(v) < 1 else v
                elif isinstance(v, list) and v and all(
                        isinstance(x, (int, float)) for x in v):
                    row[k] = [round(x * MM, 5) for x in v]
                else:
                    row[k] = v
            found.append(row)
            print("  ", json.dumps(row))

        feats = S.api(page, "GET", f"/api/partstudios/{doc.path}/features")["body"]
        eye_vars = {}
        for f in feats["features"]:
            m = f["message"]
            if m.get("featureType") != "assignVariable":
                continue
            name = expr = None
            for prm in m.get("parameters", []):
                pm = prm["message"]
                if pm.get("parameterId") == "name":
                    name = pm.get("value")
                elif pm.get("parameterId") == "value":
                    expr = pm.get("expression")
            if name and name.lower().startswith("eye"):
                eye_vars[name] = expr
        print("\nthe tab's eye variables:", json.dumps(eye_vars, indent=2))

        OUT.mkdir(parents=True, exist_ok=True)
        (OUT / "eye-read.json").write_text(json.dumps(
            {"document": "stickbot-draft9p4-check", "did": CHECK_DID, "wid": CHECK_WID,
             "element": head["id"], "sketches": names, "eye_profile": found,
             "eye_variables": eye_vars}, indent=2) + "\n")
        print(f"\nwrote {OUT / 'eye-read.json'}")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
