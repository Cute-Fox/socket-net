import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('188.126.56.144', 9999))

client = []
print('Сеовер запущен')

while True:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres)  # Если такого клиента нету , то добавить
    for clients in client:
            if clients == addres:
                continue  # Не отправлять данные клиенту, который их прислал
            sock.sendto(data, clients)
