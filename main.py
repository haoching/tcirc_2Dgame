import pygame
import ctypes
FPS = 60

pygame.init()

ctypes.windll.user32.SetProcessDPIAware()
screen = pygame.display.set_mode((1920,1080))

clock = pygame.time.Clock()


running =True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((135,206,235))
    pygame.display.update()

pygame.quit()
#測試