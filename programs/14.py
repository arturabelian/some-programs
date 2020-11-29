# Число Армстронга.

limit = input("Введите число: ")
limit = int(limit)
numb = 10
result = []

while numb <= limit:

    str_numb = str(numb)
    len_numb = len(str_numb)
    
    total_sum = 0

    temp = numb
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** len_numb
        temp //= 10

    if numb == total_sum:
        result.append(numb)
        numb += 1
    if numb != total_sum:
        numb += 1

print(result)

# Введите число: 1000
# [153, 370, 407]