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

hypotenuse = start[1] - end[1] #fixed length of turret
degree = 90  # initial degree

paratrooper = pygame.image.load('images/person_parachute.png')
paratrooper_rect = paratrooper.get_rect()
screen.blit(paratrooper, (30,50))


while True:
    for event in pygame.event.get(): #listen for events
        if event.type == pygame.QUIT: #if window is closed, game quits
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                degree -= 1
            elif event.key == pygame.K_LEFT:
                degree += 1

    radian_conversion = degree * (math.pi / 180)  # convert theta to radian, math.sin takes radians
    new_end_x = end[0] + (hypotenuse * (math.cos(radian_conversion)))  # calculate math.cos and add it to x_pos
    new_end_y = start[1] - (
                hypotenuse * (math.sin(radian_conversion)))  # calculate math.sin and add it to y_pos

    screen.fill((0,0,0))
    screen.blit(tank, tank_rect)
    pygame.draw.line(screen, (250, 250, 250), start,(new_end_x, new_end_y), 5)  # rotated turret

    pygame.display.flip()


