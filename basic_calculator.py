num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter an operation (+ or -): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
else:
    print("Invalid operation.")

print(f"Result: {result}")
