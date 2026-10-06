
# A transaction is considered valid if:

# Its value appears exactly once in the list.
# The value is greater than every previously seen valid transaction.

# Return the values of all valid transactions in the order they appear.

# Input: [4, 2, 7, 2, 9, 4, 10, 7, 12]

# Output: [9, 10, 12]

arr =  list(map(int,input().split()))
freq = {
}
for i in arr:
    freq[i] = freq.get(i, 0)+1
max_value = float('-inf')
for i in arr:
    if freq[i] == 1 and i > max_value:
        print(i, end = " ")
        max_value = i 