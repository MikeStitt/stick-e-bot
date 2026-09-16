---
name: drawing-conventions
description:
  "On design drawings, never put counts (instances, unique parts); every dimension carries its
  unit."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7a2d0bd-c646-4b69-9103-9c444fdbf1e2
  modified: 2026-08-11T12:33:42.458Z
---

Two standing rules for any design/plan drawing in this repo:

1. **No counts on drawings** — no per-part quantities (`×2`), no "eight parts, fourteen
   instances" in a header, no "stud ×2" callouts.
2. **Every dimension carries its unit** — `150 mm`, not `150 tall`; `30 mm`, not `30 deep`.
   Units, not words: `mm`, `deg`, and so on. The extension lines already say *which*
   dimension it is.
3. **No design rationale from the plan** — e.g. "every dimension is a fraction of the 48 mm
   torso". We chose that to make the numbers easy to talk about, but it is our trick, not
   the student's problem, and it is one more thing to keep in step. The drawing shows *what*
   the thing is; the plan says *why*.

**Why:** a drawing that carries a count has to be redrawn every time the count changes, and
the count already lives in the BOM — it is pure maintenance for no information. Words like
"tall"/"deep"/"wide" are doing the unit's job while saying nothing the geometry does not.

**How to apply:** when generating sheets — `src/stickbot/make_plans.py` renders every
one of them, and `ninja plan` runs it — keep quantities in the build plan's tables and out of the
SVG. Also check that every dimension
has extension lines aligned with the feature it measures — a dimension floating under a
shape cannot be read against it.
