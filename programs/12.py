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

# Введите число: 100
# 2
# 3
# 5
# 7
# 11
# 13
# 17
# 19
# 23
# 29
# 31
# 37
# 41
# 43
# 47
# 53
# 59
# 61
# 67
# 71
# 73
# 79
# 83
# 89
# 97