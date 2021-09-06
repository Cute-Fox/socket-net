import threading
import socket

def read_sok():
    while True:
        data = sor.recv(1024)
        print(data.decode('utf-8'))


server = '', 9999

nickname = input("Введите ваш псевдоним ")  # Вводим наш псевдоним
sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sor.bind(('188.126.56.144', 0))  # Задаем сокет как клиент
sor.sendto((nickname +' Connect to server').encode('utf-8'),
           server)  # Уведомляем сервер о подключении
potok = threading.Thread(target=read_sok)
potok.start()
while 1:
    mensahe = input()
    sor.sendto(('['+nickname+']'+mensahe).encode('utf-8'), server)
