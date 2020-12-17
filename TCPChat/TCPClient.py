# AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

from Model.SocketTCP import TCPClient

clientTCP = TCPClient()
clientTCP.createSocketTCP()

while True:
    strMESSAGE = input()

    # Way to finish the chat
    if strMESSAGE == "exit":
        break

    clientTCP.sendMessageTCP(strMESSAGE)

    data = clientTCP.receiveMessageTCP()
    print("Server response:", data)

clientTCP.closeSocketTCP()
