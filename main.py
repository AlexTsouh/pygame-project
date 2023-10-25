import pygame, random
from pygame.locals import *
from sys import exit
pygame.init()
import json

def main():
    screen_w = 1550
    screen_h = 750
    
    player_x_vel = 0
    player_y_vel = 0
    player_jump = False

    screen = pygame.display.set_mode((screen_w,screen_h))

    player = pygame.Rect((screen_w/2,screen_h/2,50,50))

    lvl = pygame.Rect((screen_w/2,screen_h-100,500,10))
    clock = pygame.time.Clock()
    
    platforms = []
    particles = []

    f = open('lvl.json')
    lvlfile = json.load(f)

    for i in lvlfile['lvl']:
        platforms.append(tuple(i))

    platforms.append((screen_w/2,screen_h-100,500,10))
    run = True
    while run:
        clock.tick(330)
        screen.fill((0,0,0))
        particles.append([[player.x+player.width/2,player.y+player.width-player.width/5], [random.randint(-2,2)/10, random.randint(-2,2)/10], random.randint(3,6)])

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
        #jump
        if key[pygame.K_SPACE] == True:
            if player_jump == False:
                player_y_vel = -7
                player.move_ip(0, player_y_vel)
                player_jump = True

        if player.y > screen_h - player_y_vel - player.size[0]:
            player_y_vel = 0
            player_jump = False
        
        if player.colliderect(lvl) == True:
                player_jump = False
                player_y_vel = 0

        if player_jump == True:
            if player_y_vel <5:
                player_y_vel += 0.15

        if player.colliderect(lvl) == False and player_jump == False:
            if player_y_vel <5:
                player_y_vel += 0.15

        player.move_ip(player_x_vel, player_y_vel)

        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= 0.1
            pygame.draw.circle(screen, ('red'), particle[0], particle[2])
            if particle[2] <= 0:
                particles.remove(particle)

        pygame.draw.rect(screen, (255,255,255), player)
        pygame.draw.rect(screen, (255,255,255), lvl)
        for e in platforms:
            print(e[1])
            # pygame.draw.rect(screen, platforms[e][0], pygame.Rect(platforms[e][1], platforms[e][2], platforms[e][3], platforms[e][4]))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()