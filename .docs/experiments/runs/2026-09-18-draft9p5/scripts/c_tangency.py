#!/usr/bin/env python3
"""Where two faces meet with a crease, and where they meet tangent.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/c_tangency.py [tab]

`head.md` and `foot.md` each ask that a profile be tangent throughout, with no
crease where an arc meets a line. A crease is an edge whose two faces have
different normals along it; a tangent meeting is an edge where they agree. The
face dump carries both halves: `loops` give each face's edges, so an edge names
the two faces that share it, and each surface's own description gives a normal at
a point on that edge.

It reports the angle at every edge, and then walks the profile itself.

**`src/stickbot/measure_tangency.py` already does the every-edge half**, off the
tessellation, and says in its own docstring that facet normals lag the surface by
about 1.15 deg so the exact figure should be read off `bodydetails`. This reads
`bodydetails`, so its angles are exact; and it adds the profile walk, which is
what the briefs are asking for. The every-edge answer on its own reports the eyes
and the socket as creases, which they are and which no brief objects to.
"""

from __future__ import annotations

import math
import sys
from collections import defaultdict

from stickbot import onshape_session as S

DID, WID = "2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062"
TABS = {"head": "303898bd4ba38fc3957b0a21", "foot": "229aa0900e5a7e7aa4768c6f",
        "ball and socket": "1a8322899842a1934e85851d",
        "gripper": "a3a4fac68ffb7372a7803003", "body": "5441067befc71f1e3b91482e"}
MM = 1000.0
TANGENT = 1.0      # degrees; nearer than this and the two faces run into each other smoothly


def vec(v, scale=MM):
    if v is None:
        return None
    if isinstance(v, dict):
        return [v.get(k, 0.0) * scale for k in "xyz"]
    return [float(v[i]) * scale for i in range(3)]


def sub(a, b):
    return [a[i] - b[i] for i in range(3)]


def dot(a, b):
    return sum(a[i] * b[i] for i in range(3))


def norm(a):
    n = math.sqrt(dot(a, a))
    return [v / n for v in a] if n > 1e-12 else None


def normal_at(surf, p):
    """The surface's outward normal at a point on it, or None where it is not worked out."""
    t = surf["type"]
    if t == "PLANE":
        return norm(surf["normal"])
    if t == "SPHERE":
        return norm(sub(p, surf["origin"]))
    if t == "CYLINDER":
        d = sub(p, surf["origin"])
        along = dot(d, surf["axis"])
        return norm([d[i] - along * surf["axis"][i] for i in range(3)])
    if t == "CONE":
        d = sub(p, surf["origin"])
        along = dot(d, surf["axis"])
        radial = norm([d[i] - along * surf["axis"][i] for i in range(3)])
        if radial is None:
            return None
        half = surf.get("halfAngle") or 0.0
        return norm([radial[i] * math.cos(half) - surf["axis"][i] * math.sin(half)
                     for i in range(3)])
    return None


def read(page, eid):
    base = f"/api/v10/parts/d/{DID}/w/{WID}/e/{eid}"
    out = []
    for p in S._raw_api(page, "GET", base)["body"]:
        bd = S._raw_api(page, "GET", f"{base}/partid/{p['partId']}/bodydetails")["body"]
        b = bd["bodies"][0]
        faces, by_edge = {}, defaultdict(list)
        for f in b["faces"]:
            s = f.get("surface") or {}
            faces[f["id"]] = {
                "id": f["id"], "type": (s.get("type") or "").upper(),
                "origin": vec(s.get("origin")), "axis": vec(s.get("axis"), 1.0),
                "normal": vec(s.get("normal"), 1.0),
                "halfAngle": s.get("halfAngle"),
                "area": f["area"] * MM * MM,
                "outer": [(ce["edgeId"], ce.get("orientation", True))
                          for loop in f.get("loops", []) if loop.get("isOuter")
                          for ce in loop.get("coedges", [])],
            }
            for loop in f.get("loops", []):
                for ce in loop.get("coedges", []):
                    by_edge[ce["edgeId"]].append(f["id"])
        edges = {}
        for e in b.get("edges", []):
            g = e.get("geometry") or {}
            edges[e["id"]] = {"mid": vec(g.get("midPoint")),
                              "start": vec(g.get("startPoint")),
                              "end": vec(g.get("endPoint")),
                              "sv": vec(g.get("startVector"), 1.0),
                              "ev": vec(g.get("endVector"), 1.0),
                              "arc": "Arc" in (g.get("btType") or "")}
        out.append({"name": p.get("name"), "faces": faces, "edges": edges, "by_edge": by_edge})
    return out


