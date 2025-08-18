def greet(name, message):
    print("Good morning, "+name) #this line did string concatenation
    print(message)
greet("Krishna", "Thank you")
greet("Raju", "Thanks")
#we can use arguments in functions to pass values to them.
#we used message as an argument to the function greet, which allows us to customize the greeting message for each user.
#output:
'''
Good morning, Krishna
Thank you
Good morning, Raju
Thanks'''
#another function with return value
#it will print value of a is 9 if we will not use return statement it will give none as value of a . 
def greet(name, message):
    print("Good morning, "+name) #this line did string concatenation
    print(message)
    return 9
a=greet("Krishna", "Thank you")
print(a)