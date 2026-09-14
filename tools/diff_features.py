"""Diff two Part Studio reads parameter by parameter, for `audit.part`.

    uv run --project . python tools/diff_features.py <mine.json> <reference.json>

[`diff_construction.py`](diff_construction.py) answers what each feature was built on.  This
answers what each feature was told, which is where a sketch that reaches the right shape by the
wrong dimension shows up.

Geometry ids are per document, so a query is compared by how many entities it holds rather than by
which ones.  A query that holds one entity in one document and two in the other is a real
difference; a query holding `Jr6` where the other holds `Js6` is the same pick on the same face.
"""
import json
import sys

# A parameter carrying an enum keeps the choice in `value` and the enum's own type name in
# `enumName`.  Reading `enumName` makes every enum look alike.
SCALAR = ("value", "expression")


def key(m, seen):
    """What to call a feature when two of them share a name.

    A variable carries the placeholder `###name = #value` in the tree and its real name in a
    parameter, so a tab with twelve variables has twelve features called the same thing. Keying on
    the tree name alone drops eleven of them and reports a tab as agreeing when it has never been
    compared. A name that still repeats gets a number, so nothing is lost quietly.
    """
    name = m.get("name")
    if m.get("featureType") == "assignVariable":
        for p in m.get("parameters", []):
            pm = p["message"]
            if pm["parameterId"] == "name":
                name = f"#{pm.get('value')}"
                break
    seen[name] = seen.get(name, 0) + 1
    return name if seen[name] == 1 else f"{name} ({seen[name]})"


def read(path):
    """Name to parameters, plus the order the tree is in."""
    doc = json.load(open(path))
    out, order, seen = {}, [], {}
    for f in doc["features"]:
        m = f["message"]
        name = key(m, seen)
        order.append(name)
        out[name] = {"type": m.get("featureType"), "parameters": params(m)}
    return out, order


def params(m):
    got = {}
    for p in m.get("parameters", []):
        pm = p["message"]
        pid = pm["parameterId"]
        if "queries" in pm:
            got[pid] = ("entities", sum(len(q["message"].get("geometryIds") or [])
                                        for q in pm["queries"]))
        else:
            got[pid] = next(((k, pm[k]) for k in SCALAR if k in pm), ("empty", None))
    return got


def main(mine_path, ref_path):
    a, order_a = read(mine_path)
    b, order_b = read(ref_path)

    print(f"features: mine {len(a)}, reference {len(b)}")
    only_a = [n for n in order_a if n not in b]
    only_b = [n for n in order_b if n not in a]
    print(f"  only in mine     : {only_a}")
    print(f"  only in reference: {only_b}")
    shared_a = [n for n in order_a if n in b]
    shared_b = [n for n in order_b if n in a]
    print(f"  same order       : {shared_a == shared_b}")
    if shared_a != shared_b:
        print(f"      mine     : {shared_a}")
        print(f"      reference: {shared_b}")

    print("\nparameters -- differences only")
    same = 0
    for n in shared_b:
        fa, fb = a[n], b[n]
        rows = []
        if fa["type"] != fb["type"]:
            rows.append(("featureType", fa["type"], fb["type"]))
        pa, pb = fa["parameters"], fb["parameters"]
        for pid in sorted(set(pa) | set(pb)):
            va, vb = pa.get(pid, ("absent", None)), pb.get(pid, ("absent", None))
            if va != vb:
                rows.append((pid, va, vb))
        if not rows:
            same += 1
            continue
        print(f"  {n}  ({fb['type']})")
        for pid, va, vb in rows:
            print(f"      {pid}")
            print(f"          mine     : {va}")
            print(f"          reference: {vb}")
    print(f"\n{same} of {len(shared_b)} shared features agree on every parameter")


if __name__ == "__main__":
    main(*sys.argv[1:3])
