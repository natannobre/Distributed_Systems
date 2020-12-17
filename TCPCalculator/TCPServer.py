# AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

from Model.SocketTCP import TCPServer
from Model.Methods import Calculator

serverTCP = TCPServer()
serverTCP.createSocketTCP()

data = serverTCP.receiveMessageTCP()
list_Data = data.split(' ')
op = list_Data[1]

result = Calculator(list_Data[0], op, list_Data[2])
serverTCP.sendMessageTCP(str(result))
