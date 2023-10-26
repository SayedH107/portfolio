import math

print("This is THREE calculators in ONE, a regular one, a quadratic formula one and a celsius/fahrenheit calculator.")
pick = input("Pick which calculator you would like to use; type in 1 for regular, 2 for quadratic or 3 for converter: ")

#Calculator 1
if pick == 1:
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide(a, b):
        return a / b
    print("Pick from below the operation you would like to perform:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice(1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            # check if user wants another calculation
            # break the while loop if answer is no
            next_calculation = input("Another one? (yes/no): ")
            if next_calculation == "no":
                break

        else:
            print("Invalid Input")



#Calculator 2
if pick == 2:
    print("Important note, the quadratic formula can not solve values if the discriminant (the b²-4ac in the square root) is negative. ")
    print("This isn't the programme's fault but a limitation of the formula as a negative number can not be square rooted.")
    print("Welcome to the quadratic formula calculator!")
    print("Please type in one after the other, the coefficients in your equation, the calculator will then solve for x.")

    a = int(input("Type in your coefficient for A: "))
    b = int(input("Now type in your coefficient for B: "))
    c = int(input("Last type in your coefficient for C: "))

    negative_b = b*-1
    b_squared = b**2
    four_a_c = 4*a*c
    two_a = a*2

    sub_operation_1 = math.sqrt(b_squared-four_a_c)
    sub_operation_2 = negative_b + sub_operation_1
    sub_operation_3 = negative_b - sub_operation_1
    operation_1 = sub_operation_2/two_a
    operation_2 = sub_operation_3/two_a

    print("The two possible answers for x are:")
    print("x = " + str(operation_1))
    print("or")
    print("x = " + str(operation_2))
    print("Thank you for using the calculator.")


#Calculator 3
if pick == 3:
    celsius = int(input("Please type in the number you would like to convert from Celsius to Fahrenheit: "))
    fahrenheit = (celsius*1.8)/32
    print("Your number in Fahrenheit is: " + str(fahrenheit) + ".")

