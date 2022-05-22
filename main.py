from re import T
import pygame
import ctypes
import random
import os

FPS = 60

# 初始化
pygame.init()
ctypes.windll.user32.SetProcessDPIAware()
screen_width = 1920
screen_high = 1080
screen = pygame.display.set_mode((screen_width, screen_high))
pygame.display.set_caption("電研成發第二組")

clock = pygame.time.Clock()

#物理
jump_speed = 80
player_speed = 15
gravity = 5

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
        self.rect.x = screen_width/3
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



player_2_high = 200
player_2_width = 100

player_2_speed_y=jump_speed
player_2_jumping=False
class Player_2(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((player_2_width, player_2_high))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x=screen_width
        self.rect.y=screen_high-player_1_high

    def update(self):
        global player_2_speed_y
        global player_2_jumping
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_j]:
            self.rect.x -= player_speed
        if key_pressed[pygame.K_l]:
            self.rect.x += player_speed
        if key_pressed[pygame.K_i]:
            player_2_jumping=True
        if player_2_jumping:
            self.rect.y-=player_2_speed_y
            player_2_speed_y-=gravity
        if self.rect.y>=screen_high-player_2_high:
            player_2_jumping = False
            player_2_speed_y = jump_speed
        #邊界判斷
        if self.rect.x >= screen_width-player_2_width:
            self.rect.x = screen_width-player_2_width
        if self.rect.x <= 0:
            self.rect.x = 0     
                        

all_sprites = pygame.sprite.Group()
player_1 = Player_1()
all_sprites.add(player_1)
player_2 = Player_2()
all_sprites.add(player_2)

running = True


while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
    #
    if pygame.key.get_pressed()[pygame.K_w]:
        player_1.jumping = True
    all_sprites.update()
    #
    
    
    screen.fill((135, 206, 235))
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()

