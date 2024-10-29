'''
Author: Sourav V S
Date: 22-10-2024
This program is to make a sample multiplication table upto 12.
'''
number=int(input("Enter a number:"))
for i in range(1,13):
    value=number*i
    print(f"{number}*{i}={value}")
    
