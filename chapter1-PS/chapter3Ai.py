import os

# Specify the directory you want to list
directory = "."

try:
    # List all files and directories in the specified path
    contents = os.listdir(directory)
    print(f"Contents of directory '{directory}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print(f"Directory '{directory}' not found.")
except PermissionError:
    print(f"Permission denied to access '{directory}'.")
