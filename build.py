#!/usr/bin/env python3
"""Wrap lesson body fragments into standalone HTML pages with a shared nav.

Each lessons/_lN_body.html is a fragment: <title>, <style>, and body markup,
exactly as authored for the Artifact harness (no <!doctype>/<html>/<head>/<body>).
This wraps them so they render standalone on GitHub Pages, and injects a shared
top nav (breadcrumb back to the path + a light/dark theme toggle).
"""
import re
import pathlib

ROOT = pathlib.Path(__file__).parent
LESSONS = ROOT / "lessons"

# Shared nav: breadcrumb home + theme toggle. Styled to inherit each page's tokens.
NAV_CSS = """
  /* shared top nav (injected by build.py) */
  .pbn {
    position: sticky; top: 0; z-index: 50;
    display: flex; align-items: center; justify-content: space-between;
    gap: 1rem;
    padding: .7rem 1.5rem;
    background: color-mix(in srgb, var(--paper) 88%, transparent);
    backdrop-filter: saturate(140%) blur(8px);
    -webkit-backdrop-filter: saturate(140%) blur(8px);
    border-bottom: 1px solid var(--rule);
    font-family: var(--mono);
    font-size: .74rem;
    letter-spacing: .06em;
  }
  .pbn a.home { color: var(--ink-soft); text-decoration: none; display: inline-flex; align-items: center; gap: .5rem; }
  .pbn a.home:hover { color: var(--accent); }
  .pbn a.home .arw { color: var(--accent); }
  .pbn .brand { text-transform: uppercase; letter-spacing: .16em; color: var(--ink-faint); }
  .pbn button.tt {
    font-family: var(--mono); font-size: .74rem; letter-spacing: .04em;
    background: transparent; color: var(--ink-soft);
    border: 1px solid var(--rule-strong); border-radius: 6px;
    padding: .35em .8em; cursor: pointer; transition: color .15s, border-color .15s;
  }
  .pbn button.tt:hover { color: var(--accent); border-color: var(--accent); }
  .pbn button.tt:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
"""

NAV_HTML = """<nav class="pbn">
  <a class="home" href="../index.html"><span class="arw">&larr;</span> the path</a>
  <span class="brand">paper breadcrumbs</span>
  <button class="tt" onclick="pbTheme()" aria-label="Toggle light or dark theme">theme</button>
</nav>
"""

THEME_JS = """
<script>
  // shared theme toggle (injected by build.py)
  (function(){
    var saved = null;
    try { saved = localStorage.getItem('pb-theme'); } catch(e){}
    if(saved){ document.documentElement.setAttribute('data-theme', saved); }
  })();
  function pbTheme(){
    var el = document.documentElement;
    var cur = el.getAttribute('data-theme');
    if(!cur){
      cur = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    var next = cur === 'dark' ? 'light' : 'dark';
    el.setAttribute('data-theme', next);
    try { localStorage.setItem('pb-theme', next); } catch(e){}
  }
</script>
"""

SKELETON = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="../favicon.svg" type="image/svg+xml">
{title}
<style>{nav_css}</style>
{style}
</head>
<body>
{nav}
{body}
{theme_js}
{scripts}
</body>
</html>
"""

def build(fragment_path, out_path):
    src = fragment_path.read_text(encoding="utf-8")

    title_m = re.search(r"<title>.*?</title>", src, re.S)
    title = title_m.group(0) if title_m else "<title>Paper Breadcrumbs</title>"

    style_m = re.search(r"<style>.*?</style>", src, re.S)
    style = style_m.group(0) if style_m else ""

    # everything after </style> up to first <script> is the body markup;
    # scripts collected separately and placed at end of body.
    after_style = src[style_m.end():] if style_m else src
    scripts = "\n".join(re.findall(r"<script>.*?</script>", after_style, re.S))
    body = re.sub(r"<script>.*?</script>", "", after_style, flags=re.S).strip()

    html = SKELETON.format(
        title=title, nav_css=NAV_CSS, style=style,
        nav=NAV_HTML, body=body, theme_js=THEME_JS, scripts=scripts,
    )
    out_path.write_text(html, encoding="utf-8")
    print(f"built {out_path.relative_to(ROOT)}  ({len(html):,} bytes)")

if __name__ == "__main__":
    build(LESSONS / "_l1_body.html", LESSONS / "01-jacobian.html")
    build(LESSONS / "_l2_body.html", LESSONS / "02-jlens.html")
    build(LESSONS / "_l3_body.html", LESSONS / "03-workspace-tests.html")
