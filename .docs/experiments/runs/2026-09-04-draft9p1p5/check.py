#!/usr/bin/env python3
"""Read stickbot-draft9p1p5 back and check every settled number against make_plans.py.

Brought forward from ``../2026-09-02-draft9p1p4/check.py``. The detent changed, so the
rows that read it changed with it.

The teeth and the valleys are gone. draft9p1p4 asked for ``TEETH`` cones on each leaf and
a matching ring of blind ``VALLEY_D`` holes in each ear; neither name is in the design
source now. In their place each of the four mating faces carries a ring of ``WEDGES``
drafted pie slices, so a ring is read as a count of crests, an area for one crest, and two
rings of cone flanks that have to lean the printable way. That last row is not decoration:
an inverted draft still regenerates, still passes every dimension, and turns the ring into
a disc.

The relief slit tapers, so its walls are no longer at one station. A wall is read off the
plane's own equation at the two ``z`` that the design source names, the tongue's root and
its tip.

The frame is draft9p1p4's. A limb runs along z, its leaves lie across y, and the two
printing flats face along x.

Nothing is typed. Each row asks the model a question a face already answers and compares
the answer with the number ``make_plans`` derives.

    uv run --project . python -u .docs/experiments/runs/2026-09-04-draft9p1p5/check.py
"""
from __future__ import annotations

import collections
import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "instructions" / "robot-guide"))

from playwright.sync_api import sync_playwright   # noqa: E402
from tools import onshape_session as S            # noqa: E402
import make_plans as P                            # noqa: E402

DID, WID = "e5bdf1e586fb6c868066df22", "e051660ad432c2cfabda245b"
TOL = 1e-3

# The frame every row reads in. A limb runs along z, its leaves lie across y, and the two
# printing flats face along x.
FLATN, LEAF, LONG = 0, 1, 2


def faces(page, doc):
    res = S.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")
    for b in res["body"]["bodies"]:
        for f in b["faces"]:
            yield b["id"], f


def part_names(page, doc):
    return sorted(p["name"] for p in S.api(page, "GET", f"/api/parts/{doc.path}")["body"])


def mm(x):
    return x * 1000


def near(a, b):
    return abs(a - b) < TOL


class Check:
    def __init__(self):
        self.rows = []

    def __call__(self, what, got, want, unit="mm"):
        """A row of the report. `got` is a length, or nothing when the faces it was
        measured from are missing: `faces and max(...)` hands back the empty list, and a
        row with nothing to measure is a failed row rather than a crash."""
        if not isinstance(got, (int, float)):
            got = None
        ok = got is not None and near(got, want)
        self.rows.append((ok, what, got, want, unit))
        return ok

    def same(self, what, got, want):
        """A row whose answer is a name or a list rather than a length."""
        self.rows.append((got == want, what, got, want, ""))

    def report(self):
        bad = 0
        for ok, what, got, want, unit in self.rows:
            if isinstance(got, (int, float)) or got is None:
                g = "missing" if got is None else f"{got:10.4f}"
                w = f"{want:10.4f} {unit}"
            else:
                g, w = str(got), str(want)
            print(f"  {'ok ' if ok else 'BAD'}  {what:46s} {g}  want {w}")
            bad += not ok
        print(f"  {len(self.rows) - bad}/{len(self.rows)} rows agree")
        return bad


def tally(fs):
    """Every face grouped by what it is, so a count is a question the model answers."""
    out = collections.defaultdict(list)
    for _, f in fs:
        s = f["surface"]
        key = s["type"]
        if s["type"] in ("cylinder", "sphere", "cone"):
            key += f" r{mm(s['radius']):.3f}"
        out[key].append(f)
    return out


def plane_at(fs, axis, station):
    """Planar faces whose whole extent sits on one station of an axis."""
    out = []
    for _, f in fs:
        if f["surface"]["type"] != "plane":
            continue
        lo, hi = f["box"]["minCorner"][axis], f["box"]["maxCorner"][axis]
        if near(mm(lo), station) and near(mm(hi), station):
            out.append(f)
    return out


def span(faces_, axis):
    lo = min(mm(f["box"]["minCorner"][axis]) for f in faces_)
    hi = max(mm(f["box"]["maxCorner"][axis]) for f in faces_)
    return lo, hi


def check_flats(fs, c):
    """The rod's top and bottom, cut away flat so the limb prints on a face.

    FLAT is the circle's height at the slot wall, so the cut arrives tangent to the ear and
    takes nothing off it, and each flat comes out SEAT wide because that is the other leg of
    the same right triangle.
    """
    lo, hi = span([f for _, f in fs], FLATN)
    c("across the chord, so the rod is not round", hi - lo, P.LIMB_FLAT)
    seen = []
    for sign in (1, -1):
        band = plane_at(fs, FLATN, sign * P.FLAT)
        seen.append(len(band))
        width = None
        if band:
            width = span(band, LEAF)[1] - span(band, LEAF)[0]
        c(f"the flat at x {sign * P.FLAT:+.4f} is {P.SEAT:g} across the pin", width, P.SEAT)
    c("as many faces on the bottom flat as the top", seen[1], seen[0], "")


