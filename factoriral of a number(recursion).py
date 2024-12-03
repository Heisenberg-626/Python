'''
Author: Sourav V S
Date: 03-12-2024
This program defines a function to find the factorial of a number using recursion.
'''
def factorial (n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
num = int(input("Enter the number: "))
print("Factorial of the given number: ",factorial(num))