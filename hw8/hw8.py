first_list = [1, 3, 5]
new_first_list = first_list[:]

total = 0

if new_first_list:
    for i, el in enumerate(new_first_list):
        if i % 2 == 0:
            total = total + el
    result = total * new_first_list[len(new_first_list) - 1]
    print(first_list, "=>", result)

else:
    print(0)


first_list = [6]
new_first_list = first_list[:]

total = 0

if new_first_list:
    for i, el in enumerate(new_first_list):
        if i % 2 == 0:
            total = total + el
    result = total * new_first_list[len(new_first_list) - 1]
    print(first_list, "=>", result)

else:
    print(0)


first_list = []
new_first_list = first_list[:]

total = 0

if new_first_list:
    for i, el in enumerate(new_first_list):
        if i % 2 == 0:
            total = total + el
    result = total * new_first_list[len(new_first_list) - 1]
    print(first_list, "=>", result)

else:
    print(first_list, "=>", 0)