'''
Author: Sourav V s
Date: 08-10-2024
This program is used to perform various tasks on strings
'''
first_name=input("Enter first name:")
last_name=input("Enter last name:")
full_name=first_name+" "+last_name
print(full_name)
length=len(first_name)
extracted_first_name=full_name[length+1:]
print(extracted_first_name)