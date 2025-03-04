---
title: "RightClickRunPython – Run Python Scripts with a Right-Click"
layout: single
excerpt: "quick way to instant click and run python scripts"
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/rightpython.webp
date: 2025-02-19
tags:
  - Python
  - Windows
  - Automation
  - Productivity
categories:
  - Projects
  - Tools
description: "A simple way to run Python scripts from the Windows context menu with a right-click."
permalink: /projects/rightclick-run-python/
---

# GUI right click run python in Window 11
For those who not used to type in command prompt or power shell, this enable you to right click and run python script straight. 
<br><br>It will:
- open power shell on the respective folder and
- run the script in this folder

To add a right-click context menu option in Windows 11 that opens PowerShell and runs a selected Python script, follow these steps:

### Step 1: Create a PowerShell Script

First, create a PowerShell script that will handle running the Python script. Save this script in a known location, for example, `C:\Scripts\RunPythonScript.ps1`.

```powershell
# RunPythonScript.ps1
param (
    [string]$FilePath
)

if (-Not (Test-Path $FilePath)) {
    Write-Host "File does not exist: $FilePath"
    exit
}

# Get the directory of the selected file
$dir = Split-Path -Parent $FilePath

# Change to the directory
Set-Location -Path $dir

# Run the Python script
python $FilePath
```


### Step 2: Modify the Windows Registry

Next, you need to modify the Windows Registry to add a new context menu entry.

1.  **Open the Registry Editor:**
    
    -   Press `Win + R`, type `regedit`, and press `Enter`.
        
2.  **Navigate to the Context Menu Key:**
    
    -   Go to the following path:
        
        ```
        
        HKEY\_CLASSES\_ROOT\\\*\\shell
        ```
        
3.  **Create a New Key for the Context Menu:**
    
    -   Right-click on `shell`, select `New > Key`, and name it something like `RunPythonScript`.
        
4.  **Set the Menu Label:**
    
    -   In the `RunPythonScript` key, double-click on the `(Default)` value and set it to `Run Python Script`.
        
5.  **Create a Command Key:**
    
    -   Right-click on the `RunPythonScript` key, select `New > Key`, and name it `command`.
        
6.  **Set the Command to Run the PowerShell Script:**
    
    -   In the `command` key, double-click on the `(Default)` value and set it to:
        
        ```
        
        powershell.exe -ExecutionPolicy Bypass -File "C:\\Scripts\\RunPythonScript.ps1" "%1"
        ```
        

### Step 3: Test the Context Menu

1.  Right-click on any `.py` file in File Explorer.
    
2.  You should see a new option called `Run Python Script`.
    
3.  Clicking it will open PowerShell, navigate to the directory of the script, and run the selected Python script.
    

### Notes:

-   **Execution Policy:** The `-ExecutionPolicy Bypass` flag is used to allow the script to run without changing the system's execution policy permanently. If you trust the script, you can change the execution policy globally.
    
-   **Python Path:** Ensure that Python is added to your system's PATH environment variable so that the `python` command works in PowerShell.
    

This setup will allow you to run any Python script directly from the context menu in Windows 11.

### REGEDIT via below not working:
```
HKEY_CLASSES_ROOT\Python.File\shell
```


---

Give it a try and let me know your feedback! 🚀


## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)
