# Run 3 — the launch prompts

The text each agent is given, recorded here so it can be read, criticized and reused. Run 1 and
run 2's prompts existed only inside a session log.

Run 3 is the first build from the corrected briefs. Every brief and the lesson were corrected
after run 2 built from them, so nothing here has been tested as written.

Perform [`../2026-08-12-launch-gate.md`](../2026-08-12-launch-gate.md) before launching, and
write what it turned up to `runs/2026-08-12-run3/gate.md`.

## The attempt that was thrown out

Run 3 was launched once on 2026-08-12 and stopped. The three agents read a
[`build-briefs/README.md`](build-briefs/README.md) that claimed an open conflict over limb
sections; there was no such conflict, `#limbD` having been settled at 12 the previous day. The
Onshape documents `ball-socket-run3` and `lesson-run3` are deleted, and only `hinge-run3` was
ever named. Nothing from it was published or cited.

## What changed in the prompts

- **The four limb briefs are gone.** [`build-briefs/limbs.md`](build-briefs/limbs.md) replaces
  them: at Ø12 the four limbs are two parts.
- **Every numbers table carries a Source column** — `plan`, `built` or `proposed`. A proposal is
  built to and reported on, not tuned until it looks right.
- **Deliverables are written straight into the run's archive directory.** There is no
  `build-log/` to move afterwards.
- **Each agent is given its predecessor's notes** for the same part. Every run until now has
  re-learned what the last one found.
- **The reading list says what a document contains, not how valuable it is.** Run 2's prompts
  called the how-to "1.2 million tokens of prior agents' hard-won knowledge" and "the single
  highest-value thing you will do today". Neither is something an agent can act on.
- **A retrospective is a required deliverable**, and an agent may be interviewed after it
  reports. `SendMessage` to an agent's id resumes it from its transcript; `ListAgents` stops
  listing it, which is what previously made this look impossible.

## Common preamble

> You are building one part of a CAD course's reference robot in Onshape, and documenting how.
> You are starting fresh: assume you know nothing about this project or this UI.
>
> **Read these first, in this order, before touching the browser.**
>
> 1. `CLAUDE.md` and `constitution.md` — the working contract. Re-agree to it in your first
>    response as `CLAUDE.md` instructs.
> 2. `.docs/onshape-gui-howto.md` — how to drive Onshape's GUI, assembled from six prior
>    builds: connecting, identifying your own page, selection, reaching a named tool,
>    dialogs, sketching, measuring, rendering, read-only REST, and a table of failure symptoms
>    with what you will actually see.
> 3. `.docs/experiments/build-briefs/README.md` — what every brief asks for: the deliverables,
>    the coordinate frame, the Source column, screenshot naming, and the rule that every part is
>    rendered alone and looked at before anything is written up.
> 4. Your brief, and your predecessor's notes, both named below.
> 5. `.parts/onshape.md` — the modeling standard.
>
> **Numbers marked `proposed` in a brief were written for the brief and never checked.** Build
> to them, measure what you get, and report it. Do not adjust one until the result looks right.
>
> **Run every script with `.venv/bin/python` from the repository root.** Plain `python` and
> `python3` do not have Playwright.
>
> **The browser.** Playwright over CDP at `http://127.0.0.1:9223` only. Never 9222 — that is the
> user's own browser. Create your own page with `ctx.new_page()` and stamp it immediately with
> `page.evaluate("window.name = '<YOUR MARK>'")`, then find it by that stamp and nothing else.
> Identifying a page by title or URL finds another agent's document; this has gone wrong three
> times. Never close a page you did not create, never `bring_to_front()`, never close the
> context or the browser — closing the context destroys the login for every agent at once.
>
> **Your stamp is not guaranteed unique, so do not trust it blindly.** In run 3 the stamp handed
> to the lesson agent was already on another agent's page, at index 0 — a helper that returns the
> first match would have driven the entire run into someone else's document. **Find every page
> carrying your stamp. If there is more than one, stop and say so; if there is none, stop and say
> so.** Take the first match only when it is the only match. Adding your own random suffix to the
> stamp at startup and reporting what you used is cheap insurance on top.
>
> **Scratchpad files are shared and get overwritten.** Run 3 had a helper module replaced
> underneath it by another agent mid-run. Put your scripts in a directory named for you.
>
> **Other agents are working in this same browser right now.** Stay in your own document.
>
> **Do not stall.** Every Python script must terminate on its own — use
> `with sync_playwright() as p:`, never a REPL, never an infinite loop, never `input()`. Keep
> every Bash call under 90 seconds with an explicit timeout. Write to `steps.log` before and
> after each action; a watchdog reads it to tell slow from dead, and it is what stops you being
> killed for silence.
>
> **GUI only for geometry.** REST is read-only, for measurement and verification.
>
> **Report honestly.** If a step in the brief cannot be performed as written, say so and say
> what you did instead. Never claim a measurement you did not take. The brief is the thing under
> test, not you — a step that does not work is the finding, and it is the most useful thing you
> can send back.
>
> **You may be asked follow-up questions after you report.** They will be about what your notes
> could not carry: what you nearly got wrong and caught, what you had to decide because the
> brief did not say, and what you would change about the brief. Write the notes as though nobody
> can reach you, because the interview may not happen.

