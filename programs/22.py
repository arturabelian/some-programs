# Рекурсивный вывод слова.

def resursion_word(word):
  print(word)
  if word:
    return hell(word[:-1])

resursion_word("Programming")

# Programming
# Programmin
# Programmi
# Programm
# Program
# Progra
# Progr
# Prog
# Pro
# Pr
# P