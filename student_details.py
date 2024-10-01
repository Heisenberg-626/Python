'''
Python program to get the student details
Author: Sourav V S
Date: 01-10-2024
Version: 1.0
'''

name=input("Enter the Name of the Student:")
roll_no=int(input("Enter the Roll No:"))
cgpa=float(input("Enter cgpa:"))
percentage=cgpa*10
print("Name of the Student:",name)
print("Roll No:",roll_no)
print("cgp of student:",cgpa)
print("Percentage:",percentage,"%")