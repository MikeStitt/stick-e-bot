---
name: draw-it-and-print-it
description:
  "Never refuse to draw a shape because it might not print as drawn; draw it, print it, and look at
  what came out."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-09-08T14:22:46.836Z
---

Do not gate geometry on a prediction about the printer. If a shape might come out rounded,
bridged or short of the drawing, that is a reason to print it and measure it, not a reason to
draw something else. Nothing prints exactly as drawn, so "it might not print that way" rules out
every shape equally and decides nothing.

**Why:** the user (Mike), 2026-09-08, on refusing to draw pointed wedge crests because a single-bead
tip would not resolve: *"You've been asserting that we can't draw them certain ways because we can't
guarantee they'll print... Let's draw them and print them and see if they work... I would like 15
degree step user experience, more than I'd like controlled mathematical analysis."* The printed
draft9p1p5 joint had already shown the analysis wrong by 2x on leaf tip deflection, so the model was
the weaker evidence and the part was the stronger.

**How to apply:** Draw what the design wants. Say once, plainly, what you expect the printer to do
to it and what to look for in the part; then build it. When a print comes back, measure it and let
the measurement correct the model, as in [[fix-the-model-retake-the-frames]]. Reserve a real
refusal for geometry that cannot exist, not geometry that may come out soft. Related:
[[design-intent-is-not-sacred]], [[write-for-students-who-will-succeed]].
