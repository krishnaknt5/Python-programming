# 1. Write a python program to add two numbers.
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
num1 = float(num1)
num2 = float(num2)
total = num1 + num2
print(total)

# 2. Write a python program to find remainder when a number is divided by z. 
a=42
b=10
remainder = a % b
print(remainder)

# 3. Check the type of variable assigned using input () function. 
a=input("Enter a number: ")
print(type(a))  

# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80 
a=int(input("enter value of a: "))
b=int(input("enter value of b: "))
print(a > b)  # at a=34 and b=80, this will print False


# 5. Write a python program to find an average of two numbers entered by the user.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("The average of 2 number is",(a+b)/2)

# 6. Write a python program to calculate the square of a number entered by the user.
a = int(input("Enter a number(n): "))
print("the aqure of n is", a*a) #in place of a*a if there are given number is a yto the power any number we can use a**2
