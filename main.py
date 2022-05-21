import pygame
import ctypes
FPS = 60

pygame.init()

ctypes.windll.user32.SetProcessDPIAware()
pygame.display.set_mode((1920,1080))

clock = pygame.time.Clock()


running =True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#git 測試2

pygame.quit()
