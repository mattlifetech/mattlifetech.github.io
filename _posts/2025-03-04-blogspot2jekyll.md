---
title: "Migrate Blogspot Posts to Your Own Jekyll Website"
layout: single
excerpt: "Step-by-step guide to exporting your Blogger posts and converting them to Jekyll format."
date: 2025-03-04
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/blogger_teaser.webp
categories: [Jekyll, Blogging]
tags: [Blogger, Jekyll, Website Migration]
---


![blogtojek](https://raw.githubusercontent.com/mattchoo2/mattchoo2.github.io/main/assets/images/blogger_teaser.webp)

# Migrate Blogspot Posts to Your Own Jekyll Website

If you're moving from **Blogger (Blogspot)** to a self-hosted **Jekyll website**, this guide will walk you through the entire process.

---

## Step 1: Export Your Blogspot Posts

1. Log in to your **Blogger Dashboard**.
2. Navigate to **Settings > Manage Blog**.
3. Under "Download Content," click **Download**.
4. This will generate an `XML` file containing all your blog posts.

Save this file as `blog-export.xml`.

---

## Step 2: Install Requirements

You'll need **Python** installed on your system. Then, install the required dependencies:

```sh
pip install lxml
```

---

## Step 3: Convert Blogger Posts to Jekyll Format

Use the following `blogger_to_jekyll.py` script to convert the exported XML file into Jekyll-compatible Markdown files.

```python
import os
import re
import html
import xml.etree.ElementTree as ET

def clean_filename(title):
    """Convert title to a valid filename"""
    title = re.sub(r'[^\w\s-]', '', title).strip().lower()
    return re.sub(r'[\s]+', '-', title)

def blogger_to_jekyll(xml_file, output_dir="_posts"):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    ns = {'default': 'http://www.w3.org/2005/Atom'}
    entries = root.findall("default:entry", ns)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for entry in entries:
        title = entry.find("default:title", ns).text
        content = entry.find("default:content", ns).text
        date = entry.find("default:published", ns).text[:10]  # Extract YYYY-MM-DD
        
        if title and content:
            filename = f"{date}-{clean_filename(title)}.md"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"title: \"{html.unescape(title)}\"\n")
                f.write(f"date: {date}\n")
                f.write(f"layout: post\n")
                f.write(f"---\n\n")
                f.write(html.unescape(content))

    print(f"Converted {len(entries)} posts to Jekyll format!")

# Example usage
blogger_to_jekyll("blog-export.xml")
```

### What This Script Does:
- Reads the **Blogger XML export**.
- Extracts **title, content, and publication date**.
- Saves posts in Jekyll's `_posts` folder with **YYYY-MM-DD-title.md** format.
- Preserves post content and converts it into Markdown format.

Run the script:
```sh
python blogger_to_jekyll.py
```

This will generate `.md` files in the `_posts` directory.

---

## Step 4: Upload Posts to Jekyll Website

1. Move the generated `.md` files to your **Jekyll project's `_posts`** folder.
2. Commit and push changes to your GitHub repository:

```sh
git add _posts/*
git commit -m "Migrated Blogger posts to Jekyll"
git push origin main
```

3. Deploy your site:
   - If using **GitHub Pages**, the changes will be reflected automatically.
   - If self-hosting, rebuild the site using:

   ```sh
   bundle exec jekyll build
   bundle exec jekyll serve
   ```

Your Blogger posts are now successfully migrated to your Jekyll website!

---

By following this guide, you can seamlessly transition from Blogger to Jekyll, keeping full control over your content. 🚀
