# Все совершенные числа.

limit = input("Введите число: ")
limit = int(limit)

numb = 1

while numb <= limit:
    total_sum = 0
    div = 1
    while div < numb:
        if not numb % div:
            total_sum += div
        div += 1
    if total_sum == numb:
        print(numb)
    numb += 1

# Введите число: 1000
# 6
# 28
# 496