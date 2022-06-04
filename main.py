import pygame
import ctypes
import math
import os
import socket
import threading

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

#socket
HOST = '127.0.0.1'
PORT = 48763
server_addr = (HOST, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("connect".encode(), server_addr)


# 初始化
pygame.init()
pygame.mixer.init()
ctypes.windll.user32.SetProcessDPIAware()
screen_width = 1920
screen_high = 1080
screen = pygame.display.set_mode((screen_width, screen_high))
pygame.display.set_caption("電研成發第二組")



clock = pygame.time.Clock()

#載入圖片
background_img_0 = pygame.image.load(os.path.join("img","background_mountain.png")).convert()
background_img_1 = pygame.image.load(os.path.join("img","background_SAO.jpg")).convert()
background_img_2 = pygame.image.load(os.path.join("img","background_tcfsh.jpg")).convert()
background_img_3 = pygame.image.load(os.path.join("img","background_night.jpg")).convert()
background_img_4 = pygame.image.load(os.path.join("img","background_umamusume_fullsize.jpg")).convert()



#載入音樂
pygame.mixer.music.load(os.path.join("sound","1234.mp3"))
#Sound = pygame.mixer.music.load(os.path.join("sound","12345.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#繪圖
font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, RED)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#初始
def draw_start():
    screen.blit(background_img_3, (0,0))
    draw_text(screen, 'tcirc online', 200,  screen_width/2, screen_high/4)
    draw_text(screen, 'click to start!', 80, screen_width/2, screen_high*3/4)
    pygame.display.update()
    
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                waiting = False
                return False

screen.blit(background_img_3, (0,0))
draw_text(screen, 'tcirc online', 200,  screen_width/2, screen_high/4)
pygame.display.update()

#物理
jump_speed = 85
player_speed = 20
gravity = 5


#角色圖片
player_1_img = pygame.image.load(os.path.join("img","principal.png")).convert()
player_2_img = pygame.image.load(os.path.join("img","giphy.gif")).convert()

#玩家1
player_1_high = 300
player_1_width = 200

class Player_1(pygame.sprite.Sprite):
    attackcd = 0
    jumping = False
    y_speed = jump_speed
    rotation = "r"
    attack = False
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.score = 0
        self.image = pygame.transform.scale(player_1_img, (player_1_width, player_1_high))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width / 3 - player_1_width
        self.rect.y = screen_high - player_1_high
    def update(self):
        self.attackcd += 1
        self.attackcd %= 30
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            self.rect.x -= player_speed
            self.image = pygame.transform.flip(pygame.transform.scale(player_1_img, (player_1_width, player_1_high)), True, False)
            self.image.set_colorkey(BLACK)
            self.rotation = "l"
        if key_pressed[pygame.K_d]:
            self.rect.x += player_speed
            self.image = pygame.transform.flip(pygame.transform.scale(player_1_img, (player_1_width, player_1_high)), False, False)
            self.image.set_colorkey(BLACK)
            self.rotation = "r"
        if key_pressed[pygame.K_SPACE]:
            self.jumping = True
        if key_pressed[pygame.K_e] and self.attackcd <= 5:
            self.attack = True
        if self.jumping:
            self.rect.y -= self.y_speed
            self.y_speed -= gravity
        if self.rect.y >= screen_high-player_1_high:
            self.jumping = False
            self.y_speed = jump_speed
        #邊界判斷
        if self.rect.x >= screen_width-player_1_width:
            self.rect.x = screen_width-player_1_width
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.attack:
            data = "a"
            self.attack = False
        else:
            data = "l"
        data += str(player_1.rect.x).zfill(4)
        data += str(player_1.rect.y).zfill(4)
        data += self.rotation
        s.sendto(data.encode(), server_addr)
#player2
player_2_high = 200
player_2_width = 100

class Player_2(pygame.sprite.Sprite):
    x = screen_width/3*2
    y=screen_high-player_2_high
    r = "r"
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_2_img, (player_2_width, player_2_high))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=screen_width/3*2
        self.rect.y=screen_high-player_2_high
        self.score = 0
        self.health = 100
    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        if self.r == "r":
            self.image = pygame.transform.scale(player_2_img, (player_2_width, player_2_high))
            self.image.set_colorkey(BLACK)
        elif self.r == "l":
            self.image = pygame.transform.flip(pygame.transform.scale(player_2_img, (player_2_width, player_2_high)), True, False)
            self.image.set_colorkey(BLACK)
        

#血條玩家一(做完生命值和碰撞後再放入變數)
def draw_blood(surf,hp, x, y):
    line_length = 300
    line_height = 20
    fill = (hp/100)*line_length
    outline_rect = pygame.Rect(x, y, line_length, line_height)
    fill_rect = pygame.Rect(x, y, fill, line_height)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#血條玩家二(做完生命值和碰撞後再放入變數)
def draw_blood2(surf, hp, x, y):
    line_length = 300
    line_height = 20
    fill = (hp/100)*line_length
    outline_rect = pygame.Rect(x, y, line_length, line_height)
    fill_rect = pygame.Rect(x, y, fill, line_height)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#分數玩家一(有變數再加入)
def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#分數玩家二(有變數再加入)
def draw_score2(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

all_sprites = pygame.sprite.Group()
player_1 = Player_1()
all_sprites.add(player_1)
player_2 = Player_2()
all_sprites.add(player_2)

running = True
show_init = True

print("game start")

#連線
connectting = False
def connnectserver(self):
    global connectting
    while running:
        indata ,address = s.recvfrom(1024)
        data = indata.decode()
        if str(data[0:4]) == "conn":
            print("connected")
            connectting = True
        elif str(data[0:1]) == "l":
            print(str(data[1:5]),str(data[5:9]))
            player_2.x = 1920-int(data[1:5])-player_1_width
            player_2.y = int(data[5:9])
            player_2.r = str(data[9:10])
            player_1.health = int(data[10:13])
            player_2.health = int(data[13:16])
            player_1.score = int(data[16:18])
            player_2.score = int(data[18:20])
        elif str(data[0:1]) == "w":
            draw_text(screen, 'YOU WIN', 300,  screen_width/2, screen_high/2.5)
        elif str(data[0:1]) == "d":
            draw_text(screen, 'YOU LOSE', 300,  screen_width/2, screen_high/2.5)
            
t = threading.Thread(target = connnectserver, args=('Nash',))
t.start() # 開始
while connectting == False:
    s.sendto("connect".encode(), server_addr)

while running:
    clock.tick(FPS)
    if show_init:
        draw_start()
        show_init = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
    #
    all_sprites.update()
    
    #畫面顯示
    
    screen.blit(background_img_1 , (0,0))
    all_sprites.draw(screen)
    draw_score(screen, str(player_1.score), 100, screen_width/3, 40)
    draw_score2(screen, str(player_2.score), 100, screen_width/1.5, 40)
    draw_blood(screen, player_1.health, 5, 15)
    draw_blood2(screen, player_2.health, 1610, 15)
    pygame.display.update()
    
pygame.quit()
