#!/usr/bin/env python3
"""Build the settled hinge, and the two limbs that carry it, in stickbot-draft9p1p2.

Mike's message of 2026-08-30 lifts the standing "GUI only for geometry" rule for this
document, so every feature here is written through the REST feature API. The numbers all
come from ``instructions/robot-guide/make_plans.py``; nothing is typed twice.

The frame. The pin is world X, the limb is world Y, the chord is world Z, and the pin sits
at the origin. That follows from the slit: ``hinge_spring`` slices the tongue along the
axis the joint opens, so the two leaves are separated along the pin and the tongue is a
tuning fork. The three default planes then fall out as

    Right JEC   sketch (u, v) = (limb, chord)   profiles, the tooth ring, the bore
    Front JCC   sketch (u, v) = (pin,  chord)   the Ø LIMB rod, and everything round it
    Top   JDC   sketch (u, v) = (pin,  limb)    the slot's land section, and the slit

Every part is a profile prism cut back to the rod: sketch the outline on Right, extrude it
across the pin, then intersect with the limb section drawn on Front, which is the Ø LIMB
circle with its top and bottom cut away flat so the part prints on a face. That is why no
fillet appears anywhere; the rounding is the rod.

What the model does not carry. Eight variables drive the feature parameters that have a
length in them, and the sketch geometry is generated from the same numbers by this script.
Changing a driving dimension means re-running this, not editing in Onshape.
"""
from __future__ import annotations

import math
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "instructions" / "robot-guide"))

from tools import onshape_session as S       # noqa: E402
import make_plans as P                       # noqa: E402

MM = 1 / 25.4          # sketch coordinates are inches; this converts a millimeter

DOC_NAME = "stickbot-draft9p1p2"
TOP, FRONT, RIGHT = "JDC", "JCC", "JEC"

# The eight lengths a feature parameter asks for by name.
VARIABLES = [
    ("limb", P.LIMB), ("blade", P.BLADE), ("tab_free", P.TAB_FREE),
    ("ear_free", P.EAR_FREE), ("rod_fork", P.ROD_FORK), ("rod_blade", P.ROD_BLADE),
    ("stub_proud", P.STUB_PROUD), ("tooth_proud", P.TOOTH_PROUD),
]


# ------------------------------------------------------------------ feature helpers

def variable(name, mm):
    return {
        "type": 134, "typeName": "BTMFeature",
        "message": {
            "featureType": "assignVariable", "name": f"#{name}", "suppressed": False,
            "parameters": [
                S.enum_param("mode", "VariableMode", "ASSIGNED"),
                S.enum_param("variableType", "VariableType", "LENGTH"),
                {"type": 149, "typeName": "BTMParameterString",
                 "message": {"parameterId": "name", "value": name}},
                S.qty("lengthValue", f"{mm:g} mm"),
            ],
        },
    }


def _drop(feature, *parameter_ids):
    ps = feature["message"]["parameters"]
    ps[:] = [p for p in ps if p["message"].get("parameterId") not in parameter_ids]
    return feature


def through(feature):
    """Blind depth out, through-all in. Every cut in this part studio wants it."""
    for p in feature["message"]["parameters"]:
        if p["message"].get("parameterId") == "endBound":
            p["message"]["value"] = "THROUGH_ALL"
    return _drop(feature, "depth")


def start_at(feature, expression, opposite=False):
    feature["message"]["parameters"] += [
        S.bool_param("startOffset", True),
        S.enum_param("startOffsetBound", "StartOffsetType", "BLIND"),
        S.qty("startOffsetDistance", expression),
        S.bool_param("startOffsetOppositeDirection", opposite),
    ]
    return feature


def draft_in(feature, angle="45 deg"):
    """Taper toward the far end, which is what makes a tooth a truncated cone."""
    feature["message"]["parameters"] += [
        S.bool_param("hasDraft", True),
        S.qty("draftAngle", angle),
        S.bool_param("draftPullDirection", True),
    ]
    return feature


def only(feature, *part_ids):
    """Confine a boolean to named parts, so one member's cuts leave the other alone."""
    _drop(feature, "defaultScope")
    feature["message"]["parameters"] += [
        S.bool_param("defaultScope", False),
        S.query_list("booleanScope", S.q_geom(*part_ids)),
    ]
    return feature


# ------------------------------------------------------------------ reading it back

def bodies(page, doc):
    """Every solid body, as {geometryId: (min, max)} in millimeters."""
    out = {}
    res = S.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")
    for b in res["body"]["bodies"]:
        lo, hi = [1e9] * 3, [-1e9] * 3
        for f in b.get("faces", []):
            box = f.get("box") or {}
            for i in range(3):
                lo[i] = min(lo[i], box["minCorner"][i])
                hi[i] = max(hi[i], box["maxCorner"][i])
        out[b["id"]] = ([round(c * 1000, 4) for c in lo], [round(c * 1000, 4) for c in hi])
    return out


