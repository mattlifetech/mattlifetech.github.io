---
title: "Getting Started with Python for Absolute Beginners Using PowerShell"
layout: single
excerpt: "A step-by-step guide for those with zero coding knowledge to set up Python and run scripts using PowerShell."
date: 2025-02-20
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/python-beginner-powershell.webp
categories: [Python, Beginner]
tags: [Python, PowerShell, Setup, Virtual Environment, Git]
---

## Introduction

If you're new to coding and want to try Python, this guide will help you set up everything step by step. We'll use **PowerShell** as the main command console for running Python scripts. This guide is designed for **absolute beginners**, so no prior knowledge is needed!

## Step 1: Install PowerShell (If Not Already Installed)

PowerShell comes pre-installed on **Windows 10 and later**, but if you need the latest version, follow these steps:

1. Download PowerShell from the official Microsoft page: [PowerShell Releases](https://github.com/PowerShell/PowerShell/releases)
2. Choose the **MSI package** for Windows and install it.
3. After installation, open PowerShell by searching for **"PowerShell"** in the Windows Start menu.
4. To check if PowerShell is working, type:
   ```powershell
   $PSVersionTable.PSVersion
   ```
   This should display the PowerShell version installed on your system.

## Step 2: Install Python

To install Python, follow these steps:

1. Download Python from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Choose the **latest stable version** for Windows.
3. During installation, check the box **"Add Python to PATH"** (important!).
4. After installation, verify Python by running:
   ```powershell
   python --version
   ```
   or
   ```powershell
   py --version
   ```
   This should display the installed Python version.

### Additional Recommended Tools

- **pip**: Installed with Python (used for installing additional packages).
- **virtualenv**: Helps manage Python environments.
  ```powershell
  pip install virtualenv
  ```
- **Git** (optional but useful): Download from [Git for Windows](https://git-scm.com/)

## Step 3: Understanding Python Installation Types

Python installations can be system-wide or folder-specific. Here’s a breakdown:

| Type            | Description |
|----------------|-------------|
| **System-wide installation** | Python is installed for all users. Any script can use it. |
| **Virtual environment (folder-based)** | A self-contained Python setup inside a specific folder. Useful for project-specific dependencies. |

To create a **folder-specific virtual environment**:
```powershell
python -m venv my_project_env
```
To activate it:
```powershell
my_project_env\Scripts\Activate
```
To deactivate it:
```powershell
deactivate
```

## Step 4: Running Python Scripts in PowerShell

- **Running a script in the current folder:**
  ```powershell
  python script.py
  ```
  This runs `script.py` inside the current folder.

- **Running a script inside a virtual environment:**
  ```powershell
  my_project_env\Scripts\Activate
  python script.py
  deactivate
  ```

- **Running a script from another folder:**
  ```powershell
  python C:\path\to\script.py
  ```

## Comparison of Python, PowerShell, Git & Virtual Environment

| Tool               | Use Case | Why Use It? |
|--------------------|----------------------------------------------------------|--------------------------------|
| **Python**        | General-purpose programming language for scripting, automation, web development, and more. | Essential for coding, data analysis, and automation. |
| **PowerShell**    | Command-line shell and scripting language for system automation on Windows. | Helps automate system tasks and manage configurations. |
| **Git**           | Version control system used for tracking code changes and collaboration. | Prevents code loss, supports teamwork, and tracks modifications. |
| **Virtual Environment** | Isolated Python environment for managing dependencies per project. | Avoids conflicts between projects with different dependencies. |

## Conclusion

You now have Python set up and ready to use with PowerShell! Try writing your first Python script and running it with `python script.py`. Happy coding!
