#!/usr/bin/env python3
"""Read stickbot-draft9p1p2 back and check every settled number against make_plans.py.

Nothing here is typed. Each row asks the model a question whose answer a face already
carries — a radius, a plane's station, an area, a cone's half angle — and compares it with
the number ``make_plans`` derives. A row that cannot be answered is a failure, not a skip.

    uv run --project . python -u .docs/experiments/runs/2026-08-30-draft9p1p2/check.py
"""
from __future__ import annotations

import collections
import math
import pathlib
import sys


from playwright.sync_api import sync_playwright   # noqa: E402
from stickbot import onshape_session as S            # noqa: E402
from stickbot import make_plans as P                            # noqa: E402

DID, WID = "2741f86a206bbf1af0dca541", "1f88a856b82f57bbace9bd09"
TOL = 1e-3


def faces(page, doc):
    res = S.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")
    for b in res["body"]["bodies"]:
        for f in b["faces"]:
            yield b["id"], f


def mm(x):
    return x * 1000


def near(a, b):
    return abs(a - b) < TOL


class Check:
    def __init__(self):
        self.rows = []

    def __call__(self, what, got, want, unit="mm"):
        ok = got is not None and near(got, want)
        self.rows.append((ok, what, got, want, unit))
        return ok

    def report(self):
        bad = 0
        for ok, what, got, want, unit in self.rows:
            g = "missing" if got is None else f"{got:10.4f}"
            print(f"  {'ok ' if ok else 'BAD'}  {what:44s} {g}  want {want:10.4f} {unit}")
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


def check_flats(fs, c):
    """The rod's top and bottom, cut away flat so the limb prints on a face.

    Every member here is its own profile intersected with the limb section, so the two cuts
    reach the ear and the tongue as well as the rod. FLAT is the circle's height at the slot
    wall, so the plane arrives tangent to the ear and takes nothing off it; what it removes
    is 1.1613 off the rod's crown and 0.0700 off the leaf's outer face.
    """
    lo = min(mm(f["box"]["minCorner"][2]) for _, f in fs)
    hi = max(mm(f["box"]["maxCorner"][2]) for _, f in fs)
    c("across the chord, so the rod is not round", hi - lo, P.LIMB_FLAT)
    seen = []
    for sign in (1, -1):
        band = plane_at(fs, 2, sign * P.FLAT)
        seen.append(len(band))
        # The flat's width is the other leg of the right triangle that sets FLAT, so the
        # limb lies on SEAT of bed rather than on the line a round rod touches along.
        width = None
        if band:
            width = (max(mm(f["box"]["maxCorner"][0]) for f in band)
                     - min(mm(f["box"]["minCorner"][0]) for f in band))
        c(f"the flat at z {sign * P.FLAT:+.4f} is {P.SEAT:g} across the pin", width, P.SEAT)
    # One sketch makes both cuts, so a top face without its bottom is a lopsided section
    # rather than an intersect that missed.
    c("as many faces on the bottom flat as the top", seen[1], seen[0], "")


