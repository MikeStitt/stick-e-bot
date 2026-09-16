"""Check that no interim capture, build output or outsized file is tracked.

The previous repository committed 12,977 screenshots totaling 1,651 MB, because
capture and publication shared a directory and the rule against it lived in a
note nobody ran. `.gitignore` asks for the right thing; this is what checks that
it happened, including for files added with `git add -f`.

Three rules:

  images      a tracked raster image or video sits under a guide's
              source/images/, or it is interim capture that should have gone to
              the scratchpad
  build       Sphinx renders build/ from source/; a tracked one is a second copy
              that goes stale
  size        nothing here legitimately exceeds the ceiling, so the file that
              does is an accident

Prints one line per violation and exits non-zero if there are any.
"""

import os
import re
import subprocess

from stickbot import repo_root
import sys

CEILING = 5 * 1024 * 1024

MEDIA = re.compile(r"\.(png|jpg|jpeg|gif|bmp|tiff?|mp4|mov|webm)$", re.I)
PUBLISHED = re.compile(r"^instructions/[^/]+/source/images/")
BUILD_OUTPUT = re.compile(r"^(instructions|\.docs/reviews)/[^/]+/build/")


def tracked() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files"], capture_output=True, text=True, check=True, cwd=repo_root()
    ).stdout
    return out.splitlines()


def main() -> int:
    total = 0
    for path in tracked():
        if MEDIA.search(path) and not PUBLISHED.match(path):
            print(f"{path}: image outside instructions/<guide>/source/images/")
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
