# Open the file in read mode using 'with', which automatically closes the file 
f=open('use.txt')
print(f.read())
with open('use.txt', 'r') as f:
    print(f.read())


# Open the file in write mode using 'with', which automatically closes the file no need to close explicitly