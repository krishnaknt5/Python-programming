# Write a program to accept marks of 6 students and display them in a sorted manner. 
marks = []  
f1= int(input("Enter marks 1 here: "))
marks.append(f1)   
f2= int(input("Enter marks 2 here: "))
marks.append(f2)
f3= int(input("Enter marks 3 here: "))
marks.append(f3)
f4= int(input("Enter marks 4 here: "))
marks.append(f4)
f5= int(input("Enter marks 5 here: "))
marks.append(f5)
f6= int(input("Enter marks 6 here: "))
marks.append(f6)
marks.sort()  
print(marks) 


#or we can use the following method to accept marks of 6 students and display them in a sorted manner.

marks = []  # Start with an empty list
for i in range(1, 7):  # Loop from 1 to 6
    mark = int(input(f"Enter marks for student #{i}: "))
    marks.append(mark)  # Add each input to the list
    marks.sort()  # Sort the list of marks    
print(marks)  # Display the sorted list of marks