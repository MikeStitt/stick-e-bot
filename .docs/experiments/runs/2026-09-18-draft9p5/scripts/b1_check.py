#!/usr/bin/env python3
"""Phase B tab 1, Ring 2 — every `robot sizes` row, resolved in a Part Studio.

Two things at once. It checks each row against the number `make_plans.py`
computes, imported rather than copied; and because it asks a Part Studio rather
than the studio, it also proves the Part Studios can see the studio's rows at
all, which is what *Insert into all Part Studios and Assemblies* decides.

    uv run python .docs/experiments/runs/2026-09-18-draft9p5/scripts/b1_check.py
"""

from __future__ import annotations

import json
import sys

from playwright.sync_api import sync_playwright

from stickbot import make_plans as P
from stickbot import onshape_session as S
from stickbot import repo_root

DOC = S.Doc("2f08b54d795df0ee6b72e321", "1d8e4c837228c90bab9ff062",
            "1a8322899842a1934e85851d")          # the empty `ball and socket` tab
OUT = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/results"

# Each row, and the constant that says what it should be. `#wall` is
# `COLLAR_WALL` and `#collar` is `COLLAR_L`; the rest carry their own name.
EXPECTED = {
    "torsoH": P.TORSO_H, "torsoW": P.TORSO_W, "torsoD": P.TORSO_D,
    "limbCenter": P.LIMB_CENTER, "wall": P.COLLAR_WALL, "ball": P.BALL,
    "stand": P.STAND, "collar": P.COLLAR_L, "fit": P.FIT, "ballLoss": P.BALL_LOSS,
    "t_print": P.T_PRINT, "grip": P.GRIP, "limbD": P.LIMB, "blade": P.BLADE,
    "wedge_h": P.WEDGE_H, "wedge_c": P.WEDGE_C, "gap": P.GAP, "seat": P.SEAT,
    "blade_out": P.BLADE_OUT, "slot_deep": P.SLOT_DEEP, "tab_free": P.TAB_FREE,
    "ear_free": P.EAR_FREE, "flat": P.FLAT,
}

NEAR = 1e-6     # millimeters; the two are the same number computed two ways


def script_for(names):
    rows = ", ".join(f'"{n}"' for n in names)
    return """function(context is Context, queries is map)
{
    var s = "";
    for (var n in [%s])
    {
        s = s ~ n ~ "=" ~ toString(getVariable(context, n) / millimeter) ~ "\\n";
    }
    return s;
}""" % rows


def main() -> int:
    with sync_playwright() as p:
        browser, _ctx, page = S.connect(p)
        text = S.eval_fs(page, DOC, script_for(EXPECTED))
        browser.close()

    got = {}
    for line in text.splitlines():
        if "=" in line:
            name, value = line.split("=", 1)
            got[name.strip()] = float(value)

    bad = []
    for name, want in EXPECTED.items():
        saw = got.get(name)
        if saw is None or abs(saw - want) > NEAR:
            bad.append((name, want, saw))
    width = max(len(n) for n in EXPECTED)
    for name, want in EXPECTED.items():
        saw = got.get(name)
        mark = "" if saw is not None and abs(saw - want) <= NEAR else "   <- differs"
        print(f"  #{name:<{width}}  {saw!s:>18} mm   make_plans {want}{mark}")
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "robot-sizes.resolved.json").write_text(json.dumps(
        {"read_in": "ball and socket", "resolved_mm": got,
         "expected_mm": EXPECTED}, indent=2) + "\n")
    if bad:
        raise RuntimeError(f"{len(bad)} rows do not match make_plans: {bad}")
    print(f"\nall {len(EXPECTED)} rows resolve in `ball and socket` to the number "
          f"make_plans computes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
