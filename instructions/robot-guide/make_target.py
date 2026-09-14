#!/usr/bin/env python3
"""Emit every number the design asserts, as JSON, for measuring the CAD against.

Nothing here is typed in. The constants come out of `make_plans.py` by
introspection, so the target cannot drift from the sheets: if a number moves in
the generator it moves here on the next run, and if somebody adds a constant it
appears without this file being touched.

The joint stations at the bottom are the same values in the frame each part is
modeled in, which is what a FeatureScript measurement comes back in.

    python make_target.py            # to stdout
    python make_target.py FILE       # to a file
"""
import json
import math
import pathlib
import re
import sys

import make_plans as P

# Every module-level numeric constant, by name. Leading underscore means the
# generator considers it working-out rather than design.
NUMBERS = {k: v for k, v in vars(P).items()
           if not k.startswith("_") and k.isupper() and isinstance(v, (int, float))}

# The same, for the tuples the generator carries (stud direction, and so on).
VECTORS = {k: list(v) for k, v in vars(P).items()
           if not k.startswith("_") and k.isupper()
           and isinstance(v, tuple) and all(isinstance(x, (int, float)) for x in v)}


def joints():
    """Joint centers in the frame each part is modeled in, in mm.

    A part is modeled with its own primary joint on the origin, so these are what
    evBox3d and evSurfaceDefinition report back.
    """
    return {
        "torso": {
            "neck ball": [0, 0, P.NECK_Z],
            "hip ball R": [P.LEG_X, 0, P.HIP_Z],
            "hip ball L": [-P.LEG_X, 0, P.HIP_Z],
            # The shoulder is the one that is not on a face. It roots on the side
            # face SHOULDER_DROP below the top, and leaves at SHOULDER_EL/AZ.
            "shoulder root R": [P.TORSO_W / 2, 0, P.SH_ROOT],
            "shoulder ball R": [P.SH_X, P.ARM_PLANE_Y, P.SH_Z],
            "shoulder ball L": [-P.SH_X, P.ARM_PLANE_Y, P.SH_Z],
        },
        "limb-fork": {
            "socket ball": [0, 0, 0],
            "pin axis": [0, 0, -P.LIMB_CENTER],
            # The ear is rooted where its own limb's rod stops, which is EAR_FREE
            # back from the pin. The slot is cut past that, to SLOT_DEEP from the
            # fork's tip, and the two agree only when the rod is ROD_FORK long.
            "rod stops": [0, 0, -P.LIMB_CENTER + P.EAR_FREE],
            "slot root": [0, 0, -P.LIMB_CENTER + P.EAR_FREE],
            "ear tip": [0, 0, -P.LIMB_CENTER - P.NOSE],
        },
        "limb-blade": {
            "pin axis": [0, 0, 0],
            "ball": [0, 0, -P.LIMB_CENTER],
            # The tongue's tip is NOSE above the pin axis and it stands BLADE_OUT
            # out of its own limb, so the limb's end face is below the axis.
            "rod stops": [0, 0, P.NOSE - P.BLADE_OUT],
            "tongue root": [0, 0, -P.TAB_FREE],
            "tongue tip": [0, 0, P.NOSE],
        },
        "head": {"socket ball": [0, 0, 0],
                 "underside at the boss": [0, 0, -P.GRIP],
                 "top": [0, 0, -P.GRIP + P.HEAD_H]},
        "foot": {"socket ball": [0, 0, 0], "sole": [0, 0, -P.FOOT_H]},
        "hand": {"socket ball": [0, 0, 0],
                 "gripper bottom": [0, 0, -P.GRIPPER_L]},
    }


def stations():
    """Global z of everything on the figure's centerline, and the figure's height."""
    return {"sole": P.SOLE_Z, "ankle": P.ANKLE_Z, "knee": P.KNEE_Z,
            "hip": P.HIP_Z, "shoulder root": P.SH_ROOT, "shoulder ball": P.SH_Z,
            "elbow": P.EL_Z, "wrist": P.WR_Z, "gripper bottom": P.GB_Z,
            "neck": P.NECK_Z, "head underside": P.HEAD_B, "head top": P.HEAD_T,
            "height": P.HEIGHT}


BRIEFS = pathlib.Path(__file__).resolve().parents[2] / ".docs/experiments/build-briefs"

# A row is a target if its Source column says the design chose the number, and a
# record if the number came back out of a model. The plan turns on the difference.
TARGET_SOURCES = {"plan", "derived", "proposed", "balance", "r2"}
RECORD_SOURCES = {"built", "measured", "run 3", "run 4"}


def _classify(source):
    s = source.replace("*", "").strip().lower()
    if any(w in s for w in RECORD_SOURCES):
        return "record" if not any(w in s for w in TARGET_SOURCES) else "both"
    if any(w in s for w in TARGET_SOURCES):
        return "target"
    return "unclassified"


def _number(cell):
    """The first plain number in a cell, or None when the cell is not one."""
    m = re.search(r"-?\d+(?:\.\d+)?", cell.replace("Ø", ""))
    return float(m.group()) if m else None


def briefs():
    """Every numbers-table row in every brief, with its Source classified.

    Parsed, not transcribed, so a row that moves in a brief moves here. Tables
    are recognized by a header carrying both a units column and a Source column;
    anything else in the file is left alone and reported as skipped.
    """
    out, skipped = {}, []
    for path in sorted(BRIEFS.glob("*.md")):
        rows, header = [], None
        for line in path.read_text().splitlines():
            if not line.startswith("|"):
                header = None
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            low = [c.lower() for c in cells]
            if "source" in low and len(cells) >= 3:
                header = {"src": low.index("source")}
                header["val"] = next((i for i, c in enumerate(low)
                                      if c in ("mm", "value", "global z")), 1)
                continue
            if header is None or set("".join(cells)) <= set("-: "):
                continue
            if len(cells) <= max(header["src"], header["val"]):
                continue
            name, raw = cells[0], cells[header["val"]]
            src = cells[header["src"]]
            rows.append({"name": name, "raw": raw, "value": _number(raw),
                         "source": src, "kind": _classify(src)})
        if rows:
            out[path.stem] = rows
        else:
            skipped.append(path.stem)
    return out, skipped


def main():
    btab, skipped = briefs()
    doc = {"source": "make_plans.py by introspection; build-briefs/*.md by parsing",
           "numbers": dict(sorted(NUMBERS.items())),
           "vectors": dict(sorted(VECTORS.items())),
           "stations": stations(),
           "joints": joints(),
           "briefs": btab,
           "briefs_without_a_numbers_table": skipped}
    text = json.dumps(doc, indent=1, sort_keys=False)
    if len(sys.argv) > 1:
        open(sys.argv[1], "w").write(text + "\n")
        rows = sum(len(v) for v in btab.values())
        print(f"wrote {sys.argv[1]}  ({len(NUMBERS)} numbers, "
              f"{rows} brief rows across {len(btab)} briefs)")
        if skipped:
            print("  no numbers table: " + ", ".join(skipped))
    else:
        print(text)


if __name__ == "__main__":
    main()
