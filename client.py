import socket

class User:
    def __init__(self, port, name):
        self.serverPort = 9090
        self.port = port
        self.name = name


    def go_to_network(self): # Подключение к серверу
        sock = socket.socket()
        self.sock = sock
        sock.connect(('localhost', self.serverPort))
        print("Соединение с сервером успешно - отправлен ваш порт {}",self.port)
    
    def close_network(self):
        self.sock.close

    def send_message(self):
        getterPort = input("Кому вы хотите отправить сообщение (введите порт получателя) ")
        self.getterPort = getterPort
        self.sock.send(self.port.encode()) # Отправляем свой порт
        self.sock.send(self.getterPort.encode()) # Отправляем порт кому мы отправляем сообщение
        message = input()
        self.message = message
        self.sock.send(message.encode())
        data = self.sock.recv(1024)
        print(data)


print("Приветик, для начала чтобы войти в сеть надо зарегестрироваться")
port = int(input("""Для начала введи порт с которого ты будешь писать
(выбери люое число от 7 000 до 40 000.
И так ваш порт -  """))
name = input("""Введите свое имя в сети.
И так ваше имя -  """)

user = User(port,name)

user.go_to_network()
user.send_message()
user.close_network()



#hello = "Hello, world"
#sock = socket.socket()
#sock.connect(('localhost', 9090))
#sock.send(hello.encode())

#data = sock.recv(1024)
#sock.close()

#print(data)
