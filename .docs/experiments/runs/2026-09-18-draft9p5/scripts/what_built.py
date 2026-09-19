#!/usr/bin/env python3
"""Which features actually made geometry, and which made none.

    uv run python .../scripts/what_built.py "body"

`featureStates` needs `/features`, which is the route Onshape rate limits
hardest. This asks the model instead: `qCreatedBy` on each feature's id, over
`featurescript`, which is a different family. A feature that created nothing is
either a feature that does not create (a variable, a mate connector, a plane) or
a feature that failed, and the first one in the list that should have built is
where to look.
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

# These make no geometry of their own, so creating nothing is not a failure.
MAKES_NOTHING = {"assignVariable", "mateConnector", "cPlane"}


def main(tab: str) -> int:
    stem = tab.replace(" ", "-")
    rec = json.loads((OUT / f"{stem}.ring1.json").read_text())
    rows = [r for r in rec["features"] if r["type"] != "assignVariable"]
    doc = S.Doc(DID, WID, ELEMENTS[tab])
    ids = ",".join(f'"{r["featureId"]}"' for r in rows)
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
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        text = S.eval_fs(page, doc, script)
        browser.close()
    counts = {}
    for line in text.splitlines():
        bits = line.split()
        if len(bits) == 3:
            counts[bits[0]] = (int(bits[1]), int(bits[2]))
    suspect = []
    for r in rows:
        nf, nb = counts.get(r["featureId"], (-1, -1))
        flag = ""
        if nf == 0 and nb == 0 and r["type"] not in MAKES_NOTHING:
            flag = "   <- created nothing"
            suspect.append(r["step"])
        print(f"  {r['i']:>2}  {r['type']:<16} {str(r['step'])[:30]:<30} "
              f"faces={nf:<4} bodies={nb}{flag}")
    if suspect:
        print(f"\nfirst to create nothing: {suspect[0]!r}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
