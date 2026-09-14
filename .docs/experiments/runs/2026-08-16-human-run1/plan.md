# Human run 1 — a person follows `robot-guide2`, and the run records what happens

Run 6 built the robot and wrote the guide from the build. This run does the opposite: a person who
is not the author follows the written page in a browser, and everything they do is recorded — every
key, every mouse move, the frame before each green ✓ and the frame after it.

The recording is the deliverable. `robot-guide3` is written from it.

## The gate this closes

The Constitution's first Quality Gate is *Steps reproduce* — "rebuild the result from an empty
document following **only** the written steps" — and
[`register.md`](../2026-08-14-run6/register.md) records it as unmet for every page of
`robot-guide2`. Nobody has run it. This run runs it, on
[`index.rst`](../../../../instructions/robot-guide2/source/index.rst) and
[`ball-and-socket.rst`](../../../../instructions/robot-guide2/source/ball-and-socket.rst).

It also produces the first honest number for *Fits the clock*, because a human at a keyboard is
student pace by definition. `lesson-design.md` balances the four sessions on captured clicks and
says so; this replaces that with a measurement for one page.

## The rule that makes it a gate

**During the run, the page is the only input.** I answer no questions about what to click, I do not
watch over your shoulder and correct a wrong turn, and I do not repair the model afterward so it
matches. A question you have to ask is the finding — it gets logged with a timestamp and left
unanswered until the run ends.

If you get stuck and cannot proceed, that is a result, not a failure. Say so into the note key, and
either stop or look it up however a student would. What you looked up gets recorded too.

## The harness

One Python process launches the window and records it. Nothing attaches after the fact.

**The window.** Headed Chromium on port **9224**, its own persistent profile under
`~/.cache/onshape-automation/human-profile`, launched by Playwright. Port 9222 stays your own
browser and 9223 stays the agent's; neither is touched. You sign in by hand once, before the
recorder starts, so no password is ever live while capture is running.

**Keys and mouse.** `context.add_init_script` installs a listener ahead of Onshape's own scripts on
every Onshape tab: `pointermove` (throttled to movement, not to time), `pointerdown`, `pointerup`,
`click`, `contextmenu`, `wheel`, `keydown`, `input`. Each event carries what was under the cursor —
`elementFromPoint`, its DOM path, and its `aria-label`, `title` or text. That is what separates
"hovered the green ✓" from "hovered the canvas". Values from `input[type=password]` are dropped.

**The frame before the tick.** CDP `Page.startScreencast` streams timestamped JPEG frames into a
rolling buffer a few seconds deep. When an accept fires, the recorder writes the frame from before
it and another after it settles. Hooking the button and taking a screenshot on demand cannot
produce the *before* — only a buffer that was already running can.

**Video, as well.** `record_video_dir` on the context writes a webm of the whole session, and it
coexists with the screencast: one probe run produced timestamped frames and a webm off the same
page. It costs one parameter, it is watchable with no tooling at all, and it is the fallback if the
frame logic has a bug. It is not a substitute for the buffer — Playwright writes the webm out when
the context closes, so a crash mid-run loses it, and a single file has nothing to index the tick
against.

**The cursor is drawn afterward, from the log.** Neither the video nor the screencast contains a
mouse pointer: the pointer belongs to macOS, and both capture page content. What they do capture is
Onshape's *highlight*, which is page content and is the informative half of a hover. The position
comes from the pointer events, at higher fidelity than pixels and carrying what was under it, so
painting the recorded cursor onto the frames gives a truer picture than a screen recording would.
An `ffmpeg -f avfoundation -capture_cursor 1` recording is the alternative; it needs a Screen
Recording grant and shares no clock with the log, so it is not the default.

**Step marks.** One chord starts each numbered step; a second key opens a one-line box for "this is
where I got lost". Your own words at the moment of confusion are the best input `robot-guide3` can
get. The marks make alignment to the written page exact, so "this step took four minutes and two
undos" is a fact rather than an inference.

**The log.** One JSONL file, one event per line, monotonic timestamps, plus the frames in a
directory beside it. Same shape as `gui_steps.Steps` writes, so the same eyes read both.

## What it cannot see

The 3D viewport is one `<canvas>`. When you hover a face the DOM knows nothing about it, so a
viewport event carries canvas-relative coordinates and the frame, and the identity of what you
picked has to come from the frame by eye or from the API afterward. Every DOM-side click — toolbar,
dialog, feature tree, field — is fully identified.

## What we are hunting

Not the clicks that worked. These:

- **Dwell with no click.** You knew what the page said and could not find it on screen.
- **Red ✗ and Ctrl+Z.** A step went in wrong and had to come out.
- **A dialog opened and abandoned.** The page named the wrong tool.
- **The tool search box opening.** The page did not say where the tool lives.
- **A click the page never mentions.** The author knew something they did not write down.
- **Time between accepted features**, against the page's own click count
  (`grep -c '^\.\. figure::' instructions/robot-guide2/source/ball-and-socket.rst`).

## Phases

**0 — Spike the two unknowns.** Done — [`phase0-findings.md`](phase0-findings.md). The ✓ carries
`data-automation="ok-button"`, and so do the ✗ and the disabled state and the regeneration error
text. Screencast runs at 51.9 fps with a worst gap of 124 ms while the viewport is being dragged,
so the buffer holds the frame before a tick with room to spare.

**1 — Build the recorder.** Done. [`human_browser.py`](human_browser.py) opens the window,
[`capture.js`](capture.js) rides inside the page, [`recorder.py`](recorder.py) drains it and keeps
the frames. All three are probes under the Constitution's escape hatch until they survive a page;
then they move to `tools/` with the gates applied.

```
python human_browser.py --video capture/video     # window; sign in once, nothing recording
python recorder.py                                # attach and record until Ctrl-C
```

Driven end to end against a scratch document four times, fixing what each run exposed. The last
run recorded a plane picked from the tree, a tool reached through **Alt + c**, a dialog opened, a
note typed at the moment of confusion, and the ✓ clicked — with a before-and-after frame for each
and no phantom events from the tree's first paint.

**2 — Dry run.** Done — [`phase2-dryrun.md`](phase2-dryrun.md). The capture holds the whole path
from **Create** to the green ✓, including the frame taken before the tick with the dialog still
readable. Four defects in the harness were found and fixed, one of which would have thrown five
seconds into phase 3. The guide's first defect turned up too: `index.rst` asks for a **Display
decimals** value that is not among the ones Onshape offers.

**3 — The run.** Done. Both pages, from an empty document, in 31 minutes 31 seconds. The follower
reached `Relief slits`, which is the last thing `ball-and-socket.rst` asks for.

**4 — The read-back.** Done — [`deviation-report.md`](deviation-report.md). The page reproduces:
the part measures identical to the one it was written from, and every target in the
ball-and-socket brief of [`target.json`](../2026-08-14-run6/target.json) is met. Two names did not
survive, both of them renames riding at the end of a sentence about something else, and the two
sketches account for 28% of the clock.

**5 — `robot-guide3`.** Written from the report, not from the guide2 text with patches. What
carries over unchanged is what the recording showed nobody stumbled on.

## What this run does not do

It does not touch the model documents run 6 published, it does not edit `robot-guide2`, and it does
not amend the Constitution. Findings land here; the rewrite is phase 5 and it writes a new guide.
