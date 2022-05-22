import pygame
import ctypes
FPS = 60

#初始化
pygame.init()
ctypes.windll.user32.SetProcessDPIAware()
screen = pygame.display.set_mode((1920,1080))
pygame.display.set_caption("電研成發第二組")

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

running =True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135,206,235))
    all_sprites.draw(screen)
    pygame.display.update()


pygame.quit()
