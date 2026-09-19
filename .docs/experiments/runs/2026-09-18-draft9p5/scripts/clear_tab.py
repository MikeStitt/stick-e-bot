#!/usr/bin/env python3
"""Delete every feature in a tab, newest first.

    uv run python .../scripts/clear_tab.py "body"

Ids come from `results/<tab>.tree-ids.json`, which `tree_ids.py` reads off the
GUI, so a tab can be cleared while `/features` refuses to list it.
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}


def main(tab: str) -> int:
    stem = tab.replace(" ", "-")
    rows = [r for r in json.loads((OUT / f"{stem}.tree-ids.json").read_text())
            if r.get("type")]
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        refused = 0
        for r in reversed(rows):
            res = S._raw_api(page, "DELETE",
                             f"/api/partstudios/{doc.path}/features/featureid/{r['id']}")
            if res.get("status") not in (200, 204):
                refused += 1
                print(f"  {res.get('status')} refused {r['name']}")
            S.pace(page, 120)
        bd = S.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")["body"]
        v = S.api(page, "GET",
                  f"/api/variables/d/{DID}/w/{WID}/e/{doc.eid}/variables")["body"]
        locals_ = [x["name"] for t in (v or []) for x in (t.get("variables") or [])]
        print(f"deleted {len(rows) - refused} of {len(rows)}; "
              f"{len(bd['bodies'])} bodies and {len(locals_)} local variables left")
        browser.close()
    return 1 if refused else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
