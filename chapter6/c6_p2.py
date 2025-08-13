# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each marks to pass.  
# Assume 3 markss and take marks as an input from the user.
m1 = int(input("Enter marks for marks 1: "))
m2 = int(input("Enter marks for marks 2: "))
m3 = int(input("Enter marks for marks 3: "))
tot = m1 + m2 + m3
avg = tot / 3
if avg >= 40 and m1 >= 33 and m2 >= 33 and m3 >= 33:
    print("The student has passed.")
else:
    print("The student has failed.")