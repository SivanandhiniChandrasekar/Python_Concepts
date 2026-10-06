# # # List
# # # Insertion
# # # .append()
# # arr = []
# # arr.append(1) # single value addition
# # arr.extend([2,3,4]) # multiple values
# # print(arr)
# # arr.pop(0) # Position based deletion
# # arr.remove(3)
# # print(arr)
# # # arr.clear()
# # # print(arr)
# # ar1 = arr[0] # Element 
# # ar = arr.index(4) # getting index value
# # print(ar, ar1)
# # arr2 = arr.copy()
# # print(arr2)
# arr = [2,1,5,6,3,0,9,8,76,43,23]
# # print(sorted(arr))
# # print(arr)
# # print(arr.sort())
# # print(arr)
# arr.reverse() arr[::-1]
# arr.sort(reverse=True)
# print(arr.count(3))

# # Slicing Operators
# arr = [2,1,5,6,3,0,9,8,76,43,23]

#   #    0 1 2 3 4 5 6 7  8  9 10
# #                         -3  -2  -1
# a = arr[1:5:2]
# # 1 - starting position
# # 5 - Stopping position
# # 2 - Step 
# print(a)
# # [1,6]
# # print(arr[::-2])
# print(arr[:6])
# print(arr[:])

# max(arr)
# min(arr)
# sum(arr)
# type(arr)
# lst = list(range(10))
# print(lst)
# print(abs(-4))
# print(round(4.67853)) -> 
# print(all([True, False, False]))
# print(all([False, False, False]))
# print(all([True, True, True]))

# STRING METHODS:

# 
# word = "vowels in a string"

# # upper
# print(word.upper())
# # lower
# print(word.lower())
# # strip 
# print(word.strip())
# # replace
# print(word.replace("in","is"))
# # split
# print(word.split(" "))
# words = word.split(" ")
# print(" ".join(words))
# # arr = list(map(int,input("Enter an array: ").split()))
# # print(arr)

# # index
# print(word.index("string"))

# # find
# print(word.find("in"))

# # startswith
# print(word.startswith(" "))

# # endswith
# print(word.endswith("ng"))

# # word = " "
# # isalpha()
# print(word.isalpha())

# # isdigit()
# print(word.isdigit())

# # isspace()
# print(word.isspace())

# # Capitalize
# print(word.capitalize())

# # title
# print(word.title())

# word = "a1b2c3"
# # isalnum
# print(word.isalnum())


# # Dictionary methods
# # Insertion nd deletion
# d = {'a':10, 'a': 50}
# d['a'] = 10
# d.update({'b':20, 'c':30})

# # Accessing or traversing
# d.keys()
# d.values()
# d.items()
# d.get() 
# d['a']

# # deletion
# # del d 
# d.pop('a', 0)
# d.popitem()
# d.clear()
# del d['a']

# enumerate 
# arr = [1,2,34,56,78,99]
# for index, element in enumerate(arr):
#   print(index, element)
  

# for i in range(len(arr)):
#   arr[i] = arr[i] * 2
  
# map
# res = list(map(lambda x:x*2, arr))
# print(res)



# print(len(100))
# output: TypeError

# print(list('Hello'))
# # output: ['H', 'e',...]

# print(max('abc'), max([123]))

# print(bool([]), bool([0]))

s = 'hello'
s = s.replace('h', 'H')
print(s)