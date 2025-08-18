# 3. How do you prevent a python print() function to print a new line at the end.
print("a")
print("b")
print("c", end="")
print("d", end=""), 
#this will print "abcd" without a new line at the end.
#it use to ignore the default behavior of print function to add a new line at the end.