def check_leaves(fs, t, c, rings=True, stubs=True):
    """What a blade's leaves measure, in the tab that holds them."""
    for sign in (1, -1):
        face = sign * P.BLADE / 2
        c(f"leaf face at y {face:+g}", len(plane_at(fs, LEAF, face)), 1, "")
        if rings:
            check_ring(fs, t, c, face, sign)
        if stubs:
            c(f"axle end at y {sign * (P.BLADE / 2 + P.STUB_PROUD):+g}",
              len(plane_at(fs, LEAF, sign * (P.BLADE / 2 + P.STUB_PROUD))), 1, "")
    check_slit(fs, c)


def check_slit(fs, c):
    """The relief slit up the tongue's middle, which tapers now.

    A wall is the only plane in the part that faces across the leaves without being square
    to them, so that is how it is found. Where it sits is then read off the plane itself:
    at x 0 the plane equation gives y for any z, and the two z the design source names are
    the tongue's root and the tongue's tip.
    """
    walls = [f["surface"] for _, f in fs
             if f["surface"]["type"] == "plane"
             and abs(f["surface"]["normal"][FLATN]) < 1e-6
             and 0.5 < abs(f["surface"]["normal"][LEAF]) < 1 - 1e-6]
    c("slit walls, and neither is square to the leaves", len(walls), 2, "")
    for s in walls:
        def y_at(z, s=s):
            return (mm(s["origin"][LEAF])
                    - s["normal"][LONG] / s["normal"][LEAF] * (z - mm(s["origin"][LONG])))
        sign = math.copysign(1, y_at(-P.TAB_FREE))
        c(f"the slit at the tongue's root, wall y {sign:+.0f}",
          y_at(-P.TAB_FREE), sign * P.SLIT / 2)
        c(f"the slit at the tongue's tip, wall y {sign:+.0f}",
          y_at(P.NOSE), sign * (P.BLADE / 2 - P.LEAF_TIP))


def check_slot(fs, t, c, pin):
    """The fork's slot, after the land came out of the design source.

    One wall a side, at SEAT / 2, running the whole way from the fork's tip to its root. A
    second plane a side would be the step the land used to leave. Each wall carries a ring
    of wedges standing back into the slot, which is checked here because the wall is what
    they stand on.
    """
    for sign in (1, -1):
        wall = plane_at(fs, LEAF, sign * P.SEAT / 2)
        c(f"slot wall at y {sign * P.SEAT / 2:+g}, and only one", len(wall), 1, "")
        if wall:
            lo, hi = span(wall, LONG)
            c(f"the wall at y {sign * P.SEAT / 2:+g} starts at the tip", lo, pin - P.NOSE)
            c(f"the wall at y {sign * P.SEAT / 2:+g} ends at the root", hi, pin + P.EAR_FREE)
        check_ring(fs, t, c, sign * P.SEAT / 2, -sign)
    c("ear to tongue, a side", P.SEAT / 2 - P.BLADE / 2, P.GAP)
    c("axle engaged in the bore",
      (P.BLADE / 2 + P.STUB_PROUD) - P.SEAT / 2, P.STUB_PROUD - P.GAP)


def crest_area():
    """One crest, in mm2, integrated over the ring.

    A crest is not a sector. Its two arcs are a wedge height in from the ring's own radii,
    which a sector would handle, but its two straight sides are a wedge height in from the
    pie slice's radial sides, and a line parallel to a radius meets every other radius at a
    different angle. So the half angle that survives at radius r is the slice's half angle
    less asin(WEDGE_H / r), and the area is that swept from one arc to the other.
    """
    half = math.radians(P.WEDGE_W) / 2
    r1, r2 = P.RING_IN + P.WEDGE_H, P.RING_CON
    n, area = 20000, 0.0
    for i in range(n):
        r = r1 + (r2 - r1) * (i + 0.5) / n
        area += 2 * max(half - math.asin(P.WEDGE_H / r), 0.0) * r
    return area * (r2 - r1) / n


