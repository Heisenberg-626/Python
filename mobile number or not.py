def mobile_no_or_not (mobile_num):
    digit = len(mobile)
    if digit == 10 and mobile[0]== "7" or mobile[0]== "8" or mobile[0]== "9":
        print ("The given number is a valid mobile number.")
    else:
        print ("The given number is not a valid mobile number.")
mobile = input("Enter the mobile number: ")
mobile_no_or_not (mobile)
