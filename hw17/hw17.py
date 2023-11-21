def correct_sentence(text):
    result = f"{text.rstrip(".").capitalize() + "."}"
    if result.count(".") >= 2:
        result = f"{text.lstrip(".").title() + "."}"
    return result

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
