#this is about type functions and typecasting in python 

a = 31 
type(a) # class <int> 
b = "krishna" 
type (b) # class <str> 
c= 3.14
type(c) # class <float>
d= a
type(d) # class <int>
print(type(a))  # prints the type of a
print(type(b))  # prints the type of b
print(type(c))  # prints the type of c
print(type(d))  # prints the type of d

# There are many functions to convert one data type into another. 
print(str(31))    # "31"   # integer to string conversion 
print(int("32"))  # 32    # string to integer conversion 
print(float(32))  # 32.0  # integer to float conversion 