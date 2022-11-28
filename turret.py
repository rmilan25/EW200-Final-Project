import pygame
import math
ROTATION_SPEED = 1
class Turret:
    def __init__(self, position):
        self.position = position
        self.rotation = 90
        self.hypotenuse = 20
        self.rotate_left = False
        self.rotate_right = False

    def update(self):
        if self.rotate_left:
            self.rotation += ROTATION_SPEED
            #print(self.rotation)
        elif self.rotate_right:
            self.rotation -= ROTATION_SPEED
            #print(self.rotation)

    def draw(self, screen):
        self.radian_conversion = self.rotation * (math.pi / 180)  # convert theta to radian, math.sin takes radianst
        x = self.position[0] + (self.hypotenuse * (math.cos(self.radian_conversion)))  # calculate math.cos and add it to x_pos
        y = self.position[1] - (self.hypotenuse * (math.sin(self.radian_conversion)))  # calculate math.sin and add it to y_pos
        self.end_pos = (x, y)
        pygame.draw.line(screen, (250,250,250),self.position,(self.end_pos),5)


