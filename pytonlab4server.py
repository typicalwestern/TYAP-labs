import socket

socks = socket.socket() #создание пременной типа сокет
socks.bind(('', 9090)) #занимает определённый адрес и порт 9090
socks.listen(1) #сколько подключений может быть одновременно
rez = 'Поступившего сообщения не было'
vir1 = ' '
conn, addr = socks.accept() #создает подключение и называет conn, localhost - addr

print('connected:', addr)

while True:
    conn.send(rez.encode())
    vir1 = conn.recv(1024).decode()
    if not vir1:
        break
    rez = vir1