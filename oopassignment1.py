# Accounts Class 
class Account:
    def __init__(self, name, student_id, phone_number, fee):
        self.name = name
        self.student_id = student_id
        self.phone_no = phone_number
        self.fee = fee

    def display_info_Accounts(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Phone Number:", self.phone_no)
        print("fee: " , self.fee)


# Admission Class
class Admission():
    def __init__(self, name, student_id, age, gender, phone_number, course):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender
        self.phone_number = phone_number
        self.course = course

    def display_admission(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Age: ", age)
        print("Gender: ", gender)
        print("Phone Number:", self.phone_number)
        print("Course:", self.course)


# Result Class
class Result():
    def __init__(self, name, student_id, course, marks):
        self.name = name
        self.student_id = student_id
        self.course = course
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        elif self.marks >= 40:
            return "C"
        else:
            return "Fail"

    def display_result(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Grade:", self.calculate_grade())


# 🎯 Main Program
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
age = int(input("Enter age: "))
gender = input("Enter gender: ")
phone = input("Enter phone number: ")
course = input("Enter course: ")
Fee = int(input("Enter Fee of the course: "))
marks = int(input("Enter marks: "))

a1 = Account(name, student_id, phone, Fee)
print("---Accounts Display---")
a1.display_info_Accounts()

a2 = Admission(name, student_id, age, gender, phone, course)
print("---Admission display---")
a2.display_admission()

a3 = Result(name, student_id, course, marks)
print("---Result---")
a3.display_result()