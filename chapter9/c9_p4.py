'''4. A file contains a word “Donkey” multiple times. You need to write a program 
which replace this word with ##### by updating the same file.  '''
# This code replaces occurrences of the word "Donkey" with "#####" in a file named 'donkey.txt'.
word = "Donkey"
with open('p4.txt', 'r') as f:
    content = f.read()
    contentNew = content.replace(word, "#####")
with open('p4.txt', 'w') as f:
    f.write(contentNew)
