import pygame
import ctypes

FPS = 60

# 初始化
pygame.init()
ctypes.windll.user32.SetProcessDPIAware()
screen_width = 1920
screen_high = 1080
screen = pygame.display.set_mode((screen_width, screen_high))
pygame.display.set_caption("電研成發第二組")

clock = pygame.time.Clock()



player_1_speed_y=0
player_1_high = 100
player_1_width = 100
jumping=False
class Player_1(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((player_1_width, player_1_high))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x=screen_width/2
        self.rect.y=screen_high-player_1_high

    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_a]:
            self.rect.x -= 10
        if key_pressed[pygame.K_d]:
            self.rect.x += 10
        if key_pressed[pygame.K_w]:
            jumping=True
            


all_sprites = pygame.sprite.Group()
player_1 = Player_1()
all_sprites.add(player_1)

running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False
    #

    all_sprites.update()
    #
    screen.fill((135, 206, 235))
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()