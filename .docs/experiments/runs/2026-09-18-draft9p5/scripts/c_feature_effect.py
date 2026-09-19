#!/usr/bin/env python3
"""What every feature in every tab actually made, asked of the model.

    uv run python .../scripts/c_feature_effect.py

The *Model inspected* gate wants each feature seen and given a verdict. This is
the half a picture cannot give: `qCreatedBy` on each feature's id, over
`featurescript`, counting the faces and bodies it is responsible for. A feature
that made nothing and is not a variable, a mate connector or a plane is one to
look at; the rest are accounted for.

Ids come from the tree, so this needs no `/features`.
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S
from stickbot import repo_root

OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}
TABS = ["ball and socket", "hinge", "body", "head", "foot", "u limb", "l limb", "gripper"]
# Features that change the model without being credited with a face of their own:
# a boolean rewrites bodies, a transform moves one, and a variable, a mate
# connector and a plane make no geometry at all. `trim shoulder cut` is the one
# other silent feature, and it is silent because it cuts the shoulder boss flush
# with the torso's top rather than leaving a new face.
MAKES_NOTHING = {"assignVariable", "mateConnector", "cPlane",
                 "booleanBodies", "transform"}
SKIP = {"Default geometry", "Origin", "Top", "Front", "Right"}


def main() -> int:
    report = {}
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        for tab in TABS:
            rows = [r for r in json.loads(
                (OUT / f"{tab.replace(' ', '-')}.tree-ids.json").read_text())
                if r.get("type") and r.get("name") not in SKIP]
            doc = S.Doc("2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062",
                        ELEMENTS[tab])
            ids = ",".join(f'"{r["id"]}"' for r in rows)
            script = """function(context is Context, queries is map)
{
    var s = "";
    for (var f in [%s])
    {
        s = s ~ f ~ " "
              ~ size(evaluateQuery(context, qCreatedBy(makeId(f), EntityType.FACE))) ~ " "
              ~ size(evaluateQuery(context, qCreatedBy(makeId(f), EntityType.BODY))) ~ "\\n";
    }
    return s;
}""" % ids
            counts = {}
            for line in S.eval_fs(page, doc, script).splitlines():
                bits = line.split()
                if len(bits) == 3:
                    counts[bits[0]] = (int(bits[1]), int(bits[2]))
            silent = [r["name"] for r in rows
                      if counts.get(r["id"], (0, 0)) == (0, 0)
                      and r["type"] not in MAKES_NOTHING]
            report[tab] = {"features": [
                {"name": r["name"], "type": r["type"],
                 "faces": counts.get(r["id"], (-1, -1))[0],
                 "bodies": counts.get(r["id"], (-1, -1))[1]} for r in rows],
                "silent": silent}
            print(f"  {tab:<16} {len(rows):>3} rows, "
                  f"{sum(1 for r in rows if r['type'] not in MAKES_NOTHING):>3} that build, "
                  f"{len(silent)} silent" + (f": {silent}" if silent else ""))
        browser.close()
    (OUT / "feature-effect.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"\nwrote {OUT / 'feature-effect.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
