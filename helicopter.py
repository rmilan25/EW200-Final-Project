import pygame
from pygame.sprite import Sprite

class Helicopter(Sprite):
    def __init__(self, game, position):
        super(). __init__()
        self.image = pygame.image.load('images/helicopter.png') #load image
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.left = self.position
        self.screen = game.screen
    def draw(self):
        self.screen.blit(self.image,self.rect)
    def fly(self):
        self.rect.x -= 5
