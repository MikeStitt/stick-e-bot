#!/usr/bin/env python3
"""Build the cup in `elephant cup`: nine variables, one sketch, one revolve.

Every feature is read back after it is written: the stored parameters against the
ones sent, every `featureStates` entry, and `rollbackIndex` against the feature count.
A feature already in the tree under its name is not written again, so a run that
stopped can be resumed.

The sketch's starting coordinates are seeds for the solver, computed from the agreed
numbers so it lands on the intended branch (the lip below its tangent point, the
ridge bulging inward). The constraints and dimensions decide where everything ends up.

    uv run python .docs/experiments/2026-09-30-elephant-cup/build.py
"""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

from stickbot import onshape_session as S

HERE = Path(__file__).parent
IDS = json.loads((HERE / "ids.json").read_text())
DOC = S.Doc(IDS["did"], IDS["wid"], IDS["eid"])
ORIGIN = "IB"
FRONT = S.FRONT_PLANE
FL_OZ = "29.5735295625 cm^3"  # one US fluid ounce

# The agreed table, in tree order. Each is typed before the sketch, its first reader.
VARIABLES = [
    ("fill", "ANY", f"12 * {FL_OZ}"),
    ("overfill", "ANY", f"1 * {FL_OZ}"),
    ("innerD", "LENGTH", "70 mm"),
    ("wall", "LENGTH", "1.5 mm"),
    ("floor", "LENGTH", "3 mm"),
    ("lipR", "LENGTH", "1.5 mm"),
    ("ridgeR", "LENGTH", "1 mm"),
    ("fillH", "LENGTH", "#fill / (PI * (#innerD / 2) ^ 2)"),
    ("brimH", "LENGTH", "(#fill + #overfill) / (PI * (#innerD / 2) ^ 2)"),
]
SKETCH = "cup profile"
REVOLVE = "revolve cup"
PART = "Cup"

VALUE_PARAM = {"LENGTH": "lengthValue", "ANY": "anyValue"}


def variable(name, vtype, expression):
    return {
        "type": 134, "typeName": "BTMFeature",
        "message": {
            "featureType": "assignVariable", "name": "###name = #value", "suppressed": False,
            "parameters": [
                S.enum_param("mode", "VariableMode", "ASSIGNED"),
                S.enum_param("variableType", "VariableType", vtype),
                {"type": 149, "typeName": "BTMParameterString",
                 "message": {"parameterId": "name", "value": name}},
                S.qty(VALUE_PARAM[vtype], expression),
            ],
        },
    }


# ---- sketch geometry, in millimeters, converted to meters on the way out ----

M = 0.001


