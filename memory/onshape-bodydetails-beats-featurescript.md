---
name: onshape-bodydetails-beats-featurescript
description:
  "bodydetails returns every face's surface, radius, axis, area and box, and is not rate limited
  when featurescript is 429."
metadata: 
  node_type: memory
  type: reference
  originSessionId: c7e95b50-7b3c-4747-a656-ece9f33b51c4
  modified: 2026-08-14T02:04:36.118Z
---

`GET /api/v10/parts/d/{d}/w/{w}/e/{e}/partid/{p}/bodydetails` returns every face of a part with
its surface type (PLANE, CYLINDER, SPHERE, TORUS, CONE, SWEEP), radius, origin, axis, area and
bounding box. It kept returning 200 through a run where `POST .../featurescript` and
`GET/POST .../partstudios/.../features` were all 429.

It answers most acceptance checks without Feature Script: ball diameters and centers, whether a
socket collar is split into four tabs (four cylindrical faces at the collar radius), how many
groove floors a sole has and at what z, detent counts and spacing, and symmetry about a plane
(compare each face's type, area and mirrored box against the set).

What it does **not** give is the distance between two faces, so minimum wall thickness still needs
Feature Script.

Get the part id first from `GET /api/v10/parts/d/{d}/w/{w}/e/{e}`, which also settles the
"Parts (1)" check. See [[onshape-api-via-browser-session]].
