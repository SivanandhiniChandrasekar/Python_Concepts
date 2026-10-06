# For loop - It is used to iterate a sequence

# Lists, Strings, Tuples, set, dictionary

# for(int i = 0; i < n; i++)
# print("Using start, stop and step")
# for i in range(0,11,1):
#     print(i)
    
# print("Using only stop")
# for i in range(5,15,2):
#     print(i)

# 0, len(n)-1

# count the frequency of vowels  - a,e,i, o, u in a string
# s = input("Enter the string: ") # nandhini = 8
# a = 1
# e = 0
# i = 2
# o = 0
# u = 0
# for j in range(len(s)): 
#     # j = 6
#     # j = len(s) - 1
#     if s[j]  == 'a': s[0] = a s[1] = s
#         a += 1
#     elif s[j] == 'e':
#         e += 1
#     elif s[j] == 'i':
#         i += 1
#     elif s[j] == 'o':
#         o += 1
#     elif s[j] == 'u':
#         u += 1

# for j in s:
#     print(j)

# print(a,e,i,o,u)    

# 6. Store runs scored in each over.Find the highest run scored in a single over.
# input: runs = [6,12,4,15,8]
# output: 151

arr = [6,12,4,15,8]
print(max(arr))
m = 0
for i in arr: 
    if m < i:
        m = i 
print(m)