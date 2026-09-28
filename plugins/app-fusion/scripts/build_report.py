#!/usr/bin/env python3
"""Build one self-contained page with everything the program has found so far.

    python3 build_report.py <program> [--workspace DIR] [--out FILE]

Reads whatever exists under analysis/<program>/ (every file is optional; a missing one shows as missing, never an
error) and writes analysis/<program>/REPORT.html. The artifacts come from untrusted code and designs, so every value
is treated as hostile: data travels only as escaped JSON inside a <script type="application/json"> block, the page
builds its DOM with textContent, and a Content-Security-Policy allows only this page's own script and style (by hash),
local images, and no network request. Files named *.local.* or SECRETS* are never read. Works offline.
Standard library only.
"""

import argparse
import base64
import hashlib
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import status as statusmod  # noqa: E402
from fusionlib.common import check_name, load_json, program_dir, workspace, write_text  # noqa: E402
from fusionlib.status import parse_brief  # noqa: E402

STYLE = """
:root{--bg:#f7f7f5;--fg:#1d1d1b;--mute:#6b6b66;--line:#dcdcd6;--card:#fff;--accent:#1f6feb;--ok:#1a7f37;--warn:#9a6700;--bad:#cf222e}
@media (prefers-color-scheme:dark){:root{--bg:#161616;--fg:#e8e8e3;--mute:#9a9a93;--line:#333;--card:#1f1f1f;--accent:#58a6ff;--ok:#3fb950;--warn:#d29922;--bad:#f85149}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif}
header{padding:20px 24px 8px}h1{font-size:22px;margin:0 0 4px}header p{margin:0;color:var(--mute)}
nav{display:flex;flex-wrap:wrap;gap:4px;padding:8px 24px;border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg)}
nav button{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:6px;padding:6px 10px;cursor:pointer;font:inherit}
nav button[aria-selected=true]{border-color:var(--accent);color:var(--accent);font-weight:600}
main{padding:16px 24px 48px;max-width:1400px}section{display:none}section.on{display:block}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px;margin:12px 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px}.card b{display:block;font-size:22px}
.card span{color:var(--mute);font-size:12px}.next{background:var(--card);border:1px solid var(--accent);border-radius:8px;padding:12px;margin:12px 0}
.next code{font-size:15px;user-select:all}table{border-collapse:collapse;width:100%;background:var(--card);margin:8px 0 16px}
th,td{border:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{position:sticky;top:44px;background:var(--card)}
td.num{text-align:right;font-variant-numeric:tabular-nums}.muted{color:var(--mute)}.pill{display:inline-block;border-radius:10px;padding:0 8px;font-size:12px;border:1px solid var(--line)}
.PROVEN,.pass,.done{color:var(--ok);border-color:var(--ok)}.PARTLY,.gap,.partial{color:var(--warn);border-color:var(--warn)}.NOT,.fail{color:var(--bad);border-color:var(--bad)}
input[type=search]{padding:6px 8px;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg);min-width:260px;font:inherit}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:12px}.shot{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px}
.shot img{width:100%;height:auto;border-radius:4px;background:#8882}.shot .pair{display:grid;grid-template-columns:1fr 1fr;gap:6px}
pre{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;overflow:auto;white-space:pre-wrap}
details{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:8px 12px;margin:6px 0}summary{cursor:pointer;font-weight:600}
"""

