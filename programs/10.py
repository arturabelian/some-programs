# Азбука морзе.

# -*- coding: utf-8 -*-

message = input("Введите сообщение: ").upper()
morse = []

for item in message:
    if item == "А":          morse.append("( .- )")
    elif item == "Б":        morse.append("( -... )")
    elif item == "В":        morse.append("( .-- )")
    elif item == "Г":        morse.append("( --. )")
    elif item == "Д":        morse.append("( -.. )")
    elif item == "Е":        morse.append("( . )")
    elif item == "Ж":        morse.append("( ...- )")
    elif item == "З":        morse.append("( --.. )")
    elif item == "И":        morse.append("( .. )")
    elif item == "Й":        morse.append("( .--- )")
    elif item == "К":        morse.append("( -.- )")
    elif item == "Л":        morse.append("( .-.. )")
    elif item == "М":        morse.append("( -- )")
    elif item == "Н":        morse.append("( -. )")
    elif item == "О":        morse.append("( --- )")
    elif item == "П":        morse.append("( .--. )")
    elif item == "Р":        morse.append("( .-. )")
    elif item == "С":        morse.append("( ... )")
    elif item == "Т":        morse.append("( - )")
    elif item == "У":        morse.append("( ..- )")
    elif item == "Ф":        morse.append("( ..-. )")
    elif item == "Х":        morse.append("( .... )")
    elif item == "Ц":        morse.append("( -.-. )")
    elif item == "Ч":        morse.append("( ---. )")
    elif item == "Ш":        morse.append("( ---- )")
    elif item == "Щ":        morse.append("( --.- )")
    elif item == "Ъ":        morse.append("( .--.-. )")
    elif item == "Ы":        morse.append("( -.-- )")
    elif item == "Ь":        morse.append("( -..- )")
    elif item == "Э":        morse.append("( ..-.. )")
    elif item == "Ю":        morse.append("( ..-- )")
    elif item == "Я":        morse.append("( .-.- )")

morse=[''.join(morse)]
print(message, " - ", morse)