# Фибоначчи.

array = [0, 1]
index = 0
while index < 10:
    last_second_sum = array[-2] + array[-1]
    array.append(last_second_sum)
    index += 1
print(array)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]