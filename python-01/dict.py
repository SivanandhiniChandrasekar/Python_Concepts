# Group Words by Length

words = ["cat", "dog", "apple", "bat", "orange"]
d = {}
for i in words:
    ln = len(i) 
    d[ln] = d.get(ln,[])
    d[ln].append(i) 
print(d)

