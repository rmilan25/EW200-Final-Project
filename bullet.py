import pygame
import math
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.color = (250,250,250)

        self.rect = pygame.Rect(0,0,5,10)
        self.rect.midtop = game.turret.end_pos

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

        self.angle = game.turret.radian_conversion

    def update(self):
        self.y -= 10*math.sin(self.angle)
        self.x += 10*math.cos(self.angle)
        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self, ):
        pygame.draw.rect(self.screen, self.color,self.rect)
