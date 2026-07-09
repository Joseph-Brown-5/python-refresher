# Goal: To make a calculator that specifically only utilizes if statmenets and user input
#       take 2 inputs from the user and an operator and do the approprate math

num1 = int(input("Please enter the first number: "))
num2 = int(input("Please enter the second number: "))
op = input("Please enter the desired operation (+-/*): ")

if not op:
    print("no operator provided")
elif op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
