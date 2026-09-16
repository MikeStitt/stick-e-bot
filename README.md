# stick-e-bot — a CAD course in Onshape

An introduction to Onshape, taught by building a printable stick figure robot
about 300 mm tall, with a ball-and-socket neck and hips and a ratcheting hinge at
the elbows and knees.

## Repository layout

```
CLAUDE.md                  The agreement to follow the Constitution, for AI assistants.
README.md                  This file.
build.ninja                `ninja check` — wrap, spelling, reading level and capture, in one
                           command. `ninja guides` builds the Sphinx sites.

instructions/              What a student or a teacher is handed.
  robot-guide/             The design source. make_plans.py renders every plan drawing from the
                           numbers, so a dimension is changed in one place.
  stickbot-draft9p4/       The guide in progress: fourteen tutorial pages and their frames.
docs/                      Background for those same people: how things work, what things are.
src/stickbot/              The Python, installed into .venv by `uv sync`: the four checks, the
                           design source, and the browser and API machinery. Imported by name —
                           nothing here or anywhere else touches sys.path.

.claude/rules/             The contract. Injected into an agent's context on every request.
  constitution.md          How material gets written and verified. Read first.
  parts/prose-style.md     How every word in this repository is written.
  parts/plan-activation.md How a plan becomes the active one, and how it stops being.
  active-plan.md           One import naming the plan being executed, empty when none is.
.claude/skills/            The rest of the contract. Read the one your task needs.
  onshape/                 Shared modeling and step-writing conventions.
  lesson-design/           Shared session-design rules: pacing, floor/ceiling, checkpoints, rubrics.
  modeling-practice/       The design-intent standard every reference model must meet.
  constitution-maintenance/  How the Constitution is amended, and its changelog.
.docs/                     For the people building the class, and for agents. Working notes,
                           design decisions, and the build specification under .docs/build/.
  experiments/runs/        One folder per draft: its plan, its notes, its logs, its register.
```

## Images

**A frame reaches git only by being placed on a guide page.** `.gitignore` denies raster images and
video everywhere and un-ignores exactly `instructions/*/source/images/`; a take writes its interim
capture to the session scratchpad, which is outside this tree. `src/stickbot/check_images.py` is the
*Capture is out* Quality Gate and checks that it happened, so a file added with `git add -f` is
caught too.

The repository this one replaces committed 12,977 screenshots totaling 1,651 MB because capture and
publication shared a directory. It sits beside this one and keeps that history;
[`.docs/2026-09-14-move-to-stick-e-bot.md`](.docs/2026-09-14-move-to-stick-e-bot.md) records what
moved and what did not.

## Getting set up

```sh
uv sync                            # the environment, from uv.lock
uv run playwright install chromium # separate step; uv sync does not do it
ninja check                        # wrap, spelling, reading level, capture
```

Every Python command in this repo is `uv run python …`.

## Reference models

The Onshape documents a session starts and ends from. Cite a **named version**, never the live
workspace; a workspace moves under the class.

| Document             | Purpose                                  | Link   |
| -------------------- | ---------------------------------------- | ------ |
| Instructor reference | The finished model, built the taught way | _TODO_ |
| Session 2 start      | Recovery point: end-of-session-1 state   | _TODO_ |
| Session 3 start      | Recovery point: end-of-session-2 state   | _TODO_ |
| Session 4 start      | Recovery point: end-of-session-3 state   | _TODO_ |

These are placeholders, and there is a known obstacle in front of them. On 2026-09-14 a second
Onshape account was given the document and workspace id of `stickbot-draft9p4` and was refused:
*document does not exist or you don't have permission to access it*. So a link here will not work
until the document is deliberately shared, and no link goes in until it has been opened by an
account without ownership rights.

## Contributing

Read [`.claude/rules/constitution.md`](.claude/rules/constitution.md) in full, then the part or
skill for your work type. Work on a feature branch; never commit to `main`; push only when asked.
