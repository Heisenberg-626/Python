'''
Author: Sourav V S
Date: 10-11-2024
This program is to print the first five multiples of the given number.
'''
number = int(input("Enter a number: "))
for i in range(1,6):
    value = i * number
    print(value, end=" ")