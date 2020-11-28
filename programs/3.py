# Клиент.

# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:

	a = input('Enter the messge: ')
	sock.send(a.encode())

	data = sock.recv(1024).decode()
	print(data)
sock.close()
