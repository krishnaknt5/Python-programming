# 5. Repeat program 4 for a list of such words to be censored. 
words =[ "Donkey" , "Bad", "Ugly"]
with open('p5.txt', 'r') as f:
    content = f.read()
for word in words:
    content = content.replace(word, "$"*len(word))
with open('p5.txt', 'w') as f:
    f.write(content)