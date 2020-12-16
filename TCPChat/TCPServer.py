#AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ("Connection address:", addr)

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("Client Message:", data.decode())
    response = input()
    conn.send(str.encode(response))

conn.close()