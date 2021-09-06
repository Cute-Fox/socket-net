# Импорт модулей
import socket
import random
import os


class Client():
    def __init__(self,port,name):
        self.port = port
        self.name = name

    def input_messaage(messageText,getterPort,self):
        getterPort = conn.recv(1024)
        while True:
            messageText = conn.recv(1024)
            if not messageText:
                break
            messageText.decode()
            


# Создаем сокет
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)

conn, addr = sock.accept()
print ('connected:', addr)


port = conn.recv(1024)
print("Подключен пользователь с портом ", port)
int(port)

while True:
    data = conn.recv(1024)
    if not data:
        break
    data.decode()
    conn.send(data.upper())

conn.close()
