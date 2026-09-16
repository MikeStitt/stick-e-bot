"""Diff two Part Studios face by face, for the shape half of `audit.part`.

    uv run --project . python tools/diff_shape.py <mine.json> <reference.json>

[`diff_features.py`](diff_features.py) answers what each feature was told, and reads `/features`.
This answers what the part came out as, and reads `bodydetails`, so it still works while
`/features` is rate limited.  Each file is the list [`read_shape.py`](read_shape.py) writes: one
entry per face, holding the face's surface, its area and its bounding box, in millimeters.

**A near miss is the finding this tool exists for.**  A part that is 1 mm out of place shares most
of its faces with the reference and reads as agreeing on the count, so a count is not a verdict.
Every face that fails to match is followed up: the nearest face of the same kind and size in the
reference is found, and how far it had to look is printed.  A face a fraction of a millimeter away
from its counterpart is a sketch placed by clicking rather than by constraint; a face with no
counterpart at all is something built or not built.

A surface is compared by what fixes it in space, not by the numbers the read happens to carry.  A
cylinder's `origin` is any point on its axis, so two records of one cylinder can hold different
origins and opposite axes; what identifies it is the axis line, written here as the direction with
its sign settled and the foot of the perpendicular from the world origin.  A plane's `origin` is
any point on it, so it is written as its normal with its sign settled and its distance along that
normal.  A sphere and a torus are fixed by their centers, which are read as given.
"""
import json
import math
import sys

PLACE = 4       # millimeters are rounded here, which is finer than any dimension in the model
NEAR = 5.0      # a counterpart further away than this is a different face, not a moved one


def clean(x):
    """Round, and take the sign off a zero, so that 0.0 and -0.0 are one number."""
    return round(x, PLACE) + 0.0


def direction(v):
    """The unit direction, pointed so that its first real component is positive."""
    for c in v:
        if abs(c) > 10 ** -PLACE:
            flip = -1 if c < 0 else 1
            return tuple(clean(a * flip) for a in v)
    return tuple(clean(a) for a in v)


def where(s):
    """What fixes this surface in space, and what size it is."""
    kind = s["type"]
    o = s.get("origin", [0, 0, 0])
    if kind == "plane":
        n = direction(s["normal"])
        return ("plane", n, clean(sum(a * b for a, b in zip(n, o))))
    if kind == "cylinder":
        a = direction(s["axis"])
        along = sum(p * q for p, q in zip(o, a))
        foot = tuple(clean(p - along * q) for p, q in zip(o, a))
        return ("cylinder", clean(s["radius"]), a, foot)
    if kind == "torus":
        return ("torus", clean(s["majorRadius"]), clean(s["minorRadius"]),
                direction(s["axis"]), tuple(clean(c) for c in o))
    if kind == "cone":
        return ("cone", clean(s["radius"]), clean(s["halfAngle"]), direction(s["axis"]),
                tuple(clean(c) for c in o))
    if kind == "sphere":
        return ("sphere", clean(s["radius"]), tuple(clean(c) for c in o))
    # Anything else is compared on its own numbers, rounded, because a read carries a surface out
    # to the last bit it has and two builds of one face need not agree there: the head's four
    # cones differ in the thirteenth decimal of their half angle and are the same cone.
    return (kind, tuple(sorted((k, tuple(clean(c) for c in v) if isinstance(v, list)
                                else clean(v) if isinstance(v, float) else v)
                               for k, v in s.items() if k != "type")))


def spot(f):
    """The middle of the face itself, which says where along a surface the face was trimmed."""
    box = f.get("box") or {}
    lo, hi = box.get("minCorner"), box.get("maxCorner")
    if not lo or not hi:
        return None
    return tuple(clean((a + b) / 2) for a, b in zip(lo, hi))


def key(f):
    return (where(f["surface"]), clean(f["area"]), spot(f))


