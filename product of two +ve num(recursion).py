'''
Author: Sourav V S
Date: 03-12-2024
This program defines a function to find the product of two numbers using recursion.
'''
def multi_num(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multi_num(n1,n2-1)
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print("Product of the two numbers: ",multi_num(num_1,num_2))
