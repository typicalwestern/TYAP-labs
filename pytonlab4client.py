import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
while True:
    mission = input('Введите строку: ')
    sock.send(mission.encode())
    answer= sock.recv(1024).decode()
    if not answer:
        break
    print('Результат работы сервера: ', answer)
sock.close()
