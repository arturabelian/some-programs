# Рекурсивное преобразование списка чисел в число.

def resursive_digit(ary):
  return resursive_digit(ary[:-1]) * 10 + ary[-1] if ary else 0

resursive_digit([1, 2, 3, 4, 5])

# 12345