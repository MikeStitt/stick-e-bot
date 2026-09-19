#!/usr/bin/env python3
"""Score every tab's construction against the plan's rulings, from its own tree.

    uv run python .../scripts/c_score.py

The rows are what the GUI shows, read by `tree_ids.py`, so this scores the model
as a student would see it rather than as a record describes it. Three of the
seven rulings can be answered from the rows alone; the other four are answered
from what this draft built and are named with their evidence.
"""

from __future__ import annotations

import json
import re
import sys

from stickbot import repo_root

OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
TABS = ["ball and socket", "hinge", "body", "head", "foot", "u limb", "l limb", "gripper"]

# A row Onshape names itself, which the ruling says no feature may keep.
DEFAULT = re.compile(r"^(Extrude|Sketch|Revolve|Fillet|Chamfer|Mirror|Boolean|Plane|"
                     r"Mate connector|Derived|Split|Transform|Linear pattern|"
                     r"Circular pattern)\s*\d*$")
# What an untyped variable's row reads.
VARIABLE = re.compile(r"^#\w+ = ")
SKIP = {"Default geometry", "Origin", "Top", "Front", "Right", "Parts"}


def rows(tab):
    path = OUT / f"{tab.replace(' ', '-')}.tree-ids.json"
    return [r for r in json.loads(path.read_text())
            if r.get("type") and r.get("name") not in SKIP]


def main() -> int:
    print(f"{'tab':<16} {'features':>8} {'variables':>10} {'typed titles':>13} "
          f"{'default names':>14} {'says connector':>15}")
    bad = 0
    for tab in TABS:
        rs = rows(tab)
        variables = [r for r in rs if r["type"] == "assignVariable"]
        typed = [r for r in variables if not VARIABLE.match(r["name"] or "")]
        geometry = [r for r in rs if r["type"] != "assignVariable"]
        default = [r for r in geometry if DEFAULT.match((r["name"] or "").strip())]
        connector = [r for r in rs if "connector" in (r["name"] or "").lower()]
        bad += len(typed) + len(default) + len(connector)
        print(f"{tab:<16} {len(geometry):>8} {len(variables):>10} {len(typed):>13} "
              f"{len(default):>14} {len(connector):>15}")
        for r in typed:
            print(f"      variable titled over: {r['name']!r}")
        for r in default:
            print(f"      default feature name: {r['name']!r}")
        for r in connector:
            print(f"      still says connector: {r['name']!r}")
    print(f"\n{bad} rows fail a ruling a tree row can answer")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