def angles(part):
    """One (degrees, edge id, the two face ids) per edge that two faces share."""
    got = []
    for eid, fids in part["by_edge"].items():
        seen = [f for i, f in enumerate(fids) if f not in fids[:i]]
        if len(seen) != 2 or eid not in part["edges"]:
            continue
        p = part["edges"][eid]["mid"]
        if p is None:
            continue
        na = normal_at(part["faces"][seen[0]], p)
        nb = normal_at(part["faces"][seen[1]], p)
        if na is None or nb is None:
            continue
        got.append((math.degrees(math.acos(max(-1.0, min(1.0, dot(na, nb))))), eid,
                    seen[0], seen[1], part["edges"][eid]["arc"]))
    return sorted(got)


# Which way each part's outline was extruded. A profile's joins are the straight
# edges that run along that axis, so they are what the briefs' "tangent throughout"
# is about; every other crease is a face the profile never had, such as an eye
# standing proud or a socket bored in.
EXTRUDED_ALONG = {"head": 1, "foot": 2, "gripper": 0, "body": 1}


def end_cap(part, axis):
    """The extrude's end face: the largest plane whose normal runs along the extrude."""
    caps = [f for f in part["faces"].values()
            if f["type"] == "PLANE" and f["normal"]
            and abs(abs(f["normal"][axis]) - 1) < 1e-6]
    return max(caps, key=lambda f: f["area"]) if caps else None


def profile_joins(part, axis):
    """The angle at each corner of the profile, walking the end cap's outer loop.

    The profile is the end cap's own boundary, so a crease in it is a corner where
    one curve leaves in a different direction from the one arriving.
    """
    cap = end_cap(part, axis)
    if cap is None or len(cap["outer"]) < 2:
        return [], cap
    ring = cap["outer"]
    got = []
    for i, (eid, fwd) in enumerate(ring):
        nid, nfwd = ring[(i + 1) % len(ring)]
        a, b = part["edges"].get(eid), part["edges"].get(nid)
        if not a or not b or a["sv"] is None or b["sv"] is None:
            continue
        leaving = norm(a["ev"] if fwd else [-v for v in a["sv"]])
        arriving = norm(b["sv"] if nfwd else [-v for v in b["ev"]])
        if leaving is None or arriving is None:
            continue
        got.append((math.degrees(math.acos(max(-1.0, min(1.0, dot(leaving, arriving))))),
                    eid, "arc" if a["arc"] else "line", "arc" if b["arc"] else "line"))
    return got, cap


def main(only: str | None = None) -> int:
    with S.sync_playwright() as pw:
        browser, ctx, page = S.connect(pw)
        for tab, eid in TABS.items():
            if only and tab != only:
                continue
            print(f"\n{tab}")
            for part in read(page, eid):
                got = angles(part)
                tangent = [g for g in got if g[0] < TANGENT]
                print(f"  {part['name']}: {len(got)} shared edges measured,"
                      f" {len(tangent)} tangent under {TANGENT:g} deg")
                for a, eid_, fa, fb, arc in tangent:
                    ta, tb = part["faces"][fa]["type"], part["faces"][fb]["type"]
                    print(f"      tangent {a:7.4f} deg   {eid_:<6} {ta} to {tb}"
                          f"{'   on an arc' if arc else ''}")
                creases = [g for g in got if g[0] >= TANGENT]
                kinds = defaultdict(list)
                for a, _eid, fa, fb, _arc in creases:
                    pair = tuple(sorted((part["faces"][fa]["type"],
                                         part["faces"][fb]["type"])))
                    kinds[pair].append(a)
                for pair, aa in sorted(kinds.items()):
                    print(f"      crease  {pair[0]} to {pair[1]:<9} "
                          f" {min(aa):7.3f} to {max(aa):7.3f} deg")
                axis = EXTRUDED_ALONG.get(tab)
                if axis is None:
                    continue
                joins, cap = profile_joins(part, axis)
                if cap is None:
                    continue
                print(f"      the profile is the outer loop of {cap['id']},"
                      f" the end cap normal to {'xyz'[axis]}: {len(joins)} corners")
                for a, eid_, ta, tb in joins:
                    kind = "tangent" if a < TANGENT else "CREASE "
                    print(f"        {kind} {a:8.4f} deg   after {eid_:<6} {ta} then {tb}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
