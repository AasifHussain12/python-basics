print("For Loop Example")

#print numbers from 1 to 10 using a for loop

print("\nNumbers from 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")
    
print("\nMultiplication Table: ")
n = int(input("\nEnter a number to display its multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
    
#Sum of first n natural numbers
print("\nSum of first n natural numbers:")
n = int(input("\nEnter a number to calculate the sum of first n natural numbers: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("The sum of first ",n," natural numbers is: ", sum)