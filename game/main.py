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
    particles = []

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
        particles.append([[player.x+player.width/2,player.y+player.width-player.width/5], [random.randint(-2,2)/10, random.randint(-2,2)/10], random.randint(3,6)])
        key = pygame.key.get_pressed()
        #left/right
        if key[pygame.K_a] == True and player_x_vel>=-3:
            if player_x_vel >= 0:
                player_x_vel -= player_x_vel
            player_x_vel += -0.25
        if key[pygame.K_d] == True and player_x_vel<=3:
            if player_x_vel <= 0:
                player_x_vel -= player_x_vel
            player_x_vel += 0.25
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            if player_x_vel != 0:
                player_x_vel -= player_x_vel
        
        #jump
        if collide() == True:
                player_jump = False
                player_y_vel = 0

        if player_jump == True:
            if collide() == False:
                if player_y_vel <5:
                    player_y_vel += 0.15

        if collide() == False and player_jump == False:
            if player_y_vel <5:
                player_y_vel += 0.15

        if key[pygame.K_SPACE] == True:
            if player_jump == False:
                if collide() == True:
                    player_y_vel = -7
                    player_jump = True

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(screen, ('white'), particle[0], particle[2]*1.5)
            if particle[2] <= 0:
                particles.remove(particle)

        player.move_ip(player_x_vel, player_y_vel)

        pygame.draw.rect(screen, (255,255,255), player)
        for e in platforms:
            print(e['color'])
            pygame.draw.rect(screen, e['color'], pygame.Rect((int(e['x']), int(e['y']), int(e['w']), int(e['h']))))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    pygame.quit()
    

if __name__ == "__main__":
    main()