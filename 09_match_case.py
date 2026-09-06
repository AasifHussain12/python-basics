print("Match Case Example")
print("\nChoose an Operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("\nEnter your choice (1-4): "))

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

match choice:
    case 1:
        print("Result: ", num1 + num2)
    case 2:
        print("Result: ", num1 - num2)
    case 3:
        print("Result: ", num1 * num2)
    case 4:
        if num2 != 0:
            print("Result: ", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid choice. Please select a valid operation.")