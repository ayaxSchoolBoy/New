import math

print("Welcome to the Python Calculator!\n")
print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Exponentiation")
print("7. Square Root")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")
print("11. Logarithm (natural)")
print("12. Logarithm (base 10)")
print("13. EXIT")

choice = input("\nEnter choice (1-13): ")

if choice == '1':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 + num2)

elif choice == '2':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 - num2)

elif choice == '3':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 * num2)

elif choice == '4':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    if num2 == 0:
        print("Error! must be greater than 0.")
    else:
        print("Result:", num1 / num2)

elif choice == '5':
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Result:", num1 % num2)

elif choice == '6':
    num1 = float(input("Enter base number: "))
    num2 = float(input("Enter exponent: "))
    print("Result:", num1 ** num2)

elif choice == '7':
    num = float(input("Enter number: "))
    print("Result:", math.sqrt(num))

elif choice == '8':
    num = float(input("Enter angle in degrees: "))
    print("Result:", math.sin(math.radians(num)))

elif choice == '9':
    num = float(input("Enter angle in degrees: "))
    print("Result:", math.cos(math.radians(num)))

elif choice == '10':
    num = float(input("Enter angle in degrees: "))
    print("Result:", math.tan(math.radians(num)))

elif choice == '11':
    num = float(input("Enter number: "))
    if num <= 0:
        print("Error! must be greater than 0.")
    else:
        print("Result:", math.log(num))

elif choice == '12':
    num = float(input("Enter number: "))
    if num <= 0:
        print("Error! must be greater than 0.")
    else:
        print("Result:", math.log10(num))
elif choice == '13':        
    print("EXIT")
else:
    print("Invalid input. Please restart the program and choose the correct option.")