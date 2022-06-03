import socket
import threading

#socket
HOST = '0.0.0.0'
PORT = 48763
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#UDP
s.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

player_1_address = 0
player_2_address = 0

player_1_x = 1920 / 3
player_1_y = 1080 - 200
player_2_x = 1920 / 3 * 2
player_2_y = 1080 - 200
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
    if str(data[0:1]) == "l":
        if address == player_1_address:
            player_1_x=int(data[1:5])
            player_1_y=int(data[5:9])
            s.sendto(indata, player_2_address)
        elif address == player_2_address:
            player_2_x=int(data[1:5])
            player_2_y=int(data[5:9])
            s.sendto(indata, player_1_address)
        else:
            print("error")
    working = True