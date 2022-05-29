import pygame

screen_width = 1920
screen_high = 1080

#物理
jump_speed = 85
player_speed = 20
gravity = 5
#test

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

