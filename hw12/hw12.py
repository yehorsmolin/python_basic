user_input = str(input("Please enter data to create a hashtag: "))

user_input = user_input.strip().title()
hashtag = ''.join(char for char in user_input if char.isalnum())
hashtag = f"#{hashtag[:139]}"

print(hashtag)