while True:

    yes_list = ["yes", "YES", "Yes", "YEs", "yEs", "yES", "y", "Y"]
    first_number = float(input("Please enter first number: "))
    second_number = float(input("Please enter second number: "))
    action = input("Please enter action: ")

    if action != "+" and action != "-" and action != "*" and action != "/":
        print("Please enter one of the following actions: +, -, *, /")
    elif action == "+":
        summation = first_number + second_number
        print("Your result is:", summation)
    elif action == "-":
        deduct = first_number - second_number
        print("Your result is:", deduct)
    elif action == "*":
        multiply = first_number * second_number
        print("Your result is:", multiply)
    elif action == "/" and second_number != 0:
        divide = first_number / second_number
        print("Your result is:", divide)
    elif action == "/" and second_number == 0:
        print("You can't divide by", second_number)

    request = str(input("Do you want to perform another calculation? "))
    if request in yes_list:
        continue
    else:
        break
