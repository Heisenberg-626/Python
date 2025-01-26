'''
Author: Sourav V S
Date: 03-12-2024
This program defines a function that prints fibonacci series upto a limit.
'''
def fibonacci(n):
    first_num = 1
    second_num = 0
    third_num = 0
    while (third_num <= n):
        print(third_num, end=" ")
        third_num = first_num +second_num
        first_num = second_num
        second_num = third_num
