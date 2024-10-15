'''
Author: Sourav V S
Date:08-10-2024
This program is to print n odd numbers
'''
limit=int(input("Enter the limit:"))
odd_num=1
count=0
while count<limit:
    print(odd_num,"",end="")
    count+=1
    odd_num+=2
