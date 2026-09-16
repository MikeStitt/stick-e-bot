"""Diff two tabs' sketches by where their geometry landed, for `audit.part`.

    uv run --project . python tools/diff_geometry.py <mine.json> <reference.json>

Each file is what [`read_sketches.py`](read_sketches.py) writes, off
`/api/partstudios/.../sketches?includeGeometry=true`, which answers while `/features` is rate
limited.  [`diff_sketches.py`](diff_sketches.py) says what a sketch was told and needs `/features`;
this says where the sketch ended up, which is the half that catches a point placed by clicking
instead of by constraint.  A circle whose center is 0.98 mm off the origin looks right on the
screen, extrudes without complaint, and moves everything built on it.

Every entity is reduced to the points that fix it, and matched against the reference's entity
nearest it, so the report is a distance rather than a list of ids.  Ids are per document and are
not compared.  The exit status is 1 if any sketch differs.
"""
import json
import math
import sys

PLACE = 4
SAME = 0.0001   # millimeters; nearer than this is the same point


def points(e):
    """The points that fix an entity, and what kind of entity it is."""
    kind = e.get("type")
    if kind == "circle":
        return kind, [tuple(e["center"]), (e["radius"],)]
    if kind == "arc":
        return kind, [tuple(e["center"]), tuple(e["startPoint"]), tuple(e["endPoint"]),
                      (e["radius"],)]
    if kind == "lineSegment":
        return kind, sorted([tuple(e["startPoint"]), tuple(e["endPoint"])])
    if kind == "point":
        return kind, [tuple(e["point"])] if "point" in e else [(0.0, 0.0)]
    fixed = [tuple(v) for k, v in sorted(e.items())
             if isinstance(v, list) and all(isinstance(c, (int, float)) for c in v)]
    return kind, fixed


def apart(a, b):
    """The furthest any one of an entity's points is from the matching point of another."""
    ka, pa = points(a)
    kb, pb = points(b)
    if ka != kb or len(pa) != len(pb):
        return None
    return max(math.sqrt(sum((x - y) ** 2 for x, y in zip(p, q))) for p, q in zip(pa, pb))


def say(e):
    kind, pts = points(e)
    return f"{kind} " + " ".join("(" + ", ".join(str(round(c, PLACE)) for c in p) + ")"
                                 for p in pts)


def plane(sk):
    p = sk.get("plane", {})
    return (tuple(round(c, PLACE) + 0.0 for c in p.get("origin", [])),
            tuple(round(c, PLACE) + 0.0 for c in p.get("normal", [])))


def match(mine, ref):
    """Pair each of my entities with the reference entity nearest it, and report the gaps."""
    spare = list(ref)
    gaps, lost = [], []
    for e in mine:
        near = sorted(((apart(e, g), g) for g in spare if apart(e, g) is not None),
                      key=lambda n: n[0])
        if not near:
            lost.append(e)
            continue
        gap, g = near[0]
        spare.remove(g)
        if gap > SAME:
            gaps.append((gap, e, g))
    return gaps, lost, spare


def main(mine_path, ref_path):
    a = json.load(open(mine_path))["sketches"]
    b = json.load(open(ref_path))["sketches"]
    print(f"sketches: mine {len(a)}, reference {len(b)}")
    only_a, only_b = sorted(set(a) - set(b)), sorted(set(b) - set(a))
    if only_a:
        print(f"  only in mine     : {only_a}")
    if only_b:
        print(f"  only in reference: {only_b}")

    differs = list(only_a) + list(only_b)
    for name in sorted(set(a) & set(b)):
        lines = []
        if plane(a[name]) != plane(b[name]):
            lines.append(f"  plane   : mine {plane(a[name])}, reference {plane(b[name])}")
        gaps, lost, spare = match(a[name].get("entities", []), b[name].get("entities", []))
        for gap, mine, ref in sorted(gaps, reverse=True):
            lines.append(f"  {round(gap, PLACE)} mm out: {say(mine)}")
            lines.append(f"        reference: {say(ref)}")
        for e in lost:
            lines.append(f"  only in mine     : {say(e)}")
        for e in spare:
            lines.append(f"  only in reference: {say(e)}")
        if lines:
            differs.append(name)
            print(f"\n{name}")
            print("\n".join(lines))

    if not differs:
        print(f"\nall {len(a)} sketches landed where the reference's did")
        return 0
    print(f"\n{len(differs)} sketch(es) differ: {sorted(set(differs))}")
    return 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
