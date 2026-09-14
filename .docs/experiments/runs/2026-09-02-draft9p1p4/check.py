#!/usr/bin/env python3
"""Read stickbot-draft9p1p4 back and check every settled number against make_plans.py.

Brought forward from ``../2026-08-30-draft9p1p2/check.py``. Two things changed with it.

The land is gone, so the slot's two rows are one. draft9p1p2 asked for a narrow land at
``SEAT`` near the mouth and a wider relieved slot at ``SLOT`` behind it; ``SLOT`` and
``LAND`` are no longer in the design source, and the slot is one wall at ``SEAT / 2`` from
the fork's tip to its root. The row now asks for exactly one plane a side and for that
plane to run the whole depth, which is what "no step anywhere in it" means to a face.

The frame turned. draft9p1p2 laid a limb along y with its leaves across x; draft9p1p4 lays
a limb along z with its leaves across y and its flats across x. Every station here reads in
this document's frame, so a row that looks transposed against the older script is the same
row.

Nothing is typed. Each row asks the model a question a face already answers and compares
the answer with the number ``make_plans`` derives.

    uv run --project . python -u .docs/experiments/runs/2026-09-02-draft9p1p4/check.py
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

DID, WID = "eca1f9c7feff156a3303d563", "3a7d66574eb06d933f843fae"
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


def check_leaves(fs, c, teeth=True, stubs=True):
    """What a blade's leaves measure, in the tab that holds them."""
    for sign in (1, -1):
        c(f"leaf face at y {sign * P.BLADE / 2:+g}",
          len(plane_at(fs, LEAF, sign * P.BLADE / 2)), 1, "")
        if teeth:
            c(f"tooth tops at y {sign * (P.BLADE / 2 + P.TOOTH_PROUD):+g}",
              len(plane_at(fs, LEAF, sign * (P.BLADE / 2 + P.TOOTH_PROUD))), P.TEETH, "")
        if stubs:
            c(f"axle end at y {sign * (P.BLADE / 2 + P.STUB_PROUD):+g}",
              len(plane_at(fs, LEAF, sign * (P.BLADE / 2 + P.STUB_PROUD))), 1, "")
        c(f"relief slit wall at y {sign * P.SLIT / 2:+g}",
          len(plane_at(fs, LEAF, sign * P.SLIT / 2)), 1, "")


def check_slot(fs, c, pin):
    """The fork's slot, after the land came out of the design source.

    One wall a side, at SEAT / 2, running the whole way from the fork's tip to its root. A
    second plane a side would be the step the land used to leave.
    """
    for sign in (1, -1):
        wall = plane_at(fs, LEAF, sign * P.SEAT / 2)
        c(f"slot wall at y {sign * P.SEAT / 2:+g}, and only one", len(wall), 1, "")
        if wall:
            lo, hi = span(wall, LONG)
            c(f"the wall at y {sign * P.SEAT / 2:+g} starts at the tip", lo, pin - P.NOSE)
            c(f"the wall at y {sign * P.SEAT / 2:+g} ends at the root", hi, pin + P.EAR_FREE)
    c("ear to tongue, a side", P.SEAT / 2 - P.BLADE / 2, P.GAP)
    c("axle engaged in the bore",
      (P.BLADE / 2 + P.STUB_PROUD) - P.SEAT / 2, P.STUB_PROUD - P.GAP)


def check_teeth(fs, t, c):
    c("teeth, both leaves", len(t.get(f"cone r{P.CONE_D / 2:.3f}", [])), 2 * P.TEETH, "")
    if t.get(f"cone r{P.CONE_D / 2:.3f}"):
        c("tooth half angle", math.degrees(
            t[f"cone r{P.CONE_D / 2:.3f}"][0]["surface"]["halfAngle"]), 45.0, "deg")
        c("tooth flat top area",
          min(f["area"] * 1e6 for f in
              plane_at(fs, LEAF, P.BLADE / 2 + P.TOOTH_PROUD)),
          math.pi * (P.TOOTH_FLAT / 2) ** 2, "mm2")


def check_valleys(t, c, pin):
    valleys = t.get(f"cylinder r{P.VALLEY_D / 2:.3f}", [])
    c("valleys, both ears", len(valleys), 2 * P.TEETH, "")
    if valleys:
        # Every valley's axis stands BUMP_R off the pin, which is the circle the teeth ride.
        s = valleys[0]["surface"]
        c("a valley stands off the pin", math.hypot(
            mm(s["origin"][FLATN]), mm(s["origin"][LONG]) - pin), P.BUMP_R)


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
    c.same("two parts", part_names(page, doc), ["Ball stud", "Socket body"])
    c("two bodies, and they are apart", len({b for b, _ in fs}), 2, "")
    check_socket(fs, t, c, 0.0)
    check_stud(fs, t, c, 0.0, +1)


def check_hinge(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c.same("two parts", part_names(page, doc), ["blade", "fork"])
    check_teeth(fs, t, c)
    check_valleys(t, c, 0.0)
    c("bores, both ears", len(t.get(f"cylinder r{P.BORE_D / 2:.3f}", [])), 2, "")
    # Two patches and not three. The slit is cut last, so it cuts the axle into a stub on
    # each leaf; a third patch would be a shaft bridging the pair at the pin.
    c("axle, one stub per leaf", len(t.get(f"cylinder r{P.STUB / 2:.3f}", [])), 2, "")
    check_leaves(fs, c)
    check_slot(fs, c, 0.0)
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
    check_valleys(t, c, -P.LIMB_CENTER)
    c("bore", len(t.get(f"cylinder r{P.BORE_D / 2:.3f}", [])), 2, "")
    check_slot(fs, c, -P.LIMB_CENTER)
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
    check_teeth(fs, t, c)
    c("axle, one stub per leaf", len(t.get(f"cylinder r{P.STUB / 2:.3f}", [])), 2, "")
    check_leaves(fs, c)
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
