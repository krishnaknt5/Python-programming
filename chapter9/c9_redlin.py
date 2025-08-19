'''this is about readlining a file which is a file that has been created in the previous chapter use to read the lnes of a file'''
f=open('use.txt')
# lines=f.readlines() 
# print(lines,type(lines)) 

'''readline() reads one line at a time from the file'''
'''i can use above code to read all lines at once and then iterate through them, but here i will read one line at a time'''

# line1=f.readline() 
# print(line1,type(line1)) 
# line2=f.readline() 
# print(line2,type(line2)) 
# line3=f.readline() 
# print(line3,type(line3))

# line7=f.readline() 
# print(line7 ==" ") 

'''i can also use a while to readlines through the lines of the file'''


line=f.readline()
while (line !=''):
    print(line)  
    line=f.readline()  #read the next line
# this will read the file line by line until the end of the file is reached

f.close() 


'''in this code i have read the file line in 3 different ways by line and printed each line'''