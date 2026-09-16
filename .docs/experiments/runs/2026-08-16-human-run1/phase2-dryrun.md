# Phase 2 — the dry run

Five minutes, one throwaway document, and only the *Set the units first* admonition from
[`index.rst`](../../../../instructions/robot-guide2/source/index.rst). The point was to prove the
harness before a session rode on it. It also found the first defect in the guide.

The capture is `capture/2026-08-16-173158/`.

## The harness works

The trace reads as a sentence: **Create** → **Document…** → the name field → `experiment` → Enter →
into the Part Studio → the ☰ menu → **Workspace units…** → **Millimeter** → **0.12345** → the green
✓. Every one of those carries the element that was under the cursor, and three F8 marks sit where
the person put them.

A person moves a mouse the way a script does not: 156 pointer moves against the 3 a driven run
produced. The hover stream is real.

`1-0007-before-dialog-ok.jpg` is the frame the whole design was for — the units dialog still open,
**Millimeter** and **0.12345** both readable, the ✓ lit under the cursor, taken before the click
that closed it.

## The guide names a value Onshape does not have

`index.rst` says:

> Set **Display decimals** to **0.00001**.

The dropdown offers `0`, `0.1`, `0.12`, `0.123`, `0.1234`, `0.12345`. There is no `0.00001` in it.
Five decimal places is the right intent and `0.12345` is what was picked, but the label in the guide
is not the label on the screen, which is the *Names are real* gate.

Not fixed here. `robot-guide2` is not edited by this run; it goes into `robot-guide3` in phase 5.

## Reading the guide is invisible, and the clock pays for it

Seventeen seconds passed between the ☰ menu opening and **Workspace units…** being clicked. Read off
the trace alone that looks like hunting through a menu. It was not: the person had switched windows
to read the step.

Nothing in the browser sees that, so the time landed on the next click as if it had been spent
searching. Every duration in the capture carries the same error, in an unknown amount, and the
duration is the whole point of phase 3 — *Fits the clock* is the gate this run exists to answer
honestly.

`capture.js` now records `away` and `back`, from the window's own blur and focus and from the tab's
visibility. Time outside the window is subtracted rather than guessed at.

The listeners are verified wired — dispatching `blur`, `focus` and `visibilitychange` into the page
produced `away/window`, `back/window` and `back/tab`. They are **not** verified against a real
window switch, because moving the desktop's focus is not something this end can do. The first
alt-tab of phase 3 is the test, and it happens in the first minute.

Two things follow for phase 3:

- **Read the guide in a second tab of the same window.** `instructions/robot-guide2/` builds to
  local HTML, and a tab is a page the recorder already handles: which page was open, for how long,
  and how often it was returned to. A separate application is a hole in the record; a second tab is
  part of it.
- **Hands-on time and reading time are different numbers**, and the session plan wants the first
  one. Now they can be told apart.

## Four defects in the harness, all fixed

- **The dialog detector only knew feature dialogs.** Workspace units carries the same ✓ in different
  chrome, so no `dialog-open` or `dialog-close` was recorded for the one dialog this run was about.
  Now a dialog is "open" when there is a tick on the page, which is true of both.
- **A key pressed with nothing focused reports `<body>`**, whose text is the whole application.
  Elements with more than a handful of children no longer have their text quoted.
- **`session.json` was lost to a hard kill.** It is now rewritten every few seconds, so stopping the
  recorder any way at all keeps the summary. `events.jsonl` was never at risk; it is line buffered.
- **`SUMMARY_S` was referenced and never defined**, which would have thrown five seconds into the
  real run. `py_compile` does not catch a missing global; starting the recorder and watching it pass
  the five-second mark does.

## The capture is sticky, and that hid the first fix

`capture.js` guards itself with `if (window.__hrec) return`, because injecting it twice would leave
two sets of listeners on the page and no way to unhook the first. The consequence is that **editing
the file changes nothing in a page that is already open.** The `away` and `back` listeners were
written, the page was tested, and the events did not appear — not because they were wrong, but
because the page was still running the version from before the edit.

The script now carries a `version`, the recorder reads that number out of the file rather than
holding its own copy, and a tab running an older one is reloaded on attach. A reload before any work
starts costs nothing; the alternative is an edit that silently does not apply.

## Worth knowing before phase 3

`capture.js` keeps running when the recorder stops, because it lives in the page. The next recorder
to attach drains what accumulated in between, so those events carry timestamps from before it
started. Nothing is lost; the order is by timestamp, not by arrival.
