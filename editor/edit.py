import pygame, random
from pygame.locals import *
from sys import exit
pygame.init()
import json
import time

def main():
    screen_w = 1920
    screen_h = 1025
    
    player_x_vel = 0
    player_y_vel = 0
    player_jump = False

    screen = pygame.display.set_mode((screen_w,screen_h))

    player = pygame.Rect((screen_w/2,screen_h/2,50,50))
    clock = pygame.time.Clock()
    
    platforms = []

    f = open("game\lvl.json")
    data= json.load(f)
    for i in data['lvl']:
        platforms.append(i)

    def collide():
        c = False
        for i in platforms:
            if player.colliderect(int(i['x']),int(i['y']),int(i['w']),int(i['h'])):
                c = True

        return c
    
    run = True
    while run:
        clock.tick(165)
        screen.fill((0,0,0))

        #movement
        key = pygame.key.get_pressed()
        #left/right
        if key[pygame.K_a] == True and player_x_vel>=-3:
            player_x_vel += -0.1
        if key[pygame.K_d] == True and player_x_vel<=3:
            player_x_vel += 0.1
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            if player_x_vel >= 0:
                player_x_vel += -0.04
            else:
                player_x_vel += 0.04
        #jump and collide
        if key[pygame.K_SPACE] == True:
            if player_jump == False:
                player_y_vel = -7
                player.move_ip(0, player_y_vel)
                player_jump = True
        if player.y > screen_h - player_y_vel - player.size[0]:
            player_y_vel = 0
            player_jump = False
        if collide() == True:
                player_jump = False
                player_y_vel = 0
        if player_jump == True:
            if player_y_vel <5:
                player_y_vel += 0.15
        if collide() == False and player_jump == False:
            if player_y_vel <5:
                player_y_vel += 0.15
        player.move_ip(player_x_vel, player_y_vel)

        #draw
        pygame.draw.rect(screen, (255,255,255), player)
        for e in platforms:
            pygame.draw.rect(screen, "white", pygame.Rect((int(e['x']), int(e['y']), int(e['w']), int(e['h']))))
            
        #quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    pygame.quit()
    

if __name__ == "__main__":
    main()