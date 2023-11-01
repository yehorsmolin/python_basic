n = int(input("Please enter 4-digit integer number: "))

m, d = divmod(n, 10)
l, c = divmod(m, 10)
k, b = divmod(l, 10)

print(k)
print(b)
print(c)
print(d)
