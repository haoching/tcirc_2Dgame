from asyncio.windows_events import NULL
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

'''
player_1_x = 1920 / 3
player_1_y = 1080 - 200
player_2_x = 1920 / 3 * 2
player_2_y = 1080 - 200
player_1_r = "r"
player_2_r = "r"
player_1_hp = 100
player_2_hp = 100
'''

class player():
    address = 0
    x = 1920/3
    y = 1080 - 200
    r = "r"
    hp = 100
    score = 0

player_1 = player()
player_2 = player()

while True:
    indata, address = s.recvfrom(1024)
    data = indata.decode()
    if player_1.address:
        if player_2.address:
            print(str(player_1.address)+str(player_2.address))
            break
        elif player_1.address != address:
            player_2.address = address
    else:
        player_1.address = address

working = False

def response(self):
    while working == False:
        s.sendto("connected".encode(), player_1.address)
        s.sendto("connected".encode(), player_2.address)

#多執行序
t = threading.Thread(target=response, args=('Nash',))
t.start() # 開始

#server邏輯
while True:
    indata, address = s.recvfrom(1024)
    data = indata.decode()
    if str(data[0:1]) == "l":
        if address == player_1.address:
            player_1.x=int(data[1:5])
            player_1.y=int(data[5:9])
            data+=str(player_2.hp).zfill(3)
            data+=str(player_1.hp).zfill(3)
            data+=str(player_2.score).zfill(2)
            data+=str(player_1.score).zfill(2)
            s.sendto(data.encode(), player_2.address)
        elif address == player_2.address:
            player_2.x=int(data[1:5])
            player_2.y=int(data[5:9])
            data+=str(player_1.hp).zfill(3)
            data+=str(player_2.hp).zfill(3)
            data+=str(player_1.score).zfill(2)
            data+=str(player_2.score).zfill(2)
            s.sendto(data.encode(), player_1.address)
        else:
            print("error")
    if str(data[0:1]) == "a":
        if address == player_1.address:
            if abs(player_1.x-(1920-player_2.x-200))**2 + abs(player_1.y-player_2.y)**2 <= 10000:
                player_2.hp -= 10
            player_1.x=int(data[1:5])
            player_1.y=int(data[5:9])
            data+=str(player_2.hp).zfill(3)
            data+=str(player_1.hp).zfill(3)
            data+=str(player_2.score).zfill(2)
            data+=str(player_1.score).zfill(2)
            s.sendto(data.encode(), player_2.address)
        elif address == player_2.address:
            if abs(player_1.x-(1920-player_2.x-200))**2 + abs(player_1.y-player_2.y)**2 <= 10000:
                player_1.hp -= 10
            player_2.x=int(data[1:5])
            player_2.y=int(data[5:9])
            data+=str(player_1.hp).zfill(3)
            data+=str(player_2.hp).zfill(3)
            data+=str(player_1.score).zfill(2)
            data+=str(player_2.score).zfill(2)
            s.sendto(data.encode(), player_1.address)
        else:
            print("error")
    if player_1.hp <= 0:
        data = "w"
        s.sendto(data.encode(), player_2.address)
        data = "d"
        s.sendto(data.encode(), player_1.address)
    if player_2.hp <= 0:
        data = "w"
        s.sendto(data.encode(), player_1.address)
        data = "d"
        s.sendto(data.encode(), player_2.address)
    working = True