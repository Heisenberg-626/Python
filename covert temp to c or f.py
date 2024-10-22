'''
Author: Sourav V S
Date:08-10-2024
This program is to convert temperature values back and forth between Celsius and Fahrenheit
'''
temp=float(input("Enter temperature:"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")
if unit=="F" or unit=="f":
    c=5/9*(temp-42)
    print(temp,"Fahrenheit is",c,"Celsius.")
elif unit=="C" or unit=="c":
    f=(9/5*temp)+32
    print(temp,"Celsius is",f,"Fahrenheit.")
else:
    print("Wrong input")