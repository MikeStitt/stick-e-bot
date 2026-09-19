#!/usr/bin/env python3
"""Phase B — the build order for every tab, derived rather than typed.

Three sources meet here. The brief's *Recommended steps* gives the geometry in
order, under the names this draft builds; the plan's rename table says what each
of those was called in the parent, because the parents' records predate the
names; and Phase A's walk says which variable is read first by which feature, so
each `assignVariable` lands immediately above its first reader.

Writes `results/build-order.json`, which `b_build.py` reads, and prints the
tab-by-tab lines the plan's unrolled checklist carries.

    uv run python .../scripts/b_order.py
"""

from __future__ import annotations

import json
import re
import sys

from stickbot import repo_root

ROOT = repo_root()
BRIEFS = ROOT / ".docs/experiments/build-briefs"
D4 = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"

# tab -> the brief it is built from, which record the parent is, and which of
# the brief's step tables when a brief carries two.
TABS = [
    ("ball and socket", "ball-and-socket.md", D4 / "ball-and-socket.features.json", 0),
    ("hinge", "hinge.md", D4 / "hinge.features.json", 0),
    ("body", "torso.md", D3 / "body.features.json", 0),
    ("head", "head.md", D3 / "head.features.json", 0),
    ("foot", "foot.md", D3 / "foot.features.json", 0),
    ("u limb", "limbs.md", D4 / "u-limb.features.json", 0),
    ("l limb", "limbs.md", D4 / "l-limb.features.json", 1),
    ("gripper", "gripper.md", D3 / "gripper.features.json", 0),
    ("stickbot", "assembly.md", D3 / "assembly.features.json", 0),
]

# The plan's § The features that change name, as new name -> the parent's name.
RENAME = {
    "hinge": {
        "fork prong wedge outline": "ear wedge outline",
        "fork prong wedge": "ear wedge",
        "fork prong wedges": "ear wedges",
        "axle bore sketch": "pocket axle sketch",
        "axle bore on fork": "pocket axle on fork",
        "fork to robot": "fork to robot connector",
        "blade to robot": "blade to robot connector",
    },
    "body": {
        "neck": "neck connector",
        "left shoulder": "left shoulder connector",
        "right shoulder": "r shoulder connector",
        "left hip": "l hip connector",
        "right hip": "r hip connector",
        "mate for shoulder stud": "connector on torso shoulder",
        "mate for hip stud": "hip connector on torso",
        "mate for neck stud": "neck connector on torso",
        "hip stud location": "hip connector location",
        "neck stud location": "neck connector location",
    },
}

ROW = re.compile(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|")


def brief_steps(name, which):
    """Every *Recommended steps* table in a brief, as (featureType, name) rows."""
    tables, current, in_table = [], [], False
    for line in (BRIEFS / name).read_text().splitlines():
        m = ROW.match(line)
        if m:
            in_table = True
            current.append((m.group(2), m.group(3)))
        elif in_table and not line.strip().startswith("|"):
            tables.append(current)
            current, in_table = [], False
    if current:
        tables.append(current)
    return tables[which]


def parent_names(path):
    """The parent's features: geometry by name, variables by `#name`."""
    geometry, variables = set(), {}
    for f in json.loads(path.read_text())["features"]:
        m = f["message"]
        if m.get("featureType") == "assignVariable":
            n = next(p["message"].get("value") for p in m["parameters"]
                     if p["message"]["parameterId"] == "name")
            variables[f"#{n}"] = m.get("name")
        else:
            geometry.add(m.get("name"))
    return geometry, variables


def main() -> int:
    walk = json.loads((OUT / "variable-first-reader.json").read_text())
    out, lines = {}, []
    for tab, brief, parent_path, which in TABS:
        steps = brief_steps(brief, which)
        geometry, variables = parent_names(parent_path)
        rename = RENAME.get(tab, {})

        missing = [n for _, n in steps if rename.get(n, n) not in geometry]
        if missing:
            raise RuntimeError(f"`{tab}`: the parent has no feature named {missing}")

        # Each variable, against the parent name of the feature that first reads it.
        first = walk.get(tab, {}).get("first_reader", {})
        order_names = walk.get(tab, {}).get("order", [])
        above = {}
        for var, idx in first.items():
            if idx is None:
                continue
            above.setdefault(order_names[idx], []).append(f"#{var}")

        order, rows = [], []
        for ftype, new in steps:
            parent = rename.get(new, new)
            for var in above.get(parent, []):
                order.append({"parent": var, "name": None, "type": "assignVariable"})
                rows.append((var, "assignVariable", var))
            order.append({"parent": parent, "name": new, "type": ftype})
            rows.append((new, ftype, parent))

        placed = {o["parent"] for o in order if o["type"] == "assignVariable"}
        unplaced = [v for v in variables if v not in placed]
        out[tab] = {"brief": brief, "parent": str(parent_path.relative_to(ROOT)),
                    "order": order, "dropped_variables": unplaced}

        lines.append(f"\n#### Tab `{tab}` — {len(order)} features "
                     f"({len(rows) - len(placed)} geometry, {len(placed)} variables)")
        if unplaced:
            lines.append(f"  dropped, read by nothing: {', '.join(sorted(unplaced))}")
        for new, ftype, parent in rows:
            note = "" if new == parent or ftype == "assignVariable" else f"  (was `{parent}`)"
            lines.append(f"- [ ] `{new}` — {ftype}{note}")

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "build-order.json").write_text(json.dumps(out, indent=2) + "\n")
    (OUT / "build-order.md").write_text("\n".join(lines) + "\n")
    total = sum(len(v["order"]) for v in out.values())
    print(f"wrote {OUT / 'build-order.json'}")
    for tab, v in out.items():
        n_var = sum(1 for o in v["order"] if o["type"] == "assignVariable")
        print(f"  {tab:<16} {len(v['order']):>3} features  ({n_var} variables)"
              + (f"  dropped {v['dropped_variables']}" if v["dropped_variables"] else ""))
    print(f"  {'total':<16} {total:>3}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
