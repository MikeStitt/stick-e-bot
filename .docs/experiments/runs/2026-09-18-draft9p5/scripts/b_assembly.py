#!/usr/bin/env python3
"""Phase B tab 10 — the `stickbot` assembly's thirteen mates.

    uv run python .../scripts/b_assembly.py

The instances go in first, in draft9p1p1's own order, so the `<n>` its mates
name line up index for index. Each mate is then replayed with two things
remapped: the `path`, which is the instance, and the `featureId`, which is the
mate connector inside that instance's Part Studio. The parent's connector ids
are matched to names through its own per-tab records, and the names to this
document's ids through what the tree reports.

The assemblies route is a different endpoint family from `partstudios/features`,
so this works with that one refused.
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

ROOT = repo_root()
DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}

# Which of the parent's records holds each instance's connectors.
SOURCE = {"torso": "body", "head": "head", "u limb": "u-limb", "l limb": "l-limb",
          "Gripper": "gripper", "Foot": "foot"}
# The plan's rename table, for the connectors the assembly picks: the parent
# calls them `neck connector` and the rest, and this draft drops the word.
RENAMED = {"neck connector": "neck", "left shoulder connector": "left shoulder",
           "r shoulder connector": "right shoulder", "l hip connector": "left hip",
           "r hip connector": "right hip"}

# Where this document's connector of that name lives.
TAB = {"torso": "body", "head": "head", "u limb": "u limb", "l limb": "l limb",
       "Gripper": "gripper", "Foot": "foot"}


def parent_connectors():
    """The parent's connector featureId -> its name, per source record."""
    out = {}
    for stem in set(SOURCE.values()):
        for f in json.loads((D3 / f"{stem}.features.json").read_text())["features"]:
            m = f["message"]
            if m.get("featureType") == "mateConnector":
                out[m["featureId"]] = (stem, m.get("name"))
    return out


def mine_connectors():
    """This document's connector name -> featureId, per tab."""
    out = {}
    for tab in set(TAB.values()):
        rows = json.loads((OUT / f"{tab.replace(' ', '-')}.tree-ids.json").read_text())
        out[tab] = {r["name"]: r["id"] for r in rows if r.get("type") == "mateConnector"}
    return out


def main(only=None) -> int:
    """`only` rebuilds just the mates named, deleting them first."""
    parent = json.loads((D3 / "assembly.json").read_text())
    feats = json.loads((D3 / "assembly.features.json").read_text())["features"]
    p_conn, m_conn = parent_connectors(), mine_connectors()
    mine_inst = json.loads((OUT / "assembly.instances.json").read_text())
    if len(mine_inst) != len(parent["instances"]):
        raise RuntimeError(f"{len(mine_inst)} instances here, "
                           f"{len(parent['instances'])} in the parent")
    path_of = {p["id"]: m["id"] for p, m in zip(parent["instances"], mine_inst)}
    kind_of = {p["id"]: p["name"].rsplit(" <", 1)[0] for p in parent["instances"]}

    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        if only:
            have = S.api(page, "GET", f"/api/assemblies/d/{DID}/w/{WID}"
                                      f"/e/{ELEMENTS['stickbot']}/features")["body"]
            for g in have.get("features", []):
                if g["message"].get("name") in only:
                    S.api(page, "DELETE", f"/api/assemblies/d/{DID}/w/{WID}"
                          f"/e/{ELEMENTS['stickbot']}/features/featureid/"
                          f"{g['message']['featureId']}")
                    print(f"  deleted {g['message'].get('name')}")
                    S.pace(page)
        for f in feats:
            if only and f["message"].get("name") not in only:
                continue
            m = json.loads(json.dumps(f["message"]))
            m.pop("featureId", None)
            for prm in m["parameters"]:
                pm = prm["message"]
                if pm.get("parameterId") != "mateConnectorsQuery":
                    continue
                for q in pm["queries"]:
                    qm = q["message"]
                    old_path = qm["path"][0]
                    qm["path"] = [path_of[old_path]]
                    stem, name = p_conn[qm["featureId"]]
                    name = RENAMED.get(name, name)
                    tab = TAB[kind_of[old_path]]
                    if name not in m_conn[tab]:
                        raise RuntimeError(f"`{tab}` has no connector called {name!r}")
                    qm["featureId"] = m_conn[tab][name]
            res = S.api(page, "POST",
                        f"/api/assemblies/d/{DID}/w/{WID}/e/{ELEMENTS['stickbot']}/features",
                        {"feature": {"type": f["type"], "typeName": f["typeName"],
                                     "message": m}})
            if not res["ok"]:
                raise RuntimeError(f"{m.get('name')!r} refused: {res['status']} "
                                   f"{json.dumps(res.get('body'))[:240]}")
            print(f"  mated {m.get('name')}")
            S.pace(page)
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:] or None))
