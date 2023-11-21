user_input = str(input("Please enter your number: "))
result = int(user_input)
digits_list = []

while result > 9:
    digits_list = [int(digit) for digit in str(result)]
    result = 1
    for element in digits_list:
        result *= element

print("Result:", result)
