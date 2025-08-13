# 4. Write a program to find whether a given USN contains less than 10 characters or not. 
USN = input("Enter your USN: ")
if len(USN) < 10:
    print("USN is valid, it contains less than 10 characters.")
else:
    print("USN is invalid, it contains 10 or more characters.")
