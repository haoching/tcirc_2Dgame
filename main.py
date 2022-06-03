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
pygame.mixer.music.load(os.path.join("sound","background.ogg"))
#sound = pygame.mixer.music.load(os.path.join("sound","14620.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#繪圖
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
    draw_text(screen, 'SAO fighting', 200,  screen_width/2, screen_high/4)
    draw_text(screen, 'click to start!', 80, screen_width/2, screen_high*3/4)
    pygame.display.update()
    
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                waiting = False
                return False

#物理
jump_speed = 85
player_speed = 20
gravity = 5


#角色圖片
player_1_img = pygame.image.load(os.path.join("img","principal.png")).convert()
player_2_img = pygame.image.load(os.path.join("img","giphy.gif")).convert()

#玩家1運動
player_1_high = 300
player_1_width = 200
player_1_speed_y=jump_speed
player_1_jumping=False

class Player_1(pygame.sprite.Sprite):
    jumping = False
    player_1_speed_y = 100
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.health = 100
        self.score1 = 0
        self.image = pygame.transform.scale(player_1_img, (player_1_width, player_1_high))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width/3-player_1_width
        self.rect.y = screen_high-player_1_high
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
        if key_pressed[pygame.K_e]:
            self.health -= 1
            self.score1 += 2
                
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
#player2
player_2_high = 200
player_2_width = 100

class Player_2(pygame.sprite.Sprite):
    player_2_x = screen_width/3*2
    player_2_y=screen_high-player_2_high
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_2_img, (player_2_width, player_2_high))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x=screen_width/3*2
        self.rect.y=screen_high-player_2_high
        self.score2 = 0
        self.health = 100
    def update(self):
        self.rect.x = self.player_2_x
        self.rect.y = self.player_2_y


#血條玩家一(做完生命值和碰撞後再放入變數)
def draw_blood(surf,HP2, x, y):
    if HP2 < 0:
        HP2 = 0
        draw_text(screen, 'SAO WIN', 300,  screen_width/2, screen_high/2.5)
    line_LENGTH = 300
    line_HEIGHT = 20
    fill = (HP2/100)*line_LENGTH
    outline_rect = pygame.Rect(x, y, line_LENGTH, line_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, line_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#血條玩家二(做完生命值和碰撞後再放入變數)
def draw_blood2(surf, HP1, x, y):
    if HP1 < 0:
        HP1 = 0
        draw_text(screen, 'PRINCIPAL WIN', 300,  screen_width/2, screen_high/2.5)
    line_LENGTH = 300
    line_HEIGHT = 20
    fill = (HP1/100)*line_LENGTH
    outline_rect = pygame.Rect(x, y, line_LENGTH, line_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, line_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#分數玩家一(有變數再加入)
font_name = pygame.font.match_font('arial')
def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, GREEN)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#分數玩家二(有變數再加入)
font_name = pygame.font.match_font('arial')
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
        else:
            print(str(data[0:4]),str(data[4:8]))
            player_2.player_2_x=int(data[0:4])
            player_2.player_2_y=int(data[4:8])
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
    p1data = ""
    p1data += str(player_1.rect.x).zfill(4)
    p1data += str(player_1.rect.y).zfill(4)
    p1data += "f"
    s.sendto(p1data.encode(), server_addr)
    #
    HP1 = player_1.health
    HP2 = player_2.health
    score1 = player_1.score1
    score2 = player_2.score2
    all_sprites.update()
    
    #畫面顯示
    
    screen.blit(background_img_1 , (0,0))
    all_sprites.draw(screen)
    draw_score(screen, str(score1), 100, screen_width/3, 40)
    draw_score2(screen, str(score2), 100, screen_width/1.5, 40)
    draw_blood(screen, HP2, 5, 15)
    draw_blood2(screen, HP1, 1610, 15)
    pygame.display.update()
    
pygame.quit()
