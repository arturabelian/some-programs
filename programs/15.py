# Палиндромы.

limit = input("Введите число: ")
limit = int(limit)
current_digit = 10

while current_digit < limit:
    str_digit = str(current_digit)
    if str_digit == str_digit[::-1]:
        print(str_digit)
    current_digit += 1