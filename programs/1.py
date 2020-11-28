# Генератор паролей.

import random

chars = "abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = input("Password length? ")
int_length = int(length)
password = ''
for item in range(int_length):
    password += random.choice(chars)
print(password)

# Length? 10
# coj9HLPsiY