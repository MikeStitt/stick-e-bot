"""Check that no interim capture, build output or outsized file is tracked.

Three rules, which are the three the Constitution's *Capture is out* gate asks
for:

  capture     no tracked raster image or video under `.docs/experiments/runs/`,
              which is where a take's frames would land. They go to the session
              scratchpad instead, and reach git only by being placed on a page
  build       Sphinx renders build/ from source/; a tracked one is a second copy
              that goes stale
  size        nothing here legitimately exceeds the ceiling, so the file that
              does is an accident

`.gitignore` asks for the first of those; this is what checks it happened,
including for files added with `git add -f`. The archive holds 13,962
screenshots, 1,837 MB, all of it under that one path, because capture and
publication shared a directory. A raster elsewhere is allowed: an engineering
figure is not capture.

Prints one line per violation and exits non-zero if there are any.
"""

import re
import subprocess

from stickbot import repo_root
import sys

CEILING = 5 * 1024 * 1024

MEDIA = re.compile(r"\.(png|jpg|jpeg|gif|bmp|tiff?|mp4|mov|webm)$", re.I)
CAPTURE = re.compile(r"^\.docs/experiments/runs/")

BUILD_OUTPUT = re.compile(r"^(instructions|\.docs/reviews)/[^/]+/build/")


def tracked() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True, cwd=repo_root()
    ).stdout
    return out.splitlines()


def main() -> int:
    total = 0
    for path in tracked():
        if MEDIA.search(path) and CAPTURE.match(path):
            print(f"{path}: interim capture; frames belong in the scratchpad")
            total += 1
        if BUILD_OUTPUT.match(path):
            print(f"{path}: Sphinx output, rendered from source/")
            total += 1
        full = repo_root() / path
        if full.exists() and full.stat().st_size > CEILING:
            mb = full.stat().st_size / 1048576
            print(f"{path}: {mb:.1f} MB, over the {CEILING // 1048576} MB ceiling")
            total += 1
    if total:
        print(f"\n{total} violation(s). Untrack these, or change the rule on purpose.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
