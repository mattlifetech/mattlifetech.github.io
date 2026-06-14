#!/usr/bin/env python3
"""
Import product-focused Medium articles to Jekyll.
- Downloads images from Medium CDN to assets/images/medium/
- Rewrites image URLs to local paths
- Keeps original publication dates
- Skips social comments / short replies

Usage:
    python3 scripts/import_medium_products.py
    python3 scripts/import_medium_products.py --dry-run
"""

import argparse
import hashlib
import os
import re
import sys
import unicodedata
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
POSTS_DIR  = REPO_ROOT / "_posts"
IMAGES_DIR = REPO_ROOT / "assets" / "images" / "medium"

EXPORT_DIR = REPO_ROOT / "medium-export-040ac616aba9969b6238d89a183a01765007cccc85715fe24eedcc2742d1eb94" / "posts"

# ── Curated list: product/tech articles with affiliate potential ──────────────
IMPORT_LIST = [
    # Smart home & switches
    ("2025-03-26_Smart-Homes--The-Dream-That-Stalled---Why-People-Are-Losing-Interest-fbb097793987.html",
     ["smart-home", "gadgets"], "Smart Home"),
    ("2025-03-26_Smart-Light-Switches---The-Secrets-Many-Didn-t-Understand-Before-Buying-One-e56743f0bea0.html",
     ["smart-home", "gadgets"], "Smart Home"),
    ("2025-04-06_TTLock-Smart-Deadbolt--A-Budget---Versatile-Guardian-for-Your-Door-72f679be00f3.html",
     ["smart-home", "security", "gadgets"], "Smart Home"),
    ("2025-04-08_Smart-vs--Traditional-Home-Appliances--Is-DIY-Repair-the-Key-to-Saving-Money-and-the-Planet--f1407c4fb9ed.html",
     ["smart-home", "gadgets"], "Smart Home"),
    ("2025-12-15_Mastering-the-2026-Home-Assistant-Shift--Updating-Malaysia-TNB-Energy-Sensors-ab7eb9379e2a.html",
     ["smart-home", "home-assistant", "malaysia"], "Smart Home"),
    # Monitors & display
    ("2025-04-08_HDR-Monitors--Why-Your-Screenshots-Look-Washed-Out--and-Other-Surprising-Facts--8abcdfe7e136.html",
     ["monitor", "display", "gadgets"], "Gadgets"),
    ("2025-04-15_Why-Using-a-TV-as-a-PC-Monitor-Is-a-Bad-Idea--And-How-to-Make-It-Work-If-You-Must--d1ef0e904743.html",
     ["monitor", "tv", "gadgets"], "Gadgets"),
    ("2025-06-05_Portable-Monitors--The-On-the-Go-Productivity-Powerhouse-c3bb5d2e505f.html",
     ["monitor", "productivity", "gadgets"], "Gadgets"),
    # Storage & drives
    ("2025-05-05_Protecting-Yourself-from-NVMe-or-C--Drive-Failure---Practical-Strategies-for-Recovery-a39b06f431e7.html",
     ["storage", "nvme", "pc"], "Gadgets"),
    ("2025-05-07_Why-Monitor-Your-NVMe-SSD-s-Health--7c11ca348fe4.html",
     ["storage", "nvme", "pc"], "Gadgets"),
    ("2025-05-08_You-Don-t-Realize-Your-Storage-Drive-Has-So-Many-Parts---Here-s-What-They-All-Do-8e3076d58e8a.html",
     ["storage", "pc", "gadgets"], "Gadgets"),
    # Audio
    ("2025-05-19_Choosing-the-Right-Bluetooth-Earbuds-for-Background-Media-Consumption-48bcd10c6c6f.html",
     ["audio", "earbuds", "bluetooth", "gadgets"], "Gadgets"),
    ("2025-06-23_Understand-Your-Seamless-Bluetooth-Features-to-Blend-with-It-a65545ed748a.html",
     ["bluetooth", "audio", "gadgets"], "Gadgets"),
    # Peripherals & accessories
    ("2025-04-16_Which-Keyboard-is-Right-for-Your-Xiaomi-Pad-7--65f0f86fa79a.html",
     ["keyboard", "xiaomi", "tablet", "gadgets"], "Gadgets"),
    ("2025-05-19_Why-Your-USB-C-Cable-Won-t-Connect-to-a-Monitor-e8d003827a0d.html",
     ["usb-c", "cable", "gadgets"], "Gadgets"),
    ("2025-08-21_Ditch-the-Drawer-of-Dongles-799e4a14dfd8.html",
     ["usb-hub", "dongles", "gadgets"], "Gadgets"),
    # Laptop & computing
    ("2025-04-09_Why-the-MacBook-Air-M1-Is-Still-the-Best-Budget-MacBook-You-Can-Buy-in-2025-1eb8feb8be40.html",
     ["macbook", "laptop", "apple", "gadgets"], "Gadgets"),
    # Gaming
    ("2025-04-05_Cost-Effective-Gaming-Upgrades--Leveraging-LSFG-for-Better-Performance-2cea5156404e.html",
     ["gaming", "pc", "gadgets"], "Gaming"),
    ("2025-04-16_Why-Couch-Co-op-Games-Are-Disappearing---And-Why-We-Need-Them-Back-8509e27cae66.html",
     ["gaming", "couch-coop"], "Gaming"),
    # Printer
    ("2025-03-28_A-Must-Have-Printer-You-Didn-t-Realize-in-Today-s-Paperless-Society-cdb7b673dfb9.html",
     ["printer", "gadgets"], "Gadgets"),
    # Mobile & tablets
    ("2025-03-27_Unlocking-the-Hidden-Power-of-Old-Samsung-Phones--The-Magic-of-the-ROUTINE-App-e920ba9447eb.html",
     ["samsung", "android", "mobile"], "Gadgets"),
    ("2025-05-11_The-Best-Way-to-Improve-Remote-Desktop-Experience-from-a-Tablet--Use-PowerToys-to-Map-Two-Essential--7df0f9b94a17.html",
     ["tablet", "remote-desktop", "productivity"], "How-To"),
    # VR/AR
    ("2025-03-27_Challenges-of-VR---AR-Glasses-for-Users-Over-40-2a41e04c09be.html",
     ["vr", "ar", "glasses", "gadgets"], "Gadgets"),
    # Solar & energy
    ("2025-04-11_Navigating-Malaysia-s-Solar-NEM-3-0--707531224e04.html",
     ["solar", "malaysia", "energy"], "Smart Home"),
    # Pop culture collectibles
    ("2025-08-11_The-Labubu-Effect-eb934b58c2dc.html",
     ["collectibles", "toys", "trend"], "Blog"),
    # China travel (travel accessories)
    ("2025-12-16_China-Travel-2025--A-Malaysian-s-Guide-to-Surviving-the-Cashless-Great-Wall-1015675d9074.html",
     ["travel", "china", "malaysia", "cashless"], "Blog"),
]


