#AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEERING

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
strMESSAGE = "Hello World!"
byteMESSAGE = str.encode(strMESSAGE)

print("UDP target IP: ", UDP_IP)
print("UDP target port: ", UDP_PORT)
print("message: ", strMESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(byteMESSAGE, (UDP_IP, UDP_PORT))