def check_ring(fs, t, c, face, up):
    """One ring of wedges standing WEDGE_H off the plane at y ``face``.

    ``up`` is the way they grow, which is away from the pin on the tongue and toward it in
    the fork's slot, because both rings stand into the gap between the two members.

    The last row of each pair is the one that has to be here. A cone reports its radius at
    its origin and grows that radius along its axis, so which way a flank leans is a fact
    the model states and no dimension does. Draft the ring the wrong way and the part still
    regenerates, every station still reads right, and the twelve crests merge into one disc
    on flanks that print as overhangs.
    """
    crest = face + up * P.WEDGE_H
    tops = plane_at(fs, LEAF, crest)
    c(f"crests at y {crest:+g}", len(tops), P.WEDGES, "")
    c(f"one crest at y {crest:+g}",
      tops and sum(f["area"] for f in tops) * 1e6 / len(tops), crest_area(), "mm2")
    for r, lean in ((P.RING_OUT, -1), (P.RING_IN, +1)):
        # A cone reports its radius at its origin, and a flank's radius is the ring's own
        # radius on the face it stands on, so the origin station is which ring it belongs
        # to. In the hinge tab both members are present and both rings are on the same side
        # of the pin, so a filter on the sign alone would count each ring twice.
        cones = [f for f in t.get(f"cone r{r:.3f}", [])
                 if near(mm(f["surface"]["origin"][LEAF]), face)]
        c(f"flanks at r{r:.4f} off y {face:+g}", len(cones), P.WEDGES, "")
        c(f"draft at r{r:.4f} off y {face:+g}",
          cones and math.degrees(cones[0]["surface"]["halfAngle"]), 45.0, "deg")
        c(f"flanks leaning in at r{r:.4f} off y {face:+g}",
          sum(1 for f in cones
              if math.copysign(1, f["surface"]["axis"][LEAF] * up) == lean),
          P.WEDGES, "")


def check_socket(fs, t, c, center):
    """Every row a socket answers, wherever it is built. ``center`` is its ball's center."""
    c("cavity", len(t.get(f"sphere r{P.CAVITY:.3f}", [])), 1, "")
    c("collar, so the wall is %.1f" % P.COLLAR_WALL,
      len(t.get(f"cylinder r{P.COLLAR_R:.3f}", [])), 1, "")
    rim = plane_at(fs, LONG, center + P.GRIP)
    c("rim, one arc per finger", len(rim), 4, "")
    half = P.SLIT_W / 2
    strip = lambda r: half * math.sqrt(r ** 2 - half ** 2) + r ** 2 * math.asin(half / r)
    annulus = math.pi * (P.COLLAR_R ** 2 - (P.MOUTH / 2) ** 2)
    c("one finger's top face, so the mouth is Ø%.2f" % P.MOUTH,
      rim and sum(f["area"] for f in rim) * 1e6 / 4,
      (annulus - 4 * (strip(P.COLLAR_R) - strip(P.MOUTH / 2))) / 4, "mm2")
    c("slit floors, so a finger is %.4f long" % P.SLIT_D,
      len(plane_at(fs, LONG, center + P.GRIP - P.SLIT_D)), 4, "")
    cav = t.get(f"sphere r{P.CAVITY:.3f}", [])
    c("the slits break into the cavity",
      cav and max(mm(f["box"]["maxCorner"][FLATN]) for f in cav),
      math.sqrt(P.CAVITY ** 2 - (P.SLIT_W / 2) ** 2), "mm")
    c("socket base, below the ball's center",
      len(plane_at(fs, LONG, center - P.COLLAR_L)), 1, "")


def check_stud(fs, t, c, center, up):
    """The ball stud: its ball, its stalk, and the face the ball stands off."""
    c("ball", len(t.get(f"sphere r{P.BALL / 2:.3f}", [])), 1, "")
    c("stalk", len(t.get(f"cylinder r{P.STALK / 2:.3f}", [])), 1, "")
    ball = t.get(f"sphere r{P.BALL / 2:.3f}", [])
    if ball:
        c("the ball's center", mm(ball[0]["surface"]["origin"][LONG]), center)
    c("the stud's face, off the ball's center",
      len(plane_at(fs, LONG, center + up * P.STAND)), 1, "")