def check_hinge(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c("teeth, both leaves", len(t.get(f"cone r{P.CONE_D / 2:.3f}", [])), 2 * P.TEETH, "")
    c("valleys, both ears", len(t.get(f"cylinder r{P.VALLEY_D / 2:.3f}", [])),
      2 * P.TEETH, "")
    c("tooth half angle", math.degrees(
        t[f"cone r{P.CONE_D / 2:.3f}"][0]["surface"]["halfAngle"]), 45.0, "deg")
    c("tooth flat top area", t[f"cone r{P.CONE_D / 2:.3f}"] and
      min(f["area"] * 1e6 for f in plane_at(fs, 0, P.BLADE / 2 + P.TOOTH_PROUD)),
      math.pi * (P.TOOTH_FLAT / 2) ** 2, "mm2")
    c("bores, both ears", len(t.get(f"cylinder r{P.BORE_D / 2:.3f}", [])), 2, "")
    # Two patches and not three. The slit is cut last, so it cuts the axle into a stub on
    # each leaf; a third patch would be a shaft bridging the pair at the pin, which ties
    # the leaves together where hinge_spring has them free to bend.
    c("axle, one stub per leaf", len(t.get(f"cylinder r{P.STUB / 2:.3f}", [])), 2, "")
    for sign in (1, -1):
        c(f"land at x {sign * P.SEAT / 2:+g}",
          len(plane_at(fs, 0, sign * P.SEAT / 2)), 1, "")
        c(f"relieved slot at x {sign * P.SLOT / 2:+g}",
          len(plane_at(fs, 0, sign * P.SLOT / 2)), 2 + P.TEETH, "")
        c(f"leaf face at x {sign * P.BLADE / 2:+g}",
          len(plane_at(fs, 0, sign * P.BLADE / 2)), 1, "")
        c(f"axle end at x {sign * (P.BLADE / 2 + P.STUB_PROUD):+g}",
          len(plane_at(fs, 0, sign * (P.BLADE / 2 + P.STUB_PROUD))), 1, "")
    c("slot root, from the pin", len(plane_at(fs, 1, P.EAR_FREE)), 1, "")
    c("fork rod ends", len(plane_at(fs, 1, P.EAR_FREE + P.ROD_FORK)), 1, "")
    c("blade rod ends", len(plane_at(fs, 1, -(P.TAB_FREE + P.ROD_BLADE))), 1, "")
    check_flats(fs, c)


def check_socket(fs, t, c, center):
    """Every row a socket answers, wherever it is built. ``center`` is its ball's center."""
    c("cavity", len(t.get(f"sphere r{P.CAVITY:.3f}", [])), 1, "")
    c("collar, so the wall is %.1f" % P.COLLAR_WALL,
      len(t.get(f"cylinder r{P.COLLAR_R:.3f}", [])), 1, "")
    rim = plane_at(fs, 1, center + P.GRIP)
    c("rim, one arc per finger", len(rim), 4, "")
    # What one finger's top face has to measure. The annulus runs from the mouth out to
    # the collar, and each of the four slits takes a strip SLIT_W across out of it.
    half = P.SLIT_W / 2
    strip = lambda r: half * math.sqrt(r ** 2 - half ** 2) + r ** 2 * math.asin(half / r)
    annulus = math.pi * (P.COLLAR_R ** 2 - (P.MOUTH / 2) ** 2)
    c("one finger's top face, so the mouth is Ø%.2f" % P.MOUTH,
      rim and sum(f["area"] for f in rim) * 1e6 / 4,
      (annulus - 4 * (strip(P.COLLAR_R) - strip(P.MOUTH / 2))) / 4, "mm2")
    # The floor is where the fingers are rooted, so this row is the free length that buys
    # the mouth its elastic opening. It goes as the square of this station's distance from
    # the rim; see tools/socket_spring.py.
    c("slit floors, so a finger is %.4f long" % P.SLIT_D,
      len(plane_at(fs, 1, center + P.GRIP - P.SLIT_D)), 4, "")
    # Each slit has to cut into the hollow rather than stop in the wall, or the mouth never
    # opens. Where it does, the cavity's widest surviving point is not its own equator but
    # the edge of a slit, and that is a number the sphere's own box reports.
    cav = t.get(f"sphere r{P.CAVITY:.3f}", [])
    c("the slits break into the cavity",
      cav and max(mm(f["box"]["maxCorner"][0]) for f in cav),
      math.sqrt(P.CAVITY ** 2 - (P.SLIT_W / 2) ** 2), "mm")


def check_u_limb(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    check_socket(fs, t, c, P.LIMB_CENTER)
    c("valleys, both ears", len(t.get(f"cylinder r{P.VALLEY_D / 2:.3f}", [])),
      2 * P.TEETH, "")
    # The socket's root and the fork's rod end meet at one station, so the limb is one body
    # and not two. Two would mean the rod stopped short of where the collar stands.
    c("one body, so the collar met the rod", len({b for b, _ in fs}), 1, "")
    check_flats(fs, c)


def check_ball_socket(page, doc, c):
    """The coupon pair: the socket that presses onto the stud, and nothing else."""
    fs = list(faces(page, doc))
    t = tally(fs)
    check_socket(fs, t, c, P.LIMB_CENTER)
    c("ball", len(t.get(f"sphere r{P.BALL / 2:.3f}", [])), 1, "")
    c("stalk", len(t.get(f"cylinder r{P.STALK / 2:.3f}", [])), 1, "")
    c("two parts, and they are apart", len({b for b, _ in fs}), 2, "")
    # The socket's stub is held while the ball is pressed in, so it has to start clear of
    # the collar's root rather than at it.
    c("the socket's stub end", len(plane_at(fs, 1, P.EAR_FREE + P.ROD_FORK - 12)), 1, "")
    # No flats row here. The two stubs are Ø LIMB, but the code that raised them is not in
    # build.py, so whether they come off the limb section or off a circle of their own is
    # not something this repository answers. Read the first run's stubs before adding one.


def check_l_limb(page, doc, c):
    fs = list(faces(page, doc))
    t = tally(fs)
    c("ball", len(t.get(f"sphere r{P.BALL / 2:.3f}", [])), 1, "")
    c("stalk", len(t.get(f"cylinder r{P.STALK / 2:.3f}", [])), 1, "")
    c("teeth, both leaves", len(t.get(f"cone r{P.CONE_D / 2:.3f}", [])), 2 * P.TEETH, "")
    c("axle, one stub per leaf", len(t.get(f"cylinder r{P.STUB / 2:.3f}", [])), 2, "")
    ball = t.get(f"sphere r{P.BALL / 2:.3f}", [])
    lo = ball and min(mm(f["box"]["minCorner"][1]) for f in ball)
    c("ball's far pole", lo, -(P.LIMB_CENTER + P.BALL / 2), "mm")
    check_flats(fs, c)


def main():
    with sync_playwright() as pw:
        browser, ctx, page = S.connect(pw)
        els = S.api(page, "GET", f"/api/documents/d/{DID}/w/{WID}/elements")["body"]
        by_name = {e["name"]: e["id"] for e in els}
        bad = 0
        for tab, fn in (("hinge", check_hinge), ("u limb", check_u_limb),
                        ("l limb", check_l_limb),
                        ("ball and socket", check_ball_socket)):
            print(f"{tab}:")
            c = Check()
            fn(page, S.Doc(DID, WID, by_name[tab]), c)
            bad += c.report()
        print("FAILED" if bad else "every row agrees")
        return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
