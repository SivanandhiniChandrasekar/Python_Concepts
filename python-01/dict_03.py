cart = {
    "Gadgets":{
        "Name": "Laptop",
        "Id": "LaDe20262134",
        "Brand": "Dell",
        "Processor": "AMD",
        "Screen_Size": "1240 X 1240",
        "Storage": 512
    },
    "Books":{
        "Book_Name": "Atomic Habits",
        "Pages": 216,
        "Price": 100
    },
    "Toys":{
        "Toy_name": "Teddy",
        "Color": "Pink",
        "Price": 500
    }
} 

# product = input("Enter the product: ")
product = "Gifts"
if product in cart:
    # payment process
    cart[product] = "Ordered"
    print("Before:" , cart)
else:
    cart[product] = "Gifts"
    print("After adding to cart:" , cart)

    # Payment process
    cart[product] = 'Ordered'
    print("After ordering:" , cart)
    
del cart[product]
print("Try these things also that you might love the most...!")
print("After: ",cart)

print(len(cart))

k = ['Name', 'Age', 'Class', 'Total_Marks']
stu = dict.fromkeys(k, 0)
print(stu)
print(type(stu))

# fromkeys --> {
#     "Name": 0,
#     "Age": 0,
#     "Class": 0,
#     "Total_Marks" : 0
# }

# popitem --> last inserted key
# print("Toys" in  cart)