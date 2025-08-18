def greet(name, ending="Thank you"):
    print(f"Good morning, {name}") #this line did string concatenation
    print(ending)
greet("Krishna") #in this case, it will use the default ending "Thank you" as default argument
greet("Krishna", "Thanks") #this will override the default ending it will print "Thanks" instead of "Thank you" 
# We can have a value as default as default argument in a function. 