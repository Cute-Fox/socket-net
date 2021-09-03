# Импорт модулей
import socket
import random
import os

# Создаем сокет
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()
print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    data.decode()
    conn.send(data.upper())

conn.close()
