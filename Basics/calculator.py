print("enter number 1:")
num1 = float(input())
print("enter number 2:")
num2 = float(input())
print("enter operation (+, -, *, /):")
operation = input()

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2

print("Result:", result)