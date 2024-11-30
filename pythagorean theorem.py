'''
Author: Sourav V S
Date: 30-11-2024
This program accepts the lengths of three sides of a triangle as inputs. The program should output whether or not the triangle is a right triangle.
'''
def right_triangle_or_not ():
   sides = [side1,side2,side3]
   sides.sort()
   if sides[2]**2 == sides[0]**2 + sides[1]**2:
       return True
   return False
side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))
if right_triangle_or_not ():
    print("The given sides are of a right triangle")
else:
    print("The given sides are not of a right triangle")