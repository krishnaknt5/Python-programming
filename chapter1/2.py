#this is problem given by code with harry
# Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that. 
# on page number 10 in the handbook
#in the line 20 i just give the path of the directory which i want to see i can give any path which are exist in my system

import os
def list_directory_contents(path='.'):
    """Print names of all entries in the specified directory."""
    try:
        entries = os.listdir(path)  # ← this function lists everything in the directory
        print(f"Contents of {os.path.abspath(path)}:")
        for entry in entries:
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                print(f"[DIR]  {entry}")
            else:
                print(f"       {entry}")
    except FileNotFoundError:
        print(f"Error: Directory '{path}' not found.")
    except NotADirectoryError:
        print(f"Error: '{path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied accessing '{path}'.")
list_directory_contents('C:/Users/BijayKrishna/OneDrive/Desktop/python')
