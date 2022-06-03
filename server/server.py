import socket
import threading

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
            break
        elif player_1_address != address:
            player_2_address = address
    else:
        player_1_address = address

working = False

def response(self):
    while working == False:
        s.sendto("connected".encode(), player_1_address)
        s.sendto("connected".encode(), player_2_address)

#多執行序
t = threading.Thread(target=response, args=('Nash',))
t.start() # 開始

#server邏輯
while True:
    indata, address = s.recvfrom(1024)
    data = indata.decode()
    if address == player_1_address:
        s.sendto(indata, player_2_address)
    elif address == player_2_address:
        s.sendto(indata, player_1_address)
    else:
        print("error")
    working = True