---
title: "Scan and Delete Empty Folders Automatically"
layout: single
excerpt: "A Python script to scan directories and remove empty folders dynamically."
date: 2025-02-27
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/folder-cleaning-thumb.webp
categories: [Automation, Python]
tags: [Python, File Management, Automation]
---

![delempty](https://raw.githubusercontent.com/mattchoo2/mattchoo2.github.io/main/assets/images/folder-cleaning-thumb.webp)


## Scan and Delete Empty Folders Automatically

When managing large directories, empty folders often accumulate due to file deletions or restructuring. Instead of manually checking and removing them, we can automate the process with a simple Python script.

### Problem Analysis

This script scans a given directory and removes any empty folders. Originally, it was hardcoded to a specific path (`V:\\Book\\txt`), but we have modified it to work dynamically with the root folder where the script is placed.

### Python Script to Remove Empty Folders

```python
import os

def delete_empty_folders(folder):
    for root, dirs, files in os.walk(folder, topdown=False):  # Traverse from bottom to top
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            if not os.listdir(dir_path):  # Check if the directory is empty
                os.rmdir(dir_path)
                print(f"Deleted empty folder: {dir_path}")

if __name__ == "__main__":
    target_folder = os.path.dirname(os.path.abspath(__file__))  # Automatically set the folder
    delete_empty_folders(target_folder)
```

### How It Works
1. The script recursively scans the directory from bottom to top using `os.walk()`.
2. It checks if any folder is empty and deletes it.
3. Instead of a fixed folder path, it now detects the directory where the script is placed and runs automatically.

### Usage
1. Save the script as `delempfol.py`.
2. Place it in the folder you want to clean.
3. Run the script, and all empty folders inside will be removed.

This small yet powerful script ensures your directories remain clutter-free without manual intervention!
