#!/usr/bin/env python3
"""
Migrate Medium export to Jekyll posts.

Usage:
    python3 scripts/medium_to_jekyll.py /path/to/medium-export/posts/

Medium export: Medium Settings → Account → Export content → unzip the downloaded file.
The posts are in the 'posts' subfolder of the export.

What this does:
- Converts Medium HTML → Jekyll markdown with frontmatter
- Preserves titles, dates, tags, images (as external Medium CDN links)
- Skips drafts (unpublished posts)
- Generates clean slugs for filenames
"""

import argparse
import os
import re
import sys
import unicodedata
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "_posts"


# ── Minimal HTML → Markdown converter ────────────────────────────────────────

class MediumHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.md = []
        self._stack = []
        self._skip = False
        self.title = ""
        self.subtitle = ""
        self.tags = []
        self.published_at = ""
        self._in_title = False
        self._in_subtitle = False
        self._in_tag = False
        self._link_href = ""
        self._in_pre = False
        self._code_lang = ""
        self._img_count = 0
        self._figcaption = ""
        self._in_figcaption = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self._stack.append(tag)

        if tag in ("script", "style", "nav", "footer", "header"):
            self._skip = True
            return
        if self._skip:
            return

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
        elif tag == "strong" or tag == "b":
            self.md.append("**")
        elif tag == "em" or tag == "i":
            self.md.append("*")
        elif tag == "blockquote":
            self.md.append("\n\n> ")
        elif tag == "ul":
            self.md.append("\n")
        elif tag == "ol":
            self.md.append("\n")
        elif tag == "li":
            parent = next((t for t in reversed(self._stack[:-1]) if t in ("ul", "ol")), "ul")
            self.md.append("\n- " if parent == "ul" else "\n1. ")
        elif tag == "a":
            self._link_href = attrs.get("href", "")
            self.md.append("[")
        elif tag == "img":
            src = attrs.get("src", "")
            alt = attrs.get("alt", "image")
            if src:
                self.md.append(f"\n\n![{alt}]({src})\n")
                self._img_count += 1
        elif tag == "code":
            if "pre" in self._stack:
                pass  # handled by pre
            else:
                self.md.append("`")
        elif tag == "pre":
            self._in_pre = True
            lang = attrs.get("data-lang", attrs.get("class", ""))
            lang = re.sub(r"[^a-z0-9]", "", lang.lower()) if lang else ""
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
        elif tag == "a" and "tag" in attrs.get("class", ""):
            self._in_tag = True

    def handle_endtag(self, tag):
        if tag in ("script", "style", "nav", "footer", "header"):
            self._skip = False
        if self._skip:
            if self._stack and self._stack[-1] == tag:
                self._stack.pop()
            return

        if self._stack and self._stack[-1] == tag:
            self._stack.pop()

        if tag == "h1" and self._in_title:
            self._in_title = False
        elif tag in ("strong", "b"):
            self.md.append("**")
        elif tag in ("em", "i"):
            self.md.append("*")
        elif tag == "a":
            href = self._link_href
            # Clean Medium tracking URLs
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
        if self._skip:
            return
        if self._in_title:
            self.title += data
            return
        if self._in_figcaption:
            self._figcaption += data
            return
        self.md.append(data)

    def get_markdown(self):
        text = "".join(self.md)
        # Clean up excessive blank lines
        text = re.sub(r"\n{4,}", "\n\n", text)
        return text.strip()


# ── Helpers ───────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^\w\s-]", "", text.lower())
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:60]


def parse_date_from_filename(filename: str) -> str:
    m = re.match(r"(\d{4}-\d{2}-\d{2})", filename)
    return m.group(1) if m else datetime.today().strftime("%Y-%m-%d")


def extract_tags_from_html(html: str) -> list[str]:
    # Medium tags appear as links with class "tag"
    return re.findall(r'class="[^"]*tag[^"]*"[^>]*>\s*([^<]+)\s*<', html, re.IGNORECASE)


def extract_subtitle(html: str) -> str:
    m = re.search(r'<h2[^>]*>(.*?)</h2>', html, re.DOTALL)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    # Try subtitle/section description
    m = re.search(r'<p[^>]*class="[^"]*subtitle[^"]*"[^>]*>(.*?)</p>', html, re.DOTALL)
    if m:
        return re.sub(r"<[^>]+>", "", m.group(1)).strip()
    return ""


def html_to_jekyll(html_path: Path, out_dir: Path) -> str | None:
    html = html_path.read_text(encoding="utf-8", errors="ignore")

    # Skip drafts — Medium marks them with 'draft' in the filename or no time element
    if "draft" in html_path.name.lower():
        return None

    # Extract date from filename first, fallback to <time> tag
    date_str = parse_date_from_filename(html_path.name)

    # Parse HTML
    parser = MediumHTMLParser()
    # Only parse the article body
    article_match = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
    body_html = article_match.group(1) if article_match else html

    parser.feed(body_html)

    if parser.published_at:
        date_str = parser.published_at

    title = parser.title.strip() or html_path.stem
    content = parser.get_markdown()
    tags = extract_tags_from_html(html)
    subtitle = extract_subtitle(html)

    # Generate excerpt from first paragraph
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip() and not p.startswith("#")]
    excerpt = paragraphs[0][:200].replace('"', "'") if paragraphs else ""

    slug = slugify(title)
    out_filename = f"{date_str}-{slug}.md"
    out_path = out_dir / out_filename

    # Build frontmatter
    tags_yaml = "\n".join(f"  - {t}" for t in tags) if tags else ""
    tags_block = f"tags:\n{tags_yaml}" if tags_yaml else ""

    frontmatter = f"""---
title: "{title.replace('"', "'")}"
layout: single
date: {date_str}
excerpt: "{excerpt}"
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/filler.webp
categories: [Blog]
{tags_block}
author_profile: true
read_time: true
share: true
---

"""

    out_path.write_text(frontmatter + content + "\n", encoding="utf-8")
    return out_filename


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Convert Medium export to Jekyll posts")
    parser.add_argument("posts_dir", help="Path to the 'posts' folder inside your Medium export")
    parser.add_argument("--out", default=str(POSTS_DIR), help=f"Output directory (default: {POSTS_DIR})")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    posts_dir = Path(args.posts_dir)
    out_dir = Path(args.out)

    if not posts_dir.exists():
        print(f"Error: {posts_dir} does not exist")
        sys.exit(1)

    html_files = sorted(posts_dir.glob("*.html"))
    if not html_files:
        print(f"No HTML files found in {posts_dir}")
        sys.exit(1)

    print(f"Found {len(html_files)} HTML files in {posts_dir}")
    print(f"Output → {out_dir}\n")

    ok, skipped = 0, 0
    for f in html_files:
        if args.dry_run:
            print(f"  would process: {f.name}")
            ok += 1
            continue
        result = html_to_jekyll(f, out_dir)
        if result:
            print(f"  ✓ {result}")
            ok += 1
        else:
            print(f"  – skipped (draft): {f.name}")
            skipped += 1

    print(f"\nDone: {ok} converted, {skipped} skipped.")
    if ok and not args.dry_run:
        print(f"\nNext steps:")
        print(f"  1. Review posts in {out_dir}")
        print(f"  2. git add _posts/ && git commit -m 'Migrate articles from Medium'")
        print(f"  3. git push origin main")


if __name__ == "__main__":
    main()
