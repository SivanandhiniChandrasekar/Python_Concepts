# Reverse Pattern

# * * * *
# * * *
# * *
# *

# n = 4
# for i in range(n, 0, -1 ):
#     for j in range(1, i + 1):
#         print(j, end = " ")
#     print()



# Right Aligned Pattern
#   - - - *
#  - - * *
#  * * *
n = 4
for i in range(1, n + 1):
    for j in range(n - i): # -> Space
        print(" ", end = " ")
    for k in range(1, i + 1): # -> pattern printing
        print("*", end = " ")
    print()
    
# Right Triangle range, reverse triangle range - tips
