#!/usr/bin/env python3
"""
Fetch product images for affiliate cards.
Follows short affiliate URLs, extracts og:image, downloads to assets/images/products/.
Updates _data/affiliate_links.yml with local image paths.

Usage:
    python3 scripts/fetch_product_images.py
    python3 scripts/fetch_product_images.py --product xiaomi_pad7   # single product
    python3 scripts/fetch_product_images.py --force                  # re-download existing
"""

import argparse
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).parent.parent
YAML_PATH = REPO_ROOT / "_data" / "affiliate_links.yml"
IMG_DIR   = REPO_ROOT / "assets" / "images" / "products"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


def follow_redirect(url: str) -> str:
    """Follow redirects and return the final URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    opener = urllib.request.build_opener(urllib.request.HTTPRedirectHandler())
    try:
        resp = opener.open(req, timeout=10)
        return resp.url
    except Exception:
        return url


def fetch_og_image(url: str) -> str | None:
    """Fetch a URL and extract og:image meta tag content."""
    final_url = follow_redirect(url)
    req = urllib.request.Request(final_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            html = resp.read(200_000).decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"  ✗ fetch error: {e}")
        return None

    # Match og:image or og:image:secure_url
    match = re.search(
        r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
        html, re.IGNORECASE
    ) or re.search(
        r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
        html, re.IGNORECASE
    )
    if not match:
        return None
    img = match.group(1).strip()
    # Fix protocol-relative URLs
    if img.startswith("//"):
        img = "https:" + img
    return img


def download_image(img_url: str, dest: Path) -> bool:
    """Download an image URL to dest path. Returns True on success."""
    req = urllib.request.Request(img_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
        return True
    except Exception as e:
        print(f"  ✗ download error: {e}")
        return False


def ext_from_url(url: str) -> str:
    path = url.split("?")[0].split("#")[0]
    suffix = Path(path).suffix.lower()
    return suffix if suffix in {".jpg", ".jpeg", ".png", ".webp", ".gif"} else ".jpg"


def pick_source_url(product: dict) -> str | None:
    """Return the best product URL to scrape og:image from."""
    # source_url is explicitly set for scraping — use it first
    if product.get("source_url"):
        return product["source_url"]
    # Then prefer direct product pages over search/short URLs
    for key in ("official", "amazon"):
        url = product.get(key)
        if url and "search" not in url:
            return url
    # Skip Shopee short links (s.shopee.com.my) — they don't serve og:image
    for key in ("lazada", "aliexpress"):
        url = product.get(key)
        if url and "s.shopee" not in url:
            return url
    return None


def main():
    parser = argparse.ArgumentParser(description="Fetch affiliate product images")
    parser.add_argument("--product", help="Only update this product key")
    parser.add_argument("--force", action="store_true", help="Re-download even if image exists")
    args = parser.parse_args()

    with open(YAML_PATH) as f:
        data = yaml.safe_load(f)

    changed = False
    for key, product in data.items():
        if args.product and key != args.product:
            continue

        # Skip if image already set to a local products/ path and not forcing
        current_image = product.get("image", "")
        if current_image.startswith("/assets/images/products/") and not args.force:
            print(f"[{key}] skipping — image already set to {current_image}")
            continue

        source_url = pick_source_url(product)
        if not source_url:
            print(f"[{key}] skipping — no URL found")
            continue

        print(f"[{key}] fetching og:image from {source_url[:60]}...")
        og_img = fetch_og_image(source_url)

        if not og_img:
            print(f"[{key}] ✗ no og:image found")
            time.sleep(1)
            continue

        print(f"  og:image → {og_img[:80]}")
        ext = ext_from_url(og_img)
        dest = IMG_DIR / f"{key}{ext}"
        local_path = f"/assets/images/products/{key}{ext}"

        if download_image(og_img, dest):
            print(f"  ✓ saved → {dest.name}")
            product["image"] = local_path
            changed = True
        else:
            print(f"  ✗ download failed, keeping existing image")

        time.sleep(1.5)  # be polite

    if changed:
        with open(YAML_PATH, "w") as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        print(f"\n✓ Updated {YAML_PATH}")
    else:
        print("\nNo changes made.")


if __name__ == "__main__":
    main()
