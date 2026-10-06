# numbers = [10, 50, 40, 20, 30, 80]
# # Third largest number
# # 80 50 40
# first = second = third = -1 

# for i in numbers:
#     if i > first:
#         third = second # -1
#         second = first #-1
#         first = i #10
#     elif i > second:
#         third = second 
#         second = i 
#     elif i > third:
#         third = i 

# print(third)

# first non-repeated element

numbers = [10, 20, 30, 10, 40, 50]
10 
n = len(numbers)
for i in range (n):
    flag = False 
    for j in range (i+1, n):
        if numbers[i] (10) == numbers[j] (10):
            flag = True 
            break
    if flag == False:
        print(numbers[i]) 
        break