# Самое большое слово в строке.

string_of_text = input('Enter the text: ').split()
count = 0
for item in string_of_text:
    if len(item) > count:
        count = len(item)
        word = item    
print('The longest word is: ', word)

# The longest word is
# The longest word is: longest