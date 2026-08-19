print("Welcome to the calculator program!")
print("You can perform addition, subtraction, multiplication, and division.")
print("Please enter two integers to perform calculations.") 

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = first_number + second_number
    print(f"The result of {first_number} + {second_number} is: {result}")
elif operation == "-":
    result = first_number - second_number
    print(f"The result of {first_number} - {second_number} is: {result}")
elif operation == "*":
    result = first_number * second_number
    print(f"The result of {first_number} * {second_number} is: {result}")
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
        print(f"The result of {first_number} / {second_number} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

