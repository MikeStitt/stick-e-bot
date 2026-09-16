---
name: feature-edits-apply-live
description:
  "An open Onshape feature dialog writes to the model as you change it; only its × reverts."
metadata:
  type: reference
---

Opening a feature for edit rolls the model back to just before that feature and applies every
change as it is made. There is no draft that is discarded when the dialog goes. The dialog's ×
cancels and reverts; a crash, a closed page or a navigation keeps whatever the dialog last applied.

A script that opens a feature for edit MUST press Escape on every failure path. One that cleared
the Entities box, mis-picked the torso's side face instead of the pivot line and then raised left
the plane standing on the face; the torso came back 72 mm across with no shoulders.

Two picking facts came with it: a sketch Onshape has already consumed is hidden, and a hidden
sketch cannot be clicked; and a short line lying in a face needs the view zoomed in before a click
lands on the line rather than on the face. See [[onshape-api-via-browser-session]] and
[[onshape-bodydetails-beats-featurescript]] for reading the result back.