# ── HTML → Markdown parser ────────────────────────────────────────────────────

class MediumHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.md = []
        self._stack = []
        self._skip = False
        self.title = ""
        self._in_title = False
        self._link_href = ""
        self._in_pre = False
        self._figcaption = ""
        self._in_figcaption = False
        self.published_at = ""
        self.images = []  # (original_url, local_path)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._stack.append(tag)
        if tag in ("script", "style", "nav", "footer", "header"):
            self._skip = True; return
        if self._skip: return

        if tag == "h1" and not self.title:
            self._in_title = True
        elif tag == "h1":
            self.md.append("\n## ")
        elif tag == "h2":
            self.md.append("\n## ")
        elif tag == "h3":
            self.md.append("\n### ")
        elif tag == "h4":
            self.md.append("\n#### ")
        elif tag == "p":
            self.md.append("\n\n")
        elif tag in ("strong", "b"):
            self.md.append("**")
        elif tag in ("em", "i"):
            self.md.append("*")
        elif tag == "blockquote":
            self.md.append("\n\n> ")
        elif tag in ("ul", "ol"):
            self.md.append("\n")
        elif tag == "li":
            parent = next((t for t in reversed(self._stack[:-1]) if t in ("ul","ol")), "ul")
            self.md.append("\n- " if parent == "ul" else "\n1. ")
        elif tag == "a":
            self._link_href = attrs.get("href", "")
            self.md.append("[")
        elif tag == "img":
            src = attrs.get("src", "")
            alt = attrs.get("alt", "image")
            if src and "cdn-images" in src:
                placeholder = f"__IMG_{len(self.images)}__"
                self.images.append((src, None, placeholder))
                self.md.append(f"\n\n![{alt}]({placeholder})\n")
        elif tag == "code":
            if "pre" not in self._stack:
                self.md.append("`")
        elif tag == "pre":
            self._in_pre = True
            lang = re.sub(r"[^a-z0-9]", "", attrs.get("data-lang", attrs.get("class", "")).lower())
            self.md.append(f"\n\n```{lang}\n")
        elif tag == "hr":
            self.md.append("\n\n---\n")
        elif tag == "br":
            self.md.append("  \n")
        elif tag == "figure":
            self._figcaption = ""
        elif tag == "figcaption":
            self._in_figcaption = True
        elif tag == "time":
            dt = attrs.get("datetime", "")
            if dt and not self.published_at:
                self.published_at = dt[:10]

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer", "header"):
            self._skip = False
        if self._skip:
            if self._stack and self._stack[-1] == tag: self._stack.pop()
            return
        if self._stack and self._stack[-1] == tag: self._stack.pop()

        if tag == "h1" and self._in_title:
            self._in_title = False
        elif tag in ("strong", "b"):
            self.md.append("**")
        elif tag in ("em", "i"):
            self.md.append("*")
        elif tag == "a":
            href = self._link_href
            if "medium.com" in href and "?source=" in href:
                href = href.split("?")[0]
            self.md.append(f"]({href})")
            self._link_href = ""
        elif tag == "code" and "pre" not in self._stack:
            self.md.append("`")
        elif tag == "pre":
            self._in_pre = False
            self.md.append("\n```\n")
        elif tag == "figcaption":
            self._in_figcaption = False
            if self._figcaption:
                self.md.append(f"\n*{self._figcaption.strip()}*\n")
                self._figcaption = ""

    def handle_data(self, data):
        if self._skip: return
        if self._in_title:
            self.title += data; return
        if self._in_figcaption:
            self._figcaption += data; return
        self.md.append(data)

    def get_markdown(self):
        text = "".join(self.md)
        text = re.sub(r"\n{4,}", "\n\n", text)
        return text.strip()


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:60]


