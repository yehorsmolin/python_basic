first_list = [12, 3, 4, 10]
new_first_list = first_list[:]

if len(new_first_list) == 0:
    print(first_list, "=>", new_first_list)
else:
    first_number = new_first_list.pop(len(new_first_list)-1)
    new_first_list.insert(0, first_number)
    print(first_list, "=>", new_first_list)


second_list = [1]
new_second_list = second_list[:]

if len(new_second_list) == 0:
    print(second_list, "=>", new_second_list)
else:
    second_number = new_second_list.pop(len(new_second_list)-1)
    new_second_list.insert(0, second_number)
    print(second_list, "=>", new_second_list)


third_list = []
new_third_list = third_list[:]

if len(new_third_list) == 0:
    print(third_list, "=>", new_third_list)
else:
    third_number = new_third_list.pop(len(new_third_list)-1)
    new_third_list.insert(0, third_number)
    print(third_list, "=>", new_third_list)


fourth_list = [12, 3, 4, 10, 8]
new_fourth_list = fourth_list[:]

if len(new_fourth_list) == 0:
    print(fourth_list, "=>", new_fourth_list)
else:
    fourth_number = new_fourth_list.pop(len(new_fourth_list)-1)
    new_fourth_list.insert(0, fourth_number)
    print(fourth_list, "=>", new_fourth_list)
