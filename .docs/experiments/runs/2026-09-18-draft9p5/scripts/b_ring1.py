#!/usr/bin/env python3
"""Ring 1's feature read, for every tab, in one pass.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/b_ring1.py

The plan's Ring 1 asks three things of every feature: that what Onshape stored is
what was sent, that no `featureStates` entry is `ERROR` or `WARNING`, and that
`rollbackIndex` equals the feature count so nothing downstream is being read
short.

**It fetches once and writes to disk.** The `/features` GET has its own daily
quota and spent it on 2026-09-18; every later question is asked of the saved
copy, so re-reading costs nothing and a second opinion never costs a call.

`featureStates` is an array of `{key, value}` wrappers, not a map, and the status
is at `value.message.featureStatus`.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
TABS = [("robot sizes", "3d67f51a630c05c2b5d0b9ea", "variables"),
        ("ball and socket", "1a8322899842a1934e85851d", "partstudios"),
        ("hinge", "db0ef2ae9777492e7b242acf", "partstudios"),
        ("body", "5441067befc71f1e3b91482e", "partstudios"),
        ("head", "303898bd4ba38fc3957b0a21", "partstudios"),
        ("foot", "229aa0900e5a7e7aa4768c6f", "partstudios"),
        ("u limb", "fc89b8128993be73a0c9f092", "partstudios"),
        ("l limb", "be3bd8b485e32946c24ed799", "partstudios"),
        ("gripper", "a3a4fac68ffb7372a7803003", "partstudios"),
        ("stickbot", "c81b630354bd0739d788a42d", "assemblies")]
OUT = Path("/private/tmp/claude-501/-Users-mikestitt-projects-first-2027-stick-e-bot"
           "/c3730b06-661a-42fb-887a-a5f90835fc73/scratchpad/features")


def states(doc):
    """Every feature's status, as a map, from the array of wrappers it arrives in."""
    got = {}
    for s in doc.get("featureStates") or []:
        got[s.get("key")] = (((s.get("value") or {}).get("message") or {})
                             .get("featureStatus", "?"))
    return got


def main() -> int:
    OUT.mkdir(exist_ok=True)
    with api.sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        for name, eid, route in TABS:
            path = OUT / f"{name.replace(' ', '-')}.features.json"
            if path.exists():
                doc = json.loads(path.read_text())
                got = "cached"
            else:
                r = api._raw_api(page, "GET",
                                 f"/api/{route}/d/{DID}/w/{WID}/e/{eid}/features")
                if r["status"] != 200:
                    print(f"  {name:<16} GET -> {r['status']}  {str(r['body'])[:90]}")
                    continue
                doc = r["body"]
                path.write_text(json.dumps(doc))
                got = "fetched"
                api.pace(page, 600)
            feats = doc.get("features") or []
            st = states(doc)
            bad = {k: v for k, v in st.items() if v not in ("OK", "?")}
            roll = doc.get("rollbackIndex")
            parked = roll not in (None, -1, len(feats))
            print(f"  {name:<16} {got:<8} {len(feats):>3} features,"
                  f" {len(st):>3} states, rollbackIndex {roll}"
                  f"{'  BAR PARKED' if parked else ''}"
                  f"{'  ' + repr(bad) if bad else '  all OK'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
