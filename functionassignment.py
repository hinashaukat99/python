#assignment3
def addition(a, b):
    print("Sum =", a + b)

def subtraction(a, b):
    print("Difference =", a - b)

def multiplication(a, b):
    print("Product =", a * b)

def division(a, b):
    if b != 0:
        print("Quotient =", a / b)
    else:
        print("Cannot divide by zero")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition(num1, num2)
subtraction(num1, num2)
multiplication(num1, num2)
division(num1, num2)