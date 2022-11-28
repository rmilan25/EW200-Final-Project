import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.color = (250,250,250)

        self.rect = pygame.Rect(0,0,5,10)
        self.rect.midtop = game.turret.end_pos

        self.y = float(self.rect.y)

    def update(self):
        self.y -= 1.0
        self.rect.y = self.y

    def draw(self, ):
        pygame.draw.rect(self.screen, self.color,self.rect)
