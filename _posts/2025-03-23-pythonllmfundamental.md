---
title: "Totally Fundamental Knowledge for Newbies to Start Playing with Python and LLMs"
layout: single
excerpt: "A beginner-friendly guide to understanding terminal access, coding installation, virtual environments, and package management for Python and LLMs."
date: 2025-03-23
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/funda.webp
categories: [Tech, Coding, Python, LLM]
tags: [Python, LLM, Terminal, Virtual Environment, AI, Beginners]
---

![python_basics](https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/main/assets/images/funda.webp)

## 1. Accessing the Terminal

### What is a Terminal?
A terminal is a command-line interface (CLI) that allows users to interact with their computer using text commands. There are different types of terminals, including:

- **Command Prompt (cmd)** - Default CLI for Windows.
- **PowerShell** - More powerful than cmd, supports scripting.
- **Git Bash** - A Unix-like environment for Windows, often used with Git.
- **Terminal (Mac/Linux)** - The default CLI for macOS and Linux systems.

### Where to Locate the Terminal on PC?
- **Windows:** Press `Win + R`, type `cmd` or `powershell`, and hit Enter.
- **Mac:** Press `Cmd + Space`, type `Terminal`, and hit Enter.
- **Linux:** Use the shortcut `Ctrl + Alt + T` or search for "Terminal."

### Differences Between Them?
- **Cmd** is basic and doesn't support advanced scripting.
- **PowerShell** supports scripting and automation.
- **Git Bash** offers Linux-like commands.
- **Mac/Linux Terminal** natively supports UNIX commands.

---

## 2. Installing Python and Running It in Different Terminals

### Why is Python Popular for Beginners?
- **Easy to Learn:** Python has a simple syntax that is easy to read and write.
- **Vast Community Support:** Large community and extensive documentation.
- **Versatility:** Used in web development, data science, AI, and automation.
- **Built-in Libraries:** Comes with many built-in functions and modules.

### How to Install Python?
1. Download Python from [python.org](https://www.python.org/downloads/).
2. Install it and ensure the "Add Python to PATH" option is checked.

### Where is Python Installed?
- Windows: Typically in `C:\Users\YourUsername\AppData\Local\Programs\Python`
- Mac/Linux: `/usr/local/bin/python3`

### How to Run Python in Different Terminals?
- **Cmd:** `python` or `python3`
- **PowerShell:** `python`
- **Git Bash:** `python3`
- **Mac/Linux Terminal:** `python3`

---

## 3. Installing Packages Using Pip

### What is Pip?
Pip is Python’s package manager that allows installing external libraries.

### How to Install a Package?
Run the following command in any terminal:
```bash
pip install package_name
```

### Where Are Packages Installed?
- **Global Installation:** `C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX\Lib\site-packages`
- **Virtual Environment Installation:** Inside the `venv/Lib/site-packages` directory.
  - If starting from `C:\`, it would be in `C:\path\to\your\project\venv\Lib\site-packages`
- **Conda Virtual Environment Installation:** Typically under `C:\Users\YourUsername\anaconda3\envs\your_env\Lib\site-packages`

### How to Know If a Package is Installed Globally or in a Virtual Environment?
- **Global Installation Check:** Run `pip show package_name` and check the `Location` field.
- **Virtual Environment Check:** If inside an activated virtual environment, the package will be installed in the `venv` directory.
- **Conda Installation Check:** Run `conda list package_name` to verify package location.
- **Local Folder Installation Check (Non-Virtual Environment):** If a package is installed in the folder where the terminal is opened, check if a `Lib` or `site-packages` folder exists within that directory.

### How to Check Installed Packages?
```bash
pip list
```

---

## 4. Virtual Environments

### What is a Virtual Environment?
A virtual environment isolates dependencies for different projects to prevent conflicts.

### Why Use It?
- Some apps require older Python versions.
- Avoid conflicts between different package versions.

### How to Create and Activate a Virtual Environment?
```bash
python -m venv myenv
```
- **Windows (cmd/PowerShell):** `myenv\Scripts\activate`
- **Mac/Linux:** `source myenv/bin/activate`

To deactivate, use:
```bash
deactivate
```

### Conda Virtual Environment
Conda is another virtual environment and package management tool, mainly used in data science.

#### How to Create and Activate a Conda Virtual Environment?
```bash
conda create --name myenv python=3.9
conda activate myenv
```
- Unlike `venv`, Conda manages its own environments separately from system Python.
- Some applications require Conda because they depend on libraries that need special dependency management, such as TensorFlow or PyTorch.
- To deactivate, use:
```bash
conda deactivate
```
- **Why Some Apps Require Conda Virtual Environment?**
  - Some applications use packages that require system-level dependencies managed better by Conda than Pip.
  - Conda environments can include non-Python dependencies (like CUDA for machine learning applications).

---

## 5. Potential File Duplication Issue

Many applications require separate storage for LLM models, leading to redundant files:
- **KoboldAI, Text Generation WebUI, Oobabooga, etc.** each store models in separate folders.
- If using multiple tools, check storage usage to avoid excessive duplication.

---

## 6. Using AI (ChatGPT) for Debugging Terminal Errors

### Common Issue:
Some commands are terminal-specific. Example:
- `ls` (Mac/Linux) vs. `dir` (Windows cmd)

### How to Ask AI for Help?
- Copy the error message and search for it.
- Use ChatGPT: “I ran this command in PowerShell, but it doesn’t work in cmd. How should I modify it?”

---

## 7. Environment Variables

### What Are Environment Variables?
Environment variables store system-wide settings that applications and scripts can access.

### Why Are They Needed?
- Helps define system-wide configurations.
- Ensures scripts can locate required executables and dependencies.

### How to Set Up Environment Variables?
- **Windows:**
  1. Search `Environment Variables` in the Start menu.
  2. Under `System Variables`, add or edit `PATH`.
- **Mac/Linux:**
  - Add variables in `~/.bashrc` or `~/.zshrc`:
  ```bash
  export PATH="$HOME/.local/bin:$PATH"
  ```
  - Apply changes with:
  ```bash
  source ~/.bashrc
  ```

### Common Variables to Set Up
- **Python PATH** (`C:\Users\YourUsername\AppData\Local\Programs\Python\PythonXX`)
- **Conda PATH** (`C:\Users\YourUsername\anaconda3\Scripts`)

---

## 8. Right-Click Run of Python Script

You can follow this post to add this function to your right click menu context
https://mattlifetech.github.io/projects/rightclick-run-python/



---

### Final Thoughts
Mastering these basics will help you get started with Python, LLMs, and automation. Experiment, break things, and keep learning!


## Support Me 💖
[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/mattchoo2)

