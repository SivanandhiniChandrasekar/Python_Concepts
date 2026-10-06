# Pyramid Pattern

#     A - 1
#    BBB - 3
#   CCCCC - 5
#  DDDDDDD - 7
# EEEEEEEEE - 9

# 1. count the rows - 5
# 2. changes in column - odd numbers (i * 2 - 1 = 1)
# 3. 3rd for loop - characters

# n = int(input())
# n = 5
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print("", end = " " )
#         # if i % 2 != 0: 
#     for k in range(i * 2 - 1):
#         print(chr(64 + i), end = "")
#     print()

# Hollow Square

#j=1 2 3 4 5
# * * * * * i = 1
# *       * 2
# *       * 3
# *       * 4
# * * * * * 5

n = 5
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if i == 1 or j == 1:
#             print("*", end = "")
#         elif i == n or j == n:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()

# 1 2 3 4 5
# # . . . # 1 (1, 5)
# . # . #(2, 4) . 2
# . . #(3, 3) . . 3
# . #(4, 2) . # . 4
# #(5, 1) . . . # 5
n = 5
for i in range(1, n + 1): 
    for j in range(1, n + 1): 
        if i == j:
            print("#", end = " ")
        elif j == n - i + 1: 
            print("#", end = " ")
        else:
            print(".", end = " ")
    print()