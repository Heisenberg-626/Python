def add_num(n1,n2):
    if n2==0:
        return n1
    else:
        return add_num(n1+1,n2-1)
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print("Sum of two numbers: ",add_num(num_1,num_2))