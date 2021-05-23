import argparse

parser=argparse.ArgumentParser(
    description='''Select Operators by choosing options '1, 2, 3 & 4'. ''',
    epilog="""Author: Faisal Rehman.""")
args=parser.parse_args()

print("Type '-h' or '--help' to show help")

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y

num1: int = int(input("Enter a Number: "))

print("Select Operator Below.")
print("1- Addition")
print("2- Subtraction")
print("3- Multiplication")
print("4- Division")

ope = input("Enter Operator Number: ")

num2 = int(input("Enter Another Number: "))

if ope == '1':
    print("Your Answer Is: ", num1, '+', num2, "=", add(num1, num2))
elif ope == '2':
    print("Your Answer Is: ", num1, "-", num2, "=", subtract(num1, num2))
elif ope == '3':
    print("Your Answer Is: ", num1, "x", num2, "=", multiply(num1, num2))
elif ope == '4':
    print("Your Answer Is: ", num1, "÷", num2, "=", divide(num1, num2))
else:
    print("Wrong input!")
