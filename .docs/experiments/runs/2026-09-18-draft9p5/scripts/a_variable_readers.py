#!/usr/bin/env python3
"""Phase A — where each `assignVariable` goes in the new tree.

The ruling is that a variable is typed immediately before the first feature that
reads it, and a record can say whether that holds only if the expressions are
walked. This walks them: every string in every parameter of every feature, at any
depth, so a dimension inside a sketch constraint counts as a read.

A variable that is read only by another variable is placed by that one: the chain
is followed to the first feature that is not an `assignVariable`, which is what
the plan calls the first geometry feature.

Nothing here talks to Onshape. It reads the parents' records where they sit.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/a_variable_readers.py
"""

from __future__ import annotations

import json
import re
import sys

from stickbot import repo_root

ROOT = repo_root()
D4 = ROOT / ".docs/experiments/runs/2026-09-08-draft9p4/reference"
D3 = ROOT / ".docs/experiments/runs/2026-08-29-draft9p3/reference"
OUT = ROOT / ".docs/experiments/runs/2026-09-18-draft9p5/results"

# Each tab, and the record it is read from. The four joint tabs come from
# draft9p4's reference, which reads draft9p1p6; the rest from draft9p3's, which
# reads draft9p1p1.
TABS = [
    ("robot sizes", D4 / "robot-sizes.features.json"),
    ("ball and socket", D4 / "ball-and-socket.features.json"),
    ("hinge", D4 / "hinge.features.json"),
    ("body", D3 / "body.features.json"),
    ("head", D3 / "head.features.json"),
    ("foot", D3 / "foot.features.json"),
    ("u limb", D4 / "u-limb.features.json"),
    ("l limb", D4 / "l-limb.features.json"),
    ("gripper", D3 / "gripper.features.json"),
]

NAME = re.compile(r"#(\w+)")


def strings(node):
    """Every string anywhere under a parameter, at any depth."""
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for v in node.values():
            yield from strings(v)
    elif isinstance(node, list):
        for v in node:
            yield from strings(v)


def variable_name(message):
    for p in message.get("parameters", []):
        pm = p["message"]
        if pm.get("parameterId") == "name":
            return pm.get("value")
    return None


def reads(message, own_name=None):
    """The variable names this feature mentions, anywhere in it.

    A sketch's dimensions are in `constraints`, which is a sibling of
    `parameters` rather than inside it, so scanning parameters alone reports a
    tab whose every length is driven as reading nothing. The feature's own
    `name` is dropped because a variable's tree row is the literal
    `###name = #value`, and a variable's own `name` parameter is dropped because
    declaring a name is not reading it.
    """
    body = {k: v for k, v in message.items() if k != "name"}
    if own_name is not None:
        body["parameters"] = [p for p in message.get("parameters", [])
                              if p["message"].get("parameterId") != "name"]
    got = set(NAME.findall(" ".join(strings(body))))
    got.discard("name")
    got.discard("value")
    return got


def walk(path):
    """Per tab: the features in order, which are variables, and who reads what."""
    doc = json.loads(path.read_text())
    rows = []
    for i, f in enumerate(doc["features"]):
        m = f["message"]
        is_var = m.get("featureType") == "assignVariable"
        name = variable_name(m) if is_var else None
        rows.append({
            "i": i,
            "type": m.get("featureType"),
            "label": f"#{name}" if is_var else (m.get("name") or "(unnamed)"),
            "variable": name,
            "reads": sorted(reads(m, own_name=name)),
        })
    return rows


def first_readers(rows):
    """For each variable, the index of the first feature that is not a variable
    and that reads it, directly or through a chain of variables that read it."""
    declared = {r["variable"]: r["i"] for r in rows if r["variable"]}
    direct = {v: [] for v in declared}
    for r in rows:
        for v in r["reads"]:
            if v in direct:
                direct[v].append(r["i"])

    # A variable read only by other variables is placed by whatever places those.
    by_index = {r["i"]: r for r in rows}
    answer = {}
    for v in declared:
        seen, stack, best = set(), list(direct[v]), None
        while stack:
            i = stack.pop()
            if i in seen:
                continue
            seen.add(i)
            r = by_index[i]
            if r["variable"] is None:
                best = i if best is None else min(best, i)
            else:
                stack.extend(direct.get(r["variable"], []))
        answer[v] = best
    return declared, direct, answer


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    report, data = [], {}
    report.append("# Phase A — the first geometry feature that reads each variable\n")
    report.append(
        "Written by [`../scripts/a_variable_readers.py`](../scripts/a_variable_readers.py) on\n"
        "2026-09-18, from the parents' records. **Goes above** is where the variable is typed in\n"
        "draft9p5's tree: immediately before that feature. A variable with no reader is one\n"
        "nothing in the tab uses.\n")
    for tab, path in TABS:
        rows = walk(path)
        declared, direct, answer = first_readers(rows)
        by_index = {r["i"]: r for r in rows}
        data[tab] = {"declared": declared, "first_reader": answer,
                     "order": [r["label"] for r in rows]}
        n_vars = len(declared)
        report.append(f"## `{tab}`\n")
        report.append(f"{len(rows)} features, {n_vars} of them variables. "
                      f"Read from `{path.relative_to(ROOT)}`.\n")
        if not declared:
            report.append("No variables are declared in this tab.\n")
            continue
        if all(r["variable"] is not None for r in rows):
            report.append(
                "**A Variable Studio holds no geometry**, so no row here has a first reader in\n"
                "its own tab. Every reader is in another tab, and the order of the rows is the\n"
                "order the studio lists them in. draft9p4 walked these rows once; this table is\n"
                "the declaration order, and which tab reads each row is that walk's answer.\n")
        report.append("| Variable | Declared at | First geometry reader | Goes above |")
        report.append("| -------- | ----------: | --------------------- | ---------- |")
        for v, i in sorted(declared.items(), key=lambda kv: kv[1]):
            j = answer[v]
            if j is None:
                report.append(f"| `#{v}` | {i} | nothing reads it | — |")
            else:
                report.append(f"| `#{v}` | {i} | {j} `{by_index[j]['label']}` "
                              f"| `{by_index[j]['label']}` |")
        report.append("")
        unread = [v for v, j in answer.items() if j is None]
        if unread:
            report.append("**Read by nothing in this tab:** "
                          + ", ".join(f"`#{v}`" for v in sorted(unread)) + ".\n")
    (OUT / "variable-first-reader.md").write_text("\n".join(report) + "\n")
    (OUT / "variable-first-reader.json").write_text(json.dumps(data, indent=2) + "\n")
    print(f"wrote {OUT / 'variable-first-reader.md'}")
    for tab in data:
        d = data[tab]
        unread = [v for v, j in d["first_reader"].items() if j is None]
        print(f"  {tab:<16} {len(d['declared']):>2} variables, "
              f"{len(unread)} read by nothing")
    return 0


if __name__ == "__main__":
    sys.exit(main())
