# 01. Checking if two words are anagrams or not.
# word1 = input()
# word2 = input()


# # listen
# # silent 

# word_dict = {}

# for i in word1:
#     word_dict[i] = word_dict.get(i,0) + 1
# for i in word2:
#     word_dict[i] = word_dict.get(i,0) - 1

# for i in word_dict:
#     if word_dict[i] != 0:
#         print("Not an anagram")
#         break
# else:
#     print("Anagram")
# word_dict{
#     'l': 0,
#     'i': 0,
#     's':0,
#     't':0,
#     'e':0,
#     'n':0
# }

# 3. Find the length of the longest substring without repeating characters.
# input: "abcabcbb"
# output: 3

# abc 
# abcabcddf
# 0 1 2 3 4 5 6 7 8
# a b c a b c d d f

# s = input()
# char_dict = {}
# left = 0
# max_length = 0
# # i == right
# for i in range(len(s)):
#     if s[i] in char_dict and char_dict[s[i]] >= left:
#         left = char_dict[s[i]] + 1
#     char_dict[s[i]] = i 
    
#     ln = i - left + 1
#     max_length = max(max_length, ln)
# print(max_length)



# 2. Group all words that are anagrams of each other.
# input: words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# d = {}

# for i in words:
#     ar = sorted(i)
#     ar = "".join(ar)
#     if ar not in d:
#         d[ar] = []
#     d[ar].append(i)
# res = list(d.values())
# print(res)

arr1 = [1,2,4,3,5,6,4,3,2,1,9]
arr2 = [1,2,3,3,5,6,4,3,4,1,2,9]

dict1 = {}
dict2 = {}

for i in arr1:
    dict1[i] = dict1.get(i, 0) + 1

for i in arr2:
    dict2[i] = dict2.get(i, 0) + 1

result = []

for i in dict1:
    if i in dict2 and dict1[i] == dict2[i]:
        result.append(i)

print(result)