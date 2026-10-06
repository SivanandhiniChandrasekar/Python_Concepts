# Pyramid pattern

# 1....A - 1 + 2 => (i * 2 - 1) => 1
# 2...BBB- 3 => (2 * 2 - 1) => 3
# 3..CCCCC - 5 
# 4.DDDDDDD - 7
# 5EEEEEEEEE - 9

# no.of.rows = 5
# spaces = 4, 3, 2, 1

n = 5
# Rows Spaces Alphabet
# 1     4       1 +2
# 2     3       3 +2
# 3     2       5 +2
# 4     1       7
# 5     0       9


# spaces - decreases by 1
# alphabets - 1 .. increases 2
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end = "")
    for k in range(i * 2 - 1):
        print(chr(64+i), end = "")
    print()
    
#     A|A
#    BB|BB
#   CCC|CCC
#  DDDD|DDDD
# EEEEEEEEEE