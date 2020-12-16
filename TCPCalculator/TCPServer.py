#AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ("Connection address:", addr)
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break

    list_Data = data.split(str.encode(' '))
    op = list_Data[1].decode()
    result = float(0)

    # Calculator
    if op is '+':
        result = float(list_Data[0]) + float(list_Data[2])

    elif op == '-':
        result = float(list_Data[0]) - float(list_Data[2])

    elif op == '*':
        result = float(list_Data[0]) * float(list_Data[2])

    elif op == '/':
        result = float(list_Data[0]) / float(list_Data[2])

    result = str.encode(str(result))
    conn.send(result)
conn.close()