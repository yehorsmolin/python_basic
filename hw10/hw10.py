import keyword
import string

variable_name = str(input("Please enter any variable name: "))
result = 0

if variable_name[0].isdigit() or variable_name in keyword.kwlist:
    result += 1

for char in variable_name:
    if char.isupper() or char in string.punctuation or char in string.whitespace:
        if char == "_":
            continue
        result += 1

if result > 0:
    print(False)
else:
    print(True)
