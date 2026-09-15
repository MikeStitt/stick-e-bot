---
name: capture-while-you-experiment
description:
  "Take the named frames on the first pass through a click sequence, not on a second pass; a
  debugging screenshot is not a frame, and attempting the shot is how tooling gaps surface"
metadata:
  type: feedback
---

**Capture while working out the click sequence, not afterwards.** Do not split the work into
*figure out the sequence*, then *do it again with capture*. Every place a `page.screenshot`
happens for debugging is a place a named frame belongs — `gui.frame(page, path)` is one line, and
the expensive part (driving the browser into the right state) has already been paid for.

**Why:** on 2026-08-20 tutorial 1 was built with 17 scratchpad screenshots and **zero** frames.
The screenshots were named `dim1.png`, `state.png`, `extrude3.png` — framed for reading, not for use
on a page. Attempting the planned shots would have caught
two plan defects at the moment they happened: the *version dialog* shot is unreachable when the
version is published by a REST call, and the *insert into all, off* shot does not exist because
the control arrives already ticked.

**How to apply:** the shot plan exists so the shots get taken. Name the frame by its step
identifier at the moment the state is on screen. Trying the shot is itself the test of the capture
tooling. Holding the step and its frames in mind at once costs context, and the user would rather
raise the context limit than get a second pass.

Related: [[every-feature-gets-its-name]], [[write-for-students-who-will-succeed]].
