# Accounts Class 
class Account:
    def __init__(self, name, student_id, age, gender, phone_number):
        self.name = name
        self.student_id = student_id
        self.age = age
        self.gender = gender
        self.phone_no = phone_number

    def display_info(self):
        print("Name:", self.name)
        print("Student ID:", self.student_id)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Phone Number:", self.phone_no)


# Admission Class
class Admission(Account):
    def __init__(self, name, student_id, age, gender, phone_number, course):
        super().__init__(name, student_id, age, gender, phone_number)
        self.course = course

    def display_admission(self):
        self.display_info()
        print("Course:", self.course)


# Result Class
class Result(Admission):
    def __init__(self, name, student_id, age, gender, phone_number, course, marks):
        super().__init__(name, student_id, age, gender, phone_number, course)
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
marks = int(input("Enter marks: "))

student = Result(name, student_id, age, gender, phone, course, marks)

print("--- Student Record ---")
student.display_result()