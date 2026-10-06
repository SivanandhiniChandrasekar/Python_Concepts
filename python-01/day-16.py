#n = 4

# 1 2 3 4 5 6 7 - column
    # j
# i 4 4 4 4 4 4 4 - 1
# 4 3 3 3 3 3 4 - 2
# 4 3 2 2 2 3 4 - 3
# 4 3 2 1 2 3 4 - 4
# 4 3 2 2 2 3 4 - 5
# 4 3 3 3 3 3 4 - 6
# 4 4 4 4 4 4 4 - 7

# n = 4
#  4th layer, 3rd layer, 2nd layer, 1st layer

# * * *
# * *
# *
# n - i

# * i 
# * * j(1, i+1)
# * * *
# i - left
# j - right
# 
# row count = 7
# column = 
# 
# right - left, top - bottom 
# if i == 1 or j == 1 or i == 2*n - 1 - i or j == 2*n - 1
n = 4
# m = 2 * n - 1
# for i in range(m):
#     for j in range(m):
#         mn = min(i, j, m - i - 1, m - j - 1)
#         print(n - mn, end = " ")
#     print()
    
for i in range(1,n+1):
    for j in range(n - i):
        print(" ", end = "")
    for k in range(n, n - i, -1):
        print("*", end = " ")
    print()
        
# i = 1
# j = 2
# m = 4 * 2 - 1 = 7
# m - i - 1 = 5
# m - j - 1 = 4
# mn = min(1,2,5,4)
# mn = 1
# n - mn = 3
# 4 

# 4 3 2 1 2 3 = 1 4 = 0
# Pattern concepts
#                         j - loop
# 01. Right triangle - 1, i + 1
# 02. Numbers printing - RT
# 03. Alphabets printing - RT
# 04. Square printing - n
# 05. Reverse Pattern - i loop (n, 0 , -1)
# 06. Right aligned pattern - Space + star 
# 07. Pyramid - space + star (2 * i - 1)
# 08. Hollow Square - if condition i, j
# 09. x-pattern - if condtion
# 10. z-pattern - ........
# 11. inverted pyramid - 
# 12. dia

