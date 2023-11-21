import string

# ---------string_method

user_input = str(input("Please enter a letter range: "))

first_letter_index = string.ascii_letters.find(user_input[0])
second_letter_index = string.ascii_letters.find(user_input[2])

print(string.ascii_letters[first_letter_index:second_letter_index + 1])


# ---------tuple_method

# user_input = str(input("Please enter a letter range: "))
# letters_tuple = tuple(string.ascii_letters)
#
# first_letter_index = letters_tuple.index(user_input[0])
# second_letter_index = letters_tuple.index(user_input[2])
#
# result = ''.join(letters_tuple[first_letter_index:second_letter_index + 1])
#
# print(result)

