'''
Author: Sourav V S
Date:08-10-2024
This program is to determine the smallest of three numbers
'''
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1<num2 and num1<num3:
    print("The smallest number is:",num1)
elif num2<num1 and num2<num3:
    print("The smallest number is:", num2)
elif num3<num1 and num3<num2:
    print("The smallest number is:", num3)
else:
    print("The given numbers are equal")

