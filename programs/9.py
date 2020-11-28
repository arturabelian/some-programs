# Вычисление среднего арифметического.

list_of_numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
length_of_list = len(list_of_numb)

def average_func(list_of_numb, length_of_list):
    sum_of_list = sum(list_of_numb)
    print(sum_of_list) # Сумма элементов.
    print(length_of_list) # Кол-во элементов.
    average = (sum(list_of_numb)) / length_of_list # Сумма на кол-во элементов.
    return print(average)

average_func(list_of_numb, length_of_list)

# 55
# 10
# 5.5