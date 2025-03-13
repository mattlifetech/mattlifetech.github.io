import os

# Define the replacement rules
replacements = {
    "https://raw.githubusercontent.com/mattchoo2/mattchoo2.github.io/": "https://raw.githubusercontent.com/mattlifetech/mattlifetech.github.io/",
    "https://github.com/mattchoo2/": "https://github.com/mattlifetech/"
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
