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
        self.name = name
        self.roll_number = roll_number
        self.dob = dob 
        self.marks = marks
        
        Student.total_no_of_students += 1
    
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
            return "True"
        
    def mark_update(self, subject, updated_mark):
        if subject not in self.marks:
            return "Subject not registered to this student"
        if not 0<= updated_mark <=100:
            return "Enter valid marks"
        self.marks[subject] = updated_mark
        
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
# name, roll_number, dob,marks
s1 = Student("Aswini","es32it01",'25-09-2004',{'Tamil': 80, 'English':78,'Maths':89})
s1.mark_update("English",88)
details = s1.display_details()
for i in details:
    print(i, details[i])
