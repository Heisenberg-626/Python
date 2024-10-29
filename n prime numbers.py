'''
Author: Sourav V S
Date: 22-10-2024
This program is to print prime numbers upto n.
'''
limit=int(input("Enter the limit:"))
for i in range(2,limit+1):
    isPrime=True
    for j in range(2,i//2+1):
        if i%j == 0:
            isPrime= False
            break
    if isPrime:
        print(i,end=" ")