import os

def print_folder_structure(root_folder, indent=""):
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        print(indent + "|-- " + item)
        if os.path.isdir(item_path):
            print_folder_structure(item_path, indent + "    ")

# Run for your GitHub Page folder
folder_path = r"C:\Users\b_cer\Documents\GitWebpage\mattchoo.github.io"
print_folder_structure(folder_path)
