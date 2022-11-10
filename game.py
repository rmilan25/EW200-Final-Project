import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((400, 400)) #created surface
screen_rect = screen.get_rect() #get rect attributes of screen

screen.fill((0,0,0)) #paint the surface background

turret = pygame.image.load('images/turret.png')
turret_rect = turret.get_rect()
screen.blit(turret, (200-2, 400-40-30))

tank = pygame.image.load('images/tank.png') #load image
tank_rect = tank.get_rect() #get rect attributes of tank
screen.blit(tank,(200-30,400-40))

pygame.display.flip()
while True:
    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #if window is closed, game quits
            sys.exit()
