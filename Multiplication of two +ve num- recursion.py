def multi_num(n1,n2):
    if n2==1:
        return n1
    else:
        return n1+multi_num(n1,n2-1)
num_1 = int(input("Enter the first number: "))
num_2 = int(input("Enter the second number: "))
print(multi_num(num_1,num_2))