import random


def common_elements(beg_range, end_range):

    first_list = []
    second_list = []

    for element in range(random.randint(beg_range, end_range)):
        if element % 3 == 0:
            first_list.append(element)

    for elewoment in range(random.randint(beg_range, end_range)):
        if elewoment % 5 == 0:
            second_list.append(elewoment)

    first_list = set(first_list)
    second_list = set(second_list)

    set_intersection = first_list.intersection(second_list)
    return set_intersection


beg_range = int(input("Please enter the first range pointer: "))
end_range = int(input("Please enter the second range pointer: "))

print(common_elements(beg_range, end_range))

