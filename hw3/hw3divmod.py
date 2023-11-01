n = int(input("Please enter 5-digit positive integer number: "))
test = 0

m, d = divmod(n, 10)
test = test + d

l, c = divmod(m, 10)
test = test * 10 + c

k, b = divmod(l, 10)
test = test * 10 + b

j, a = divmod(k, 10)
test = test * 10 + a
test = test * 10 + j

print(test)
