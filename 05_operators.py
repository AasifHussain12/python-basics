print("Python Operators")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

print("\nArithematic Operators")
print("Addition     :", a+b)
print("Subtraction  :", a-b)
print("Multiplication :", a*b)
print("Division     :", a/b)
print("Floor Division :", a//b)
print("Modulus      :", a%b)
print("Exponent     :", a**b)

print("\nComparison Operators")
print("a == b", a==b)
print("a != b", a!=b)
print("a > b", a>b)
print("a < b", a<b)
print("a >= b", a>=b)
print("a <= b", a<=b)

print("\nAssignment Operator")
c = a
print("Value of c :", c)
c += b
print("After c += b :", c)

print("\nLogical Operators")
print("(a > 0 and b > 0):", a > 0 and b > 0)
print("(a > 0 or b > 0):", a > 0 or b > 0)
print("not(a > b):", not (a>b))