def size(f):
    """The kind and size of a surface, with where it sits left out.

    Two faces are only worth measuring the distance between if they could be the same face built
    in the wrong place, so a plane is only compared with a plane facing the same way and a
    cylinder only with a cylinder of the same radius.
    """
    w = where(f["surface"])
    kind = w[0]
    if kind == "plane":
        return ("plane", w[1])
    if kind in ("cylinder", "sphere"):
        return (kind, w[1])
    if kind == "cone":
        return ("cone", w[1], w[2], w[3])
    if kind == "torus":
        return ("torus", w[1], w[2], w[3])
    return (kind,)


def place(f):
    """The point that stands for where a surface sits.

    A cylinder is its axis line, so the point is the foot of the perpendicular from the world
    origin; a plane is the point on it nearest the world origin. Neither depends on where along
    the surface the face happens to have been trimmed, which is what makes this the distance to
    measure. The middle of the face's own box is the other thing worth knowing and is reported
    beside it.
    """
    w = where(f["surface"])
    kind = w[0]
    if kind == "plane":
        return tuple(clean(c * w[2]) for c in w[1])
    if kind == "cylinder":
        return w[3]
    if kind in ("cone", "torus"):
        return w[-1]
    if kind == "sphere":
        return w[2]
    return None


def apart(f, g):
    """How far apart two surfaces of the same kind sit."""
    a, b = place(f), place(g)
    if a is None or b is None:
        return None
    return math.sqrt(sum((p - q) ** 2 for p, q in zip(a, b)))


def say(f):
    s = f["surface"]
    w = where(s)
    tail = f"  area {clean(f['area'])} mm2"
    if s["type"] == "plane":
        return f"plane, normal {w[1]}, {w[2]} mm along it{tail}"
    if s["type"] == "cylinder":
        return f"cylinder r {w[1]}, axis {w[2]} through {w[3]}{tail}"
    if s["type"] == "torus":
        return f"torus R {w[1]} r {w[2]}, axis {w[3]} at {w[4]}{tail}"
    if s["type"] == "sphere":
        return f"sphere r {w[1]} at {w[2]}{tail}"
    return f"{s['type']}{tail}"


def take(pool, k):
    """Take one face matching k out of the pool, and say whether there was one."""
    for i, f in enumerate(pool):
        if key(f) == k:
            pool.pop(i)
            return True
    return False


def main(mine_path, ref_path):
    mine = json.load(open(mine_path))
    ref = json.load(open(ref_path))
    print(f"faces: mine {len(mine)}, reference {len(ref)}")

    left, spare = [], list(ref)
    for f in mine:
        if not take(spare, key(f)):
            left.append(f)
    print(f"  {len(mine) - len(left)} faces are the same face in both")

    moved = 0
    for f in left:
        near = [(apart(f, g), g) for g in spare if size(g) == size(f)]
        near = sorted([n for n in near if n[0] is not None], key=lambda n: n[0])
        print(f"\n  only in mine     : {say(f)}")
        if near and near[0][0] <= NEAR:
            gap = round(near[0][0], PLACE)
            moved += bool(gap)
            print(f"      {gap} mm from where the reference puts a face of that kind"
                  if gap else "      in the same place as a face the reference has, "
                              "trimmed to a different size")
            print(f"      reference has    : {say(near[0][1])}")
        elif near:
            print(f"      nothing of that kind nearer than {round(near[0][0], PLACE)} mm")
        else:
            print("      the reference has no face of that kind and size")
    for g in spare:
        if not any(size(g) == size(f) and (apart(f, g) or NEAR + 1) <= NEAR for f in left):
            print(f"\n  only in reference: {say(g)}")

    if not left and not spare:
        print("\nthe two parts are the same shape, face for face")
        return 0
    print(f"\n{len(left)} faces of mine and {len(spare)} of the reference's went unmatched, "
          f"{moved} of them a face that moved rather than a face that is not there")
    return 1


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
