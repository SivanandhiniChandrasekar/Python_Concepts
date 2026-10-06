# 01. Missing values in a number series
n = [1,2,4,5,6,7]
mx = max(n)
# for i in range(1,mx):
#     if i not in n:
#         print(i)
#         break
# time complexity  - O(n)
all_n = set(range(1, mx+1))
n_set = set(n)
print(all_n - n_set)

# 02. Find the common elements without duplicates
n1 = [1,2,3,4,4,5,6,7]
n2 = [2,4,4,5,5,6,7,7,8,8,9,0]

# step1 - Convert to set
set1 = set(n1)
set2 = set(n2)

result = set1.intersection(set2)
print(result)

# 03. find common characters in strings
word1 = "Hello"
word2 = "World"
set1 = set(word1)
set2 = set(word2)
result = set1.intersection(set2)
print(result)