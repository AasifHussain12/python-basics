print("While Loop Example")

#print numbers from 1 to 10
print("\nNumbers from 1 to 10:")

i = 1
while i <= 10:
    print(i, end=" ")
    i += 1

#Multiplication Table
print("\nMultiplication Table: ")

num = int(input("\nEnter a number to display its multiplication table: "))
i = 1
while i <= 10:
    print( num, "x", i, "=", num * i)
    i += 1
#Countdown  
print("\nCountdown")
count = int(input("\nEnter a number to start countdown: "))
while count >= 1:
    print(count)
    count -= 1
    
print("Countdown finished!")