#A Basic Calculator.
num1 = input("Enter Number: ")
operater = input("Operator: ")
num2 = input("Enter 2nd Number: ")
if operater == "+":
    print(float(num1) + float(num2))
elif operater == "-":
    print(float(num1) - float(num2))
elif operater == "*":
    print(float(num1) * float(num2))
elif operater == "/":
    print(float(num1) / float(num2))
else:
    print("Invalid")