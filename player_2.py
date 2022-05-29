import pygame

screen_width = 1920
screen_high = 1080

#物理
jump_speed = 85
player_speed = 20
gravity = 5

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
        self.rect.y=screen_high-player_2_high

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
                        