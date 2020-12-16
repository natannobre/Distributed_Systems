import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
strMESSAGE = "Hello World!"
byteMESSAGE = str.encode(strMESSAGE)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #STREAM = TCP / DATAGRAM = UDP
s.connect((TCP_IP, TCP_PORT))
s.send(byteMESSAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data:", data.decode())