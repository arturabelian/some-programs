# Гипотеза Коллатца.

def collatz_hypothesis(numb):
    counter = 0
    while numb != 1:
        print(numb)
        if numb % 2 == 0:
            numb = numb // 2
        else:
            numb = 3 * numb + 1

limit = input("Введите число: ")
limit = int(limit)
collatz_hypothesis(limit)
print(1)