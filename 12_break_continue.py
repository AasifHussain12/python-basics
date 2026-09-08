#Break and Continue Statements in Python

print("Break and Continue Example")

# Example of break statement
print("\nBreak Statement")

for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    print("Current value of i:", i)

# Example of continue statement
print("\nContinue Statement")

for i in range(1, 11):
    if i == 6:
        continue
    print("i =", i)
    
#Practical Example
print("\nSkipping Even Numbers using Continue Statement")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print("Odd number:", i)