user_input = str(input("Please enter a number between 0 and 8640000: "))

keys_den = [1, 21, 31, 41, 51, 61, 71, 81, 91]
value_den = 'день'

days_dict = {}
for key in keys_den:
    days_dict[key] = value_den

keys_dniv = [0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 25, 26,
             27, 28, 29, 30, 35, 36, 37, 38, 39, 40, 45, 46, 47, 48, 49, 50, 55,
             56, 57, 58, 59, 60, 65, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 80,
             85, 86, 87, 88, 89, 90, 95, 96, 97, 98, 99, 100]
value_dniv = 'днів'

for key in keys_dniv:
    days_dict[key] = value_dniv

keys_dni = [2, 3, 4, 22, 23, 24, 32, 33, 34, 42, 43, 44, 52, 53, 54,
            62, 63, 64, 72, 73, 74, 82, 83, 84, 92, 93, 94]
value_dni = 'дні'

for key in keys_dni:
    days_dict[key] = value_dni

day = 86400
hour = 3600
minute = 60

user_days, user_seconds = divmod(int(user_input), day)
user_hours, user_seconds = divmod(user_seconds, hour)
user_minutes, user_seconds = divmod(user_seconds, 60)

dict_pointer = days_dict.get(user_days)

result = f"{user_days} {dict_pointer}, {str(user_hours).zfill(2)}:{str(user_minutes).zfill(2)}:{str(user_seconds).zfill(2)}"

print(result)
