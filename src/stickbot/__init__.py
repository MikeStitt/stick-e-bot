"""The course's Python: the checks, the Onshape client, and the design source.

Everything here is imported by name once the project is installed, which
`uv sync` does. Nothing needs `sys.path` touched, and nothing should touch it:
a script that does is finding its imports by where it happens to sit rather
than by what is installed, which is how a run once read one repository's
modules while writing into another's.

`repo_root()` is the one thing a module may need that the package cannot carry:
where the working tree is. Output paths and the checks' file lists are relative
to it, never to `__file__`.
"""

from __future__ import annotations

import functools
import pathlib
import subprocess

__all__ = ["repo_root"]


@functools.cache
def repo_root() -> pathlib.Path:
    """The working tree this package's source lives in.

    Found by walking up from this file, not by asking git about the current
    directory — an editable install puts this file inside the tree it belongs
    to, and answering from the working directory would let a command run in one
    checkout read or write another's. That is the failure this package exists to
    remove. Git is the fallback for a non-editable install, where `__file__` is
    in site-packages and says nothing about any tree.
    """
    for parent in pathlib.Path(__file__).resolve().parents:
        if (parent / ".git").exists():
            return parent
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        if out:
            return pathlib.Path(out)
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    raise RuntimeError("stickbot is not installed from a git working tree")
