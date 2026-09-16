"""Diff two tabs' sketches out of their `/features` records.

    uv run --project . python tools/diff_sketches.py <mine.features.json> <ref.features.json>

`tools/diff_construction.py` reads the dependency graph, which names what a feature was
built on and cannot see how. Two sketches can stand on the same plane, hold the same
dimensions and land the same shape, and still say different things about why the shape is
that shape. This reads the sketches themselves and reports four things per sketch:

- the plane it sits on,
- what entities it holds, so a projected edge that is missing shows up as a shortfall,
- every constraint by type, so a length standing where a distance should be shows up,
- every id the constraints reach for outside the sketch, so picking the origin where the
  reference picks an edge, or an edge where the reference picks the origin, shows up.

An id is not promised to mean the same thing in two documents. Two tabs built the same way
in the same order do come out with the same ids, so a difference is worth reading; a match
is worth nothing on its own. The exit status is 1 if any sketch differs.
"""
import json
import sys
from collections import Counter

# A dimension's value is one of these. `labelDistance` and `labelRatio` are expressions too,
# and they hold where the number is drawn on the screen, so reading the last expression in
# the list makes every sketch look different from every other.
VALUE = ("length", "angle", "radius", "diameter")


def load(path):
    d = json.load(open(path))
    return d["features"] if isinstance(d, dict) and "features" in d else d


def sketches(feats):
    return {f["message"]["name"]: f["message"]
            for f in feats if f.get("typeName") == "BTMSketch"}


def plane(sk):
    for p in sk.get("parameters", []):
        m = p.get("message", p)
        if m.get("parameterId") == "sketchPlane":
            return [g for q in m.get("queries", [])
                    for g in (q.get("message", q).get("geometryIds") or [])]
    return []


def entities(sk):
    return Counter(e.get("typeName", "?").replace("BTMSketch", "")
                   for e in sk.get("entities", []))


def constraints(sk):
    """Each constraint as (type, the expression it drives), None where it drives nothing."""
    got = []
    for c in sk.get("constraints", []):
        m = c.get("message", c)
        expr = None
        for p in m.get("parameters", []):
            pm = p.get("message", p)
            if pm.get("parameterId") in VALUE and "expression" in pm:
                expr = pm["expression"]
        got.append((m.get("constraintType"), expr))
    return got


def reaches(sk):
    """Every id the constraints hold on to outside the sketch, and how often."""
    t = Counter()
    for c in sk.get("constraints", []):
        for p in c.get("message", c).get("parameters", []):
            for q in p.get("message", p).get("queries", []):
                for g in q.get("message", q).get("geometryIds") or []:
                    t[g] += 1
    return t


def main(mine_path, ref_path):
    a, b = sketches(load(mine_path)), sketches(load(ref_path))
    print(f"sketches: mine {len(a)}, reference {len(b)}")
    print(f"  only in mine     : {sorted(set(a) - set(b))}")
    print(f"  only in reference: {sorted(set(b) - set(a))}")

    differs = sorted(set(a) - set(b)) + sorted(set(b) - set(a))
    for name in sorted(set(a) & set(b)):
        sa, sb = a[name], b[name]
        lines = []

        if plane(sa) != plane(sb):
            lines.append(f"  plane       : mine {plane(sa)}, reference {plane(sb)}")
        ea, eb = entities(sa), entities(sb)
        if ea != eb:
            lines.append(f"  entities    : mine {dict(ea)}, reference {dict(eb)}")

        ca, cb = constraints(sa), constraints(sb)
        ta, tb = Counter(t for t, _ in ca), Counter(t for t, _ in cb)
        if ta != tb:
            lines.append("  constraints :")
            for t in sorted(set(ta) | set(tb)):
                if ta[t] != tb[t]:
                    lines.append(f"      {t}: mine {ta[t]}, reference {tb[t]}")

        da = sorted(e for _, e in ca if e is not None)
        db = sorted(e for _, e in cb if e is not None)
        if da != db:
            lines.append(f"  dimensions  : mine {da}")
            lines.append(f"                reference {db}")

        ra, rb = reaches(sa), reaches(sb)
        if ra != rb:
            lines.append(f"  reaches for : mine {dict(ra)}, reference {dict(rb)}")

        if lines:
            differs.append(name)
            print(f"\n== {name}")
            print("\n".join(lines))

    print()
    if differs:
        print(f"{len(set(differs))} sketch(es) differ from the reference: "
              f"{sorted(set(differs))}")
        return 1
    print(f"every one of the {len(a)} sketches matches the reference")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
