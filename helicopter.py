import pygame
from pygame.sprite import Sprite

class Helicopter(Sprite):
    def __init__(self, game):
        super(). __init__()
        self.image = pygame.image.load('images/helicopter.png') #load image
        self.rect = self.image.get_rect()
        self.screen = game.screen
    def draw(self):#Do I need this for sprite?
        self.screen.blit(self.image,self.rect)
    def move(self):
        self.rect.x -= 1
