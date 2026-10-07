def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

Quit = True

while Quit:
    num1 = int(input("enter first number: "))
    result =0
    calc = True
    while calc:
        operator = input("enter operator[ + - * / ] : ")
        num2 = int(input("enter second number: "))
        if operator == "+":
            result = addition(num1, num2)
        elif operator == "-":
            result = subtraction(num1, num2)
        elif operator == "*":
            result = multiplication(num1, num2)
        elif operator == "/":
            result = division(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")
        usr = str(input("continue with answer? [y/n] otherwise Quit : "))
        if usr == "n":
            calc = False
        elif usr == "y":
            num1 = result
        else:
            calc = False
            Quit = False