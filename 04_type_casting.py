# Type Casting in Python

print("Type Casting Example")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

print("\nBefore Type Casting")
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))

# Convert string to integer
num1 = int(num1)
num2 = int(num2)

print("\nAfter Type Casting")
print("Type of num1:", type(num1))
print("Type of num2:", type(num2))

# Perform arithmetic operations
print("\nResults")
print("Addition       :", num1 + num2)
print("Subtraction    :", num1 - num2)
print("Multiplication :", num1 * num2)
print("Division       :", num1 / num2)