"""Every number draft9p1p6 types rather than derives, per tab, from the P0 record.

    uv run --project . python .docs/experiments/runs/2026-09-08-draft9p4/scripts/typed_numbers.py

A feature stores a value for every parameter it could have, whether or not that parameter
is switched on. An extrude that is neither drafted nor offset still carries `draftAngle
3 deg` and `offsetDistance 25 mm`; a transform that moves a part to a mate connector still
carries `distance 25 mm` and `angle 30 deg` from the translate and rotate options it is not
using. Reporting those buries the handful of numbers a builder actually typed, so each
feature type is read through the switch that turns its parameters on.

A sketch dimension's value is its `length` or `angle` parameter. `labelRatio` and
`labelAngle` place the label on the screen and are not the dimension.

A zero is not a typed size, so zeros are dropped.
"""
import glob
import json
import os
import re

R = os.path.join(os.path.dirname(__file__), "..", "reference")
DIMS = ("DISTANCE", "RADIUS", "DIAMETER", "ANGLE", "LENGTH")
ZERO = re.compile(r"^0(\.0*)?\s*(mm|cm|m|in|deg|rad|\*m|\*rad)?$")
# a size written inside an expression that otherwise derives: `#stub + 0.1 mm`, `0.48 * #ball`
HIDDEN = re.compile(r"\d+(\.\d+)?\s*(mm|cm|in|deg|rad)\b|(?<![\d/])\d*\.\d+")


def live(msg, ps):
    """The parameterIds this feature is actually using, by feature type."""
    t = msg["featureType"]
    g = lambda k: ps.get(k, {}).get("value")
    if t == "assignVariable":
        return ["value"]
    if t == "extrude":
        out = []
        if g("endBound") == "BLIND":
            out.append("depth")
        if g("hasOffset"):
            out.append("offsetDistance")
        if g("hasDraft"):
            out.append("draftAngle")
        if g("hasSecondDirection") and g("secondDirectionBound") == "BLIND":
            out.append("secondDirectionDepth")
        if g("hasSecondDirectionDraft"):
            out.append("secondDirectionDraftAngle")
        if g("bodyType") == "THIN":
            out += ["thickness1", "thickness2", "thickness"]
        return out
    if t == "revolve":
        return [] if g("fullRevolve") else ["angle", "angleBack"]
    if t == "circularPattern":
        return ["instanceCount"] + ([] if g("fullFeaturePattern") is None else ["angle"])
    if t == "linearPattern":
        return ["instanceCount", "distance"]
    if t == "mateConnector":
        return ["translationX", "translationY", "translationZ", "rotation"]
    if t == "transform":
        tt = g("transformType")
        if tt == "TRANSLATION_DISTANCE":
            return ["distance"]
        if tt == "ROTATION":
            return ["angle"]
        if tt == "TRANSLATION_3D":
            return ["dx", "dy", "dz"]
        return []
    return []


def typed_in(msg):
    """Every live number in one feature that names no variable and is not zero."""
    ps = {p["message"]["parameterId"]: p["message"] for p in msg.get("parameters", [])}
    out = []
    for pid in live(msg, ps):
        e = (ps.get(pid, {}).get("expression") or "").strip()
        if e and "#" not in e and not ZERO.match(e):
            out.append((pid, e))
    for c in msg.get("constraints", []):
        cm = c["message"]
        if cm.get("constraintType") not in DIMS:
            continue
        for p in cm["parameters"]:
            pm = p["message"]
            if pm.get("parameterId") not in ("length", "angle"):
                continue
            e = (pm.get("expression") or "").strip()
            if e and "#" not in e and not ZERO.match(e):
                out.append((cm["constraintType"].lower(), e))
    return out


def label(msg):
    """What to call a feature in a table. A variable goes by its variable name, because
    an unrenamed assignVariable feature is called `###name = #value` and eight of them
    under one heading say nothing."""
    if msg["featureType"] == "assignVariable":
        for p in msg["parameters"]:
            if p["message"]["parameterId"] == "name":
                return "#" + (p["message"].get("value") or "?")
    return msg.get("name")


def main():
    for path in sorted(glob.glob(os.path.join(R, "*.features.json"))):
        tab = os.path.basename(path).replace(".features.json", "")
        rows = []
        for f in json.load(open(path))["features"]:
            m = f["message"]
            for pid, e in typed_in(m):
                rows.append((label(m), m["featureType"], pid, e))
        print(f"\n## {tab} — {len(rows)} typed")
        for name, t, pid, e in rows:
            print(f"| `{name}` | {t} | {pid} | `{e}` |")


def hidden():
    """Sizes typed inside expressions that otherwise derive. A ratio such as `3 / 160` is
    how one size is built from another; a millimeter added to a variable is a typed size
    wearing an expression."""
    print("\n## typed inside a derived expression")
    for path in sorted(glob.glob(os.path.join(R, "*.features.json"))):
        tab = os.path.basename(path).replace(".features.json", "")
        for f in json.load(open(path))["features"]:
            m = f["message"]
            if m["featureType"] != "assignVariable":
                continue
            ps = {p["message"]["parameterId"]: p["message"] for p in m["parameters"]}
            e = (ps["value"].get("expression") or "").strip()
            if "#" in e and HIDDEN.search(e):
                print(f"| {tab} | `#{ps['name'].get('value')}` | `{e}` |")


if __name__ == "__main__":
    main()
    hidden()
