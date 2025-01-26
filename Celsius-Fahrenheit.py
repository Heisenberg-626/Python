'''
Author: Sourav V S
Date:22-10-2024
This program is to convert temperature values back and forth between Celsius and Fahrenheit
'''
temperature=float(input("Enter temperature:"))
unit=input("Is this in (C)elsius or (F)ahrenheit?")
if unit=="F" or unit=="f":
    c=5/9*(temperature)
    print(temperature,"Fahrenheit is",c,"Celsius.")
elif unit=="C" or unit=="c":
    f=(9/5*temperature)+32
    print(temperature,"Celsius is",f,"Fahrenheit.")
else:
    print("Wrong input")
