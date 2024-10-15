'''
Author: Sourav V S
Date:08-10-2024
This program is to determine the sum of digits of a number
'''
num=int(input("Enter the number:"))
sum=0
while num>0:
    r=num%10
    num=num//10
    sum=sum+r
    print("Sum:",sum)