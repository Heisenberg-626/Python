'''
Author: Sourav V S
Date:08-10-2024
This program is to determine the entry-ticket fare in a zoo based on age
'''
age=int(input("Enter the age:"))
if age<10:
    print("Fare is:",7)
elif age>=10 and age<60:
    print("Fare is:",10)
else:
    print("Fare is:",5)
