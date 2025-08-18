#This program is abpit recursion in Python.

#in this program we will find the factorial of a number using recursion.


'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 X 1
factorial(3) = 3 X 2 X 1
factorial(4) = 4 X 3 X 2 X 1
factorial(5) = 5 X 4 X 3 X 2 X 1
factorial(n) = n X n-1 X......3 X 2 X 1

factorial(n) = n * factorial(n-1)
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1) 
n=int(input("Enter a number: "))
print(f"The factorial of {n} is {factorial(n)}")

'''The programmer needs to be extremely careful while working with recursion to ensure 
that the function doesn't infinitely keep calling itself. Recursion is sometimes the most 
direct way to code an algorithm. However, it can be less efficient than an iterative solution,'''
'''especially for large inputs, due to the overhead of multiple function calls and the risk of hitting the recursion limit.'''
'''end of c8_recursion.py'''