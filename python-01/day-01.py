"""name = input("Enter your name here: ")

print(type(name))

age = int(input("Enter your Age: ")) Type casting
print(type(age))

print("The user name is "+ name + "and her age is" ,age)

print("Her i printed using coma")
print("The user name is", name ,"and her age is" , age)
"""
# if
# if-else
# if-elif-else
# switch -- match case 
# nested if-else 

# voting_age = int(input("Enter your age: "))
# if voting_age > 18:
#     print("You are eligible to vote")
# else:
#     print("Try next time")


balance = 1000
withdraw = int(input("Enter your amount to withdrw: "))
if withdraw > balance:
    print("Your entered amount is greater than the balance")
    print(balance)
elif withdraw == balance:
    print("Your entered amount is equal to balance amount")
    print(balance)
else:
    balance = balance - withdraw
    print("the amount is withdrawn")
    print(balance)