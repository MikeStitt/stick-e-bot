# Phase 0 — what the spikes found

Two unknowns stood between the plan and a recorder. Both were measured in the human browser on
port 9224, signed in, against a real Onshape document. Neither needs a workaround.

## The green ✓ is identifiable, and it says more than expected

`.docs/onshape-gui-howto.md` warns that "toolbar buttons, menu items, and most dialog controls do
not resolve". That is true of Playwright locators used for *clicking*. It is not true of reading
the DOM, which is all the recorder does. A feature dialog's header:

```html
<div class="ns-dialog-header" role="dialog">
  <div class="ns-drag-area">
    <span class="ns-dialog-title has-regen-error"
          data-bs-original-title="Plane 1 did not regenerate properly: Offset plane requires …">Plane 1</span>
  </div>
  <div class="ns-dialog-button-ok button-ok disabled" disabled="disabled">
    <osc-svg-icon icon="ok-button"><svg data-automation="ok-button">
  <div class="ns-dialog-button-cancel backbone-cancel">
    <osc-svg-icon icon="cancel-button"><svg data-automation="cancel-button">
```

Four things the recorder gets from this:

- **`data-automation` is an explicit automation hook**, so the ✓ and the ✗ are named rather than
  guessed at. `elementFromPoint` lands on the inner `<svg>` or `<use>`; `closest('.ns-dialog-button-ok')`
  resolves it.
- **The ✗ is as interesting as the ✓.** `cancel-button` is a step that went in wrong and came back
  out — one of the things this run is hunting.
- **Disabled is exposed**, as a class and as an attribute. A hover over a disabled ✓ is a student
  who believes the feature is finished when Onshape does not, and that is a finding about the page,
  not about the student.
- **The regen error is in the DOM verbatim**, in `data-bs-original-title` on the title span. The
  recorder can log the message itself rather than a screenshot of a red row.

The dialog root is `#feature-dialog`, class `ns-dialog-panel feature-dialog`.

**Accept is still detected two ways.** The button gives the click; a MutationObserver on the
feature tree gives the fact that a feature landed. The second one is what the timeline is built
from, because it survives a class rename and it fires for Enter-to-accept as well as for the ✓.

## Screencast keeps up, with room to spare

Measured while spinning `torso-run6p2` by dragging in the viewport, which is the heaviest thing the
canvas does:

| | |
| --- | --- |
| Rate | 51.9 fps over 4.5 s |
| Gap between frames | median 8 ms, p90 43 ms, max 124 ms |
| Frame size | median 84 KB, JPEG quality 70, 1600×1000 |
| A four-second buffer | ~207 frames, ~18 MB in memory |

The max gap is the number that mattered: at 124 ms the worst case for "the frame just before the
tick" is an eighth of a second stale, which is far inside a human's reaction time. No throttling is
needed and `everyNthFrame: 1` stands.

## One thing found on the way

**Onshape writes need an `Accept` header, not only the XSRF one.** A POST carrying
`Content-Type` and `X-XSRF-TOKEN` came back 401 with an empty body. The same POST with
`Accept: application/json;charset=UTF-8; qs=0.09` — what `tools/onshape_session.py` sends — came
back 200. The 401 says nothing about which header is missing.

## What is left in the scratch document

`human-run1 scratch — delete me` (`5212b7307bf3e9f2e5849029`) holds one errored `Plane 1` from the
first spike. It is mine and it can go.
