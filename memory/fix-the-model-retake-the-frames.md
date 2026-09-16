---
name: fix-the-model-retake-the-frames
description:
  "Fixing a model obsoletes every frame that shows the old state; retake them, never write around
  them."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-30T01:48:09.904Z
---

When a fix changes what the model looks like, the frames of the old state are wrong and MUST be
retaken. Do not write the page around them, and do not offer that as an option.

**Why:** a page is written from its frames. A frame showing a state the model no longer has teaches
the reader something untrue, and the caption usually asserts it out loud — tutorial 8's
`pedestal_sketch-05` says "black because the sketch is now fully defined" over a picture of an
under-defined sketch. Leaving it turns one model defect into a permanent page defect.

**How to apply:** the moment a fix lands, list every frame of every step the fix touches and drive
those steps again. Retaking is part of the fix, not a follow-up task. Keep pushing until the frames
and the model agree.

See [[capture-while-you-experiment]], [[design-intent-is-not-sacred]] and
[[write-for-students-who-will-succeed]].
