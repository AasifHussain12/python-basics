#Functions in python

print("Functions in Python")

#Function without parameters
def greet():
    print("Hello! Welcome to Python Functions.")
    
#Function with parameters
def add(a, b):
    return a + b

#Function to find square of a number
def square(num):
    return num * num

#Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
#Calling the functions
greet()

num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)
print("Addition of", num1, "and", num2, "is:", result)

number = int(input("\nEnter a number to find its square: "))
print("Square of", number, "is:", square(number))

number = int(input("\nEnter a number to check if it's even or odd: "))
print("The number", number, "is:", check_even_odd(number))

print("\nAll functions executed successfully.")