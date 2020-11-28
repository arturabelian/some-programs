# Обезьяна и случайность.

import random

def random_message():

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    message = ''
    for item in range(word_length):
        message += random.choice(chars)
    return message

word_length = 11
word = "HELLO WORLD"
random_word = ''
counter = 0

while word != random_word:

    random_word = random_message()
    counter += 1
    if word == random_word:
        print(counter, random_word)


# Для получения слова потребовалось 875443 запуска.