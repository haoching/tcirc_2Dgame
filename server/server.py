import socket
import time

#socket
HOST = '0.0.0.0'
PORT = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#UDP
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

player_1_address = 0
player_2_address = 0

while True:
    indata, address = s.recvfrom(1024)
    data = indata.decode()
    if player_1_address:
        if player_2_address:
            print(str(player_1_address)+str(player_2_address))
        elif player_1_address != address:
            player_2_address = address
    else:
        player_1_address = address
        
    print('recvfrom ' + str(address) + ': ' + data)