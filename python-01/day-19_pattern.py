# Inverted Pyramid
# Diamond Pattern

# ******* - 7
#  *****  - 5
#   ***   - 3
#    *    - 1

# Row count - 4
# space  - 0, 1, 2, 3
# star (pattern) - 

# n = 4
# for i in range(n):
#     for j in range(n - i):
#         print(" ", end = "")
#     for k in range(2 * i -1):
#         print("*", end = "")
#     print()
# for i in range(n, 0, -1):
#     for j in range(n - i):
#         print(" ", end = "")
#     for k in range(2 * i -1):
#         print("*", end = "")
#     print()

# Hollow pyramid
# 1234567
#1   *
#2  * *
#3 *   *
# #4*******
# n = 4
# for i in range(1, n + 1):
#     for j in range(n - i):
#         print(" ", end = "")
#     for k in range(2 * i - 1):
#         if k == 0 or k == 2 * i - 2 or i == n:
#             print("*", end = "")
#         else:
#             print(" ", end = "")
#     print()
    
n = 5
# 1       5
#   2   4
#     3
#   2   4
# 1       5

# Pascal's Triangle
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# row count = 5
# colum changes = space -- decreasing, numbers -- increasing

# column 1 - 1
# column 2 - 1 1
# column 3 
# column 4 
# column 5

#  num = 1
#  1 - 2 - 1
# num, 

# Combination 
# nCr = n! / r! * (n - r)!
# 5C0 = 1
# nC1 = 
# ...
# 5C5 = 1
# curr = prev * (i - j) // (j + 1)

n = 4
for i in range(n): #1
    num = 1
    for j in range(n - i):
        print(" ", end = "")
    for k in range(i + 1):
        print(num, end = " ")
        num = num * ( i - k) // (k + 1) # 1 * (0) // 1) = 0
    print()
    
#  [[1]]
    
# Pascal's Triangle
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

# Combination = nCr = n!/ r! * (n - r)!
# 5
# column chnages - spac dec, num increasing
# 