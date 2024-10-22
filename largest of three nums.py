'''
Author: Sourav V S
Date:22-10-2024
This program is to find the largest of three numbers
'''
firstnum=int(input("Enter first number:"))
secondnum=int(input("Enter second number:"))
thirdnum=int(input("Enter third number:"))
if firstnum>secondnum and firstnum>thirdnum:
    print("The largest number is:",firstnum)
elif secondnum>firstnum and secondnum>thirdnum:
    print("The largest number is:",secondnum)
elif thirdnum>firstnum and thirdnum>secondnum:
    print("The largest number is:",thirdnum)
else:
    print("The numbers are equal!")
