# AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER


from Model.SocketTCP import TCPServer

serverTCP = TCPServer()
serverTCP.createSocketTCP()

while 1:
    data = serverTCP.receiveMessageTCP()
    if not data: break
    print("Client Message:", data)

    response = input()
    serverTCP.sendMessageTCP(response)

serverTCP.closeSocketTCP()
