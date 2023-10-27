import pygame
from pygame.locals import *
from sys import exit
pygame.init()
WIN = pygame.display.set_mode((1600,900))

player = player = pygame.Rect((50,50,50,50))
player_x_vel = 0
player_y_vel = 0
clock = pygame.time.Clock()
player_speed = 5

while True:
    clock.tick(165)
    WIN.fill((0,0,0))
    player.move_ip(player_x_vel, player_y_vel)
    key = pygame.key.get_pressed()
    #left/right
    if key[pygame.K_a] == True and player_x_vel>=-player_speed:
        if player_x_vel >= 0:
            player_x_vel -= player_x_vel
        player_x_vel += -0.1
    if key[pygame.K_d] == True and player_x_vel<=player_speed:
        if player_x_vel <= 0:
            player_x_vel -= player_x_vel
        player_x_vel += 0.1
    
    if key[pygame.K_w] == True and player_y_vel>=-player_speed:
        if player_y_vel >= 0:
            player_y_vel -= player_y_vel
        player_y_vel += -0.1
    if key[pygame.K_s] == True and player_y_vel<=player_speed:
        if player_y_vel <= 0:
            player_y_vel -= player_y_vel
        player_y_vel += 0.1
    
    if key[pygame.K_a] == False and key[pygame.K_d] == False:
        if player_x_vel != 0:
            player_x_vel -= player_x_vel
    if key[pygame.K_w] == False and key[pygame.K_s] == False:
        if player_y_vel != 0:
            player_y_vel -= player_y_vel
    pygame.draw.rect(WIN,(255,255,255),player)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    
    pygame.display.update()
