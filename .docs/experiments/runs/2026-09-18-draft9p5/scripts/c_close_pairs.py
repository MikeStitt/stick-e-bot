#!/usr/bin/env python3
"""The closest approaches in a part, by `evDistance`, with the faces named.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_close_pairs.py [tab]

[`c_thinnest_wall.py`](c_thinnest_wall.py) answers every pair whose surfaces face
each other and refuses the rest, because plane arithmetic carried past where a
face ends is not a measurement. This is the instrument for the rest:
`evDistance` searches the faces themselves, so a closest approach at an edge is
found where the analytic method has to decline.

**One call per tab.** The loop runs inside FeatureScript and returns only the
closest few, because `featurescript` has its own daily quota and this run has
already spent it once.

It reports each pair's two faces with their surface types, so a number can be
recognised as a wall, a slit or a near-tangency rather than being left as a
figure nobody can place.
"""

from __future__ import annotations

import sys

from stickbot import onshape_session as api

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
TABS = {"gripper": "a3a4fac68ffb7372a7803003",
        "head": "303898bd4ba38fc3957b0a21",
        "foot": "229aa0900e5a7e7aa4768c6f",
        "body": "5441067befc71f1e3b91482e",
        "ball and socket": "1a8322899842a1934e85851d"}

SCRIPT = """function(context is Context, queries is map)
{
    // The solid's own faces, not the Part Studio's. `qEverything(FACE)` also
    // returns the faces of every construction plane and surface body, and a
    // distance from one of those is not a wall in the part.
    var solids = evaluateQuery(context,
        qBodyType(qEverything(EntityType.BODY), BodyType.SOLID));
    var faces = [];
    for (var s in solids)
    {
        faces = concatenateArrays([faces,
            evaluateQuery(context, qOwnedByBody(s, EntityType.FACE))]);
    }
    var out = [];
    for (var i = 0; i < size(faces); i += 1)
    {
        for (var j = i + 1; j < size(faces); j += 1)
        {
            var d = try silent(evDistance(context, {
                "side0" : faces[i], "side1" : faces[j] }));
            if (d == undefined) { continue; }
            var mm = d.distance / millimeter;
            if (mm < 1e-7) { continue; }
            out = append(out, [mm, i, j]);
        }
    }
    out = sort(out, function(a, b) { return a[0] - b[0]; });
    var best = [];
    for (var k = 0; k < min(8, size(out)); k += 1)
    {
        var a = faces[out[k][1]];
        var b = faces[out[k][2]];
        best = append(best,
            toString(round(out[k][0] * 100000) / 100000) ~ "  " ~
            toString(out[k][1]) ~ ":" ~ toString(evSurfaceDefinition(context,
                { "face" : a }).surfaceType) ~ "  to  " ~
            toString(out[k][2]) ~ ":" ~ toString(evSurfaceDefinition(context,
                { "face" : b }).surfaceType));
    }
    return best;
}"""


def main(only: str | None = None) -> int:
    with api.sync_playwright() as pw:
        browser, ctx, page = api.connect(pw)
        for tab, eid in TABS.items():
            if only and tab != only:
                continue
            r = api._raw_api(page, "POST",
                             f"/api/partstudios/d/{DID}/w/{WID}/e/{eid}/featurescript",
                             {"script": SCRIPT})
            # A FeatureScript that will not parse still answers 200, with the
            # complaint in `notices`. Reading only the status makes a broken
            # script look like a part with nothing close in it.
            bad = [n["message"]["message"] for n in (r["body"].get("notices") or [])
                   if n.get("message", {}).get("level") == "ERROR"]
            if r["status"] != 200 or bad:
                print(f"  {tab:<16} -> {r['status']}  {bad or str(r['body'])[:140]}")
                continue
            msg = ((r["body"].get("result") or {}).get("message") or {})
            rows = [v["message"]["value"] for v in (msg.get("value") or [])]
            print(f"\n  {tab}: the closest approaches, in millimetres")
            for row in rows:
                print(f"      {row}")
            api.pace(page, 800)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
