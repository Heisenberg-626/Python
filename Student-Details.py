'''
Author: Sourav V S
Date: 01-10-2024
This program allows the user to input the student details
'''

name=input("Enter the Name of the Student:")
roll_no=int(input("Enter the Roll No:"))
cgpa=float(input("Enter cgpa:"))
percentage=cgpa*10
print("Name of the Student:",name)
print("Roll No:",roll_no)
print("cgp of student:",cgpa)
print("Percentage:",percentage,"%")
