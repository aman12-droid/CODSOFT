# Simple Calculator using if-elif-else conditions

def calculator():
    print("Welcome to the Calculator!")
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    choice = input("choose the number (1/2/3/4): ")

    if choice == '1':
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = n1 + n2
        print(f"The result of {n1} + {n2} is: {result}")
    elif choice == '2':
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = n1 - n2
        print(f"The result of {n1} - {n2} is: {result}")
    elif choice == '3':
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        result = n1 * n2
        print(f"The result of {n1} * {n2} is: {result}")
    elif choice == '4':
        n1 = float(input("Enter the first number: "))
        n2 = float(input("Enter the second number: "))
        if n2 != 0:
            result = n1 / n2
            print(f"The result of {n1} / {n2} is: {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print(" Please select a valid operation.")

calculator()
