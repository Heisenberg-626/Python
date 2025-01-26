'''
Author: Sourav V S
Date: 30-11-2024
This program is to print the count of upper and lower characters of a given string.
'''
def count_upper_lower(str):
    upper_char = 0
    lower_char = 0
    for char in str:
        if char.isupper():
            upper_char += 1
        elif char.islower():
            lower_char += 1
    return upper_char,lower_char
str = input("Enter a string: ")
a,b = count_upper_lower(str)
print (a,b)
