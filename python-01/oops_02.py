# attributes - What does it have? 
# Behaviours - What can it do? 

# init() - to initialize the object with starting data
# self - to refer the current object, 

# Methods 
# Instance method - Works with a particular object.
# Class variable vs instance variable

# Modifying object state - 

class Student_details():
    def __init__(self):
        self.School_name = "SVV"

    
    def display_student_details(self,name, standard):
        self.name = name 
        self.standard = standard
        print("The Student details:")
        print(name)
        print(standard)

student1 = Student_details()
student2 = Student_details()
student3 = Student_details()
student3.School_name = "Viveham"
print(student1.display_student_details("Nandhini", "10th"))
print(student2.display_student_details("Eswari","12th"))

# Modifying object state - The state changing

