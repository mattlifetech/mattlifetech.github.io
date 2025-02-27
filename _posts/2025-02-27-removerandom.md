---
title: "Batch Removing Random Characters in Story Text Files"
layout: single
excerpt: "A guide to cleaning up story text files by removing unwanted random characters using a Python script."
date: 2025-02-21
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/text-cleaning.webp
categories: [Text Processing, Python]
tags: [Python, Text Cleaning, Automation, Regex]
---

## Removing Random Characters in Story Text Files

When processing large text files, especially those converted from different formats, unwanted random characters can appear. These can include symbols, numbers, and inconsistent letter sequences. 

### Problem Analysis

The Python script below is designed to clean text files by removing unwanted random character sequences. It scans all `.txt` files within a specified folder, applies a regex-based cleaning function, and saves the modified text back to the file.

### Example of Unwanted Text

The script will remove text patterns like:

```
h2 ?# _% j2 k. C( Y, v
```

These random sequences do not contribute to meaningful content and can disrupt readability.

### Python Script for Cleaning Text

```python
import os
import re

def clean_text(text):
    # Define a regex pattern to remove sequences matching 'SPACE-XX' where XX is not both A-Z
    pattern = r'\s+[A-Za-z!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~0-9][^A-Za-z](?:\s+[A-Za-z!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~0-9][^A-Za-z])+'
    
    # Remove matching sequences from the text
    cleaned_text = re.sub(pattern, '', text)
    
    return cleaned_text

def process_files(folder):
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                    
                    cleaned_text = clean_text(text)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(cleaned_text)
                    print(f"Processed: {file_path}")
                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    folder_path = os.path.dirname(os.path.abspath(__file__))
    process_files(folder_path)
    print("Processing complete!")
```

### How It Works
1. The `clean_text()` function uses a regex pattern to find and remove unwanted sequences.
2. The `process_files()` function scans all `.txt` files in the folder and applies the cleaning function.
3. The script processes each file and overwrites it with cleaned text.
4. Simply place the script in the respective folder and run it—no need to edit anything, as it will automatically detect the folder path.

This script ensures your story text files remain free from clutter and enhances readability.
