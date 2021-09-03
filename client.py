import socket

hello = "Hello, world"
sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(hello.encode())

data = sock.recv(1024)
sock.close()

print(data)
