#first create class and just pass predefined method and take its variable and print
#second class and pass method of  
#third class and pass method of init which is predefined function used to settle variable
class Addmission:
    pass
a1 = Addmission()
a1.name = "Ali"
a1.age = 22
print(a1.name)
class Ali:
    def study(self):
        print("studying")
a2=Ali()
a2.study()
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
s1 = Student("Ali",22)
s2= Student("amir",32)
s3 = Student("Khadija",34)
print(s1.name,s1.age)
class standie:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no =roll_no
        self.marks = marks
    def show_details(self):
        print("name : ",self.name)
        print("roll no : ", self.roll_no)
        print("marks : ", self.marks)
ss1 = standie("AAA",22,243)
ss1.show_details()
class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color
    def start(self):
        print("Name: ", self.name)
        print("model : ", self.model)
    def stop(self):
        print("name: ",self.name)
        print("color:" ,self.color)

c1 = Car("Toyota","civic","black")
c2 = Car("Honda","Carolla", "white")
c1.start()
c1.stop()
c2.start()
c2.stop()