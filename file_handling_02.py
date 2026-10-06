# 5. Log File Analysis
# Create app.log:
# INFO: User login successful
# ERROR: Database connection failed
# INFO: User logout successful
# WARNING: Disk space is low
# ERROR: File not found
# INFO: User login successful
# Write a program to:
# 1.	Read the log file.
# 2.	Count INFO, WARNING, and ERROR messages.
# 3.	Store only ERROR messages in errors.log.
# Expected output:
# INFO: 3
# WARNING: 1
# ERROR: 2
# errors.log:
# ERROR: Database connection failed
# ERROR: File not found

d = {}
with open("C:\\Users\\ASUS Vivobook\\Documents\\Siva\\Coding-session\\app1.log","r") as file:
    f = file.readlines()
    for i in f:
        word = i.split(":")
        d[word[0]] = d.get(word[0], 0)+1
        if word[0] == 'ERROR':
            with open("C:\\Users\\ASUS Vivobook\\Documents\\Siva\\Coding-session\\errors.log","a") as file:
                file.write(i)
for i in d:
    print(i, d[i])      