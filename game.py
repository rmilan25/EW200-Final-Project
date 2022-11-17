import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400)) #created surface
screen_rect = screen.get_rect() #get rect attributes of screen

screen.fill((0,0,0)) #paint the surface background

tank = pygame.image.load('images/tank.png') #load image
tank_rect = tank.get_rect() #get rect attributes of tank
tank_rect.midbottom = screen_rect.midbottom

screen.blit(tank,tank_rect)


start = tank_rect.midtop #start of the line
turret = pygame.draw.line(screen, (250,250,250),start,(200,330),5)


pygame.display.flip()

while True:
    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #if window is closed, game quits
            sys.exit()
