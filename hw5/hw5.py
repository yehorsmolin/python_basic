first_example = [1, 2, 3, 4, 5, 6]

first_list = int(-1 * (len(first_example) / 2) // 1 * -1)
new_first_list = [
    first_example[:first_list],
    first_example[first_list:]
    ]

print(first_example, "=>", new_first_list)

second_example = [1, 2, 3]

second_list = int(-1 * (len(second_example) / 2) // 1 * -1)
new_second_list = [
    second_example[:second_list],
    second_example[second_list:]
    ]

print(second_example, "=>", new_second_list)

third_example = [1, 2, 3, 4, 5]

third_list = int(-1 * (len(third_example) / 2) // 1 * -1)
new_third_list = [
    third_example[:third_list],
    third_example[third_list:]
    ]

print(third_example, "=>", new_third_list)

fourth_example = [1]

fourth_list = int(-1 * (len(fourth_example) / 2) // 1 * -1)
new_fourth_list = [
    fourth_example[:fourth_list],
    fourth_example[fourth_list:]
    ]

print(fourth_example, "=>", new_fourth_list)

fifth_example = []

fifth_list = int(-1 * (len(fifth_example) / 2) // 1 * -1)
new_fifth_list = [
    fifth_example[:fifth_list],
    fifth_example[fifth_list:]
    ]

print(fifth_example, "=>", new_fifth_list)
