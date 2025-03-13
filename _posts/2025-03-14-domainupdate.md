---
title: "Batch Update Jekyll Post Links When Changing Domain Name"
layout: single
excerpt: "Learn how to efficiently update Jekyll post links when migrating your GitHub Pages domain."
date: 2025-03-14
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/domainupdate.webp
categories: [Jekyll, GitHub]
tags: [Jekyll, GitHub, Automation, Python]
---

![domainupdate](https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/main/assets/images/domainupdate.webp)

# Batch Update Jekyll Post Links When Changing Domain Name

When migrating a Jekyll website to a new domain name on GitHub Pages, updating image and repository links in all markdown (`.md`) files can be time-consuming. This guide provides a **Python script** to automate the process.

## Problem: Old Links in Markdown Files

After renaming a GitHub repository, the old links may still work due to GitHub’s automatic redirection. However, it's best to update them to:
- **Avoid redirection delays**
- **Ensure long-term compatibility**
- **Maintain consistency** across posts

### Example of Old vs. New Links
#### Before (Old Domain: `ABC.github.io`)
```md
![example](https://raw.githubusercontent.com/ABC/ABC.github.io/main/assets/images/example.webp)  
# Replace 'ABC.github.io' with your old domain
```
#### After (New Domain: `CDE.github.io`)
```md
![example](https://raw.githubusercontent.com/CDE/CDE.github.io/main/assets/images/example.webp)  
# Replace 'CDE.github.io' with your new domain
```

## Solution: Python Script to Update Links

The following script scans all `.md` files in the current directory and replaces outdated links.

### Python Script
```python
import os

# Define the replacement rules
replacements = {
    "https://raw.githubusercontent.com/ABC/ABC.github.io/": "https://raw.githubusercontent.com/CDE/CDE.github.io/",
    "https://github.com/ABC/": "https://github.com/CDE/"
}

def update_md_files():
    for filename in os.listdir():  # Scan files in the current directory
        if filename.endswith(".md"):  # Process only .md files
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read()
            
            new_content = content
            for old, new in replacements.items():
                new_content = new_content.replace(old, new)
            
            if new_content != content:  # Update file only if changes are made
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"Updated: {filename}")
            else:
                print(f"No changes needed: {filename}")

if __name__ == "__main__":
    update_md_files()
    print("Processing completed.")
```

## How to Use the Script
1. **Save the script** as `update_links.py` in your Jekyll project folder.
2. **Run the script** in a terminal:
   ```sh
   python update_links.py
   ```
3. **Check your files** to ensure updates were applied.
4. **Commit and push** the changes to GitHub:
   ```sh
   git add .
   git commit -m "Updated links to new domain"
   git push
   ```

## Conclusion
Migrating a Jekyll site to a new GitHub repository name is straightforward, but updating internal links is essential. This Python script helps automate the process, ensuring consistency and avoiding future issues.

🚀 Happy coding!

## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)