SCRIPT = r"""
(function(){
const D = JSON.parse(document.getElementById('data').textContent);
const $ = (t, a, kids) => { const e = document.createElement(t); if (a) for (const k in a) { if (k === 'text') e.textContent = a[k]; else if (k === 'cls') e.className = a[k]; else e.setAttribute(k, a[k]); } (kids||[]).forEach(c => c && e.appendChild(typeof c === 'string' ? document.createTextNode(c) : c)); return e; };
const table = (heads, rows, numeric) => { const t = $('table'); const h = $('tr'); heads.forEach(x => h.appendChild($('th', {text: x}))); t.appendChild($('thead', null, [h])); const b = $('tbody'); rows.forEach(r => { const tr = $('tr'); r.forEach((c, i) => { const td = $('td', (numeric||[]).includes(i) ? {cls: 'num'} : null); if (c instanceof Node) td.appendChild(c); else td.textContent = c == null ? '' : String(c); tr.appendChild(td); }); b.appendChild(tr); }); t.appendChild(b); return t; };
const pill = (text, cls) => $('span', {cls: 'pill ' + (cls || String(text).split(' ')[0]), text: text});
const card = (n, label) => $('div', {cls: 'card'}, [$('b', {text: String(n)}), $('span', {text: label})]);
const sec = id => document.getElementById(id);
const tabs = [['overview','Overview'],['apps','Apps'],['caps','Capabilities'],['design','Design'],['rules','Rules'],['decisions','Decisions'],['plan','Plan'],['proof','Proof'],['security','Security']];
const nav = document.querySelector('nav');
tabs.forEach(([id, label], i) => { const b = $('button', {text: label, 'aria-selected': i === 0 ? 'true' : 'false', 'data-tab': id}); b.addEventListener('click', () => { document.querySelectorAll('nav button').forEach(x => x.setAttribute('aria-selected', 'false')); b.setAttribute('aria-selected', 'true'); document.querySelectorAll('section').forEach(s => s.classList.toggle('on', s.id === id)); }); nav.appendChild(b); });
const S = D.status || {};
// overview
(function(){ const o = sec('overview'); o.classList.add('on');
  const nx = S.next || {}; o.appendChild($('div', {cls: 'next'}, [$('div', {cls: 'muted', text: 'Next step'}), $('code', {text: nx.command || '-'}), $('div', {cls: 'muted', text: nx.reason || ''})]));
  const cov = S.coverage || {}; const v = S.verdicts || {};
  const cards = $('div', {cls: 'cards'}, [card((D.apps||[]).length, 'source apps'), card(S.capabilities || 0, 'capabilities'), card(S.journeys || 0, 'journeys'), card((cov.percent != null ? cov.percent + '%' : '-'), 'designed'), card((S.built||[]).length, 'built'), card(v.PROVEN || 0, 'proven'), card(S.openQuestions || 0, 'open questions')]);
  o.appendChild(cards);
  o.appendChild($('h2', {text: 'Steps'}));
  o.appendChild(table(['Step', 'State', 'Files'], (S.stages||[]).map(s => [s.stage, pill(s.present === s.total ? 'done' : (s.present ? 'partial' : 'not yet'), s.present === s.total ? 'done' : (s.present ? 'partial' : 'muted')), s.files.join(', ')])));
  if ((S.stale||[]).length) { o.appendChild($('h2', {text: 'Stale'})); const ul = $('ul'); S.stale.forEach(x => ul.appendChild($('li', {text: x}))); o.appendChild(ul); }
  o.appendChild($('h2', {text: 'Legacy apps (never edited)'}));
  o.appendChild(table(['App', 'Product', 'Stack', 'Commit', 'Working tree'], (D.apps||[]).map(a => { const l = (S.legacy||[]).find(x => x.app === a.name) || {}; return [a.name, a.product, a.stack, (a.commit||'').slice(0,12), l.exists ? (l.clean ? 'clean' : (l.clean === false ? 'CHANGED' : 'not git')) : 'missing']; })));
})();
// apps
(function(){ const s = sec('apps'); const inv = D.inventories || {}; const names = Object.keys(inv);
  if (!names.length) { s.appendChild($('p', {cls: 'muted', text: 'No inventory yet: run fuse-assess.'})); return; }
  const keys = []; names.forEach(n => Object.keys(inv[n].counts || {}).forEach(k => { if (!keys.includes(k)) keys.push(k); }));
  s.appendChild($('p', {cls: 'muted', text: 'Every number is printed with the rule that produced it: quote the rule with the number.'}));
  const rows = keys.map(k => {
    const vals = names.map(n => { const c = inv[n].counts || {}; return c[k] === undefined ? '' : c[k]; });
    const rule = names.map(n => (inv[n].rules || {})[k]).filter(Boolean)[0] || '';
    return [k].concat(vals).concat([rule]);
  });
  s.appendChild(table(['What'].concat(names).concat(['Rule']), rows, names.map((_, i) => i + 1)));
})();
// capabilities
(function(){ const s = sec('caps'); const caps = (D.capabilities || {}).capabilities || []; const apps = (D.apps||[]).map(a => a.name);
  if (!caps.length) { s.appendChild($('p', {cls: 'muted', text: 'No capability map yet: run fuse-map.'})); return; }
  const q = $('input', {type: 'search', placeholder: 'Filter by id, name, domain or class'}); s.appendChild(q);
  const tr = (D.trace || {}).capabilities || {}; const vf = (D.verification || {}).capabilities || {};
  const holder = $('div'); s.appendChild(holder);
  const draw = () => { const f = q.value.toLowerCase(); holder.textContent = '';
    const rows = caps.filter(c => !f || [c.id, c.name, c.domain, c.fusion].join(' ').toLowerCase().includes(f)).map(c => [c.id, c.name, c.domain, pill(c.fusion, c.fusion === 'shared-diverged' ? 'gap' : 'muted')].concat(apps.map(a => c.implementations && c.implementations[a] ? 'yes' : '')).concat([(tr[c.id]||{}).status || '-', vf[c.id] ? pill(vf[c.id].verdict) : '-']));
    holder.appendChild(table(['Id', 'Capability', 'Domain', 'Fusion'].concat(apps).concat(['Design', 'Proof']), rows)); };
  q.addEventListener('input', draw); draw();
  const js = (D.capabilities || {}).journeys || []; if (js.length) { s.appendChild($('h2', {text: 'Journeys'})); js.forEach(j => { const d = $('details', null, [$('summary', {text: j.id + ' ' + j.name + ' (' + (j.persona||'-') + ')'})]); const ol = $('ol'); (j.steps||[]).forEach(st => ol.appendChild($('li', {text: st.label + ' [' + (st.capabilities||[]).join(', ') + ']'}))); d.appendChild(ol); s.appendChild(d); }); }
})();
// design
(function(){ const s = sec('design'); const d = D.design || {}; const screens = (d.screens||[]).filter(x => x.kind === 'screen' || x.kind === 'state');
  if (!screens.length) { s.appendChild($('p', {cls: 'muted', text: 'No design inventory yet: run fuse-design.'})); return; }
  const links = {}; ((D.trace||{}).links||[]).forEach(l => links[l.screen] = l.capabilities);
  const shots = {}; ((D.runs||{}).screenshots||[]).forEach(x => shots[x.screen] = x.app);
  s.appendChild($('p', {cls: 'muted', text: screens.length + ' frames. Where the new app has a screenshot of a screen, it is shown to the right of the design: a person signs visual conformance from these pairs.'}));
  const g = $('div', {cls: 'grid'}); screens.forEach(x => { const box = $('div', {cls: 'shot'}); const pair = $('div', {cls: shots[x.id] ? 'pair' : ''}); if (x.shot) pair.appendChild($('img', {src: D.rel + x.shot, alt: 'design: ' + x.name, loading: 'lazy'})); else pair.appendChild($('div', {cls: 'muted', text: '(no screenshot cached)'})); if (shots[x.id]) pair.appendChild($('img', {src: D.rel + shots[x.id], alt: 'app: ' + x.name, loading: 'lazy'})); box.appendChild(pair); box.appendChild($('div', {text: x.name})); box.appendChild($('div', {cls: 'muted', text: (links[x.id] || ['no capability']).join(', ')})); g.appendChild(box); }); s.appendChild(g);
  const gaps = (D.trace||{}).gaps || {}; if ((gaps.capabilitiesWithoutDesign||[]).length) { s.appendChild($('h2', {text: 'Capabilities with no design'})); s.appendChild($('p', {text: gaps.capabilitiesWithoutDesign.join(', ')})); }
})();
// rules
(function(){ const s = sec('rules'); const r = (D.rules||{}).rules || []; if (!r.length) { s.appendChild($('p', {cls: 'muted', text: 'No rules yet: run fuse-rules.'})); return; }
  s.appendChild(table(['Id', 'Rule', 'App', 'Capability', 'Category', 'Priority', 'Confidence', 'Source'], r.map(x => [x.id, x.name, x.app, x.capability || '-', x.category, x.priority, x.confidence, x.source])));
  const c = (D.rules||{}).conflicts || []; if (c.length) { s.appendChild($('h2', {text: 'Cross-app conflicts'})); s.appendChild(table(['Capability', 'Rules', 'Difference'], c.map(x => [x.capability || '-', (x.rules||[]).join(', '), x.difference]))); }
})();
// decisions
(function(){ const s = sec('decisions'); const d = (D.decisions||{}).decisions || {}; const ids = Object.keys(d);
  s.appendChild($('p', {cls: 'muted', text: (S.openQuestions || 0) + ' open question(s). Only a person answers them, with fuse-review.'}));
  if (ids.length) s.appendChild(table(['Id', 'Kind', 'About', 'Choice', 'Note', 'By', 'When'], ids.map(k => [k, d[k].kind, d[k].about, d[k].choice, d[k].note, d[k].by, (d[k].at||'').slice(0,10)])));
})();
// plan
(function(){ const s = sec('plan'); const b = D.brief || {}; if (!b.exists) { s.appendChild($('p', {cls: 'muted', text: 'No brief yet: run fuse-brief.'})); return; }
  s.appendChild($('p', null, [pill(b.approved ? 'approved' : 'not approved', b.approved ? 'pass' : 'gap'), ' ', b.approved ? ('by ' + b.approvedBy + (b.covers ? ', covers ' + b.covers : '')) : 'Nothing is built before a person signs the Approval block.']));
  s.appendChild(table(['Phase', 'Name', 'Command', 'Capabilities', 'Scale', 'Risk'], (b.phases||[]).map(p => [p.number, p.name, p.command, (p.capabilities||[]).join(', '), p.scale, p.risk])));
})();
// proof
(function(){ const s = sec('proof'); const v = (D.verification||{}).capabilities || {}; const ids = Object.keys(v); const checks = (D.verification||{}).checks || [];
  if (!ids.length) { s.appendChild($('p', {cls: 'muted', text: 'Nothing verified yet: build a capability, then run fuse-verify.'})); return; }
  s.appendChild($('p', {cls: 'muted', text: 'Computed by scripts/fusion_proof.py from evidence files, never by a model. Visual conformance is signed by a person.'}));
  s.appendChild(table(['Capability', 'Name', 'Verdict'].concat(checks), ids.map(k => [k, v[k].name, pill(v[k].verdict)].concat(checks.map(c => pill((v[k].checks[c]||{}).status || '-'))))));
  ids.forEach(k => { const d = $('details', null, [$('summary', {text: k + ' ' + v[k].name + ': ' + v[k].verdict})]); const ul = $('ul'); checks.forEach(c => ul.appendChild($('li', {text: c + ' (' + ((v[k].checks[c]||{}).status||'-') + '): ' + ((v[k].checks[c]||{}).detail||'')}))); d.appendChild(ul); s.appendChild(d); });
})();
// security
(function(){ const s = sec('security'); if (!D.security) { s.appendChild($('p', {cls: 'muted', text: 'No security review yet: run fuse-harden.'})); return; } s.appendChild($('pre', {text: D.security})); })();
})();
"""


