import imp
import pygame
import os

screen_width = 800
screen_high = 450
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


#角色圖片
P_1 = pygame.image.load(os.path.join("img","principal.png")).convert()
P_2 = pygame.image.load(os.path.join("img","giphy.gif")).convert()

#物理
jump_speed = 85
player_speed = 20
gravity = 5

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
        self.image = pygame.transform.scale(P_1, (player_1_width, player_1_high))
        self.image.set_colorkey(BLACK)
        #self.image.fill((255, 255, 255))
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
        self.image = pygame.transform.scale(P_2, (player_2_width, player_2_high))
        self.image.set_colorkey(BLACK)
        #self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x=screen_width/3*2
        self.rect.y=screen_high-player_2_high
        self.score2 = 0
        self.health = 100
    def update(self):
        self.rect.x = self.player_2_x
        self.rect.y = self.player_2_y