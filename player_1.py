import pygame
import socket
import math

screen_width = 1920
screen_high = 1080

#socket
HOST = '127.0.0.1'
PORT = 7000
server_addr = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#物理
jump_speed = 85
player_speed = 20
gravity = 5

#玩家1運動
player_1_high = 200
player_1_width = 100
player_1_speed_y=jump_speed
player_1_jumping=False

class Player_1(pygame.sprite.Sprite):
    jumping = False
    player_1_speed_y = 100
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((player_1_width, player_1_high))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = screen_width/3-player_1_width
        self.rect.y = screen_high-player_1_high
        self.health = 100

    def update(self):
        global player_1_speed_y
        global player_1_jumping

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            self.rect.x -= player_speed
        if key_pressed[pygame.K_d]:
            self.rect.x += player_speed
        if key_pressed[pygame.K_w]:
            player_1_jumping = True
        #問題程式碼(待解決)    
        if key_pressed[pygame.K_e]: 
            if ((abs(player_1.rect.x-player_2.rect.x)**2+abs(player_1.rect.y-player_2.rect.y)**2)**0.5) <= 2:
                HP2 -=2
<<<<<<< HEAD
                score1 += 1   
          
=======
                score1 += 1

>>>>>>> a43c7119484cb2fec32e31fff6575da45515e065
        if player_1_jumping:
            self.rect.y-=player_1_speed_y
            player_1_speed_y-=gravity
        if self.rect.y>=screen_high-player_1_high:
            player_1_jumping = False
            player_1_speed_y = jump_speed
        #邊界判斷
        if self.rect.x >= screen_width-player_1_width:
            self.rect.x = screen_width-player_1_width
        if self.rect.x <= 0:
            self.rect.x = 0
        data = ""
        data += str(self.rect.x).zfill(4)
        data += str(self.rect.y).zfill(4)
        data += "f"
        s.sendto(data.encode(), server_addr)
