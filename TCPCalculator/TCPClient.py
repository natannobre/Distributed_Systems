# AUTHOR: NATAN NOBRE CHAVES - COMPUTER ENGINEER

# MODEL TO REQUEST: 10 + 2
# NUM[SPACE]SYMBOL[SPACE]NUM
#
# NUMBERS ALLOWED: ANY RATIONAL NUMBER
# SYMBOLS ALLOWED: +,-,* AND /

from Model.SocketTCP import TCPClient

strMESSAGE = input()

clientTCP = TCPClient()
clientTCP.createSocketTCP()

clientTCP.sendMessageTCP(strMESSAGE)
data = clientTCP.receiveMessageTCP()

data = '{0:g}'.format(float(data))
print("Result:", data)
