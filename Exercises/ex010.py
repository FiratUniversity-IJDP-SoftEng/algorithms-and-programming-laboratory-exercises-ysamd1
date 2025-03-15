# Your Student ID:220543009
# Your Name and Surname:Yaşam Doğa Çevik
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            operation = input("Choose operation (+, -, *, /): ").strip()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    print("Error: Division by zero is not allowed!")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation! Please choose +, -, *, or /.")
                continue

            print(f"Result: {result:.2f}")

        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != "yes":
            print("Goodbye!")
            break
calculator()