def sha(text):
    return "sha256-" + base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode("ascii")


def safe_read(path, limit=200_000):
    base = os.path.basename(path)
    if ".local." in base or base.startswith("SECRETS") or os.path.islink(path) or not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read(limit)


def collect(ws, program):
    pdir = program_dir(ws, program)
    prog = load_json(os.path.join(pdir, "program.json")) or {}
    inv = {}
    for a in prog.get("apps", []):
        data = load_json(os.path.join(pdir, "apps", a["name"], "inventory.json"))
        if data:
            inv[a["name"]] = {"counts": data.get("counts"), "rules": data.get("rules")}
    design = load_json(os.path.join(pdir, "design", "design.json")) or {}
    runs = load_json(os.path.join(pdir, "evidence", "test-runs.json")) or {}
    brief = parse_brief(os.path.join(pdir, "FUSION_BRIEF.md"))
    status = statusmod.summary(ws, program) if prog else {}
    security = safe_read(os.path.join(pdir, "SECURITY_FINDINGS.md"), 60_000)
    return {
        "program": program, "apps": prog.get("apps", []), "status": status, "inventories": inv,
        "capabilities": load_json(os.path.join(pdir, "capabilities.json")) or {},
        "trace": load_json(os.path.join(pdir, "traceability.json")) or {},
        "design": {"screens": [{k: s.get(k) for k in ("id", "name", "kind", "shot", "page")} for s in design.get("screens", [])]},
        "rules": load_json(os.path.join(pdir, "rules.json")) or {},
        "decisions": load_json(os.path.join(pdir, "DECISIONS.json")) or {},
        "brief": brief, "verification": load_json(os.path.join(pdir, "VERIFICATION.json")) or {},
        "runs": {"screenshots": runs.get("screenshots") or []}, "security": security,
        # images are referenced relative to the workspace root; the page lives in analysis/<program>/
        "rel": "../../",
    }


