/* What the page records about a person following the guide.
 *
 * Everything lands in a ring buffer that Python drains a few times a second. Nothing
 * here calls out to Python directly: a buffer plus a poll has no callback re-entrancy
 * to get wrong, and every event carries its own Date.now(), so the drain being late
 * costs nothing.
 *
 * Two kinds of thing are recorded. Input — what the person did. And state — what
 * Onshape did about it, sampled on a timer rather than through a MutationObserver,
 * because Onshape's DOM churns constantly and a diff of a small snapshot is cheaper
 * and quieter than filtering the churn.
 */
(() => {
  /* Sticky by design: re-injecting would register a second set of listeners on top of
   * the first. The recorder reloads the page when this version does not match the
   * file on disk, which is the only way an edit here reaches a page already open. */
  if (window.__hrec) return;

  const MAX = 6000;          // ring buffer depth; Python drains long before this
  const MOVE_MS = 40;        // pointermove floor
  const MOVE_PX = 6;         // ...and it must have actually moved
  const WATCH_MS = 500;      // state sampling period

  const buf = [];
  let seq = 0, step = 0;

  const push = (kind, data) => {
    if (buf.length >= MAX) buf.shift();
    buf.push(Object.assign({seq: ++seq, t: Date.now(), step, kind}, data || {}));
  };

  // ---- describing an element -------------------------------------------------

  const cls = e => {
    const c = e.className;
    return (c && c.baseVal !== undefined ? c.baseVal : c) || '';
  };

  const path = e => {
    const out = [];
    for (let n = e; n && n.nodeType === 1 && out.length < 5; n = n.parentElement) {
      const c = cls(n).trim().split(/\s+/).filter(Boolean).slice(0, 2).join('.');
      out.unshift(n.tagName.toLowerCase() + (n.id ? '#' + n.id : '') + (c ? '.' + c : ''));
    }
    return out.join(' > ');
  };

  /* What the person would say they were pointing at. The DOM under Onshape's chrome
   * is anonymous divs, so the useful identity is which known container it sits in. */
  const role = e => {
    if (!e || e.nodeType !== 1) return null;
    if (e.closest('.ns-dialog-button-ok')) return 'dialog-ok';
    if (e.closest('.ns-dialog-button-cancel')) return 'dialog-cancel';
    if (e.closest('#feature-dialog')) return 'dialog';
    if (e.closest('.os-list-item')) return 'tree-row';
    if (e.tagName === 'CANVAS' || e.closest('#viewerdiv')) return 'viewport';
    if (e.closest('input, textarea')) return 'field';
    return null;
  };

  const describe = e => {
    if (!e || e.nodeType !== 1) return null;
    const svg = e.closest('[data-automation]') || e.querySelector?.('[data-automation]');
    const d = {
      tag: e.tagName.toLowerCase(),
      cls: cls(e).slice(0, 80),
      role: role(e),
      path: path(e),
    };
    if (e.id) d.id = e.id;
    const auto = svg && svg.getAttribute('data-automation');
    if (auto) d.auto = auto;
    const label = e.getAttribute('aria-label') || e.getAttribute('title');
    if (label) d.label = label.slice(0, 80);
    // A key pressed with nothing focused reports <body> as its target, whose text is
    // the whole application. Only leaf-ish elements are worth quoting.
    if (e.children.length <= 4) {
      const txt = (e.innerText || '').trim().replace(/\s+/g, ' ');
      if (txt) d.text = txt.slice(0, 60);
    }
    const row = e.closest('.os-list-item');
    if (row) d.row = (row.innerText || '').trim().split('\n')[0].slice(0, 60);
    return d;
  };

  const canvasXY = (e, ev) => {
    const c = e && (e.tagName === 'CANVAS' ? e : e.closest?.('#viewerdiv'));
    if (!c) return null;
    const r = c.getBoundingClientRect();
    return [Math.round(ev.clientX - r.x), Math.round(ev.clientY - r.y)];
  };

  const secret = e => e && e.tagName === 'INPUT' && e.type === 'password';

  /* This recorder puts two elements on the page. Neither is part of what the person
   * was doing, so nothing that happens inside them is recorded as if it were. */
  const ours = e => !!(e && e.closest && e.closest('[data-hrec-ui]'));

  // ---- input -----------------------------------------------------------------

  let lastMove = 0, lastX = -999, lastY = -999, lastRole = null;

  const at = ev => document.elementFromPoint(ev.clientX, ev.clientY);

  addEventListener('pointermove', ev => {
    const now = ev.timeStamp;
    const far = Math.abs(ev.clientX - lastX) + Math.abs(ev.clientY - lastY) >= MOVE_PX;
    const el = at(ev);
    const r = role(el);
    // A hover that changes what you are over is always kept, however small the move:
    // that is the moment the guide is being tested against the screen.
    if (r !== lastRole) {
      lastRole = r;
      push('hover', {x: ev.clientX, y: ev.clientY, el: describe(el),
                     canvas: canvasXY(el, ev),
                     okDisabled: !!el?.closest?.('.ns-dialog-button-ok.disabled')});
    } else if (now - lastMove >= MOVE_MS && far) {
      push('move', {x: ev.clientX, y: ev.clientY, role: r});
    } else {
      return;
    }
    lastMove = now; lastX = ev.clientX; lastY = ev.clientY;
  }, {capture: true, passive: true});

  for (const type of ['pointerdown', 'pointerup', 'click', 'dblclick', 'contextmenu']) {
    addEventListener(type, ev => {
      const el = at(ev) || ev.target;
      if (ours(el)) return;
      push(type, {x: ev.clientX, y: ev.clientY, button: ev.button,
                  el: describe(el), canvas: canvasXY(el, ev)});
    }, {capture: true, passive: true});
  }

  let lastWheel = 0;
  addEventListener('wheel', ev => {
    if (ev.timeStamp - lastWheel < 120) return;
    lastWheel = ev.timeStamp;
    push('wheel', {x: ev.clientX, y: ev.clientY, dy: Math.round(ev.deltaY),
                   role: role(at(ev))});
  }, {capture: true, passive: true});

  addEventListener('keydown', ev => {
    if (secret(ev.target) || ours(ev.target)) return;
    push('key', {key: ev.key, code: ev.code,
                 mod: [ev.ctrlKey && 'ctrl', ev.metaKey && 'meta', ev.altKey && 'alt',
                       ev.shiftKey && 'shift'].filter(Boolean).join('+') || null,
                 el: describe(ev.target)});
  }, {capture: true});

  addEventListener('input', ev => {
    if (secret(ev.target) || ours(ev.target)) return;
    push('input', {value: String(ev.target.value ?? '').slice(0, 60),
                   el: describe(ev.target)});
  }, {capture: true, passive: true});

  /* Time spent reading the guide happens in another window, where nothing here can
   * see it — and without this it lands on the clock as if it were time spent hunting
   * for a menu. The dry run attributed seventeen seconds to a menu that was never
   * being searched. Away and back are what make a duration mean anything. */
  addEventListener('blur', () => push('away', {reason: 'window'}));
  addEventListener('focus', () => push('back', {reason: 'window'}));
  document.addEventListener('visibilitychange', () =>
    push(document.hidden ? 'away' : 'back', {reason: 'tab'}));

  // ---- state, sampled --------------------------------------------------------

  /* Rows that are furniture rather than features. `Parts (3)` renames itself every
   * time a part appears, which would read as one row leaving and another arriving. */
  const DEFAULTS = ['Default geometry', 'Origin', 'Top', 'Front', 'Right', 'Parts'];
  const furniture = name => !name || /^Parts \(\d+\)$/.test(name) || DEFAULTS.includes(name);

  /* A dialog is open when there is a tick to press. Keying off the tick rather than
   * off `#feature-dialog` catches Workspace units and its like, which carry the same
   * button in different chrome — and the units dialog is the first thing the guide
   * asks for, in every document. */
  const snapshot = () => {
    const ok = document.querySelector('.ns-dialog-button-ok');
    const feat = document.querySelector('#feature-dialog');
    const title = document.querySelector('.ns-dialog-title');
    const rows = Array.from(document.querySelectorAll('.os-list-item')).map(r => ({
      name: (r.innerText || '').trim().split('\n')[0].slice(0, 60),
      bad: cls(r).includes('ns-list-item-error'),
    })).filter(r => !furniture(r.name));
    return {
      dialog: ok ? {
        title: title ? title.textContent.trim() : '',
        feature: !!feat,
        okDisabled: cls(ok).includes('disabled'),
        error: feat && title && cls(title).includes('has-regen-error')
          ? (title.getAttribute('data-bs-original-title') || '') : '',
      } : null,
      rows,
    };
  };

  let prev = snapshot();
  /* The tree is still rendering when this script lands, so its first appearance would
   * read as every default plane being created at once. Watch quietly until it settles. */
  const quietUntil = Date.now() + 5000;

  const watch = () => {
    const now = snapshot();
    if (Date.now() < quietUntil) { prev = now; return; }

    const wasOpen = !!prev.dialog, isOpen = !!now.dialog;
    if (!wasOpen && isOpen) push('dialog-open', {dialog: now.dialog});
    if (wasOpen && !isOpen) push('dialog-close', {was: prev.dialog.title});
    if (wasOpen && isOpen) {
      if (prev.dialog.okDisabled !== now.dialog.okDisabled) {
        push('ok-enabled', {enabled: !now.dialog.okDisabled, title: now.dialog.title});
      }
      if (prev.dialog.error !== now.dialog.error && now.dialog.error) {
        push('dialog-error', {title: now.dialog.title, error: now.dialog.error});
      }
    }

    const before = prev.rows.map(r => r.name), after = now.rows.map(r => r.name);
    const added = after.filter(n => !before.includes(n));
    const gone = before.filter(n => !after.includes(n));
    if (added.length) push('feature-added', {names: added});
    if (gone.length) push('feature-removed', {names: gone});

    const bad = now.rows.filter(r => r.bad).map(r => r.name);
    const wasBad = prev.rows.filter(r => r.bad).map(r => r.name);
    if (bad.join('|') !== wasBad.join('|')) push('tree-errors', {names: bad});

    prev = now;
  };
  setInterval(watch, WATCH_MS);

  // ---- the person's own marks ------------------------------------------------

  const hud = document.createElement('div');
  hud.setAttribute('data-hrec-ui', 'hud');
  hud.style.cssText = 'position:fixed;right:10px;bottom:10px;z-index:2147483647;' +
    'font:12px system-ui;color:#fff;background:rgba(20,20,20,.82);padding:5px 9px;' +
    'border-radius:4px;pointer-events:none;letter-spacing:.3px';
  const paint = () => { hud.textContent = `● REC  step ${step}   F8 next · F9 note`; };
  paint();

  const box = document.createElement('div');
  box.setAttribute('data-hrec-ui', 'note');
  box.style.cssText = 'position:fixed;left:50%;top:22%;transform:translateX(-50%);' +
    'z-index:2147483647;display:none;background:#1b1b1b;color:#fff;padding:12px 14px;' +
    'border-radius:6px;font:13px system-ui;box-shadow:0 6px 30px rgba(0,0,0,.5)';
  box.innerHTML = '<div style="margin-bottom:7px">What just happened? ' +
    '<span style="opacity:.6">Enter keeps it, Esc drops it</span></div>';
  const note = document.createElement('input');
  note.style.cssText = 'width:440px;font:13px system-ui;padding:6px 8px;border-radius:4px;' +
    'border:1px solid #555;background:#111;color:#fff';
  box.appendChild(note);

  const attach = () => {
    if (!document.body) return;
    if (!hud.isConnected) document.body.appendChild(hud);
    if (!box.isConnected) document.body.appendChild(box);
  };
  attach();
  setInterval(attach, 2000);   // Onshape replaces large parts of the page

  const openNote = () => { box.style.display = 'block'; note.value = ''; note.focus(); };
  const closeNote = () => { box.style.display = 'none'; note.blur(); };

  note.addEventListener('keydown', ev => {
    ev.stopPropagation();                       // Onshape must not see this typing
    if (ev.key === 'Enter') {
      if (note.value.trim()) push('note', {text: note.value.trim()});
      closeNote();
    } else if (ev.key === 'Escape') {
      closeNote();
    }
  }, true);

  addEventListener('keydown', ev => {
    if (ev.key === 'F8') {
      ev.preventDefault(); ev.stopPropagation();
      step += 1; paint();
      push('step', {step});
    } else if (ev.key === 'F9') {
      ev.preventDefault(); ev.stopPropagation();
      openNote();
    }
  }, true);

  // ---- the drain -------------------------------------------------------------

  window.__hrec = {
    drain() { const out = buf.splice(0, buf.length); return out; },
    step() { return step; },
    version: 2,
  };
  push('capture-start', {url: location.href, w: innerWidth, h: innerHeight});
})();