def url_to_local_name(url: str, slug: str, idx: int) -> str:
    ext = os.path.splitext(url.split("?")[0])[-1] or ".jpg"
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp"):
        ext = ".jpg"
    return f"{slug}-{idx}{ext}"


def download_image(url: str, dest: Path, dry_run: bool) -> bool:
    if dest.exists():
        return True
    if dry_run:
        print(f"    [dry-run] would download → {dest.name}")
        return True
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r, open(dest, "wb") as f:
            f.write(r.read())
        print(f"    ↓ {dest.name}")
        return True
    except Exception as e:
        print(f"    ✗ {url}: {e}")
        return False


def parse_date_from_filename(filename: str) -> str:
    m = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    return m.group(1) if m else "2025-01-01"


# ── Main conversion ───────────────────────────────────────────────────────────

def convert(html_file: Path, tags: list, category: str, dry_run: bool) -> str | None:
    html = html_file.read_text(encoding="utf-8", errors="ignore")

    article_match = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
    body_html = article_match.group(1) if article_match else html

    parser = MediumHTMLParser()
    parser.feed(body_html)

    date_str = parse_date_from_filename(html_file.name)
    if parser.published_at:
        date_str = parser.published_at

    title = parser.title.strip() or html_file.stem
    # slugify title; strip any leading date the slugifier may carry over
    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", slugify(title))
    content = parser.get_markdown()

    # Download images and rewrite placeholders
    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    first_local = None
    for i, (url, _, placeholder) in enumerate(parser.images):
        local_name = url_to_local_name(url, slug, i)
        local_path = IMAGES_DIR / local_name
        ok = download_image(url, local_path, dry_run)
        web_path = f"/assets/images/medium/{local_name}"
        content = content.replace(placeholder, web_path if ok else url)
        if i == 0 and ok:
            first_local = web_path

    teaser = first_local or "/assets/images/filler.webp"

    # First paragraph as excerpt
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip() and not p.startswith("#")]
    excerpt = re.sub(r"!\[.*?\]\(.*?\)", "", paragraphs[0])[:200].replace('"', "'").strip() if paragraphs else ""

    tags_yaml = "\n".join(f"  - {t}" for t in tags)
    frontmatter = f"""---
title: "{title.replace('"', "'")}"
layout: single
date: {date_str}
excerpt: "{excerpt}"
header:
  teaser: {teaser}
categories:
  - {category}
tags:
{tags_yaml}
author_profile: true
read_time: true
share: true
related: true
---

"""

    out_filename = f"{date_str}-{slug}.md"
    out_path = POSTS_DIR / out_filename

    if dry_run:
        print(f"  [dry-run] {out_filename}  (images: {len(parser.images)})")
        return out_filename

    if out_path.exists():
        print(f"  – skipped (exists): {out_filename}")
        return None

    out_path.write_text(frontmatter + content + "\n", encoding="utf-8")
    print(f"  ✓ {out_filename}  (images: {len(parser.images)})")
    return out_filename


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not EXPORT_DIR.exists():
        print(f"Export dir not found: {EXPORT_DIR}")
        sys.exit(1)

    print(f"Importing {len(IMPORT_LIST)} product articles → {POSTS_DIR}\n")
    ok = skipped = 0
    for filename, tags, category in IMPORT_LIST:
        html_file = EXPORT_DIR / filename
        if not html_file.exists():
            print(f"  ✗ NOT FOUND: {filename}")
            continue
        result = convert(html_file, tags, category, args.dry_run)
        if result:
            ok += 1
        else:
            skipped += 1

    print(f"\nDone: {ok} imported, {skipped} skipped.")
    if ok and not args.dry_run:
        print("\nNext: git add _posts/ assets/images/medium/ && git commit && git push")


if __name__ == "__main__":
    main()
