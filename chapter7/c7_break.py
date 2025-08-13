# break and continue statements in loops
#break statement example
#it exits the loop when a certain condition is met
for i in range (0,80): 
        
# Exit the loop if i is 31, 32, or 33
    if i==15: 
        break 
    print(i) 


#continue statement example
#it skips the current iteration and continues with the next one
for i in range (0,80): 
        
# Exit the loop if i is 31, 32, or 33
    if i==15: 
        continue 
    print(i) 


#pass statement example
#it does nothing and is used as a placeholder
l= [1,7,8] 
for item in l: 
    pass  