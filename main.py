import pygame
import ctypes
import random
import os


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
score = 0


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
    line_LENGTH = 100
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
        self.rect.x = screen_width/3-player_1_width#對稱
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


#玩家2運動
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
        self.rect.x=screen_width/3*2
        self.rect.y=screen_high-player_1_high
        self.health = 100

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
    screen.blit(background_img_4 , (0,0))
    all_sprites.draw(screen)
    pygame.display.update()
    draw_score(screen, str(score), 15, screen_width/3, 10)
    #draw_blood(screen, 100, 5, 15)


pygame.quit()
