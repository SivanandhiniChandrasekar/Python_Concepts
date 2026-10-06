# Set
# To store unique values
# removes the dulicate automatically

# mobile number, emp ids, aadhar number
# CRUD 
# create, delete, read but no update --> tuple

# Creating a set
s = {1,2,3,4,5,5}
print(type(s))

# Creating an empty set
s = set()
print(type(s))

# Insertion
# Inserting single element

s.add(6)
print(s)

s.add(1)
print(s)

s.update([2,3,4,5,7])
print(s)

# Delete 
s.remove(1)
print(s)

s.discard(20)
print(s)

s.pop()
print(s)

# s.clear()
# print(s)

# del s 
# print(s)

len(s)
print(1 in s)
if 1 in s:
    print(True)
for i in s:
    print(i)
    
# Set Operations
# Union, Intersection, Difference

# Union
a = {1,2,3,4,5}
b = {3,4,5,6,7,8}

c = a.union(b)
print("Union Set operation: ", c)
d = a|b
print("Union Set operation: ",d)

# Intersection
c = a.intersection(b)
print("Intersection Set operation: ", c)
d = a & b 
print("Intersection Set operation: ", d)

# Difference
c = a - b
print("Difference: ", c)

# Reverse Difference
c = b - a 
print("Reverse Difference: ", c)

# Symmetric Difference
c = a ^ b 
print("Symmetric Difference: ", c)

# subset, superset, disjoint set
s1 = {6, 7, 9} #child
s2 = {1,2,3,4,5, 6, 7} #parent

print(s1.issubset(s2))

print(s1 <= s2)

# superset
print("Superset checking: ",s2.issuperset(s1))

# disjoint set
print(s1.isdisjoint(s2))

a = [1,2,3,3,7,9] 
b = {1,2,3,4,4}

# bank transaction - 
# Difference between set and list
# 1. in set No duplicacy, automatic duplicate removal
# 2. No indexing
# 3. unique 