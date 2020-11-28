# Факториал.

def factorial(numb):
  return numb * factorial(numb - 1) if numb else 1

factorial(5)
# 120