def add(page, doc, feature, note=""):
    fid = S.add_feature(page, doc, feature)["feature"]["message"]["featureId"]
    print(f"  + {feature['message']['name']:22s} {fid} {note}")
    return fid


# ------------------------------------------------------------------ the sketches

def sk_limb(name="limb section"):
    """The Ø LIMB rod with its top and bottom cut away flat, on Front. Three features use
    it: two intersects and a rod.

    Front is (pin, chord) and the chord is world Z, so the two cuts are at chord ± FLAT and
    what survives of the circle is the two arcs the pin runs through. The limb is printed in
    this orientation, so the cuts are what it lies on: FLAT is the land's outer corner, and
    the same right triangle makes each flat face SEAT wide, against the line a round rod
    would touch the bed along. Nothing is taken off the ear, which reaches only that far.
    """
    r, f = P.LIMB / 2, P.FLAT
    h = math.sqrt(r * r - f * f)          # half a flat face, which is SEAT / 2
    a = math.asin(f / r)                  # where a cut meets the arc, off the pin axis
    return S.sketch(name, FRONT, [
        S.line("r1", -h * MM, -f * MM, h * MM, -f * MM),
        S.arc("r2", 0, 0, r * MM, -a, a),
        S.line("r3", h * MM, f * MM, -h * MM, f * MM),
        S.arc("r4", 0, 0, r * MM, math.pi - a, math.pi + a),
    ])


def sk_fork_profile():
    """The fork's outline on Right: a rod that stops at the slot's root, rounded on NOSE
    about the pin at the other end."""
    r, top = P.NOSE, P.EAR_FREE + P.ROD_FORK
    return S.sketch("fork profile", RIGHT, [
        S.line("f1", 0, -r * MM, top * MM, -r * MM),
        S.line("f2", top * MM, -r * MM, top * MM, r * MM),
        S.line("f3", top * MM, r * MM, 0, r * MM),
        S.arc("f4", 0, 0, r * MM, math.pi / 2, 3 * math.pi / 2),
    ])


def sk_slot():
    """The slot, on Top, drawn as one section: relieved to SLOT, raised to SEAT over the
    land, and ramped between the two. The outboard ramp runs off the ear's round end."""
    s, seat, land, cham = P.SLOT / 2, P.SEAT / 2, P.LAND, P.LAND_CHAM
    root, out = P.EAR_FREE, -(P.NOSE + 1)
    pts = [(s, root), (s, land + cham), (seat, land), (seat, -land),
           (s, -(land + cham)), (s, out)]
    pts = pts + [(-u, v) for u, v in reversed(pts)]
    ents = [S.line(f"s{i}", a[0] * MM, a[1] * MM, b[0] * MM, b[1] * MM)
            for i, (a, b) in enumerate(zip(pts, pts[1:] + pts[:1]))]
    return S.sketch("slot profile", TOP, ents)


def sk_ring(name, diameter):
    """One ring of TEETH circles on Right, at BUMP_R. The valleys and the teeth share it,
    so a tooth cannot land anywhere but in a valley."""
    ents = []
    for k in range(P.TEETH):
        a = math.radians(k * P.STEP)
        ents.append(S.circle(f"t{k}", P.BUMP_R * math.cos(a) * MM,
                             P.BUMP_R * math.sin(a) * MM, diameter / 2 * MM))
    return S.sketch(name, RIGHT, ents)


def sk_tongue_profile():
    """The blade's outline on Right: the tongue, rooted where its own rod stops."""
    r, root = P.NOSE, -P.TAB_FREE
    return S.sketch("tongue profile", RIGHT, [
        S.line("g1", root * MM, -r * MM, 0, -r * MM),
        S.arc("g2", 0, 0, r * MM, -math.pi / 2, math.pi / 2),
        S.line("g3", 0, r * MM, root * MM, r * MM),
        S.line("g4", root * MM, r * MM, root * MM, -r * MM),
    ])


def sk_slit():
    """The relief slit, on Top. It runs past the tongue's tip so it opens there, and stops
    at the tongue's root, which is where the rod begins."""
    return S.sketch("slit", TOP, S.rect(
        "sl", -P.SLIT / 2 * MM, -P.TAB_FREE * MM, P.SLIT / 2 * MM, (P.NOSE + 1) * MM))


# ------------------------------------------------------------------ the two members

