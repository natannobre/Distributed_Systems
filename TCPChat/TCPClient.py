#AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #STREAM = TCP / DATAGRAM = UDP
s.connect((TCP_IP, TCP_PORT))

while True:
    strMESSAGE = input()

    #Way to finish the chat
    if(strMESSAGE == "exit"):
        break

    byteMESSAGE = str.encode(strMESSAGE)

    s.send(byteMESSAGE)
    data = s.recv(BUFFER_SIZE)

    print("Server:", data.decode())

s.close()

