n = int(input("Please enter 5-digit positive integer number: "))

m = n // 10
l = m // 10
k = l // 10
j = k // 10

e = n % 10
d = m % 10
c = l % 10
b = k % 10
a = j % 10

test = ((((((e * 10) + d) * 10) + c) * 10) + b) * 10 + a

print(test)
