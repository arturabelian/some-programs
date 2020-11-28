# Шифр Цезаря.

message = input("Enter message for encrypt: ")

encrypted_message = " "

for item in message:
	ord_item = ord(item)
	if ord_item > 109:
		ord_item = ord_item - 13
	else:
		ord_item = ord_item + 13
	chr_item = chr(ord_item)
	encrypted_message = encrypted_message + chr_item

print(encrypted_message)

# artur - neghe