def render(data):
    payload = json.dumps(data, ensure_ascii=False, default=str)
    payload = payload.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    csp = (f"default-src 'none'; img-src 'self' data: file:; style-src '{sha(STYLE)}'; script-src '{sha(SCRIPT)}'; "
           "base-uri 'none'; form-action 'none'")
    title = re.sub(r"[^A-Za-z0-9 _-]", "", data["program"])
    return ("<!doctype html>\n<html lang=\"en\"><head><meta charset=\"utf-8\">"
            f"<meta http-equiv=\"Content-Security-Policy\" content=\"{csp}\">"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">"
            f"<title>App Fusion: {title}</title><style>{STYLE}</style></head><body>"
            f"<header><h1>App Fusion: {title}</h1><p>One page with everything found so far. Refreshed by every step; "
            "the files under analysis/ are the source of truth.</p></header><nav></nav><main>"
            + "".join(f"<section id=\"{s}\"></section>" for s in ("overview", "apps", "caps", "design", "rules", "decisions", "plan", "proof", "security"))
            + f"</main><script type=\"application/json\" id=\"data\">{payload}</script><script>{SCRIPT}</script></body></html>\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("program")
    ap.add_argument("--workspace")
    ap.add_argument("--out")
    args = ap.parse_args()
    ws = workspace(args.workspace)
    check_name(args.program, "program")
    pdir = program_dir(ws, args.program)
    if not os.path.isdir(pdir):
        print(f"nothing found under analysis/{args.program}/")
        sys.exit(1)
    out = args.out or os.path.join(pdir, "REPORT.html")
    write_text(out, render(collect(ws, args.program)))
    print(f"wrote {os.path.relpath(out, ws)}")


if __name__ == "__main__":
    main()
