# 1. Write a program to print multiplication table of a given number using for loop.
n= int(input("Enter number n to print its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n* i}")
