# _TODO_l in Onshape

TODO Describe this class

## Repository layout

```
CLAUDE.md                  The agreement to follow the Constitution, for AI assistants.
README.md                  This file.
build.ninja                `ninja check` — wrap, spelling and reading level in one command.

instructions/              What a student or a teacher is handed.
  robot-guide/             Session 1: a Sphinx page written by hand, source and built site.
    source/index.rst       The steps themselves. Built and corrected across two test runs.
docs/                      Background for those same people: how things work, what things are.
tools/                     The check scripts, and the browser and API machinery.

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
                           and the working list. See .docs/README.md.
  experiments/             What we tried and what it taught: build briefs and logs, test
                           reports, the superseded first session, the retired sponge guide.

guide/                     Retired. The sponge walkthrough and the pipeline that generated
                           it from the live Onshape UI. It still owns the browser and API
                           tooling. Now at .docs/experiments/spongebob-guide/.
```


## Getting set up

```sh
uv sync                            # the environment, from uv.lock
uv run playwright install chromium # separate step; uv sync does not do it
ninja check                        # wrap, spelling, reading level
```

Every Python command in this repo is `uv run python …`.

## Reference models

The instructor-side Onshape documents each session starts and ends from. Cite a **named version**,
never the live workspace; a workspace moves under the class.

| Document             | Purpose                                  | Link   |
| -------------------- | ---------------------------------------- | ------ |
| Instructor reference | The finished model, built the taught way | _TODO_ |
| Session 2 start      | Recovery point: end-of-session-1 state   | _TODO_ |
| Session 3 start      | Recovery point: end-of-session-2 state   | _TODO_ |
| Session 4 start      | Recovery point: end-of-session-3 state   | _TODO_ |

These are placeholders. No links have been created yet — do not cite one until it exists and you
have opened it as a student would.


## Contributing

Read [`.claude/rules/constitution.md`](.claude/rules/constitution.md) in full, then the part or
skill for your work type. Work on a feature branch; never commit to `main`; push only when asked.
