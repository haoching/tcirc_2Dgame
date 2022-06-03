# import imp
# import pygame
# import ctypes
# import math
# import os
# import socket

# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLACK = (0, 0, 0)


# screen_width = 1920
# screen_high = 1080
# pygame.init()
# pygame.mixer.init()
# screen = pygame.display.set_mode((screen_width, screen_high))

# #socket
# HOST = '127.0.0.1'
# PORT = 7000
# server_addr = (HOST, PORT)
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# #物理
# jump_speed = 85
# player_speed = 20
# gravity = 5

# #血條玩家二(做完生命值和碰撞後再放入變數)
# def draw_blood(surf,HP2, x, y):
#     if HP2 < 0:
#         HP2 = 0
#     line_LENGTH = 300
#     line_HEIGHT = 20
#     fill = (HP2/100)*line_LENGTH
#     outline_rect = pygame.Rect(x, y, line_LENGTH, line_HEIGHT)
#     fill_rect = pygame.Rect(x, y, fill, line_HEIGHT)
#     pygame.draw.rect(surf, RED, fill_rect)
#     pygame.draw.rect(surf, WHITE, outline_rect, 2)


# #分數玩家二(有變數再加入)
# font_name = pygame.font.match_font('arial')
# def draw_score2(surf, text, size, x, y):
#     font = pygame.font.Font(font_name, size)
#     text_surface = font.render(text, True, GREEN)
#     text_rect = text_surface.get_rect()
#     text_rect.centerx = x
#     text_rect.top = y
#     surf.blit(text_surface, text_rect)    



# #玩家2運動
# player_2_high = 200
# player_2_width = 100
# player_2_speed_y=jump_speed
# player_2_jumping=False
# class Player_2(pygame.sprite.Sprite):
#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.Surface((player_2_width, player_2_high))
#         self.image.fill((0, 0, 0))
#         self.rect = self.image.get_rect()
#         self.rect.x=screen_width/3*2
#         self.rect.y=screen_high-player_2_high
#         self.score2 = 0
#         self.health = 100

#     def update(self):
#         global player_2_speed_y
#         global player_2_jumping
#         key_pressed = pygame.key.get_pressed()
#         if key_pressed[pygame.K_j]:
#             self.rect.x -= player_speed
#         if key_pressed[pygame.K_l]:
#             self.rect.x += player_speed
#         if key_pressed[pygame.K_i]:
#             player_2_jumping=True
#         if key_pressed[pygame.K_u]:
#             self.health -= 1 
#             self.score2 += 5   
#         if player_2_jumping:
#             self.rect.y-=player_2_speed_y
#             player_2_speed_y-=gravity
#         if self.rect.y>=screen_high-player_2_high:
#             player_2_jumping = False
#             player_2_speed_y = jump_speed
#         #邊界判斷
#         if self.rect.x >= screen_width-player_2_width:
#             self.rect.x = screen_width-player_2_width
#         if self.rect.x <= 0:
#             self.rect.x = 0

# player_2 = Player_2()


# running = True
# show_init = True
# while running:
# #     clock.tick(FPS)
# #     if show_init:
# #         draw_start()
# #         show_init = False
# #     for event in pygame.event.get():
# #         if event.type == pygame.QUIT:
# #             running = False
# #         if pygame.key.get_pressed()[pygame.K_ESCAPE]:
# #             running = False
# #     #
# #     player1 = Player_1()
# #HP1 = player_1.health
#     HP2 = player_2.health
# #score1 = player_1.score1
#     score2 = player_2.score2
# #all_sprites.update()
    
#     #畫面顯示
#     draw_score2(screen, str(score2), 100, screen_width/1.5, 40)
#     draw_blood(screen, HP2, 5, 15)
#     pygame.display.update()
    
# pygame.quit()