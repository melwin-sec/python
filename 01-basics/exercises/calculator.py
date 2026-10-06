again = "y"

while again == "y":

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice (1-4): "))
    if choice > 4 or choice < 1:
        print("Invalid choice. Please select a valid option (1-4).")

    else:
        if choice == 4:
            n_num = 2
        else:
            n_num = int(input("Enter the number of numbers to calculate: "))

    if choice == 1:
        total = 0
        for i in range(n_num):
            total += int(input("Enter number: "))
        print("sum of numbers is: ", total)
    elif choice == 2:
        total = int(input("Enter the first number: "))
        for i in range(n_num - 1):
            total -= int(input("Enter number: "))
        print("difference of numbers is: ", total)
    elif choice == 3:
        product = 1
        for i in range(n_num):
            product *= int(input("Enter number: "))
        print("product of numbers is: ", product)

    elif choice == 4:
        numerator = int(input("Enter the first number: "))
        denominator = int(input("Enter the second number: "))
        if denominator != 0:
            print("quotient of numbers is: ", numerator / denominator)
        else:
            print("Error: Division by zero is not allowed.")

    again = input("Do you want to calculate again? (y/n): ")
