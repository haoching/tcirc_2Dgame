import socket
import time

#socket
HOST = '0.0.0.0'
PORT = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#UDP
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    indata, address = s.recvfrom(1024)
    data = indata.decode()

    print('recvfrom ' + str(address) + ': ' + data)