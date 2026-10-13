# Question 1: Arithmetic Operations on Two Integers

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))

print("Addition       :", a + b)
print("Subtraction    :", a - b)
print("Multiplication :", a * b)

if b != 0:
    print("Division       :", a / b)
    print("Floor Division :", a // b)
    print("Modulus        :", a % b)
else:
    print("Division       : Error - Cannot divide by zero")
    print("Floor Division : Error - Cannot divide by zero")
    print("Modulus        : Error - Cannot divide by zero")

print("Exponentiation :", a ** b)