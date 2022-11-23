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
        elif self.rotate_right:
            self.rotation -= ROTATION_SPEED

    def draw(self, screen):
        radian_conversion = self.rotation * (math.pi / 180)  # convert theta to radian, math.sin takes radianst
        x = self.position[0] + (self.hypotenuse * (math.cos(radian_conversion)))  # calculate math.cos and add it to x_pos
        y = self.position[1] - (self.hypotenuse * (math.sin(radian_conversion)))  # calculate math.sin and add it to y_pos
        pygame.draw.line(screen, (250,250,250),self.position,(x, y),5)