def build_fork(page, doc, limb_sketch, rod_top=None, keep_teeth=True):
    """The fork: a rod that stops at the slot's root, with the slot cut out of its end.

    Nothing else exists when this runs, so every boolean here is unscoped.
    """
    fid = add(page, doc, sk_fork_profile())
    add(page, doc, S.extrude("fork blank", fid, "NEW", "#limb", symmetric=True))
    add(page, doc, through(S.extrude("fork rod", limb_sketch, "INTERSECT", "1 mm",
                                     symmetric=True)))
    sid = add(page, doc, sk_slot())
    add(page, doc, through(S.extrude("slot", sid, "REMOVE", "1 mm", symmetric=True)))
    bid = add(page, doc, S.sketch("bore", RIGHT, [S.circle("b", 0, 0, P.BORE_D / 2 * MM)]))
    add(page, doc, through(S.extrude("bore", bid, "REMOVE", "1 mm", symmetric=True)))
    vid = add(page, doc, sk_ring("valleys", P.VALLEY_D))
    add(page, doc, through(S.extrude("valleys", vid, "REMOVE", "1 mm", symmetric=True)))


def build_blade(page, doc, limb_sketch, part):
    """The blade: a slit tongue on its own rod, with an axle and two rings of teeth.

    ``part`` is the blade's own body, and every boolean is confined to it, or the fork
    loses its slot to the tongue and its valleys to the teeth.

    It ends with ``axle_and_slit``, which is where the order matters.
    """
    tid = add(page, doc, sk_tongue_profile())
    add(page, doc, S.extrude("tongue blank", tid, "NEW", "#blade", symmetric=True))
    add(page, doc, only(through(S.extrude("tongue rod", limb_sketch, "INTERSECT", "1 mm",
                                          symmetric=True)), part()))
    add(page, doc, only(start_at(S.extrude("blade rod", limb_sketch, "ADD", "#rod_blade"),
                                 "#tab_free"), part()))
    rid = add(page, doc, sk_ring("teeth", P.CONE_D))
    # The extrude's direction and the starting offset's have separate flips, and the ring
    # on the far leaf needs both: start at the far face, then grow away from the tongue.
    for name, flip in (("teeth out", False), ("teeth in", True)):
        add(page, doc, only(draft_in(start_at(
            S.extrude(name, rid, "ADD", "#tooth_proud", opposite=flip),
            "#blade / 2", opposite=flip)), part()))
    axle_and_slit(page, doc, part)


def axle_and_slit(page, doc, part):
    """The axle, and then the slit that cuts it in two.

    The slit goes last, so everything standing in its way is cut with it. That is what
    makes the axle a stub on each leaf rather than a shaft across the pair. A shaft would
    tie the two leaves together at the pin, and ``hinge_spring`` presses the axle against
    a leaf whose only support is its root, free to bend at that station: see ``press``,
    which asks station 0.0 to open by ``engage`` on ``lev_leaf = 0 + tab_free``.
    """
    aid = add(page, doc, S.sketch("axle", RIGHT, [S.circle("a", 0, 0, P.STUB / 2 * MM)]))
    add(page, doc, only(S.extrude("axle", aid, "ADD", "#blade + 2 * #stub_proud",
                                  symmetric=True), part()))
    sid = add(page, doc, sk_slit())
    add(page, doc, only(through(S.extrude("slit", sid, "REMOVE", "1 mm", symmetric=True)),
                        part()))


def report(page, doc):
    for bid, (lo, hi) in bodies(page, doc).items():
        print(f"    {bid:8s} x {lo[0]:8.3f} {hi[0]:8.3f}   y {lo[1]:8.3f} {hi[1]:8.3f}"
              f"   z {lo[2]:8.3f} {hi[2]:8.3f}")


def open_doc(page):
    doc = S.find_document(page, DOC_NAME)
    if doc is None:
        raise RuntimeError(f"{DOC_NAME} is missing")
    return doc


# ------------------------------------------------------------------ the two ends

def cyl_face(page, doc, radius_mm, body=None):
    """One cylindrical face of a given radius, which is how a revolve gets its axis.

    The rod, the collar and the stalk are all turned about the limb axis, so any of their
    faces names that axis. Take the id before a cut splits the face into patches.
    """
    res = S.api(page, "GET", f"/api/partstudios/{doc.path}/bodydetails")
    found = [f["id"] for b in res["body"]["bodies"] if body in (None, b["id"])
             for f in b["faces"]
             if f["surface"]["type"] == "cylinder"
             and abs(f["surface"]["radius"] * 1000 - radius_mm) < 1e-6]
    if not found:
        raise RuntimeError(f"no Ø{2 * radius_mm:g} cylinder to turn about")
    return found[0]


def half_disc(name, center_mm, radius_mm):
    """A half disc on Right, flat side on the limb axis. Revolved, it is a sphere."""
    c, r = center_mm * MM, radius_mm * MM
    return S.sketch(name, RIGHT, [
        S.line("d1", c - r, 0, c + r, 0),
        S.arc("d2", c, 0, r, 0, math.pi),
    ])


