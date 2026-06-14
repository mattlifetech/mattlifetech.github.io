---
title: "Batch Image Download (DLZ) - Sort, Rename, and Organize in Folders"
layout: single
excerpt: "Learn how to use the DLZ Chrome extension to batch download images, auto-sort them, and rename files into organized folders."
date: 2025-03-14
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/DLZ.png
categories:
  - How-To
tags: [Chrome, Downloads, Image Management, Automation]
---

![DLZ](https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/main/assets/images/DLZ.png)

# Batch Image Download (DLZ) - Sort, Rename, and Organize in Folders

Downloading multiple images from a webpage can be tedious. The **DLZ Chrome extension** automates this by **identifying images, allowing selection by type, renaming files sequentially, and saving them in organized folders** directly inside your Downloads folder.

## 🔹 Key Features
✅ **Detects all images on a webpage** and counts them by type (JPG, PNG, GIF, etc.)  
✅ **Multi-select filtering by image type** before downloading  
✅ **Automatically renames images** in sequence based on their order on the webpage  
✅ **Saves images into a structured folder** named by user input (or defaults to "Image")  
✅ **Prevents trailing symbols or spaces in folder names**  
✅ **Auto-increments folder names** if a duplicate exists (e.g., "Folder", "Folder (2)")  

## 📥 How It Works

### 1️⃣ **Install & Open DLZ**
Once installed, **pin the extension** to your Chrome toolbar for quick access.

### 2️⃣ **Scan and Preview Images**
Click on the **DLZ icon** to scan the webpage for images. A preview window will show:
- A **grid of thumbnails** for all detected images
- A **multi-select dropdown** to filter images by format (JPG, PNG, etc.)
- A **checkbox for each image** (selected by default)

### 3️⃣ **Choose Folder Name**
Enter a **folder name** (optional). If left blank, the folder will be named "Image".
- If you enter **"story_"**, the folder will be named **"story"**, and files will be named **"story_1001.jpg"**.
- If the folder already exists, it will create **"story (2)"**, **"story (3)"**, etc.

### 4️⃣ **Click "Download"**
DLZ will **download images to your system's Downloads folder** inside the designated folder.

## 📂 Where Are My Files Saved?
Images are saved inside **`Downloads/[FolderName]`**. Example:
```
Downloads/
 ├── story/
 │   ├── story_1001.jpg
 │   ├── story_1002.jpg
 │   ├── story_1003.png
 │   └── ...
```
If the folder already exists, DLZ will create a **new numbered version**:
```
Downloads/
 ├── story/
 ├── story (2)/
 ├── story (3)/
```

## ⚙️ Technical Details
- **Sequential renaming** ensures files are saved in the order they appear on the webpage.
- **Trailing special characters (like "_", "-", "~") in folder names are removed** to keep folder names clean.
- **Chrome does not allow direct folder creation**, so files are prefixed with the folder name inside Downloads.

## 🚀 Why Use DLZ?
Instead of manually saving images **one by one**, use DLZ to automate the process and keep everything **neatly sorted**. Perfect for saving:
- Manga scans & comic pages
- Design assets & stock images
- Research & reference materials

## 🎯 Get Started Today!
1. Download DLZ from the GitHub Release
2. Open Google Chrome.
3. Go to chrome://extensions/.
4. Enable Developer Mode (toggle in the top-right corner).
5. Click "Load unpacked".
6. Select the downloaded DLZ extension folder


**Happy downloading!** 🚀


## GitHub repo
https://github.com/mattlifetech/chromeimagedlz/tree/v1.0

## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)