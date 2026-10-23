# STUDENT MANAGEMENT SYSTEM
'''
1. Registration
2. Subject
3. Marks 
4. Pass/Fail
5. Object modification - updation 
'''

class Student():
    total_no_of_students = 0
    def __init__(self, name, roll_number, dob,marks):
        self.name = name #Public access modifier
        self.roll_number = roll_number #Protected access modifier
        self.__dob = dob #Private access modifier
        self.marks = marks
        
        Student.total_no_of_students += 1
        
    # Getters
    def get_marks(self):
        return self.marks 
    
    @property
    def names(self):
        return self.name 
    
    @names.setter
    def names(self, updated_name):
        self.name = updated_name
        return "Updated successfully"
    
    def average_mark(self):
        if not self.marks:
            return 0 
        total = sum(self.marks.values())
        average = round(total / len(self.marks)) 
        return average
    
    def grade_calculation(self):
        average = self.average_mark()
        if average > 90:
            return 'A'
        elif average < 90 and average > 70:
            return 'B'
        elif average < 70 and average > 50:
            return 'C'
        elif average < 50 and average > 35:
            return 'D'
        else:
            return 'S'
    
    def status_checking(self):
        if not self.marks:
            return "No marks to Analyse"
        flag = 1
        for i in self.marks.values():
            if i < 35:
                flag = 0
                return "Fail"
        if flag:
            return "Pass"
        
    # Setters
    def set_mark(self, subject, updated_mark):
        if subject not in self.marks:
            return "Subject not registered to this student"
        if not 0<= updated_mark <=100:
            return "Enter valid marks"
        self.marks[subject] = updated_mark
        return "Marks updated Successfully!"
    
    def display_details(self):
        d = {
                "Name": self.name,
                "Roll_Number": self.roll_number,
                "Marks in all subject": self.marks,
                "Average": self.average_mark(),
                "Grade": self.grade_calculation(),
                "Result": self.status_checking()
            }
        return d 

class School_Student(Student):
    def __init__(self, name, roll_number, dob,marks, school_name):
        super().__init__(name, roll_number, dob,marks)
        self.school_name = school_name
    
    def display_details(self):
        d = super().display_details() 
        d["School Name"] = self.school_name
        return d

    def average_mark(self, internal_marks=0):
        if not self.marks:
            return 0 
        total = sum(self.marks.values())
        average = round(total / len(self.marks)) 
        return average + internal_marks

skl_s1 = School_Student("Aswini","es32it01",'25-09-2004',{'Tamil': 80, 'English':78,'Maths':89}, "xyz School")
print(skl_s1.name)
skl_s1.names = "Praveena"
# Student - 
print(skl_s1.names)
print(skl_s1.name)
print(skl_s1.status_checking())
print(skl_s1.display_details())
print(skl_s1.average_mark(20))

# MRO - Method Resolution Order - The order in which the methods are resolved in case of multiple inheritance. 
# Method Lookup

# name, roll_number, dob,marks
# s1 = Student("Aswini","es32it01",'25-09-2004',{'Tamil': 80, 'English':78,'Maths':89})
# print(s1.name
# print(s1._roll_number)
# print(s1.__dob)
# print(s1.get_dob())
# s1.mark_update("English",88)
# details = s1.display_details()
# for i in details:
#     print(i, details[i])
# print(s1.names)
# s1.names = "Praveena"
# print(s1.names)