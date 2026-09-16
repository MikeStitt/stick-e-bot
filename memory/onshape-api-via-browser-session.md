---
name: onshape-api-via-browser-session
description: Hard-won gotchas for driving the Onshape REST API from a logged-in browser session
metadata: 
  node_type: memory
  type: reference
  originSessionId: f7a2d0bd-c646-4b69-9103-9c444fdbf1e2
  modified: 2026-08-16T21:05:59.835Z
---

Onshape has no API key set up for this project; access rides a logged-in Playwright
Chromium session via same-origin fetch from cad.onshape.com.

Gotchas that cost real time and are not obvious:

- Cookie auth alone returns **401 on writes**. The `XSRF-TOKEN` cookie must be echoed
  back as an `X-XSRF-TOKEN` header, which is what Onshape's own web client does.
- The XSRF header is not enough on its own: a write also needs
  `Accept: application/json;charset=UTF-8; qs=0.09`. Without it the same POST is 401
  with an empty body, which reads exactly like a session problem and is not one.
- Geometry is referenced by `geometryIds` (e.g. Front plane is `"JCC"`), not by a
  FeatureScript `queryString`. Sketch regions use `BTMIndividualSketchRegionQuery`
  (type 140) keyed by the sketch's `featureId`.
- Every **Add**/**Remove** operation needs `defaultScope: true`, or it fails with
  "No merge scope selected" — sometimes only on a *later* regeneration.
- A feature's POST response can say `OK` and the feature can break later. Read
  `featureStates` from `GET .../features`; it is an **array of {key, value} pairs**,
  not a map. Verify after metadata writes, which trigger regeneration.
- Part IDs are **not stable** across metadata writes. Re-resolve them immediately
  before writing names or appearances.
- `featureStatus` does not capture "not fully defined" — see
  [[cad-models-need-design-intent]].
