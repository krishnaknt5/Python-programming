# Write a program to store seven fruits in a list entered by the user. 
fruits = []  # Start with an empty list
f1= input("Enter fruit name: ")
fruits.append(f1)  # Add the first fruit to 
f2= input("Enter fruit name: ")
fruits.append(f2)
f3= input("Enter fruit name: ")
fruits.append(f3)
f4= input("Enter fruit name: ")
fruits.append(f4)
f5= input("Enter fruit name: ")
fruits.append(f5)
f6= input("Enter fruit name: ")
fruits.append(f6)
f7= input("Enter fruit name: ")
fruits.append(f7)
print(fruits)  

#in palce of the above program we can use billow method to store seven fruits in a list entered by the user.



fruits = []  # Start with an empty list
for i in range(1, 8):  # Loop from 1 to 7
    fruit = input(f"Enter name of fruit #{i}: ")
    fruits.append(fruit)  # Add each input to the list
print(fruits)
