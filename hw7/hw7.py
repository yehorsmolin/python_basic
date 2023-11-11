first_list = [0, 1, 0, 12, 3]
new_first_list = first_list[:]

zero_list = []

i = 0

while i < len(new_first_list):
    number = new_first_list[i]
    if number == 0:
        to_new_list = new_first_list.pop(i)
        zero_list.insert(0, to_new_list)
        i -= 1
    i += 1

new_first_list = new_first_list + zero_list
print(first_list, "->", new_first_list)


first_list = [0]
new_first_list = first_list[:]

zero_list = []

i = 0

while i < len(new_first_list):
    number = new_first_list[i]
    if number == 0:
        to_new_list = new_first_list.pop(i)
        zero_list.insert(0, to_new_list)
        i -= 1
    i += 1

new_first_list = new_first_list + zero_list
print(first_list, "->", new_first_list)


first_list = [1, 0, 13, 0, 0, 0, 5]
new_first_list = first_list[:]

zero_list = []

i = 0

while i < len(new_first_list):
    number = new_first_list[i]
    if number == 0:
        to_new_list = new_first_list.pop(i)
        zero_list.insert(0, to_new_list)
        i -= 1
    i += 1

new_first_list = new_first_list + zero_list
print(first_list, "->", new_first_list)


first_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
new_first_list = first_list[:]

zero_list = []

i = 0

while i < len(new_first_list):
    number = new_first_list[i]
    if number == 0:
        to_new_list = new_first_list.pop(i)
        zero_list.insert(0, to_new_list)
        i -= 1
    i += 1

new_first_list = new_first_list + zero_list
print(first_list, "->", new_first_list)


