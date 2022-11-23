import pygame
import sys
from turret import Turret

pygame.init()
screen = pygame.display.set_mode((400, 400)) #created surface
screen_rect = screen.get_rect() #get rect attributes of screen

screen.fill((0,0,0)) #paint the surface background

tank = pygame.image.load('images/tank.png') #load image
tank_rect = tank.get_rect() #get rect attributes of tank
tank_rect.midbottom = screen_rect.midbottom

screen.blit(tank,tank_rect)


turret = Turret(tank_rect.midtop)

paratrooper = pygame.image.load('images/person_parachute.png')
paratrooper_rect = paratrooper.get_rect()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #if window is closed, game quits
            sys.exit()
        elif event.type == pygame.KEYDOWN: #listen to keydown events
            if event.key == pygame.K_RIGHT:
                turret.rotate_right = True
            elif event.key == pygame.K_LEFT:
                turret.rotate_left = True
        elif event.type == pygame.KEYUP: #listen to keyup events
            if event.key == pygame.K_RIGHT:
                turret.rotate_right = False
            elif event.key == pygame.K_LEFT:
                turret.rotate_left = False



    screen.fill((0,0,0))
    screen.blit(tank, tank_rect)
    screen.blit(paratrooper, (30, 50))
    turret.update()
    turret.draw(screen)

    pygame.display.flip()
    clock.tick(60)


