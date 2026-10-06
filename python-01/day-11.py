# nested for loop
# Common Patterns - Right Triangle, Reverse Triangle, Left Triangle, Square Pattern, Star, Diamond, half-diamond

# Right Trianlge
# *
# * *
# * * *
# * * * *


# n = 4 - no.of.rows
# for i in range(1, n + 1): - row 
#     for j in range(1, i + 1): -(1,2)
#         print("*", end=" ")
#     print()


# 2. Numbers printing

# ouput:
# 1
# 2* 2*
# 3 3 3
# 4* 4* 4* 4* ....

# i % 2 == 0:
#     print(i + "*")

# A
# A B 
# A B C

# ASCII value - A TO Z => 65, a to z => 96
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        
        print(chr(64 + i), end = " ")
    print()

# Square Pattern
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

# 1. Count the rows
# 2. Changes in the column
# 3. print - j loop range condition

# for i in range(1, 4 + 1):
#     for j in range(1, 4 + 1):
#         print(j, end = " ")
#     print()

# 2 4 6 8
# 10 12 14 16
# 18 20 22 24
# 26 28 30 32
count = 1
for i in range(1, 5):
    for j in range(1, 5): 
        print(count * 2, end = " ")
        count += 1 
    print()