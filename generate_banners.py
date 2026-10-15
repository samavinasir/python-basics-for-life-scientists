#!/usr/bin/env python3
"""Generate B-vac-style numbered section banners as SVG files.

Usage:  python generate_banners.py
Edit SECTIONS below (or the colours) and re-run. Output: assets/banners/NN-slug.svg
"""
import os, re

# --- Theme (TraceReview palette; change these for other repos) -------------
ACCENT   = "#20b8aa"   # left bar + label colour
TITLE    = "#172b45"   # title text
CARD     = "#eef3f8"   # card fill
BORDER   = "#cdd8e4"   # card outline (keeps it visible on light GitHub theme)
NUMBER   = "#cbd6e2"   # large faded number
MONO     = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
SANS     = "-apple-system, 'Segoe UI', Helvetica, Arial, sans-serif"

# --- Sections: (label, title) ----------------------------------------------
SECTIONS = [
    ("OVERVIEW",        "Overview"),
    ("🎯 Target Audience",    "Who this content is for"),
    ("📚 What You Will Learn",        "Key takeaways and insights"),
    ("🗂️ Module Outline",  "Structure and main topics"),
    ("⚡ Quickstart Code Example", "Fast implementation snippet"),
    ("💻 Setup & Environment Installation",        "Steps to configure workspace"),
    ("📄 TERMS",           "License"),
]

W, H = 900, 84

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def banner(n, label, title):
    num = f"{n:02d}"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{num} {esc(label.title())}: {esc(title)}">
  <title>{num} / {esc(label)} - {esc(title)}</title>
  <defs>
    <clipPath id="card"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10"/></clipPath>
  </defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="{CARD}" stroke="{BORDER}" stroke-width="1.5"/>
  <g clip-path="url(#card)"><rect x="1" y="1" width="7" height="{H-2}" fill="{ACCENT}"/></g>
  <text x="34" y="31" font-family="{MONO}" font-size="12" font-weight="600" letter-spacing="3" fill="{ACCENT}">{num} / {esc(label)}</text>
  <text x="34" y="62" font-family="{SANS}" font-size="28" font-weight="800" fill="{TITLE}">{esc(title)}</text>
  <text x="{W-30}" y="64" text-anchor="end" font-family="{SANS}" font-size="56" font-weight="800" fill="{NUMBER}">{num}</text>
</svg>
'''

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

os.makedirs("assets/banners", exist_ok=True)
for i, (label, title) in enumerate(SECTIONS, 1):
    path = f"assets/banners/{i:02d}-{slug(title)}.svg"
    with open(path, "w", encoding="utf-8") as f:
        f.write(banner(i, label, title))
    print("wrote", path)