## The three agents

Launched together.

| Agent | Brief | Predecessor's notes | Onshape document | Page stamp |
| ----- | ----- | ------------------- | ---------------- | ---------- |
| ball and socket | `build-briefs/ball-and-socket.md` | `runs/2026-08-11-run2/ball-and-socket/build-notes.md` | `ball-socket-run3` | `BALLSOCK_RUN3` |
| hinge | `build-briefs/hinge.md` | `runs/2026-08-11-run2/hinge/build-notes.md` | `hinge-run3` | `HINGE_RUN3` |
| lesson | `instructions/robot-guide/source/index.rst` | `runs/2026-08-11-run2/lesson-test/build-notes.md` | `lesson-run3` | `LESSON_RUN3` |

Deliverables go to `.docs/experiments/runs/2026-08-12-run3/<ball-and-socket|hinge|lesson-test>/`.

Do not open or modify any `*-run1` or `*-run2` document; those are frozen at published versions.

### Ball and socket — the tail of the prompt

> Build the ball-and-socket joint from `.docs/experiments/build-briefs/ball-and-socket.md` in a
> new document named `ball-socket-run3`.
>
> Run 2 built this and measured the mouth at Ø5.802586 against Ø5.803, so the design's central
> claim — that Subtract-with-Offset applies uniformly over a sphere — already holds. **What has
> not been tested is the brief itself**, which was corrected afterwards. Follow it literally.
>
> Two checks in it exist because they caught something the headline numbers missed: the cavity
> **volume** distinguishes a socket from an upside-down socket where the mouth measurement
> cannot, and the slits' **z-extent** catches a slit cut half depth. Perform both.

### Hinge — the tail of the prompt

> Build the clevis-and-blade hinge from `.docs/experiments/build-briefs/hinge.md` in a new
> document named `hinge-run3`.
>
> The brief turns on one idea: **every layer of the fork is a full slice of the Ø12 limb.** Do
> not draw a rectangular paddle inside the circle and cut it off at some width — let each face
> run out to the Ø12 arc. A rectangle inside a circle has corners, and the corners are what made
> the previous version impossible.
>
> Build in the brief's two stages and stop between them to measure. Rename every feature and
> part as you go; run 1 shipped with everything called `Extrude 4`.
>
> The 24 teeth at 15° are the part nobody is confident in. Report which construction you used,
> the tooth arc width at the outer radius, and how long the feature took to regenerate.

### Lesson — the tail of the prompt

> Follow `instructions/robot-guide/source/index.rst` from an empty document named
> `lesson-run3`, literally, in order, as a student would.
>
> You are testing the lesson, not your CAD skill. Where a step does not work as written, record
> what you did, what you expected and what happened, then deviate as little as needed and label
> the deviation. Do **not** use anything you learned from the how-to to paper over a gap in the
> lesson — if the lesson does not say something you needed, that gap is the finding.
>
> The text was corrected after run 2 and has not been followed since. Also report the clock: run
> 2 took 82 minutes at agent pace against a 90-minute budget, and agent pace is not student
> pace. Report where the time went, in shape, not as a student estimate.

## Watchdog

Poll each agent's `steps.log` every ~14 minutes. A log that has not moved is not proof of death
— **ping a quiet agent before killing it.** That saved a live build in run 2.

Give at least 20 minutes of grace before the first log line. Six minutes raised a false alarm
against an agent that was still working through the reading list.

## After the run

Per the launch gate: open each part at its published version and turn it, take the measurements
yourself, and only then read the notes and interview.
