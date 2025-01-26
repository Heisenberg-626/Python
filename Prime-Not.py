'''
Author: Sourav V S
Date: 22-10-2024
This program is to check whether the given number is prime or not.
'''
number=int(input("Enter the number:"))
isPrime=True
for i in range(2,number//2+1):
    if number % i ==0:
        isPrime= False
        break
if isPrime:
        print(f"The given number {number} is a prime number")
else:
        print(f"The given number {number} is not a prime number")
