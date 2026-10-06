# Task - 01

# 200 - success
# 400 - error not found 
# 403 - forbidden
# 500 - internal 

# Match - case

user = int(input("Enter a number from 1 to 7: "))
match user:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")    
    case 7:
        print("Saturday")
    case _:
        print("Enter valid number")    
