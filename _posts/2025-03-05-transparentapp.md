---
title: "Make Image Background Transparent - EXE App"
layout: single
excerpt: "Learn how to create a simple Python app to remove image backgrounds and convert it into an EXE file for easy use."
date: 2025-03-04
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/transparent_app.webp
categories: [Python, Image Processing, EXE]
tags: [Python, Tkinter, Pillow, PyInstaller, Image Editing]
---

![tptapp](https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/main/assets/images/transparent_app.webp)

# Make Image Background Transparent - EXE App

Removing image backgrounds can be useful for various design and editing tasks. In this guide, we'll walk through how to create a simple **Python application** that allows users to select an image, click on the background color to remove it, and save it as a **transparent PNG**. Finally, we'll show how to convert this script into an **EXE application** so it can run on any Windows computer without needing Python installed.

## What the Python Script Does

Our Python script provides a **graphical interface (GUI)** for users to:

1. **Select an image** to process.
2. **Click on the background color** in the image to remove it.
3. **Save the processed image** as a new transparent PNG file.

It uses:
- **Pillow** (PIL) for image processing
- **Tkinter** for the user interface

### Key Features
✅ **Click-based background color selection** (no manual RGB input needed).  
✅ **No external dependencies** required after conversion to EXE.  
✅ **Simple and lightweight** GUI.

## Python Code to Create the App

```python
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        img = Image.open(file_path)
        img.thumbnail((300, 300))  # Resize for preview
        img_tk = ImageTk.PhotoImage(img)
        
        label_image.config(image=img_tk)
        label_image.image = img_tk
        label_image.file_path = file_path  # Store path for processing
        label_image.img = img  # Store original image for pixel selection

def pick_color(event):
    if not hasattr(label_image, "img"):
        return
    
    x, y = event.x, event.y
    img_resized = label_image.img.copy()
    img_resized.thumbnail((300, 300))  # Match displayed image size

    x_ratio = label_image.img.width / img_resized.width
    y_ratio = label_image.img.height / img_resized.height
    orig_x, orig_y = int(x * x_ratio), int(y * y_ratio)

    selected_color = label_image.img.convert("RGB").getpixel((orig_x, orig_y))
    label_color.config(text=f"Selected Color: {selected_color}", fg="black")
    label_color.color = selected_color  # Store selected color

def make_transparent():
    if not hasattr(label_image, "file_path"):
        result_label.config(text="Please select an image first.")
        return

    image = Image.open(label_image.file_path).convert("RGBA")
    datas = image.getdata()

    if hasattr(label_color, "color"):
        r_bg, g_bg, b_bg = label_color.color
    else:
        result_label.config(text="Please select a background color first.")
        return

    new_data = [
        (r, g, b, 0) if (abs(r - r_bg) < 50 and abs(g - g_bg) < 50 and abs(b - b_bg) < 50) else (r, g, b, a)
        for (r, g, b, a) in datas
    ]

    image.putdata(new_data)
    
    save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
    if save_path:
        image.save(save_path)
        result_label.config(text=f"Saved to: {save_path}")

# GUI Setup
root = tk.Tk()
root.title("Transparent PNG Maker")

label_instructions = tk.Label(root, text="""Steps:\n1. Click \"Select Image\" to choose an image.\n2. Click on the background color you wish to remove.\n3. Click \"Make Transparent & Save\" to save the result.""", justify="left", padx=10, pady=5)
label_instructions.pack()

btn_select = tk.Button(root, text="Select Image", command=select_image)
btn_select.pack()

label_image = tk.Label(root)
label_image.pack()
label_image.bind("<Button-1>", pick_color)

label_color = tk.Label(root, text="Click image to select background color")
label_color.pack()

btn_process = tk.Button(root, text="Make Transparent & Save", command=make_transparent)
btn_process.pack()

result_label = tk.Label(root, text="", fg="blue")
result_label.pack()

root.mainloop()
```

## Convert Python Script to EXE
To allow non-Python users to run the app, we can **convert it into an EXE file** using **PyInstaller**.

### Steps:
1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```
2. Convert script to EXE:
   ```sh
   pyinstaller --onefile --windowed transparent_app.py
   ```
3. The `dist/transparent_app.exe` file is now ready for distribution!

### Optional: Add an Icon
To add an app icon:
```sh
pyinstaller --onefile --windowed --icon=app_icon.ico transparent_app.py
```

## Troubleshooting Tips
✅ **If the EXE file is missing dependencies**, try adding:
   ```sh
   pyinstaller --onefile --windowed --hidden-import=PIL --hidden-import=tkinter transparent_app.py
   ```
✅ **EXE file too large?** PyInstaller packs everything—use `UPX` compression.
✅ **Some users report missing DLLs?** Ensure a clean environment before packaging.

## Conclusion
This guide showed how to build a **simple GUI app to remove image backgrounds**, convert it into a **Windows EXE**, and package it for easy distribution. 🚀  

## 📥 Download the App

You can download the **Offline Background Transparent App** as an `.exe` from GitHub:

[➡ Download v1.0.0](https://github.com/mattlifetech/offlinebackgroundtransparent/releases/tag/v1.0.0)


## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)


