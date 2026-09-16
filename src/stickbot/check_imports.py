"""Check that no tracked Python finds its imports by editing `sys.path`.

The package is installed into the environment by `uv sync`, so `import stickbot`
resolves the same way from any directory and any checkout. Editing that list at
run time undoes it: what gets imported starts depending on where the file sits or
where the command was run, and the failure is silent — the wrong module imports
fine.

This file cannot spell the pattern it looks for in its own prose, because it
scans every tracked module including itself. The regex below is the only place
the three names appear.

That is not hypothetical here. Thirteen of draft9p4's scripts inserted an
absolute path to a different checkout, so they read one repository's modules
while writing their output into it, and nothing said so.

Prints one line per violation and exits non-zero if there are any.
"""

import re
import subprocess
import sys

from stickbot import repo_root

MUTATION = re.compile(r"\bsys\.path\.(insert|append|extend)\b")

# Runs finished before the package existed. Their scripts are a record of what
# was driven, not code anyone runs again, and the paths they name are part of
# that record. The Constitution's probe-script escape hatch covers them.
BEFORE_THE_PACKAGE = (
    ".docs/experiments/runs/2026-08-16-human-run1/",
    ".docs/experiments/runs/2026-08-23-draft9p0/",
    ".docs/experiments/runs/2026-08-25-draft9p1/",
    ".docs/experiments/runs/2026-08-26-draft9p1p1/",
)


def tracked_python() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--", "*.py"],
        capture_output=True,
        text=True,
        check=True,
        cwd=repo_root(),
    ).stdout
    return [p for p in out.splitlines() if not p.startswith(BEFORE_THE_PACKAGE)]


def main() -> int:
    total = 0
    for path in tracked_python():
        with open(repo_root() / path, encoding="utf-8") as fh:
            for n, line in enumerate(fh, start=1):
                if MUTATION.search(line):
                    print(f"{path}:{n}: {line.strip()}")
                    total += 1
    if total:
        print(
            f"\n{total} line(s) edit sys.path. Import from the installed package "
            f"instead, and use stickbot.repo_root() for paths into the tree."
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
