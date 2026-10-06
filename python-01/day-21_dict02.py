# a,e,i,o,u 
# Counting vowels
d = {}
d = {'e': 1}
words = input("Enter the word to count vowels: ")
# python
for i in words:
    if i in "aeiouAEIOU":
        d[i] = d.get(i, 0) + 1
print(d)