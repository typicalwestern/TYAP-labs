import socket

socks = socket.socket() 
socks.bind(('', 9090)) 
socks.listen(1) 
rez = 'Поступившего сообщения не было'
vir1 = ' '
conn, addr = socks.accept() 

print('connected:', addr)

while True:
    conn.send(rez.encode())
    vir1 = conn.recv(1024).decode()
    if not vir1:
        break
    rez = vir1
