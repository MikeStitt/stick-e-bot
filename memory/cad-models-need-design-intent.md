---
name: cad-models-need-design-intent
description:
  "Onshape models for this course must be built from constraints and relationships, never absolute
  magic coordinates"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f7a2d0bd-c646-4b69-9103-9c444fdbf1e2
  modified: 2026-08-09T20:36:50.904Z
---

The user (Mike) expects CAD models here to be built the way a person actually models: first
sketch is a center-point rectangle on the origin, and every later sketch, extrude
or revolve is tied to existing geometry through projected edges and constraints
(Coincident, Collinear, Equal, Symmetric) plus named variables. No magic numbers,
no independently authored absolute coordinates — a web of relationships.

**Why:** the deliverable is a class teaching people to CAD. A reference model made
of typed coordinates looks correct but teaches the exact habit the course exists
to prevent, and it teaches it invisibly. It also shatters the moment one driving
dimension changes.

**How to apply:** treat "every sketch reports *fully defined*" plus "change one
driving variable and the model updates sensibly" as the acceptance gate for any
model, not just "the render looks right". When an API or scripting path makes raw
geometry easy and constraints laborious, do not let that shape the model — that is
the tool dictating pedagogy. Related: [[onshape-api-via-browser-session]].
