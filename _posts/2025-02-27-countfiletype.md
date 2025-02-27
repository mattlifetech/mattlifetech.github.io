---
title: "Counting Files by Type in Folders and Subfolders"
layout: single
excerpt: "A Python script to analyze and count files by type in a directory and its subdirectories, exporting results to an Excel report."
date: 2025-02-27
header:
  overlay_image: /assets/images/filler.webp
  teaser: /assets/images/file-counting.webp
categories: [File Management, Python]
tags: [Python, File Analysis, Automation, Data Processing]
---

![counttype](https://raw.githubusercontent.com/mattchoo2/mattchoo2.github.io/main/assets/images/file-counting.webp)


## Counting Files by Type in Folders and Subfolders

When managing large collections of files, it can be helpful to analyze and count the different file types within a directory, including its subfolders. This Python script automates the process and exports the results to an Excel file.

### How the Script Works

The script performs the following tasks:
1. Recursively scans all files inside a specified root folder.
2. Counts the number of files by type (file extension).
3. Categorizes counts both globally and per subfolder.
4. Exports the results to an Excel file with two sheets: 
   - **Total Counts**: Summarizes the count of each file type.
   - **Folder Counts**: Provides file type counts per folder.

### Python Script for File Type Counting

```python
import os
import pandas as pd
from collections import defaultdict

def count_files_by_type(root_folder):
    total_counts = defaultdict(int)
    folder_counts = defaultdict(lambda: defaultdict(int))
    
    for folder_path, _, files in os.walk(root_folder):
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext:
                total_counts[file_ext] += 1
                folder_counts[folder_path][file_ext] += 1
    
    return total_counts, folder_counts

def export_to_excel(root_folder, total_counts, folder_counts, output_file):
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    
    # Total counts sheet
    total_df = pd.DataFrame(list(total_counts.items()), columns=['File Type', 'Total Count'])
    total_df.to_excel(writer, sheet_name='Total Counts', index=False)
    
    # Folder-wise counts sheet
    folder_data = []
    for folder, counts in folder_counts.items():
        for file_type, count in counts.items():
            folder_data.append([folder, file_type, count])
    
    folder_df = pd.DataFrame(folder_data, columns=['Folder Path', 'File Type', 'Count'])
    folder_df.to_excel(writer, sheet_name='Folder Counts', index=False)
    
    writer.close()

def main():
    root_folder = os.path.dirname(os.path.abspath(__file__))  # Auto-detect script location
    output_file = os.path.join(root_folder, 'file_type_report.xlsx')
    
    total_counts, folder_counts = count_files_by_type(root_folder)
    export_to_excel(root_folder, total_counts, folder_counts, output_file)
    print(f'Report saved to {output_file}')

if __name__ == '__main__':
    main()
```

### Sample Output
After running the script, an Excel file (`file_type_report.xlsx`) is generated, containing two sheets:

#### **Total Counts Sheet**
```
| File Type | Total Count |
|-----------|------------|
| .txt      | 150        |
| .pdf      | 35         |
| .jpg      | 20         |
```

#### **Folder Counts Sheet**
```
| Folder Path             | File Type | Count |
|-------------------------|----------|-------|
| /home/user/docs        | .txt     | 50    |
| /home/user/images      | .jpg     | 20    |
| /home/user/downloads   | .pdf     | 35    |
```

### Enhancements
- The script now automatically detects the root folder based on where it is placed.
- Uses `os.walk()` to recursively count files within subdirectories.
- Saves results in an Excel file with structured sheets.

This script is a powerful tool for quickly analyzing file distributions in large directories, making file management easier and more efficient.
