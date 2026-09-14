"""Check that Markdown prose is wrapped at 100 columns.

The Quality Gate exempts tables, so a line starting with `|` is skipped. Fenced
code blocks are skipped too: a long command line cannot be wrapped without
changing what it says. So is a line holding one unbroken token — a URL or an
API path has no space to wrap at, and breaking it would break the thing.

Prints one line per violation and exits non-zero if there are any.
"""

import subprocess
import sys

LIMIT = 100

# Written by agents and tools, not by hand. Not prose, and not a gate.
SKIP_PREFIXES = (".docs/experiments/build-log/", ".docs/experiments/runs/", ".docs/experiments/inspect/")


def tracked_markdown() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--", "*.md"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [
        p for p in out.splitlines() if not p.startswith(SKIP_PREFIXES)
    ]


def violations(path: str) -> list[tuple[int, int]]:
    found = []
    in_fence = False
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, start=1):
            line = line.rstrip("\n")
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if in_fence or line.startswith("|"):
                continue
            if len(line.split()) == 1:
                continue
            if len(line) > LIMIT:
                found.append((n, len(line)))
    return found


def main() -> int:
    total = 0
    for path in tracked_markdown():
        for line_no, length in violations(path):
            print(f"{path}:{line_no}: {length} columns")
            total += 1
    if total:
        print(f"\n{total} line(s) over {LIMIT} columns.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
