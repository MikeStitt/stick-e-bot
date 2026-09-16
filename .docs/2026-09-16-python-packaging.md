# The Python becomes an installed package

Every script in this repository finds its imports by accident. `tools/` is thirty flat modules
that import each other by bare name, which works only because the interpreter happens to have put
that directory on `sys.path`; four live files patch `sys.path` by hand; and forty-seven archived
scripts hardcode an absolute path to a repository that is now the archive. This plan makes the code
a package installed into the `uv` virtual environment, so `import` resolves the way Python resolves
anything else.

## What is wrong now, measured

- **`pyproject.toml` says `package = false`.** The environment holds dependencies and nothing of
  ours, so there is nothing to import by name and no install step to get it wrong.
- **`tools/`'s thirty modules import each other bare** — `import onshape_session as api`, eight
  times across the set. That resolves only because running `python tools/foo.py` puts `tools/` at
  the front of `sys.path`. Import the same module any other way and it fails.
- **Four live files patch the path by hand**: `tools/browser.py`, `tools/onshape_gui.py`,
  `instructions/robot-guide/make_plans.py`, `.docs/reviews/hinge/make_figures.py`.
- **Forty-seven archived scripts hardcode `/Users/mikestitt/projects/first/2027/sponge`**, thirteen
  of them draft9p4's live P0 reads and spikes. Today those silently import the archive's `tools/`
  and write their output into the archive.
- **`ninja check` runs three of its four gates on `python3`, not on the environment**, and the
  fourth on `uv run --with textstat`. Four commands, three different Pythons.

## What being installed buys

`import` stops depending on where a file sits or how it was invoked. A script under
`.docs/experiments/runs/` and a gate under `tools/` reach the same code by the same name, the
environment is the single answer to *which copy*, and renaming or cloning the repository changes
nothing. It also makes the failure loud: an import that cannot be satisfied raises, where a wrong
`sys.path` silently supplies the wrong file.

## Decisions this plan takes

- **A `src/` layout, package `stickbot`.** `src/stickbot/` cannot be imported by being in the
  current directory, which is exactly the accident being removed. A flat `tools/` package would
  keep working for the wrong reason and hide the next mistake.
- **An editable install, through `uv sync`.** `package = true` plus a build backend; edits take
  effect with no reinstall step for anyone to forget.
- **The four gates become console scripts.** `ninja check` calls a name, not a path, and all four
  run in the environment.
- **`dictionary.txt` becomes package data**, so the spelling gate carries its own dictionary.
- **Archived run scripts are not rewritten.** The 915 under `2026-08-23-draft9p0/` and the rest
  point at a scratchpad that no longer exists; they are records of what was run, and the
  Constitution's probe-script escape hatch already exempts them. They will not work, and they do
  not work today.

## Open, and worth deciding before Phase 2

**Where `make_plans.py` lives.** It is the design source — the Variables table's arithmetic, the
stations, every plan drawing — and seven live documents name its path. It currently sits under
`instructions/`, which the Constitution reserves for students and teachers, and it is neither. It
has to become importable either way. Moving it to `src/stickbot/plans.py` fixes the folder-by-reader
question in the same stroke and costs seven reference updates plus `build.ninja`'s `plan` rule.
Leaving it where it is means the package imports out of `instructions/`, which is the odd shape.

## Phase 1 — the package exists and the gates run from it

- `src/stickbot/` with `__init__.py`; `tools/*.py` moved in with `git mv` so `git log --follow`
  answers.
- The eight bare cross-imports become `from stickbot import onshape_session as api`.
- `tools/browser.py` and `tools/onshape_gui.py` lose their `sys.path.insert`.
- `pyproject.toml` gains a build backend, drops `package = false`, gains four
  `[project.scripts]` entries, and declares `dictionary.txt` as package data. `textstat` moves from
  `--with` into the dev group.
- `build.ninja`'s four check rules call the console scripts.
- The gates find the repository root with `git rev-parse --show-toplevel` rather than assuming the
  working directory, since they are repo-scoped and are about to be callable from anywhere.
- `uv sync`, then `ninja check` green with every gate running in the environment.

## Phase 2 — the live callers stop patching paths

- `.docs/reviews/hinge/make_figures.py` and the nineteen run scripts from draft9p1p2 onward import
  `stickbot` and delete their `sys.path` lines.
- draft9p4's thirteen P0 reads and spikes lose their hardcoded absolute paths, and their `OUT` and
  `CAP` destinations become paths relative to the repository they run in rather than to the
  archive.
- `make_plans.py` moves or does not, per the open question above.

## Phase 3 — the rule becomes a gate

A fifth check: **a tracked `.py` outside `.docs/experiments/runs/` may not contain `sys.path`.**
One pass over `git ls-files`, the shape of `check_images.py`. Without it this plan is a tidy-up that
the next hurried script undoes; with it, the next hurried script fails at the gate.

Exercised the way the Constitution's maintenance step 5 asks: plant a `sys.path.insert` in a live
file, watch the gate refuse it, remove it, watch it pass.

## What does not change

The Onshape work, the guide, the design numbers, and every `.rst` and `.md` in the repository.
This is entirely about how Python finds Python.
