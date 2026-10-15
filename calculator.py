
import math

def calculator():
    while True:
        print("\n===== SCIENTIFIC CALCULATOR =====")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√)")
        print("7. Sin (degrees)")
        print("8. Cos (degrees)")
        print("9. Tan (degrees)")
        print("10. Log base 10")
        print("11. Natural Log (ln)")
        print("12. Exit")

        choice = input("\nChoose (1-12): ")

        try:
            if choice == "12":
                print("Calculator closed. Goodbye!")
                break

            elif choice in ["1", "2", "3", "4", "5"]:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))

                if choice == "1":
                    result = a + b
                elif choice == "2":
                    result = a - b
                elif choice == "3":
                    result = a * b
                elif choice == "4":
                    if b == 0:
                        print("Error: Cannot divide by zero!")
                        continue
                    result = a / b
                else:
                    result = a ** b

                print("Result =", result)

            elif choice == "6":
                x = float(input("Enter number: "))
                if x < 0:
                    print("Error: Negative number!")
                    continue
                print("Result =", math.sqrt(x))

            elif choice in ["7", "8", "9"]:
                angle = float(input("Enter angle in degrees: "))
                radians = math.radians(angle)

                if choice == "7":
                    result = math.sin(radians)
                elif choice == "8":
                    result = math.cos(radians)
                else:
                    if math.isclose(
                        math.cos(radians), 0,
                        abs_tol=1e-12
                    ):
                        print("Error: Tan is undefined!")
                        continue
                    result = math.tan(radians)

                print("Result =", round(result, 10))

            elif choice in ["10", "11"]:
                x = float(input("Enter positive number: "))

                if x <= 0:
                    print("Error: Number must be positive!")
                    continue

                if choice == "10":
                    print("Result =", math.log10(x))
                else:
                    print("Result =", math.log(x))

            else:
                print("Invalid choice! Choose 1-12.")

        except ValueError:
            print("Error: Please enter a valid number!")
        except OverflowError:
            print("Error: Result is too large!")
        except ZeroDivisionError:
            print("Error: Division by zero!")

calculator()
