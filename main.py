import pygame
import ctypes
import random
import os
from player_1 import Player_1
from player_2 import Player_2

FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


# 初始化
pygame.init()
pygame.mixer.init()
ctypes.windll.user32.SetProcessDPIAware()
screen_width = 1920
screen_high = 1080
screen = pygame.display.set_mode((screen_width, screen_high))
pygame.display.set_caption("電研成發第二組")
score = 69
HP1 = 100
HP2 = 100


clock = pygame.time.Clock()

#載入圖片
background_img_0 = pygame.image.load(os.path.join("img","background_mountain.png")).convert()
background_img_1 = pygame.image.load(os.path.join("img","background_SAO.jpg")).convert()
background_img_2 = pygame.image.load(os.path.join("img","background_tcfsh.jpg")).convert()
background_img_3 = pygame.image.load(os.path.join("img","background_night.jpg")).convert()
background_img_4 = pygame.image.load(os.path.join("img","background_umamusume_fullsize.jpg")).convert()

#載入音樂
pygame.mixer.music.load(os.path.join("sound","background.ogg"))
#pygame.mixer.music.load(os.path.join("sound","14620.mp3"))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)


#繪圖
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#初始
def draw_start():
    screen.blit(background_img_4, (0,0))
    draw_text(screen, 'SAO 格鬥遊戲', 70, screen_width/2, screen_high/4)
    draw_text(screen, '按任意鍵start!', 20, screen_width/2, screen_high*3/4)
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

#血條玩家一(做完生命值和碰撞後再放入變數)
def draw_blood(surf, HP1, x, y):
    if HP1 < 0:
        HP1 = 0
    line_LENGTH = 100
    line_HEIGHT = 10
    fill = (HP1/100)*line_LENGTH
    outline_rect = pygame.Rect(x, y, line_LENGTH, line_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, line_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#血條玩家二(做完生命值和碰撞後再放入變數)
def draw_blood(surf, HP2, x, y):
    if HP2 < 0:
        HP2 = 0
    line_LENGTH = 300
    line_HEIGHT = 10
    fill = (HP2/100)*line_LENGTH
    outline_rect = pygame.Rect(x, y, line_LENGTH, line_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, line_HEIGHT)
    pygame.draw.rect(surf, GREEN, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

#分數玩家一(有變數再加入)
font_name = pygame.font.match_font('arial')
def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.top = y
    surf.blit(text_surface, text_rect)

#分數玩家一(有變數再加入)
font_name = pygame.font.match_font('arial')
def draw_score(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
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


#遊戲迴圈
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
    #
    all_sprites.update()
    
    #畫面顯示
    screen.fill((135, 206, 235))
    screen.blit(background_img_1 , (0,0))
    all_sprites.draw(screen)
    draw_score(screen, str(score), 100, screen_width/3, 10)
    draw_blood(screen, 100, 5, 15)
    pygame.display.update()
    
    #test

pygame.quit()
