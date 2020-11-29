# Обезьяна и случайность.

import random

def random_message():

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    message = ''
    for item in range(word_length):
        message += random.choice(chars)
    return message

word_length = 7
word = "HELP ME"
random_word = ''
counter = 0

while word != random_word:

    random_word = random_message()
    counter += 1
    if word == random_word:
        print(counter, random_word)

# Для получения слова H потребовалось 7 циклов.
# Для получения слова HE потребовалось 115 циклов.
# Для получения слова HEL потребовалось 20756 циклов.
# Для получения слова HELP потребовалось 1226782 цикла.
# Для получения слова HELP ME потребовалось 1226782 цикла.