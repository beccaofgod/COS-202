print("========================================")
print("SIMPLE MATHEMATICAL CALCULATOR")
print("========================================")

while True:

    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Clear (C)")
    print("8. OFF")

    choice = input("Enter your choice (1-8): ")

    match choice:

        case "1":
            print("You selected Addition")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            addition = num1 + num2

            print("Addition =", addition)

        case "2":
            print("You selected Subtraction")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            subtraction = num1 - num2

            print("Subtraction =", subtraction)

        case "3":
            print("You selected Multiplication")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            multiplication = num1 * num2

            print("Multiplication =", multiplication)

        case "4":
            print("You selected Division")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            if num2 == 0:
                print("Division by zero is not allowed.")

            else:
                division = num1 / num2

                print("Division =", division)

        case "5":
            print("You selected Modulus")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            modulus = num1 % num2

            print("Modulus =", modulus)

        case "6":
            print("You selected Power")

            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))

            power = num1 ** num2

            print("Power =", power)

        case "7":
            print("Calculator Cleared!")

        case "8":
            print("Calculator OFF")
            print("Thank you for using the calculator.")
            break

        case _:
            print("Invalid choice. Please try again.")