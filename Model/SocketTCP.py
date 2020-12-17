# AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

import socket


class TCPClient:
    def __init__(self, TCP_IP='127.0.0.1', TCP_PORT=5005, BUFFER_SIZE=1024):
        self.BUFFER_SIZE = BUFFER_SIZE
        self.TCP_PORT = TCP_PORT
        self.TCP_IP = TCP_IP

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def createSocketTCP(self):
        self.s.connect((self.TCP_IP, self.TCP_PORT))

    def sendMessageTCP(self, message=""):
        byteMessage = str.encode(message)
        self.s.send(byteMessage)

    def receiveMessageTCP(self):
        return str(self.s.recv(self.BUFFER_SIZE).decode())

    def closeSocketTCP(self):
        self.s.close()


class TCPServer:
    def __init__(self, TCP_IP='127.0.0.1', TCP_PORT=5005, BUFFER_SIZE=1024):
        self.BUFFER_SIZE = BUFFER_SIZE
        self.TCP_PORT = TCP_PORT
        self.TCP_IP = TCP_IP

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn = None

    def createSocketTCP(self):
        self.s.bind((self.TCP_IP, self.TCP_PORT))
        self.s.listen(1)
        self.conn, address = self.s.accept()
        print("Connection address:", address)

    def sendMessageTCP(self, message=""):
        byteMessage = str.encode(message)
        self.conn.send(byteMessage)

    def receiveMessageTCP(self):
        while True:
            data = self.conn.recv(self.BUFFER_SIZE)
            if not data: break

            data = data.decode()
            return data
        self.closeSocketTCP()
        return None

    def closeSocketTCP(self):
        self.conn.close()
