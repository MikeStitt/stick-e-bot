---
name: never-busy-wait-in-bash
description:
  "read -t N </dev/zero is a busy-wait that eats a core; wait on the harness notification instead."
metadata:
  type: feedback
---

Foreground `sleep` is blocked in this harness, and `read -t N x </dev/zero` is not a
substitute. `/dev/zero` never delivers a newline, so `read` consumes null bytes at full
speed until the timeout — a busy-wait, not a sleep. Four of those polling loops running
at once ate about a full core and made the user's UI stutter as they typed.

**Why:** the user noticed the machine had gone slow and asked me to kill background
tasks. The culprit was my own polling, not the CAD browsers.

**How to apply:** run the long job with `run_in_background: true` and wait for the task
notification instead of polling for it. When something genuinely has to be waited on in
shell, block on the thing itself — `wait <pid>`, or a command that blocks on I/O — never
a spin against `/dev/zero`. Piping a long job to `tail` also hides all its output until
it exits, so redirect to a file and read the file. See [[capture-while-you-experiment]]
for the related habit of getting evidence out as it happens rather than at the end.
