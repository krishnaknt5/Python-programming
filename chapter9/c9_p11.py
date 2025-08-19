# 11. Write a python program to rename a file to “renamed_by_ python.txt.
# This code renames a file named 'p11.txt' to 'renamed_by_python.txt'.
with open('p11.txt') as f:
    content = f.read()
with open('renamed_by_python.txt', 'w') as f:
    f.write(content)
    # this program will rename the file p11.txt to renamed_by_python.txt which will be a new file