def sk_collar_section():
    """The collar's outside, a Ø 2 × COLLAR_R circle on Front."""
    return S.sketch("collar section", FRONT, [S.circle("c", 0, 0, P.COLLAR_R * MM)])


def sk_slits():
    """The four relief slits, as rectangles on Front, extruded down from the rim.

    Each runs from SLIT_IN out past the collar, so the cut is a slot for all of its depth
    and opens into the cavity where it bottoms out. SLIT_IN is what keeps that true; see
    make_plans, where it is derived from how wide the cavity still is at the slit's floor.
    """
    ents = []
    for k in range(4):
        turn = math.radians(90 * k)
        cos, sin = round(math.cos(turn)), round(math.sin(turn))
        near, far, half = P.SLIT_IN, P.COLLAR_R + 1, P.SLIT_W / 2
        pts = [(near, -half), (far, -half), (far, half), (near, half)]
        pts = [((u * cos - v * sin) * MM, (u * sin + v * cos) * MM) for u, v in pts]
        ents += [S.line(f"q{k}{i}", a[0], a[1], b[0], b[1])
                 for i, (a, b) in enumerate(zip(pts, pts[1:] + pts[:1]))]
    return S.sketch("slits", FRONT, ents)


def build_socket(page, doc, root=None, center=None, part=None):
    """A socket standing on a face: a collar, a spherical cavity, and four slits.

    ``root`` is the face the collar grows from and ``center`` is where the ball's center
    will sit; both are stations on the limb axis. The mouth is not cut. The cavity's
    center sits GRIP below the rim, so where the sphere breaks the rim face it leaves an
    opening MOUTH across, and that is the mouth.
    """
    root = P.EAR_FREE + P.ROD_FORK if root is None else root
    center = P.LIMB_CENTER if center is None else center
    scope = (lambda f: f) if part is None else (lambda f: only(f, part()))
    cid = add(page, doc, sk_collar_section())
    add(page, doc, scope(start_at(
        S.extrude("collar", cid, "ADD", f"{P.COLLAR_PROUD:g} mm", opposite=True),
        f"{root:g} mm", opposite=True)))
    axis = cyl_face(page, doc, P.COLLAR_R)
    hid = add(page, doc, half_disc("cavity profile", center, P.CAVITY))
    add(page, doc, scope(S.revolve("cavity", hid, axis, "REMOVE")))
    rim = root + P.COLLAR_PROUD
    sid = add(page, doc, sk_slits())
    add(page, doc, scope(start_at(
        S.extrude("slits", sid, "REMOVE", f"{P.SLIT_D:g} mm"),
        f"{rim:g} mm", opposite=True)))


def build_ball(page, doc, root=None, center=None, part=None):
    """A ball stud growing off a face: a stalk STAND long, and a ball on the end of it.

    ``root`` is the face it grows from; the stalk always runs toward the joint, which is
    the falling direction on the limb axis. ``center`` is where the ball's center sits.
    """
    root = -(P.TAB_FREE + P.ROD_BLADE) if root is None else root
    center = -P.LIMB_CENTER if center is None else center
    scope = (lambda f: f) if part is None else (lambda f: only(f, part()))
    sid = add(page, doc, S.sketch("stalk section", FRONT,
                                  [S.circle("s", 0, 0, P.STALK / 2 * MM)]))
    add(page, doc, scope(start_at(
        S.extrude("stalk", sid, "ADD", f"{P.STAND:g} mm"),
        f"{abs(root):g} mm", opposite=root > 0)))
    axis = cyl_face(page, doc, P.STALK / 2, body=part and part())
    hid = add(page, doc, half_disc("ball profile", center, P.BALL / 2))
    add(page, doc, scope(S.revolve("ball", hid, axis, "ADD")))


# ------------------------------------------------------------------ the tabs

def part_studio(page, doc, name):
    """A new Part Studio in the same document, returned ready to build in."""
    res = S.api(page, "POST", f"/api/partstudios/d/{doc.did}/w/{doc.wid}", {"name": name})
    if not res["ok"]:
        raise RuntimeError(f"could not make {name}: {res['status']}")
    return S.Doc(doc.did, doc.wid, res["body"]["id"])


def rename_element(page, doc, name):
    return S.api(page, "POST", f"/api/elements/d/{doc.did}/w/{doc.wid}/e/{doc.eid}"
                 f"/update", {"name": name})


def rename_part(page, doc, part_id, name):
    return S.api(page, "POST", f"/api/parts/d/{doc.did}/w/{doc.wid}/e/{doc.eid}"
                 f"/pid/{part_id}/metadata",
                 {"properties": [{"name": "Name", "value": name}]})


def variables_and_rod(page, doc):
    """What every tab starts with: the eight driving lengths and the Ø LIMB circle."""
    for name, mm in VARIABLES:
        add(page, doc, variable(name, mm), f"= {mm:g} mm")
    return add(page, doc, sk_limb())
