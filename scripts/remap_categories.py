#!/usr/bin/env python3
"""
Remap messy post categories to 5 clean buckets.

Buckets: Smart Home | Gadgets | Gaming | How-To | Automotive | Blog
"""

import re
import sys
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "_posts"

# keyword → bucket (first match wins; check in order)
VALID_BUCKETS = {"smart home", "gadgets", "gaming", "how-to", "automotive", "blog"}

RULES = [
    # Gallery — leave untouched
    ({"gallery"}, None),

    # Automotive — very specific, keep separate
    ({"automotive", "cars", "car"}, "Automotive"),

    # Smart Home (check BEFORE Gadgets so networking/privacy land here)
    ({"smart home", "home assistant", "home automation", "home security",
      "pi-hole", "pihole", "ad-blocking", "ad blocking",
      "networking", "privacy", "remote access"}, "Smart Home"),

    # Gaming
    ({"gaming", "game optimization", "couch", "couch-coop"}, "Gaming"),

    # How-To — troubleshooting, coding, scripting, apps/productivity guides
    ({"troubleshooting", "python", "coding", "automation", "jekyll",
      "github", "web development", "chrome extension", "chrome extensions",
      "ocr", "vba", "excel", "file management", "image processing",
      "text processing", "llm", "whatsapp", "blogging",
      "apps", "productivity"}, "How-To"),

    # Gadgets — everything hardware/product
    ({"gadgets", "tech", "tablets", "tablet", "wearables", "e-readers",
      "apple", "android", "amazon fire", "media", "streaming",
      "home entertainment", "e-commerce", "shopping", "monitor",
      "bluetooth", "audio", "storage", "nvme", "usb", "keyboard",
      "printer", "projector", "samsung", "xiaomi", "mobile",
      "security", "vr", "ar", "solar", "collectibles", "toys",
      "travel", "budget tech", "ios", "windows"}, "Gadgets"),

    # Blog — opinion and general writing
    ({"blog"}, "Blog"),
]


def detect_bucket(cats_raw: str) -> str | None:
    """Return the target bucket, or None to leave unchanged."""
    cats_lower = {c.strip().strip("'\"").lower()
                  for c in cats_raw.replace("[", "").replace("]", "").split(",")}

    # Already a single clean bucket — leave it alone
    if cats_lower <= VALID_BUCKETS:
        return None

    for keywords, bucket in RULES:
        if bucket is None:  # gallery guard
            if cats_lower & keywords:
                return None  # skip
        elif cats_lower & keywords:
            return bucket

    return "Blog"  # catch-all


def remap_file(path: Path, dry_run: bool) -> tuple[str, str] | None:
    """Returns (old_cats, new_cats) if changed, else None."""
    text = path.read_text(encoding="utf-8")

    # Find categories line(s)
    # Supports both inline `categories: [A, B]` and block form
    inline_m = re.search(r"^categories:\s*\[([^\]]+)\]", text, re.MULTILINE)
    block_m  = re.search(r"^categories:\s*\n((?:  -[^\n]+\n)+)", text, re.MULTILINE)

    if inline_m:
        old_raw = inline_m.group(1)
        bucket = detect_bucket(old_raw)
        if bucket is None:
            return None  # skip (gallery)
        old_cats = f"[{old_raw}]"
        new_line = f"categories:\n  - {bucket}"
        new_text = text[:inline_m.start()] + new_line + text[inline_m.end():]
    elif block_m:
        old_raw = block_m.group(1)
        # Extract actual values
        vals = re.findall(r"-\s*(.+)", old_raw)
        bucket = detect_bucket(", ".join(vals))
        if bucket is None:
            return None
        old_cats = str(vals)
        new_line = f"categories:\n  - {bucket}\n"
        new_text = text[:block_m.start()] + f"categories:\n" + text[block_m.start() + len("categories:\n"):]
        new_text = re.sub(r"^categories:\s*\n((?:  -[^\n]+\n)+)", f"categories:\n  - {bucket}\n", new_text, flags=re.MULTILINE)
    else:
        return None  # no categories found

    if new_text == text:
        return None  # already correct

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")

    return (old_cats, bucket)


def main():
    dry_run = "--dry-run" in sys.argv
    changed = unchanged = 0

    for post in sorted(POSTS_DIR.glob("*.md")):
        result = remap_file(post, dry_run)
        if result:
            old, new = result
            tag = "[dry]" if dry_run else "✓"
            print(f"  {tag} {post.name[:55]:<57}  {old} → [{new}]")
            changed += 1
        else:
            unchanged += 1

    print(f"\n{'[dry-run] ' if dry_run else ''}Changed: {changed}, Unchanged: {unchanged}")


if __name__ == "__main__":
    main()
