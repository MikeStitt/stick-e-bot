---
name: one-guide-is-the-end-state
description:
  "robot-guide 1-3 are kept only as a record of improvement; the end state is a single guide, so
  never update the old ones."
metadata: 
  node_type: memory
  type: project
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-20T12:48:46.526Z
---

`instructions/robot-guide`, `robot-guide2` and `robot-guide3` are **archival**. The user (Mike)
keeps them as a record of how the instructions improved, not as material anyone will follow. The end
state is **one** `instructions/robot-guide*`. `robot-guide4` is the live one.

**Why:** nothing in the repo says this — four guides sit side by side under `instructions/`, and
`robot-guide/build/` is even committed, so they all look current.

**How to apply:** write and fix only the live guide. Do not back-port a style change, a keystroke
convention or a toolbar close-up into the older ones, and do not offer to. If a superseded guide
has a defect, it is history, not a bug. See [[every-feature-gets-its-name]] and
[[write-for-students-who-will-succeed]] for what the live guide is held to.
