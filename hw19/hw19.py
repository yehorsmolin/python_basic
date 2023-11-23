import string


def is_palindrome(text: str) -> bool:
    text_list = []
    for char in text:
        if char in string.punctuation or char in string.whitespace:
            continue
        else:
            text_list.append(char)

    text = ''.join(text_list)

    return text.lower() == text.lower()[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")
