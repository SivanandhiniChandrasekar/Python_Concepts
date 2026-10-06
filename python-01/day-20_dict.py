# Dictionary 
# {} - json format 
# Key - Value
# {
    # color:,
    # size:,
    # material:,
    
# }
# {
    # price:,
    # RAM storage:,
    # Processor:,
    # Screen inches:,
# }

# String, integer, tuple 
# {
#  "Name": "Sanjay",
#  "DOB": "12-04-2000",
#  "Schooling": "",
#  ""   
# }
# Name, DOB, Schooling - Keys

# CRUD - Create, Read, Update, Delete

# Creating a dictionary
# d = {}
# d = dict()
# print(type(d))
student = {
    "Name": "Ashwini",
    "DOB": "14-08-2000",
    "Marks": [90, 87, 76, 98, 59],
    "Age": 21
    
}

# print(student)
# # # Reading Keys only
# print(student.keys())
# for i in student.keys():
#     print(i)

# # # # Reading Values only
# print(student.values())

# # Reading Both
# print(student.items())
for i,j in student.items():
    print(i,j)

print(student['Subject'])

print(student.get("Subject", 6))



# # Insertion
# student['Subject'] = 5
# print(student)

# # Update
# student["Name"] = "Sathya"

# print(student)
# student.update(
#     {'Name': "Prabha", #update
#      "Age": 21}
# )

# print(student)

# # Deletion
# del student['Age'] 
# print(student)

# # del student 
# print(student)

# temp = student.pop('Age')
# print(temp)
# print(student)

# to find length of the dictionary
# print(len(student))

# creating dict from Keys list
# k = ['Name', 'Age', 'Class', 'Total_Marks']
# stu = dict.fromkeys(k, 0)
# print(stu)
# print(type(stu))

# del, pop
# popitem() -> to delete the last inserted key
# student.popitem()
# print(student)

# del student  -> including structure
# student.clear() -> keys, values

# To check a key exists in dictionary 
# if "Age" in student:
#     print("It is present")