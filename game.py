import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((400, 400)) #created surface
screen_rect = screen.get_rect() #get rect attributes of screen

screen.fill((0,0,0)) #paint the surface background

tank = pygame.image.load('images/tank.png') #load image
tank_rect = tank.get_rect() #get rect attributes of tank
tank_rect.midbottom = screen_rect.midbottom

screen.blit(tank,tank_rect)


start = tank_rect.midtop #start of the line
end = (start[0],start[1]-20) #end of line
turret = pygame.draw.line(screen, (250,250,250),start,end,5)

hypotenuse = start[1] - end[1]
degree = 130
radian_conversion = degree * (math.pi/180)
new_end_x = end[0] + (hypotenuse*(math.cos(radian_conversion)))
new_end_y = start[1] - (hypotenuse*(math.sin(radian_conversion)))

turret_rotated = pygame.draw.line(screen, (250, 250, 250), start, (new_end_x,new_end_y), 5)

pygame.display.flip()

while True:
    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #if window is closed, game quits
            sys.exit()
