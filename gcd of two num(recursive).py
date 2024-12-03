'''
Author: Sourav V S
Date: 03-12-2024
This program defines a function to find the gcd of two numbers using recursion.
'''
def gcd(n1,n2):
    if n1%n2 ==0:
        return n2
    else:
        return gcd(n2,n1%n2)
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print("GCD of the given two numbers: ",gcd(num_1,num_2))