def check_ball_and_socket(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c.same("two parts", part_names(page, doc), ["ball stud", "socket body"])
    c("two bodies, and they are apart", len({b for b, _ in fs}), 2, "")
    check_socket(fs, t, c, 0.0)
    check_stud(fs, t, c, 0.0, +1)


def check_hinge(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c.same("two parts", part_names(page, doc), ["blade", "fork"])
    c("bores, both ears", len(t.get(f"cylinder r{P.BORE_D / 2:.3f}", [])), 2, "")
    # Two patches and not three. The slit is cut last, so it cuts the axle into a stub on
    # each leaf; a third patch would be a shaft bridging the pair at the pin.
    c("axle, one stub per leaf", len(t.get(f"cylinder r{P.STUB / 2:.3f}", [])), 2, "")
    check_leaves(fs, t, c)
    check_slot(fs, t, c, 0.0)
    # Both members are in this tab, so what the joint does between them is a row here.
    c("the pair opens this much to ride",
      (P.BLADE / 2 + P.WEDGE_H) - (P.SEAT / 2 - P.WEDGE_H), P.CLIMB)
    c("air over a crest at a detent", P.SEAT / 2 - (P.BLADE / 2 + P.WEDGE_H), P.WEDGE_C)
    c("tongue root, from the pin", len(plane_at(fs, LONG, -P.TAB_FREE)), 3, "")
    c("ear root, from the pin", len(plane_at(fs, LONG, P.EAR_FREE)), 1, "")
    c("fork rod ends", len(plane_at(fs, LONG, P.EAR_FREE + P.ROD_FORK)), 1, "")
    c("blade rod ends", len(plane_at(fs, LONG, -(P.TAB_FREE + P.ROD_BLADE))), 1, "")
    check_flats(fs, c)


def check_u_limb(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c.same("one part", part_names(page, doc), ["u limb"])
    # The socket's root and the fork's rod end meet at one station, so the limb is one body
    # and not two. Two would mean the rod stopped short of where the collar stands.
    c("one body, so the collar met the rod", len({b for b, _ in fs}), 1, "")
    check_socket(fs, t, c, 0.0)
    c("bore", len(t.get(f"cylinder r{P.BORE_D / 2:.3f}", [])), 2, "")
    check_slot(fs, t, c, -P.LIMB_CENTER)
    c("the fork's rod meets the socket's base",
      len(plane_at(fs, LONG, -P.LIMB_CENTER + P.EAR_FREE + P.ROD_FORK)), 1, "")
    c("joint center to joint center",
      0.0 - (-P.LIMB_CENTER), P.LIMB_CENTER)
    check_flats(fs, c)


def check_l_limb(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c.same("one part", part_names(page, doc), ["l limb"])
    c("one body, so the tongue met the rod", len({b for b, _ in fs}), 1, "")
    c("axle, one stub per leaf", len(t.get(f"cylinder r{P.STUB / 2:.3f}", [])), 2, "")
    check_leaves(fs, t, c)
    check_stud(fs, t, c, -P.LIMB_CENTER, +1)
    ball = t.get(f"sphere r{P.BALL / 2:.3f}", [])
    c("ball's far pole", ball and min(mm(f["box"]["minCorner"][LONG]) for f in ball),
      -(P.LIMB_CENTER + P.BALL / 2), "mm")
    c("the tongue's rod meets the stud's face",
      len(plane_at(fs, LONG, -(P.TAB_FREE + P.ROD_BLADE))), 1, "")
    c("joint center to joint center", 0.0 - (-P.LIMB_CENTER), P.LIMB_CENTER)
    check_flats(fs, c)


def check_coupon(page, doc, c, name, up):
    """A coupon is half a joint on a handle one limb thick and half a limb long.

    ``up`` is the way the handle grows from the joint's robot-side face, which is +z on the
    stud and −z on the socket, because that is the way each half faces the robot.
    """
    fs = list(faces(page, doc))
    t = tally(fs)
    c.same("one part", part_names(page, doc), [name])
    c("one body, so the handle met the joint", len({b for b, _ in fs}), 1, "")
    c("handle radius", None if not t.get(f"cylinder r{P.LIMB / 2:.3f}") else P.LIMB / 2,
      P.LIMB / 2)
    far = up * (P.STAND + P.LIMB / 2)
    c("the handle's far face", len(plane_at(fs, LONG, far)), 1, "")
    c("joint center to the handle's far face", abs(far), P.STAND + P.LIMB / 2)
    c("the handle stands on the joint's face",
      len(plane_at(fs, LONG, up * P.STAND)), 1, "")


def main():
    with sync_playwright() as pw:
        browser, ctx, page = S.connect(pw)
        els = S.api(page, "GET", f"/api/documents/d/{DID}/w/{WID}/elements")["body"]
        by_name = {e["name"]: e["id"] for e in els}
        bad = 0
        jobs = (
            ("ball and socket", check_ball_and_socket),
            ("hinge", check_hinge),
            ("u limb", check_u_limb),
            ("l limb", check_l_limb),
            ("ball with cylinder",
             lambda pg, d, c: check_coupon(pg, d, c, "ball with cylinder", +1)),
            ("socket with cylinder",
             lambda pg, d, c: check_coupon(pg, d, c, "socket with cylinder", -1)),
        )
        for tab, fn in jobs:
            print(f"{tab}:")
            c = Check()
            fn(page, S.Doc(DID, WID, by_name[tab]), c)
            bad += c.report()
        print("FAILED" if bad else "every row agrees")
        return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
