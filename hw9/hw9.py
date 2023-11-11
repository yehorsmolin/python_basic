import random

mylist = [random.randint(10, 60) for i in range(random.randint(3, 10))]
new_list = [mylist[0], mylist[2], mylist[len(mylist)-2]]
print(mylist, "->", new_list)

mylist = [random.randint(28, 132) for x in range(random.randint(3, 10))]
super_new_list = [mylist[0], mylist[2], mylist[len(mylist)-2]]
print(mylist, "->", super_new_list)

mylist = [random.randint(1, 10) for y in range(random.randint(3, 10))]
ultra_new_list = [mylist[0], mylist[2], mylist[len(mylist)-2]]
print(mylist, "->", ultra_new_list)
