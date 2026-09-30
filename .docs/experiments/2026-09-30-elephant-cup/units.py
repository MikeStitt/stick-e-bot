#!/usr/bin/env python3
"""Set the workspace length unit to millimeters, with draft9p5's GUI drive.

A new document displays inches. The geometry is the same either way, because every
expression carries its unit; this decides what the variable titles read.

    uv run python .docs/experiments/2026-09-30-elephant-cup/units.py
"""

import importlib.util
import json
import sys
from pathlib import Path

from stickbot import onshape_session as S
from stickbot import repo_root

HERE = Path(__file__).parent
IDS = json.loads((HERE / "ids.json").read_text())
SOURCE = repo_root() / ".docs/experiments/runs/2026-09-18-draft9p5/scripts/a0_units.py"

spec = importlib.util.spec_from_file_location("a0_units", SOURCE)
a0_units = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a0_units)
a0_units.DOC = S.Doc(IDS["did"], IDS["wid"], IDS["eid"])

if __name__ == "__main__":
    sys.exit(a0_units.main())
