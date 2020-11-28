# Все простые числа.

limit = input("Введите число: ")
limit = int(limit)

current_digit = 2

while current_digit < limit:
    current_div = 2
    is_simple = True
    while current_div < current_digit:
        if current_digit % current_div == 0:
            is_simple = False
        current_div += 1
    if is_simple:
        print(current_digit)
    current_digit += 1

