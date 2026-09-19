#!/usr/bin/env python3
"""Phase B, Ring 2 — the brief's acceptance checks, measured off the model.

    uv run python .../scripts/b_accept.py "ball and socket" [version_id]

Every expected number is imported from `make_plans.py`, never copied. Given a
version id it measures that version instead of the workspace, which is how a tab
is checked while `/features` is rate limited: `bodydetails` and `massproperties`
are different endpoint families and a version's read paths answer.

A check that the tab cannot answer says so rather than passing quietly.
"""

from __future__ import annotations

import json
import math
import sys

from playwright.sync_api import sync_playwright

from stickbot import make_plans as P
from stickbot import onshape_session as S
from stickbot import repo_root

DID = "2f08b54d795df0ee6b72e321"
WID = "1d8e4c837228c90bab9ff062"
OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"
ELEMENTS = {e["name"]: e["id"] for e in json.loads(
    (OUT / "elements.json").read_text())["elements"]}

MM, MM2, MM3 = 1e3, 1e6, 1e9
NEAR = 5e-4      # millimeters, or square or cubic millimeters


def faces(page, path):
    """Every body's faces, in millimeters."""
    body = S.api(page, "GET", f"/api/partstudios/{path}/bodydetails")["body"]
    out = {}
    for b in body["bodies"]:
        rows = []
        for f in b["faces"]:
            s = f["surface"]
            rows.append({"id": f["id"], "area": f["area"] * MM2, "type": s["type"],
                         "radius": (s.get("radius") or 0) * MM,
                         "origin": [v * MM for v in (s.get("origin") or [0, 0, 0])],
                         "box": {k: [v * MM for v in c]
                                 for k, c in (f.get("box") or {}).items()}})
        out[b["id"]] = rows
    return out


def volumes(page, path):
    body = S.api(page, "GET", f"/api/partstudios/{path}/massproperties")["body"]
    return {k: v["volume"][0] * MM3 for k, v in (body.get("bodies") or {}).items()
            if isinstance(v, dict) and v.get("volume")}


def check(rows, what, saw, want, unit="mm"):
    ok = saw is not None and abs(saw - want) <= NEAR
    rows.append((what, saw, want, unit, ok))


def ball_and_socket(page, path):
    by_body = faces(page, path)
    vol = volumes(page, path)
    rows = []

    stud = next((b for b, fs in by_body.items()
                 if any(f["type"] == "sphere" and abs(f["radius"] - P.BALL / 2) < 1e-6
                        for f in fs)), None)
    socket = next(b for b in by_body if b != stud)

    sphere = next(f for f in by_body[stud] if f["type"] == "sphere")
    stalk = next(f for f in by_body[stud] if f["type"] == "cylinder")
    top = next(f for f in by_body[stud] if f["type"] == "plane")
    cavity = next(f for f in by_body[socket] if f["type"] == "sphere")
    collar = next(f for f in by_body[socket] if f["type"] == "cylinder")
    root = max((f for f in by_body[socket] if f["type"] == "plane"),
               key=lambda f: f["area"])

    check(rows, "ball diameter", 2 * sphere["radius"], P.BALL)
    check(rows, "ball unchanged by the subtract: its sphere is one face",
          float(sum(1 for f in by_body[stud] if f["type"] == "sphere")), 1.0, "faces")
    check(rows, "stalk diameter", 2 * stalk["radius"], P.STALK)
    check(rows, "stalk top face area", top["area"],
          math.pi * (P.STALK / 2) ** 2, "mm^2")
    check(rows, "collar diameter", 2 * collar["radius"], 2 * P.COLLAR_R)
    check(rows, "socket root face area", root["area"],
          math.pi * P.COLLAR_R ** 2, "mm^2")
    check(rows, "cavity spherical face radius", cavity["radius"], P.CAVITY)

    # The mouth is where the cavity sphere crosses the rim plane, so it follows
    # from the two and is not a face of its own.
    rim_z = P.GRIP
    mouth = 2 * math.sqrt(cavity["radius"] ** 2 - rim_z ** 2)
    check(rows, "mouth diameter, cavity sphere across the rim plane", mouth, P.MOUTH)

    # Four slits, three faces each: two walls and an end.
    walls = [f for f in by_body[socket]
             if f["type"] == "plane" and abs(f["area"] - 12.992) < 0.5]
    ends = [f for f in by_body[socket]
            if f["type"] == "plane" and abs(f["area"] - 5.1693) < 0.5]
    check(rows, "slit walls", float(len(walls)), 8.0, "faces")
    check(rows, "slit ends", float(len(ends)), 4.0, "faces")

    stud_v = vol.get(stud)
    socket_v = vol.get(socket)
    want_stud = (4 / 3) * math.pi * (P.BALL / 2) ** 3 \
        + math.pi * (P.STALK / 2) ** 2 * P.STAND \
        - (math.pi * (P.STALK / 2) ** 2 * math.sqrt((P.BALL / 2) ** 2
                                                    - (P.STALK / 2) ** 2))
    rows.append(("`Ball stud` volume", stud_v, want_stud, "mm^3",
                 stud_v is not None and abs(stud_v - want_stud) < 1.0))
    rows.append(("`Socket body` volume", socket_v, None, "mm^3", None))
    return rows, {"stud_body": stud, "socket_body": socket,
                  "volumes": vol, "face_counts":
                  {b: len(f) for b, f in by_body.items()}}


def main(tab: str, version: str | None) -> int:
    eid = ELEMENTS[tab]
    path = f"d/{DID}/v/{version}/e/{eid}" if version else f"d/{DID}/w/{WID}/e/{eid}"
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        print("signed in as", S.require_signed_in(page))
        print(f"measuring `{tab}` at {'version ' + version if version else 'the workspace'}\n")
        rows, extra = {"ball and socket": ball_and_socket}[tab](page, path)
        browser.close()

    width = max(len(r[0]) for r in rows)
    failed = 0
    for what, saw, want, unit, ok in rows:
        shown = "-" if saw is None else f"{saw:.4f}"
        expect = "" if want is None else f"  want {want:.4f} {unit}"
        mark = {True: "ok", False: "DIFFERS", None: "recorded"}[ok]
        print(f"  {what:<{width}}  {shown:>12} {unit}{expect}   {mark}")
        failed += ok is False
    OUT.mkdir(parents=True, exist_ok=True)
    stem = tab.replace(" ", "-")
    (OUT / f"{stem}.acceptance.json").write_text(json.dumps(
        {"tab": tab, "version": version,
         "checks": [{"what": w, "saw": s, "want": t, "unit": u, "ok": o}
                    for w, s, t, u, o in rows], **extra}, indent=2) + "\n")
    print(f"\n{len(rows)} checks, {failed} differ")
    print(f"wrote {OUT / f'{stem}.acceptance.json'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None))
