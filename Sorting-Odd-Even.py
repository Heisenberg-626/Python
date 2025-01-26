'''
Author: Sourav V S
Date: 05-12-2024
This program allows the user to input two lists and merge them into a new list containing all even numbers followed by odd number in sorted order.
'''
list1 = []
list2 = []
#Adding list 1 elements
list1_size = int(input("Enter the size of list 1: "))
print("Enter the elements of list 1: ")
for i in range(list1_size):
    list1.append(int(input()))
print(f"list 1: {list1}")
#Adding list 2 elements
list2_size = int(input("Enter the size of list 2: "))
print("Enter the elements of list 2: ")
for i in range(list2_size):
    list2.append(int(input()))
print(f"list 2: {list2}")

list3 = list1 + list2
even_list = []
odd_list = []
for i in list3:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)
even_list.sort()
odd_list.sort()
merged_list = even_list + odd_list
print(f"Merged list: {merged_list}")
