---
name: no-em-dash-near-a-number
description: Never use an em dash where it could read as a minus sign; use a semicolon instead.
metadata: 
  node_type: memory
  type: feedback
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-27T16:34:26.165Z
---

Never put an em dash next to a number. Use a semicolon.

**Why:** This work is nothing but dimensions. Written beside a figure, an em dash is
indistinguishable from a minus sign at a glance, so `33.0 — 0.0535 longer` reads as the subtraction
`33.0 - 0.0535`, which happens to equal the other number in the same row. The user (Mike) hit
exactly that ambiguity in a before/after table and had to ask which one I meant.

**How to apply:** In tables, prose, commit messages and briefs, scan for an em dash with a digit
on either side and replace it with a semicolon: `33.0; 0.0535 longer`. The rule is about
confusion, not about em dashes in general, so a dash between two words is unaffected. Applies to
the same documents as [[drawing-conventions]] and [[instructions-state-facts-not-importance]].
