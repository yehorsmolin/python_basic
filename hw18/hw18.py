import random


def common_elements():

    first_list = []
    second_list = []

    for element in range(random.randint(1, 200)):
        if element % 3 == 0:
            first_list.append(element)

    for elewoment in range(random.randint(1, 200)):
        if elewoment % 5 == 0:
            second_list.append(elewoment)

    first_list = set(first_list)
    second_list = set(second_list)

    set_intersection = first_list.intersection(second_list)
    return set_intersection


result = common_elements()


print(result)
