'''
Author: Sourav V S
Date: 19-11-2024
This program is to construct patterns of stars (*), using a nested for loop.
'''
rows = int(input("Enter the limit: "))
print("\nIncreasing Triangle")
for i in range(rows + 1):
    for j in range(i):
        print("*",end=" ")
    print()

print("\nDecreasing Triangle")
for i in range(rows,0,-1):
    for j in range (i):
        print("*", end=" ")
    print()

print("\nHill Pattern")
for i in range(1,rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

print("\nReverse Hill Pattern")
for i in range(rows,0,-1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(2 * i - 1):
        print("*", end=" ")
    print()

