#this chapter is about file and input and outputs
'''The random-access memory is volatile, and all its contents are lost once a program 
terminates. In order to persist the data forever, we use files.'''

'''in python open is a built-in function that is used to open a file.'''
#the bilow code opens a file i crewated use.txt in read mode

f=open('use.txt')
data=f.read() #read() reads the entire content of the file
print(data)
f.close()
#.close() is used to close the file after reading it

#

