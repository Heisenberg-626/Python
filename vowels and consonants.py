'''
Author: Sourav V S
Date: 22-10-2024
This program is to find the number of vowels and consonants in a given string.
'''
str=input("Enter a string:")
vowels="aeiouAEIOU"
consonants="bcdfghjklmnpqrstvwxyz"
vowels_count=0
consonants_count=0
for char in str:
    if char in vowels:
        vowels_count+=1
    else:
        consonants_count+=1
print(f"No of vowels in the given string {str} : {vowels_count}")
print(f"No of consonants in the given string{str}: {consonants_count}")
