"""Run codespell's en-GB dictionary over the prose we maintain.

codespell skips hidden directories, and this repository's contract lives in
`.claude/` and its working notes in `.docs/`. So the file list is assembled here
and passed by name rather than letting codespell walk the tree — that is the
whole reason this is a script and not one line in `build.ninja`.

`tools/dictionary.txt` carries the compounds the builtin dictionary does not
know. To quote a banned word deliberately, put `<!-- codespell:ignore -->` on
the line; a real mistake elsewhere on an unmarked line is still caught.
"""

import subprocess
import sys

DICTIONARY = "tools/dictionary.txt"

PATTERNS = ["*.md", "*.rst", "*.py"]

EXCLUDE = [
    # Agent and tool output, not prose anyone wrote.
    ":!.docs/experiments/build-log",
    ":!.docs/experiments/runs",
    ":!.docs/experiments/inspect",
    # Retired. The sponge guide is kept as the experiment it was, text and all.
    ":!.docs/experiments/spongebob-guide",
    # Another repository's constitution, copied in to diff against. Correcting
    # its spelling would corrupt the baseline it exists to be.
    ":!old-constitution.md",
]


def files() -> list[str]:
    out = subprocess.run(
        ["git", "ls-files", "--"] + PATTERNS + EXCLUDE,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return out.splitlines()


def main() -> int:
    paths = files()
    if not paths:
        print("Nothing to check.")
        return 0
    return subprocess.run(
        [
            "uvx",
            "codespell",
            "--builtin",
            "en-GB_to_en-US",
            "-D",
            "-",
            "-D",
            DICTIONARY,
            *paths,
        ]
    ).returncode


if __name__ == "__main__":
    sys.exit(main())
