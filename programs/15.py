# Палиндромы.

limit = input("Введите число: ")
limit = int(limit)
current_digit = 10

while current_digit < limit:
    str_digit = str(current_digit)
    if str_digit == str_digit[::-1]:
        print(str_digit)
    current_digit += 1

# Введите число: 200
# 11
# 22
# 33
# 44
# 55
# 66
# 77
# 88
# 99
# 101
# 111
# 121
# 131
# 141
# 151
# 161
# 171
# 181
# 191