def seg(eid, x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    length = math.hypot(dx, dy)
    return {"type": 155, "typeName": "BTMSketchCurveSegment", "message": {
        "entityId": eid, "startPointId": f"{eid}.start", "endPointId": f"{eid}.end",
        "startParam": 0, "endParam": length * M, "isConstruction": False,
        "geometry": {"type": 117, "typeName": "BTCurveGeometryLine", "message": {
            "pntX": x1 * M, "pntY": y1 * M, "dirX": dx / length, "dirY": dy / length}}}}


def arc(eid, cx, cy, r, a0, a1):
    return {"type": 155, "typeName": "BTMSketchCurveSegment", "message": {
        "entityId": eid, "startPointId": f"{eid}.start", "endPointId": f"{eid}.end",
        "centerId": f"{eid}.center", "startParam": a0, "endParam": a1, "isConstruction": False,
        "geometry": {"type": 115, "typeName": "BTCurveGeometryCircle", "message": {
            "radius": r * M, "xCenter": cx * M, "yCenter": cy * M,
            "xDir": 1, "yDir": 0, "clockwise": False}}}}


def s(pid, value):
    return {"type": 149, "typeName": "BTMParameterString",
            "message": {"parameterId": pid, "value": value}}


def con(cid, ctype, *params):
    return {"type": 2, "typeName": "BTMSketchConstraint",
            "message": {"constraintType": ctype, "entityId": cid, "parameters": list(params)}}


def pair(cid, ctype, first, second=None):
    params = [s("localFirst", first)]
    if second is not None:
        params.append(s("localSecond", second))
    return con(cid, ctype, *params)


def to_origin(cid, point):
    return con(cid, "COINCIDENT", s("localFirst", point),
               S.query_list("externalSecond", S.q_geom(ORIGIN)))


def length(cid, eid, expression):
    return con(cid, "LENGTH", s("localFirst", eid),
               S.enum_param("direction", "DimensionDirection", "MINIMUM"),
               S.qty("length", expression),
               S.enum_param("alignment", "DimensionAlignment", "ALIGNED"))


def distance(cid, first, second, expression):
    return con(cid, "DISTANCE", s("localFirst", first), s("localSecond", second),
               S.enum_param("direction", "DimensionDirection", "MINIMUM"),
               S.qty("length", expression))


def radius(cid, eid, expression):
    return con(cid, "RADIUS", s("localFirst", eid), S.qty("length", expression))


def profile():
    """The cup's half section on Front: x is the radius, y is the height."""
    ri, wall, floor, lip_r, ridge_r = 35, 1.5, 3, 1.5, 1
    fill_h = 12 * 29.5735295625e3 / (math.pi * ri ** 2)
    brim_h = 13 * 29.5735295625e3 / (math.pi * ri ** 2)
    ro = ri + wall
    lip_cy = floor + brim_h - lip_r
    ridge_cy = floor + fill_h
    entities = [
        seg("bottom", 0, 0, ro, 0),
        seg("outer", ro, 0, ro, lip_cy - lip_r),
        arc("lip", ri + lip_r, lip_cy, lip_r, -math.pi / 2, math.pi),
        seg("upper", ri, lip_cy, ri, ridge_cy + ridge_r),
        arc("ridge", ri, ridge_cy, ridge_r, math.pi / 2, 3 * math.pi / 2),
        seg("lower", ri, ridge_cy - ridge_r, ri, floor),
        seg("floor", ri, floor, 0, floor),
        seg("axis", 0, floor, 0, 0),
    ]
    constraints = [
        to_origin("c.bottom.origin", "bottom.start"),
        pair("c.bottom.h", "HORIZONTAL", "bottom"),
        pair("c.outer.start", "COINCIDENT", "outer.start", "bottom.end"),
        pair("c.outer.v", "VERTICAL", "outer"),
        pair("c.lip.start", "COINCIDENT", "lip.start", "outer.end"),
        pair("c.lip.end", "COINCIDENT", "lip.end", "upper.start"),
        pair("c.lip.tangent", "TANGENT", "lip", "upper"),
        pair("c.upper.v", "VERTICAL", "upper"),
        pair("c.ridge.start", "COINCIDENT", "ridge.start", "upper.end"),
        pair("c.ridge.end", "COINCIDENT", "ridge.end", "lower.start"),
        pair("c.ridge.on.upper", "COINCIDENT", "ridge.center", "upper"),
        pair("c.ridge.on.lower", "COINCIDENT", "ridge.center", "lower"),
        pair("c.lower.v", "VERTICAL", "lower"),
        pair("c.floor.start", "COINCIDENT", "floor.start", "lower.end"),
        pair("c.floor.h", "HORIZONTAL", "floor"),
        pair("c.axis.start", "COINCIDENT", "axis.start", "floor.end"),
        pair("c.axis.v", "VERTICAL", "axis"),
        pair("c.axis.end", "COINCIDENT", "axis.end", "bottom.start"),
        length("d.innerD", "floor", "#innerD / 2"),
        distance("d.wall", "outer", "lower", "#wall"),
        length("d.floor", "axis", "#floor"),
        radius("d.lipR", "lip", "#lipR"),
        radius("d.ridgeR", "ridge", "#ridgeR"),
        distance("d.fillH", "ridge.center", "floor", "#fillH"),
        distance("d.brimH", "lip.center", "floor", "#brimH - #lipR"),
    ]
    return S.sketch(SKETCH, FRONT, entities, constraints)


AXIS_SCRIPT = """function(context is Context, queries is map)
{
    var q = sketchEntityQuery(makeId("%s"), EntityType.EDGE, "axis");
    return evaluateQuery(context, q)[0].transientId;
}"""


def revolve(sketch_fid, axis_gid):
    return S.revolve(REVOLVE, sketch_fid, axis_gid, "NEW")


# ---- Ring 1 ----


def tree(page):
    return S.api(page, "GET", f"/api/partstudios/{DOC.path}/features")["body"]


def ring1(page, sent):
    """Read the tree back and check the newest feature against what was sent."""
    body = tree(page)
    feats = body["features"]
    states = {e["key"]: e["value"]["message"]["featureStatus"] for e in body["featureStates"]}
    new = feats[-1]["message"]
    want = sent["message"]
    problems = []
    if new["name"] != want["name"] or new["featureType"] != want["featureType"]:
        problems.append(f"last feature is {new['featureType']} {new['name']!r}")
    got = {p["message"]["parameterId"]: p["message"] for p in new["parameters"]}
    for p in want["parameters"]:
        m = p["message"]
        g = got.get(m["parameterId"])
        for key in ("value", "expression"):
            if key in m and (g is None or g.get(key) != m[key]):
                problems.append(f"{m['parameterId']}.{key}: sent {m[key]!r}, "
                                f"stored {None if g is None else g.get(key)!r}")
    if "constraints" in want:
        sent_ids = {c["message"]["entityId"] for c in want["constraints"]}
        got_ids = {c["message"]["entityId"] for c in new.get("constraints", [])}
        if sent_ids - got_ids:
            problems.append(f"constraints missing: {sorted(sent_ids - got_ids)}")
        sent_e = {e["message"]["entityId"] for e in want["entities"]}
        got_e = {e["message"]["entityId"] for e in new.get("entities", [])}
        if sent_e != got_e:
            problems.append(f"entities differ: sent {sorted(sent_e)}, stored {sorted(got_e)}")
    bad = {k: v for k, v in states.items() if v != "OK"}
    if bad:
        problems.append(f"feature states not OK: {bad}")
    if body.get("rollbackIndex") != len(feats):
        problems.append(f"rollbackIndex {body.get('rollbackIndex')} against {len(feats)}")
    print(f"  ring 1: {len(feats)} features, state {states.get(new['featureId'])}, "
          f"rollback {body.get('rollbackIndex')}")
    if problems:
        raise RuntimeError("ring 1 failed:\n  " + "\n  ".join(problems))
    return new


def post(page, feature):
    S.add_feature(page, DOC, feature)
    S.pace(page)
    return ring1(page, feature)


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        name = S.api(page, "GET", f"/api/documents/{DOC.did}")["body"]["name"]
        if name != IDS["document"]:
            raise RuntimeError(f"document reads back as {name!r}")
        print("document:", name)

        have = [f["message"] for f in tree(page)["features"]]
        var_names = {next(p["message"]["value"] for p in f["parameters"]
                          if p["message"]["parameterId"] == "name")
                     for f in have if f["featureType"] == "assignVariable"}
        by_name = {f["name"]: f for f in have}

        for vname, vtype, expression in VARIABLES:
            if vname in var_names:
                print(f"#{vname} already in the tree")
                continue
            print(f"#{vname} = {expression}")
            post(page, variable(vname, vtype, expression))

        if SKETCH in by_name:
            sk = by_name[SKETCH]
            print(f"{SKETCH!r} already in the tree")
        else:
            print(SKETCH)
            sk = post(page, profile())

        if REVOLVE not in by_name:
            axis = S.eval_fs(page, DOC, AXIS_SCRIPT % sk["featureId"])
            print(f"{REVOLVE}, about the sketch's axis line, geometry id {axis}")
            post(page, revolve(sk["featureId"], axis))
        else:
            print(f"{REVOLVE!r} already in the tree")
        browser.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
